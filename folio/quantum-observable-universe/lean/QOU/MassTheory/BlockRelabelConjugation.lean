import QOU.MassTheory.TransportedPairBond

/-!
# QOU.Mass.BlockRelabelConjugation — reordering nucleons is a conjugation (permutation level)

Issue #8960. Owner, 2026-11-21: *"P-n-p-n seems chosen, not derived"*, then
*"Order is from GB reduction?"*; owner card choice "1+2 now, then 3".

## Claim being prepared

With nucleon `k` on strands `3k, 3k+1, 3k+2`, putting the nucleons in a different order
relabels the 3-strand blocks. The relabelling of two neighbouring blocks is realised by the
**cable crossing** `P_k`: block `k + 1`'s three strands pass, as a ribbon, across block `k`'s.
If `P_k` moves each nucleon rigidly to its new block, then the atom word for the swapped order
is `P_k · W · P_k⁻¹`, and since the Markov trace is a trace, `tr(P_k W P_k⁻¹) = tr(W)`. Order
would then not be an independent input; only the path the bonds take would be.

## What this file proves (permutation level)

* `swap_moves_left_block` — `P_k` carries strand `3k + a` (`a < 3`) to `3k + 3 + a`;
* `swap_moves_right_block` — and `3k + 3 + a` to `3k + a`;
* `swap_fixes_left`, `swap_fixes_right` — strands outside the two blocks stay put;
* `swap_internal_letter` — the two strands of an internal letter `σ_{3k+a}` (`a < 2`) are
  carried to the two strands of `σ_{3k+3+a}`, so at the level of permutations, `P_k` conjugates
  each internal nucleon letter of block `k` to the same letter of block `k + 1`;
* `swap_bond_letter` — the old neighbour bond `σ_{3k+2}` joins strands that `P_k` carries to
  `3k + 5` and `3k`: the last strand of the moved block `k` and the first strand of the moved
  block `k + 1`, which are no longer adjacent. The bond becomes a transported bond.

## Scope (stated, not hidden)

Pure `ℕ` arithmetic on strand positions: this is the underlying permutation, not the braid.
The braid-level fact (the cable crossing conjugates `σ_{3k+a}` to `σ_{3k+3+a}` in `B_n`, hence in
`H_n(q)`) is **not** proved here; it is checked in the Hecke algebra by
`computations/probes/he4_order_conjugation/order_conjugation_probe.py`. Nothing here says which
over/under path a transported bond should take. §7c: no ring, no archimedean construct.
-/

namespace QOU.Mass.BlockRelabelConjugation

open QOU.Mass.TransportedPairBond

/-- The cable crossing of blocks `k` and `k + 1`, as generator indices applied left to right. -/
def swapWord (k : Nat) : List Nat :=
  [3*k+2, 3*k+1, 3*k, 3*k+3, 3*k+2, 3*k+1, 3*k+4, 3*k+3, 3*k+2]

