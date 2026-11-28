import Mathlib.GroupTheory.Perm.Fin
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Tactic

/-!
# QOU.StandardModel.StrandCountFromBring — five strands if strand relabellings are Bring's symmetries

`prop:odd-strands-force-chirality` shows the strand count `n` must be odd. This module
records what fixes `n = 5`, conditionally.

Bring's surface has automorphism group `S₅` (`BringMapChain.lean`: darts are
`Perm (Fin 5)`), acting on the five homogeneous coordinates of its model
`p₁ = p₂ = p₃ = 0` in `ℙ⁴`. The traceless condition on strand charges is the
hyperplane `p₁ = 0`.

* `strandCount_eq_five` — **if** the relabellings of the `n` strands are in bijection
  with Bring's symmetries, then `n = 5`. Only the order `120 = 5!` is used.
* `isospin_count` — a split `5 = colour + isospin` with three colour strands has
  two isospin strands.
* `five_odd` — `5` is odd, as chirality requires; the two constraints agree.

## Input

That the strand relabellings are Bring's symmetries is a hypothesis, not proved. The
three colour strands are the colour tube coordinates (`def:color-tube-coordinates`),
also not derived here. Base ring: none (counting only).
-/

namespace QOU.StandardModel.StrandCount

/-- **Five strands.** If the relabellings of `n` strands are in bijection with Bring's
symmetry group `S₅`, then `n = 5`. -/
theorem strandCount_eq_five {n : ℕ} (e : Equiv.Perm (Fin n) ≃ Equiv.Perm (Fin 5)) :
    n = 5 := by
  have h := Fintype.card_congr e
  simp only [Fintype.card_perm, Fintype.card_fin] at h
  rcases Nat.lt_or_ge 1 n with hn | hn
  · exact (Nat.factorial_inj hn).1 h
  · interval_cases n <;> simp [Nat.factorial] at h

/-- With three colour strands, the remaining isospin strands number two. -/
theorem isospin_count (colour isospin : ℕ) (h : colour + isospin = 5) (hc : colour = 3) :
    isospin = 2 := by omega

theorem five_odd : Odd 5 := ⟨2, rfl⟩

end QOU.StandardModel.StrandCount
