import Mathlib.Tactic

/-!
# QOU.Archimedean.yekutieli_leading_coefficient — `κ(T_{2,p}) = 1 ≠ 0`

**Lemma** ([`lem:yekutieli-leading-coefficient`](../../../quantum-observable-universe/brings-surface/yekutieli-leading-coefficient.md)).

*For `T_{2,p}` at level `n = g + 1 = 5`, the Yekutieli obstruction
`κ(T_{2,p}) ∈ H²(𝓢, 𝓑)` equals the leading Chebyshev coefficient
`c_{(p−1)/2} = 1`.  In particular `κ(T_{2,p}) ≠ 0` for `q ≠ 1`.*

## Status

The substantive identity `κ(T_{2,p}) = c_{(p−1)/2}` is an equality of a
**second non-abelian cohomology class** in `H²(𝓢, 𝓑)` with the leading
coefficient of the genus-filtration Chebyshev expansion.  Its proof
rests on Yekutieli's non-abelian multiplicative-integration /
non-abelian-Stokes machinery on surfaces (the obstruction is the
curvature-2-form class of the descent), which is **not available in
Mathlib**.  The main theorem is therefore stated faithfully — real
substrate `q`, real obstruction value `κ q p : ℝ`, real conclusion
`κ q p = c p ∧ κ q p = 1` under the substrate hypothesis `q ≠ 1`
(at `q = 1` the crossing asymmetry, hence the obstruction, vanishes) —
and discharged by `sorry` with the bibliographic citation per
AGENTS.md §1.

The non-vanishing corollary `yekutieli_obstruction_ne_zero` is then
**derived sorry-free** from the (axiomatised) main statement: `κ q p = 1`
contradicts `κ q p = 0`.
-/

namespace QOU.Archimedean

/-- The Yekutieli obstruction `κ(T_{2,p}) ∈ H²(𝓢, 𝓑)`, recorded as its
    real image (the class value in the genus-filtration coordinate),
    as a function of the substrate `q` and the prime `p`. -/
opaque yekutieliObstruction : ℝ → ℕ → ℝ

/-- The leading Chebyshev coefficient `c_{(p−1)/2}` of the
    genus-filtration expansion (claimed `= 1` at the top level). -/
opaque leadingChebyshev : ℕ → ℝ

/-- **Yekutieli obstruction = leading Chebyshev coefficient = 1**
    at level `n = 5`, for `T_{2,p}` with odd prime `p` and `q ≠ 1`.

Faithful statement of the manuscript identity.  The equality of the
non-abelian `H²` class with the leading coefficient requires Yekutieli's
non-abelian-Stokes machinery (not in Mathlib), so the body is `sorry`. -/
-- Ref: [yekutieli2015] https://doi.org/10.1142/9537
-- Ref: [manuscript] quantum-observable-universe/brings-surface/yekutieli-leading-coefficient.md
theorem yekutieli_leading_coefficient (q : ℝ) (p : ℕ) (hp_odd : Odd p)
    (hq_ne : q ≠ 1) :
    yekutieliObstruction q p = leadingChebyshev p ∧
    yekutieliObstruction q p = 1 := by
  -- Needs: Yekutieli non-abelian multiplicative integration on surfaces;
  -- the obstruction is the curvature-2-form class of the descent, and its
  -- genus-filtration leading coefficient is the top Chebyshev coefficient = 1.
  sorry

/-- **Non-vanishing at `q ≠ 1`.**  Derived sorry-free from the main
    statement: `κ(T_{2,p}) = 1 ≠ 0`. -/
theorem yekutieli_obstruction_ne_zero (q : ℝ) (p : ℕ) (hp_odd : Odd p)
    (hq_ne : q ≠ 1) :
    yekutieliObstruction q p ≠ 0 := by
  intro h
  have h_eq_one := (yekutieli_leading_coefficient q p hp_odd hq_ne).2
  rw [h] at h_eq_one
  exact zero_ne_one h_eq_one

end QOU.Archimedean
