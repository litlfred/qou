/-!
# QOU.Mass.TransportedPairBond — a bond between non-neighbouring nucleons

Issue #8960, owner ask 2026-11-21: *"Not all γγ production should be on same strands.
Look at how He formed."* Companion to `QOU.Mass.StrandLayoutForcesChain`.

## What this settles

`StrandLayoutForcesChain.no_single_generator_joins_nonadjacent` proves that, with nucleon `k`
on strands `3k, 3k+1, 3k+2`, a single generator joins two nucleons only when they are
neighbours. So a word of single inter-nucleon letters writes the chain (`A − 1` bonds) and
never the complete graph (`A(A−1)/2` pairs).

This file gives the word that reaches a non-neighbour and proves that it does. For nucleons
`i < j`, the **transport** `T_ij = σ_{3i+2} σ_{3i+3} ⋯ σ_{3j−2}` carries nucleon `i`'s last
strand from position `3i+2` to position `3j−1`. It leaves nucleon `j`'s first strand at `3j`.
A bond letter on generator `3j−1` therefore crosses a strand of nucleon `i` with a strand of
nucleon `j`, and `T_ij · b · T_ij⁻¹` is a bond between them.

* `carry_transport` — `T_ij` takes position `3i+2` to `3j−1`;
* `carry_partner_fixed` — and fixes position `3j`;
* `transported_bond_joins` — so the letter on `3j−1` joins block `i` to block `j`;
* `transport_length` — `T_ij` has `3(j−i) − 3` letters (empty for neighbours: the production
  chain letter is the case `j = i + 1`).

## Scope

Pure `ℕ` arithmetic on strand positions: `step g` is the permutation action of the generator
`σ_g` on positions, so this is the underlying permutation of the braid word, not the braid
itself. It does **not** say which bond set, which over/under transport, or which formation
order the physics wants. Those are modelling choices, recorded in
`computations/probes/he4_all_pairs_formation/preregistration.md` and measured there with
every option reported. §7c does not apply (no ring, no archimedean construct).
-/

namespace QOU.Mass.TransportedPairBond

/-- The nucleon owning strand position `m` (nucleon `k` occupies `3k, 3k+1, 3k+2`). -/
def block (m : Nat) : Nat := m / 3

/-- Action of the generator `σ_g` on a strand position: it swaps positions `g` and `g+1`. -/
def step (p g : Nat) : Nat :=
  if p = g then g + 1 else if p = g + 1 then g else p

/-- Position reached by the strand at `p` after the generators `gs`, applied left to right. -/
def carry (p : Nat) (gs : List Nat) : Nat := gs.foldl step p

/-- The transport `T_ij = σ_{3i+2} ⋯ σ_{3j−2}`, as its list of generator indices. -/
def transport (i j : Nat) : List Nat := List.range' (3 * i + 2) (3 * (j - i) - 3)

/-- Consecutive generators starting at the strand's own position walk it `k` places right. -/
theorem carry_range' (a k : Nat) : carry a (List.range' a k) = a + k := by
  induction k generalizing a with
  | zero => simp [carry]
  | succ k ih =>
    have h := ih (a + 1)
    simp only [carry, List.range'_succ, List.foldl_cons] at h ⊢
    rw [show step a a = a + 1 by simp [step]]
    omega

/-- A strand strictly to the right of every generator's pair `{g, g+1}` does not move. -/
theorem carry_fixed (p : Nat) (gs : List Nat) (h : ∀ g ∈ gs, g + 1 < p) :
    carry p gs = p := by
  induction gs with
  | nil => simp [carry]
  | cons g gs ih =>
    have hg : g + 1 < p := h g (by simp)
    have hrest : ∀ x ∈ gs, x + 1 < p := fun x hx => h x (by simp [hx])
    have hs : step p g = p := by
      unfold step
      split
      · omega
      · split
        · omega
        · rfl
    simp only [carry, List.foldl_cons, hs]
    exact ih hrest

/-- `T_ij` has `3(j−i) − 3` letters. For neighbours (`j = i + 1`) it is empty, and the bond
letter sits on `3j − 1 = 3i + 2`: exactly the production chain letter. -/
theorem transport_length (i j : Nat) : (transport i j).length = 3 * (j - i) - 3 := by
  simp [transport]

/-- **The transport carries nucleon `i`'s last strand to position `3j − 1`.** -/
theorem carry_transport (i j : Nat) (h : i < j) :
    carry (3 * i + 2) (transport i j) = 3 * j - 1 := by
  unfold transport
  rw [carry_range']
  omega

/-- **And it leaves nucleon `j`'s first strand where it was.** -/
theorem carry_partner_fixed (i j : Nat) (h : i < j) :
    carry (3 * j) (transport i j) = 3 * j := by
  apply carry_fixed
  intro g hg
  simp [transport, List.mem_range'] at hg
  omega

/-- **The transported bond joins block `i` to block `j`.** After `T_ij`, the letter on
generator `3j − 1` swaps positions `3j − 1` and `3j`; the first holds nucleon `i`'s strand
and the second nucleon `j`'s. -/
theorem transported_bond_joins (i j : Nat) (h : i < j) :
    block (3 * i + 2) = i ∧ block (3 * j) = j ∧
      carry (3 * i + 2) (transport i j) = 3 * j - 1 ∧
      carry (3 * j) (transport i j) = 3 * j := by
  refine ⟨by simp [block]; omega, by simp [block], carry_transport i j h,
    carry_partner_fixed i j h⟩

/-- Pair counts: the chain has `A − 1` bonds, the complete graph `A(A−1)/2`. At `A = 4`
these are 3 and 6, which is the bond-count half of the ⁴He gap discussed in
`docs/audits/2026-11-21-he4-binding-breakdown.md`. -/
theorem he4_pair_counts : (4 - 1 = 3) ∧ (4 * (4 - 1) / 2 = 6) := by decide

end QOU.Mass.TransportedPairBond
