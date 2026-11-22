/-
  Width of a parallel layer of braid generators.

  In `B_{m+1}` the generators `σ_i` and `σ_j` commute when `|i − j| ≥ 2`.
  Read computational time as the number of Cartier–Foata layers of a braid
  word, and the letters inside one layer as simultaneous ("spacelike")
  operations.  Then a layer is a set of generator indices in `{0, …, m−1}`
  that are pairwise at distance `≥ 2`.

  `card_le_of_far` : such a set has at most `⌈m/2⌉ = (m+1)/2` elements.
  `exists_far_card`: the bound is attained (the even indices).

  So the spatial extent of one time step grows linearly in the number of
  strands, and the far-commutation graph is a path: braid words carry a
  1+1-dimensional causal structure.  A higher-dimensional space would need a
  commutation graph that is a higher-dimensional lattice.

  Pure combinatorics over `ℕ`.
-/
import Mathlib.Data.Finset.Card
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Tactic.Linarith

namespace QOU.BraidsAndKnots.CommutingGeneratorWidth

/-- Indices pairwise at distance at least two: the generators commute. -/
def Far (S : Finset ℕ) : Prop :=
  ∀ i ∈ S, ∀ j ∈ S, i ≠ j → i + 2 ≤ j ∨ j + 2 ≤ i

/-- **A layer of commuting generators among `σ_0, …, σ_{m−1}` has at most
`(m+1)/2` letters.**  Halving is injective on a far set. -/
theorem card_le_of_far {m : ℕ} {S : Finset ℕ} (hS : ∀ i ∈ S, i < m) (hfar : Far S) :
    S.card ≤ (m + 1) / 2 := by
  have hinj : Set.InjOn (fun i => i / 2) S := by
    intro i hi j hj hij
    by_contra hne
    have := hfar i hi j hj hne
    simp only at hij
    omega
  have himg : S.image (fun i => i / 2) ⊆ Finset.range ((m + 1) / 2) := by
    intro k hk
    simp only [Finset.mem_image] at hk
    obtain ⟨i, hi, rfl⟩ := hk
    have := hS i hi
    simp only [Finset.mem_range]
    omega
  calc S.card = (S.image (fun i => i / 2)).card := (Finset.card_image_of_injOn hinj).symm
    _ ≤ (Finset.range ((m + 1) / 2)).card := Finset.card_le_card himg
    _ = (m + 1) / 2 := Finset.card_range _

/-- **The bound is attained** by the even indices `0, 2, 4, …`. -/
theorem exists_far_card (m : ℕ) :
    ∃ S : Finset ℕ, (∀ i ∈ S, i < m) ∧ Far S ∧ S.card = (m + 1) / 2 := by
  refine ⟨(Finset.range ((m + 1) / 2)).image (fun k => 2 * k), ?_, ?_, ?_⟩
  · intro i hi
    simp only [Finset.mem_image, Finset.mem_range] at hi
    obtain ⟨k, hk, rfl⟩ := hi
    omega
  · intro i hi j hj hne
    simp only [Finset.mem_image, Finset.mem_range] at hi hj
    obtain ⟨k, -, rfl⟩ := hi
    obtain ⟨l, -, rfl⟩ := hj
    omega
  · rw [Finset.card_image_of_injective _ (fun a b h => by simpa using h), Finset.card_range]

end QOU.BraidsAndKnots.CommutingGeneratorWidth
