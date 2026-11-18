/-
Copyright (c) 2026 litlfred. All rights reserved.

# μ–p residual: the two-term bar-even sum is sign-forced and coefficient-pinned

Bean `qou-6gf9`. Successor to
`QOU/BraidKnot/MuPCorrectionAdmissibility.lean`, which proves that **no single**
bar-even small-height monomial carries the residual. That theorem quantifies
over one exponent pair `(k, m)`; a *sum* lies outside its statement, and the
corpus had never tested one — no probe, no Lean, no audit doc.

## What this adds

The immediate next shape is a two-term tail of the bar-even `w`-tower,

  `t = c₃·w³ + c₄·w⁴`,   `w := q·ℏ_q² = q + q⁻¹ − 2`,

with both coefficients of small height, `|c| ∈ [1/5, 5]`. Orders 3 and 4 are
the only pair that can bracket the residual: `no_small_height_w_monomial`
excludes `j ≤ 3` from above and `j ≥ 4` from below, so any two-term sum reaching
`t` must straddle exactly there.

That family is **not** empty — and it is far more constrained than "two free
small-height coefficients" suggests. Over the whole pin window
`q ∈ [11099/10000, 111/100]` and the whole residual window
`t ∈ [1.8e-7, 2.4e-7]`:

* `sum_signs_forced` — the tower must **alternate**: `0 < c₃` and `c₄ < 0`.
  Neither sign is assumed; both are consequences.
* `sum_c3_pinned` — `1/5 ≤ c₃ ≤ 1/4`. The leading coefficient is confined to an
  interval of width `1/20`, against a small-height band of width `48/10`: the
  cubic rung is pinned to about **1 %** of its a-priori range.
* `sum_c4_bounded` — `c₄ ≤ −4/5`, so the quartic rung occupies `[−5, −4/5]`,
  `44 %` of the band rather than the full `[−5, −1/5] ∪ [1/5, 5]`.

None of this identifies a correction, and it is not meant to: the entropy bound
(`σ_exp/t ≈ 10 %`) says matching cannot identify anything. It is the
formalize-first move — narrow the class **before** anyone searches it, so that a
derived pair can be checked against a sharp prediction rather than a wide band.
A derivation landing outside these intervals is refuted without a numerical
comparison.

## Scope

Scope-**(b)** for the stated class, and the class is narrow: a *two-term* tail
of the `w`-tower at orders `(3, 4)` with small-height coefficients. It says
nothing about three or more terms, about coefficients of genuinely non-unit
height, about an operator-valued correction, or about a correction that is not a
`w`-tower tail at all. As in the parent file, the bar-even precondition is
argued from the amphichirality of `4₁`, not proved, so every exclusion here is
conditional on it.

## Provenance of the numbers

`w(q₀) = 0.0108968667071222997524919780919` at the proton pin
`q₀ = 1.10997858275138080759166909561`
(`qou_substrate.constants.Q_50_DIGIT_STR`); `t = 2.1116491436e-7` from
`computations/mu-substrate-tension-audit-100dps.witness.json`
(`data.residual_ppb_at_canonical_q0 = 211.16491436`, CODATA 2022). At that pin
`t/w³ = 0.16319876` and `t/w⁴ = 14.976668`, so the exact feasible set is
`c₄ ∈ [−5, −3.3772317]`, `c₃ ∈ [1/5, 0.21768309]` — tighter than the
window-wide intervals proved below, which must hold for every `q` and every `t`
in their windows. Both are recomputed here at 50 dps rather than quoted: the
bean's own `t/w³ = 0.16211` is the superseded CODATA-2018 value.
-/

import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import QOU.BraidKnot.MuPCarrierBarParity
import QOU.BraidKnot.MuPCorrectionAdmissibility

namespace QOU.BraidKnot.MuPTwoTermSum

open QOU.BraidKnot.MuPCarrier
open QOU.BraidKnot.MuPCorrectionAdmissibility

/-! ## 1. Window facts

Everything below runs off the two `w`-bounds already proved in the parent file,
plus positivity of the relevant powers. -/

