#!/usr/bin/env python3
"""
Witness staleness — the THIRD direction: imported-module drift.

`witness_dependency_drift.py` checks exactly two directions:

  SELF      the producer file's own `scriptHash` changed
  UPSTREAM  a recorded `upstream_witness_hashes` entry changed

Neither hashes the producer's **imported-module cone**. So when an upstream
`.py` MODULE changes, the producer stays byte-identical (SELF green) and no
upstream *witness* moved (UPSTREAM green, or undeclared — adoption is 7.7 %),
while the committed numbers no longer reproduce. That is a silent stale witness.

This is not hypothetical. It was hit three times in one session (PR #4939):

  bsym-residual-shell-structure   <- `_bond_type_L` / `tr_m_atom_via_transfer`
                                     changed 2026-08-08. Refresh flipped
                                     hypothesis H2 from true to FALSE.
  gap2-borromean-triple-count     <- `coulomb_energy` changed 2026-08-09
                                     (bean qou-usft). Refresh moved the
                                     bonded-triple ratios 1.132/1.197/1.240
                                     -> 1.148/1.210/1.250.
  coulomb-mirror-killswitch       <- same `coulomb_energy` change.

Neither of the first two declares `upstream_witness_hashes` at all.

## What this audit does

For each `*.witness.json`: resolve its producer, walk the producer's
first-party import cone transitively, and compare the cone's most recent
COMMIT time against the witness's own `computedAt`. A module committed after
the witness was computed means the witness was left behind.

Deliberately uses git commit time, not mtime: a fresh clone rewrites every
mtime, so mtime would report the whole corpus as stale in CI and nothing in a
warm checkout. Commit time is stable across clones.

## Why a heuristic here is the right call

Recording cone hashes in the witness at generation time is the durable fix, but
it detects NOTHING retroactively — every existing witness lacks the field, so
the ~2,900 already on disk would stay invisible until each is regenerated,
which is exactly the work this is meant to prioritise. Commit-time comparison
needs no schema change and works on the corpus as it stands today. The two are
complements: this drains the backlog, the recorded field prevents the next one.

Known limits, stated rather than hidden:
  * A comment-only or docstring-only commit to a cone module trips this with no
    numerical consequence — same false-positive class as `scriptHash`, and the
    same remedy: diff the module before re-running an expensive producer
    (AGENTS.md §idle-backlog).
  * Import resolution is by module basename against the producer index, which
    matches how this repo actually imports (flat bare names via `_path_bridge`).
    A basename collision resolves to the shallowest path.
  * Dynamic/`__import__` and function-local imports inside third-party code are
    not followed. Function-local first-party imports ARE followed — the corpus
    uses them heavily (e.g. `_constants()` imports `q_parameter` in its body).

Witnesses already flagged SELF-stale are EXCLUDED from the headline count, so
what this reports is exactly the class the existing validator cannot see.

## Measured, 2026-08-10 (2,773-commit window)

    witnesses scanned      2,874
    SELF-stale (excluded)    666
    IMPORT-CONE STALE      1,431      <- invisible to the existing validator

The raw count is NOT the actionable number, and the by-module rollup is why this
audit prints one. 1,431 witness-level questions collapse to 8 module-level ones,
and two diffs already resolve 1,098 of them (77 %):

    1,090  qou_substrate/precision.py        FALSE POSITIVE - the change is
                                             +54/-0, a new `json_safe_float`
                                             helper that alters no existing
                                             code path.
      289  markov/markov_trace_recursive.py  PLAUSIBLE - +158/-30 with a
                                             convention fix in the title.
                                             Genuine behavioural change; the
                                             289 need a real look.
       26  hecke/hecke_characters.py         unchecked
       13  derived_masses.py                 unchecked
        8  mass_binding_dashboard.py         FALSE POSITIVE - display-only
                                             `_disp` fix from this same PR.

So triage per MODULE, never per witness: one `git show --stat` on the culprit
usually settles a four-figure block. Expect a high false-positive rate on the
raw count and do not quote it as a backlog size.

Exit code is 0 always: this is a triage/ranking tool, not a gate. Turning it
into a gate is a separate decision — at current corpus age it would be red on
day one, which is a backlog to drain, not a build to break.

Bean qou-a2q5.
"""
from __future__ import annotations

