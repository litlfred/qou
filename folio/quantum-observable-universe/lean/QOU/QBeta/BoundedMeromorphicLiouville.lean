import Mathlib.Analysis.Meromorphic.NormalForm
import Mathlib.Analysis.Meromorphic.Order
import Mathlib.Analysis.Complex.Basic

/-!
# Bounded meromorphic ⇒ entire (the state-integral / growth-bound route)

A boundedness companion to brick (c)
(`QOU.QBeta.RatioEntire.entire_toMeromorphicNFOn_div_of_same_order`) for the
Faddeev–Volkov uniqueness leg of the A_ω monodromy datum (`qou-2cvs` / route 2,
bean `qou-aanp`).

Brick (c) makes the ratio `Φ₁/Φ₂` entire by **matching divisors** (the `PhiBProd`
route). This file supplies the **other** honest route the elliptic-freedom
obstruction (`FaddeevPhiEllipticFreedom.faddeevPhi_mul_elliptic`) leaves open: a
nonconstant elliptic factor `℘` has **poles**, so it is **unbounded**; conversely a
**bounded** meromorphic ratio has no poles and is therefore entire. The boundedness
is exactly the endowment the **state-integral / Écalle–Borel resurgent
representation** of `Φ_b` supplies — `Φ_b` is analytic with controlled growth in a
fundamental strip, so the prefactor-cancelled ratio of two genuine solutions is
bounded on `ℂ`.

The mechanism reuses the Mathlib `Meromorphic` cone (built from pinned source, see
[`scripts/build-meromorphic-cone.sh`](../../../../../scripts/build-meromorphic-cone.sh)):
a pole forces `‖f‖ → ∞` (`tendsto_cobounded_of_meromorphicOrderAt_neg`), which a
uniform bound contradicts, so `meromorphicOrderAt ≥ 0` everywhere; a normal-form
function of nonnegative order is analytic
(`MeromorphicNFAt.meromorphicOrderAt_nonneg_iff_analyticAt`), hence entire.

Discipline: this is a **conditional** brick (§3b-cond). Boundedness is a named,
non-axiomatised hypothesis — a growth statement that does **not** assume the
conclusion (constancy/proportionality is far stronger, and there are bounded
non-constant functions). It excludes the elliptic freedom honestly, on the merits.
Verified `lean`-direct against the Meromorphic cone (exit 0).
-/

open Filter Topology Bornology

namespace QOU.QBeta.BoundedMeromorphicLiouville

/-- **Bounded ⇒ meromorphic order `≥ 0` everywhere.** If `‖f z‖ ≤ C` for all `z`,
then `f` has no pole: a negative-order point would force `f → ∞`
(`tendsto_cobounded_of_meromorphicOrderAt_neg`), impossible under a uniform bound
(the punctured neighbourhood `𝓝[≠] z` is `NeBot` in `ℂ`, so the empty preimage of the
unbounded target cannot lie in it). -/
theorem meromorphicOrderAt_nonneg_of_bounded {f : ℂ → ℂ} {C : ℝ}
    (hbdd : ∀ z, ‖f z‖ ≤ C) (z : ℂ) : 0 ≤ meromorphicOrderAt f z := by
  by_contra h
  push_neg at h
  have htend : Tendsto f (𝓝[≠] z) (cobounded ℂ) :=
    tendsto_cobounded_of_meromorphicOrderAt_neg h
  have hset : {w : ℂ | ‖w‖ ≤ C} = Metric.closedBall (0 : ℂ) C := by
    ext w; simp [Metric.mem_closedBall, dist_zero_right]
  have hball : IsBounded {w : ℂ | ‖w‖ ≤ C} := by
    rw [hset]; exact Metric.isBounded_closedBall
  have hpre : f ⁻¹' {w : ℂ | ‖w‖ ≤ C}ᶜ ∈ 𝓝[≠] z :=
    htend (Bornology.isBounded_def.mp hball)
  have hempty : f ⁻¹' {w : ℂ | ‖w‖ ≤ C}ᶜ = ∅ := by
    ext w
    simp only [Set.mem_preimage, Set.mem_compl_iff, Set.mem_setOf_eq,
      Set.mem_empty_iff_false, iff_false, not_not]
    exact hbdd w
  rw [hempty] at hpre
  exact (inferInstance : (𝓝[≠] z).NeBot).ne (empty_mem_iff_bot.mp hpre)

/-- **Bounded meromorphic-normal-form ⇒ entire.** A function in meromorphic normal
form on `ℂ` that is bounded has nonnegative order everywhere (no poles), and a
normal-form function of nonnegative order is analytic — so it is entire. -/
theorem entire_of_meromorphicNFOn_bounded {g : ℂ → ℂ} {C : ℝ}
    (hg : MeromorphicNFOn g Set.univ) (hbdd : ∀ z, ‖g z‖ ≤ C) :
    Differentiable ℂ g := by
  intro z
  have hord : 0 ≤ meromorphicOrderAt g z := meromorphicOrderAt_nonneg_of_bounded hbdd z
  exact ((hg (Set.mem_univ z)).meromorphicOrderAt_nonneg_iff_analyticAt.1 hord).differentiableAt

/-- **Bounded ⇒ the normal-form representative is entire.** For any `f`, if its
normal-form representative `g = toMeromorphicNFOn f univ` is bounded, then `g` is
entire. This is the boundedness analogue of brick (c)
(`RatioEntire.entire_toMeromorphicNFOn_div_of_same_order`): there the ratio is made
entire by matching divisors; here, by a uniform growth bound (the state-integral
endowment). -/
theorem entire_toMeromorphicNFOn_of_bounded {f : ℂ → ℂ} {C : ℝ}
    (hbdd : ∀ z, ‖toMeromorphicNFOn f Set.univ z‖ ≤ C) :
    Differentiable ℂ (toMeromorphicNFOn f Set.univ) :=
  entire_of_meromorphicNFOn_bounded (meromorphicNFOn_toMeromorphicNFOn f Set.univ) hbdd

end QOU.QBeta.BoundedMeromorphicLiouville
