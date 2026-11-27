import QOU.Transcendental.MassTheory.AlphaEmTwoLoopBlochSchwinger
import Mathlib.Analysis.PSeries

/-!
# What the Form C conditional (`AlphaEmTwoLoopBlochSchwingerClass`) actually asserts

`AlphaEmTwoLoopBlochSchwingerClass q δ α` is the carrier of the "Form C" two-loop
Bloch-`B₃` reading of `1/α_EM` (audit
`docs/audits/2026-11-24-alpha-em-two-loop-bloch-schwinger-l4t2-9y43.md`, candidate
`C1`, quoted there at `−0.16σ` against CODATA 2022). Its prose says `δ` is the
weight-3 defect `Δ_{B₃}(q) = ζ(3) − Li₃(q⁻²)`. **The class does not say that:**
`δ` is a free real parameter, constrained only by `0 ≤ δ`.

This file proves that, as a consequence, the class is equivalent to a *formula
for `δ` in terms of `α`* (`class_iff`): for given `q > 1` and `α > 0`, exactly one
`δ` satisfies it, namely `deltaReq q α`, and it does whenever that number is
`≥ 0` (`class_of_deltaReq_nonneg`). So the class is a one-parameter envelope that
any `α` in range satisfies by choosing `δ`; it does not encode the Form C claim.
The Form C claim is the identification `δ = ζ(3) − Li₃(q⁻²)`, which no Lean
declaration currently states.

Nothing here is a statement about measured `α`; `α` is a real variable.
-/

set_option autoImplicit false

namespace QOU.Archimedean
namespace AlphaEmFormCConditionalContent

open QOU.QInteger (qIntBal)
open QOU.Archimedean.BringSchwingerNormalizationDerivation (habiroNorm hHecke)
open QOU.Archimedean.AlphaEmTwoLoopBlochSchwinger

/-- The part of the fixed-point equation that does not involve `δ`. -/
noncomputable def restTerm (q α : ℝ) : ℝ :=
  (q * qIntBal q 9 * qIntBal q 10 + (2 * 4) / bringSurfaceArea) +
    α * habiroNorm q * (1 - (hHecke q) ^ 2 * α)

/-- The unique `δ` compatible with a given `(q, α)`. -/
noncomputable def deltaReq (q α : ℝ) : ℝ :=
  (Real.pi * firstBetti 4 / habiroNorm q) * ((1 / α - restTerm q α) / α ^ 2)

theorem habiroNorm_pos {q : ℝ} (hq : 0 < q) : 0 < habiroNorm q := by
  unfold habiroNorm
  have : 0 < q⁻¹ := inv_pos.2 hq
  positivity

theorem firstBetti_four_pos : 0 < firstBetti 4 := by
  unfold firstBetti; norm_num

/-- The fixed-point equation pins `δ`: it holds iff `δ = deltaReq q α`. -/
theorem fixedPoint_iff_delta {q δ α : ℝ} (hq : 0 < q) (hα : α ≠ 0) :
    IsTwoLoopBringFixedPoint (q * qIntBal q 9 * qIntBal q 10) 4 q ((hHecke q) ^ 2)
        (habiroNorm q * (δ / (Real.pi * firstBetti 4))) α ↔
      δ = deltaReq q α := by
  have hH : habiroNorm q ≠ 0 := (habiroNorm_pos hq).ne'
  have hb : Real.pi * firstBetti 4 ≠ 0 :=
    (mul_pos Real.pi_pos firstBetti_four_pos).ne'
  have hα2 : α ^ 2 ≠ 0 := pow_ne_zero _ hα
  have hb4 : firstBetti 4 ≠ 0 := firstBetti_four_pos.ne'
  have hπ : Real.pi ≠ 0 := Real.pi_ne_zero
  unfold IsTwoLoopBringFixedPoint deltaReq
  rw [show (q * qIntBal q 9 * qIntBal q 10 + (2 * 4) / bringSurfaceArea) +
        α * habiroNorm q * (1 - (hHecke q) ^ 2 * α) = restTerm q α from rfl]
  constructor
  · intro h
    rw [h]
    field_simp
    ring
  · intro h
    rw [h]
    field_simp
    ring

