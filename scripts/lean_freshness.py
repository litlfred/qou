#!/usr/bin/env python3
"""lean_freshness.py — the ONE definition of "is this olean current?".

Two tools ask that question and, until 2026-08-26, answered it differently:

* ``scripts/lean_cone_build.py`` (behind ``scripts/lean-direct-cone.sh``) rebuilt
  a module whose olean was older than the source's **mtime**;
* ``scripts/lean-axiom-guard.py`` failed a module whose olean was older than the
  source's **commit time**.

The guard's docstring tells you to compose them::

    scripts/lean-direct-cone.sh $(scripts/lean-axiom-guard.py --print-modules)

and that compose **deadlocked** whenever you built before committing — the
natural order, since you verify and then commit what verified.  Measured
2026-08-26 on this branch: source mtime ``06:45:09``, olean ``06:45:12``, commit
time ``06:47:15``.  The builder saw olean-newer-than-mtime and skipped; the guard
saw olean-older-than-commit and returned rc=2; re-running either changed nothing.
Hit three times in one session (bean ``qou-5v24``).

``-B/--force`` was the first fix and is a workaround: it makes the builder ignore
freshness entirely, so the operator supplies by hand the agreement the tools
should have had.  This module is the actual fix — both import
:func:`effective_source_time`, so the two notions cannot drift apart again.

**Commit time is the right notion, and mtime is the wrong one**, for a reason
that is specific to how this repo's Lean trees come into being.  A clone or
checkout stamps every source with the checkout time, which is later than any
olean restored from a build cache; an mtime comparison therefore reports the
whole cone stale in exactly the environment these tools are built for.  Measured
2026-08-15: mtime flagged 15 modules stale — ``Specht`` source 10:08, olean 03:33
— while ``lake build``, which hashes content, replayed all 3285 jobs as already
up to date.  So adopting the guard's rule does not merely make the builder agree
with the guard; it stops the builder recompiling a correctly-restored cache.

A **dirty** file falls back to mtime: a local edit is precisely the case the
check exists for, and there is no commit to trust.
"""

from __future__ import annotations

import subprocess
from functools import lru_cache
from pathlib import Path

DEFAULT_LEAN_ROOT = Path("folio/quantum-observable-universe/lean")


def dirty_paths(scope: Path | str = DEFAULT_LEAN_ROOT) -> set[str]:
    """Repo-relative paths under `scope` with uncommitted content changes.

    Staged and unstaged both count.  With no git available this returns the empty
    set, which makes every file look clean — see :func:`effective_source_time`,
    where a missing commit time then falls back to mtime anyway.
    """
    try:
        proc = subprocess.run(
            ["git", "status", "--porcelain", "--", str(scope)],
            capture_output=True, text=True, timeout=120,
        )
    except (FileNotFoundError, subprocess.SubprocessError):
        return set()
    out: set[str] = set()
    for line in proc.stdout.splitlines():
        # "XY path" or "XY old -> new"; take the final path.
        path = line[3:].strip()
        if "->" in path:
            path = path.split("->")[-1].strip()
        out.add(path.strip('"'))
    return out


@lru_cache(maxsize=None)
def _commit_time(src_str: str) -> float | None:
    """Unix time of the commit that last touched `src`, or None if unavailable.

    Cached because the cone builder asks once per module and a cone runs to a few
    hundred; one `git log` per module per run is enough.
    """
    try:
        proc = subprocess.run(
            ["git", "log", "-1", "--format=%ct", "--", src_str],
            capture_output=True, text=True, timeout=120,
        )
    except (FileNotFoundError, subprocess.SubprocessError):
        return None
    val = proc.stdout.strip()
    return float(val) if val else None


@lru_cache(maxsize=1)
def _repo_root() -> Path | None:
    """Absolute path of the git worktree root, or None outside a repo."""
    try:
        proc = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, timeout=120,
        )
    except (FileNotFoundError, subprocess.SubprocessError):
        return None
    out = proc.stdout.strip()
    return Path(out) if out else None


