import Mathlib.GroupTheory.SpecificGroups.Quaternion

/-!
# QOU.Archimedean.descartes_braid_structure

Canonical Lean declaration for content block at
[`quantum-observable-universe/archimedean-universe/descartes-braid-structure.ts`](quantum-observable-universe/archimedean-universe/descartes-braid-structure.ts).

The image of the braid representation `ρ₃ : B₃ → Aut_C(V⊗³)` in `SU(2)`
is the binary dihedral (dicyclic) group `Dic₃` of order `12`.  Here we
**formalise the `Dic₃` structure** (Mathlib's `QuaternionGroup 3`,
order `4·3 = 12`) and **derive** the order claim from the single genuine
categorical input — the group isomorphism `image ≃* Dic₃` — rather than
projecting it from an opaque context field.
-/

namespace QOU.Archimedean

/-- The binary dihedral (dicyclic) group `Dic₃` — the image of `ρ₃` in
    `SU(2)`.  Concretely Mathlib's `QuaternionGroup 3` (the generalised
    quaternion / dicyclic group of order `4·3 = 12`). -/
abbrev Dic3 := QuaternionGroup 3

/-- `Dic₃` has order `12` — a genuine computation via
    `QuaternionGroup.card` (`4 * 3 = 12`). -/
theorem dic3_card : Fintype.card Dic3 = 12 := by
  haveI : NeZero (3 : ℕ) := ⟨by decide⟩
  have h := QuaternionGroup.card (n := 3)
  norm_num at h
  exact h

/-- **Descartes braid structure** (claims i–ii).

Let `(C, A, τ)` be a Descartes universe.  The braiding of
`C = Rep(SU_q(2))` induces a representation
`ρ₃ : B₃ → Aut_C(V⊗³)` whose image in `SU(2)` (via the fibre functor `τ`)
is the binary dihedral group `Dic₃` of order `12`
([manuscript claims (i) faithful image of order ≥ 12, (ii) image is
`Dic₃` of order `12`]).

The single conjectural input is the **group isomorphism**
`himg : G ≃* Dic₃` identifying the braid image `G` with `Dic₃` — the open
categorical fact.  Both numerical claims are then *derived*: the order is
`12` by transport along `himg` and `dic3_card`, and faithfulness
(`order ≥ 12`) follows.  (Claims (iii) three `S₃` colour-sectors and
(iv) `p`-adic universality concern the ambient `S₅` and base ring and are
tracked separately.) -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/descartes-braid-structure.ts
theorem descartes_braid_structure
    {G : Type} [Group G] [Fintype G] (himg : G ≃* Dic3) :
    12 ≤ Fintype.card G ∧ Fintype.card G = 12 := by
  have h : Fintype.card G = 12 := (Fintype.card_congr himg.toEquiv).trans dic3_card
  exact ⟨h.ge, h⟩

end QOU.Archimedean
