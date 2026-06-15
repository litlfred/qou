#!/usr/bin/env python3
"""
C_geom from the Kauffman bracket of the electron-proton link.

The fine structure constant relates to q via:
    α = tanh(ln q) / C_geom

where C_geom is the total Skein weight of the electron-proton
evaluation — the ratio of the Jones polynomial of the composite
link to the product of Jones polynomials of the components.

This script computes:
1. Jones polynomials of trefoil, Hopf link, Borromean at q
2. The composite link invariant via satellite link formula
3. C_geom from the ratio

Usage:
    python3 computations/electron-proton-skein-weight.py

Output:
    computations/electron-proton-skein-weight.witness.json
"""

import json
import math
from datetime import datetime, timezone
from pathlib import Path

from q_parameter import (Q as q, Q_INV as qi, HA as ha,
                         S_SKEIN as s, TWO_Q as two_q, q_int)

# ══════════════════════════════════════════════════════════════════
# Jones polynomials at q = 1.110
# ══════════════════════════════════════════════════════════════════

# Unknot: J = 1
J_unknot = 1.0

# Left trefoil T_{2,3}: J(q) = -q⁻⁴ + q⁻³ + q⁻¹
J_trefoil = -q**(-4) + q**(-3) + q**(-1)

# Mirror trefoil: J(q) = -q⁴ + q³ + q
J_mirror_trefoil = -q**4 + q**3 + q

# Figure-eight 4_1: J(q) = q² - q + 1 - q⁻¹ + q⁻²
J_figure_eight = q**2 - q + 1 - qi + qi**2

# Hopf link L2a1: J(q) = -(q^{1/2} + q^{5/2})
J_hopf = -(q**0.5 + q**2.5)

# ══════════════════════════════════════════════════════════════════
# Quantum group S-matrix approach
# ══════════════════════════════════════════════════════════════════
#
# For the Hopf link colored by representations V_a, V_b:
#   J(Hopf; V_a, V_b; q) = S_{ab} / S_{0b}
#
# where S is the modular S-matrix of SU_q(2).
#
# For the fundamental representation (spin-1/2, dim = [2]_q):
#   S_{1/2, 1/2} / S_{0, 1/2} = -(q^{1/2} + q^{5/2}) / [2]_q
#
# For the adjoint representation (spin-1, dim = [3]_q):
#   S_{1, 1/2} / S_{0, 1/2} relates to the coupling strength

# Quantum dimensions (q_int imported from q_parameter)
dim_fund = q_int(2)      # [2]_q = q + q⁻¹
dim_adj = q_int(3)       # [3]_q

# ══════════════════════════════════════════════════════════════════
# Satellite link formula for electron-proton
# ══════════════════════════════════════════════════════════════════
#
# The hydrogen atom is: electron (trefoil) Hopf-linked to proton.
# The proton's internal structure is Borromean (Vol = 7.328).
#
# For the electromagnetic coupling, the relevant quantity is the
# LINKING interaction between electron and proton. The Skein
# evaluation of this Hopf link gives the coupling strength.
#
# For a Hopf link between knots K₁ and K₂:
# The interaction strength per unit charge is:
#   α_link = |J(K₁ ∪_Hopf K₂)| / (|J(K₁)| × |J(K₂)| × [2]_q)
#
# The [2]_q factor in the denominator normalizes by the quantum
# dimension of the exchanged photon (spin-1 boson = Hopf link).

# For electron (trefoil) linked to a point particle (unknot):
# J(T_{2,3} ∪_Hopf 0_1) = J(Hopf) × J(trefoil) (satellite formula)
# But this is NOT correct — the satellite formula is more complex.

# ══════════════════════════════════════════════════════════════════
# Direct computation: crossing resolutions of Hopf(T_{2,3}, proton)
# ══════════════════════════════════════════════════════════════════
#
# The Hopf link between electron and proton has 1 inter-component
# crossing. The Skein resolution at this crossing gives:
#
#   q × (trefoil ⊔ proton)  →  separate, unlinked
#   -q⁻¹ × (negative crossing variant)
#   s × (smoothed crossing: trefoil connected to proton)
#
# The "smoothed" state (L₀) is a composite knot formed by joining
# the electron and proton strands. This composite has a specific
# Jones polynomial that depends on both internal structures.
#
# The coupling strength α comes from how much of the "linked" state
# overlaps with the "smoothed" state:
#
#   α ∝ s / (q + q⁻¹) = (q^½ - q^{-½}) / (q + q⁻¹)
#     = tanh(ln q) × q^{-½}/(q^{½} + q^{-½})
#
# The C_geom factor accounts for the INTERNAL crossing resolutions
# that occur when the composite L₀ knot is further reduced.

# For the trefoil (3 crossings), each internal crossing adds a
# q-factor to the total Skein weight. The proton (Borromean, 6
# crossings) contributes similarly. But the crossings are not
# independent — they form a specific topological structure.

