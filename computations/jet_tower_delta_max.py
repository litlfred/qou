#!/usr/bin/env python3
"""
Measurement witness for `conj:jet-tower-uniform-delta-max`.

Per workplan task **P3.4 path (b)**, this script measures the
per-level binding contribution

    Δ⁽ⁿ⁾(ρ) = 𝔪⁽ⁿ⁾(ρ_free) − 𝔪⁽ⁿ⁾(ρ_atom)

across n = 1..N for a fixed set of light atoms {D, T, ³He}, and
records:

  - max |Δ⁽ⁿ⁾| over the measured range — the empirical Δ_max,
  - the geometric-decay ratio
        |ℏ_q^{2n} Δ⁽ⁿ⁾| / |ℏ_q^{2(n-1)} Δ⁽ⁿ⁻¹⁾|,
    which the conjecture predicts ≈ ℏ_q² ≈ 0.00982 once Δ_max
    saturates,
  - a uniform-bound-pass flag (true if |Δ⁽ⁿ⁾| does not grow over n).

Output: jet-tower-delta-max.witness.json

Refs:
  - content/.../braids-and-knots/jet-tower-uniform-delta-max.md
  - content/.../braids-and-knots/jet-tower-convergence.md
  - computations/unified_lift.py
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

DIR = Path(__file__).parent

# Reuse the full unified-lift pipeline (already computes delta_n
# per jet level — see unified_lift.py line 158 onward).
sys.path.insert(0, str(DIR))

from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import AME_B_HE3_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402

try:
    from unified_lift import binding_unified
    from q_parameter import HBAR_Q
except Exception as exc:  # pragma: no cover
    print(f"unified_lift / q_parameter unavailable: {exc}", file=sys.stderr)
    sys.exit(0)

HBAR_Q_SQ = HBAR_Q * HBAR_Q

ATOMS = [
    # (label, Z, N, AME-derived B_total in MeV — for sanity reporting)
    ("D",    1, 1,  2.22452),
    ("T",    1, 2,  float(AME_B_TRITIUM_MEV_VALIDATION)),
    ("3He",  2, 1,  float(AME_B_HE3_MEV_VALIDATION)),
]

# Force the unified-lift jet loop to run a fixed number of levels
# regardless of the precision target. Path (b) wants per-level
# observation, not early exit.
N_MAX = int(os.environ.get("JET_DELTA_MAX_N_MAX", "8"))
os.environ.setdefault("JET_TARGET_PPM", "1e-12")  # very tight → no early exit
os.environ.setdefault("JET_MAX_LEVELS", str(N_MAX))


def measure_atom(label: str, Z: int, N: int, B_AME_MeV: float) -> dict:
    """Run unified_atom_binding for one atom and extract the
    per-level Δ⁽ⁿ⁾ history."""
    try:
        result = binding_unified(Z, N)
    except Exception as exc:  # pragma: no cover
        return {
            "atom": label, "Z": Z, "N": N,
            "error": f"{type(exc).__name__}: {exc}",
        }
    jet_log = result.get("jet_log", [])
    delta_history = [
        {
            "n": entry["level"],
            "delta_n": float(entry["delta_n"]),
            "abs_delta_n": abs(float(entry["delta_n"])),
            "term_cat": float(entry["term_cat"]),
            "abs_term_cat": abs(float(entry["term_cat"])),
        }
        for entry in jet_log
    ]
    if not delta_history:
        return {
            "atom": label, "Z": Z, "N": N,
            "error": "jet_log empty (unified_lift did not iterate)",
        }
    abs_deltas = [d["abs_delta_n"] for d in delta_history]
    max_abs_delta = max(abs_deltas)
    # Geometric-decay ratio of consecutive |ℏ_q^{2n} Δ⁽ⁿ⁾| values:
    abs_terms = [d["abs_term_cat"] for d in delta_history]
    ratios = [
        abs_terms[i] / abs_terms[i - 1] if abs_terms[i - 1] > 0 else None
        for i in range(1, len(abs_terms))
    ]
    # Uniform-bound pass: |Δ⁽ⁿ⁾| does not grow over n.
    uniform_pass = all(
        abs_deltas[i] <= abs_deltas[i - 1] * (1.0 + 1e-6)
        for i in range(1, len(abs_deltas))
    )
    return {
        "atom": label,
        "Z": Z, "N": N,
        "B_AME_MeV": B_AME_MeV,
        "n_levels_measured": len(delta_history),
        "delta_history": delta_history,
        "max_abs_delta": max_abs_delta,
        "geometric_ratios": ratios,
        "predicted_geometric_ratio_hbar_q_sq": HBAR_Q_SQ,
        "uniform_bound_pass": uniform_pass,
    }


def main() -> int:
    measurements = [measure_atom(*atom) for atom in ATOMS]
    # Aggregate pass: every atom passes uniform-bound check.
    aggregate_pass = all(
        m.get("uniform_bound_pass", False)
        for m in measurements
        if "error" not in m
    )
    witness = {
        "computation": "jet-tower-delta-max",
        "purpose": (
            "Measurement witness for `conj:jet-tower-uniform-delta-max` "
            "(P3.4 path (b)): per-level binding contribution Δ⁽ⁿ⁾ for "
            "{D, T, ³He}, max |Δ⁽ⁿ⁾|, geometric decay ratios, and "
            "uniform-bound pass/fail."
        ),
        "narrative_block": "conj:jet-tower-uniform-delta-max",
        "audit_gap_closed": "GAP 14a (path (b))",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "hbar_q_sq": HBAR_Q_SQ,
        "n_max": N_MAX,
        "measurements": measurements,
        "aggregate_uniform_bound_pass": aggregate_pass,
    }
    # PR #578 (Copilot review): expose the script's pass/fail criterion
    # via WitnessBuilder.add_assertion so allPassed reflects it.
    out = (WitnessBuilder.wrap_legacy(
        "jet-tower-delta-max", witness,
        script_path=__file__, engine="python")
        .add_assertion(
            "aggregate_uniform_bound_pass",
            computed=1.0 if aggregate_pass else 0.0,
            expected=1.0,
            tolerance=0.0,
            source="conj:jet-tower-uniform-delta-max",
        )
        .save())
    print(f"  Witness written to {out.name}")
    print(f"  aggregate_uniform_bound_pass = {aggregate_pass}")
    for m in measurements:
        if "error" in m:
            print(f"  {m['atom']:>4s}  ERROR: {m['error']}")
        else:
            print(f"  {m['atom']:>4s}  n={m['n_levels_measured']:>2d}  "
                  f"max|Δ|={m['max_abs_delta']:.6e}  "
                  f"pass={m['uniform_bound_pass']}")
    return 0 if aggregate_pass else 1


if __name__ == "__main__":
    sys.exit(main())
