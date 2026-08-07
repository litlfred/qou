import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Algebra.Field.Basic

/-!
# `hA`, `hB`, `hC` are genuine five-term instances — the argument matching, proved

Bean `qou-rhyp`; roast item 1 of `qou-rstq`, which set this as the first thing to
attack:

> "If any of `hA`, `hB`, `hC` is not a genuine five-term instance — wrong
> argument, wrong branch — the whole derivation collapses. They were checked
> numerically to `1e-40`; check the *algebra* of the arguments independently."

This file is that check, in Lean. Probe
`qbeta_5two_route14_fiveterm_arguments_exact_probe.py` does it in exact
arithmetic in `ℚ(w)`; the two agree.

## The point

The five-term (Abel) relation

    L x + L y - L (x·y) - L (x(1-y)/(1-x·y)) - L (y(1-x)/(1-x·y)) = 0

determines its last three arguments **as rational functions of `(x, y)`**. So
"`hA` is a five-term instance" is not a numerical claim — it is the claim that
those rational functions evaluate to the arguments `hA` actually names. A check
to `1e-40` cannot distinguish that from "some other identity that happens to
hold at these points". Matching the arguments *identically* can.

## The generator

Everything is written in terms of `x = w₂`, which is itself a root of the same
cubic (`σ z = (z-1)/z` is an order-3 automorphism of `ℚ(w)`, and `w₂ = σ w₁`).
In that generator the argument dictionary is as simple as it ever gets:

    q = 1/(2-x)        r = x/(x+1)        s = (1-x)/x

and it is worth seeing which identities need the cubic and which do not:

| identity | needs |
|---|---|
| `arg_A2`, `arg_B1`, `arg_C1` | **nothing** — true for every `x` |
| `arg_A1`, `arg_B2` | the minimal polynomial |
| `arg_C2` | the minimal polynomial, in the form `(1-x)²(1+x) = x²` — i.e. `bloch_key` |

`arg_C2` is `FiveTwoCyclotomicBloch.bloch_key` at a different point: the same
identity that made the Bloch-group element `2[w] + [-w]` work turns up again as
the reason `hC`'s last argument is `1 - r`. That is not a coincidence worth
hiding in a comment, so it is stated as a theorem.

## Two collapses that make the instances legible

`arg_B1` says `(1-x)·q = 1-q`, so `hB`'s denominator `1 - x·y` **collapses to
`q`** — which is why its fifth argument comes out as exactly `x`, with no
denominator left. `arg_C1` says `x·s = 1-x`, so `hC`'s denominator collapses to
`x`, and its fourth argument is exactly `1-s`. Both are division-free facts.

## Scope — what is and is not proved here

Proved: the argument matching, over any `Field`, with the non-vanishing
hypotheses stated rather than assumed.

One of them turned out not to be needed. `arg_B2` and `arg_C2` were first stated
with `x ≠ 1`, on the reasoning that `s = (1-x)/x` needs `x` invertible. But the
*relation* `s·x = 1-x` already forces it: at `x = 0` it reads `0 = 1`. So
`ne_zero_of_hs` assumes nothing beyond `hs`, and the two theorems lost a
hypothesis. Worth recording as a small instance of a general point — a
multiplicative defining relation often carries its own non-degeneracy, and
adding the side condition by reflex hides that.

**Not proved: the five-term relation itself.** That is classical (Abel) and
remains the one open analytic input to the level-7 numerators. This file shows
the three hypotheses are instances *of* it; it does not show it holds.

**The 5₂ sum rule remains verified to 80 dps, unproved.**
-/

namespace QOU.QBeta.FiveTwoFiveTermArguments

variable {K : Type*} [Field K] {x q r s : K}

/-- `q = 1/(2-x)` forces `2 - x` to be a unit. -/
theorem two_sub_ne_zero (hq : q * (2 - x) = 1) : (2 : K) - x ≠ 0 := by
  intro h
  rw [h, mul_zero] at hq
  exact zero_ne_one hq

/-- `s = (1-x)/x` already forces `x` to be a unit, with nothing else assumed: at
`x = 0` the relation `s·x = 1-x` reads `0 = 1`. -/
theorem ne_zero_of_hs (hs : s * x = 1 - x) : x ≠ 0 := by
  intro h
  rw [h, mul_zero] at hs
  norm_num at hs

/-! ### `hA` — the diagonal instance `x = y = w₂` -/

/-- **`arg_A1`**: the third argument. `x·y = x²` at the diagonal, and it equals
`1 - q`. This needs the minimal polynomial. -/
theorem arg_A1 (hx : x ^ 3 - 2 * x ^ 2 - x + 1 = 0) (hq : q * (2 - x) = 1) :
    x * x = 1 - q := by
  have h2 := two_sub_ne_zero hq
  have key : (x * x - (1 - q)) * (2 - x) = 0 := by linear_combination -hx + hq
  rcases mul_eq_zero.mp key with h | h
  · linear_combination h
  · exact absurd h h2

