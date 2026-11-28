import Mathlib.Tactic

/-!
# Three colour strands from two conditions on the blocks

Bean `qou-h0zz` (owner pick "Why three colour strands", 2026-11-28). With `n = 5` strands
(`prop:strand-count-from-bring`), split them into a colour block of size `k` and a weak block
of size `m`, `k + m = 5`. Hypercharge is constant on each block, so its stabiliser is
`S_k × S_m` (`stabiliser_of_Y` for `k = 3`).

Inside a block of size `k`, a single strand is the fundamental state, and its conjugate is the
complement within the block, a `(k − 1)`-strand state. `selfConj_iff`: the conjugate layer is
the fundamental layer exactly when `k = 2`. This is the strand form of "the fundamental of
`SU(k)` is self-conjugate only for `k = 2`" (`Λ^{k−1} ≅ (Λ¹)^* ⊗ det`).

## The two conditions

* **(C) colour is non-abelian and complex**: `k ≥ 2` and the colour fundamental is not
  self-conjugate, i.e. quarks and antiquarks are distinct states. This is the condition that
  `OctonionColourTripletComplexType.lean` checks for the octonionic triplet.
* **(W) the weak block is non-abelian**: `m ≥ 2`, so there is a doublet.

`colour_weak_split`: (C), (W) and `k + m = 5` force `k = 3`, `m = 2`. `split_alternatives`
shows each other split fails: `4 + 1` has an abelian weak block, `2 + 3` has a self-conjugate
colour fundamental, and `1 + 4`, `5 + 0` have an abelian block.

## What is derived and what is assumed

The arithmetic and the self-conjugacy criterion are proved. Conditions (C) and (W) are
inputs. (C) is the standing requirement that colour be complex type; (W) that the weak block
carry a doublet. Neither is yet derived from the braid or Bring structure. With them the
`3 + 2` split is forced and no count is chosen to match data.

Finite combinatorics and natural-number arithmetic only. No empirical value enters.
-/

namespace QOU.StandardModel.ColourCount

/-- The fundamental layer of a block of size `k`: single strands. -/
def fund (k : ℕ) : Finset (Finset (Fin k)) := Finset.univ.powersetCard 1

/-- Its conjugate layer: complements within the block. -/
def conjLayer (k : ℕ) : Finset (Finset (Fin k)) := (fund k).image (fun S => Sᶜ)

/-- The conjugate of a single strand has `k − 1` strands (for `k ≥ 1`). -/
theorem conjLayer_eq (k : ℕ) (hk : 1 ≤ k) : conjLayer k = Finset.univ.powersetCard (k - 1) := by
  ext T
  simp only [conjLayer, fund, Finset.mem_image, Finset.mem_powersetCard, Finset.subset_univ,
    true_and]
  constructor
  · rintro ⟨S, hS, rfl⟩; rw [Finset.card_compl, hS, Fintype.card_fin]
  · intro hT
    refine ⟨Tᶜ, ?_, compl_compl T⟩
    rw [Finset.card_compl, hT, Fintype.card_fin]; omega

/-- Self-conjugate fundamental: the conjugate layer is the fundamental layer. -/
def SelfConj (k : ℕ) : Prop := conjLayer k = fund k

/-- **The fundamental is self-conjugate exactly for `k = 2`** (blocks of size `1` to `5`). -/
theorem selfConj_iff : ∀ k ∈ [1, 2, 3, 4, 5], (SelfConj k ↔ k = 2) := by
  intro k hk
  simp only [List.mem_cons, List.not_mem_nil, or_false] at hk
  rcases hk with rfl | rfl | rfl | rfl | rfl <;>
    rw [SelfConj, conjLayer_eq _ (by norm_num), fund] <;> decide

/-- Condition (C): colour block non-abelian with a non-self-conjugate fundamental. -/
def ColourOK (k : ℕ) : Prop := 2 ≤ k ∧ ¬ SelfConj k

/-- Condition (W): weak block non-abelian. -/
def WeakOK (m : ℕ) : Prop := 2 ≤ m

/-- **The `3 + 2` split is forced.** -/
theorem colour_weak_split (k m : ℕ) (hn : k + m = 5) (hC : ColourOK k) (hW : WeakOK m) :
    k = 3 ∧ m = 2 := by
  obtain ⟨hk, hsc⟩ := hC
  unfold WeakOK at hW
  have hk' : k ∈ [1, 2, 3, 4, 5] := by simp; omega
  have h2 : k ≠ 2 := fun h => hsc ((selfConj_iff k hk').mpr h)
  omega

/-- `3 + 2` satisfies both conditions, and its weak fundamental is self-conjugate. -/
theorem three_two_ok : ColourOK 3 ∧ WeakOK 2 ∧ SelfConj 2 := by
  refine ⟨⟨by norm_num, fun h => ?_⟩, by unfold WeakOK; norm_num, ?_⟩
  · exact absurd ((selfConj_iff 3 (by simp)).mp h) (by norm_num)
  · exact (selfConj_iff 2 (by simp)).mpr rfl

/-- Every other split fails one condition. -/
theorem split_alternatives :
    ¬ WeakOK 1 ∧ ¬ ColourOK 2 ∧ ¬ ColourOK 1 ∧ ¬ WeakOK 0 := by
  refine ⟨by unfold WeakOK; norm_num, fun h => h.2 ((selfConj_iff 2 (by simp)).mpr rfl),
    fun h => by have := h.1; omega, by unfold WeakOK; norm_num⟩

end QOU.StandardModel.ColourCount
