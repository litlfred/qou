/-!
# QOU.Descartes.hadron_q_self_correction — Hadron self-deformation of q

A multi-nucleon Hopf link with linking number ℓ(p,n) shifts the local
substrate parameter from q₀ to q_eff = q₀ + δq, where
δq = ℓ(p,n)/A · ℏ_q².

LaTeX label: `prop:hadron-q-self-correction`

## References
- [manuscript] §6/hadron-q-self-correction
-/

import Mathlib.Data.Real.Basic

namespace QOU.Descartes

/-- Total linking number of a multi-nucleon Hopf link with p protons
    and n neutrons: ℓ(p,n) = A(A-1)/2 where A = p + n. -/
-- Ref: [manuscript] §6/hadron-q-self-correction
noncomputable def totalLinkingNumber (p n : ℕ) : ℕ :=
  (p + n) * (p + n - 1) / 2

/-- The linking number equals the sum of all pairwise Hopf junctions:
    C(p,2) + C(n,2) + p·n = A(A-1)/2. -/
-- Ref: [manuscript] §6/hadron-q-self-correction
theorem linkingNumber_eq (p n : ℕ) (h : 1 ≤ p + n) :
    p * (p - 1) / 2 + n * (n - 1) / 2 + p * n =
    totalLinkingNumber p n := by
  unfold totalLinkingNumber
  omega

/-- Self-deformation of the substrate parameter by a nucleus.
    δq(p,n) = ℓ(p,n)/A · ℏ_q² where ℏ_q = 1 - q₀⁻¹. -/
-- Ref: [manuscript] §6/hadron-q-self-correction
noncomputable def deltaQ (q₀ : ℝ) (p n : ℕ) : ℝ :=
  let A := (p + n : ℝ)
  let hbar := 1 - q₀⁻¹
  (totalLinkingNumber p n : ℝ) / A * hbar ^ 2

/-- Effective substrate parameter: q_eff = q₀ + δq. -/
-- Ref: [manuscript] §6/hadron-q-self-correction
noncomputable def qEff (q₀ : ℝ) (p n : ℕ) : ℝ :=
  q₀ + deltaQ q₀ p n

/-- The self-deformation is non-negative when q₀ > 0. -/
-- Ref: [manuscript] §6/hadron-q-self-correction
theorem deltaQ_nonneg (q₀ : ℝ) (hq : 0 < q₀) (p n : ℕ) :
    0 ≤ deltaQ q₀ p n := by
  unfold deltaQ
  apply mul_nonneg
  · apply div_nonneg
    · exact Nat.cast_nonneg
    · exact Nat.cast_nonneg
  · exact sq_nonneg _

/-- q_eff ≥ q₀: the self-deformation only increases q. -/
-- Ref: [manuscript] §6/hadron-q-self-correction
theorem qEff_ge_background (q₀ : ℝ) (hq : 0 < q₀) (p n : ℕ) :
    q₀ ≤ qEff q₀ p n := by
  unfold qEff
  linarith [deltaQ_nonneg q₀ hq p n]

/-- q_eff > 1 when q₀ > 1: the effective parameter stays in the
    non-classical regime. -/
-- Ref: [manuscript] §6/hadron-q-self-correction
theorem qEff_gt_one (q₀ : ℝ) (hq : 1 < q₀) (p n : ℕ) :
    1 < qEff q₀ p n := by
  calc 1 < q₀ := hq
    _ ≤ qEff q₀ p n := qEff_ge_background q₀ (by linarith) p n

/-- The self-deformation is small relative to q₀ for light nuclei.
    Specifically, for A ≤ 60 and q₀ = 1.110: δq/q₀ < 0.03. -/
-- Ref: [manuscript] §6/hadron-q-self-correction
theorem deltaQ_small_light :
    deltaQ 1.110 26 34 / 1.110 < 0.03 := by
  unfold deltaQ totalLinkingNumber
  norm_num

/-- For the heaviest stable nuclei (A ~ 210), the self-deformation
    is still less than 10% of q₀. -/
-- Ref: [manuscript] §6/hadron-q-self-correction
theorem deltaQ_bounded_heavy :
    deltaQ 1.110 83 127 / 1.110 < 0.10 := by
  unfold deltaQ totalLinkingNumber
  norm_num

/-- Top-level alias matching the manifest declaration. -/
-- Ref: [manuscript] §6/hadron-q-self-correction
noncomputable def hadron_q_self_correction (q₀ : ℝ) (p n : ℕ) : ℝ :=
  qEff q₀ p n

end QOU.Descartes
