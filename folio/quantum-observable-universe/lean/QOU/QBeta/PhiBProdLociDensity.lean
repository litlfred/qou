import QOU.QBeta.PhiBProdUniquenessComplete
import QOU.QBeta.PhiBProdDivisor
import QOU.Common.PeriodicDense
import Mathlib.Analysis.SpecialFunctions.Complex.Circle

/-!
# The periodicity loci are dense (G5 specialization: discharges the loci-density inputs)

Discharges the last carried inputs of
`PhiBProdUniquenessComplete.phiBProd_uniqueUpToScalar` — the density of the two periodicity
loci `S₀, S₁` — for the concrete substrate `phiBProd`, giving a `phiBProd` uniqueness statement
whose **only** remaining hypothesis is the honest regularity `MeromorphicNFOn Φ₁`.

The loci are taken as the explicit membership sets, so `hmem₀`/`hmem₁` are definitional. Their
density is `dense_compl_of_countable` applied to the **total bad set** — a finite union of the
prefactor lattice (`Common.dense_*Pole_compl`'s pattern) and `phiBProd`'s zeros (and one shift),
each **countable**: `phiBProd`'s zeros inject into `{num = 0} ∪ {den = 0}`, and each product's
zeros are a countable union over `k` of the factor `ℤ`-lattices.

Verified `lean`-direct against the merged `phiBProd` chain + `Common.PeriodicDense`. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-26-faddeev-keystone-7xvy-canonical-arc.md
-/

open Complex Set
open QOU.MathlibExt.PhiBProd
open QOU.MathlibExt.FaddeevQuantumDilogarithm
open QOU.QBeta.PhiBProdProductConvergence
open QOU.QBeta.PhiBProdDivisor

namespace QOU.QBeta.PhiBProdLociDensity

/-- Each numerator factor's zero set is countable (a discrete `ℤ`-lattice). -/
theorem numFactor_zeros_countable (b : ℂ) (hb : b ≠ 0) (k : ℕ) :
    {z : ℂ | numFactor b z k = 0}.Countable := by
  have h2pib : (2 : ℂ) * (Real.pi : ℂ) * b ≠ 0 :=
    mul_ne_zero (mul_ne_zero two_ne_zero (by exact_mod_cast Real.pi_ne_zero)) hb
  refine (Set.countable_range (fun n : ℤ =>
    ((Real.pi : ℂ) * I + (n : ℂ) * (2 * (Real.pi : ℂ) * I)
      - (Real.pi : ℂ) * I * b ^ 2 * (2 * (k : ℂ) + 1)) / (2 * (Real.pi : ℂ) * b))).mono ?_
  intro z hz
  simp only [Set.mem_setOf_eq, numFactor] at hz
  have hexp : Complex.exp ((Real.pi : ℂ) * I * b ^ 2 * (2 * (k : ℂ) + 1)
      + 2 * (Real.pi : ℂ) * b * z) = -1 := by linear_combination hz
  rw [← Complex.exp_pi_mul_I, Complex.exp_eq_exp_iff_exists_int] at hexp
  obtain ⟨n, hn⟩ := hexp
  exact ⟨n, by rw [div_eq_iff h2pib]; linear_combination -hn⟩

/-- Each denominator factor's zero set is countable. -/
theorem denFactor_zeros_countable (b : ℂ) (hb : b ≠ 0) (k : ℕ) :
    {z : ℂ | denFactor b z k = 0}.Countable := by
  have hb2 : b ^ 2 ≠ 0 := pow_ne_zero 2 hb
  have h2pi : (2 : ℂ) * (Real.pi : ℂ) ≠ 0 :=
    mul_ne_zero two_ne_zero (by exact_mod_cast Real.pi_ne_zero)
  refine (Set.countable_range (fun n : ℤ =>
    (((Real.pi : ℂ) * I + (n : ℂ) * (2 * (Real.pi : ℂ) * I)
      + (Real.pi : ℂ) * I / b ^ 2 * (2 * (k : ℂ) + 1)) * b) / (2 * (Real.pi : ℂ)))).mono ?_
  intro z hz
  simp only [Set.mem_setOf_eq, denFactor] at hz
  have hexp : Complex.exp (-((Real.pi : ℂ) * I) / b ^ 2 * (2 * (k : ℂ) + 1)
      + 2 * (Real.pi : ℂ) * z / b) = -1 := by linear_combination hz
  rw [← Complex.exp_pi_mul_I, Complex.exp_eq_exp_iff_exists_int] at hexp
  obtain ⟨n, hn⟩ := hexp
  refine ⟨n, ?_⟩
  have hb2 : b ^ 2 ≠ 0 := pow_ne_zero 2 hb
  show (((Real.pi : ℂ) * I + (n : ℂ) * (2 * (Real.pi : ℂ) * I)
      + (Real.pi : ℂ) * I / b ^ 2 * (2 * (k : ℂ) + 1)) * b) / (2 * (Real.pi : ℂ)) = z
  field_simp [hb, hb2] at hn ⊢
  linear_combination -hn

/-- The numerator product's zero set is countable (union over `k` of the factor lattices). -/
theorem num_zeros_countable (b : ℂ) (hβ : 0 < (b ^ 2).im) (hb : b ≠ 0) :
    {z : ℂ | (∏' k, numFactor b z k) = 0}.Countable := by
  refine (Set.countable_iUnion (fun k => numFactor_zeros_countable b hb k)).mono ?_
  intro z hz
  simp only [Set.mem_setOf_eq] at hz
  rw [Set.mem_iUnion]
  by_contra hcon
  push_neg at hcon
  exact tprod_numFactor_ne_zero b z hβ (fun k => hcon k) hz

/-- The denominator product's zero set is countable. -/
theorem den_zeros_countable (b : ℂ) (hβ : 0 < (b ^ 2).im) (hb : b ≠ 0) :
    {z : ℂ | (∏' k, denFactor b z k) = 0}.Countable := by
  refine (Set.countable_iUnion (fun k => denFactor_zeros_countable b hb k)).mono ?_
  intro z hz
  simp only [Set.mem_setOf_eq] at hz
  rw [Set.mem_iUnion]
  by_contra hcon
  push_neg at hcon
  exact tprod_denFactor_ne_zero b z hβ (fun k => hcon k) hz

/-- **`phiBProd`'s zero set is countable**: `phiBProd = num·den⁻¹`, so it vanishes only where
`num` or `den` does, both countable. -/
theorem phiBProd_zeros_countable (b : ℂ) (hβ : 0 < (b ^ 2).im) (hb : b ≠ 0) :
    {z : ℂ | phiBProd b z = 0}.Countable := by
  refine ((num_zeros_countable b hβ hb).union (den_zeros_countable b hβ hb)).mono ?_
  intro z hz
  simp only [Set.mem_setOf_eq, phiBProd, div_eq_mul_inv] at hz
  rcases mul_eq_zero.mp hz with h | h
  · exact Or.inl h
  · exact Or.inr (inv_eq_zero.mp h)

/-- The zero set of `z ↦ phiBProd b (z + c)` is countable (a translate of `phiBProd`'s zeros). -/
theorem phiBProd_shift_zeros_countable (b c : ℂ) (hβ : 0 < (b ^ 2).im) (hb : b ≠ 0) :
    {z : ℂ | phiBProd b (z + c) = 0}.Countable := by
  refine ((phiBProd_zeros_countable b hβ hb).image (fun w => w - c)).mono ?_
  intro z hz
  simp only [Set.mem_setOf_eq] at hz
  exact ⟨z + c, hz, by ring⟩

/-- The primary quasi-period prefactor's zero set is countable. -/
theorem primaryPrefactor_zeros_countable (b : ℂ) (hb : b ≠ 0) :
    {z : ℂ | (1 : ℂ) + Complex.exp (I * (Real.pi : ℂ) * b ^ 2)
      * Complex.exp (2 * (Real.pi : ℂ) * b * z) = 0}.Countable := by
  have h2pib : (2 : ℂ) * (Real.pi : ℂ) * b ≠ 0 :=
    mul_ne_zero (mul_ne_zero two_ne_zero (by exact_mod_cast Real.pi_ne_zero)) hb
  refine (Set.countable_range (fun n : ℤ =>
    ((Real.pi : ℂ) * I + (n : ℂ) * (2 * (Real.pi : ℂ) * I) - I * (Real.pi : ℂ) * b ^ 2)
      / (2 * (Real.pi : ℂ) * b))).mono ?_
  intro z hz
  simp only [Set.mem_setOf_eq] at hz
  have hexp : Complex.exp (I * (Real.pi : ℂ) * b ^ 2)
      * Complex.exp (2 * (Real.pi : ℂ) * b * z) = -1 := by linear_combination hz
  rw [← Complex.exp_add, ← Complex.exp_pi_mul_I, Complex.exp_eq_exp_iff_exists_int] at hexp
  obtain ⟨n, hn⟩ := hexp
  exact ⟨n, by rw [div_eq_iff h2pib]; linear_combination -hn⟩

/-- The dual quasi-period prefactor's zero set is countable. -/
theorem dualPrefactor_zeros_countable (b : ℂ) (hb : b ≠ 0) :
    {z : ℂ | (1 : ℂ)
      + Complex.exp (2 * (Real.pi : ℂ) * (z + I / (2 * b)) / b) = 0}.Countable := by
  have hπ : (Real.pi : ℂ) ≠ 0 := by exact_mod_cast Real.pi_ne_zero
  have h2pi : (2 : ℂ) * (Real.pi : ℂ) ≠ 0 := by simp [hπ]
  refine (Set.countable_range (fun n : ℤ =>
    ((Real.pi : ℂ) * I + (n : ℂ) * (2 * (Real.pi : ℂ) * I)) * b
      / (2 * (Real.pi : ℂ)) - I / (2 * b))).mono ?_
  intro z hz
  simp only [Set.mem_setOf_eq] at hz
  have hexp : Complex.exp (2 * (Real.pi : ℂ) * (z + I / (2 * b)) / b) = -1 := by
    linear_combination hz
  rw [← Complex.exp_pi_mul_I, Complex.exp_eq_exp_iff_exists_int] at hexp
  obtain ⟨n, hn⟩ := hexp
  refine ⟨n, ?_⟩
  show ((Real.pi : ℂ) * I + (n : ℂ) * (2 * (Real.pi : ℂ) * I)) * b
      / (2 * (Real.pi : ℂ)) - I / (2 * b) = z
  rw [div_eq_iff hb] at hn
  have hz2 : z + I / (2 * b)
      = ((Real.pi : ℂ) * I + (n : ℂ) * (2 * (Real.pi : ℂ) * I)) * b / (2 * (Real.pi : ℂ)) := by
    rw [eq_div_iff h2pi]; linear_combination hn
  rw [← hz2]; ring

/-- **`phiBProd` uniqueness up to scalar — loci discharged.** Any substrate `FaddeevPhi` +
`FaddeevPhiStripGrowth` solution `Φ₁` in meromorphic normal form is proportional to `phiBProd`.
The dense periodicity loci are constructed explicitly and their density is proved from the
countability of the prefactor and `phiBProd`-zero sets. The **only** remaining hypothesis is the
honest regularity `MeromorphicNFOn Φ₁`. -/
theorem phiBProd_uniqueUpToScalar_of_normalForm {t : ℝ} (ht : 0 < t) {Φ₁ : ℂ → ℂ}
    [FaddeevPhi (substrateB t) Φ₁] [FaddeevPhiStripGrowth (substrateB t) Φ₁]
    (hΦ₁NF : MeromorphicNFOn Φ₁ Set.univ) :
    ∃ c, ∀ z, phiBProd (substrateB t) z ≠ 0 → Φ₁ z = c * phiBProd (substrateB t) z := by
  set b := substrateB t with hbdef
  have hb : b ≠ 0 := by
    intro h; have := substrateB_re_pos ht; rw [← hbdef, h] at this; simp at this
  have hβ : 0 < (b ^ 2).im := substrateB_sq_im_pos ht
  -- S₀
  set S₀ : Set ℂ := {z : ℂ |
    (1 : ℂ) + Complex.exp (I * (Real.pi : ℂ) * b ^ 2) * Complex.exp (2 * (Real.pi : ℂ) * b * z) ≠ 0
      ∧ phiBProd b z ≠ 0 ∧ phiBProd b (z + I * b) ≠ 0} with hS0def
  set S₁ : Set ℂ := {z : ℂ |
    (1 : ℂ) + Complex.exp (2 * (Real.pi : ℂ) * (z + I / (2 * b)) / b) ≠ 0
      ∧ phiBProd b z ≠ 0 ∧ phiBProd b (z + I / b) ≠ 0} with hS1def
  have hdenseS₀ : Dense S₀ := by
    set bad₀ : Set ℂ := {z : ℂ | (1 : ℂ) + Complex.exp (I * (Real.pi : ℂ) * b ^ 2)
          * Complex.exp (2 * (Real.pi : ℂ) * b * z) = 0}
        ∪ {z : ℂ | phiBProd b z = 0} ∪ {z : ℂ | phiBProd b (z + I * b) = 0} with hbad0
    have hcnt : bad₀.Countable :=
      ((primaryPrefactor_zeros_countable b hb).union
        (phiBProd_zeros_countable b hβ hb)).union
        (phiBProd_shift_zeros_countable b (I * b) hβ hb)
    have heq : S₀ = bad₀ᶜ := by
      rw [hS0def, hbad0]; ext z
      simp only [Set.mem_setOf_eq, Set.mem_compl_iff, Set.mem_union, not_or, ne_eq]
      tauto
    rw [heq]; exact QOU.Common.dense_compl_of_countable hcnt
  have hdenseS₁ : Dense S₁ := by
    set bad₁ : Set ℂ := {z : ℂ | (1 : ℂ) + Complex.exp (2 * (Real.pi : ℂ) * (z + I / (2 * b)) / b) = 0}
        ∪ {z : ℂ | phiBProd b z = 0} ∪ {z : ℂ | phiBProd b (z + I / b) = 0} with hbad1
    have hcnt : bad₁.Countable :=
      ((dualPrefactor_zeros_countable b hb).union
        (phiBProd_zeros_countable b hβ hb)).union
        (phiBProd_shift_zeros_countable b (I / b) hβ hb)
    have heq : S₁ = bad₁ᶜ := by
      rw [hS1def, hbad1]; ext z
      simp only [Set.mem_setOf_eq, Set.mem_compl_iff, Set.mem_union, not_or, ne_eq]
      tauto
    rw [heq]; exact QOU.Common.dense_compl_of_countable hcnt
  exact PhiBProdUniquenessComplete.phiBProd_uniqueUpToScalar ht hΦ₁NF hdenseS₀ hdenseS₁
    (fun z hz => hz) (fun z hz => hz)

end QOU.QBeta.PhiBProdLociDensity
