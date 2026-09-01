import Mathlib.Tactic

/-!
# QOU.Mass.StrandLayoutForcesChain — the chain bond set is forced by the strand layout

Arc `bk-crossing-mass-binding`, bean `qou-brng`; companion to
`QOU.Mass.CoordinationSaturation` and `QOU.MassTheory.ChainBondOrderDependence`.

## What this settles

The corpus carries two inter-nucleon bond sets and they have been compared as though
they were two *choices* of the same kind of object:

* `mass_at_3A_proper.atom_braid_word_3A` wires `A − 1` bonds (the chain);
* `hecke_core_symbolic.build_atom_nf_sym` wires `C(A,2)` (the complete graph).

They are not two choices. Measured on the live producer, `atom_braid_word_3A` places
its pp/nn/pn bridge at generator `3k+2` for `k = 0 … A−2` — verified directly by
diffing the `include_inter=False` and `include_inter=True` words at `A = 4, 5, 6`,
which added generators `{2, 5, 8}`, `{2, 5, 8, 11}` and `{2, 5, 8, 11, 14}`.

This file proves *why* those are the only ones available. Nucleon `k` occupies
strands `3k, 3k+1, 3k+2` of a `3A`-strand braid, and the generator `σ_m` swaps
strands `m` and `m+1`. So:

* `crossesBlocks_iff` — `σ_m` joins two different nucleons **iff** `m % 3 = 2`;
* `adjacent_of_crosses` — and when it does, the two nucleons are **consecutive**;
* `no_single_generator_joins_nonadjacent` — hence no single generator joins
  non-adjacent nucleons, at any `A`.

**The chain is therefore forced by the layout, not selected among bond sets.** A
non-adjacent bond is not a different edge set one could equally have written; it is
not a single crossing at all, and would need a word transporting strands past each
other — which `atom_braid_word_3A` does not write and which would not sit at a
Markov-removable position in the same way.

## The consequence worth carrying

The layout is a *linear order on nucleons*. So the chain bond set and the nucleon
ordering convention are **the same unlicensed choice**, not two independent ones —
which merges this arc's bond-set question into the ordering gap already tracked as
`qou-48is` (there the ordering moves `tr_M` by O(10 %) at `A ≥ 3`).

## Scope

Pure `ℕ` arithmetic about the block map `m ↦ m / 3`; §7c does not apply (no ring, no
archimedean construct). It says nothing about which bond set the *physics* wants, and
nothing about `build_atom_nf_sym`, whose inter-nucleon factors are all at generator 0
and therefore carry no strand assignment at all (measured separately: that product is
invariant under every permutation of its bond multiset, so it encodes a bond *count*
rather than a graph).
-/

namespace QOU.Mass.StrandLayoutForcesChain

/-- The nucleon index owning strand `m`, under the framework's layout in which
nucleon `k` occupies strands `3k`, `3k+1`, `3k+2` of a `3A`-strand braid. -/
def block (m : ℕ) : ℕ := m / 3

/-- **A generator crosses a nucleon boundary exactly at `m ≡ 2 (mod 3)`.**
`σ_m` swaps strands `m` and `m+1`; those lie in different nucleons iff `m % 3 = 2`. -/
theorem crossesBlocks_iff (m : ℕ) : block m ≠ block (m + 1) ↔ m % 3 = 2 := by
  unfold block
  omega

/-- **And the two nucleons it joins are consecutive.** This is the half that forces
the chain: a boundary-crossing generator never reaches past its neighbour. -/
theorem adjacent_of_crosses (m : ℕ) (h : m % 3 = 2) :
    block (m + 1) = block m + 1 := by
  unfold block
  omega

/-- **No single generator joins non-adjacent nucleons**, at any `A`. So the edges
expressible as one crossing are exactly the `A − 1` consecutive pairs, and the
complete graph is not among the bond sets this layout can write. -/
theorem no_single_generator_joins_nonadjacent (m i j : ℕ)
    (hi : block m = i) (hj : block (m + 1) = j) (hne : i ≠ j) : j = i + 1 := by
  subst hi; subst hj
  have h : m % 3 = 2 := (crossesBlocks_iff m).mp (fun hEq => hne hEq)
  exact adjacent_of_crosses m h

/-- The bridge generator the producer actually uses for the `k`-th bond, `3k+2`,
does cross a boundary — the positive direction of `crossesBlocks_iff`, instantiated
at the measured value. -/
theorem bridge_crosses (k : ℕ) : block (3 * k + 2) ≠ block (3 * k + 3) := by
  have : (3 * k + 2) % 3 = 2 := by omega
  simpa using (crossesBlocks_iff (3 * k + 2)).mpr this

/-- And it joins nucleon `k` to nucleon `k+1`, which is what makes the wired bond set
the chain. -/
theorem bridge_joins_consecutive (k : ℕ) :
    block (3 * k) = k ∧ block (3 * k + 3) = k + 1 := by
  constructor <;> · unfold block; omega

end QOU.Mass.StrandLayoutForcesChain
