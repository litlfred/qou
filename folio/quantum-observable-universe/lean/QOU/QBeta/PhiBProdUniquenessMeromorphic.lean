import QOU.QBeta.PhiBProdUniquenessFinal
import QOU.QBeta.PhiBProdHrRatio
import QOU.QBeta.PhiBProdLociDensity

/-!
# `phiBProd` uniqueness for a merely-meromorphic, continuous second solution (broadening)

`PhiBProdLociDensity.phiBProd_uniqueUpToScalar_of_normalForm` requires the second solution `Φ₁`
to be in meromorphic **normal form** (`MeromorphicNFOn Φ₁`). That hypothesis is **load-bearing,
not cosmetic**: a general `MeromorphicOn` function may be discontinuous at an isolated removable
point, and the *pointwise* proportionality `∀ z, … → Φ₁ z = c·phiBProd z` genuinely fails there.

This file gives the honest broadening: `MeromorphicOn Φ₁` **plus continuity on the nonzero
locus** (`∀ z, phiBProd z ≠ 0 → ContinuousAt Φ₁ z`) — a strictly weaker, more elementary
hypothesis than `MeromorphicNFOn` (which implies both). The key is `MeromorphicAt.analyticAt`:
a meromorphic function that is **continuous** at `z` is analytic there, discharging the `Φ₁`
analyticity that `hr_ratio` needs without the normal-form machinery.

`phiBProd_uniqueUpToScalar_of_meromorphic` — the resulting statement. The dense periodicity loci
are reconstructed from the merged countability lemmas (`PhiBProdLociDensity`), so the **only**
inputs are `MeromorphicOn Φ₁` and continuity-where-finite — exactly what "the physical `Φ_b` is a
genuine meromorphic function" means.

Verified `lean`-direct against the merged `phiBProd` chain. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-26-faddeev-keystone-7xvy-canonical-arc.md
-/

open Complex Set
open QOU.MathlibExt.PhiBProd
open QOU.MathlibExt.FaddeevQuantumDilogarithm
open QOU.QBeta.PhiBProdProductConvergence

namespace QOU.QBeta.PhiBProdUniquenessMeromorphic

/-- **`hr_ratio` for a continuous meromorphic second solution.** If `Φ₁` is meromorphic on `ℂ`
and continuous at `z` (where `phiBProd b z ≠ 0`), then `Φ₁` is analytic at `z`
(`MeromorphicAt.analyticAt`), so the ratio `Φ₁/phiBProd` is analytic — hence its normal form
agrees with the pointwise ratio. No normal-form hypothesis on `Φ₁`. -/
theorem hr_ratio_of_continuous (b z : ℂ) (hβ : 0 < (b ^ 2).im) {Φ₁ : ℂ → ℂ}
    (hmer : MeromorphicOn Φ₁ Set.univ) (hcont : ContinuousAt Φ₁ z)
    (hz : phiBProd b z ≠ 0) :
    toMeromorphicNFOn (Φ₁ / phiBProd b) Set.univ z = Φ₁ z / phiBProd b z := by
  have hphi_ana : AnalyticAt ℂ (phiBProd b) z :=
    PhiBProdHrRatio.phiBProd_analyticAt_of_ne_zero b z hβ hz
  have hΦ₁_ana : AnalyticAt ℂ Φ₁ z := (hmer z (mem_univ z)).analyticAt hcont
  have hratio_ana : AnalyticAt ℂ (Φ₁ / phiBProd b) z := hΦ₁_ana.div hphi_ana hz
  have hmerR : MeromorphicOn (Φ₁ / phiBProd b) Set.univ :=
    hmer.div (phiBProd_meromorphicOn b hβ)
  rw [toMeromorphicNFOn_eq_toMeromorphicNFAt hmerR (mem_univ z),
    toMeromorphicNFAt_eq_self.mpr hratio_ana.meromorphicNFAt]
  rfl

/-- **`phiBProd` uniqueness up to scalar — meromorphic + continuous second solution.** Any
substrate `FaddeevPhi` + `FaddeevPhiStripGrowth` solution `Φ₁` that is meromorphic on `ℂ` and
continuous wherever `phiBProd ≠ 0` is proportional to `phiBProd`. This weakens the normal-form
hypothesis of `phiBProd_uniqueUpToScalar_of_normalForm` to `MeromorphicOn` + continuity, the
honest physical statement. -/
theorem phiBProd_uniqueUpToScalar_of_meromorphic {t : ℝ} (ht : 0 < t) {Φ₁ : ℂ → ℂ}
    [FaddeevPhi (substrateB t) Φ₁] [FaddeevPhiStripGrowth (substrateB t) Φ₁]
    (hmer : MeromorphicOn Φ₁ Set.univ)
    (hcont : ∀ z, phiBProd (substrateB t) z ≠ 0 → ContinuousAt Φ₁ z) :
    ∃ c, ∀ z, phiBProd (substrateB t) z ≠ 0 → Φ₁ z = c * phiBProd (substrateB t) z := by
  set b := substrateB t with hbdef
  have hb : b ≠ 0 := by
    intro h; have := substrateB_re_pos ht; rw [← hbdef, h] at this; simp at this
  have hβ : 0 < (b ^ 2).im := substrateB_sq_im_pos ht
  -- Dense loci, reconstructed from the merged countability lemmas.
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
      ((PhiBProdLociDensity.primaryPrefactor_zeros_countable b hb).union
        (PhiBProdLociDensity.phiBProd_zeros_countable b hβ hb)).union
        (PhiBProdLociDensity.phiBProd_shift_zeros_countable b (I * b) hβ hb)
    have heq : S₀ = bad₀ᶜ := by
      rw [hS0def, hbad0]; ext z
      simp only [Set.mem_setOf_eq, Set.mem_compl_iff, Set.mem_union, not_or, ne_eq]
      tauto
    rw [heq]; exact QOU.Common.dense_compl_of_countable hcnt
  have hdenseS₁ : Dense S₁ := by
    set bad₁ : Set ℂ := {z : ℂ | (1 : ℂ) + Complex.exp (2 * (Real.pi : ℂ) * (z + I / (2 * b)) / b) = 0}
        ∪ {z : ℂ | phiBProd b z = 0} ∪ {z : ℂ | phiBProd b (z + I / b) = 0} with hbad1
    have hcnt : bad₁.Countable :=
      ((PhiBProdLociDensity.dualPrefactor_zeros_countable b hb).union
        (PhiBProdLociDensity.phiBProd_zeros_countable b hβ hb)).union
        (PhiBProdLociDensity.phiBProd_shift_zeros_countable b (I / b) hβ hb)
    have heq : S₁ = bad₁ᶜ := by
      rw [hS1def, hbad1]; ext z
      simp only [Set.mem_setOf_eq, Set.mem_compl_iff, Set.mem_union, not_or, ne_eq]
      tauto
    rw [heq]; exact QOU.Common.dense_compl_of_countable hcnt
  refine PhiBProdUniquenessFinal.phiBProd_uniqueUpToScalar_of_stripGrowth ht
    (fun z hz => hr_ratio_of_continuous b z hβ hmer (hcont z hz) hz)
    hdenseS₀ hdenseS₁ (fun z hz => hz) (fun z hz => hz)

end QOU.QBeta.PhiBProdUniquenessMeromorphic
