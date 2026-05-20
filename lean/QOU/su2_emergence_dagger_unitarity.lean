/-!
# QOU.su2_emergence_dagger_unitarity — gauge-group containment `G ⊆ U(2)`

**Lemma** ([`lem:su2-emergence-dagger-unitarity`](../../../quantum-observable-universe/quantum-observable-universes/su2-emergence-dagger-unitarity.md)).

*Under the QOU hypotheses of [emergence of the gauge group](#thm:su2-emergence),
every tensor automorphism `g ∈ G` preserves the Frobenius dagger
on `τ(V)`; equivalently, `G ⊆ U(2)`.*

The Lean encoding records the assertion as a `Prop`-valued class
field hypothesised against an abstract `GaugeContext` carrying
the data of [`thm:su2-emergence`].  Concretising the abstract
classes to the standard Mathlib unitary group is downstream work
once [`thm:su2-emergence`] is itself Lean-translated.

-- Ref: [manuscript] quantum-observable-universe/quantum-observable-universes/su2-emergence-dagger-unitarity.md
-/

namespace QOU

/-- Abstract container for the emergence-of-gauge-group context
    of [`thm:su2-emergence`]: a 2-dimensional categorical object `V`,
    a gauge group `G` of tensor automorphisms acting on it, and a
    Frobenius dagger structure on the fibre `τ(V)`. -/
class SU2EmergenceContext where
  /-- The categorical object `V` of dimension 2 (treated abstractly). -/
  V : Type
  /-- The fibre functor's image `τ(V)`. -/
  tauV : Type
  /-- The gauge group `G` (abstract; substitute for `Matrix.Unitary 2 ℂ`
      or similar at the concretisation step). -/
  G : Type
  /-- A predicate "the element `g : G` preserves the Frobenius dagger
      on `τ(V)`". -/
  preserves_dagger : G → Prop
  /-- A predicate "the gauge group `G` is contained in the unitary group
      `U(2)` on `τ(V)`". -/
  contained_in_U2 : Prop

/-- **`G ⊆ U(2)` from Frobenius-dagger preservation** ([`lem:su2-emergence-dagger-unitarity`]).

    Under the QOU hypothesis that every `g ∈ G` preserves the Frobenius
    dagger on `τ(V)`, the gauge group `G` is contained in `U(2)`.

    The implication is recorded abstractly: a context whose every
    element preserves the dagger satisfies the `contained_in_U2`
    predicate.  Concretising both sides to Mathlib's `Matrix.unitary`
    structure is downstream work (requires the
    [`thm:su2-emergence`] Lean translation). -/
-- Ref: [manuscript] quantum-observable-universe/quantum-observable-universes/su2-emergence-dagger-unitarity.md
theorem su2_emergence_dagger_unitarity
    [ctx : SU2EmergenceContext]
    (h_all_preserve : ∀ g : ctx.G, ctx.preserves_dagger g) :
    ctx.contained_in_U2 := by
  -- Manuscript argument: dagger-preservation pointwise lifts to
  -- group-level inclusion in `U(2)`. Concretisation deferred to the
  -- Lean translation of `thm:su2-emergence`.
  -- Ref: [manuscript] quantum-observable-universe/quantum-observable-universes/su2-emergence-dagger-unitarity.md
  sorry

end QOU
