#!/usr/bin/env python3


# polynomial_q_not_applicable: source-scanning audit, no q-arithmetic.
"""Audit: stale substrate-q₀ literals + float64-leak risk in compute scripts.

Surfaced by the 2026-05-29 q₀ re-pin (#1422): q₀ moved from the muon
pin (1.10997859555…) to the proton pin (1.10997858275…). Scripts that
hardcoded the OLD value — instead of importing the canonical q₀ from
`q_parameter` — silently keep computing at the stale constant.

This audit scans `folio-assistant/computations/**/*.py` (and the
`tools/qou-substrate` package) and flags:

  * OLD-q₀ literal   — the muon-pin digits "10997859555" / "859555"
                       hardcoded as a value (NOT a `q_muon`/cross-check
                       reference, NOT a `# comment` documenting history).
  * stale-q₀ tr_M    — the old-q₀ Markov-trace leaf literals
                       (1.0653062285…, 0.9232332971…, 0.3882864715…)
                       that differ from the re-pinned values
                       (1.0653061442…, 0.9232332299…, 0.3882864240…).

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
ROOTS = [HERE, HERE.parent.parent / "tools" / "qou-substrate"]

OLD_Q0_PATTERNS = [re.compile(r"10997859555"), re.compile(r"(?<!\d)859555(?!\d)")]
# old-q₀ tr_M leaf literals (proton / neutron / deuteron) — first 13 sig figs
STALE_TRM_PATTERNS = [
    re.compile(r"1\.0653062285"),
    re.compile(r"0\.9232332971"),
    re.compile(r"0\.3882864715"),
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
            "Scans compute scripts for stale muon-pin q₀ literals "
            "(10997859555 / 859555) and old-q₀ tr_M leaf values left "
            "behind by the 2026-05-29 proton re-pin (#1422). "
            "production-hardcode entries are real bugs (a live constant "
            "kept at the old value); stale-docstring are cosmetic; "
            "legit-muon-xcheck are the intentional muon cross-check."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "canonical_q0_source": "q_parameter.q_at() / Q_50_DIGIT_STR (proton pin)",
        "old_muon_q0": "1.10997859555418057528…",
        "new_proton_q0": "1.10997858275138080759…",
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
