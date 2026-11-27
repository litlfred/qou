import Mathlib.Analysis.Meromorphic.NormalForm
import Mathlib.Analysis.Meromorphic.Order
import Mathlib.Analysis.Complex.Basic

/-!
# Punctured-neighborhood boundedness ⇒ global boundedness of a meromorphic normal form (G5 crux)

The analytic heart of brick **G5** of the Faddeev growth-estimate epic (`qou-mz4f`). The
boundedness capstone `FaddeevUniquenessBoundedCapstone.faddeevPhi_proportional_of_bounded_ratio`
consumes `hbdd : ∀ z, ‖toMeromorphicNFOn (Φ₁/Φ₂) univ z‖ ≤ C` — a bound on the normal form at
**every** point. The strip-growth class (`FaddeevPhiStripGrowth`, G4) only bounds the raw ratio
on the **dense** non-vanishing locus `{Φ₂ ≠ 0}`. This file bridges the gap: a bound on a
*punctured neighborhood* of every point promotes to a global bound.

* `meromorphicOrderAt_nonneg_of_bounded_punctured` — the **local** form of
  `BoundedMeromorphicLiouville.meromorphicOrderAt_nonneg_of_bounded`: boundedness on
  `𝓝[≠] z` alone forces `meromorphicOrderAt f z ≥ 0` (a pole would push `f → ∞` on that very
  punctured filter, contradicting the bound). No global hypothesis.
* `norm_le_of_bounded_on_punctured` — for a normal-form function bounded on a punctured
  neighborhood of every point: each point is a **removable** singularity (order ≥ 0 ⇒
  analytic ⇒ continuous), so the value equals the limit and inherits the bound. This yields
  the global `hbdd` from a codiscrete (dense-complement) bound.

Together these discharge the removable-singularity extension of G5. What remains to *call* the
capstone (assembly-level, **no Mathlib gap**): (i) `∀ᶠ w in 𝓝[≠] z, Φ₂ w ≠ 0` — `Φ₂`'s zeros
isolated (for `phiBProd`, from `meromorphicOrderAt ≠ ⊤`, PR #4225); (ii) `hr_ratio`
(`toMeromorphicNFOn (Φ₁/Φ₂) = Φ₁/Φ₂` off poles, from the meromorphic normal-form API); (iii)
the honest physical hypothesis `MeromorphicOn Φ₁` for the arbitrary second solution.

Verified `lean`-direct against the pinned Mathlib `Meromorphic` cone. Sorry-free.

-- Ref: [leitner2026] docs/workplans/2026-07-26-faddeev-growth-estimate-epic-scope.md
-/

open Filter Topology Bornology

namespace QOU.QBeta.MeromorphicPuncturedBounded

/-- **Local bounded ⇒ order ≥ 0.** A bound on a *punctured neighborhood* `𝓝[≠] z` alone
forces `meromorphicOrderAt f z ≥ 0`: a negative-order point would send `f → ∞` on `𝓝[≠] z`
(`tendsto_cobounded_of_meromorphicOrderAt_neg`), but the bound keeps `f` inside a ball there —
and `𝓝[≠] z` is `NeBot`, so it cannot simultaneously be eventually-in and eventually-out. This
is the punctured-neighborhood strengthening of
`BoundedMeromorphicLiouville.meromorphicOrderAt_nonneg_of_bounded` (which assumes a global
bound). -/
theorem meromorphicOrderAt_nonneg_of_bounded_punctured {f : ℂ → ℂ} {C : ℝ} {z : ℂ}
    (hbdd : ∀ᶠ w in 𝓝[≠] z, ‖f w‖ ≤ C) : 0 ≤ meromorphicOrderAt f z := by
  by_contra h
  push_neg at h
  have htend : Tendsto f (𝓝[≠] z) (cobounded ℂ) :=
    tendsto_cobounded_of_meromorphicOrderAt_neg h
  have hball : IsBounded {w : ℂ | ‖w‖ ≤ C} := by
    have hset : {w : ℂ | ‖w‖ ≤ C} = Metric.closedBall (0 : ℂ) C := by
      ext w; simp [Metric.mem_closedBall, dist_zero_right]
    rw [hset]; exact Metric.isBounded_closedBall
  have hcpre : f ⁻¹' {w : ℂ | ‖w‖ ≤ C}ᶜ ∈ 𝓝[≠] z :=
    htend (Bornology.isBounded_def.mp hball)
  have h1 : ∀ᶠ w in 𝓝[≠] z, C < ‖f w‖ := by
    filter_upwards [hcpre] with w hw; simpa using hw
  have hfalse : ∀ᶠ w in 𝓝[≠] z, False := by
    filter_upwards [hbdd, h1] with w hle hlt using absurd hle (not_le.mpr hlt)
  exact (NeBot.ne inferInstance) (Filter.eventually_false_iff_eq_bot.mp hfalse)

/-- **Punctured-bounded everywhere ⇒ globally bounded** (normal form). If a meromorphic
normal-form function `g` on `ℂ` is bounded by `C` on a punctured neighborhood of *every* point,
then `‖g z‖ ≤ C` for every `z`: order ≥ 0 (previous lemma) makes each point a removable
singularity, so `g` is analytic — hence continuous — at `z`, and its value is the limit of the
(bounded) nearby values. This turns a codiscrete (dense-complement) bound into the global
`hbdd` the boundedness capstone requires. -/
theorem norm_le_of_bounded_on_punctured {g : ℂ → ℂ} {C : ℝ}
    (hg : MeromorphicNFOn g Set.univ)
    (hpunc : ∀ z, ∀ᶠ w in 𝓝[≠] z, ‖g w‖ ≤ C) (z : ℂ) : ‖g z‖ ≤ C := by
  have hord : 0 ≤ meromorphicOrderAt g z :=
    meromorphicOrderAt_nonneg_of_bounded_punctured (hpunc z)
  have hana : AnalyticAt ℂ g z :=
    (hg (Set.mem_univ z)).meromorphicOrderAt_nonneg_iff_analyticAt.1 hord
  have htend : Tendsto (fun w => ‖g w‖) (𝓝[≠] z) (𝓝 ‖g z‖) :=
    (hana.continuousAt.norm.tendsto).mono_left nhdsWithin_le_nhds
  exact le_of_tendsto htend (hpunc z)

end QOU.QBeta.MeromorphicPuncturedBounded