/-- **`arg_A2`**: the fourth and fifth arguments coincide at the diagonal, and
`x(1-x)/(1-x²) = x/(1+x) = r`. Note this is true for **every** `x` — the cubic
plays no part. Stated division-free. -/
theorem arg_A2 (hr : r * (x + 1) = x) : r * (1 - x * x) = x * (1 - x) := by
  linear_combination (1 - x) * hr

/-! ### `hB` — the instance `x = 1 - w₂`, `y = q` -/

/-- **`arg_B1`**: the third argument, `(1-x)·q = 1-q`. True for every `x`; and it
is what makes `hB`'s denominator `1 - x·y` collapse to `q`. -/
theorem arg_B1 (hq : q * (2 - x) = 1) : (1 - x) * q = 1 - q := by
  linear_combination hq

/-- **`hB`'s denominator collapses**: `1 - (1-x)·q = q`. Immediate from `arg_B1`,
and the reason the fifth argument `q(1-(1-x))/(1-(1-x)q) = q·x/q` is exactly
`x`. -/
theorem hB_denom (hq : q * (2 - x) = 1) : 1 - (1 - x) * q = q := by
  have h := arg_B1 hq
  linear_combination -h

/-- **`arg_B2`**: the fourth argument. `(1-x)(1-q)/q = 1-s`, stated division-free
as `(1-s)·q = (1-x)(1-q)`. This needs the minimal polynomial. -/
theorem arg_B2 (hx : x ^ 3 - 2 * x ^ 2 - x + 1 = 0) (hq : q * (2 - x) = 1)
    (hs : s * x = 1 - x) :
    (1 - s) * q = (1 - x) * (1 - q) := by
  have hx0 := ne_zero_of_hs hs
  have h2 := two_sub_ne_zero hq
  have key : ((1 - s) * q - (1 - x) * (1 - q)) * (x * (2 - x)) = 0 := by
    linear_combination -hx + (2 * x - x ^ 2 - x * s) * hq - hs
  rcases mul_eq_zero.mp key with h | h
  · linear_combination h
  · rcases mul_eq_zero.mp h with h' | h'
    · exact absurd h' hx0
    · exact absurd h' h2

/-! ### `hC` — the instance `x = w₂`, `y = s` -/

/-- **`arg_C1`**: the third argument, `x·s = 1-x`. This is the *defining*
relation of `s`, so it is free — and it makes `hC`'s denominator `1 - x·s`
collapse to `x`. -/
theorem arg_C1 (hs : s * x = 1 - x) : x * s = 1 - x := by linear_combination hs

/-- **`hC`'s denominator collapses**: `1 - x·s = x`. The reason the fourth
argument `x(1-s)/(1-x·s)` is exactly `1-s`. -/
theorem hC_denom (hs : s * x = 1 - x) : 1 - x * s = x := by
  have h := arg_C1 hs
  linear_combination -h

/-- **`arg_C2`**: the fifth argument. `s(1-x)/x = 1-r`, division-free as
`(1-r)·x = s(1-x)`.

This is `bloch_key` again: clearing `r = x/(x+1)` and `s = (1-x)/x` turns it into
`x² = (1-x)²(1+x)`, exactly
`QOU/QBeta/FiveTwoCyclotomicBloch.bloch_key`. The identity that made the Bloch
element `2[w] + [-w]` work is the same one that fixes `hC`'s last argument. -/
theorem arg_C2 (hx : x ^ 3 - 2 * x ^ 2 - x + 1 = 0) (hr : r * (x + 1) = x)
    (hs : s * x = 1 - x) :
    (1 - r) * x = s * (1 - x) := by
  have hx0 := ne_zero_of_hs hs
  have hx1' : x + 1 ≠ 0 := by
    intro h
    have hxv : x = -1 := by linear_combination h
    rw [hxv] at hx
    norm_num at hx
  have key : ((1 - r) * x - s * (1 - x)) * (x * (x + 1)) = 0 := by
    linear_combination (-1 : K) * hx + (-x ^ 2) * hr + (x ^ 2 - 1) * hs
  rcases mul_eq_zero.mp key with h | h
  · linear_combination h
  · rcases mul_eq_zero.mp h with h' | h'
    · exact absurd h' hx0
    · exact absurd h' hx1'

/-! ### The identity behind `arg_C2`, stated on its own

Worth isolating, because it is the bridge to `FiveTwoCyclotomicBloch`. -/

/-- `bloch_key` in the `w₂` generator: `(1-x)²(1+x) = x²` for any root of the
cubic. Identical to `FiveTwoCyclotomicBloch.bloch_key`; restated here so the
connection to `arg_C2` is a `linear_combination` and not a comment. -/
theorem bloch_key' (hx : x ^ 3 - 2 * x ^ 2 - x + 1 = 0) :
    (1 - x) ^ 2 * (1 + x) = x ^ 2 := by linear_combination hx

end QOU.QBeta.FiveTwoFiveTermArguments
