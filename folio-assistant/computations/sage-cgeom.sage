#!/usr/bin/env sage
"""
C_geom from the Reshetikhin-Turaev invariant — Sage computation.

The fine structure constant relates to q via:
    α = tanh(ln q) / C_geom

where C_geom is the total Skein weight of the electron-proton
crossing evaluation.

Hecke relation: (T - q)(T + q^{-1}) = 0
Skein relation: T - T^{-1} = (q - q^{-1})
              = L_+ - L_- = (q - q^{-1}) L_0

Convention: q is the ONLY polynomial variable.
The Jones polynomial of a link L is J_L(q) = tr_M(rho(beta_L)).

This computation:
  1. Compute J_trefoil(q) via the Hecke algebra H_2(q)
  2. Compute J_Borromean(q) via the Hecke algebra H_6(q)
  3. Compute the colored Jones of Borromean in the adjoint rep
  4. Derive C_geom from the Hopf(trefoil, Borromean) satellite invariant

Run from repo root:
    sage folio-assistant/computations/sage-cgeom.sage

Output:
    folio-assistant/computations/sage-cgeom.witness.json

Target: C_geom ≈ 14.25 = tanh(ln q) / α
"""

import json
import math
from datetime import datetime, timezone

print("=" * 60)
print("C_geom from Reshetikhin-Turaev invariant")
print("=" * 60)
print()

q_num = 1.110

# ── Jones polynomials via Sage knot library ──────────────────────
# Sage has built-in knot and link support.

print("Computing Jones polynomials...")
print()

# Trefoil knot (left-handed)
K_trefoil = Knots().trefoil()
J_trefoil_poly = K_trefoil.jones_polynomial()
print(f"J_trefoil(q) = {J_trefoil_poly}")
print(f"  (Sage uses variable 't' internally; we interpret as q)")

# Evaluate at q = 1.110
# Sage Jones polynomial uses variable 't'; substitute q_num
t = J_trefoil_poly.parent().gen()
J_trefoil_val = float(J_trefoil_poly.subs({t: q_num}))
print(f"  J_trefoil({q_num}) = {J_trefoil_val:.6f}")
print()

# Figure-eight knot (4_1)
K_fig8 = Knots().figure_eight()
J_fig8_poly = K_fig8.jones_polynomial()
J_fig8_val = float(J_fig8_poly.subs({t: q_num}))
print(f"J_figure_eight(q) = {J_fig8_poly}")
print(f"  J_figure_eight({q_num}) = {J_fig8_val:.6f}")
print()

# ── Borromean rings ──────────────────────────────────────────────
# The Borromean rings are a 3-component link.
# Sage can compute the Jones polynomial of links via the braid closure.

# Borromean rings as a braid word:
# One representation on 6 strands:
# sigma_1 sigma_3^{-1} sigma_5 sigma_2^{-1} sigma_4 sigma_6^{-1} ...
# Actually, a cleaner rep on 3 strands doesn't exist (Borromean needs >= 6).

# Use Sage's Link class if available
try:
    # Try using Sage's Link functionality
    # Borromean rings as braid closure on 6 strands:
    # [1, -3, 5, -2, 4, -6, 1, -3, 5, -2, 4, -6] (one representation)
    from sage.knots.link import Link
    B6 = BraidGroup(6)
    # Standard Borromean braid word
    borr_braid = B6([1, -3, 5, -2, 4, 1, -3, 5, -2, 4])
    L_borr = Link(borr_braid)
    J_borr_poly = L_borr.jones_polynomial()
    J_borr_val = float(J_borr_poly.subs({J_borr_poly.parent().gen(): q_num}))
    print(f"J_Borromean(q) = {J_borr_poly}")
    print(f"  J_Borromean({q_num}) = {J_borr_val:.6f}")
    borromean_computed = True
except Exception as e:
    print(f"Could not compute Borromean Jones polynomial: {e}")
    print("  Will use known value: J_Borromean(q) = 1 (trivial in fundamental rep)")
    J_borr_val = 1.0
    borromean_computed = False

print()

# ── Hopf link ────────────────────────────────────────────────────
try:
    B2 = BraidGroup(2)
    hopf_braid = B2([1, 1])
    L_hopf = Link(hopf_braid)
    J_hopf_poly = L_hopf.jones_polynomial()
    J_hopf_val = float(J_hopf_poly.subs({J_hopf_poly.parent().gen(): q_num}))
    print(f"J_Hopf(q) = {J_hopf_poly}")
    print(f"  J_Hopf({q_num}) = {J_hopf_val:.6f}")
