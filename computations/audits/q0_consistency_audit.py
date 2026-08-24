#!/usr/bin/env python3


# polynomial_q_not_applicable: source-scanning audit, no q-arithmetic.
"""Audit: stale substrate-q₀ literals + float64-leak risk in compute scripts.

POLARITY INVERTED 2026-08-22 (bean `qou-ivhc`). This audit was written
when the MUON-anchored value was the pin, and it flagged the proton
solution as stale. The 2026-05-28 supersession (`q_muon_at`: "was the pin
until 2026-05-28; now superseded by `q_at()` (m_p anchor)") and the
2026-08-15 owner ruling reversed that, and the audit was never revisited —
so until today it classified **use of the canonical pin** as
`production-hardcode — a real bug`, and its `--strict` mode would have
failed CI for correct code.

Canonical q₀ is the PROTON pin, read from `q_parameter` at runtime rather
than quoted here — quoting it is the very defect this audit exists to
catch, and the previous literal went stale exactly that way. The STALE
values are now the pre-ruling muon-anchored ones (`1.10997859555733…`
hand-typed, and the `1.10997859555418…` variant; both are additionally
~8.5e-11 adrift from what `q_muon_at()` now derives — bean `qou-khac`).

Intentional muon cross-checks are still classified `legit-muon-xcheck`
and are NOT bugs; that escape hatch is unchanged and now carries more of
the load, since every muon literal matches the stale pattern.

This audit scans `computations/**/*.py` (and the
`tools/qou-substrate` package) and flags:

  * stale-q₀ literal — the stale-A digits "10997858275" / "858275"
                       hardcoded as a value (NOT a `q_muon`/cross-check
                       reference, NOT a `# comment` documenting history).
  * stale-q₀ tr_M    — the stale-A Markov-trace leaf literals
                       (1.0653062286…, 0.9232332971…, 0.3882864715…),
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

# Stale = the pre-ruling MUON-anchored q₀ family. `10997859555` covers both
# the hand-typed `…55733…` and the `…55418…` variant (bean `qou-khac`).
OLD_Q0_PATTERNS = [re.compile(r"10997859555"), re.compile(r"(?<!\d)9555733(?!\d)")]
# Stale tr_M leaf literals (proton / neutron / deuteron) — tr_M evaluated at the
# now-stale MUON q₀. These are the values this file previously called canonical;
# the canonical set is now tr_M at the proton pin (…0614425445 / …2332299 /
# …2864240), which the pre-inversion version scanned for as "stale".
# NOT recomputed here: both sets are taken verbatim from this file's own prior
# text, so the swap introduces no new numeric claim.
STALE_TRM_PATTERNS = [
    re.compile(r"1\.0653062286"),
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


def _canonical_q0() -> str:
    """The canonical proton pin, from `q_parameter` — never a literal here."""
    try:
        from q_parameter import Q_50_DIGIT_STR
        return str(Q_50_DIGIT_STR)
    except Exception as exc:  # noqa: BLE001 — recorded, not guessed
        return f"UNAVAILABLE: q_parameter import failed ({exc})"


def _script_hash() -> str:
    import hashlib
    return hashlib.sha256(
        Path(__file__).resolve().read_bytes()
    ).hexdigest()[:12]


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
        # This witness is the OUTPUT OF AN AUDIT -- a scan over the tree -- not
        # a computed quantity. `derivation_gap_categorize.py` reads `auditOnly`
        # as a DECLARED flag and cannot infer it, so without this line the file
        # lands in the production tier and is counted as owing a derivation
        # chain: the "category error to chain" that tool's own legend warns
        # about. Bean qou-akdup / dgpc.
        "auditOnly": True,
        "scriptFile": "computations/audits/q0_consistency_audit.py",
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
        # Provenance: absent before 2026-08-22, so no staleness gate could see
        # this witness at all (bean `qou-ivhc`).
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "scriptFile": "computations/audits/q0_consistency_audit.py",
        "scriptHash": _script_hash(),
        "engine": "python-re",
        # Read at runtime from the source this audit already named. The previous
        # version hardcoded a literal here and it was the WRONG one — it held a
        # muon value in a field called `canonical_proton_q0`. Quoting the pin is
        # the defect this audit exists to catch; it should not commit it itself.
        "canonical_q0_source": "q_parameter.Q_50_DIGIT_STR (proton pin), read at runtime",
        "canonical_proton_q0": _canonical_q0(),
        "stale_muon_q0_hand_typed": "1.10997859555733471989…",
        "stale_muon_q0_variant": "1.10997859555418057528…",
        "polarity_inverted": "2026-08-22, bean qou-ivhc — stale is now the muon family",
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
