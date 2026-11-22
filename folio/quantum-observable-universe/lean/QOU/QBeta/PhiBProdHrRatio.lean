import QOU.QBeta.PhiBProdProductConvergence
import QOU.QBeta.FaddeevPhiStripGrowth
import QOU.QBeta.MeromorphicPuncturedBounded
import Mathlib.Analysis.Meromorphic.NormalForm
import Mathlib.Analysis.Analytic.Constructions

/-!
# The normal-form identity `hr_ratio` for `phiBProd` (G5 specialization)

Discharges the `hr_ratio` input of `PhiBProdUniquenessFinal.phiBProd_uniqueUpToScalar_of_stripGrowth`
for a physical (normal-form) second solution: where `phiBProd b z ≠ 0`,
`toMeromorphicNFOn (Φ₁ / phiBProd b) univ z = Φ₁ z / phiBProd b z`.

The identity holds because the ratio is **analytic** at such `z`:
* `phiBProd` is analytic where it is nonzero (`phiBProd = num/den`, both entire, and
  `phiBProd z ≠ 0 ⇒ den z ≠ 0`) — `phiBProd_analyticAt_of_ne_zero`.
* `Φ₁` is analytic there: strip-growth comparability `‖Φ₁ w‖ ≤ C‖phiBProd w‖` plus `phiBProd`
  bounded near `z` gives a punctured-neighborhood bound, so `meromorphicOrderAt Φ₁ z ≥ 0`
  (`meromorphicOrderAt_nonneg_of_bounded_punctured`, G5 crux), which for a normal-form `Φ₁`
  means analytic (`MeromorphicNFAt.meromorphicOrderAt_nonneg_iff_analyticAt`).

An analytic function is in meromorphic normal form, so `toMeromorphicNFOn (Φ₁/phiBProd) univ z`
equals `(Φ₁/phiBProd) z` (`toMeromorphicNFOn_eq_toMeromorphicNFAt` + `toMeromorphicNFAt_eq_self`).

The honest regularity hypothesis on the second solution is `MeromorphicNFOn Φ₁ univ` — the
physical `Φ_b` is a genuine meromorphic function in normal form; the shift equations alone do
not impose it.

Verified `lean`-direct against the Mathlib `Meromorphic.NormalForm` cone + merged `phiBProd`.
Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-26-faddeev-keystone-7xvy-canonical-arc.md
-/

open Complex Filter Topology Set
open QOU.MathlibExt.PhiBProd
open QOU.QBeta.PhiBProdProductConvergence
open QOU.QBeta.MeromorphicPuncturedBounded

namespace QOU.QBeta.PhiBProdHrRatio