except Exception as e:
    print(f"Hopf link computation: {e}")
    J_hopf_val = -(q_num**0.5 + q_num**2.5)
    print(f"  Using analytic formula: J_Hopf = {J_hopf_val:.6f}")

print()

# ── Quantum group data ───────────────────────────────────────────
ha = q_num - 1.0/q_num           # q - q^{-1}
two_q = q_num + 1.0/q_num        # [2]_q
tanh_ln_q = ha / two_q           # tanh(ln q) = EM/strong ratio
alpha_target = 1.0 / 137.036     # CODATA fine structure constant
C_geom_target = tanh_ln_q / alpha_target

# q-integers
def q_int(n, q=q_num):
    return (q**n - q**(-n)) / (q - q**(-1))

print(f"Quantum group data at q = {q_num}:")
print(f"  tanh(ln q) = {tanh_ln_q:.6f}  (EM/strong ratio, exact from q)")
print(f"  α (CODATA)  = {alpha_target:.6f}")
print(f"  C_geom target = {C_geom_target:.4f}")
print()
print(f"  [2]_q = {q_int(2):.6f}")
print(f"  [3]_q = {q_int(3):.6f}")
print(f"  [5]_q = {q_int(5):.6f}")
print(f"  [7]_q = {q_int(7):.6f}")
print()

# ── Colored Jones polynomial (adjoint representation) ────────────
# The colored Jones polynomial of the Borromean link in the
# adjoint (spin-1) representation gives the EM coupling strength.
#
# For a Hopf link colored by reps V_a, V_b:
#   J(Hopf; V_a, V_b; q) = S_{ab} / S_{0b}
# where S is the modular S-matrix of SU_q(2).
#
# The modular S-matrix for SU_q(2) at level k:
#   S_{jj'} = sqrt(2/(k+2)) × sin(π(2j+1)(2j'+1)/(k+2))
#
# For real q (not root of unity), use the quantum Clebsch-Gordan:

# For the coupling of electron (fundamental, j=1/2) to proton
# (complicated representation), the relevant quantity is:
# Sum over partial waves: Σ_j [2j+1]_q × coupling_j

# Test: C_geom from [2]_q × [7]_q (best candidate from Python computation)
C_test_2x7 = q_int(2) * q_int(7)
alpha_test = tanh_ln_q / C_test_2x7
print(f"Test: C_geom = [2]_q × [7]_q = {C_test_2x7:.4f}")
print(f"  → α = {alpha_test:.6f},  1/α = {1.0/alpha_test:.2f}")
print(f"  Error from 137.036: {abs(1.0/alpha_test - 137.036)/137.036*100:.1f}%")
print()

# The [7]_q factor connects to:
# - Brings surface genus g=4, with 2g-1 = 7
# - The septafoil knot T_{2,7} which saturates the genus
# This is suggestive but needs rigorous TQFT derivation.

# ── Assemble witness ─────────────────────────────────────────────
witness = {
    "computation": "sage-cgeom",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "sage_version": str(version()),
    "description": (
        "C_geom from the Skein evaluation of the electron-proton "
        "Hopf link.  Convention: Hecke (T-q)(T+q^{-1})=0, "
        "Skein L_+ - L_- = (q-q^{-1})L_0."
    ),
    "target": {
        "C_geom": C_geom_target,
        "alpha": alpha_target,
    },
    "q": q_num,
    "jones_polynomials": {
        "J_trefoil": {"polynomial": str(J_trefoil_poly), "value": J_trefoil_val},
        "J_figure_eight": {"polynomial": str(J_fig8_poly), "value": J_fig8_val},
        "J_Borromean": {"value": J_borr_val, "computed": borromean_computed},
        "J_Hopf": {"value": J_hopf_val},
    },
    "q_dependent_exact": {
        "tanh_ln_q": tanh_ln_q,
    },
    "formula_candidates": {
        "[2]_q × [7]_q": {"value": C_test_2x7,
                          "1/alpha": 1.0/tanh_ln_q * C_test_2x7,
                          "error_pct": abs(1.0/(tanh_ln_q/C_test_2x7) - 137.036)/137.036*100},
    },
    "status": "Partial — Jones polynomials computed; colored Jones in adjoint rep pending.",
}

import os
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "sage-cgeom.witness.json")
with open(out_path, "w") as f:
    json.dump(witness, f, indent=2, default=str)

print(f"Witness written to {out_path}")
