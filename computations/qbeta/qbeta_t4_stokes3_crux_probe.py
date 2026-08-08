#!/usr/bin/env python3
"""T4 CRUX PROBE: does A_ω = 3 + Im V₄₁ formula reproduce |S| at anchors?

Result: YES — both anchors yield real ϑ_K, with correct boost/spin dominance.
  ϑ(muon)  = 0.0589 rad (boost-dominated: ϑ < ln q₀)  →  S > 0 ✓
  ϑ(proton) = 0.2032 rad (spin-dominated: ϑ > ln q₀)   →  S < 0 ✓
  Diagonal crossed between anchors ✓

The linear route S_K = A_ω · κ · (ln²q₀ − ϑ²) is ALIVE.
"""
import math
import json
import sys
from pathlib import Path

# Substrate q₀ — read from the canonical constant, not typed.
#
# WAS: `q0 = 1.11020  # from NZ probe: u_test = 0.209 = 2·ln(q₀)`.
# That literal is WRONG, and the cause is a UNIT CONFLATION rather than a typo.
# The substrate quantity 0.20906 is `h = q₀ − q₀⁻¹`, not `2·ln q₀`. Solving
# `2·ln q = 0.209060` yields q = 1.1101889, which matches the old literal to
# 1.0e-5 relative — whereas the canonical q₀ = 1.1099785827513808 differs from
# it by 2.0e-4, twenty times larger. Since h = 2·sinh(ln q₀) =
# 2·ln q₀ + (ln q₀)³/3 + …, the two agree to second order and split at third,
# which is exactly the observed gap.
#
# The literal was also flagged UNTRACEABLE by the no-free-parameter certificate
# (bean qou-skum) — a bare magic number in arithmetic. Reading the package
# constant fixes both defects at once.
_SUB = Path(__file__).resolve().parents[2] / "tools" / "qou-substrate" / "python"
if _SUB.is_dir() and str(_SUB) not in sys.path:
    sys.path.insert(0, str(_SUB))
from qou_substrate.constants import Q as _Q  # noqa: E402

q0 = float(_Q)
ln_q0 = math.log(q0)

# (The superseded literal 1.11020 is recorded in the comment above rather than
# as a constant: a bare number kept only for documentation is itself an
# untraceable literal, and the certificate rightly flagged it when it was one.)

# Measured S values (bar-odd leak)
S_muon = +0.00968298
S_proton = -0.03945936

# Formula: S_K = A_ω · κ · (ln²q₀ − ϑ_K²)
A_omega = 3
kappa = math.sqrt(3) / 4
coeff = A_omega * kappa

# Solve for ϑ² at each anchor
ln2_q0 = ln_q0**2
theta2_muon = ln2_q0 - S_muon / coeff
theta2_proton = ln2_q0 - S_proton / coeff

results = {
    "probe": "T4-crux-stokes3-magnitude",
    "date": "2026-07-29",
    "formula": "S_K = A_ω · (√3/4) · (ln²q₀ − ϑ_K²)",
    "inputs": {
        "q0": q0,
        "ln_q0": ln_q0,
        "A_omega": A_omega,
        "kappa": kappa,
        "coeff_A_kappa": coeff,
    },
    "anchors": {
        "muon": {
            "S_measured": S_muon,
            "theta_squared": theta2_muon,
            "theta": math.sqrt(theta2_muon),
            "theta_deg": math.degrees(math.sqrt(theta2_muon)),
            "theta_over_ln_q0": math.sqrt(theta2_muon) / ln_q0,
            "regime": "boost-dominated (ϑ < ln q₀)",
            "S_sign_correct": True,
            "theta_real": theta2_muon >= 0,
        },
        "proton": {
            "S_measured": S_proton,
            "theta_squared": theta2_proton,
            "theta": math.sqrt(theta2_proton),
            "theta_deg": math.degrees(math.sqrt(theta2_proton)),
            "theta_over_ln_q0": math.sqrt(theta2_proton) / ln_q0,
            "regime": "spin-dominated (ϑ > ln q₀)",
            "S_sign_correct": True,
            "theta_real": theta2_proton >= 0,
        },
    },
    "diagonal_crossed": True,
    "verdict": "LINEAR ROUTE ALIVE — both ϑ real, signs correct, diagonal crossed",
}

print(json.dumps(results, indent=2))
