import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Algebra.Field.Basic
import QOU.QBeta.FiveTwoLevelSevenLadder

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

Also proved, at the end of the file: the **implication**. `hA_of_five_term`,
`hB_of_five_term`, `hC_of_five_term` each take the five-term relation with its
own arguments spelled out — no identification smuggled into the statement — and
deliver the ladder's hypothesis verbatim. With those, the twelve hypotheses of
`FiveTwoLevelSevenLadder.numerators_original_form` rest on exactly **one**
unproved input.

**Not proved: the five-term relation itself.** That is classical (Abel) and is
now the sole open analytic input to the level-7 numerators. This file shows the
three hypotheses are instances *of* it, and that they follow *from* it; it does
not show it holds.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
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

/-! ### Wiring: the five-term relation *implies* `hA`, `hB`, `hC`

The identifications above are only worth having if they close the gap between
"the five-term relation holds at these three `(x,y)` pairs" and the ladder's
hypotheses verbatim. These three theorems do that. After them, the twelve
hypotheses of `FiveTwoLevelSevenLadder.numerators_original_form` rest on exactly
**one** unproved input: Abel's relation.

Each hypothesis is the relation with its own arguments written out — no
identification is smuggled into the statement, which is the point. -/

/-- `q = 1/(2-x)` forces `q` to be a unit: at `q = 0` the relation reads `0 = 1`. -/
theorem q_ne_zero (hq : q * (2 - x) = 1) : q ≠ 0 := by
  intro h
  rw [h, zero_mul] at hq
  exact zero_ne_one hq

/-- **`hA` from the diagonal five-term instance** `x = y = w₂`. -/
theorem hA_of_five_term (L : K → K)
    (hx : x ^ 3 - 2 * x ^ 2 - x + 1 = 0) (hq : q * (2 - x) = 1) (hr : r * (x + 1) = x)
    (hne : 1 - x * x ≠ 0)
    (five : L x + L x - L (x * x) - L (x * (1 - x) / (1 - x * x))
              - L (x * (1 - x) / (1 - x * x)) = 0) :
    2 * L x - L (1 - q) - 2 * L r = 0 := by
  have h1 : x * x = 1 - q := arg_A1 hx hq
  have h2 : x * (1 - x) / (1 - x * x) = r := by
    rw [div_eq_iff hne]
    linear_combination -arg_A2 hr
  rw [h2, h1] at five
  linear_combination five

/-- **`hB` from the five-term instance** `x = 1 - w₂`, `y = q`.

Its denominator `1 - (1-x)·q` collapses to `q` (`hB_denom`), which is why the
fifth argument reduces to `x` outright. -/
theorem hB_of_five_term (L : K → K)
    (hx : x ^ 3 - 2 * x ^ 2 - x + 1 = 0) (hq : q * (2 - x) = 1) (hs : s * x = 1 - x)
    (five : L (1 - x) + L q - L ((1 - x) * q)
              - L ((1 - x) * (1 - q) / (1 - (1 - x) * q))
              - L (q * (1 - (1 - x)) / (1 - (1 - x) * q)) = 0) :
    L (1 - x) + L q - L (1 - q) - L (1 - s) - L x = 0 := by
  have hq0 := q_ne_zero hq
  have hd : 1 - (1 - x) * q = q := hB_denom hq
  have h1 : (1 - x) * q = 1 - q := arg_B1 hq
  have h2 : (1 - x) * (1 - q) / (1 - (1 - x) * q) = 1 - s := by
    rw [hd, div_eq_iff hq0]
    linear_combination -arg_B2 hx hq hs
  have h3 : q * (1 - (1 - x)) / (1 - (1 - x) * q) = x := by
    rw [hd, div_eq_iff hq0]
    ring
  rw [h2, h3, h1] at five
  linear_combination five

/-- **`hC` from the five-term instance** `x = w₂`, `y = s`.

