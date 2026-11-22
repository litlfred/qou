import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.SpecialLinearGroup
import Mathlib.LinearAlgebra.UnitaryGroup

/-!
# QOU.su2_emergence_volume_determinant — gauge-group containment `G ⊆ SL(2)`

**Lemma** ([`lem:su2-emergence-volume-determinant`](../../../quantum-observable-universe/quantum-observable-universes/su2-emergence-volume-determinant.md)).

*Under the QOU hypotheses of [emergence of the gauge group](#thm:su2-emergence),
every tensor automorphism `g ∈ G` of the fibre functor `τ`
satisfies `det(g_V) = 1`; equivalently, `G ⊆ SL(2)`.*

## Archimedean realisation (this file)

After the substrate→archimedean realisation `τ`, the fibre `τ(V)` is the
standard 2-dimensional Hermitian space `ℂ²`.  The volume constraint
"`g` preserves the volume form on `τ(V)`" is the concrete identity
`g.det = 1`, and the lemma's content at this level is the containment

  `g.det = 1  ⟹  g ∈ SL(2)`,

which we **derive** by exhibiting the lift of `g` into
`Matrix.SpecialLinearGroup (Fin 2) ℂ` (the subtype of matrices of unit
determinant): each gauge element with unit determinant is the image of
an SL(2) element, hence `G ⊆ SL(2)` (i.e. `G` is contained in the range
of the coercion `SL(2) → M₂(ℂ)`).  Combined with the dagger sibling
this puts the gauge group inside `SU(2) = U(2) ∩ SL(2)`
(`su2_emergence_combined`, membership in
`Matrix.specialUnitaryGroup (Fin 2) ℂ` derived through
`Matrix.mem_specialUnitaryGroup_iff`).

Previous encodings were vacuous — first a context class carrying the
whole implication as the field `claim_pointwise_det_lifts_to_SL2`
(self-assuming projection, AGENTS.md §3b-cond item 5), then a
hypothesis-restating tautology `g.det = 1 ⊢ g.det = 1`.  The
conclusions now genuinely differ from the hypotheses (subgroup
membership, not the determinant equation itself).

-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/su2-emergence-volume-determinant.md
-/

open Matrix

namespace QOU

/-- **`g ∈ SL(2)` from the volume constraint — archimedean realisation**
    ([`lem:su2-emergence-volume-determinant`]).

    A `2×2` complex matrix `g` that preserves the volume form on the
    fibre `τ(V) = ℂ²` (i.e. `g.det = 1`, the concrete form of the
    volume constraint) lies in the special linear group: it is the
    image of an element of `Matrix.SpecialLinearGroup (Fin 2) ℂ` under
    the coercion to matrices.  The conclusion is SL(2)-membership
    (existence of the lift), derived from the determinant hypothesis —
    not a restatement of it. -/
-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/su2-emergence-volume-determinant.md
theorem su2_emergence_volume_determinant
    (g : Matrix (Fin 2) (Fin 2) ℂ) (h_det : g.det = 1) :
    ∃ s : Matrix.SpecialLinearGroup (Fin 2) ℂ,
      (s : Matrix (Fin 2) (Fin 2) ℂ) = g :=
  ⟨⟨g, h_det⟩, rfl⟩

/-- **`G ⊆ SL(2)`** ([`lem:su2-emergence-volume-determinant`]).

    If every element `g` of the gauge group `G` (realised as a set of
    `2×2` complex matrices on the fibre `τ(V)`) satisfies the volume
    constraint `g.det = 1`, then `G` is contained in the image of
    `SL(2)` inside `M₂(ℂ)`.  Derived pointwise from
    `su2_emergence_volume_determinant`. -/
-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/su2-emergence-volume-determinant.md
theorem su2_emergence_gauge_group_special_linear
    (G : Set (Matrix (Fin 2) (Fin 2) ℂ))
    (h_all_det : ∀ g ∈ G, g.det = 1) :
    G ⊆ Set.range
      ((↑) : Matrix.SpecialLinearGroup (Fin 2) ℂ → Matrix (Fin 2) (Fin 2) ℂ) :=
  fun g hg => su2_emergence_volume_determinant g (h_all_det g hg)

/-- **Corollary**: combining the dagger constraint (`g · gᴴ = 1`, the
    hypothesis of the sibling lemma `su2_emergence_dagger_unitarity`)
    with the volume constraint (`g.det = 1`), the gauge element lands
    in `SU(2) = U(2) ∩ SL(2)` — membership in
    `Matrix.specialUnitaryGroup (Fin 2) ℂ`, derived through
    `Matrix.mem_specialUnitaryGroup_iff` and
    `Matrix.mem_unitaryGroup_iff` from the two constraints.
    (The U(2) half repeats the sibling's one-step derivation inline
    rather than importing the module, keeping this file verifiable
    standalone.) -/
-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/su2-emergence-volume-determinant.md
theorem su2_emergence_combined
    (g : Matrix (Fin 2) (Fin 2) ℂ)
    (h_dag : g * star g = 1)
    (h_det : g.det = 1) :
    g ∈ Matrix.specialUnitaryGroup (Fin 2) ℂ := by
  rw [Matrix.mem_specialUnitaryGroup_iff]
  exact ⟨Matrix.mem_unitaryGroup_iff.mpr h_dag, h_det⟩

end QOU