# ── Counting approach ────────────────────────────────────────────
# The electromagnetic vertex involves 2 Skein resolutions:
# one at the electron and one at the proton (α² dependence of
# energy = 2 resolutions). So for EACH photon exchange:
#
# Weight per resolution = tanh(ln q)
# Weight for 2 resolutions = tanh²(ln q)
#
# The ionization energy is E = m_e α² / 2 = m_e tanh²(ln q) / (2 C_geom²)
#
# If C_geom = 1, then α = tanh(ln q) = 0.1040, giving 1/α ≈ 9.6.
# Observed: 1/α = 137.036.
# So C_geom = tanh(ln q) × 137.036 = 14.25.
#
# C_geom must come from the total Skein weight of the internal
# crossing structure. Let's count what contributes:

# The trefoil has 3 crossings. In the Kauffman bracket:
# ⟨T_{2,3}⟩ = (-A)^{3w} × (expression with 2^3 = 8 terms)
# where w is the writhe.

# Trefoil writhe = +3. So the framing correction is (-A)^{-9}.
# The bracket expansion has 8 states (3 crossings, 2 choices each).

# At each crossing: A-smoothing or A⁻¹-smoothing
# A-smoothing → state with 0-smoothing, weight A
# A⁻¹-smoothing → state with ∞-smoothing, weight A⁻¹

# For the Kauffman bracket variable A related to q:
# A = q^{1/4} (Jones convention)
# or A² = -q (Kauffman convention)

# Using A² = -q^{1/2}:
# (Note: different conventions exist; we follow Jones 1985)

# ── Numerical approach ───────────────────────────────────────────
# Direct enumeration of the Kauffman bracket is feasible for
# small crossing numbers. The trefoil has 3 crossings → 8 states.

# Kauffman bracket of trefoil (writhe +3):
# Using A = q^{1/4} convention where ⟨unknot⟩ = 1:
#
# ⟨T_{2,3}⟩ = A^7 + A^3 + A^{-1} + A^{-5}  (unnormalized)
# ... but normalization conventions vary.

# Let's use the JONES POLYNOMIAL directly, which is well-defined:
# V_{T_{2,3}}(t) = -t⁻⁴ + t⁻³ + t⁻¹  (with t = q)
# Already computed above as J_trefoil.

# ══════════════════════════════════════════════════════════════════
# C_geom from the Hopf link coupling formula
# ══════════════════════════════════════════════════════════════════
#
# The electromagnetic coupling in the QOU comes from the Skein
# evaluation at the Hopf crossing between electron and proton.
# The full formula (from the Reshetikhin-Turaev TQFT) is:
#
# α = |S_{1,j}|² / |S_{0,j}|²
#
# where j labels the proton's representation and S is the
# modular S-matrix of SU_q(2).
#
# For the fundamental representation (j = 1/2):
# S_{1,1/2} / S_{0,1/2} = sin(2π/(k+2)) / sin(π/(k+2))
#
# In the q-parametrization (q = e^{2πi/(k+2)}):
# S_{1,1/2} / S_{0,1/2} = [2]_q

# But q = 1.110 is REAL, not a root of unity. For real q:
# The modular S-matrix is replaced by the universal R-matrix
# evaluation. The relevant formula is:
#
# Coupling per crossing = R-matrix eigenvalue ratio
# For the fundamental rep:
# R = q^{1/2} on symmetric channel, -q^{-1/2} on antisymmetric
# Eigenvalue ratio: q / (-q⁻¹) = -q²
# |Coupling|² = q² / (q² + 1)... not quite.

# Let me try a cleaner derivation from first principles.
# The QOU says:
# Coulomb/Strong = tanh(ln q) = (q - q⁻¹)/(q + q⁻¹)
# This gives the EM coupling relative to the STRONG force.
# The fine structure constant α is the EM coupling in absolute units.
# The conversion factor C_geom converts the relative ratio to α.

# Physical meaning of C_geom:
# It's the number of "effective photon exchange paths" between
# the electron and proton, weighted by their Skein factors.
# Each path involves resolving one crossing with weight tanh(ln q).
# The total coupling is tanh(ln q) / C_geom.

# For the hydrogen atom:
# The electron orbits at distance a₀ (Bohr radius)
# The photon must resolve crossings in BOTH the electron (trefoil)
# and the proton (Borromean) internal structures.
# C_geom counts the total weighted crossing paths.

# From the Schur-Weyl duality perspective:
# C_geom = dim(adjoint) × dim(fundamental) / dim(trivial)
#        = [3]_q × [2]_q / [1]_q
# At q = 1.110: [3]_q × [2]_q = 3.044 × 2.011 = 6.12
# That gives α = 0.104 / 6.12 = 0.017 → 1/α = 59. Not right.

# Try: C_geom = [2]_q × [3]_q × [2]_q = 12.28
# α = 0.104 / 12.28 = 0.0085 → 1/α = 118. Getting closer.

# Try: C_geom = [2]_q³ × [3]_q / [2]_q = [2]_q² × [3]_q = 12.28
# Same.

