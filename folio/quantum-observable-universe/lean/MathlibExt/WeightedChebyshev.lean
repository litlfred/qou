import Mathlib.Algebra.Order.Chebyshev
import Mathlib.Algebra.Order.Monovary
import Mathlib.Tactic

/-!
# QOU.MathlibExt.WeightedChebyshev — Chebyshev's association inequality, WEIGHTED

Mathlib has Chebyshev's sum inequality only in its **unweighted** form
(`MonovaryOn.sum_mul_sum_le_card_mul_sum`):

    (∑ f) * (∑ g)  ≤  card s * ∑ f * g

which is `Cov(f, g) ≥ 0` for the **uniform** measure on `s`. Every measure this
project actually integrates against — Plancherel, the ω-weighted edge measure —
is non-uniform, so that form does not apply. This file supplies the weighted
one:

    (∑ w f) * (∑ w g)  ≤  (∑ w) * (∑ w f g)      for `w ≥ 0` and `f`, `g` monovarying.

Setting `w ≡ 1` recovers Mathlib's statement, so this is a strict generalisation
and a candidate for upstream.

## Why this project wants it

Gap `qou-k5r5` needs `M₁ = Cov(∑ h, ∑ c²) > 0` under Plancherel. Along the
Plancherel growth chain that splits as `Cov(∑|cₖ|, ∑c²) + 2 Cov(∑Dₖ, ∑c²)` with
the first term positive and the second negative
(`wlambda_covariance_epic_M1_kappa_cancellation.py`). The positivity of the
first is exactly this inequality: `|c|` and `c²` are both increasing functions
of the single quantity `|c|`, hence monovary, so their weighted covariance is
non-negative under ANY non-negative weight.

That does not by itself settle `M₁ > 0` — the negative term is ~65 % of the
positive one, and controlling their difference is the open part. This file
proves the piece that is unconditional.

## The proof

The classical symmetrisation, exactly:

    ∑ᵢ ∑ⱼ wᵢ wⱼ (fᵢ − fⱼ)(gᵢ − gⱼ)  =  2 [ (∑w)(∑ w f g) − (∑ w f)(∑ w g) ]

with every summand on the left non-negative. No analysis, no ordering of `s`,
and no `LinearOrder` on the index — only the pointwise product condition.
-/

namespace QOU.MathlibExt.WeightedChebyshev

variable {ι : Type*} {s : Finset ι} {w f g : ι → ℚ}

/-- The symmetrisation identity. Both sides are `2 ·` the weighted covariance,
written once as a double sum of pair differences and once in closed form. -/
theorem two_mul_weighted_cov_eq (s : Finset ι) (w f g : ι → ℚ) :
    ∑ i ∈ s, ∑ j ∈ s, w i * w j * ((f i - f j) * (g i - g j))
      = 2 * ((∑ i ∈ s, w i) * (∑ i ∈ s, w i * (f i * g i))
             - (∑ i ∈ s, w i * f i) * (∑ i ∈ s, w i * g i)) := by
  have inner : ∀ i ∈ s, ∑ j ∈ s, w i * w j * ((f i - f j) * (g i - g j))
      = (w i * (f i * g i)) * (∑ i ∈ s, w i)
        - (w i * f i) * (∑ i ∈ s, w i * g i)
        - (w i * g i) * (∑ i ∈ s, w i * f i)
        + w i * (∑ i ∈ s, w i * (f i * g i)) := by
    intro i _
    have hsplit : ∀ j, w i * w j * ((f i - f j) * (g i - g j))
        = (w i * (f i * g i)) * w j - (w i * f i) * (w j * g j)
          - (w i * g i) * (w j * f j) + w i * (w j * (f j * g j)) := by
      intro j; ring
    rw [Finset.sum_congr rfl fun j _ => hsplit j]
    rw [Finset.sum_add_distrib, Finset.sum_sub_distrib, Finset.sum_sub_distrib,
      ← Finset.mul_sum, ← Finset.mul_sum, ← Finset.mul_sum, ← Finset.mul_sum]
  rw [Finset.sum_congr rfl inner]
  rw [Finset.sum_add_distrib, Finset.sum_sub_distrib, Finset.sum_sub_distrib,
    ← Finset.sum_mul, ← Finset.sum_mul, ← Finset.sum_mul, ← Finset.sum_mul]
  ring

/-- **Chebyshev's association inequality, weighted.**

If `w ≥ 0` on `s` and every pair satisfies `(fᵢ − fⱼ)(gᵢ − gⱼ) ≥ 0` — which is
what it means for `f` and `g` to vary together — then

    (∑ w f) * (∑ w g)  ≤  (∑ w) * (∑ w f g).

The pair condition is stated directly rather than through `MonovaryOn` so the
theorem can be applied without a `LinearOrder`; `monovaryOn_pairwise_nonneg`
below converts. -/
theorem weighted_chebyshev (hw : ∀ i ∈ s, 0 ≤ w i)
    (hpair : ∀ i ∈ s, ∀ j ∈ s, 0 ≤ (f i - f j) * (g i - g j)) :
    (∑ i ∈ s, w i * f i) * (∑ i ∈ s, w i * g i)
      ≤ (∑ i ∈ s, w i) * ∑ i ∈ s, w i * (f i * g i) := by
  have hnn : 0 ≤ ∑ i ∈ s, ∑ j ∈ s, w i * w j * ((f i - f j) * (g i - g j)) := by
    refine Finset.sum_nonneg fun i hi => Finset.sum_nonneg fun j hj => ?_
    exact mul_nonneg (mul_nonneg (hw i hi) (hw j hj)) (hpair i hi j hj)
  rw [two_mul_weighted_cov_eq] at hnn
  linarith

/-- `MonovaryOn` gives the pairwise condition the inequality above wants. -/
theorem monovaryOn_pairwise_nonneg (h : MonovaryOn f g s) :
    ∀ i ∈ s, ∀ j ∈ s, 0 ≤ (f i - f j) * (g i - g j) := by
  intro i hi j hj
  rcases lt_trichotomy (g i) (g j) with hlt | heq | hgt
  · have : f i ≤ f j := h hi hj hlt
    have h1 : f i - f j ≤ 0 := by linarith
    have h2 : g i - g j ≤ 0 := by linarith
    nlinarith [h1, h2]
  · simp [heq]
  · have : f j ≤ f i := h hj hi hgt
    have h1 : 0 ≤ f i - f j := by linarith
    have h2 : 0 ≤ g i - g j := by linarith
    exact mul_nonneg h1 h2

/-- The form the covariance argument uses: with a weight summing to `1`, the
weighted covariance of two monovarying observables is non-negative. -/
theorem weighted_cov_nonneg (hw : ∀ i ∈ s, 0 ≤ w i) (hsum : ∑ i ∈ s, w i = 1)
    (hpair : ∀ i ∈ s, ∀ j ∈ s, 0 ≤ (f i - f j) * (g i - g j)) :
    (∑ i ∈ s, w i * f i) * (∑ i ∈ s, w i * g i)
      ≤ ∑ i ∈ s, w i * (f i * g i) := by
  have h := weighted_chebyshev hw hpair
  rwa [hsum, one_mul] at h

end QOU.MathlibExt.WeightedChebyshev
