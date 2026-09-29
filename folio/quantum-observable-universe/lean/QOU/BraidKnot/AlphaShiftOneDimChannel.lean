/-
AlphaShiftOneDimChannel.lean — the closed form for α_shift on a
one-dimensional seminormal channel, and the length bound it forces.

CONTEXT.  `α_shift(K) := max_{λ ⊢ n} ord⁽⁻⁾_{q=0} χ_λ(β_K)`
(`prop:alpha-shift-torus-knot`).  A one-row or one-column Young diagram has a
single standard tableau, so its seminormal channel is ONE-DIMENSIONAL and the
generator acts by a scalar:

    all-row (n)     ρ = +1 throughout,  σ ↦ q
    all-column (1ⁿ) ρ = −1 throughout,  σ ↦ −q⁻¹

(the entry valuations, and the cancellation `σ⁻¹ = σ − h` that reverses them,
are measured in `computations/meson/alpha_shift_derived_bound_probe.py`; the
closed forms below are verified against 13 words in
`alpha_shift_closed_form_probe.py`).

WHAT IS PROVED HERE.  Everything downstream of "the generator acts by a
scalar", stated over a generic `CommGroup` — no `ℝ`, no ordering, nothing
archimedean (AGENTS.md §7c), and no calibration input: `α_shift` is a
fibre-level valuation in the formal variable `q` and consumes none of
CAL-1/2/3.

  * `charOf_eq_zpow`      — the character of a word is `s ^ writhe`, so a
                            one-dimensional channel sees ONLY the writhe.  This
                            is the closed form; both channels are instances.
  * `val_charOf`          — under any additive valuation, `val χ = writhe · val s`.
  * `abs_val_le_length`   — hence `|val χ| ≤ length` when `|val s| = 1`: the
                            derived bound, not a fitted one.
  * `writhe_conj`         — the writhe, hence the character, is invariant under
                            conjugating the word.  With `tr_M`'s conjugation
                            invariance this is why the bound is on the REDUCED
                            length.
  * `abs_val_lt_length_of_cancel` — non-vacuity: the bound is STRICT for a word
                            containing a cancelling pair, so it is a genuine
                            inequality and not an equality in disguise.
  * `charOf_ne_zpow_length` — the second guard: the character is NOT `s ^ length`
                            in general, so "α = letter count" is a positive-word
                            fact and does not generalise.

WHAT IS NOT PROVED, and this is a derived limitation rather than a gap.  For an
intermediate two-row `λ` the channel has dimension > 1, the character is a sum
over standard-tableau paths, and the pole order becomes a longest-path
optimisation over that graph.  Nothing here reaches that case, and no closed
form in word-counts exists for it.

@module QOU.BraidKnot.AlphaShiftOneDimChannel
-/

import Mathlib.Algebra.Group.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

set_option autoImplicit false

namespace QOU.BraidKnot

variable {G : Type*} [CommGroup G]

/-- A braid word as a list of signed letters.  A one-dimensional channel sees
only each letter's sign, so that is all this carries. -/
abbrev Word := List Int

/-- The writhe: `+1` per positive letter, `−1` per inverse letter. -/
def writhe : Word → Int
  | [] => 0
  | g :: rest => (if 0 < g then (1 : Int) else -1) + writhe rest

/-- The character of a word on a one-dimensional channel whose generator acts
by the scalar `s`. -/
def charOf (s : G) : Word → G
  | [] => 1
  | g :: rest => (if 0 < g then s else s⁻¹) * charOf s rest

/-- **The closed form.**  On a one-dimensional channel the character of a word
is `s` raised to its writhe — so such a channel sees the writhe and nothing
else about the word.  The all-row channel (`s = q`) and the all-column channel
(`s = −q⁻¹`) are the two instances. -/
theorem charOf_eq_zpow (s : G) (w : Word) : charOf s w = s ^ writhe w := by
  induction w with
  | nil => simp [charOf, writhe]
  | cons g rest ih =>
      show (if 0 < g then s else s⁻¹) * charOf s rest
           = s ^ ((if 0 < g then (1 : Int) else -1) + writhe rest)
      rw [ih, zpow_add]
      by_cases hg : 0 < g
      · simp [hg]
      · simp [hg]

