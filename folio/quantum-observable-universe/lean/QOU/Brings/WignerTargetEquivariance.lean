import QOU.Brings.S5CharactersOnBringDeformations
import Mathlib.Algebra.Module.Basic

/-!
# Equivariance forces the Wigner target out of `HH²` of the base

The Wigner axiom (`conj:wigner-axiom`, clause W2) realises the generator of the
observable line by a class whose archimedean image is the Euler class
`e(TM₀) ∈ H²(M₀; k)`. The question this file settles is *why the target is the
degree-two cohomology of the base and not the degree-two Hochschild cohomology*
`HH²(M₀) = H¹(M₀, T_{M₀})`, the space the corpus's older `χ`-chain used.

The argument is equivariance. The substrate carries the `S₅`-symmetry of Bring's
curve; the observable line is `S₅`-trivial (a scalar); an equivariant map out of a
trivial module lands in the invariants of its target. The character ledger
`QOU.Brings.S5Char.hochschild_invariants_of_base` computes, exactly, that the
`S₅`-invariant part of the base's Hochschild theory is

    HH⁰ : k,   HH¹ : 0,   HH² = H¹(T) : 0,   HH₀ : k²,   HH₁ = HH₋₁ : 0,

so a non-zero equivariant realisation into `HH²` does not exist, while `HH₀` has a
two-dimensional invariant part — the rank and the point class — and it is the point
class whose Poincaré dual is `H²(M₀; k)`.

Two layers, kept apart:

* `equivariant_image_invariant` / `equivariant_map_vanishes_of_no_invariants`
  are the abstract statements, proved for any group acting additively.
* `no_invariant_in_hh2_of_base` is the ledger entry: the inner product of the
  character of `H¹(T_{Σ₄})` (scaled by 6, as in the source file) with the trivial
  character is `0`. That `⟨χ_N, 1⟩ = dim N^G` is character theory
  (Fulton–Harris 2.11) and is the one cited input between the two layers.

No `sorry`; the ledger theorem is decided by `decide` upstream.

-- Ref: [fulton-harris1991] https://doi.org/10.1007/978-1-4612-0979-9
-- Ref: [wigner1960] https://doi.org/10.1002/cpa.3160130102
-/

namespace QOU.Brings

/-- An additive `G`-equivariant map sends invariant vectors to invariant vectors. -/
theorem equivariant_image_invariant {G M N : Type*} [Group G] [AddCommGroup M]
    [AddCommGroup N] (ρM : G → M →+ M) (ρN : G → N →+ N) (f : M →+ N)
    (hf : ∀ g m, f (ρM g m) = ρN g (f m)) (m : M) (hm : ∀ g, ρM g m = m) :
    ∀ g, ρN g (f m) = f m := by
  intro g
  rw [← hf, hm]

/-- **No invariants in the target ⇒ every equivariant map from an invariant vector is
zero.** The observable line is spanned by an invariant vector; if the target has no
non-zero invariants, its realisation there vanishes. -/
theorem equivariant_map_vanishes_of_no_invariants {G M N : Type*} [Group G]
    [AddCommGroup M] [AddCommGroup N] (ρM : G → M →+ M) (ρN : G → N →+ N)
    (f : M →+ N) (hf : ∀ g m, f (ρM g m) = ρN g (f m)) (m : M) (hm : ∀ g, ρM g m = m)
    (hN : ∀ n : N, (∀ g, ρN g n = n) → n = 0) : f m = 0 :=
  hN _ (equivariant_image_invariant ρM ρN f hf m hm)

/-- **The ledger entry:** `H¹(T_{Σ₄}) = [4,1] ⊕ [3,2]` has no `S₅`-invariant, so
`HH²` of the base cannot receive the observable line equivariantly. Read off the
character table (`S5Char.hochschild_invariants_of_base`, fourth conjunct). -/
theorem no_invariant_in_hh2_of_base :
    S5Char.inner S5Char.h1TangentSix S5Char.chiTriv = 0 :=
  S5Char.hochschild_invariants_of_base.2.2.2

/-- The invariant part that does exist: `HH₀` of the base carries two invariants
(`⟨χ_{HH₀}, 1⟩ = 240/120 = 2`), the rank and the point class. -/
theorem two_invariants_in_hh0_of_base :
    S5Char.inner (fun i => S5Char.chiTriv i + S5Char.chiTriv i) S5Char.chiTriv = 240 :=
  S5Char.hochschild_invariants_of_base.2.1

end QOU.Brings