/-- `w > 0` on the pin window. -/
theorem wGen_pos (q : ℝ)
    (hq0 : (11099 : ℝ) / 10000 ≤ q) (hq1 : q ≤ (111 : ℝ) / 100) :
    (0 : ℝ) < wGen q := by
  have h := wGen_lower_bound q hq0 hq1
  linarith

/-! ## 2. The signs are forced

Neither sign is a hypothesis. `c₃ > 0` because a non-positive leading
coefficient of small height drives the whole sum negative, while `t > 0`;
`c₄ < 0` because a non-negative quartic term leaves the cubic term alone above
the top of the residual window — the same `(1/5)·w³ ≥ 2.5194e-7 > 2.4e-7`
estimate that `no_small_height_w_monomial` uses at `j = 3`. -/

/-- **The two-term bar-even tail must alternate.** If `c₃·w³ + c₄·w⁴ = t` with
both coefficients of small height, `q` in the pin window and `t` in the residual
window, then `c₃` is positive and `c₄` is negative.

**It is stronger than its signature.** Only `1/5 ≤ |c₃|` and `|c₄| ≤ 5` are
used — `_hc31` and `_hc40` are carried so the three theorems in this file take
the same hypotheses and compose without plumbing. **The check that establishes
this is deleting both binders and fixing the two positional call sites: the
proof closes unchanged.** Do *not* reach for the unused-variable linter here;
`linter.unusedVariables` does not fire on a binder prefixed with `_`, so its
silence on this signature is the underscore doing its job and says nothing
either way. (An earlier version of this docstring cited that silence as the
evidence. The claim was true and the evidence was not: a reviewer who checked
it as invited would have seen nothing and been unable to tell "unused" from
"warning suppressed". Caught by an independent verification pass.)

