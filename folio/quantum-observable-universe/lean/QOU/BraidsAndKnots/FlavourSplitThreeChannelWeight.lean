/-
# The flavour split's `1/3` is the `q = 1` value of the corpus's own channel weight

## The gap this closes, and exactly how far

`QOU/Hecke/MarkovCrossingReversal.lean` identified the `(q² - q⁻²)` factor of
`conj:flavor-split-habiro-derivation`'s baseline as a Markov trace, and
`QOU/Hecke/FlavourSplitBarParity.lean` constrained the `ℏ_q²` by bar-parity and
vanishing order.  Both files record that **the `/3` was untouched** — bar-parity
cannot see it (`3` is bar-invariant) and neither can the order argument.

This file identifies it.  `docs/audits/2026-06-17-hecke-channel-chirality-binding.md`
carries three substrate weights per crossing,

    w_sym = w_alt = q²/(q⁴+4q²+1),      w_std = (q²+1)²/(q⁴+4q²+1)

and those are **the q-deformed Plancherel measure of `H₃`** — at `q = 1` they are
`1/6, 2/3, 1/6`, which is `(f^λ)²/n!` for the partitions `(3), (2,1), (1³)` with
`f^λ = 1, 2, 1` and `n! = 6` (`weights_at_one`, `classical_weights_eq_plancherel`).

Evaluate the `k = 2` crossing reversal on the three channels.  By
`CrossingReversalParity.reversal_two` the element is `2hσ - h²`, so in the audit's
`(c,d)` parametrisation `c = 2h`, `d = -h²`, and the channel values are

    sym  `c·q + d`      =  q² - q⁻²            =  R
    std  `c·z_D + d`    =  α·R                 α = (q⁴+1)/(q²+1)²
    alt  `-c/q + d`     =  -R

(`channel_sym`, `channel_std`, `channel_alt`).  The full weighted combination then
collapses, because the sym and alt terms cancel under `w_sym = w_alt`:

    w_sym·R + w_std·(α·R) + w_alt·(-R)  =  (q⁴+1)/(q⁴+4q²+1) · R    `weighted_channel_value`

and that weight ratio at `q = 1` is exactly **`1/3`** (`weightRatio_at_one`).

**So the block's `1/3` is the `q = 1` value of its own three-channel weight.**  The
constant is identified; it was never a free number.

## 🛑 What that does NOT settle, and the honest shape of what is left

Identifying where the `1/3` comes from is not the same as establishing that `1/3`
is the right object.  The corpus's expression pairs a **classical (`q = 1`)
measure** with **`q`-deformed channel values** and a `q`-deformed `ℏ_q²`.  Three
numbers are in play at the proton `q₀` and they are all different:

| object | value at `q₀` |
|---|---|
| fully deformed `w(q)` against `value(q)` | `0.338154459866` |
| classical `w(1)` against `value(q)` | `0.336936151003` |
| the corpus's `1/3` | `0.333333333333` |

The corpus uses the third — the fully classical one.  AGENTS.md's notation
register states the governing rule directly: *"Three partition-weight families …
are distinct at `q ≠ 1` and coincide at `q = 1`; never conflate."*  This is an
instance of that, and here it is not cosmetic: it is **1.45 %** on the weight, and
it moves the baseline from `-0.128 %` to `+1.32 %` against the measured split.

**Which of the three is correct is a modelling question this file does not
answer**, and per AGENTS.md §"NO FITTING" it must not be answered by residual —
note in particular that the *least* deformed option is the most accurate, so
choosing by accuracy would keep `1/3` for the wrong reason.  What is delivered is
the identification and the exact size of the fork.  Bean `qou-qqm4`.

## Base ring

Generic `Field R` throughout, `CharZero` where a statement divides by 3 or 6.
Nothing here needs an ordering, `Real.sqrt`, or any archimedean construct, so
there is no §7c wall to cross and no `ℝ` section.

Probe: `computations/qbeta/flavour_split_three_channel_weight_probe.py`
-/

import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.LinearCombination

namespace QOU.Hecke.FlavourSplitThreeChannelWeight

variable {R : Type*} [Field R]

/-- `h = q - q⁻¹`. -/
noncomputable def hOf (q : R) : R := q - q⁻¹

