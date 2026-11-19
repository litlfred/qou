/-
Copyright (c) 2026 Carl Leitner. All rights reserved.
Released under MIT license. Authors: Claude (Anthropic).

# Closed form for the canonical Markov trace of σ_1² (Hopf+ braid)

Proves under Convention D (`z_D = q³ / (q² + 1)`):

  tr_M(σ_1²) = (q - q⁻¹) · z_D + 1
             = (q⁴ + 1) / (q² + 1)
             = q · [2]_{q²} / [2]_q
             = 1 + q² (q² - 1) / (q² + 1)

for every n ≥ 2, where tr_M is the canonical Markov trace on the
Iwahori-Hecke algebra H_n(q) with quadratic relation
`σ_1² = (q - q⁻¹) σ_1 + 1`.

Ref: [jones1987] https://www.jstor.org/stable/1971403
Ref: [wenzl1988] https://doi.org/10.1007/BF01393699
-/
import Mathlib.Algebra.Field.Defs
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Tactic
import QOU.Braiding.HnMarkovTrace

namespace QOU.Braiding

/-! ## Generic field-level derivation from the Hecke quadratic relation (Convention D) -/

section FieldLevel

variable {K : Type*} [Field K]

/-- Balanced quantum integer `[2]_q = q + q⁻¹`. -/
def qInt2Hopf (q : K) : K := q + q⁻¹

/-- Balanced quantum integer at `q²`: `[2]_{q²} = q² + (q⁻¹)²`. -/
def qInt2SqHopf (q : K) : K := q ^ 2 + (q⁻¹) ^ 2

/-- Hecke quadratic parameter `h(q) = q - q⁻¹`. -/
def heckeHHopf (q : K) : K := q - q⁻¹

/-- Canonical Markov trace loop parameter under Convention D: `z_D(q) = q³ / (q² + 1)`. -/
def markovZConventionD (q : K) : K := q ^ 3 / (q ^ 2 + 1)

/-- Canonical Markov trace of the positive Hopf braid `σ_1²` under Convention D:
`tr_M(σ_1²) = (q⁴ + 1) / (q² + 1)`. -/
def trMHopfClosedForm (q : K) : K := (q ^ 4 + 1) / (q ^ 2 + 1)

/-- All three displayed forms in `prop:trm-hopf-sigma1-sq-closed-form` hold over any field `K`
for `q ≠ 0` and `q² + 1 ≠ 0`:
1. `(q - q⁻¹) · z_D(q) + 1 = (q⁴ + 1) / (q² + 1)`
2. `(q⁴ + 1) / (q² + 1) = q · [2]_{q²} / [2]_q`
3. `(q⁴ + 1) / (q² + 1) = 1 + q² (q² - 1) / (q² + 1)` -/
theorem trMHopfClosedForm_three_forms (q : K) (hq : q ≠ 0) (hdenom : q ^ 2 + 1 ≠ 0) :
    (q - q⁻¹) * markovZConventionD q + 1 = trMHopfClosedForm q ∧
    trMHopfClosedForm q = q * qInt2SqHopf q / qInt2Hopf q ∧
    trMHopfClosedForm q = 1 + q ^ 2 * (q ^ 2 - 1) / (q ^ 2 + 1) := by
  have hqInt2 : qInt2Hopf q ≠ 0 := by
    unfold qInt2Hopf
    intro h0
    apply hdenom
    have hmul : q * (q + q⁻¹) = q ^ 2 + 1 := by
      calc q * (q + q⁻¹) = q ^ 2 + q * q⁻¹ := by ring
      _ = q ^ 2 + 1 := by rw [mul_inv_cancel₀ hq]
    rw [← hmul, h0, mul_zero]
  refine ⟨?_, ?_, ?_⟩
  · unfold markovZConventionD trMHopfClosedForm
    field_simp
    try ring
  · unfold trMHopfClosedForm qInt2SqHopf qInt2Hopf
    field_simp
    try ring
  · unfold trMHopfClosedForm
    field_simp
    try ring

/-- From the Hecke quadratic relation `σ_1² = (q - q⁻¹) σ_1 + 1`, any `K`-linear functional
`trM : A →ₗ[K] K` on a `K`-algebra `A` satisfying `trM 1 = 1` and `trM σ_1 = z_D(q)`
evaluates on `σ_1²` to `(q - q⁻¹) · z_D(q) + 1 = (q⁴ + 1) / (q² + 1)`. -/
theorem trM_sigma1_sq_from_hecke_quadratic
    {A : Type*} [Ring A] [Algebra K A]
    (trM : A →ₗ[K] K) (sigma1 : A) (q : K)
    (hq : q ≠ 0) (hdenom : q ^ 2 + 1 ≠ 0)
    (hquad : sigma1 ^ 2 = heckeHHopf q • sigma1 + 1)
    (htr1 : trM 1 = 1)
    (htr_sigma1 : trM sigma1 = markovZConventionD q) :
    trM (sigma1 ^ 2) = (q - q⁻¹) * markovZConventionD q + 1 ∧
    trM (sigma1 ^ 2) = trMHopfClosedForm q := by
  have h1 : trM (sigma1 ^ 2) = (q - q⁻¹) * markovZConventionD q + 1 := by
    rw [hquad, map_add, map_smul, smul_eq_mul, htr_sigma1, htr1, heckeHHopf]
  exact ⟨h1, h1.trans (trMHopfClosedForm_three_forms q hq hdenom).1⟩