/-- **The class is a formula for `δ`.** -/
theorem class_iff (q δ α : ℝ) :
    AlphaEmTwoLoopBlochSchwingerClass q δ α ↔
      1 < q ∧ 0 ≤ δ ∧ 0 < α ∧ δ = deltaReq q α := by
  constructor
  · intro h
    have hq : 0 < q := lt_trans one_pos h.one_lt_q
    exact ⟨h.one_lt_q, h.delta_B3_nonneg, h.alpha_pos,
      (fixedPoint_iff_delta hq h.alpha_pos.ne').1 h.two_loop_self_consistent⟩
  · rintro ⟨hq1, hδ, hα, hdef⟩
    have hq : 0 < q := lt_trans one_pos hq1
    exact ⟨hq1, hδ, hα, (fixedPoint_iff_delta hq hα.ne').2 hdef⟩

/-- **Any `α` in range satisfies the class**, with `δ := deltaReq q α`. -/
theorem class_of_deltaReq_nonneg {q α : ℝ} (hq : 1 < q) (hα : 0 < α)
    (hδ : 0 ≤ deltaReq q α) : AlphaEmTwoLoopBlochSchwingerClass q (deltaReq q α) α :=
  (class_iff q _ α).2 ⟨hq, hδ, hα, rfl⟩

/-- At fixed `(q, α)`, the class determines `δ` uniquely. -/
theorem delta_unique {q δ δ' α : ℝ} (h : AlphaEmTwoLoopBlochSchwingerClass q δ α)
    (h' : AlphaEmTwoLoopBlochSchwingerClass q δ' α) : δ = δ' :=
  ((class_iff q δ α).1 h).2.2.2.trans ((class_iff q δ' α).1 h').2.2.2.symm


/-! ## Pinning `δ` to the weight-3 defect

`deltaB3 q = Σ_{n ≥ 1} (1 − q^{−2n}) / n³`, which is `ζ(3) − Li₃(q⁻²)` written as one
series. Every term is `≥ 0` for `q ≥ 1`, so the defect is `≥ 0` without any
analysis, and it vanishes at `q = 1`. -/

/-- The weight-3 defect `ζ(3) − Li₃(q⁻²)` as a single series. -/
noncomputable def deltaB3 (q : ℝ) : ℝ :=
  ∑' n : ℕ, (1 - (q ^ 2)⁻¹ ^ (n + 1)) / ((n + 1 : ℕ) : ℝ) ^ 3

theorem deltaB3_term_nonneg {q : ℝ} (hq : 1 ≤ q) (n : ℕ) :
    0 ≤ (1 - (q ^ 2)⁻¹ ^ (n + 1)) / ((n + 1 : ℕ) : ℝ) ^ 3 := by
  apply div_nonneg _ (by positivity)
  have h1 : (q ^ 2)⁻¹ ≤ 1 := inv_le_one_of_one_le₀ (one_le_pow₀ hq)
  have h0 : 0 ≤ (q ^ 2)⁻¹ := by positivity
  have : (q ^ 2)⁻¹ ^ (n + 1) ≤ 1 := pow_le_one₀ h0 h1
  linarith

theorem deltaB3_summable {q : ℝ} (hq : 1 ≤ q) :
    Summable fun n : ℕ => (1 - (q ^ 2)⁻¹ ^ (n + 1)) / ((n + 1 : ℕ) : ℝ) ^ 3 := by
  have hs : Summable fun n : ℕ => 1 / ((n + 1 : ℕ) : ℝ) ^ 3 :=
    (summable_nat_add_iff 1).2 (Real.summable_one_div_nat_pow.2 (by norm_num))
  refine hs.of_nonneg_of_le (deltaB3_term_nonneg hq) (fun n => ?_)
  apply div_le_div_of_nonneg_right _ (by positivity)
  have : 0 ≤ (q ^ 2)⁻¹ ^ (n + 1) := by positivity
  linarith

theorem deltaB3_nonneg {q : ℝ} (hq : 1 ≤ q) : 0 ≤ deltaB3 q :=
  tsum_nonneg (deltaB3_term_nonneg hq)

theorem deltaB3_one : deltaB3 1 = 0 := by
  simp [deltaB3]

/-- **Form C, pinned.** The carrier with `δ` *defined* as the weight-3 defect rather
than supplied. By `class_iff` this is the single equation
`deltaB3 q = deltaReq q α`; that equation is the content of the Form C reading, and
it is open (no derivation of the two-loop coefficient is in the corpus). -/
def FormCPinned (q α : ℝ) : Prop :=
  AlphaEmTwoLoopBlochSchwingerClass q (deltaB3 q) α

theorem formCPinned_iff {q α : ℝ} (hq : 1 < q) (hα : 0 < α) :
    FormCPinned q α ↔ deltaB3 q = deltaReq q α := by
  unfold FormCPinned
  rw [class_iff]
  exact ⟨fun h => h.2.2.2, fun h => ⟨hq, deltaB3_nonneg hq.le, hα, h⟩⟩

end AlphaEmFormCConditionalContent
end QOU.Archimedean
