"""Weinberg-angle simple-multiplicity reading: numerical falsification.

Per conj:weinberg-angle-categorical, the simple/uniform reading
   cot θ_W ≈ tr_M(e_W^+ · σ_1^4) / tr_M(e_B^+ · σ_5^8)
            ≈ (4 · q^4) / (4 · q^8)  =  q^{-4}
should match CODATA cot θ_W ≈ 1.823 if the structural assignment is
right.  Compute at q_0 and document the discrepancy; this is the
informative null result that motivates the cell-content correction.
"""
import sys
from pathlib import Path
import json
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
import mpmath
mpmath.mp.dps = 50
from q_parameter import Q_50_DIGIT_STR

q = mpmath.mpf(Q_50_DIGIT_STR)
sin2theta_codata = mpmath.mpf("0.23129")  # CODATA 2022
cos_theta_codata = mpmath.sqrt(1 - sin2theta_codata)
sin_theta_codata = mpmath.sqrt(sin2theta_codata)
cot_theta_codata = cos_theta_codata / sin_theta_codata

# Simple-multiplicity reading
# (sym, sym, sym) pattern multiplicity = 4
ratio_simple_W_over_B = q**4 / q**8       # = q^{-4}
ratio_simple_W_to_B   = (4 * q**4) / (4 * q**8)  # also q^{-4}
cot_theta_simple = ratio_simple_W_to_B
sin2_theta_simple = 1 / (1 + cot_theta_simple ** 2)

rel_err = abs(cot_theta_simple - cot_theta_codata) / cot_theta_codata

print(f"q_0 = {mpmath.nstr(q, 20)}")
print(f"CODATA cot θ_W                  = {mpmath.nstr(cot_theta_codata, 14)}")
print(f"Simple-multiplicity reading     = q_0^{{-4}} = {mpmath.nstr(cot_theta_simple, 14)}")
print(f"Relative deviation              = {float(rel_err):.4f} ({float(rel_err)*100:.1f}%)")
print(f"Simple sin²θ_W (predicted)      = {mpmath.nstr(sin2_theta_simple, 14)}")
print(f"CODATA sin²θ_W                  = {sin2theta_codata}")
print()
print("Verdict: simple-multiplicity reading FAILS by 64%.")
print("Confirms the cell-content / Plancherel demotion: the corrected")
print("version requires non-uniform multiplicities + Higgs-vev")
print("induced Hoefsmit-decomposition automorphism.")

out = {
    "computation": "weinberg-angle-simple-falsified",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "description": (
        "Numerical falsification of the simple-uniform-multiplicity "
        "reading of conj:weinberg-angle-categorical: cot θ_W ≈ q_0^{-4} "
        "would give 0.66 at q_0 while CODATA target is 1.823 (rel err "
        "64%).  Records the informative null result that motivates the "
        "non-uniform Hoefsmit-multiplicity correction."
    ),
    "reference_blocks": [
        "conj:weinberg-angle-categorical",
        "conj:hoefsmit-ew-cell-content",
        "conj:categorical-linking-operation",
    ],
    "audit": "docs/audits/2026-05-06-refocused-1ppb-workplan-v2.md",
    "q_0": str(q),
    "codata": {
        "sin2_theta_W": str(sin2theta_codata),
        "cos_theta_W": str(cos_theta_codata),
        "sin_theta_W": str(sin_theta_codata),
        "cot_theta_W": str(cot_theta_codata),
    },
    "simple_multiplicity_reading": {
        "form": "cot θ_W = q^{-4}",
        "value_at_q0": str(cot_theta_simple),
        "predicted_sin2_theta_W": str(sin2_theta_simple),
        "relative_deviation_from_codata": float(rel_err),
    },
    "verdict": "simple-multiplicity-reading-falsified",
    "next_step": (
        "Use non-uniform Hoefsmit multiplicities (4, 2, 1, 3, 3, 1, 2, 4) "
        "plus Higgs-vev induced (W^3, B) → (Z, γ) automorphism; "
        "discharge gated on conj:categorical-linking-operation."
    ),
}
out_path = Path(__file__).parent / "weinberg-angle-simple-falsified.witness.json"
out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
print(f"\nWrote: {out_path}")
