/-!
# QOU.Braiding.SkeinBindingLagrangian — Nuclear binding from canonical action

The Skein binding Lagrangian is S_q evaluated on the multi-nucleon
Hopf link: L_bind = L_vol - L_surf - L_Coul - L_Pauli + L_pair.

LaTeX label: `def:skein-binding-lagrangian`

## References
- [manuscript] §4/skein-binding-lagrangian
-/

import Mathlib.Data.Real.Basic

namespace QOU.Braiding

/-- The five-term Skein binding Lagrangian for a nucleus (p, n). -/
-- Ref: [manuscript] §4/skein-binding-lagrangian
structure SkeinBindingLagrangian where
  /-- Number of protons. -/
  p : ℕ
  /-- Number of neutrons. -/
  n : ℕ
  /-- Substrate parameter q. -/
  q : ℝ
  /-- q > 1. -/
  q_gt_one : 1 < q
  /-- Volume scale λ_V. -/
  lambda_V : ℝ
  /-- Surface scale λ_S. -/
  lambda_S : ℝ
  /-- Coulomb scale λ_C. -/
  lambda_C : ℝ
  /-- Pauli asymmetry coefficient a_A. -/
  a_A : ℝ
  /-- Mass number. -/
  A : ℕ := p + n

/-- Volume binding: (q + q⁻¹)/2 · λ_V · A. -/
noncomputable def SkeinBindingLagrangian.L_vol (L : SkeinBindingLagrangian) : ℝ :=
  (L.q + 1/L.q) / 2 * L.lambda_V * L.A

/-- Coulomb repulsion: (q - q⁻¹) · λ_C · p(p-1)/A^{1/3}. -/
noncomputable def SkeinBindingLagrangian.L_Coul (L : SkeinBindingLagrangian) : ℝ :=
  (L.q - 1/L.q) * L.lambda_C * (L.p * (L.p - 1)) / (L.A : ℝ)^(1/3 : ℝ)

/-- Pauli asymmetry: a_A · (n - p)²/(4A). -/
noncomputable def SkeinBindingLagrangian.L_Pauli (L : SkeinBindingLagrangian) : ℝ :=
  L.a_A * ((L.n : ℝ) - L.p)^2 / (4 * L.A)

end QOU.Braiding
