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

DEFAULT_LEAN_ROOT = Path("content/quantum-observable-universe/lean")


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
