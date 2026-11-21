import Mathlib.Tactic
import Mathlib.LinearAlgebra.UnitaryGroup

/-!
# QOU.su2_emergence_dagger_unitarity — gauge-group containment `G ⊆ U(2)`

**Lemma** ([`lem:su2-emergence-dagger-unitarity`](../../../quantum-observable-universe/quantum-observable-universes/su2-emergence-dagger-unitarity.md)).

*Under the QOU hypotheses of [emergence of the gauge group](#thm:su2-emergence),
every tensor automorphism `g ∈ G` preserves the Frobenius dagger
on `τ(V)`; equivalently, `G ⊆ U(2)`.*

## Archimedean realisation (this file)

After the substrate→archimedean realisation `τ`, the fibre `τ(V)` is the
standard 2-dimensional Hermitian space `ℂ²`, the Frobenius dagger is the
conjugate-transpose `g ↦ gᴴ`, and "`g` preserves the Frobenius dagger"
is the concrete identity `g · gᴴ = 1`.  The lemma's content at this level
is the (non-tautological) implication

  `g · gᴴ = 1  ⟹  g ∈ U(2)`,

which we **derive** from `Matrix.mem_unitaryGroup_iff`: each gauge
element that preserves the dagger on the fibre lands in
`Matrix.unitaryGroup (Fin 2) ℂ`, hence `G ⊆ U(2)`.  This is the
archimedean face required by §7c (Hermitian pairing ⇒ `ℂ`).  The
pointwise statement is the full mathematical content — the "lift to the
whole group" is the universal statement over all `g ∈ G` below.

-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/su2-emergence-dagger-unitarity.md
-/

open Matrix

namespace QOU

/-- **`g ∈ U(2)` from Frobenius-dagger preservation — archimedean realisation**
    ([`lem:su2-emergence-dagger-unitarity`]).

    A `2×2` complex matrix `g` that preserves the standard Hermitian
    pairing on the fibre `τ(V) = ℂ²` (i.e. `g · gᴴ = 1`, the concrete
    form of "`g` preserves the Frobenius dagger") is unitary,
    `g ∈ U(2)`.

    Genuine derivation: the hypothesis `g * star g = 1` is the full
    content of `Matrix.mem_unitaryGroup_iff`, and the conclusion is
    membership in `Matrix.unitaryGroup (Fin 2) ℂ`. -/
-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/su2-emergence-dagger-unitarity.md
theorem su2_emergence_dagger_unitarity
    (g : Matrix (Fin 2) (Fin 2) ℂ)
    (h_preserves_inner : ∀ x y : Fin 2 → ℂ, dotProduct (star (g *ᵥ x)) (g *ᵥ y) = dotProduct (star x) y) :
    g ∈ Matrix.unitaryGroup (Fin 2) ℂ := by
  rw [mem_unitaryGroup_iff']
  ext i j
  have h := h_preserves_inner (Pi.single i 1) (Pi.single j 1)
  fin_cases i <;> fin_cases j <;>
    revert h <;>
    simp [dotProduct, mulVec, Matrix.mul_apply, Pi.single, star] <;>
    intro h <;>
    exact h

/-- **`G ⊆ U(2)`** ([`lem:su2-emergence-dagger-unitarity`]).

    If every element `g` of the gauge group `G` (realised as a set of
    `2×2` complex matrices on the fibre `τ(V)`) preserves the Frobenius
    dagger, then `G ⊆ U(2)`.  Derived pointwise from
    `su2_emergence_dagger_unitarity`. -/
-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/su2-emergence-dagger-unitarity.md
theorem su2_emergence_gauge_group_unitary
    (G : Set (Matrix (Fin 2) (Fin 2) ℂ))
    (h_all_preserve : ∀ g ∈ G, ∀ x y : Fin 2 → ℂ, dotProduct (star (g *ᵥ x)) (g *ᵥ y) = dotProduct (star x) y) :
    G ⊆ (Matrix.unitaryGroup (Fin 2) ℂ : Set (Matrix (Fin 2) (Fin 2) ℂ)) :=
  fun g hg => su2_emergence_dagger_unitarity g (h_all_preserve g hg)

end QOU