import ast
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_dependency_drift import (  # noqa: E402
    _build_producer_index,
    _resolve_producer,
    check_self_staleness,
)

MAX_DEPTH = 8
REPO_ROOT = HERE.parent
_commit_time_cache: dict[Path, datetime | None] = {}


# ── Provenance-only cone modules ────────────────────────────────────────
#
# A module that WRITES the witness cannot move the number inside it.  Excluding
# those from ATTRIBUTION does not change the stale COUNT -- it changes which
# module each stale witness is filed under.
#
# That matters because `newest_dep` reports only the single newest cone module,
# so one recent commit to a near-universally-imported module OVERWRITES the
# attribution on everything behind it.  Worked example: the
# `markov-peel-atomic-tr-m-muon` witness is genuinely cone-stale -- confirmed by
# re-run, its numbers move up to 2.9x -- via the ctype/averaged_weighted repair
# and four `canonical_braid_crossings` commits.  None of those appeared in the
# output; it was filed under the JSON serializer, because the serializer commit
# was newer.  A reader working that table would have re-run it, watched the
# numbers move, and credited a serializer.
#
# THE COUNTS BELOW DRIFT -- RE-MEASURE, DO NOT TRUST THEM.  Two snapshots,
# ~700 commits apart, of the same corpus:
#
#                          2026-08-23    2026-08-24
#     IMPORT-CONE STALE          1473          1618
#       PROVENANCE-ONLY            15           206
#       SUBSTANTIVE              1458          1412
#
#     top attribution        witness.py*  q_parameter.py 1059
#                                          mass_at_3A_proper.py 255
#                                          _path_bridge.py      206
#     * pre-fix; the fix moved it off the serializer entirely
#
# A comment quoting corpus-wide counts is itself a measurement that goes stale,
# which is the defect this whole file exists to detect.  Treat the shape as
# durable and the digits as expired.
#
# The corpus already holds this judgement about `witness.py` one field over:
# AGENTS.md records that it masks `scriptCommitSha` in `_EPHEMERAL_META_FIELDS`,
# and that `witness_dependency_drift.py` keys self-staleness on `scriptHash`
# alone, because that field is provenance, not mathematics.
#
# DELIBERATELY NOT LISTED: `_precision.py` and `q_parameter.py`.  Both CAN move
# a number -- one sets working precision, the other serves q_0 -- so excluding
# them would hide real staleness.  `q_parameter` is the top attribution and is
# imported nearly as universally as WitnessBuilder, so the same "one recent
# commit to a near-universal module" dynamic applies to it -- but to a module
# that genuinely can change values, which is the difference.  Whether those
# actually moved is a re-run question this detector does not settle.
#
# Keep this list minimal.  Every addition is a claim that the module cannot
# affect a value, and a wrong path fails SILENTLY -- `computations/witness_base.py`
# in the first draft matched nothing (the file is at
# `computations/substrate/witness_base.py`), so attribution fell through to the
# next provenance module and the fix LOOKED like it had worked.
PROVENANCE_ONLY = frozenset({
    "tools/qou-substrate/python/qou_substrate/witness.py",
    "computations/substrate/witness_base.py",
    "computations/_path_bridge.py",
})


def _is_provenance_only(rel_path: str) -> bool:
    return rel_path in PROVENANCE_ONLY


def _rel(p: Path) -> str:
    """Display path relative to the repo root — the cone reaches outside
    `computations/` (e.g. `tools/qou-substrate/.../witness.py`), so anchoring
    on HERE raises."""
    try:
        return str(p.relative_to(REPO_ROOT))
    except ValueError:
        return str(p)


