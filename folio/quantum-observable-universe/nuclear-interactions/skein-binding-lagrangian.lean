import Mathlib.Analysis.SpecialFunctions.Pow.Real


/-!
# QOU.Braiding.SkeinBindingLagrangian — Nuclear binding from canonical action

The Skein binding Lagrangian is S_q evaluated on the multi-nucleon
Hopf link: L_bind = L_vol - L_surf - L_Coul - L_Pauli + L_pair.

LaTeX label: `def:skein-binding-lagrangian`

## References
- [leitner2026] §4/skein-binding-lagrangian

**Base ring**: the individual binding terms use rational coefficients
(`/2`, `/4`) and real exponents on the mass number (`A^{2/3}`, `A^{1/3}`),
together with the substrate inverse `q⁻¹`.  These are archimedean
constructs, so the Lagrangian lives on the **observable side of the
substrate→archimedean wall**: the q-parameter is the real evaluation
`q ↦ q₀` and the terms are real-valued (§7c base-ring convention —
fractional powers and rational divisors force `ℝ`).
-/

namespace QOU.Braiding

open scoped Real

/-- The five-term Skein binding Lagrangian for a nucleus (p, n).

    The substrate parameter is carried as its archimedean evaluation
    `q : ℝ` with `q₀ > 1` (the `1 < q` hypothesis is recorded on the
    structure for the order-dependent terms). -/
-- Ref: [leitner2026] §4/skein-binding-lagrangian
structure SkeinBindingLagrangian where
  /-- Number of protons. -/
  p : ℕ
  /-- Number of neutrons. -/
  n : ℕ
  /-- Substrate parameter q (archimedean evaluation). -/
  q : ℝ
  /-- q > 1 (substrate regime). -/
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
  (L.q + L.q⁻¹) / 2 * L.lambda_V * L.A

/-- Surface correction: (q + q⁻¹)/2 · λ_S · A^{2/3}. -/
noncomputable def SkeinBindingLagrangian.L_surf (L : SkeinBindingLagrangian) : ℝ :=
  (L.q + L.q⁻¹) / 2 * L.lambda_S * (L.A : ℝ) ^ (2 / 3 : ℝ)

/-- Coulomb repulsion: (q - q⁻¹) · λ_C · p(p-1)/A^{1/3}. -/
noncomputable def SkeinBindingLagrangian.L_Coul (L : SkeinBindingLagrangian) : ℝ :=
  (L.q - L.q⁻¹) * L.lambda_C * (L.p * (L.p - 1) : ℝ) / (L.A : ℝ) ^ (1 / 3 : ℝ)

/-- Pauli asymmetry: a_A · (n - p)²/(4A). -/
noncomputable def SkeinBindingLagrangian.L_Pauli (L : SkeinBindingLagrangian) : ℝ :=
  L.a_A * ((L.n : ℝ) - L.p) ^ 2 / (4 * L.A)

/-- The volume binding is non-negative when the volume scale is
    non-negative: the average Skein weight `(q + q⁻¹)/2` is positive in
    the substrate regime `q > 1`, and `A ≥ 0`. -/
-- Ref: [leitner2026] §4/skein-binding-lagrangian
theorem SkeinBindingLagrangian.L_vol_nonneg (L : SkeinBindingLagrangian)
    (hV : 0 ≤ L.lambda_V) : 0 ≤ L.L_vol := by
  have hq : (0 : ℝ) < L.q := lt_trans one_pos L.q_gt_one
  have hqi : (0 : ℝ) < L.q⁻¹ := inv_pos.mpr hq
  unfold SkeinBindingLagrangian.L_vol
  have hweight : 0 ≤ (L.q + L.q⁻¹) / 2 := by positivity
  have hA : (0 : ℝ) ≤ (L.A : ℝ) := Nat.cast_nonneg _
  positivity

end QOU.Braiding
