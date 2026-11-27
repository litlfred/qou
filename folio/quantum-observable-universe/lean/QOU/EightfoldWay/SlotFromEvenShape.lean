import QOU.EightfoldWay.StrandSlotSeparatesGen1
import QOU.StandardModel.OddExteriorAnomalyFreedom

/-!
# QOU.EightfoldWay.SlotFromEvenShape — the Georgi–Glashow slot is the shape of an even subset

`StrandSlotSeparatesGen1.lean` takes the slot of each first-generation quark state
(`slot`) as an input, the Georgi–Glashow embedding. This module shows that the slot
is not extra data once matter is the even part `Λ⁰ ⊕ Λ² ⊕ Λ⁴` of five strands
(`prop:even-strand-generation`, `OddExteriorAnomalyFreedom.lean`).

Split the five strands into colour `{0,1,2}` and isospin `{3,4}`. An even subset
`S` is a quark state exactly when it meets the colour strands in one or two
places. Its **shape** is then one of four kinds, and these are the four slots:

| slot      | even subset            | degree | charge at `α = 1/6` |
|-----------|------------------------|--------|---------------------|
| `colIso3` | `{c, 3}`               | 2      | `+2/3`              |
| `colIso4` | `{c, 4}`               | 2      | `-1/3`              |
| `colCol`  | `{c, c+1}`             | 2      | `-2/3`              |
| `colour`  | `{c}ᶜ`                 | 4      | `+1/3`              |

* `slotSubset_mem_even` — every slot shape is an even subset.
* `slotSubset_injective` — the twelve (slot, colour) pairs give twelve different subsets.
* `quark_iff_slotSubset` — the even subsets meeting colour once or twice are exactly
  these twelve; `card_quarkEven` counts them, `card_leptonEven` counts the other four.
* `stateCharge_slotSubset` — the strand charge of each shape at `α = 1/6` is
  `slotCharge` of its slot. The degree-4 shape gets the `5̄` charge from
  complementation (`stateCharge_compl_singleton`), with no separate `5̄` input.
* `slotCharge_injective` — the four slot charges are distinct.
* `slot_forced` — **any** slot assignment that reproduces the Standard Model charges
  (with the dual flag as sign) is `slot`. So `slot` is forced by the charges.

## What is still an input

The dual flag `dual`, i.e. which states sit in the even part and which in its
conjugate. `dual_eq_helicity` identifies it with helicity, so it carries the open
chirality sign (bean `qou-h0zz`). The SM labels enter only as the names of
`Gen1Quark`; their charges are the labels being matched.

Base ring `ℚ`; no empirical input.
-/

namespace QOU.EightfoldWay.SlotFromEvenShape

open Finset
open QOU.StandardModel.Chirality QOU.StandardModel.Chirality.Gen1Quark
open QOU.EightfoldWay.NeutralLeptonFixesCharges
open QOU.StandardModel.Su3Su2U1Z6GroupAndCommutant
open QOU.EightfoldWay.StrandSlotSeparatesGen1
open QOU.StandardModel.OddExterior
open Slot

instance : Fintype Slot :=
  ⟨{colour, colIso3, colIso4, colCol}, by intro x; cases x <;> decide⟩

/-- The colour strands `{0,1,2}`. -/
def colourStrands : Finset (Fin 5) := {0, 1, 2}

/-- Colour strand `c` as a strand of `Fin 5`. -/
def col : Fin 3 → Fin 5
  | 0 => 0
  | 1 => 1
  | 2 => 2

/-- The next colour strand after `c` (cyclically). -/
def nxt : Fin 3 → Fin 5
  | 0 => 1
  | 1 => 2
  | 2 => 0

/-- The even subset of each (slot, colour) pair. -/
def slotSubset : Slot → Fin 3 → Finset (Fin 5)
  | colour, c => ({col c} : Finset (Fin 5))ᶜ
  | colIso3, c => {col c, 3}
  | colIso4, c => {col c, 4}
  | colCol, c => {col c, nxt c}

theorem slotSubset_mem_even (s : Slot) (c : Fin 3) : slotSubset s c ∈ evenSubsets := by
  cases s <;> fin_cases c <;> decide

theorem slotSubset_injective :
    Function.Injective (fun p : Slot × Fin 3 => slotSubset p.1 p.2) := by
  rintro ⟨s, c⟩ ⟨t, d⟩ h
  cases s <;> cases t <;> fin_cases c <;> fin_cases d <;> revert h <;> decide

/-- An even subset is a quark state when it meets colour once or twice. -/
def IsQuark (S : Finset (Fin 5)) : Prop :=
  1 ≤ (S ∩ colourStrands).card ∧ (S ∩ colourStrands).card ≤ 2

instance (S : Finset (Fin 5)) : Decidable (IsQuark S) := by
  unfold IsQuark; infer_instance

/-- **The quark part of the even part is exactly the twelve slot shapes.** -/
theorem quark_iff_slotSubset :
    ∀ S ∈ evenSubsets, IsQuark S ↔ ∃ s : Slot, ∃ c : Fin 3, slotSubset s c = S := by
  decide +kernel

theorem card_quarkEven : (evenSubsets.filter IsQuark).card = 12 := by
  decide +kernel

theorem card_leptonEven : (evenSubsets.filter (fun S => ¬ IsQuark S)).card = 4 := by
  decide +kernel

/-- The five strand charges at `α = 1/6`. -/
theorem qWeight5_sixth (i : Fin 5) :
    qWeight5 (1 / 6 : ℚ) i = ![-(1 / 3), -(1 / 3), -(1 / 3), 1, 0] i := by
  obtain ⟨q0, q1, q2, q3, q4⟩ := qWeight5_apply (1 / 6 : ℚ)
  fin_cases i
  · exact q0.trans (by norm_num)
  · exact q1.trans (by norm_num)
  · exact q2.trans (by norm_num)
  · exact q3.trans (by norm_num)
  · exact q4.trans (by norm_num)

/-- **The strand charge of each shape is the slot charge.** -/
theorem stateCharge_slotSubset (s : Slot) (c : Fin 3) :
    stateCharge (qWeight5 (1 / 6 : ℚ)) (slotSubset s c) = slotCharge s := by
  obtain ⟨h1, h2, h3, h4⟩ := slotCharge_values
  cases s
  · rw [h1, slotSubset, stateCharge_compl_singleton _ (sum_qWeight5 _), qWeight5_sixth]
    fin_cases c <;> simp [col]
  all_goals
    simp only [h2, h3, h4, slotSubset, stateCharge]
    fin_cases c <;> simp only [col, nxt] <;> rw [Finset.sum_pair (by decide)] <;>
      rw [qWeight5_sixth, qWeight5_sixth] <;> simp <;> norm_num

theorem slotCharge_injective : Function.Injective slotCharge := by
  obtain ⟨h1, h2, h3, h4⟩ := slotCharge_values
  intro s t h
  cases s <;> cases t <;> simp only [h1, h2, h3, h4] at h <;> first | rfl | norm_num at h

/-- **The slot is forced by the charges.** Any assignment of slots that reproduces the
Standard Model charge of each state, with the dual flag as sign, is `slot`. -/
theorem slot_forced (σ : Gen1Quark → Slot)
    (hσ : ∀ x, (if dual x then -1 else 1) * slotCharge (σ x) = smCharge x) : σ = slot := by
  funext x
  apply slotCharge_injective
  have h := (hσ x).trans (charge_from_slot x).symm
  split_ifs at h <;> linarith

end QOU.EightfoldWay.SlotFromEvenShape
