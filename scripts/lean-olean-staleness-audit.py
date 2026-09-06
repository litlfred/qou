#!/usr/bin/env python3
"""Report Lean modules whose compiled olean is older than their source.

WHY THIS EXISTS
===============

`lean`-direct verifies a file against the *oleans on disk*, not against the
source tree. When an olean is older than its source, the environment a proof is
checked in is not the corpus a reader has. That is not a theoretical worry --
measured on this container, 2026-09-05, bean `qou-kp2z`:

  QOU/HeckeAlgebra/MarkovTrace.olean was dated 2026-06-10, ~3 months behind
  source. In that olean:

    * THREE declarations that are `def`s in source were AXIOMS --
      `JonesMarkovCoefficient`, `partitions_as_finset`, `markovTraceOnWedderburn`.
    * FIVE theorems present in source were ABSENT entirely.
    * `wenzlBridge` carried a `forall q` form that source had already RETRACTED
      (bean `qou-ck1f`) as "asserting the negation of what it was for".

The `def` -> AXIOM substitution is the dangerous one, because it is silent and
it inverts the meaning of the corpus's main hygiene check. `#print axioms` on a
theorem reaching those constants listed them as axioms -- so a footprint read
off that snapshot reported a fourth, fifth and sixth "axiom" that do not exist
in source. A reader comparing footprints across sessions would be comparing
cache states, not proofs.

WHY IT IS USUALLY REPAIRABLE
============================

The same measurement found MarkovTrace.lean could not be recompiled at all: 21
"has already been declared" errors. The cause was NOT a source defect -- a BFS
over source imports finds no cycle. It was a second stale olean:
JonesMarkovWenzl.olean (2026-07-02) still carried an `import MarkovTrace` that
its source had dropped on 2026-08-26. Rebuilding that one module from source
made MarkovTrace compile, and every kind mismatch above resolved.

So the normal remedy is a rebuild, not an investigation:

    bash scripts/lean-direct-cone.sh <Module.Name>

USAGE
=====

    python3 scripts/lean-olean-staleness-audit.py            # report all
    python3 scripts/lean-olean-staleness-audit.py --strict   # exit 1 if any
    python3 scripts/lean-olean-staleness-audit.py --top 20   # worst N

"No olean" is reported as its own state, never as fresh: a module that has
never been built is not a module that is up to date.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import subprocess
import sys
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parent.parent
LEAN_ROOT = ROOT / "content/quantum-observable-universe/lean"
SRC_ROOT = LEAN_ROOT / "QOU"
BUILD = LEAN_ROOT / ".lake/build/lib/lean/QOU"


def _stamp(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")


def _git_mtimes() -> dict[str, float]:
    """Last-commit timestamp per tracked path, from one history walk.

    Source mtimes are NOT used for the source side. `git checkout` stamps every
    working-tree file with the checkout time, so in a fresh clone all sources
    share one date and every restored olean reads as stale -- the audit would
    fire on all 2600+ modules and mean nothing. The commit date is a property of
    the content, so it is stable across clones. Falls back to mtime for paths
    git does not know (uncommitted new files), which are genuinely newer than
    any olean anyway.
    """
    out: dict[str, float] = {}
    try:
        proc = subprocess.run(
            ["git", "log", "--format=%n%at", "--name-only", "--", "content/"],
            cwd=ROOT, capture_output=True, text=True, check=True, timeout=300)
    except Exception:
        return out
    ts = 0.0
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.isdigit():
            ts = float(line)
        elif line.endswith(".lean") and line not in out:
            out[line] = ts          # history is newest-first, so first wins
    return out


def audit() -> tuple[list[dict], list[dict]]:
    git_ts = _git_mtimes()
    stale, unbuilt = [], []
    for src in sorted(SRC_ROOT.rglob("*.lean")):
        rel = src.relative_to(SRC_ROOT)
        module = "QOU." + str(rel)[:-5].replace("/", ".")
        repo_rel = str(src.relative_to(ROOT))
        s_m = git_ts.get(repo_rel) or src.stat().st_mtime
        olean = BUILD / rel.with_suffix(".olean")
        if not olean.exists():
            unbuilt.append({"module": module, "source": _stamp(s_m)})
            continue
        o_m = olean.stat().st_mtime
        if o_m < s_m:
            stale.append({
                "module": module,
                "olean": _stamp(o_m),
                "source": _stamp(s_m),
                "days": int((s_m - o_m) // 86400),
            })
    stale.sort(key=lambda r: -r["days"])
    return stale, unbuilt


def _rank_targets(limit: int) -> int:
    """List never-built modules ranked by how many others import them.

    A whole-corpus sweep answers "does it compile" in topological order, which
    means it spends its first hours on the SHALLOWEST modules -- the ones with
    fewest dependencies and therefore fewest ways to fail. Measured 2026-09-05
    (bean `qou-pdgc`): 798 such modules, 798 ok, which says little about the
    deep tail.

    This ranks the opposite way. A module that has never been built AND is
    imported by many others is where a defect would both exist undetected and
    propagate to everything above it. Reverse in-degree is direct, not
    transitive: it is a cheap proxy, and inflating it with a transitive closure
    would rank a handful of near-universal utilities above everything else and
    say nothing useful.
    """
    imports: dict[str, list[str]] = {}
    for src in sorted(SRC_ROOT.rglob("*.lean")):
        mod = "QOU." + str(src.relative_to(SRC_ROOT))[:-5].replace("/", ".")
        imports[mod] = re.findall(r"^import\s+(QOU\S*)", src.read_text(), re.M)
    known = set(imports)

    indeg: dict[str, int] = {m: 0 for m in imports}
    for deps in imports.values():
        for d in deps:
            if d in known:
                indeg[d] += 1

    def has_olean(m: str) -> bool:
        return (BUILD / (m[len("QOU."):].replace(".", "/") + ".olean")).exists()

    unbuilt = [m for m in imports if not has_olean(m)]
    ranked = sorted((m for m in unbuilt if indeg[m] > 0),
                    key=lambda m: (-indeg[m], m))
    leaves = len(unbuilt) - len(ranked)

    print(f"never built: {len(unbuilt)} of {len(imports)} module(s); "
          f"{len(ranked)} are imported by at least one other, {leaves} are leaves")
    if not ranked:
        print("  nothing to target -- every never-built module is a leaf.")
        return 0
    print()
    print(f"  {'in-deg':>6}  {'deps':>5}  module")
    for m in ranked[:limit]:
        print(f"  {indeg[m]:>6}  {len(imports[m]):>5}  {m}")
    if len(ranked) > limit:
        print(f"  ... and {len(ranked) - limit} more")
    print()
    print("  Build these before another undirected sweep: a leaf that does not")
    print("  compile breaks one module, one of these breaks everything above it.")
    print(f"      bash scripts/lean-direct-cone.sh {ranked[0]} -k -j3")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 when any olean is stale")
    ap.add_argument("--top", type=int, default=0,
                    help="show only the N stalest modules")
    ap.add_argument("--targets", type=int, default=0, metavar="N",
                    help="instead of the staleness report, list the N "
                         "never-built modules with the highest reverse "
                         "in-degree -- where a source defect would both exist "
                         "undetected and propagate. See _rank_targets")
    args = ap.parse_args()

    if args.targets:
        if not BUILD.exists():
            print(f"lean-olean-staleness-audit: no build directory at {BUILD}.")
            print("  Every module reads as never-built; that is not a finding.")
            return 2
        return _rank_targets(args.targets)

    if not BUILD.exists():
        print(f"lean-olean-staleness-audit: no build directory at {BUILD}.")
        print("  This is NOT a pass -- nothing was compared. Build first.")
        return 2

    stale, unbuilt = audit()
    shown = stale[:args.top] if args.top else stale

    if stale:
        print(f"STALE OLEANS -- olean older than source ({len(stale)} module(s)):")
        print(f"  {'days':>5}  {'olean':<12} {'source':<12} module")
        for r in shown:
            print(f"  {r['days']:>5}  {r['olean']:<12} {r['source']:<12} {r['module']}")
        if args.top and len(stale) > args.top:
            print(f"  ... and {len(stale) - args.top} more (drop --top to see all)")
        print()
        print("  A stale olean can silently turn a `def` into an AXIOM and drop")
        print("  theorems entirely, so `#print axioms` read against one reports a")
        print("  footprint the source does not have. Repair, do not interpret:")
        print(f"      bash scripts/lean-direct-cone.sh {stale[0]['module']}")
    else:
        print("lean-olean-staleness-audit: no olean is older than its source.")

    if unbuilt:
        print()
        print(f"NEVER BUILT ({len(unbuilt)} module(s)) -- reported separately, because")
        print("  a module with no olean is not a module that is up to date:")
        for r in unbuilt[:10]:
            print(f"    {r['module']}  (source {r['source']})")
        if len(unbuilt) > 10:
            print(f"    ... and {len(unbuilt) - 10} more")

    return 1 if (args.strict and stale) else 0


if __name__ == "__main__":
    sys.exit(main())
