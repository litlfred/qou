/-
Copyright (c) 2026 Quantum Observable Universe Collaboration. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Collaboration
-/
import QOU.MassEndomorphism.QBetaToroidalHarmonicsBasis

set_option autoImplicit false

/-!
# Toroidal Harmonics Global Basis (`prop:qbeta-toroidal-harmonics-basis`)

Companion chapter specialization forwarding to the unconditional proofs in
`QOU.MassEndomorphism.QBetaToroidalHarmonicsBasis`:
- `toroidalCentrifugalCoeff_zero_iff_and_principal_potential` (`m² - 1/4 = 0 ↔ m = ±1/2`),
- `principalToroidalMode_solves_exact_ode` (`F''(η) - V_tor(n, 1/2, η) F(η) = 0`),
- `toroidal_regular_turning_point` (simple Liouville–Green turning point),
- `parabolic_cylinder_order_gap_and_c4_iff` (`c_1 = 0` order-gap and `c_4 = 2 ↔ C = -22`).
-/

namespace QOU.MassEndomorphism.QBetaToroidalHarmonicsBasisSibling

open QOU.MassEndomorphism.QBetaToroidalHarmonicsBasis

/-- Combined specialization witness for `prop:qbeta-toroidal-harmonics-basis`:
1. The singular $1/\sinh^2\eta$ barrier vanishes if and only if $m = \pm\frac{1}{2}$,
2. At $(c_1, c_2, c_3) = (0, -1, -2)$, the Parabolic Cylinder jet residual at $u^2$ under
   $(A, B) = (2, 12)$ vanishes with $c_4 = 2$ if and only if $C = -22$. -/
theorem qbeta_toroidal_harmonics_basis_summary (m η : ℝ) (C_param c₄ : ℚ)
    (hres : (parabolicCylinderOp 2 12 C_param (weberJetPoly 0 (-1) (-2) c₄)).coeff 2 = 0) :
    (toroidalCentrifugalCoeff m = 0 ↔ m = 1 / 2 ∨ m = -1 / 2) ∧
      toroidalPotential (1 / 2) (1 / 2) η = 0 ∧
      (c₄ = 2 ↔ C_param = -22) := by
  have htor := toroidalCentrifugalCoeff_zero_iff_and_principal_potential (1 / 2) m η
  have hpot : toroidalPotential (1 / 2) (1 / 2) η = 0 := by
    rw [htor.2.1]
    norm_num
  exact ⟨htor.1, hpot, parabolic_cylinder_order_gap_and_c4_iff.2.2.2.2 C_param c₄ hres⟩

end QOU.MassEndomorphism.QBetaToroidalHarmonicsBasisSibling