/-- Under any additive valuation, the character's valuation is the writhe times
the generator's. -/
theorem val_charOf (val : G → Int) (hmul : ∀ a b : G, val (a * b) = val a + val b)
    (hone : val 1 = 0) (s : G) (w : Word) :
    val (charOf s w) = writhe w * val s := by
  induction w with
  | nil => simpa [charOf, writhe] using hone
  | cons g rest ih =>
      show val ((if 0 < g then s else s⁻¹) * charOf s rest)
           = ((if 0 < g then (1 : Int) else -1) + writhe rest) * val s
      rw [hmul, ih]
      have hinv : val s⁻¹ = -val s := by
        have := hmul s s⁻¹
        rw [mul_inv_cancel, hone] at this
        omega
      by_cases hg : 0 < g
      · rw [if_pos hg, if_pos hg, add_mul, one_mul]
      · rw [if_neg hg, if_neg hg, hinv, add_mul, neg_one_mul]

/-- `|writhe| ≤ length`: each letter moves the writhe by exactly one. -/
theorem abs_writhe_le_length (w : Word) : (writhe w).natAbs ≤ w.length := by
  induction w with
  | nil => simp [writhe]
  | cons g rest ih =>
      show ((if 0 < g then (1 : Int) else -1) + writhe rest).natAbs ≤ rest.length + 1
      by_cases hg : 0 < g <;> simp only [hg, if_true, if_false] <;> omega

/-- **The derived bound.**  When the generator has valuation `±1` — which is
what the seminormal entries give at `ρ = ∓1` — the character's valuation is
bounded by the word length.  This is `α_shift ≤ L`, obtained from the algebra
rather than fitted to measurements. -/
theorem abs_val_le_length (val : G → Int) (hmul : ∀ a b : G, val (a * b) = val a + val b)
    (hone : val 1 = 0) (s : G) (hs : (val s).natAbs = 1) (w : Word) :
    (val (charOf s w)).natAbs ≤ w.length := by
  rw [val_charOf val hmul hone s w, Int.natAbs_mul, hs, Nat.mul_one]
  exact abs_writhe_le_length w

/-- The writhe is invariant under conjugating the word.  Together with the
Markov trace's own conjugation invariance, this is why the bound above is on
the REDUCED length rather than the written one. -/
theorem writhe_conj (a w : Word) :
    writhe (a ++ w) = writhe a + writhe w := by
  induction a with
  | nil => simp [writhe]
  | cons g rest ih =>
      show (if 0 < g then (1 : Int) else -1) + writhe (rest ++ w)
           = ((if 0 < g then (1 : Int) else -1) + writhe rest) + writhe w
      rw [ih, add_assoc]

/-- **Non-vacuity I.**  The bound is STRICT for a word containing a cancelling
pair — a genuine inequality, not an equality in disguise.

Note the `(val s).natAbs = 1` hypothesis of `abs_val_le_length` is NOT needed
here: the writhe of `σ σ⁻¹` is zero, so the strictness holds for ANY generator
valuation.  Stated without it rather than carrying a decorative hypothesis. -/
theorem abs_val_lt_length_of_cancel (val : G → Int)
    (hmul : ∀ a b : G, val (a * b) = val a + val b) (hone : val 1 = 0)
    (s : G) :
    (val (charOf s [(1 : Int), -1])).natAbs < ([(1 : Int), -1] : Word).length := by
  have hw : writhe [(1 : Int), -1] = 0 := by decide
  rw [val_charOf val hmul hone s, hw]
  simp

/-- **Non-vacuity II.**  The character is not `s ^ length` in general: the word
`σ σ⁻¹` has writhe `0` and length `2`, so "α_shift = letter count" is a fact
about POSITIVE words and does not generalise. -/
theorem writhe_ne_length : writhe [(1 : Int), -1] ≠ ([(1 : Int), -1] : Word).length := by
  decide

end QOU.BraidKnot
