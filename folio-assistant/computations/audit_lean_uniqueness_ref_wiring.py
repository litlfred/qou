"""Audit: per-nucleus witness JSONs cite their Lean SDP-uniqueness theorem.

Per Item 4 of the post-#1537 wiring picks (PR #1554 + workplan at
`docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md`),
every per-nucleus computational witness should include a
`lean_uniqueness_ref` field citing the SDP-uniqueness theorem from
the parameterised module landed in PR #1537.

This audit:
1. Walks every `*.witness.json` in `folio-assistant/computations/`.
2. Identifies per-nucleus witnesses by filename/content heuristics
   (matches H, p, n, deuteron, tritium, helium, lithium,
   beryllium, boron, carbon, nitrogen, oxygen, ... or generic
   isotope tags).
3. Reports witnesses missing the `lean_uniqueness_ref` field.
4. In `--strict` mode, exits non-zero if any per-nucleus witness
   lacks the field.

The audit emits its own witness `audit-lean-uniqueness-ref-wiring.witness.json`
capturing the missing-field count for tracking the wiring campaign.

Usage:
    python3 audit_lean_uniqueness_ref_wiring.py
    python3 audit_lean_uniqueness_ref_wiring.py --strict
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from witness_base import WitnessBuilder  # noqa: E402


# Nucleus name patterns to identify per-nucleus witnesses (substring
# match, case-insensitive). The audit only flags witnesses matching
# one of these — generic audit / cross-check / inventory witnesses
# are excluded.
NUCLEUS_PATTERNS = [
    r"\bm[-_]p\b",        # proton
    r"\bm[-_]n\b",        # neutron
    r"\bproton",
    r"\bneutron",
    r"\bdeuteron",
    r"\bdeuterium",
    r"\btritium",
    r"\bhelium",
    r"\blithium",
    r"\bberyllium",
    r"\bboron",
    r"\bcarbon",
    r"\bnitrogen",
    r"\boxygen",
    r"\bfluorine",
    r"\bneon",
    r"\bsodium",
    r"\bmagnesium",
    r"\baluminum",
    r"\bsilicon",
    r"\bphosphorus",
    r"\bsulfur",
    r"\bchlorine",
    r"\bargon",
    r"\bpotassium",
    r"\bcalcium",
    # generic isotope tags (each requires at least one digit — a fully
    # optional digit prefix made the old Be tag match the English word
    # "be" in descriptions)
    r"\b[1-9]\d*H\b",
    r"\bHe[1-9]\d*",
    r"\bLi[1-9]\d*",
    r"\b[1-9]\d*Be\b",
    r"\b[1-9]\d*B\b",
    r"\b[1-9]\d*C\b",
]
NUCLEUS_RE = re.compile("|".join(NUCLEUS_PATTERNS), re.IGNORECASE)

# Witnesses to explicitly exclude from the audit (meta-audits,
# cross-checks, generic inventories that aren't per-nucleus).
EXCLUDE_NAME_RE = re.compile(
    r"audit|cross[_-]check|inventory|registry|table|"
    r"index|sweep|drift|status|summary",
    re.IGNORECASE,
)


def is_per_nucleus_witness(witness_path: Path) -> bool:
    """Heuristic: does this witness pertain to a specific nucleus?

    Filename-only on purpose (2026-06-12). The previous description
    fallback matched nuclei *mentioned in passing* — "m_p/m_e =",
    "cross-validate proton trace", "validated at the 2-factor level
    (deuteron…)" — flagging coefficient probes and convention
    reconciliations as per-nucleus and inflating the audit
    denominator (PR #2193 batch-2 findings: every reverted
    false-positive fired on the description, never the name).
    Per-nucleus producers put the nucleus in the witness filename
    (the per-atom loop slug convention), so the name is the reliable
    signal.
    """
    name = witness_path.name
    if EXCLUDE_NAME_RE.search(name):
        return False
    return bool(NUCLEUS_RE.search(name))


def has_lean_uniqueness_ref(witness_path: Path) -> bool:
    """Check whether the witness JSON includes `lean_uniqueness_ref`."""
    try:
        doc = json.loads(witness_path.read_text())
    except (json.JSONDecodeError, OSError):
        return False
    # Search recursively in case it's nested under "data" etc.
    def _walk(obj):
        if isinstance(obj, dict):
            if "lean_uniqueness_ref" in obj:
                return True
            return any(_walk(v) for v in obj.values())
        if isinstance(obj, list):
            return any(_walk(v) for v in obj)
        return False
    return _walk(doc)


def main() -> int:
    t0 = time.perf_counter()
    strict = "--strict" in sys.argv

    witnesses = sorted(HERE.glob("*.witness.json"))
    per_nucleus = []
    wired = []
    missing = []

    for w in witnesses:
        if not is_per_nucleus_witness(w):
            continue
        per_nucleus.append(w.name)
        if has_lean_uniqueness_ref(w):
            wired.append(w.name)
        else:
            missing.append(w.name)

    print("=" * 76)
    print("  Per-nucleus witness lean_uniqueness_ref wiring audit")
    print("=" * 76)
    print()
    print(f"  Total *.witness.json scanned:        {len(witnesses)}")
    print(f"  Per-nucleus witnesses identified:    {len(per_nucleus)}")
    print(f"  Wired (have lean_uniqueness_ref):    {len(wired)}")
    print(f"  Missing lean_uniqueness_ref:         {len(missing)}")
    print()
    if missing:
        print("  Missing wiring (per workplan):")
        for name in missing[:30]:
            print(f"    - {name}")
        if len(missing) > 30:
            print(f"    ... and {len(missing) - 30} more")
        print()
        print("  Fix pattern (in the producer script):")
        print('    w.add_data("lean_uniqueness_ref", {')
        print('        "<nucleus>": "qou:QOU.BraidKnot.<wrapper>_uniqueness_closed",')
        print('        "framework_doc": "content/quantum-observable-universe/lean/'
              'QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",')
        print('        "note": "...",')
        print('    })')
        print()
        print("  Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md")
        print()

    coverage = len(wired) / len(per_nucleus) if per_nucleus else 1.0
    print(f"  Coverage: {coverage:.1%}")
    print()

    w = WitnessBuilder("audit-lean-uniqueness-ref-wiring",
                       engine="python", start_time=t0)
    w.set_description(
        "Audit: per-nucleus witness JSONs cite their Lean "
        "SDP-uniqueness theorem (`lean_uniqueness_ref` field). "
        "Tracks the wiring campaign per workplan at "
        "docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md. "
        "In `--strict` mode exits non-zero if any per-nucleus "
        "witness is missing the field."
    )
    w.add_data("total_witnesses_scanned", len(witnesses))
    w.add_data("per_nucleus_witnesses_count", len(per_nucleus))
    w.add_data("wired_count", len(wired))
    w.add_data("missing_count", len(missing))
    w.add_data("coverage_fraction", coverage)
    w.add_data("missing_witnesses", missing[:50])
    w.add_data("wired_witnesses", wired[:50])
    w.add_assertion(
        "lean_uniqueness_ref_coverage",
        computed=len(wired),
        expected=len(per_nucleus),
        tolerance=0,
        source=(
            "Every per-nucleus witness should include a "
            "lean_uniqueness_ref field per the post-#1537 wiring "
            "workplan."
        ),
    )
    w.save()

    if strict and missing:
        print(f"  STRICT mode: {len(missing)} missing-wiring witnesses → exit 1")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
