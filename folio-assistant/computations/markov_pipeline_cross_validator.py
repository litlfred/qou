#!/usr/bin/env python3
"""
Markov pipeline cross-validator — verify archimedean tr_M(q_0)
agreement across independent producers.

The QOU computation pipeline arrives at the archimedean Markov
trace value `tr_M(q_0)` from at least two independent paths:

1. **Polynomial-ring evaluation** — the path used by
   `markov_substrate_realizer.py`: take the Habiro-completion
   polynomial `p_in_u(u) ∈ ℤ[u]` from
   `habiro-coefficients-atomic.witness.json`, evaluate at
   `u_0 = q_0^{1/2}`, and divide by `denom_in_u(u_0)`.

2. **Mittag-Leffler full pole sum** — the path used by
   `term6_full_pole_sum.py` (currently on
   `claude/continue-pr-442-DJRWm`, expected to land on main as
   `term6-full-pole-sum.witness.json`): record
   `tr_M_at_q0_polynomial` per atom as part of the residue audit.

Both should agree at high precision.  This script forms a
cross-pipeline witness that the polynomial-ring realization
(Lean `MotivicSubstrate.realize Place.infty`) is consistent with
the residue-spectral-sum computation (Lean
`prop:gb-residue-spectral-sum`).

The check is **forward-compatible**: if the term6 witness is not
yet on main (e.g. 442 still open), the script reports SKIP and
exits 0.  Once 442 merges, a green run is direct empirical evidence
for both Lean propositions on the existing witness data.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


HERE = Path(__file__).parent
REALIZER_WITNESS = HERE / "markov-substrate-realization.witness.json"
TERM6_FULL_WITNESS = HERE / "term6-full-pole-sum.witness.json"
OUTPUT_WITNESS = HERE / "markov-pipeline-cross-validation.witness.json"

AGREEMENT_RTOL = 1e-9


def load_realizer() -> Optional[dict]:
    if not REALIZER_WITNESS.exists():
        return None
    with REALIZER_WITNESS.open() as f:
        return json.load(f)


def load_term6_full() -> Optional[dict]:
    if not TERM6_FULL_WITNESS.exists():
        return None
    with TERM6_FULL_WITNESS.open() as f:
        return json.load(f)


def realizer_archimedean_by_atom(realizer_data: dict) -> dict[str, float]:
    by_atom: dict[str, float] = {}
    for atom_record in realizer_data.get("results", []):
        atom = atom_record["atom"]
        for rz in atom_record.get("realizations", []):
            if rz.get("place") == "infty" and "tr_M_at_q0" in rz:
                by_atom[atom] = float(rz["tr_M_at_q0"])
                break
    return by_atom


def term6_archimedean_by_atom(term6_data: dict) -> dict[str, float]:
    by_atom: dict[str, float] = {}
    for atom_record in term6_data.get("data", {}).get("atoms", []):
        atom = atom_record.get("atom")
        if atom and "tr_M_at_q0_polynomial" in atom_record:
            by_atom[atom] = float(atom_record["tr_M_at_q0_polynomial"])
    return by_atom


def compare_value(label: str, x: float, y: float) -> dict:
    """Relative-tolerance comparison; returns a per-atom check."""
    if x == 0 and y == 0:
        agree = True
        rel = 0.0
    elif y == 0 or x == 0:
        agree = False
        rel = float("inf")
    else:
        rel = abs(x - y) / max(abs(x), abs(y))
        agree = rel <= AGREEMENT_RTOL
    return {
        "atom": label,
        "realizer_value": x,
        "term6_value": y,
        "abs_diff": abs(x - y),
        "rel_diff": rel,
        "agree": agree,
    }


def main() -> int:
    realizer_data = load_realizer()
    if realizer_data is None:
        print(
            f"realizer witness missing at {REALIZER_WITNESS}; "
            "run markov_substrate_realizer.py first.",
            file=sys.stderr,
        )
        return 1

    term6_data = load_term6_full()
    realizer_arch = realizer_archimedean_by_atom(realizer_data)

    if term6_data is None:
        skipped = {
            "computation": "markov-pipeline-cross-validation",
            "description": (
                "Cross-pipeline check between markov_substrate_realizer.py "
                "and term6_full_pole_sum.py.  The term6 witness is not yet "
                "present on this branch (likely still open on "
                "claude/continue-pr-442-DJRWm).  Forward-compatible: re-run "
                "this script after 442 merges to obtain the cross-validation "
                "certificate."
            ),
            "computedAt": datetime.now(timezone.utc).isoformat(),
            "status": "skipped-term6-witness-absent",
            "expected_input": TERM6_FULL_WITNESS.name,
            "available_realizer_atoms": sorted(realizer_arch.keys()),
        }
        with OUTPUT_WITNESS.open("w") as f:
            json.dump(skipped, f, indent=2)
            f.write("\n")
        print(f"markov_pipeline_cross_validator: SKIP (term6 witness not on this branch yet)")
        print(f"  realizer has {len(realizer_arch)} atoms with archimedean values:")
        for a, v in realizer_arch.items():
            print(f"    {a:>24}  tr_M(q_0) = {v:.10f}")
        print(f"Wrote {OUTPUT_WITNESS}")
        return 0

    term6_arch = term6_archimedean_by_atom(term6_data)

    # Compare on the intersection of atom labels; flag missing atoms.
    common = sorted(set(realizer_arch) & set(term6_arch))
    only_in_realizer = sorted(set(realizer_arch) - set(term6_arch))
    only_in_term6 = sorted(set(term6_arch) - set(realizer_arch))

    checks = [
        compare_value(atom, realizer_arch[atom], term6_arch[atom])
        for atom in common
    ]
    overall_pass = all(c["agree"] for c in checks)

    output = {
        "computation": "markov-pipeline-cross-validation",
        "description": (
            "Verifies archimedean tr_M(q_0) agreement between the polynomial-"
            "ring realization (markov_substrate_realizer.py) and the "
            "Mittag-Leffler full-pole-sum computation (term6_full_pole_sum.py)."
        ),
        "reference_blocks": [
            "prop:full-pole-structure-mass-trace",
            "prop:gb-residue-spectral-sum",
            "def:motivic-substrate",
        ],
        "lean_classes": [
            "qou:QOU.AlgebraicSubstrate.MotivicSubstrate",
            "qou:QOU.BraidKnot.HabiroCompletion",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "agreement_rtol": AGREEMENT_RTOL,
        "overall_pass": overall_pass,
        "checks": checks,
        "atoms_only_in_realizer": only_in_realizer,
        "atoms_only_in_term6": only_in_term6,
    }

    with OUTPUT_WITNESS.open("w") as f:
        json.dump(output, f, indent=2)
        f.write("\n")

    status = "PASS" if overall_pass else "FAIL"
    print(f"markov_pipeline_cross_validator: {status}")
    for c in checks:
        marker = "✓" if c["agree"] else "✗"
        print(
            f"  {marker} {c['atom']:>24}  realizer={c['realizer_value']:.10f}  "
            f"term6={c['term6_value']:.10f}  rel_diff={c['rel_diff']:.2e}"
        )
    if only_in_realizer or only_in_term6:
        print(f"  asymmetric atom coverage: realizer-only={only_in_realizer}, term6-only={only_in_term6}")
    print(f"Wrote {OUTPUT_WITNESS}")
    return 0 if overall_pass else 2


if __name__ == "__main__":
    sys.exit(main())