/-- Polynomial-part decomposition for the `q = 1 + ε` Taylor expansion:
`tr_M(σ_1²) - 1 = (q⁴ - q²) / (q² + 1) = q² - 2 + 2 / (q² + 1)`. -/
theorem trMHopfClosedForm_sub_one_split (q : K) (hdenom : q ^ 2 + 1 ≠ 0) :
    trMHopfClosedForm q - 1 = q ^ 2 - 2 + 2 / (q ^ 2 + 1) := by
  have _ := hdenom
  unfold trMHopfClosedForm
  field_simp
  try ring

end FieldLevel

/-! ## Canonical tower interface over `ℝ` (`q > 1`) -/

/-- Closed-form value of the canonical Markov trace of `σ_1²` in `H_n(q)` under Convention D,
connected to `markovTraceTower_canonical`. -/
class TrMHopfSigma1SqClosedForm (q : ℝ) where
  /-- Hypothesis: `q` is in the Wenzl positivity regime (`q > 1`). -/
  q_gt_one : 1 < q
  /-- Canonical Markov-trace value of `σ_1²` in `H_n(q)` at any `n ≥ 2`. -/
  trM_sigma1_sq : ℝ
  /-- Derivation from the Hecke quadratic relation `σ_1² = (q - q⁻¹) σ_1 + 1` and
  the canonical Convention-D loop parameter `z = q³ / (q² + 1)`. -/
  hecke_quadratic_trace :
    trM_sigma1_sq = (q - q⁻¹) * (markovTraceTower_canonical q q_gt_one).z + 1
  /-- The Convention-D rational closed form: `tr_M(σ_1²) = (q⁴ + 1) / (q² + 1)`. -/
  closed_form :
    trM_sigma1_sq = (q ^ 4 + 1) / (q ^ 2 + 1)

/-- The Convention-D closed form equals the third boxed expression
`1 + q² (q² - 1) / (q² + 1)`. -/
theorem trm_hopf_sigma1_sq_closed_form_simplified (q : ℝ) (_hq : 1 < q)
    [inst : TrMHopfSigma1SqClosedForm q] :
    inst.trM_sigma1_sq = 1 + q ^ 2 * (q ^ 2 - 1) / (q ^ 2 + 1) := by
  have hq_pos : 0 < q := lt_trans zero_lt_one inst.q_gt_one
  have hdenom : q ^ 2 + 1 ≠ 0 := by positivity
  rw [inst.closed_form]
  exact (trMHopfClosedForm_three_forms q (ne_of_gt hq_pos) hdenom).2.2

/-- The Convention-D closed form equals the quantum-integer ratio
`q · [2]_{q²} / [2]_q = q * (q² + (q⁻¹)²) / (q + q⁻¹)`. -/
theorem trm_hopf_sigma1_sq_eq_qInt_ratio (q : ℝ) (_hq : 1 < q)
    [inst : TrMHopfSigma1SqClosedForm q] :
    inst.trM_sigma1_sq = q * qInt2SqHopf q / qInt2Hopf q := by
  have hq_pos : 0 < q := lt_trans zero_lt_one inst.q_gt_one
  have hdenom : q ^ 2 + 1 ≠ 0 := by positivity
  rw [inst.closed_form]
  exact (trMHopfClosedForm_three_forms q (ne_of_gt hq_pos) hdenom).2.1

/-- Direct agreement between `TrMHopfSigma1SqClosedForm.trM_sigma1_sq` and
`(markovTraceTower_canonical q hq).trM_sigma1_sq n` at every strand count `n`. -/
theorem trm_hopf_sigma1_sq_eq_canonical_tower
    (q : ℝ) (hq : 1 < q) [inst : TrMHopfSigma1SqClosedForm q] (n : Nat) :
    inst.trM_sigma1_sq = (markovTraceTower_canonical q hq).trM_sigma1_sq n := by
  rw [inst.closed_form]
  rfl

/-- Markov-invariance of `tr_M(σ_1²)` across `H_n` for `n ≥ 2`. -/
theorem trm_hopf_sigma1_sq_markov_invariant
    (q : ℝ) (_hq : 1 < q) [MarkovTraceTower q]
    (m n : Nat) (hm : 2 ≤ m) (hn : 2 ≤ n) :
    MarkovTraceTower.trM_sigma1_sq (q := q) m =
      MarkovTraceTower.trM_sigma1_sq (q := q) n :=
  MarkovTraceTower.trM_sigma1_sq_stabilises (q := q) m n hm hn

/-- Canonical concrete instance of `TrMHopfSigma1SqClosedForm q` for `q > 1` under Convention D. -/
noncomputable instance trMHopfSigma1SqClosedForm_canonical
    (q : ℝ) (hq : 1 < q) : TrMHopfSigma1SqClosedForm q where
  q_gt_one := hq
  trM_sigma1_sq := (q ^ 4 + 1) / (q ^ 2 + 1)
  hecke_quadratic_trace := by
    have hq_pos : 0 < q := lt_trans zero_lt_one hq
    have hq_ne : q ≠ 0 := ne_of_gt hq_pos
    have hdenom : q ^ 2 + 1 ≠ 0 := by positivity
    change (q ^ 4 + 1) / (q ^ 2 + 1) = (q - q⁻¹) * (q ^ 3 / (q ^ 2 + 1)) + 1
    exact ((trMHopfClosedForm_three_forms q hq_ne hdenom).1).symm
  closed_form := rfl

end QOU.Braiding
