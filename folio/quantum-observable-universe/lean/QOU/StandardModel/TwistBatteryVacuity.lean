/-
Copyright (c) 2026 QOU contributors. All rights reserved.

# The strand-twist hypercharge battery reduces to one equation

`eightfold-open-problems.md` item 2 and `flavor-charge-assignments.md`
report the strand-twist candidate's enumeration as

> of `10,000` helon-style assignments, only `4` survive the spectrum +
> nucleon-GMN battery; the `u`-quark twist `{0,1,1}` and the electron twist
> `{-1,-1,-1}` are uniquely determined.

Read as stated that is a `2500 : 1` filter, and the two uniquely-determined
multisets look like a strong result.  This file shows the filter is a
**definition unfolding**, and that the surviving count is pure multiset
counting.

The candidate is `Y_t = 2(Q_twist - I₃)` with `Q_twist = T(t)/3`, where
`T(t) = Σᵢ tᵢ` is the total of the per-strand framing datum
(`def:strand-twist-datum`).

## What is proved here

* `spectrum_iff_total_twist` -- the spectrum battery `Y_t = Y_SM` holds
  **iff** `T = 3Q`.  Since `Y_SM = 2(Q - I₃)` by Gell-Mann--Nishijima, both
  sides carry the same `-2I₃`, which cancels: the battery says nothing
  about isospin, only that the total twist equals three times the charge.
  That is the *defining* equation of `Q_twist`, not a test of it.
* `nucleon_totals_entailed` -- the nucleon-doublet check is **entailed** by
  the spectrum battery.  With `T_p = 2T_u + T_d` and `T_n = T_u + 2T_d`,
  `T = 3Q` for the quarks forces `T_p = 3Q_p` and `T_n = 3Q_n` by charge
  additivity alone.  It filters nothing.
* `nucleon_second_clause_redundant` -- worse, the nucleon check as
  implemented tests one condition twice: `2(T_p/3 - 1/2) = 1` is
  algebraically `T_p = 3`, which is its own first clause.
* `survivor_count_is_multiset_counting` -- the surviving assignment count
  `4` is exactly `1 × 2 × 2 × 1`, the number of multisets of three twists
  from `{-1,0,1}` with the required sums `(2, -1, 0, -3)` for
  `(u, d, νₑ, e⁻)`.  `10,000 = 10⁴` was never a search space that the
  battery cut down; each flavour is filtered independently by one linear
  equation.

The `Z₆` compatibility condition is **not modelled here** because it is not
a filter: in `strand_twist_y_battery.py`, `z6_ok` is a function of the
Standard-Model table alone (`tau`, `w`, `Y`) and never sees the candidate
assignment.  It runs as an input `assert`, so it cannot exclude any twist
multiset.

## Honest scope

This is a **scope-(a)** statement about the battery's information content,
in the sense of AGENTS.md §"Before declaring refuted".  It does **not**
refute the strand-twist datum as a hypercharge candidate, and it does not
show any twist assignment is wrong.  It shows the stated enumeration does
not *corroborate* the candidate: passing it is equivalent to choosing `t`
with `Σtᵢ = 3Q`, which is always possible and is what `Q_twist` means.

The chapter already records the real open content honestly -- whether the
twist multisets are *forced by the categorical braid words* rather than
merely consistent with them.  This file sharpens why that is the whole
question: nothing else in the battery constrains anything.

Everything is integer arithmetic: no division, no field, no characteristic
hypothesis (§7c).
-/

import Mathlib.Data.Int.Basic
import Mathlib.Data.List.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace QOU.StandardModel.TwistBattery

/-! ### 1. The spectrum battery is `T = 3Q` -/

/-- **The spectrum battery is exactly `T = 3Q`.**

Both the candidate `Y_t = 2(Q_twist - I₃)` and the Standard-Model value
`Y_SM = 2(Q - I₃)` carry the same `-2I₃` term, so requiring them equal
cancels the isospin entirely.  Stated in the cleared `3×` normalisation
(`threeQ = 3Q`, `T` the total twist, `twoI₃ = 2I₃`), where the candidate
reads `Y_t = (2T - 3·twoI₃)/3` and the target `Y = (2·threeQ - 3·twoI₃)/3`;
clearing the common denominator and the common `I₃` term leaves `2T = 2·threeQ`.

No characteristic or field hypothesis: this is `ℤ`-linear. -/
theorem spectrum_iff_total_twist (T threeQ twoI₃ : ℤ) :
    2 * T - 3 * twoI₃ = 2 * threeQ - 3 * twoI₃ ↔ T = threeQ := by
  constructor
  · intro h; linarith
  · intro h; rw [h]