def _repo_relative(src: Path) -> str:
    """`src` as `git status --porcelain` would print it.

    Relative to the worktree root, NOT to `Path.cwd()` — these tools are invoked
    from wherever the operator happens to be, and a cwd-relative path silently
    fails to match the dirty set, which makes an edited file read as clean and
    therefore fall through to commit time.  That is the one case the check exists
    for, so getting it wrong here is the failure mode that matters.
    """
    root = _repo_root()
    for base in (root, Path.cwd()):
        if base is None:
            continue
        try:
            return str(src.resolve().relative_to(base.resolve()))
        except ValueError:
            continue
    return str(src)


def effective_source_time(src: Path, dirty: set[str]) -> float:
    """Source timestamp that survives a fresh clone.

    Commit time for a clean file, mtime for a dirty one.  See the module docstring
    for why a plain mtime is wrong in the direction that *disables* the guard and
    *defeats* the restored cache.
    """
    rel = _repo_relative(src)
    if rel not in dirty:
        ct = _commit_time(str(src))
        if ct is not None:
            return ct
    return src.stat().st_mtime


# ---------------------------------------------------------------------------
# Content hashing — the actual answer, added 2026-08-26 after the clock rule
# below was measured serving a stale olean.
# ---------------------------------------------------------------------------

SIDECAR_SUFFIX = ".srcsha"


def source_sha(src: Path) -> str:
    """SHA-256 of the source bytes."""
    import hashlib
    return hashlib.sha256(src.read_bytes()).hexdigest()


def sidecar_path(olean: Path) -> Path:
    """Where the hash of the source this olean was built from is recorded."""
    return olean.with_name(olean.name + SIDECAR_SUFFIX)


def record_source_sha(olean: Path, src: Path) -> None:
    """Stamp `olean` with the hash of the source it was just built from."""
    try:
        sidecar_path(olean).write_text(source_sha(src))
    except OSError:
        pass          # a missing stamp only costs one extra rebuild later


def read_source_sha(olean: Path) -> str | None:
    sc = sidecar_path(olean)
    try:
        return sc.read_text().strip() or None
    except OSError:
        return None


def olean_is_current(src: Path, olean: Path, dirty: set[str], *,
                     conservative: bool) -> bool:
    """Is `olean` a build of the CURRENT contents of `src`?

    **Prefer the hash.** If the olean carries a `.srcsha` stamp, this is decided
    by comparing it to the source's hash and no clock is consulted at all. That
    is exact in both of the directions a timestamp gets wrong, and it is why the
    stamp exists.

    **Neither clock is right on its own, and this was measured, not reasoned.**

    * *mtime* says stale after a clone or cache restore, because checkout stamps
      every source with the checkout time. 2026-08-15: 15 modules flagged stale
      while `lake build`, which hashes, replayed all 3285 jobs as up to date.
    * *commit time* says fresh after merging a branch whose commits are DATED
      EARLIER than your existing oleans -- the content on disk just changed and
      the recorded time went backwards. Measured 2026-08-26 merging 45 commits of
      `main`: `QOU.AlgebraicSubstrate.qou_obstruction_reduction` changed in the
      merge, commit time 07:38:27, local olean 07:40:35. A commit-time rule calls
      that fresh and serves a build of the OLD source.

    So when there is no stamp, the two callers want opposite errors, and
    `conservative` picks which:

    * the **rebuilder** passes ``conservative=True`` -- the olean must beat BOTH
      clocks. It may rebuild something that did not need it; it can never serve a
      stale one, and one rebuild leaves a stamp so the clocks are never consulted
      for that module again.
    * the **guard** passes ``conservative=False`` -- commit time only, so it does
      not refuse to report on a fresh clone.

    That asymmetry is deliberate and is what keeps `qou-5v24` fixed. The deadlock
    was the rebuilder calling FRESH what the guard called STALE; since
    ``max(commit, mtime) >= commit``, the rebuilder's stale set now always
    CONTAINS the guard's, and a rebuild always satisfies the guard. The reverse --
    rebuilding a little more than strictly needed -- costs seconds and terminates.
    """
    if not olean.is_file():
        return False
    recorded = read_source_sha(olean)
    if recorded is not None:
        return recorded == source_sha(src)
    ot = olean.stat().st_mtime
    ct = effective_source_time(src, dirty)
    if conservative:
        return ot > max(ct, src.stat().st_mtime)
    return ot >= ct


