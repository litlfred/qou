/-
# The bar involution's domain obstruction — why the parity read-off needs a pair

Companion to `HabiroEvaluationTrichotomy.lean` (PR #5084), which showed a Habiro
series admits a continuous evaluation only at roots of unity, so the substrate
anchor `q₀ ≈ 1.10998 > 1` has no such value. This file formalizes the
complementary — and sharper — obstruction, which is about *domains* rather than
convergence:

**the bar involution `q ↦ q⁻¹` does not preserve the unit ball.**

A carrier written as a q-series has a domain contained in some ball; the
convergent side of the substrate bar-pair is `q₀⁻¹ ≈ 0.90092 < 1`. But then
`q₀` itself is *outside* that domain, so the bar-even and bar-odd projections

    F^even(q) = (F(q) + F(q⁻¹))/2,     F^odd(q) = (F(q) − F(q⁻¹))/2

are **not formable** — not "hard to compute", not "divergent", simply not
defined, because one of the two arguments is not in the domain. This is why
`qou-qb8g`'s programme of reading the parity off the fibre object cannot be run
with a single series, and why the object required is a *pair* (or a state
integral holomorphic off the reals) in the Garoufalidis–Zagier shape.

The results, generic-first per §7c:

* `abs_inv_lt_one_iff` / `not_mem_ball_and_inv_mem_ball` — for `q ≠ 0` in a
  linear ordered field, `|q| < 1` and `|q⁻¹| < 1` are mutually exclusive. So no
  point of the open unit ball has its bar-partner in the ball.

* `bar_pair_not_formable_of_subset_ball` — the statement as used: if a carrier's
  domain `S` sits inside the open unit ball, then for every nonzero `q` at most
  one of `q`, `q⁻¹` lies in `S`. The projections above are undefined throughout.

* `bar_modulus_stable_iff_abs_eq_one` — **the positive half, and the reason the
  Habiro ring is built where it is.** A nonzero point has `|q⁻¹| = |q|` if and
  only if `|q| = 1`. The bar involution's modulus-fixed locus is exactly the
  unit circle — precisely where the roots of unity live, precisely where
  `HabiroEvaluationTrichotomy.qPoch_eq_zero_of_pow_eq_one` says the evaluation
  exists. The two files therefore agree on one picture:

  | locus | bar-stable? | Habiro evaluation? |
  |---|---|---|
  | roots of unity (`\|q\| = 1`) | yes | yes (eventually zero) |
  | substrate anchor (`q₀ > 1`) | no | no (diverges) |
  | bar partner (`q₀⁻¹ < 1`) | no | no (nonzero limit) |

  Neither archimedean member of the substrate bar-pair is bar-stable, and
  neither admits the evaluation. The one locus that has both is the circle.

* `substrate_pair_straddles_unit_circle` — instantiated at the substrate: for
  `1 < q`, `q` is outside the closed ball and `q⁻¹` is strictly inside. The pair
  straddles the circle rather than sitting on it.

**Scope-(b), invariant named.** The invariant is that `q ↦ q⁻¹` maps the open
unit ball's nonzero points to the ball's complement, so a ball-contained domain
is never bar-stable. This is a proved structural exclusion of the
*single-series* parity read-off. It is **not** an exclusion of the parity
programme: a pair `(F, F̃)`, or a function holomorphic on `ℂ ∖ ℝ`, has both
arguments in its domain by construction and is untouched. Nothing here bears on
(H1) `c₃^even = −Vol(4₁)` one way or the other.
-/

import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Analysis.Normed.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

namespace QOU.QBeta.BarInvolutionDomainObstruction

/-! ## The involution does not preserve the unit ball -/

/-- For a nonzero `q` in a linear ordered field, `|q⁻¹| < 1 ↔ 1 < |q|`.

Generic per §7c: this is order-and-field content, no archimedean input beyond
the ordering itself, so it is stated over `[Field K] [LinearOrder K] [IsStrictOrderedRing K]`
rather than `ℝ`. -/
theorem abs_inv_lt_one_iff {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] {q : K} (hq : q ≠ 0) :
    |q⁻¹| < 1 ↔ 1 < |q| := by
  have hpos : 0 < |q| := abs_pos.mpr hq
  rw [abs_inv]
  constructor
  · intro h
    -- |q|⁻¹ < 1 with |q| > 0 gives 1 < |q|
    have := (inv_lt_one_iff₀ (a := |q|)).mp h
    rcases this with h0 | h1
    · linarith
    · exact h1
  · intro h
    exact inv_lt_one_of_one_lt₀ h

/-- **The obstruction, pointwise.** For `q ≠ 0`, the point and its bar-partner
are never both in the open unit ball. -/
theorem not_mem_ball_and_inv_mem_ball {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] {q : K}
    (hq : q ≠ 0) : ¬ (|q| < 1 ∧ |q⁻¹| < 1) := by
  rintro ⟨h1, h2⟩
  have : 1 < |q| := (abs_inv_lt_one_iff hq).mp h2
  linarith

/-- **The obstruction, as used.** If a carrier's domain `S` is contained in the
open unit ball, then for every nonzero `q` at most one of `q`, `q⁻¹` lies in `S`.

Consequently `F(q) + F(q⁻¹)` — hence the bar-even and bar-odd projections — is
not formable anywhere on `S`. Not divergent: undefined. -/
theorem bar_pair_not_formable_of_subset_ball {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (S : Set K) (hS : ∀ x ∈ S, |x| < 1) {q : K} (hq : q ≠ 0) :
    ¬ (q ∈ S ∧ q⁻¹ ∈ S) := by
  rintro ⟨hqS, hiS⟩
  exact not_mem_ball_and_inv_mem_ball hq ⟨hS q hqS, hS q⁻¹ hiS⟩

/-! ## The positive half: the modulus-fixed locus is the unit circle -/

/-- **A nonzero point is modulus-stable under the bar involution iff it lies on
the unit circle.**

This is the structural reason the Habiro ring is built at roots of unity and not
at an archimedean anchor: `|q| = 1` is exactly the locus where `q` and `q⁻¹`
have the same modulus, so a domain can contain both. Pairs with
`HabiroEvaluationTrichotomy.qPoch_eq_zero_of_pow_eq_one`, which says the
evaluation exists there. -/
theorem bar_modulus_stable_iff_abs_eq_one {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {q : K} (hq : q ≠ 0) : |q⁻¹| = |q| ↔ |q| = 1 := by
  have hpos : 0 < |q| := abs_pos.mpr hq
  rw [abs_inv]
  constructor
  · intro h
    -- |q|⁻¹ = |q| with |q| > 0 forces |q|^2 = 1, hence |q| = 1 by positivity
    have hne : |q| ≠ 0 := ne_of_gt hpos
    have hsq : |q| * |q| = 1 := by
      field_simp at h
      linarith [h]
    nlinarith [hpos, hsq]
  · intro h
    rw [h]
    simp

/-! ## Instantiated at the substrate -/

/-- **The substrate bar-pair straddles the unit circle.** For real `q > 1` the
anchor is outside the closed unit ball and its bar-partner is strictly inside.

So neither member sits on the modulus-fixed locus of
`bar_modulus_stable_iff_abs_eq_one`, and by
`not_mem_ball_and_inv_mem_ball` no ball-shaped domain holds both. -/
theorem substrate_pair_straddles_unit_circle {q : ℝ} (hq : 1 < q) :
    1 < |q| ∧ |q⁻¹| < 1 := by
  have hq0 : q ≠ 0 := by linarith
  have habs : |q| = q := abs_of_pos (by linarith)
  refine ⟨by rw [habs]; exact hq, ?_⟩
  exact (abs_inv_lt_one_iff hq0).mpr (by rw [habs]; exact hq)

/-- Neither member of a substrate bar-pair is modulus-stable. -/
theorem substrate_pair_not_bar_stable {q : ℝ} (hq : 1 < q) :
    |q⁻¹| ≠ |q| := by
  have hq0 : q ≠ 0 := by linarith
  intro h
  have habs : |q| = q := abs_of_pos (by linarith)
  have : |q| = 1 := (bar_modulus_stable_iff_abs_eq_one hq0).mp h
  rw [habs] at this
  linarith

end QOU.QBeta.BarInvolutionDomainObstruction