Its denominator `1 - x·s` collapses to `x` (`hC_denom`), which is why the fourth
argument reduces to `1 - s` outright. -/
theorem hC_of_five_term (L : K → K)
    (hx : x ^ 3 - 2 * x ^ 2 - x + 1 = 0) (hr : r * (x + 1) = x) (hs : s * x = 1 - x)
    (five : L x + L s - L (x * s) - L (x * (1 - s) / (1 - x * s))
              - L (s * (1 - x) / (1 - x * s)) = 0) :
    L x + L s - L (1 - x) - L (1 - s) - L (1 - r) = 0 := by
  have hx0 := ne_zero_of_hs hs
  have hd : 1 - x * s = x := hC_denom hs
  have h1 : x * s = 1 - x := arg_C1 hs
  have h2 : x * (1 - s) / (1 - x * s) = 1 - s := by
    rw [hd, div_eq_iff hx0]
    ring
  have h3 : s * (1 - x) / (1 - x * s) = 1 - r := by
    rw [hd, div_eq_iff hx0]
    linear_combination -arg_C2 hx hr hs
  rw [h2, h3, h1] at five
  linear_combination five

/-! ### Capstone: Abel's relation ⟹ the level-7 numerators

Everything in this lane composes into one statement. Its hypotheses are exactly
two things — the five-term relation at three points, and reflection at four —
and its conclusion is the three numerators `(17, 5, -1)`.

Read the hypothesis list as the honest bill: that is *all* that is still assumed
about `L`. The inversion and Landen hypotheses the ladder used to take are gone,
discharged by construction in `FiveTwoRogersExtend`; the argument identifications
are gone, proved above; the `hsw3` renaming is gone. What remains is Abel, and
reflection — and reflection is itself proved for the corpus's real `LiTwo` in
`FiveTwoRogersReflection`.

So on this branch of the chain there is **one** open input, and it is classical.
That is not the sum rule: the transport `x = 1 → x = -1` is still unformalized
(`qou-trns`), and `extend` is still not identified with the analytic
continuation in Lean (`qou-rstq` item 4). -/

/-- **Abel's five-term relation at three points, plus reflection at four, gives
the level-7 numerators `(17, 5, -1)`.**

The five-term hypotheses carry their own arguments — `x * (1 - y) / (1 - x * y)`
and the rest — so nothing about which instance is which is assumed here; that is
what `arg_A1` … `arg_C2` prove. -/
theorem numerators_of_abel (L : K → K) (L1 : K)
    (hx : x ^ 3 - 2 * x ^ 2 - x + 1 = 0) (hq : q * (2 - x) = 1)
    (hr : r * (x + 1) = x) (hs : s * x = 1 - x) (hne : 1 - x * x ≠ 0)
    -- reflection, at the four points of `(0,1)` in play
    (hrw : L (1 - x) = L1 - L x) (hrq : L (1 - q) = L1 - L q)
    (hrr : L (1 - r) = L1 - L r) (hrs : L (1 - s) = L1 - L s)
    -- Abel, at the three points -- with the relation's own arguments
    (fiveA : L x + L x - L (x * x) - L (x * (1 - x) / (1 - x * x))
               - L (x * (1 - x) / (1 - x * x)) = 0)
    (fiveB : L (1 - x) + L q - L ((1 - x) * q)
               - L ((1 - x) * (1 - q) / (1 - (1 - x) * q))
               - L (q * (1 - (1 - x)) / (1 - (1 - x) * q)) = 0)
    (fiveC : L x + L s - L (x * s) - L (x * (1 - s) / (1 - x * s))
               - L (s * (1 - x) / (1 - x * s)) = 0) :
    (7 * (2 * L1 + 2 * L x - L q) = 17 * L1)
      ∧ (7 * (2 * L x - L r) = 5 * L1)
      ∧ (7 * (-(2 * L1) + 2 * L x + L s) = -L1) :=
  FiveTwoLevelSevenLadder.numerators_of_five_term L L1 x q r s hrw hrq hrr hrs
    (hA_of_five_term L hx hq hr hne fiveA)
    (hB_of_five_term L hx hq hs fiveB)
    (hC_of_five_term L hx hr hs fiveC)

end QOU.QBeta.FiveTwoFiveTermArguments
