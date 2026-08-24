#!/usr/bin/env python3
# polynomial_q_not_applicable: static import-graph audit, emits no numeric physics.
"""Measure the blind spot in the self-staleness axis: its IMPORTS.

## Why this exists

`witness_dependency_drift` compares a witness's recorded `scriptHash` to its
producer's CURRENT hash. That is the right question about the producer and says
nothing about what the producer IMPORTS — and twice on one branch the cause of
a real defect was exactly one level up the import graph:

  qou-w701  `cyclic_intertwiner_verify`'s own hash barely moved (a
            `set_compute_dps()` line) while `a_operator_gauge_align` changed
            the p-n interface underneath it. Residual 6.7e-49 -> 1.15e-3.

  qou-w7qk  `qbeta_ck_local_taylor_around_u0_probe` was untouched in substance;
            `y_lambda_wenzl_bridge` moved to convention D and returned
            `y_(1,1,1) = 0`, so the producer's 7-unknown fit lost a degree of
            freedom and its Jacobian went singular.

In both the axis rated the witness FRESH and would have forever. Each took a
human-scale investigation because nothing mechanical could point there.

This counts the population that condition can hide.

## What it measures, and what the number is NOT

For every witness whose producer hash MATCHES — the ones the axis calls fresh —
it asks whether any first-party module in the producer's import closure was
committed AFTER the witness was computed.

**This is an UPPER BOUND on exposure, not a defect count.** An import changing
is not proof a number changed: a docstring edit to `hecke_core` moves nothing.
Not one of these witnesses is shown to be wrong here, and none should be
inferred to be.

## Why it is NOT registered as a gate

Measured on `claude/mass-table-comprehensive-triage`: **2122 fresh, 921 with a
moved import — 43.4%.** A gate at that rate is red on arrival, and
`precision-gates.sh` says in its own preamble that a gate red on arrival gets
skipped, which is how a checker goes quiet. It belongs as an ADVISORY dimension
reported next to self-staleness.

The ranking is the useful output, not the total:

    914  computations/substrate/q_parameter.py
    898  qou-substrate/python/qou_substrate/witness.py          [plumbing]
    893  qou-substrate/python/qou_substrate/constants.py
    891  computations/substrate/experimental_constants.py
    884  computations/substrate/witness_base.py                 [plumbing]
    737  tools/pyhecke/python/pyhecke/constants.py
    708  computations/_path_bridge.py                           [plumbing]
    705  qou-substrate/python/qou_substrate/precision.py        [plumbing]
    703  tools/pyhecke/python/pyhecke/gram.py
    658  computations/substrate/_precision.py                   [plumbing]
    601  qou-substrate/python/qou_substrate/codata.py
    582  computations/codata_2022_source.py

Those are the families that produced this branch's flips: the CONSTANTS
(`codata_2022_source`, `experimental_constants`, `qou_substrate.constants`,
`pyhecke.constants`) behind the AME deuteron stale passes and the m_n 501 ppb
miss; `q_parameter` behind the borromean muon/proton re-anchoring; `pyhecke.gram`
behind the convention C->D moves. The axis is blind precisely where the corpus
has been moving. A witness on a changed constants module is worth a look in a
way that one on a changed `witness_base` is not.

A NOTE ON THAT RANKING, because it corrects itself. The first draft of this
measurement kept only the TOP THREE movers per witness, and its table read

    658 _precision · 578 codata_2022_source · 363 hecke_core ·
    340 witness_base · 326 witness · 292 q_parameter · 154 mass_tower...

Every one of those is a FLOOR: a module ranking fourth or lower for a given
witness never appeared. Recording every mover moves `q_parameter` from sixth at
292 to FIRST at 914, and surfaces five modules the truncated table showed at
zero — including three constants modules, the exact family the finding is
about. The truncation systematically under-ranked modules that appear
alongside many others, which is precisely the modules that matter here. Same
lesson as the rest of this branch: a slice read as a population.

## Usage

    python3 computations/audits/import_staleness_audit.py            # summary
    python3 computations/audits/import_staleness_audit.py --top 40   # ranking
    python3 computations/audits/import_staleness_audit.py --json OUT # full data

Exit status is always 0. This reports; it does not gate.
"""
from __future__ import annotations

import argparse
import ast
import collections
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
#: `computations/`, LOCATED rather than derived by counting `.parent` levels —
#: that count was wrong in both layouts it was written for (bean qou-rug0).
COMPUTATIONS = next(
    (a / "computations" for a in HERE.parents if (a / "computations").is_dir()),
    HERE.parent,
)
ROOT = COMPUTATIONS.parent
sys.path.insert(0, str(COMPUTATIONS))

import witness_dependency_drift as wdd  # noqa: E402

#: How deep to follow first-party imports. Bounded because the closure is
#: cyclic in places and the marginal signal past a few hops is noise: a module
#: three removed from the producer is rarely what moved a number.
MAX_DEPTH = 3


