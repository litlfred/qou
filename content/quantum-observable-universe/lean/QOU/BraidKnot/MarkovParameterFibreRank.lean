import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic

/-!
# QOU.BraidKnot.MarkovParameterFibreRank

The Markov stabilisation parameter `z` and the fibre rank `N` are the same
datum, and the family they range over is never bar-invariant.

## Context

`markov-axioms-primitive` stipulates the Markov parameter `z` in axiom M3
(`τ(x · σₙ) = z · τ(x)`).  Two conventions are live in the corpus:

* **C** — `z = 1/(√q + 1/√q)`, used by ≥ 8 corpus sites and hard-coded in
  binding's Wenzl bridge (`computations/y_lambda_wenzl_bridge.py`).  It is
  *bar-invariant*: `z(q⁻¹) = z(q)`.
* **D** — `z = q³/(q² + 1)`, the Jones / `SU_q(2)` value.  It is *not*.

Separately, the Wenzl bridge's fractional rank condition `X = Qᴺ`
(with `Q = q²`, `X = qz/(1 - Q + qz)`) is equivalent to `z · [N]_q = qᴺ`,
so a choice of `z` *is* a choice of fibre rank.  Convention D is `N = 2`.

## What is proved here

`zRank N q = q^(2N-1)(q² - 1)/(q^(2N) - 1)` is the member of that family at
rank `N`, written without natural-number subtraction.  The results are:

* `zRank_two` — convention D is exactly rank `2`.
* `zRank_bar` — the **bar-covariance law** `zRank N q⁻¹ = zRank N q / q^(2N)`.
* `pow_two_mul_eq_one_of_zRank_bar_invariant` — hence bar-invariance of a
  nonzero `zRank N q` forces `q^(2N) = 1`.

Together these say: *no* fibre rank yields a bar-invariant Markov parameter
whenever `q^(2N) ≠ 1` — in particular at any substrate `q₀ > 1` and any
`N ≥ 1`.  So convention C's bar-invariance and a fibre reading of `z` cannot
both be had, and the choice between them cannot be deferred to a search over
`N`.

This is a statement about the family `qᴺ/[N]_q` only.  It says nothing about
which convention the corpus should adopt, and nothing about a Markov parameter
arising by some other route.

Base ring: a general `Field R` per AGENTS §7c — the argument is purely
algebraic, needing only inverses.  No ordering, no `Real.sqrt`, no archimedean
hypothesis; those belong on the far side of the substrate wall.

Companion compute:
`computations/markov_z_fibre_rank_bar_covariance_probe.py`
(witness `markov-z-fibre-rank-bar-covariance.witness.json`).
-/

namespace QOU.BraidKnot

variable {R : Type*} [Field R]

/-- The Markov stabilisation parameter at fibre rank `N`:
`zRank N q = q^(2N-1)·(q² - 1)/(q^(2N) - 1)`, equivalently `qᴺ/[N]_q`.

Written as `q^(2N)·(q² - 1) / (q·(q^(2N) - 1))` to avoid natural-number
subtraction in the exponent. -/
noncomputable def zRank (N : ℕ) (q : R) : R :=
  q ^ (2 * N) * (q ^ 2 - 1) / (q * (q ^ (2 * N) - 1))

/-- Convention D is rank `2`: `zRank 2 q = q³/(q² + 1)`.

The hypotheses are exactly non-degeneracy of the rank-2 parameter: `q ≠ 0`
and `q⁴ ≠ 1`, the latter split as `q² ≠ 1` and `q² ≠ -1`. -/
theorem zRank_two (q : R) (hq : q ≠ 0) (hm : q ^ 2 - 1 ≠ 0) (hp : q ^ 2 + 1 ≠ 0) :
    zRank 2 q = q ^ 3 / (q ^ 2 + 1) := by
  have h4 : q ^ (2 * 2) - 1 = (q ^ 2 - 1) * (q ^ 2 + 1) := by ring
  unfold zRank
  rw [h4]
  field_simp

/-- **Bar-covariance law.** Replacing `q` by `q⁻¹` rescales the rank-`N`
Markov parameter by `q^(-2N)`:

`zRank N q⁻¹ = zRank N q / q^(2N)`.

The whole family is bar-*covariant* of weight `q^(-2N)`; it is bar-invariant
only where `q^(2N) = 1`. -/
theorem zRank_bar (N : ℕ) (q : R) (hq : q ≠ 0) (hN : q ^ (2 * N) - 1 ≠ 0) :
    zRank N q⁻¹ = zRank N q / q ^ (2 * N) := by
  have hpow : q ^ (2 * N) ≠ 0 := pow_ne_zero _ hq
  have hN' : (1 : R) - q ^ (2 * N) ≠ 0 := fun h => hN (by linear_combination -h)
  have hinv : (q⁻¹) ^ (2 * N) = (q ^ (2 * N))⁻¹ := inv_pow q (2 * N)
  unfold zRank
  rw [hinv]
  field_simp
  ring

/-- Bar-invariance of a nonzero rank-`N` Markov parameter forces
`q^(2N) = 1`.

Contrapositive reading: at any `q` with `q^(2N) ≠ 1` — in particular any real
substrate `q₀ > 1` at any rank `N ≥ 1` — the rank-`N` Markov parameter is
**not** bar-invariant.  No fibre rank rescues bar-invariance. -/
theorem pow_two_mul_eq_one_of_zRank_bar_invariant
    (N : ℕ) (q : R) (hq : q ≠ 0) (hN : q ^ (2 * N) - 1 ≠ 0)
    (hz : zRank N q ≠ 0) (hbar : zRank N q⁻¹ = zRank N q) :
    q ^ (2 * N) = 1 := by
  have hpow : q ^ (2 * N) ≠ 0 := pow_ne_zero _ hq
  have h := zRank_bar N q hq hN
  rw [hbar] at h
  have key : zRank N q * q ^ (2 * N) = zRank N q := by
    conv_lhs => rw [h]
    exact div_mul_cancel₀ _ hpow
  have hfac : zRank N q * (q ^ (2 * N) - 1) = 0 := by linear_combination key
  rcases mul_eq_zero.mp hfac with h' | h'
  · exact absurd h' hz
  · linear_combination h'

end QOU.BraidKnot
