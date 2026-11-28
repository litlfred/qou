import Mathlib.GroupTheory.Perm.Fin
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Tactic
import QOU.BringsSurface.BringMapChain

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
* `bring_genus_eq_four` — the genus read off Bring's map (`bring_chi`, `χ = -6`) is `4`.
* `strandCount_of_genus` — **if** the traceless charge directions are Bring's holomorphic
  differentials, so that `n - 1 = g`, then `n = 5`. This is a second, independent route to
  the same count: the first uses the order of `S₅`, this one uses `χ = -6`.

## Input

That the strand relabellings are Bring's symmetries is a hypothesis, not proved; so is
`n - 1 = g` in the genus route. The two hypotheses are compatible: the holomorphic
differentials of Bring carry `std ⊗ sgn` of `S₅` (bean `qou-efxy`, not formalised), the
four-dimensional traceless part of the permutation representation twisted by the sign. The
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

open QOU.BringsSurface.BringMapChain QOU.RiemannSurface.CombinatorialMapEuler in
/-- Bring's genus, read off its combinatorial map, is `4`. -/
theorem bring_genus_eq_four (g : ℕ)
    (hg : (numCycles σ : ℤ) - numCycles α + numCycles (σ * α) = 2 - 2 * g) : g = 4 := by
  have h := hg.symm.trans bring_chi
  omega

open QOU.BringsSurface.BringMapChain QOU.RiemannSurface.CombinatorialMapEuler in
/-- **Five strands from `χ = -6`.** If the `n - 1` traceless charge directions are Bring's
`g` holomorphic differentials, then `n = 5`. -/
theorem strandCount_of_genus (n g : ℕ)
    (hg : (numCycles σ : ℤ) - numCycles α + numCycles (σ * α) = 2 - 2 * g)
    (hn : n = g + 1) : n = 5 := by
  rw [hn, bring_genus_eq_four g hg]

end QOU.StandardModel.StrandCount
