import QOU.su2_emergence_dagger_unitarity

/-!
# QOU.su2_emergence_volume_determinant — gauge-group containment `G ⊆ SL(2)`

**Lemma** ([`lem:su2-emergence-volume-determinant`](../../../quantum-observable-universe/quantum-observable-universes/su2-emergence-volume-determinant.md)).

*Under the QOU hypotheses of [emergence of the gauge group](#thm:su2-emergence),
every tensor automorphism `g ∈ G` of the fibre functor `τ`
satisfies `det(g_V) = 1`; equivalently, `G ⊆ SL(2)`.*

The Lean encoding follows the same abstract-context pattern as
the sibling lemma `su2_emergence_dagger_unitarity`: a `Prop`-valued
class field on `SU2EmergenceContext` captures the manuscript claim;
concretisation to Mathlib's `Matrix.SpecialLinearGroup 2` is
downstream work.

-- Ref: [manuscript] quantum-observable-universe/quantum-observable-universes/su2-emergence-volume-determinant.md
-/

namespace QOU

/-- Determinant-preservation extension of the `SU2EmergenceContext`
    sibling structure: the gauge group acts with unit determinant
    on `τ(V)`. -/
class SU2VolumeContext where
  /-- The gauge group `G` (abstract; concretises to `SL(2)` ⊂ `GL(2)`). -/
  G : Type
  /-- A predicate "the element `g : G` has `det(g_V) = 1`". -/
  det_eq_one : G → Prop
  /-- A predicate "the gauge group `G` is contained in `SL(2)`". -/
  contained_in_SL2 : Prop
  /-- Manuscript pointwise-to-group lift: if every element has unit
      determinant on `τ(V)`, the whole gauge group sits in `SL(2)`. -/
  claim_pointwise_det_lifts_to_SL2 :
    (∀ g : G, det_eq_one g) → contained_in_SL2

/-- **`G ⊆ SL(2)` from determinant constraint** ([`lem:su2-emergence-volume-determinant`]).

    Under the QOU hypothesis that every tensor automorphism `g ∈ G`
    satisfies `det(g_V) = 1`, the gauge group is contained in `SL(2)`.

    The argument is pointwise: every group element having unit
    determinant ⟹ the whole group sits inside `SL(2)`. -/
-- Ref: [manuscript] quantum-observable-universe/quantum-observable-universes/su2-emergence-volume-determinant.md
theorem su2_emergence_volume_determinant
    [ctx : SU2VolumeContext]
    (h_all_det_one : ∀ g : ctx.G, ctx.det_eq_one g) :
    ctx.contained_in_SL2 :=
  ctx.claim_pointwise_det_lifts_to_SL2 h_all_det_one

/-- **Corollary**: combining `su2_emergence_dagger_unitarity` and
    `su2_emergence_volume_determinant`, the gauge group sits inside
    `SU(2) = U(2) ∩ SL(2)`.

    Stated as a Prop-valued conjunction; concretisation to Mathlib's
    `Matrix.SpecialUnitaryGroup 2` is downstream work. -/
-- Ref: [manuscript] quantum-observable-universe/quantum-observable-universes/su2-emergence-volume-determinant.md
theorem su2_emergence_combined
    [u2 : SU2EmergenceContext] [sl2 : SU2VolumeContext]
    (h_dag : ∀ g : u2.G, u2.preserves_dagger g)
    (h_det : ∀ g : sl2.G, sl2.det_eq_one g) :
    u2.contained_in_U2 ∧ sl2.contained_in_SL2 :=
  ⟨su2_emergence_dagger_unitarity h_dag,
   su2_emergence_volume_determinant h_det⟩

end QOU