/-- The isospin term is irrelevant to the battery: for *any* two isospin
values the criterion is unchanged.  This is why the battery tests nothing
about `I₃`, only about the total twist. -/
theorem spectrum_independent_of_isospin (T threeQ twoI₃ twoI₃' : ℤ) :
    (2 * T - 3 * twoI₃ = 2 * threeQ - 3 * twoI₃) ↔
    (2 * T - 3 * twoI₃' = 2 * threeQ - 3 * twoI₃') := by
  rw [spectrum_iff_total_twist, spectrum_iff_total_twist]

/-! ### 2. The nucleon-doublet check is entailed, and internally redundant -/

/-- **The nucleon check filters nothing.**

The proton is `uud` and the neutron `udd`, so their total twists are
`T_p = 2T_u + T_d` and `T_n = T_u + 2T_d`, while their charges are
`Q_p = 2Q_u + Q_d` and `Q_n = Q_u + 2Q_d`.  If the spectrum battery holds
for the quarks (`T = 3Q` each), then `T = 3Q` holds for the nucleons
automatically -- by charge additivity alone.  No assignment surviving the
spectrum battery can fail the nucleon battery. -/
theorem nucleon_totals_entailed (Tu Td Qu Qd : ℤ)
    (hu : Tu = 3 * Qu) (hd : Td = 3 * Qd) :
    2 * Tu + Td = 3 * (2 * Qu + Qd) ∧ Tu + 2 * Td = 3 * (Qu + 2 * Qd) := by
  constructor <;> rw [hu, hd] <;> ring

/-- Specialised to the physical first-generation charges `3Q_u = 2`,
`3Q_d = -1`: the proton total is `3` and the neutron total is `0`, which are
precisely the two values the implemented nucleon check tests for. -/
theorem nucleon_totals_are_three_and_zero (Tu Td : ℤ)
    (hu : Tu = 2) (hd : Td = -1) :
    2 * Tu + Td = 3 ∧ Tu + 2 * Td = 0 := by
  constructor <;> rw [hu, hd] <;> ring

/-- **The nucleon check tests one condition twice.**

As implemented the proton clause is `T_p/3 = 1 ∧ 2·(T_p/3 - 1/2) = 1`.
Cleared of denominators the second clause is `2T_p - 3 = 3`, i.e. `T_p = 3`
— identical to the first.  The apparent two-part Gell-Mann--Nishijima check
is a single equation stated twice. -/
theorem nucleon_second_clause_redundant (Tp : ℤ) :
    (2 * Tp - 3 = 3) ↔ (Tp = 3) := by
  constructor
  · intro h; linarith
  · intro h; subst h; decide

/-- Same for the neutron clause: `2·(T_n/3 + 1/2) = 1` clears to `T_n = 0`,
its own first clause. -/
theorem neutron_second_clause_redundant (Tn : ℤ) :
    (2 * Tn + 3 = 3) ↔ (Tn = 0) := by
  constructor
  · intro h; linarith
  · intro h; subst h; decide

/-! ### 3. The survivor count is multiset counting -/

/-- The ten multisets of three strand twists drawn from `{-1, 0, +1}`,
listed as sorted triples.  This is the per-flavour candidate space. -/
def twistMultisets : List (List ℤ) :=
  [[-1, -1, -1], [-1, -1, 0], [-1, -1, 1], [-1, 0, 0], [-1, 0, 1],
   [-1, 1, 1], [0, 0, 0], [0, 0, 1], [0, 1, 1], [1, 1, 1]]

/-- There are ten of them, so the four-flavour assignment space has
`10⁴ = 10000` elements -- the figure the chapter quotes. -/
theorem twistMultisets_card : twistMultisets.length = 10 := by decide

/-- Multisets whose total twist is `s`. -/
def withSum (s : ℤ) : List (List ℤ) :=
  twistMultisets.filter (fun m => decide (m.sum = s))

/-- **The survivor count is pure multiset counting.**

The spectrum battery fixes `T = 3Q` per flavour, so each flavour is
filtered *independently* by one linear equation.  For
`(u, d, νₑ, e⁻)` the required totals are `3Q = (2, -1, 0, -3)`, giving
`1, 2, 2, 1` admissible multisets — and `1 · 2 · 2 · 1 = 4`, the reported
survivor count.  `10⁴` was never cut down by a joint condition. -/
theorem survivor_count_is_multiset_counting :
    (withSum 2).length = 1 ∧ (withSum (-1)).length = 2 ∧
    (withSum 0).length = 2 ∧ (withSum (-3)).length = 1 ∧
    (withSum 2).length * (withSum (-1)).length *
      (withSum 0).length * (withSum (-3)).length = 4 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;> decide

/-- The two "uniquely determined" multisets are exactly the two totals that
happen to admit a single multiset: `Σt = 2` for the `u` quark and
`Σt = -3` for the electron.  Uniqueness is a fact about representing `2`
and `-3` as a sum of three elements of `{-1,0,1}`, not about the framework. -/
theorem unique_multisets_are_u_and_electron :
    withSum 2 = [[0, 1, 1]] ∧ withSum (-3) = [[-1, -1, -1]] := by
  constructor <;> decide

/-- The `d` quark and the neutrino each admit two multisets, matching the
chapter's reported residual ambiguity. -/
theorem ambiguous_multisets_are_d_and_neutrino :
    withSum (-1) = [[-1, -1, 1], [-1, 0, 0]] ∧
    withSum 0 = [[-1, 0, 1], [0, 0, 0]] := by
  constructor <;> decide

/-- Under the additive framing split `lk = T + wr`, fixing `lk = 0` forces
`T = -wr` (reducing the spectrum equation to `-wr = threeQ`), whereas fixing
`lk = wr` forces `T = 0` (reducing the spectrum equation to `0 = threeQ`). -/
theorem framing_split_spectrum_dichotomy (lk T wr threeQ twoI₃ : ℤ)
    (hsplit : lk = T + wr) :
    (lk = 0 → (2 * T - 3 * twoI₃ = 2 * threeQ - 3 * twoI₃ ↔ -wr = threeQ)) ∧
    (lk = wr → (2 * T - 3 * twoI₃ = 2 * threeQ - 3 * twoI₃ ↔ 0 = threeQ)) := by
  rw [spectrum_iff_total_twist]
  constructor
  · intro hlk0
    have hT : T = -wr := by omega
    rw [hT]
  · intro hlkw
    have hT : T = 0 := by omega
    rw [hT]

end QOU.StandardModel.TwistBattery