So the alternation holds for a quartic coefficient of *arbitrarily small*
height and for a cubic coefficient of *arbitrarily large* height;
small-heightness is needed only as a floor on `|c₃|` and a ceiling on `|c₄|`.
Do not read the extra binders as required. -/
theorem sum_signs_forced (q c₃ c₄ t : ℝ)
    (hq0 : (11099 : ℝ) / 10000 ≤ q) (hq1 : q ≤ (111 : ℝ) / 100)
    (hc30 : (1 : ℝ) / 5 ≤ |c₃|) (_hc31 : |c₃| ≤ 5)
    (_hc40 : (1 : ℝ) / 5 ≤ |c₄|) (hc41 : |c₄| ≤ 5)
    (htlo : (18 : ℝ) / 10 ^ 8 ≤ t) (hthi : t ≤ (24 : ℝ) / 10 ^ 8)
    (hsum : c₃ * wGen q ^ 3 + c₄ * wGen q ^ 4 = t) :
    0 < c₃ ∧ c₄ < 0 := by
  have hwlo : (108 : ℝ) / 10000 ≤ wGen q := wGen_lower_bound q hq0 hq1
  have hwhi : wGen q ≤ (11 : ℝ) / 1000 := wGen_upper_bound q hq0 hq1
  have hwpos : (0 : ℝ) < wGen q := wGen_pos q hq0 hq1
  have h3lo : ((108 : ℝ) / 10000) ^ 3 ≤ wGen q ^ 3 := by gcongr
  have h3hi : wGen q ^ 3 ≤ ((11 : ℝ) / 1000) ^ 3 := by gcongr
  have h4lo : ((108 : ℝ) / 10000) ^ 4 ≤ wGen q ^ 4 := by gcongr
  have h4hi : wGen q ^ 4 ≤ ((11 : ℝ) / 1000) ^ 4 := by gcongr
  have h3pos : (0 : ℝ) < wGen q ^ 3 := by positivity
  have h4pos : (0 : ℝ) < wGen q ^ 4 := by positivity
  have hc4abs := abs_le.mp hc41
  have htpos : (0 : ℝ) < t := by
    have : (0 : ℝ) < (18 : ℝ) / 10 ^ 8 := by norm_num
    linarith
  -- `c₃ > 0`: a non-positive leading coefficient of small height drives the
  -- whole sum negative, because the quartic term cannot rescue it —
  -- `-(1/5)·w³ + 5·w⁴ = w³·(5w − 1/5) < 0` for `w ≤ 11/1000`. Both bounds on
  -- `c₄` are needed here; `c₄·w⁴ ≥ 0` is the wrong direction and does not close
  -- the goal.
  have hc3pos : 0 < c₃ := by
    by_contra hle
    push_neg at hle
    rw [abs_of_nonpos hle] at hc30
    have hc3neg : c₃ ≤ -((1 : ℝ) / 5) := by linarith
    have hcube : c₃ * wGen q ^ 3 ≤ -((1 : ℝ) / 5) * wGen q ^ 3 :=
      mul_le_mul_of_nonneg_right hc3neg (le_of_lt h3pos)
    have hquart : c₄ * wGen q ^ 4 ≤ 5 * wGen q ^ 4 :=
      mul_le_mul_of_nonneg_right hc4abs.2 (le_of_lt h4pos)
    have hneg : -((1 : ℝ) / 5) * wGen q ^ 3 + 5 * wGen q ^ 4 < 0 :=
      calc -((1 : ℝ) / 5) * wGen q ^ 3 + 5 * wGen q ^ 4
          = wGen q ^ 3 * (5 * wGen q - 1 / 5) := by ring
        _ < 0 := mul_neg_of_pos_of_neg h3pos (by linarith)
    linarith
  have hc3ge : (1 : ℝ) / 5 ≤ c₃ := by
    rw [abs_of_pos hc3pos] at hc30
    exact hc30
  refine ⟨hc3pos, ?_⟩
  -- `c₄ ≥ 0` leaves the cubic term alone above the top of the window: the same
  -- `(1/5)·w³ ≥ 2.5194e-7 > 2.4e-7` estimate `no_small_height_w_monomial` uses.
  by_contra hge
  push_neg at hge
  have hquart : (0 : ℝ) ≤ c₄ * wGen q ^ 4 := mul_nonneg hge (le_of_lt h4pos)
  have hcube : (1 : ℝ) / 5 * wGen q ^ 3 ≤ c₃ * wGen q ^ 3 :=
    mul_le_mul_of_nonneg_right hc3ge (le_of_lt h3pos)
  have hbig : (24 : ℝ) / 10 ^ 8 < (1 : ℝ) / 5 * ((108 : ℝ) / 10000) ^ 3 := by
    norm_num
  linarith

/-! ## 3. The coefficients are pinned

With the signs fixed, both coefficients are bounded on both sides. The cubic
rung is the sharp one: `[1/5, 1/4]` is `1 %` of the small-height band. -/

/-- **The cubic rung is pinned to `[1/5, 1/4]`.** The lower bound is the
small-height hypothesis once the sign is known; the upper bound is
`c₃·w³ = t − c₄·w⁴ ≤ 24/10⁸ + 5·(11/1000)⁴`, against `w³ ≥ (108/10000)³`. The
margin is genuine but thin — `313205/10¹²` against `314928/10¹²`, `0.5471 %` —
so it is exact rational arithmetic, not a decimal estimate.

