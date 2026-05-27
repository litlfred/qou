#!/usr/bin/env python3
"""
C_knot categorical identification: C_knot = 35/6 + 2ℏ_q² (0.015% match).

The deuteron geometric factor C_knot = B_AME / (m_e × |Σ y_λ χ^λ sgn f^λ|)
≈ 5.852 has a categorical decomposition:

  C_knot = (|S₃|² − 1) / |S₃| + 2ℏ_q²
         = 35/6 + 2×(q₀−1)²/q₀²
         = 5.8530 (vs empirical 5.8521, 0.015% match)

Leading term: 35/6 = (36−1)/6 = (dim regular_rep − dim trivial) / |S₃|
Correction: 2ℏ_q² = substrate Planck constant squared
"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from mpmath import mpf, mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

set_compute_dps()
mp.dps = 50

q0 = mpf(Q_50_DIGIT_STR)
hbar_sq = ((q0 - 1) / q0) ** 2

C_knot = mpf("5.852086")
C_formula = mpf(35) / 6 + 2 * hbar_sq
err = float(abs(C_knot - C_formula) / C_knot * 100)

print(f"C_knot = 35/6 + 2ℏ_q² = {float(C_formula):.6f} vs {float(C_knot):.6f} ({err:.4f}%)")

wb = WitnessBuilder("c-knot-categorical-identification", start_time=time.perf_counter())
wb.data["C_knot_empirical"] = fmt(C_knot, 10)
wb.data["C_knot_formula"] = fmt(C_formula, 10)
wb.data["formula"] = "(|S_3|^2 - 1)/|S_3| + 2*hbar_q^2 = 35/6 + 2*hbar_q^2"
wb.data["leading_term"] = "35/6 = (36-1)/6 = (dim(reg rep) - dim(triv)) / |S_3|"
wb.data["correction"] = "2*hbar_q^2 = substrate Planck correction"
wb.data["match_pct"] = f"{err:.4f}"
wb.add_assertion("C_knot_match", computed=float(C_formula), expected=float(C_knot), tolerance=0.01)
wb.save()
print("✓ Witness saved.")
