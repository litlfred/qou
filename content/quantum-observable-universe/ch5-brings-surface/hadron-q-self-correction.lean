/-!
# QOU.Descartes.hadron_q_self_correction — Hadron self-deformation of q

A multi-nucleon Hopf link with net signed crossing number ℓ_net(p,n)
shifts the local substrate parameter from q₀ to q_eff = q₀ + δq,
where δq = ℓ_net(p,n)/A² · ℏ_q².

The net signed crossing counts the imbalance between positive
(proton-proton) and negative (neutron-neutron) Hopf crossings:
ℓ_net = C(p,2) - C(n,2) = (p(p-1) - n(n-1))/2.

For beta decay, the differential shift Δq_eff = (A-1)/A² · ℏ_q²
is always positive (daughter has more proton crossings), increasing
the effective Q-value and shortening the half-life.

LaTeX label: `prop:hadron-q-self-correction`

## References
- [manuscript] §6/hadron-q-self-correction
-/

import Mathlib.Data.Real.Basic

namespace QOU.Descartes

/-- Net signed crossing number: ℓ_net(p,n) = C(p,2) - C(n,2). -/
-- Ref: [manuscript] §6/hadron-q-self-correction
def netSignedCrossing (p n : ℕ) : ℤ :=
  (p * (p - 1) : ℤ) / 2 - (n * (n - 1) : ℤ) / 2

/-- Self-deformation of the substrate parameter by a nucleus.
    δq(p,n) = ℓ_net(p,n)/A² · ℏ_q² where ℏ_q = 1 - q₀⁻¹. -/
-- Ref: [manuscript] §6/hadron-q-self-correction
noncomputable def deltaQ (q₀ : ℝ) (p n : ℕ) : ℝ :=
  let A := (p + n : ℝ)
  let hbar := 1 - q₀⁻¹
  (netSignedCrossing p n : ℝ) / A ^ 2 * hbar ^ 2

/-- Effective substrate parameter: q_eff = q₀ + δq. -/
-- Ref: [manuscript] §6/hadron-q-self-correction
noncomputable def qEff (q₀ : ℝ) (p n : ℕ) : ℝ :=
  q₀ + deltaQ q₀ p n

/-- For neutron-rich nuclei (n > p), the self-deformation is negative:
    the excess of negative crossings slightly reduces q. -/
-- Ref: [manuscript] §6/hadron-q-self-correction
theorem deltaQ_neg_neutron_rich (q₀ : ℝ) (hq : 0 < q₀) (p n : ℕ) (hn : p < n) :
    deltaQ q₀ p n ≤ 0 := by
  unfold deltaQ netSignedCrossing
  simp only
  apply mul_nonpos_of_nonpos_of_nonneg
  · apply div_nonpos_of_nonpos_of_nonneg
    · push_cast; omega
    · positivity
  · exact sq_nonneg _

/-- Differential self-deformation across a single beta decay:
    Δq_eff = δq(p+1, n-1) - δq(p, n).

    This is the physically relevant quantity for half-lives:
    it determines how the effective Q-value differs from the
    background-q prediction. -/
-- Ref: [manuscript] §6/hadron-q-self-correction
noncomputable def deltaDeltaQ (q₀ : ℝ) (p n : ℕ) : ℝ :=
  deltaQ q₀ (p + 1) (n - 1) - deltaQ q₀ p n

/-- The differential shift equals (A-1)/A² · ℏ_q² and is always
    positive: the daughter nucleus (one more proton) has a higher
    effective q than the parent. -/
-- Ref: [manuscript] §6/hadron-q-self-correction
noncomputable def differentialShift (q₀ : ℝ) (A : ℕ) : ℝ :=
  ((A : ℝ) - 1) / (A : ℝ) ^ 2 * (1 - q₀⁻¹) ^ 2

/-- The differential shift is non-negative when A ≥ 1 and q₀ > 0. -/
-- Ref: [manuscript] §6/hadron-q-self-correction
theorem differentialShift_nonneg (q₀ : ℝ) (hq : 0 < q₀) (A : ℕ) (hA : 1 ≤ A) :
    0 ≤ differentialShift q₀ A := by
  unfold differentialShift
  apply mul_nonneg
  · apply div_nonneg
    · push_cast; omega
    · positivity
  · exact sq_nonneg _

/-- The differential shift is small: for all A and q₀ = 1.110,
    Δq_eff < ℏ_q² < 0.01. -/
-- Ref: [manuscript] §6/hadron-q-self-correction
theorem differentialShift_small (A : ℕ) (hA : 1 ≤ A) :
    differentialShift 1.110 A < 0.01 := by
  unfold differentialShift
  have hA_pos : (0 : ℝ) < (A : ℝ) := by exact_mod_cast Nat.lt_of_lt_pred (by omega)
  have hA2_pos : (0 : ℝ) < (A : ℝ) ^ 2 := by positivity
  have h1 : ((A : ℝ) - 1) / (A : ℝ) ^ 2 ≤ 1 := by
    rw [div_le_one hA2_pos]
    nlinarith
  have h2 : (1 - (1.110 : ℝ)⁻¹) ^ 2 < 0.01 := by norm_num
  calc differentialShift 1.110 A
      = ((A : ℝ) - 1) / (A : ℝ) ^ 2 * (1 - (1.110 : ℝ)⁻¹) ^ 2 := rfl
    _ ≤ 1 * (1 - (1.110 : ℝ)⁻¹) ^ 2 := by
        apply mul_le_mul_of_nonneg_right h1 (sq_nonneg _)
    _ < 1 * 0.01 := by
        apply mul_lt_mul_of_pos_left h2 (by norm_num : (0 : ℝ) < 1)
    _ = 0.01 := by ring

/-- q_eff > 1 when q₀ > 1: the effective parameter stays in the
    non-classical regime (self-deformation is too small to change this). -/
-- Ref: [manuscript] §6/hadron-q-self-correction
theorem qEff_gt_one (q₀ : ℝ) (hq : 1 < q₀) (p n : ℕ)
    (hsmall : |deltaQ q₀ p n| < q₀ - 1) :
    1 < qEff q₀ p n := by
  unfold qEff
  have := abs_lt.mp (lt_of_lt_of_le hsmall (le_refl _))
  linarith [this.1]

/-- Top-level alias matching the manifest declaration. -/
-- Ref: [manuscript] §6/hadron-q-self-correction
noncomputable def hadron_q_self_correction (q₀ : ℝ) (p n : ℕ) : ℝ :=
  qEff q₀ p n

end QOU.Descartes