**`1/4` is content, not slack.** The sharp window-wide bound is
`313205/1259712 = 0.2486322`, so `1/4` leaves `0.00137`; a mutation to `24/100`
fails to close. Stated because a reader cannot otherwise tell a chosen round
number from a forced one. -/
theorem sum_c3_pinned (q c₃ c₄ t : ℝ)
    (hq0 : (11099 : ℝ) / 10000 ≤ q) (hq1 : q ≤ (111 : ℝ) / 100)
    (hc30 : (1 : ℝ) / 5 ≤ |c₃|) (hc31 : |c₃| ≤ 5)
    (hc40 : (1 : ℝ) / 5 ≤ |c₄|) (hc41 : |c₄| ≤ 5)
    (htlo : (18 : ℝ) / 10 ^ 8 ≤ t) (hthi : t ≤ (24 : ℝ) / 10 ^ 8)
    (hsum : c₃ * wGen q ^ 3 + c₄ * wGen q ^ 4 = t) :
    (1 : ℝ) / 5 ≤ c₃ ∧ c₃ ≤ (1 : ℝ) / 4 := by
  obtain ⟨hc3pos, _⟩ :=
    sum_signs_forced q c₃ c₄ t hq0 hq1 hc30 hc31 hc40 hc41 htlo hthi hsum
  have hwlo : (108 : ℝ) / 10000 ≤ wGen q := wGen_lower_bound q hq0 hq1
  have hwhi : wGen q ≤ (11 : ℝ) / 1000 := wGen_upper_bound q hq0 hq1
  have hwpos : (0 : ℝ) < wGen q := wGen_pos q hq0 hq1
  have h3pos : (0 : ℝ) < wGen q ^ 3 := by positivity
  have h4pos : (0 : ℝ) < wGen q ^ 4 := by positivity
  have h3lo : ((108 : ℝ) / 10000) ^ 3 ≤ wGen q ^ 3 := by gcongr
  have h4hi : wGen q ^ 4 ≤ ((11 : ℝ) / 1000) ^ 4 := by gcongr
  have hc4abs := abs_le.mp hc41
  refine ⟨?_, ?_⟩
  · rw [abs_of_pos hc3pos] at hc30
    exact hc30
  · by_contra hgt
    push_neg at hgt
    -- Lower bound on the cubic term from `c₃ > 1/4`.
    have hcube : (1 : ℝ) / 4 * wGen q ^ 3 < c₃ * wGen q ^ 3 := by
      exact mul_lt_mul_of_pos_right hgt h3pos
    have hcube' : (1 : ℝ) / 4 * ((108 : ℝ) / 10000) ^ 3 ≤ (1 : ℝ) / 4 * wGen q ^ 3 := by
      linarith
    -- Upper bound on the quartic term from `c₄ ≥ -5`.
    have hquart : -(5 : ℝ) * wGen q ^ 4 ≤ c₄ * wGen q ^ 4 :=
      mul_le_mul_of_nonneg_right hc4abs.1 (le_of_lt h4pos)
    have hquart' : -(5 : ℝ) * ((11 : ℝ) / 1000) ^ 4 ≤ -(5 : ℝ) * wGen q ^ 4 := by
      linarith
    have hnum : (24 : ℝ) / 10 ^ 8 + 5 * ((11 : ℝ) / 1000) ^ 4
        < (1 : ℝ) / 4 * ((108 : ℝ) / 10000) ^ 3 := by norm_num
    linarith

/-- **The quartic rung satisfies `c₄ ≤ −4/5`.** From
`c₄·w⁴ = t − c₃·w³ ≤ 24/10⁸ − (1/5)·(108/10000)³ = −11942.4/10¹²` against
`w⁴ ≤ (11/1000)⁴`. So the small-height band available to `c₄` is `[−5, −4/5]`,
not `[−5, −1/5] ∪ [1/5, 5]`. Margin `0.0956 %`.