/-- The convention-D Markov parameter `z_D = q³/(q²+1)`. -/
noncomputable def zD (q : R) : R := q ^ 3 / (q ^ 2 + 1)

/-- The `k = 2` reversal value on the symmetric channel, `R = q² - q⁻²`. -/
noncomputable def symValue (q : R) : R := q ^ 2 - (q ^ 2)⁻¹

/-- `α = (q⁴+1)/(q²+1)²`, the augmentation-to-`z_D` ratio. -/
noncomputable def alphaOf (q : R) : R := (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2

/-- Common denominator of the three substrate weights. -/
noncomputable def weightDen (q : R) : R := q ^ 4 + 4 * q ^ 2 + 1

/-- `w_sym = w_alt = q²/(q⁴+4q²+1)` — the `(3)` and `(1³)` weights. -/
noncomputable def wSym (q : R) : R := q ^ 2 / weightDen q

/-- `w_std = (q²+1)²/(q⁴+4q²+1)` — the `(2,1)` weight. -/
noncomputable def wStd (q : R) : R := (q ^ 2 + 1) ^ 2 / weightDen q

/-- **The three weights are a probability measure**: they sum to 1 for every `q`
with `q⁴+4q²+1 ≠ 0`. -/
theorem weights_sum_one {q : R} (hd : weightDen q ≠ 0) :
    wSym q + wStd q + wSym q = 1 := by
  unfold wSym wStd
  rw [← add_div, ← add_div, div_eq_one_iff_eq hd]
  unfold weightDen
  ring

/-- **At `q = 1` the weights are `1/6, 2/3, 1/6`** — the classical Plancherel
measure of `S₃`. -/
theorem weights_at_one [CharZero R] :
    wSym (1 : R) = 1 / 6 ∧ wStd (1 : R) = 2 / 3 := by
  refine ⟨?_, ?_⟩
  · unfold wSym weightDen; norm_num
  · unfold wStd weightDen; norm_num

/-- **Those are exactly `(f^λ)²/n!`** for `λ ⊢ 3` with `f^λ = 1, 2, 1`, `n! = 6`. -/
theorem classical_weights_eq_plancherel [CharZero R] :
    ((1 : R) ^ 2 / 6 = 1 / 6) ∧ ((2 : R) ^ 2 / 6 = 2 / 3) ∧ ((1 : R) ^ 2 / 6 = 1 / 6) := by
  refine ⟨by norm_num, by norm_num, by norm_num⟩

/-- **Symmetric channel** `c·q + d` at `(c,d) = (2h, -h²)` is `R`. -/
theorem channel_sym {q : R} (hq : q ≠ 0) :
    2 * hOf q * q - hOf q ^ 2 = symValue q := by
  unfold hOf symValue
  field_simp
  ring

/-- **Standard channel** `c·z_D + d` is `α·R`. -/
theorem channel_std {q : R} (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    2 * hOf q * zD q - hOf q ^ 2 = alphaOf q * symValue q := by
  unfold hOf zD alphaOf symValue
  field_simp
  ring

/-- **Alternating channel** `-c/q + d` is `-R`. -/
theorem channel_alt {q : R} (hq : q ≠ 0) :
    2 * hOf q * (-q⁻¹) - hOf q ^ 2 = -symValue q := by
  unfold hOf symValue
  field_simp
  ring

/-- The weight the three-channel combination reduces to,
`(q⁴+1)/(q⁴+4q²+1)`. -/
noncomputable def weightRatio (q : R) : R := (q ^ 4 + 1) / weightDen q

/-- **The full three-channel weighted value collapses to `weightRatio · R`.**
The symmetric and alternating terms cancel because `w_sym = w_alt` and their
channel values are exact negatives, leaving the standard term alone. -/
theorem weighted_channel_value {q : R} (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    wSym q * symValue q + wStd q * (alphaOf q * symValue q)
        + wSym q * (-symValue q)
      = weightRatio q * symValue q := by
  unfold wSym wStd weightRatio alphaOf weightDen symValue at *
  field_simp
  ring

/-- **The corpus's `1/3` is this weight at `q = 1`.**  `(1+1)/(1+4+1) = 1/3` —
plain evaluation, since the denominator is `6 ≠ 0`. -/
theorem weightRatio_at_one [CharZero R] : weightRatio (1 : R) = 1 / 3 := by
  unfold weightRatio weightDen
  norm_num

/-- **The deformed weight equals `1/3` EXACTLY at the classical point.**
`weightRatio q = 1/3 ↔ q⁴ + 1 = 2q² ↔ (q² - 1)² = 0`, i.e. `q² = 1`.

This is the notation register's own rule made precise for this weight: the
`q`-deformed and classical measures *coincide at `q = 1` and nowhere else*.  So
using `1/3` at the substrate `q₀ ≈ 1.11` is a genuine choice of the classical
measure, not a harmless simplification — and by `weights_at_one` that is the
Plancherel measure of `S₃`.

(Corrected in authoring: this was first stated as `q⁴ = 2q²`, which is wrong —
`lean` rejected it.  `3(q⁴+1) = q⁴+4q²+1` gives `2q⁴ - 4q² + 2 = 0`, i.e.
`(q²-1)² = 0`.) -/
theorem weightRatio_eq_third_iff [CharZero R] {q : R} (hd : weightDen q ≠ 0) :
    weightRatio q = 1 / 3 ↔ q ^ 4 + 1 = 2 * q ^ 2 := by
  unfold weightRatio weightDen at *
  rw [div_eq_div_iff hd (by norm_num : (3 : R) ≠ 0)]
  constructor
  · intro h; linear_combination h / 2
  · intro h; linear_combination 2 * h

/-- The same condition in factored form: `q⁴ + 1 = 2q²` is `(q² - 1)² = 0`. -/
theorem classical_point_iff (q : R) :
    q ^ 4 + 1 = 2 * q ^ 2 ↔ (q ^ 2 - 1) ^ 2 = 0 := by
  constructor
  · intro h; linear_combination h
  · intro h; linear_combination h

/-! ### Why the block's two sections are different KINDS of object

This is the step that unifies the `/3` with the `k=3` / `k=2` gap the arc has
been carrying as a separate open item.

**A central element needs no measure.**  If every channel sees the same value `s`
— which is exactly what "central scalar" means, and what the block proves of
`σ³ - σ⁻³ = 3h + h³` — then the weighted combination returns `s` unchanged,
because the weights sum to 1 (`central_value_unweighted`).  No `1/3`, no measure,
nothing to choose.

**A non-central element does.**  `σ² - σ⁻² = h(σ + σ⁻¹)` is not central
(`CrossingReversalParity.reversal_two`), so it has three distinct channel values
and evaluating it *requires* picking a measure — which is where `weightRatio`,
and at `q = 1` the `1/3`, comes from.

So the block's narrative half and its formula half are not two numbers for one
object; they are **two different kinds of object**, and the `1/3` is the
fingerprint of the switch: it can only appear on the side that needs a measure.
Measured at the proton `q₀` against the observed split, the narrative object read
as its own centrality argument dictates — no measure, so no `1/3` — is
**+353.5 %**, against `-0.128 %` for the formula's. Scope (a): a measured negative
about what the block's own argument yields, with no invariant excluding a `k = 3`
route that supplies its normalisation some other way. -/

/-- **A central value passes through the channel average untouched.**  The three
weights sum to 1, so a quantity every channel agrees on is returned as-is — there
is no measure factor and in particular no `1/3` on this side. -/
theorem central_value_unweighted {q : R} (hd : weightDen q ≠ 0) (s : R) :
    wSym q * s + wStd q * s + wSym q * s = s := by
  have h : wSym q + wStd q + wSym q = 1 := weights_sum_one hd
  calc wSym q * s + wStd q * s + wSym q * s
      = (wSym q + wStd q + wSym q) * s := by ring
    _ = 1 * s := by rw [h]
    _ = s := one_mul s

/-- The block's narrative object, `σ³ - σ⁻³ = 3h + h³`, as a value. -/
noncomputable def k3Value (q : R) : R := 3 * hOf q + hOf q ^ 3

/-- It is the central scalar `q³ - q⁻³`, exactly as the block states. -/
theorem k3Value_eq {q : R} (hq : q ≠ 0) :
    k3Value q = q ^ 3 - (q ^ 3)⁻¹ := by
  unfold k3Value hOf
  field_simp
  ring

end QOU.Hecke.FlavourSplitThreeChannelWeight
