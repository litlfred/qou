#!/usr/bin/env python3
"""
Bound-state-observable witness validator — CI gate enforcing the
master formula

    ⟨O⟩_T  =  Σ_{i,j ∈ A*(T)}  u_i*  (G^{-1})_{ij}  ⟨O, b_j⟩

(conj:confinement-frobenius-reciprocity).

Rule
----

Any witness whose ``description`` / ``computation`` / ``name`` field
claims to compute a **bound-state observable** (axial coupling,
magnetic moment, form factor, expectation value of an operator on
a confined state, …) must include *all four* of the following
fields anywhere in the witness JSON:

  - ``gram_matrix``    (the Frobenius Gram matrix on the NF basis)
  - ``gram_inverse``   ($G^{-1}$ used for dualisation)
  - ``lp_active_set``  (active LP-dual indices $A^*(T)$)
  - ``shadow_prices``  (LP-dual shadow prices $u^*$ on the active set)

…OR the witness must carry the explicit top-level opt-out

  - ``"observable_type": "raw_trace"``

(used when the observable IS the Hamiltonian and a raw Markov trace
is the correct answer — bucket (A) of the Frobenius-pairing audit).

The validator mirrors ``lp_dual_witness_validator.py`` in design and
defaults to warn-only (``--strict`` to fail CI).

Usage
-----
    python3 computations/bound_state_observable_validator.py
    python3 computations/bound_state_observable_validator.py --strict
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

# Hints in the witness's name / description that signal a
# bound-state-observable compute.
BOUND_STATE_HINTS = (
    "g_a",
    "g_v",
    "axial coupling",
    "axial-coupling",
    "axial form factor",
    "axial-form-factor",
    "magnetic moment",
    "magnetic-moment",
    "form factor",
    "form-factor",
    "bound-state observable",
    "bound state observable",
    "expectation value of",
    "expectation-value-of",
    "transition matrix element",
    "transition-matrix-element",
)

REQUIRED_FIELDS = (
    "gram_matrix",
    "gram_inverse",
    "lp_active_set",
    "shadow_prices",
)
OPTOUT_FIELD = "observable_type"
# Accepted opt-outs.  ``raw_trace`` is the legitimate Hamiltonian /
# raw-Markov-trace case (e.g. T_{3,5} weak-vertex form factor as
# direct Markov trace).  ``pslq_probe`` covers PSLQ / arithmetic-
# closed-form probes of *residuals* (e.g. δ_GT in g_A = [5]/[4]·(1+δ)),
# which are not bound-state observable computations and have no
# Gram / LP-active-set structure to verify.  PR #565 F5.
OPTOUT_VALUES = ("raw_trace", "pslq_probe")
OPTOUT_VALUE = OPTOUT_VALUES[0]  # back-compat for any importer


def _has_field(node, key: str) -> bool:
    if isinstance(node, dict):
        if key in node:
            return True
        return any(_has_field(v, key) for v in node.values())
    if isinstance(node, list):
        return any(_has_field(v, key) for v in node)
    return False


def is_bound_state_witness(path: Path) -> tuple[bool, str]:
    """Return (flagged, reason). Flagged iff the witness's name or
    description/computation/name field contains a bound-state hint.
    """
    name_low = path.name.lower()
    for hint in BOUND_STATE_HINTS:
        if hint in name_low:
            return True, f"filename matches '{hint}'"

    try:
        data = json.loads(path.read_text())
    except (json.JSONDecodeError, OSError):
        return False, ""

    for field in ("description", "computation", "name", "title"):
        v = data.get(field)
        if isinstance(v, str):
            v_low = v.lower()
            for hint in BOUND_STATE_HINTS:
                if hint in v_low:
                    return True, f"{field} matches '{hint}'"
    return False, ""


def verify_bound_state_witness(path: Path) -> dict:
    """Returns dict with keys: ok, missing_fields, opted_out."""
    try:
        data = json.loads(path.read_text())
    except (json.JSONDecodeError, OSError) as e:
        return {
            "ok": False,
            "missing_fields": list(REQUIRED_FIELDS),
            "opted_out": False,
            "error": str(e),
        }

    opted_out = data.get(OPTOUT_FIELD) in OPTOUT_VALUES
    missing = [f for f in REQUIRED_FIELDS if not _has_field(data, f)]
    return {
        "ok": (not missing) or opted_out,
        "missing_fields": missing,
        "opted_out": opted_out,
    }


def main(argv: list[str]) -> int:
    strict = "--strict" in argv
    root = Path(__file__).parent
    witnesses = sorted(root.glob("*.witness.json")) + sorted(
        root.glob("*-witness.json"))
    flagged: list[tuple[Path, str]] = []
    for w in witnesses:
        ok, reason = is_bound_state_witness(w)
        if ok:
            flagged.append((w, reason))

    print(
        f"Scanned {len(witnesses)} witness files; "
        f"{len(flagged)} flagged as bound-state observable."
    )
    print()

    failures = []
    for w, reason in flagged:
        result = verify_bound_state_witness(w)
        if not result["ok"]:
            failures.append((w, reason, result))

    if not failures:
        print(
            f"OK — all {len(flagged)} flagged witnesses include the required "
            f"bound-state-observable fields (gram_matrix, gram_inverse, "
            f"lp_active_set, shadow_prices) or carry the explicit "
            f"'observable_type': 'raw_trace' opt-out."
        )
        return 0

    label = "FAIL" if strict else "WARN"
    print(
        f"{label} — {len(failures)}/{len(flagged)} flagged witnesses "
        f"missing required bound-state-observable fields."
    )
    print()
    print("Sample (first 10):")
    for w, reason, result in failures[:10]:
        print(f"  ✗  {w.name}  ({reason})")
        print(f"     missing: {result['missing_fields']}")
    if len(failures) > 10:
        print(f"  ... ({len(failures) - 10} more)")
    print()
    print("To fix: implement the master formula")
    print("  ⟨O⟩_T = Σ_{i,j ∈ A*(T)} u_i (G⁻¹)_{ij} ⟨O, b_j⟩")
    print("(conj:confinement-frobenius-reciprocity), and emit:")
    print("  - gram_matrix, gram_inverse  (from gram-matrix-dual.witness.json)")
    print("  - lp_active_set, shadow_prices  (from lp_dual_solver.py)")
    print("Or, if the observable is the Hamiltonian and the raw Markov trace")
    print("is the correct answer, set top-level:")
    print('  "observable_type": "raw_trace"')
    print()
    if strict:
        print("Exit 1 (--strict mode).")
        return 1
    print("Exit 0 (warn-only mode; pass --strict to enforce).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