def _last_commit_dates() -> dict[str, str]:
    """rel-path -> YYYY-MM-DD of its most recent commit, in ONE git pass."""
    out: dict[str, str] = {}
    p = subprocess.run(
        ["git", "log", "--date=short", "--pretty=format:C|%ad", "--name-only",
         "--", "*.py"],
        cwd=ROOT, capture_output=True, text=True)
    date = None
    for line in p.stdout.splitlines():
        if line.startswith("C|"):
            date = line[2:]
        elif line.strip().endswith(".py") and date:
            out.setdefault(line.strip(), date)
    return out


def _module_index() -> dict[str, list[str]]:
    """module basename -> rel-path(s) that define it."""
    mod: dict[str, list[str]] = collections.defaultdict(list)
    for base in ("computations", "tools"):
        d = ROOT / base
        if not d.is_dir():
            continue
        for f in d.rglob("*.py"):
            if any(x in f.parts for x in ("_deprecated", "__pycache__", ".lake")):
                continue
            mod[f.stem].append(str(f.relative_to(ROOT)))
    return mod


def _imports_of(rel: str) -> set[str]:
    try:
        tree = ast.parse((ROOT / rel).read_text(encoding="utf-8", errors="replace"))
    except Exception:
        return set()
    out: set[str] = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            for a in n.names:
                out.add(a.name.split(".")[-1])
        elif isinstance(n, ast.ImportFrom) and n.module:
            out.add(n.module.split(".")[-1])
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--top", type=int, default=15,
                    help="how many movers to rank (default 15)")
    ap.add_argument("--json", metavar="PATH",
                    help="write the full per-witness data here")
    ap.add_argument("--list", type=int, default=0,
                    help="print this many example witnesses")
    args = ap.parse_args()

    last = _last_commit_dates()
    mod = _module_index()
    cache: dict[str, set[str]] = {}

    def closure(rel: str, depth: int = 0, seen: frozenset = frozenset()) -> set[str]:
        if rel in seen or depth > MAX_DEPTH:
            return set()
        if depth == 0 and rel in cache:
            return cache[rel]
        seen = seen | {rel}
        out: set[str] = set()
        for m in _imports_of(rel):
            for cand in mod.get(m, []):
                if cand == rel:
                    continue
                out.add(cand)
                out |= closure(cand, depth + 1, seen)
        if depth == 0:
            cache[rel] = out
        return out

    idx = wdd._build_producer_index([COMPUTATIONS, ROOT / "tools"])
    rows, fresh_total = [], 0
    for w in sorted(COMPUTATIONS.rglob("*.witness.json")):
        if "_deprecated" in w.parts:
            continue
        try:
            js = json.loads(w.read_text())
        except Exception:
            continue
        if not isinstance(js, dict):
            continue
        sf, sh, when = js.get("scriptFile"), js.get("scriptHash"), js.get("computedAt")
        if not (sf and sh and when):
            continue
        cands = idx.get(sf) or idx.get(pathlib.Path(sf).name)
        if not cands:
            continue
        prod = wdd._resolve_producer(cands, w)
        if wdd._file_hash12(prod) != sh:
            continue                      # already self-stale; the axis sees it
        fresh_total += 1
        wdate = when[:10]
        prel = str(prod.relative_to(ROOT))
        # EVERY mover, not a top-N slice. An earlier draft kept only the top 3,
        # which made the per-module ranking a FLOOR rather than a count — the
        # kind of truncation that gets read as a population.
        movers = sorted(((m, last[m]) for m in closure(prel)
                         if m in last and last[m] > wdate),
                        key=lambda x: x[1], reverse=True)
        if movers:
            rows.append({"witness": str(w.relative_to(ROOT)), "computedAt": wdate,
                         "producer": prel, "movers": movers,
                         "n_movers": len(movers)})

    pct = 100.0 * len(rows) / max(fresh_total, 1)
    print("=" * 74)
    print("IMPORT STALENESS — what the self-staleness axis cannot see")
    print("=" * 74)
    print(f"  witnesses the axis calls FRESH (hash matches) : {fresh_total}")
    print(f"  of those, a first-party import moved since    : {len(rows)}")
    print(f"                                                = {pct:.1f}%")
    print()
    print("  UPPER BOUND ON EXPOSURE, NOT A DEFECT COUNT. An import changing is")
    print("  not proof a number changed; a docstring edit moves nothing. No")
    print("  witness here is shown to be wrong.")
    print()

    freq = collections.Counter(m for r in rows for m, _ in r["movers"])
    print(f"  movers ranked by how many 'fresh' witnesses they sit under:")
    for m, n in freq.most_common(args.top):
        print(f"    {n:5d}  {m}")

    if args.list:
        print()
        for r in rows[:args.list]:
            print(f"  {r['witness']}")
            print(f"     computed {r['computedAt']}  producer {r['producer']}"
                  f"  ({r['n_movers']} imports moved since)")
            for m, d in r["movers"][:3]:
                print(f"        {d}  {m}")

    if args.json:
        pathlib.Path(args.json).write_text(json.dumps(rows, indent=1))
        print(f"\n  full data -> {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
