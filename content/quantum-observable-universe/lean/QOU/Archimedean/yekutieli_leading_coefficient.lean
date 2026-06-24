import Mathlib.Tactic

/-!
# QOU.Archimedean.yekutieli_leading_coefficient — `κ(T_{2,p}) = 1 ≠ 0`

**Lemma** ([`lem:yekutieli-leading-coefficient`](../../../quantum-observable-universe/archimedean-universe/yekutieli-leading-coefficient.md)).

*For `T_{2,p}` at level `n = g + 1 = 5`, the Yekutieli obstruction
`κ(T_{2,p}) ∈ H²(𝓢, 𝓑)` equals the leading Chebyshev coefficient
`c_{(p−1)/2} = 1`.  In particular `κ(T_{2,p}) ≠ 0` for `q ≠ 1`.*

The Lean encoding records the equality with the leading Chebyshev
coefficient and the non-vanishing claim at `q ≠ 1`.

-- Ref: [manuscript] quantum-observable-universe/archimedean-universe/yekutieli-leading-coefficient.md
-/

namespace QOU.Archimedean

/-- Abstract context for the Yekutieli-leading-coefficient lemma. -/
class YekutieliLeadingContext where
  /-- The substrate parameter `q`. -/
  q : ℝ
  /-- The Yekutieli obstruction class (`R`-valued image in `H²(𝓢, 𝓑)`). -/
  yekutieliObstruction : ℕ → ℝ          -- yekutieliObstruction p = κ(T_{2,p})
  /-- The leading Chebyshev coefficient (always `1` at the top level). -/
  leadingChebyshev : ℕ → ℝ              -- leadingChebyshev p = c_{(p-1)/2}
  /-- Manuscript identification: for odd primes `p`, the Yekutieli
      obstruction equals the leading Chebyshev coefficient (and both
      equal `1`). -/
  claim_yekutieli_eq_leading : ∀ p : ℕ, Odd p →
    yekutieliObstruction p = leadingChebyshev p ∧
    yekutieliObstruction p = 1

/-- **Yekutieli obstruction = 1 (leading Chebyshev coefficient)**
    at level `n = 5`, for `T_{2,p}` with odd prime `p`. -/
-- Ref: [manuscript] quantum-observable-universe/archimedean-universe/yekutieli-leading-coefficient.md
theorem yekutieli_leading_coefficient
    [ctx : YekutieliLeadingContext]
    (p : ℕ) (hp_odd : Odd p) :
    ctx.yekutieliObstruction p = ctx.leadingChebyshev p ∧
    ctx.yekutieliObstruction p = 1 :=
  ctx.claim_yekutieli_eq_leading p hp_odd

/-- **Non-vanishing at `q ≠ 1`**: a Corollary of the above. -/
-- Ref: [manuscript] quantum-observable-universe/archimedean-universe/yekutieli-leading-coefficient.md
theorem yekutieli_obstruction_ne_zero
    [ctx : YekutieliLeadingContext] (p : ℕ) (hp_odd : Odd p)
    (hq_ne : ctx.q ≠ 1) :
    ctx.yekutieliObstruction p ≠ 0 := by
  intro h
  have ⟨_, h_eq_one⟩ := yekutieli_leading_coefficient p hp_odd
  rw [h] at h_eq_one
  -- `0 = 1` is absurd
  exact zero_ne_one h_eq_one

end QOU.Archimedean