/-- The generator action commutes with a uniform shift of positions. -/
theorem step_shift (p g c : Nat) : step (p + c) (g + c) = step p g + c := by
  unfold step
  by_cases h1 : p = g
  · subst h1; simp; omega
  · by_cases h2 : p = g + 1
    · subst h2; simp; omega
    · have h1' : p + c ≠ g + c := by omega
      have h2' : p + c ≠ g + c + 1 := by omega
      simp [h1, h2, h2']

theorem carry_shift (p c : Nat) (gs : List Nat) :
    carry (p + c) (gs.map (· + c)) = carry p gs + c := by
  induction gs generalizing p with
  | nil => simp [carry]
  | cons g gs ih =>
    simp only [carry, List.map_cons, List.foldl_cons] at ih ⊢
    rw [step_shift]
    exact ih (step p g)

theorem swapWord_eq_map (k : Nat) : swapWord k = (swapWord 0).map (· + 3*k) := by
  simp [swapWord]; omega

/-- The base case `k = 0`, by computation on the six strands. -/
theorem swap0_table :
    carry 0 (swapWord 0) = 3 ∧ carry 1 (swapWord 0) = 4 ∧ carry 2 (swapWord 0) = 5 ∧
    carry 3 (swapWord 0) = 0 ∧ carry 4 (swapWord 0) = 1 ∧ carry 5 (swapWord 0) = 2 := by
  decide

theorem swap_shift (p k : Nat) : carry (p + 3*k) (swapWord k) = carry p (swapWord 0) + 3*k := by
  rw [swapWord_eq_map]; exact carry_shift p (3*k) _

/-- **`P_k` carries block `k` to block `k + 1`, strand by strand.** -/
theorem swap_moves_left_block (k a : Nat) (ha : a < 3) :
    carry (3*k + a) (swapWord k) = 3*k + 3 + a := by
  have := swap_shift a k
  rw [show 3*k + a = a + 3*k by omega, this]
  obtain ⟨h0, h1, h2, -, -, -⟩ := swap0_table
  rcases (by omega : a = 0 ∨ a = 1 ∨ a = 2) with rfl | rfl | rfl <;> omega

/-- **and block `k + 1` to block `k`.** -/
theorem swap_moves_right_block (k a : Nat) (ha : a < 3) :
    carry (3*k + 3 + a) (swapWord k) = 3*k + a := by
  have := swap_shift (a + 3) k
  rw [show 3*k + 3 + a = (a + 3) + 3*k by omega, this]
  obtain ⟨-, -, -, h3, h4, h5⟩ := swap0_table
  rcases (by omega : a = 0 ∨ a = 1 ∨ a = 2) with rfl | rfl | rfl <;>
    simp only [Nat.reduceAdd] at this ⊢ <;> omega

/-- A generator strictly to the right of `p` leaves `p` alone. -/
theorem step_left (p g : Nat) (h : p < g) : step p g = p := by
  unfold step
  have h1 : p ≠ g := by omega
  have h2 : p ≠ g + 1 := by omega
  simp [h1, h2]

theorem carry_left (p : Nat) (gs : List Nat) (h : ∀ g ∈ gs, p < g) : carry p gs = p := by
  induction gs with
  | nil => simp [carry]
  | cons g gs ih =>
    simp only [carry, List.foldl_cons]
    rw [step_left p g (h g (by simp))]
    exact ih (fun x hx => h x (by simp [hx]))

/-- Strands left of block `k` are fixed. -/
theorem swap_fixes_left (k p : Nat) (hp : p < 3*k) : carry p (swapWord k) = p := by
  apply carry_left; intro g hg; simp [swapWord] at hg; omega

/-- Strands right of block `k + 1` are fixed. -/
theorem swap_fixes_right (k p : Nat) (hp : 3*k + 6 ≤ p) : carry p (swapWord k) = p := by
  apply carry_fixed; intro g hg; simp [swapWord] at hg; omega

/-- **Internal letters move with their block.** The strands `3k+a, 3k+a+1` of an internal letter
of block `k` (`a < 2`) are carried to `3k+3+a, 3k+3+a+1`, the strands of the same letter of
block `k + 1`. -/
theorem swap_internal_letter (k a : Nat) (ha : a < 2) :
    carry (3*k + a) (swapWord k) = 3*k + 3 + a ∧
      carry (3*k + a + 1) (swapWord k) = 3*k + 3 + a + 1 := by
  refine ⟨swap_moves_left_block k a (by omega), ?_⟩
  have := swap_moves_left_block k (a + 1) (by omega)
  simpa [Nat.add_assoc] using this

/-- **The neighbour bond becomes a transported bond.** `σ_{3k+2}` joins strands `3k+2` and
`3k+3`; after `P_k` they sit at `3k+5` (last strand of the moved block `k`) and `3k` (first strand
of the moved block `k + 1`), which are not adjacent. -/
theorem swap_bond_letter (k : Nat) :
    carry (3*k + 2) (swapWord k) = 3*k + 5 ∧ carry (3*k + 3) (swapWord k) = 3*k ∧
      3*k + 1 < 3*k + 5 := by
  refine ⟨?_, ?_, by omega⟩
  · simpa using swap_moves_left_block k 2 (by omega)
  · simpa using swap_moves_right_block k 0 (by omega)

end QOU.Mass.BlockRelabelConjugation
