#!/usr/bin/env python3


# polynomial_q_not_applicable: source-scanning audit, no q-arithmetic.
"""Audit: stale substrate-q₀ literals + float64-leak risk in compute scripts.

Canonical q₀ is the proton-anchored, habiro-refined value
C = 1.10997859555733471… (`q_parameter.Q`). The stale value is the
pre-habiro proton solution A = 1.10997858275138…, differing from C at
the 8th sig-fig (~1.2e-8). Scripts that hardcoded A — instead of
importing the canonical q₀ from `q_parameter` — silently keep computing
at the stale constant. (Direction verified empirically: only C
reproduces m_p/m_e to 10 sig-figs; A→C is exactly the habiro_ratio−1
≈ 2.42e-7 correction. See docs/audits/2026-06-21-q0-clusterA-migration-plan.md.)

This audit scans `computations/**/*.py` (and the
`tools/qou-substrate` package) and flags:

  * stale-q₀ literal — the stale-A digits "10997858275" / "858275"
                       hardcoded as a value (NOT a `q_muon`/cross-check
                       reference, NOT a `# comment` documenting history).
  * stale-q₀ tr_M    — the stale-A Markov-trace leaf literals
                       (1.0653062286…, 0.9232332971…, 0.3882864240…),
                       i.e. tr_M evaluated at the stale A.  The canonical
                       values at C are (1.0653062286…, 0.9232332971…,
                       0.3882864715…).  [Verified by direct computation
                       via markov_peel.tr_M_atomic: tr_M(proton)@A =
                       …0614425445 (= the leaf hardcoded across the
                       production derivation chain), @C = …0622861317.]

Each hit is classified:
  production-hardcode  — assigned to a live constant (`Q_0 = …`,
                         `q_val=…`, `sp.Rational("…")`) → real bug.
  stale-docstring      — inside a triple-quoted block / `#` comment
                         → cosmetic, low risk.
  legit-muon-xcheck    — on a line mentioning `muon`/`q_muon`/`cross`
                         → the framework's intentional muon cross-check.

Emits `q0-consistency-audit.witness.json`. Run with `--strict` to exit
non-zero when any production-hardcode remains (CI gate once the backlog
is cleared).
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
# Scan the whole computations/ tree (HERE.parent) + the qou-substrate package.
# (Before 2026-06-22 this read `HERE`, which the 2026-06-02 subdir refactor had
# silently narrowed to computations/audits/ only — contradicting the docstring's
# "scans computations/**/*.py".  Restored to the full tree.)
ROOTS = [HERE.parent, HERE.parent.parent / "tools" / "qou-substrate"]

OLD_Q0_PATTERNS = [re.compile(r"10997858275"), re.compile(r"(?<!\d)858275(?!\d)")]
# stale-A tr_M leaf literals (proton / neutron / deuteron) — tr_M evaluated at
# the stale A q₀.  Canonical (at C) is …062286 / …332971 / …864715.
STALE_TRM_PATTERNS = [
    re.compile(r"1\.0653061442"),
    re.compile(r"0\.9232332299"),
    re.compile(r"0\.3882864240"),
]
ASSIGN_RE = re.compile(r"=\s*['\"]?[-\d.]|q_val\s*=|Rational\(|mpf\(|mpmathify\(")
MUON_RE = re.compile(r"muon|q_muon|cross[-_ ]?check|crosscheck|prediction|9\.5\s*σ", re.I)


def _in_comment_or_doc(line: str, in_doc: bool) -> bool:
    s = line.lstrip()
    return in_doc or s.startswith("#")


def scan_file(p: Path) -> list[dict]:
    hits: list[dict] = []
    in_doc = False
    doc_delim = ""
    try:
        lines = p.read_text(errors="ignore").splitlines()
    except OSError:
        return hits
    for i, line in enumerate(lines, 1):
        # crude triple-quote tracking (good enough for classification)
        for delim in ('"""', "'''"):
            cnt = line.count(delim)
            if cnt:
                if not in_doc:
                    in_doc, doc_delim = True, delim
                    if cnt % 2 == 0:
                        in_doc = False
                elif delim == doc_delim and cnt % 2 == 1:
                    in_doc = False
        pats = [("old-q0", r) for r in OLD_Q0_PATTERNS] + \
               [("stale-trM", r) for r in STALE_TRM_PATTERNS]
        for kind, rx in pats:
            if not rx.search(line):
                continue
            if _in_comment_or_doc(line, in_doc):
                cls = "stale-docstring"
            elif MUON_RE.search(line):
                cls = "legit-muon-xcheck"
            elif ASSIGN_RE.search(line):
                cls = "production-hardcode"
            else:
                cls = "production-hardcode"
            hits.append({
                "file": str(p.relative_to(HERE.parent.parent)),
                "line": i,
                "kind": kind,
                "classification": cls,
                "text": line.strip()[:160],
            })
    return hits


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any production-hardcode remains")
    args = ap.parse_args()

    all_hits: list[dict] = []
    for root in ROOTS:
        if not root.exists():
            continue
        for p in sorted(root.rglob("*.py")):
            if "_deprecated" in p.parts or p.name == "q0_consistency_audit.py":
                continue
            all_hits.extend(scan_file(p))

    by_class: dict[str, int] = {}
    for h in all_hits:
        by_class[h["classification"]] = by_class.get(h["classification"], 0) + 1
    prod = [h for h in all_hits if h["classification"] == "production-hardcode"]

    print("=" * 78)
    print(" q₀ re-pin consistency audit (old muon-q₀ literals in compute)")
    print("=" * 78)
    print(f"  scanned roots: {[str(r) for r in ROOTS]}")
    for cls, n in sorted(by_class.items()):
        print(f"  {cls:22s} {n}")
    print(f"  TOTAL hits: {len(all_hits)}  | production-hardcode: {len(prod)}")
    print()
    for h in prod:
        print(f"  [HARDCODE] {h['file']}:{h['line']}  ({h['kind']})")
        print(f"             {h['text']}")

    witness = {
        "computation": "q0-consistency-audit",
        "description": (
            "Scans compute scripts for stale pre-habiro q₀ literals "
            "(10997858275 / 858275) and stale-A tr_M leaf values "
            "(tr_M evaluated at A) that the 2026-06-22 cluster-A "
            "migration replaced with the canonical C values. "
            "production-hardcode entries are real bugs (a live constant "
            "kept at the stale value); stale-docstring are cosmetic; "
            "legit-muon-xcheck are the intentional muon cross-check."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "canonical_q0_source": "q_parameter.q_at() / Q_50_DIGIT_STR (proton pin, habiro-refined)",
        "stale_pre_habiro_q0": "1.10997858275138080759…",
        "canonical_proton_q0": "1.10997859555733471989…",
        "counts_by_classification": by_class,
        "total_hits": len(all_hits),
        "production_hardcode_count": len(prod),
        "hits": all_hits,
    }
    out = HERE / "q0-consistency-audit.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\nWitness: {out}")

    if args.strict and prod:
        print(f"\nSTRICT: {len(prod)} production-hardcode(s) remain — exiting 1")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
