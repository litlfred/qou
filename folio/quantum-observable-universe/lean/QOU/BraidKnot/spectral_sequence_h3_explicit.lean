import Mathlib.GroupTheory.Perm.Fin
import Mathlib.Data.Fintype.Perm

/-!
# QOU.BraidKnot.spectral_sequence_h3_explicit — conjecture carrier

Content block
[`conj:spectral-sequence-h3-explicit`](../../../quantum-observable-universe/mass-theory/spectral-sequence-h3-explicit.md).

**Conjecture, not a proposition (owner, 2026-11-20, bean `qou-6qbv`).** The
block claims explicit formulas for the differentials `d₁`, `d₂` of the
GB-filtered Hochschild spectral sequence on `H₃(R, q)` and the resulting
`E_∞` page identifications.

## What changed

Until 2026-11-20 a `def` projected the three claims out of a context class that
also carried free fields `Z`, `N`, `n_strands` and the bare equation
`n_strands = 3`. The projection is gone. The three claims stay as `Prop`
parameters of the carrier `SpectralSequenceH3Explicit`, because their encoding
is an author decision this file deliberately does not make (a `d₁ ∘ d₁ = 0`
encoding is true of every differential and is not the claim). No instance is
supplied: that is the open state.

## What is proved

`e1_ranks_h3`: the `E₁` page the block describes has ranks `1, 2, 2, 1`. The
filtration is by Coxeter length on the standard basis `{T_w : w ∈ S₃}` of
`H₃(q)`, and `ℓ(w)` is the inversion count of `w`; the ranks are the numbers
of permutations of three letters with `0, 1, 2, 3` inversions. This is the one
numerical claim in the block that does not depend on the open differentials.

**Caveat (2026-11-20, bean `qou-6qbv`).** These are the ranks of `gr H₃(q)` under the
length filtration, which is what the block describes. They are **not** the `E₁` page of
the Hochschild spectral sequence that `prop:gb-spectral-sequence`'s proof actually
builds: that sequence lives on `Hom(H₃^{⊗k}, H₃)` and abuts to `HH*(H₃)`, which at
generic `q` is the centre `Z(H₃)`, of dimension 3 (one per partition of 3), not 6.
The block's statement (`E_∞ ⇒ gr H_n`) and its proof (`E_∞ ≅ gr HH*`) name different
abutments, and the confinement filtration `J^•` is defined as increasing while the
proof uses it as decreasing. See `QOU.BraidKnot.GBRewriteDifferential`.
-/

namespace QOU.BraidKnot

open Equiv

/-- **Conjecture (explicit spectral sequence on `H₃`).** `d1Explicit`,
`d2Explicit`, `pagesConcretised` are the block's three sub-claims; the carrier
holds exactly when all three do. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/spectral-sequence-h3-explicit
class SpectralSequenceH3Explicit
    (d1Explicit d2Explicit pagesConcretised : Prop) : Prop where
  /-- (i) the explicit `d₁`-differential. -/
  d1 : d1Explicit
  /-- (ii) the explicit `d₂`-differential. -/
  d2 : d2Explicit
  /-- (iii) the `E_∞` page identifications on `H₃(R, q)`. -/
  pages : pagesConcretised

/-- Inversion count of a permutation, which is its Coxeter length in `Sₙ`. -/
def inversionCount {n : ℕ} (σ : Perm (Fin n)) : ℕ :=
  (Finset.univ.filter fun p : Fin n × Fin n => p.1 < p.2 ∧ σ p.2 < σ p.1).card

/-- **The `E₁` ranks.** The standard basis of `H₃(q)` graded by Coxeter length
has ranks `1, 2, 2, 1` in lengths `0, 1, 2, 3`. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/spectral-sequence-h3-explicit
theorem e1_ranks_h3 :
    (List.range 4).map (fun k =>
      (Finset.univ.filter fun σ : Perm (Fin 3) => inversionCount σ = k).card)
      = [1, 2, 2, 1] := by
  decide

end QOU.BraidKnot