**`−4/5` is content, not slack.** The sharp window-wide bound is `−0.8156820`,
so `−4/5` leaves `0.01568`; a mutation to `−82/100` fails to close. -/
theorem sum_c4_bounded (q c₃ c₄ t : ℝ)
    (hq0 : (11099 : ℝ) / 10000 ≤ q) (hq1 : q ≤ (111 : ℝ) / 100)
    (hc30 : (1 : ℝ) / 5 ≤ |c₃|) (hc31 : |c₃| ≤ 5)
    (hc40 : (1 : ℝ) / 5 ≤ |c₄|) (hc41 : |c₄| ≤ 5)
    (htlo : (18 : ℝ) / 10 ^ 8 ≤ t) (hthi : t ≤ (24 : ℝ) / 10 ^ 8)
    (hsum : c₃ * wGen q ^ 3 + c₄ * wGen q ^ 4 = t) :
    c₄ ≤ -((4 : ℝ) / 5) := by
  obtain ⟨hc3lo, _⟩ :=
    sum_c3_pinned q c₃ c₄ t hq0 hq1 hc30 hc31 hc40 hc41 htlo hthi hsum
  have hwlo : (108 : ℝ) / 10000 ≤ wGen q := wGen_lower_bound q hq0 hq1
  have hwhi : wGen q ≤ (11 : ℝ) / 1000 := wGen_upper_bound q hq0 hq1
  have hwpos : (0 : ℝ) < wGen q := wGen_pos q hq0 hq1
  have h3pos : (0 : ℝ) < wGen q ^ 3 := by positivity
  have h4pos : (0 : ℝ) < wGen q ^ 4 := by positivity
  have h3lo : ((108 : ℝ) / 10000) ^ 3 ≤ wGen q ^ 3 := by gcongr
  have h4hi : wGen q ^ 4 ≤ ((11 : ℝ) / 1000) ^ 4 := by gcongr
  by_contra hgt
  push_neg at hgt
  have hcube : (1 : ℝ) / 5 * wGen q ^ 3 ≤ c₃ * wGen q ^ 3 :=
    mul_le_mul_of_nonneg_right hc3lo (le_of_lt h3pos)
  have hcube' : (1 : ℝ) / 5 * ((108 : ℝ) / 10000) ^ 3 ≤ (1 : ℝ) / 5 * wGen q ^ 3 := by
    linarith
  have hquart : -((4 : ℝ) / 5) * wGen q ^ 4 < c₄ * wGen q ^ 4 :=
    mul_lt_mul_of_pos_right hgt h4pos
  have hquart' : -((4 : ℝ) / 5) * ((11 : ℝ) / 1000) ^ 4
      ≤ -((4 : ℝ) / 5) * wGen q ^ 4 := by linarith
  have hnum : (24 : ℝ) / 10 ^ 8
      < (1 : ℝ) / 5 * ((108 : ℝ) / 10000) ^ 3 - (4 : ℝ) / 5 * ((11 : ℝ) / 1000) ^ 4 := by
    norm_num
  linarith

/-! ## 4. What this does not say

`sum_signs_forced` is a statement about a *specific two-term shape*. Read the
arity before citing it:

* It is **not** an exclusion. The family is non-empty — at the proton pin,
  `(c₃, c₄) = (0.2014, −3.5)` reproduces `t` to `3.8e-4` relative. A future
  derivation may land in it.
* It is **not** a statement about three-term or longer tails, whose sign
  structure it does not constrain.
* It does **not** license reading the alternation as physical. An alternating
  cyclotomic tower is a familiar shape in quantum topology, and that is
  suggestive rather than evidential: the entropy bound still says a coefficient
  *matched* to `t` carries no information. The value of the alternation is that
  a **derived** pair now has a sharp prediction to fail.
-/

/-- Subtracting the quartic coefficient from negative four-fifths yields a non-negative difference under the two-term residual conditions. -/
theorem neg_four_fifths_sub_c4_nonneg (q c₃ c₄ t : ℝ)
    (hq0 : (11099 : ℝ) / 10000 ≤ q) (hq1 : q ≤ (111 : ℝ) / 100)
    (hc30 : (1 : ℝ) / 5 ≤ |c₃|) (hc31 : |c₃| ≤ 5)
    (hc40 : (1 : ℝ) / 5 ≤ |c₄|) (hc41 : |c₄| ≤ 5)
    (htlo : (18 : ℝ) / 10 ^ 8 ≤ t) (hthi : t ≤ (24 : ℝ) / 10 ^ 8)
    (hsum : c₃ * wGen q ^ 3 + c₄ * wGen q ^ 4 = t) :
    0 ≤ -((4 : ℝ) / 5) - c₄ :=
  sub_nonneg.mpr (sum_c4_bounded q c₃ c₄ t hq0 hq1 hc30 hc31 hc40 hc41 htlo hthi hsum)

end QOU.BraidKnot.MuPTwoTermSum