/-- **`phiBProd` is analytic where it is nonzero.** `phiBProd = num/den` with `num`, `den`
entire; `phiBProd z ≠ 0` forces `den z ≠ 0`, so the quotient is analytic at `z`. -/
theorem phiBProd_analyticAt_of_ne_zero (b z : ℂ) (hβ : 0 < (b ^ 2).im)
    (hz : phiBProd b z ≠ 0) : AnalyticAt ℂ (phiBProd b) z := by
  have hden : (fun z => ∏' k, denFactor b z k) z ≠ 0 := by
    intro h
    apply hz
    simp only [phiBProd, h, div_zero]
  have hnum_ana : AnalyticAt ℂ (fun z => ∏' k, numFactor b z k) z :=
    analyticOnNhd_num_tprod b hβ z (mem_univ z)
  have hden_ana : AnalyticAt ℂ (fun z => ∏' k, denFactor b z k) z :=
    analyticOnNhd_den_tprod b hβ z (mem_univ z)
  have hfun : phiBProd b
      = (fun z => ∏' k, numFactor b z k) / (fun z => ∏' k, denFactor b z k) := by
    funext z; rfl
  rw [hfun]
  exact hnum_ana.div hden_ana hden

/-- **A strip-growth second solution is analytic where `phiBProd` is nonzero** (given it is in
normal form). Comparability bounds `‖Φ₁‖` by `C‖phiBProd‖`; `phiBProd` is continuous and
nonzero at `z`, so `Φ₁` is bounded on a punctured neighborhood, giving order ≥ 0, i.e.
analytic. -/
theorem analyticAt_of_stripGrowth (b z : ℂ) (hβ : 0 < (b ^ 2).im) {Φ₁ : ℂ → ℂ}
    [FaddeevPhiStripGrowth b Φ₁] (hΦ₁NF : MeromorphicNFOn Φ₁ Set.univ)
    (hz : phiBProd b z ≠ 0) : AnalyticAt ℂ Φ₁ z := by
  obtain ⟨C, _hC, hcomp⟩ := (inferInstance : FaddeevPhiStripGrowth b Φ₁).comparable
  have hphi_ana : AnalyticAt ℂ (phiBProd b) z := phiBProd_analyticAt_of_ne_zero b z hβ hz
  -- `‖phiBProd ·‖` continuous at z, so eventually ≤ ‖phiBProd z‖ + 1
  have hbound_phi : ∀ᶠ w in 𝓝 z, ‖phiBProd b w‖ ≤ ‖phiBProd b z‖ + 1 :=
    (hphi_ana.continuousAt.norm).eventually_le_const (by linarith)
  -- punctured-neighborhood bound on ‖Φ₁‖
  have hpunc : ∀ᶠ w in 𝓝[≠] z, ‖Φ₁ w‖ ≤ C * (‖phiBProd b z‖ + 1) := by
    filter_upwards [hbound_phi.filter_mono nhdsWithin_le_nhds] with w hw
    calc ‖Φ₁ w‖ ≤ C * ‖phiBProd b w‖ := (hcomp w).1
      _ ≤ C * (‖phiBProd b z‖ + 1) :=
          mul_le_mul_of_nonneg_left hw _hC.le
  have hord : 0 ≤ meromorphicOrderAt Φ₁ z :=
    meromorphicOrderAt_nonneg_of_bounded_punctured hpunc
  exact (hΦ₁NF (mem_univ z)).meromorphicOrderAt_nonneg_iff_analyticAt.1 hord

/-- **`hr_ratio` for `phiBProd`.** For a normal-form strip-growth second solution `Φ₁`: where
`phiBProd b z ≠ 0`, the meromorphic normal form of `Φ₁/phiBProd` agrees with the pointwise
ratio. This discharges the `hr_ratio` input of the G5 specialization. -/
theorem hr_ratio_phiBProd (b z : ℂ) (hβ : 0 < (b ^ 2).im) {Φ₁ : ℂ → ℂ}
    [FaddeevPhiStripGrowth b Φ₁] (hΦ₁NF : MeromorphicNFOn Φ₁ Set.univ)
    (hz : phiBProd b z ≠ 0) :
    toMeromorphicNFOn (Φ₁ / phiBProd b) Set.univ z = Φ₁ z / phiBProd b z := by
  have hphi_ana : AnalyticAt ℂ (phiBProd b) z := phiBProd_analyticAt_of_ne_zero b z hβ hz
  have hΦ₁_ana : AnalyticAt ℂ Φ₁ z := analyticAt_of_stripGrowth b z hβ hΦ₁NF hz
  have hratio_ana : AnalyticAt ℂ (Φ₁ / phiBProd b) z := hΦ₁_ana.div hphi_ana hz
  have hmer : MeromorphicOn (Φ₁ / phiBProd b) Set.univ :=
    hΦ₁NF.meromorphicOn.div (phiBProd_meromorphicOn b hβ)
  rw [toMeromorphicNFOn_eq_toMeromorphicNFAt hmer (mem_univ z),
    toMeromorphicNFAt_eq_self.mpr hratio_ana.meromorphicNFAt]
  rfl

end QOU.QBeta.PhiBProdHrRatio