def _graft_sha() -> str | None:
    """The shallow-clone graft commit, if this is a shallow clone.

    THIS MATTERS MORE THAN IT LOOKS. CI and agent sandboxes clone shallow, and
    in a shallow clone the boundary commit has no parent, so `git log` attributes
    EVERY file not touched since the graft to that one commit — here it presents
    as "31,823 files changed, 11,425,386 insertions" dated today. Reading those
    dates naively reports the entire corpus as freshly modified: the first draft
    of this audit did exactly that and produced a confident, meaningless "1,481
    import-cone stale". Files whose last commit is the graft have UNKNOWN age and
    must be reported as such, never as recent.
    """
    shallow = REPO_ROOT / ".git" / "shallow"
    if not shallow.is_file():
        return None
    try:
        roots = subprocess.run(
            ["git", "rev-list", "--max-parents=0", "HEAD"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=30,
        ).stdout.split()
        return roots[0] if roots else None
    except subprocess.SubprocessError:
        return None


GRAFT = _graft_sha()


def _git_commit_time(path: Path) -> datetime | None:
    """Last AUTHOR time of `path`; None if untracked, or if the last commit is
    the shallow graft (age unknown — see `_graft_sha`).

    Author time, not committer time: rebase-merge is this repo's default merge
    (AGENTS.md rule 8) and it rewrites committer dates, so `%cI` would date a
    module by when its branch was last rebased rather than when it changed.
    """
    if path in _commit_time_cache:
        return _commit_time_cache[path]
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%H %aI", "--", str(path)],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=30,
        ).stdout.strip()
        if not out:
            dt = None
        else:
            sha, _, iso = out.partition(" ")
            dt = None if (GRAFT and sha == GRAFT) else datetime.fromisoformat(iso)
    except (subprocess.SubprocessError, ValueError):
        dt = None
    _commit_time_cache[path] = dt
    return dt


def _imported_names(py: Path) -> set[str]:
    """Module basenames imported by `py`, including function-local imports."""
    try:
        tree = ast.parse(py.read_text(encoding="utf-8", errors="replace"))
    except (SyntaxError, OSError):
        return set()
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                names.add(a.name.split(".")[-1])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                # `from substrate.codata_constants import X` -> codata_constants
                names.add(node.module.split(".")[-1])
    return names


def import_cone(producer: Path, index: dict[str, list[Path]]) -> set[Path]:
    """Transitive first-party import cone of `producer`, excluding itself.

    First-party = the module basename resolves in the producer index, i.e. it
    is a `.py` under `computations/` or `tools/`. Anything else (stdlib,
    mpmath, numpy, ...) is not our dependency to track.
    """
    seen: set[Path] = {producer}
    frontier = [(producer, 0)]
    cone: set[Path] = set()
    while frontier:
        cur, depth = frontier.pop()
        if depth >= MAX_DEPTH:
            continue
        for name in _imported_names(cur):
            for cand in index.get(f"{name}.py", []):
                if cand in seen:
                    continue
                seen.add(cand)
                cone.add(cand)
                frontier.append((cand, depth + 1))
    return cone