# Try: C_geom = Σ_{j=0}^{j_max} [2j+1]_q = [1]+[3]+[5]+...
# This is the total quantum dimension up to some cutoff.
# [1]+[3]+[5] = 1 + 3.044 + 5.220 = 9.264 → 1/α = 89
# [1]+[3]+[5]+[7] = ... need [7]_q
seven_q = q_int(7)
# [1]+[3]+[5]+[7] = 1 + 3.044 + 5.220 + 7.459 = 16.72 → 1/α = 161
# Too big. The truth (14.25) is between the j_max=2 and j_max=3 sums.

# ── Dimensional analysis approach ────────────────────────────────
# The proton has Borromean volume 7.328 and the electron has 3
# crossings. The interaction strength should involve both.
# Hypothesis: C_geom = Vol(B_3)/ℏ_q × n_e_crossings / [some factor]

hbar_q = 1.0 - qi
Vol_B = 7.3277
C_from_vol = Vol_B / hbar_q  # = 7.328 / 0.0991 = 73.9

# Way too big. Let me try:
# C_geom = Vol(B_3) / (n_crossings_trefoil × ℏ_q²)
C_from_vol2 = Vol_B / (3 * hbar_q**2)  # = 7.328 / (3 × 0.00982) = 248.8
# Also too big.

# ── Quantum group dimension approach ─────────────────────────────
# For SU_q(2), the total quantum dimension is:
# D² = Σ_j [2j+1]_q²
# The coupling goes as α = tanh(ln q) / √D or similar.

# Let me just compute several q-integer products and see which
# matches C_geom = 14.25.

tanh_ln_q = ha / two_q

results = {}
for formula_name, value in [
    ("[2]_q × [3]_q", dim_fund * dim_adj),
    ("[2]_q²", dim_fund**2),
    ("[2]_q × [7]_q / [1]_q", dim_fund * seven_q),
    ("[3]_q × [5]_q / [1]_q", dim_adj * q_int(5)),
    ("[2]_q² × [3]_q / [1]_q", dim_fund**2 * dim_adj),
    ("[5]_q × [3]_q / [1]_q", q_int(5) * dim_adj),
    ("Σ [2j+1]_q for j=0..2", 1 + dim_adj + q_int(5)),
    ("(1/2) Σ [2j+1]_q for j=0..3", 0.5 * (1 + dim_adj + q_int(5) + seven_q)),
    ("[2]_q⁴ / [3]_q", dim_fund**4 / dim_adj),
    ("Vol(B₃) / (ℏ_q × [2]_q)", Vol_B / (hbar_q * dim_fund)),
]:
    alpha_pred = tanh_ln_q / value
    inv_alpha = 1.0 / alpha_pred if alpha_pred != 0 else float('inf')
    results[formula_name] = {
        "value": value,
        "alpha": alpha_pred,
        "1/alpha": inv_alpha,
        "error_pct": abs(inv_alpha - 137.036) / 137.036 * 100,
    }

# ══════════════════════════════════════════════════════════════════
# Assemble witness
# ══════════════════════════════════════════════════════════════════

witness = {
    "computation": "electron-proton-skein-weight",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "description": (
        "Computation of C_geom from the Skein evaluation of the "
        "electron-proton Hopf link. C_geom = tanh(ln q) / α where "
        "α = 1/137.036 is the fine structure constant."
    ),
    "q": q,
    "target": {
        "C_geom": tanh_ln_q / (1.0 / 137.036),
        "alpha": 1.0 / 137.036,
    },
    "q_dependent_exact": {
        "tanh_ln_q": tanh_ln_q,
        "note": "This is the EM/strong ratio, exact from q alone.",
    },
    "jones_polynomials": {
        "J_unknot": J_unknot,
        "J_trefoil": J_trefoil,
        "J_mirror_trefoil": J_mirror_trefoil,
        "J_figure_eight": J_figure_eight,
        "J_hopf": J_hopf,
    },
    "quantum_integers": {
        "[2]_q": dim_fund,
        "[3]_q": dim_adj,
        "[5]_q": q_int(5),
        "[7]_q": seven_q,
    },
    "formula_candidates": results,
    "status": (
        "OPEN — the correct formula for C_geom requires the "
        "Reshetikhin-Turaev invariant of the satellite link "
        "Hopf(T_{2,3}, B_3). Multiple q-integer formulas are "
        "tested above; the correct one must come from the TQFT "
        "evaluation, not numerology."
    ),
    "required_tools": [
        "SageMath with QuantumKnotInvariants (colored Jones)",
        "SnapPy for link diagram of Hopf(trefoil, Borromean)",
        "Direct Reshetikhin-Turaev evaluation",
    ],
}

out_path = Path(__file__).parent / "electron-proton-skein-weight.witness.json"
with open(out_path, "w") as f:
    json.dump(witness, f, indent=2)

print(f"Witness written to {out_path}")
print(f"\nC_geom target = {tanh_ln_q / (1.0/137.036):.4f}")
print(f"tanh(ln q) = {tanh_ln_q:.6f}")
print(f"\nFormula candidates:")
for name, r in sorted(results.items(), key=lambda x: x[1]["error_pct"]):
    print(f"  {name:40s} = {r['value']:8.4f}  →  1/α = {r['1/alpha']:8.2f}  "
          f"(error {r['error_pct']:5.1f}%)")