# ---------------------------------------------------------------------------
# Self-test. `python3 scripts/lean_freshness.py --selftest`
#
# This exists because the commit-time rule SHIPPED BROKEN. It was introduced to
# fix a deadlock (bean qou-5v24), and it did -- while quietly acquiring the
# opposite defect: after merging 45 commits of `main` whose commits were dated
# EARLIER than the local oleans, a genuinely-changed module read as fresh. The
# hazard is invisible to any test that does not deliberately run the clocks
# backwards, so the clocks are run backwards here.
# ---------------------------------------------------------------------------

def _selftest() -> int:
    import os
    import tempfile

    d = Path(tempfile.mkdtemp())
    src, ol = d / "M.lean", d / "M.olean"
    src.write_text("theorem a : True := trivial\n")
    ol.write_text("OLEAN-v1")

    results: list[tuple[bool, str]] = []

    def check(name: str, got: bool, want: bool) -> None:
        results.append((got == want, f"{name}: got={got} want={want}"))

    # The temp dir is not a git repo, so `_commit_time` returns None and the
    # no-stamp path collapses to mtime. Pin a commit time to exercise it for real.
    real_commit_time = _commit_time
    pinned: dict[str, float | None] = {"t": None}
    globals()["_commit_time"] = lambda _s: pinned["t"]
    try:
        # --- no stamp, no commit time: mtime only ---
        os.utime(src, (1000, 1000)); os.utime(ol, (2000, 2000))
        check("no stamp, olean newer than source",
              olean_is_current(src, ol, set(), conservative=True), True)

        # --- THE REGRESSION. Content changed (mtime now); recorded commit time
        # went BACKWARDS, as it does when you merge an older-dated branch. ---
        os.utime(src, (3000, 3000)); pinned["t"] = 1500.0
        check("clock went backwards, rebuilder -> STALE (must rebuild)",
              olean_is_current(src, ol, set(), conservative=True), False)
        check("clock went backwards, guard -> tolerated (must still report)",
              olean_is_current(src, ol, set(), conservative=False), True)

        # --- containment: whatever the guard calls stale, the rebuilder must too.
        # This is the property that keeps qou-5v24 fixed; violate it and the
        # documented compose deadlocks again. ---
        for om, sm, ct in ((500, 3000, 1500), (2500, 1000, 4000),
                           (2500, 3000, 1000), (9, 9, 9)):
            os.utime(ol, (om, om)); os.utime(src, (sm, sm)); pinned["t"] = float(ct)
            lenient = olean_is_current(src, ol, set(), conservative=False)
            strict = olean_is_current(src, ol, set(), conservative=True)
            check(f"containment olean={om} src={sm} commit={ct}",
                  (not lenient) <= (not strict), True)

        # --- with a stamp, content decides and the clocks are not consulted ---
        record_source_sha(ol, src)
        os.utime(src, (9999, 9999)); os.utime(ol, (1, 1)); pinned["t"] = 9999.0
        check("stamped, unchanged, every clock says stale -> CURRENT",
              olean_is_current(src, ol, set(), conservative=True), True)

        src.write_text("theorem a : True := trivial\n-- edited\n")
        os.utime(src, (1, 1)); os.utime(ol, (9999, 9999)); pinned["t"] = 1.0
        check("stamped, CHANGED, every clock says fresh -> STALE",
              olean_is_current(src, ol, set(), conservative=True), False)
        check("stamped, CHANGED, guard also STALE",
              olean_is_current(src, ol, set(), conservative=False), False)

        ol.unlink()
        check("missing olean -> stale",
              olean_is_current(src, ol, set(), conservative=True), False)
    finally:
        globals()["_commit_time"] = real_commit_time

    for good, msg in results:
        print(f"  [{'ok  ' if good else 'FAIL'}] {msg}")
    bad = sum(1 for good, _ in results if not good)
    print(f"\nlean_freshness selftest: {'PASS' if not bad else f'{bad} FAILED'}")
    return 0 if not bad else 1


if __name__ == "__main__":
    import sys
    if "--selftest" in sys.argv:
        raise SystemExit(_selftest())
    raise SystemExit("usage: lean_freshness.py --selftest")