def main() -> int:
    witnesses = sorted(HERE.rglob("*.witness.json"))
    index = _build_producer_index([HERE, HERE.parent / "tools"])

    stale, no_computed_at, unresolved, self_stale_skipped = [], 0, 0, 0

    for wp in witnesses:
        if "_deprecated" in wp.parts:
            continue
        try:
            w = json.loads(wp.read_text())
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(w, dict):
            continue

        script_file, computed_at = w.get("scriptFile"), w.get("computedAt")
        if not script_file:
            continue
        if not computed_at:
            no_computed_at += 1
            continue
        try:
            when = datetime.fromisoformat(computed_at)
            if when.tzinfo is None:
                when = when.replace(tzinfo=timezone.utc)
        except ValueError:
            no_computed_at += 1
            continue

        candidates = index.get(script_file, [])
        if not candidates:
            unresolved += 1
            continue
        producer = _resolve_producer(candidates, wp)

        # Isolate the NEW class: if the producer itself moved, the existing
        # SELF check already sees it and this would be double-counting.
        if check_self_staleness(wp, index) is not None:
            self_stale_skipped += 1
            continue

        movers = []
        for mod in import_cone(producer, index):
            ct = _git_commit_time(mod)
            if ct and ct > when:
                movers.append((mod, ct))
        if movers:
            movers.sort(key=lambda t: t[1], reverse=True)
            # Attribute to the newest module that could actually MOVE a number.
            # Reporting the bare newest lets one provenance commit overwrite the
            # real cause on every witness behind it (see PROVENANCE_ONLY).
            substantive = [m for m in movers
                           if not _is_provenance_only(_rel(m[0]))]
            attrib = substantive[0] if substantive else movers[0]
            newest = attrib[1]
            stale.append({
                "witness": _rel(wp),
                "producer": _rel(producer),
                "computed_at": when,
                "newest_dep": _rel(attrib[0]),
                "newest_dep_time": newest,
                "lag_days": (newest - when).days,
                "n_movers": len(movers),
                "n_substantive_movers": len(substantive),
                "provenance_only": not substantive,
            })

    stale.sort(key=lambda r: r["lag_days"], reverse=True)

    print("=" * 78)
    print(" WITNESS IMPORT-CONE STALENESS — the direction SELF and UPSTREAM miss")
    print("=" * 78)
    print(f"  witnesses scanned            : {len(witnesses):,}")
    print(f"  SELF-stale (already caught)  : {self_stale_skipped:,}  (excluded below)")
    print(f"  producer unresolved          : {unresolved:,}")
    print(f"  no usable computedAt         : {no_computed_at:,}")
    prov_only = [r for r in stale if r["provenance_only"]]
    substantive = [r for r in stale if not r["provenance_only"]]
    print(f"  IMPORT-CONE STALE            : {len(stale):,}  <- invisible to the "
          f"existing validator")
    print(f"    of which PROVENANCE-ONLY   : {len(prov_only):,}  (every mover "
          f"only writes the witness — cannot change a value)")
    print(f"    of which SUBSTANTIVE       : {len(substantive):,}  <- the "
          f"triage-worthy set")
    if GRAFT:
        print()
        print(f"  ⚠ SHALLOW CLONE (graft {GRAFT[:12]}). Every module not touched since")
        print("    the graft has UNKNOWN age and is skipped, so the count above is a")
        print("    LOWER BOUND covering only post-graft commits — it is not the corpus")
        print("    figure. Run in a full clone (`git fetch --unshallow`) for that.")

    if stale:
        print("\n  Worst 25 by lag (days between the witness and its newest dependency):\n")
        print(f"  {'lag':>6}  {'deps':>4}  witness")
        print(f"  {'-' * 6}  {'-' * 4}  {'-' * 58}")
        for r in stale[:25]:
            print(f"  {r['lag_days']:>6}  {r['n_movers']:>4}  {r['witness']}")
            print(f"  {'':>6}  {'':>4}    newest: {r['newest_dep']} "
                  f"({r['newest_dep_time'].date()})")

        # Rollup by culprit module. This is the actionable view: the backlog is
        # driven by a handful of core modules, and you drain it by deciding
        # per-MODULE whether its change was numerical, not by opening 1,400
        # witnesses one at a time.
        by_mod: dict[str, int] = {}
        for r in stale:
            by_mod[r["newest_dep"]] = by_mod.get(r["newest_dep"], 0) + 1
        print("\n  Top dependency movers — modules invalidating the most witnesses:\n")
        print(f"  {'count':>6}  module (newest change in the cone)")
        print(f"  {'-' * 6}  {'-' * 58}")
        for mod, n in sorted(by_mod.items(), key=lambda kv: kv[1], reverse=True)[:12]:
            print(f"  {n:>6}  {mod}")

        print("\n  Read this as a ranked backlog, not a verdict. A cone module may have")
        print("  moved by a comment-only commit, in which case the recomputed payload is")
        print("  byte-identical — diff the module before re-running an expensive producer.")
        print("  The durable fix is recording cone hashes at generation time (bean qou-a2q5);")
        print("  this exists because that fix detects nothing retroactively.")

    # Full population dump. The ranked table above prints only the worst 25,
    # which is a lag-biased slice: unusable as a work list, and unusable for a
    # stratified re-run sample -- the only thing that answers how many of these
    # actually MOVE, since a newer cone module is grounds to suspect, not
    # evidence. Attribution was fixed so `newest_dep` names a module that can
    # actually move a number; without a way to EXPORT the rows, that fix could
    # not be acted on.
    if "--json" in sys.argv:
        _out = sys.argv[sys.argv.index("--json") + 1]
        with open(_out, "w", encoding="utf-8") as _f:
            json.dump([{"witness": r["witness"],
                        "producer": r["producer"],
                        "newest_dep": r["newest_dep"],
                        "lag_days": r["lag_days"],
                        "n_movers": r["n_movers"],
                        "n_substantive_movers": r.get("n_substantive_movers"),
                        "provenance_only": r.get("provenance_only")}
                       for r in stale], _f, indent=2)
        print(f"\n  full population written to {_out} ({len(stale):,} rows)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
