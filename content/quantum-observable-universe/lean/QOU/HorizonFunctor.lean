import Mathlib.Tactic
import Mathlib.Topology.Basic

/-!
# QOU.HorizonFunctor

**Canonical declaration** for content block at
[`quantum-observable-universe/information-theory/horizon-functor.ts`](quantum-observable-universe/information-theory/horizon-functor.ts).

Formalises the manuscript **horizon functor**
`∂ : π₀(Bun°(ℙ(V))) → 𝒫(Bun ∖ Bun°)` sending each aeon `𝒜` to its boundary
— the configurations that are limits of diagrams in `𝒜` but have
`A₀|_𝒮 = 0` (hence lie *outside* the observable subcategory `Bun°`).

**Naming note.** The codomain is a **power set** `𝒫(…)`, so `∂` is encoded
as the set-valued map `boundary : Aeon → Set Config` — an object-level map,
not a `CategoryTheory.Functor` (no morphism-map/laws). This matches the
manuscript, which writes the target as `𝒫(…)` and observes ∂ degenerates to
the identity on component inclusions. "Functor" is a naming convention here.
-/

namespace QOU

/-- Data for the horizon functor.

    A `definition` carrier: the ambient configurations `Config`, the aeons
    `Aeon = π₀(Bun°)`, the observability predicate, and the boundary map
    `∂`, with the defining property that the boundary lands in the
    non-observable complement (`A₀ = 0`). -/
structure HorizonFunctor where
  /-- Objects of the ambient bundle category `Bun(ℙ(V))`. -/
  Config : Type
  /-- Aeons `π₀(Bun°)` (connected components of the observable subcategory). -/
  Aeon : Type
  /-- Observability predicate (membership in `Bun°`). -/
  observable : Config → Prop
  /-- The horizon / boundary map `∂`. -/
  boundary : Aeon → Set Config
  /-- The boundary of an aeon consists of non-observable configurations
      (`A₀|_𝒮 = 0`) — it lands in `Bun ∖ Bun°`. -/
  boundary_nonobservable : ∀ (𝒜 : Aeon) (c : Config), c ∈ boundary 𝒜 → ¬ observable c

namespace HorizonFunctor

variable (H : HorizonFunctor)

/-- The boundary of every aeon is disjoint from the observable subcategory:
    no observable configuration lies on any horizon. -/
theorem observable_not_mem_boundary (𝒜 : H.Aeon) {c : H.Config}
    (hc : H.observable c) : c ∉ H.boundary 𝒜 :=
  fun hmem => H.boundary_nonobservable 𝒜 c hmem hc

/-- Restated as set disjointness: `∂(𝒜) ∩ {observable} = ∅`. -/
theorem boundary_disjoint_observable (𝒜 : H.Aeon) :
    H.boundary 𝒜 ∩ {c | H.observable c} = ∅ := by
  ext c
  simp only [Set.mem_inter_iff, Set.mem_setOf_eq, Set.mem_empty_iff_false, iff_false]
  rintro ⟨hb, ho⟩
  exact H.boundary_nonobservable 𝒜 c hb ho

end HorizonFunctor

/-- **De-axiomatisation (bean `bqfr`): a genuine topological horizon.** Over
    any topological space of configurations with a real degree-0 section `A₀`,
    an aeon is a region and its horizon is the topological **frontier** of the
    region intersected with the `A₀ = 0` locus. `frontier` is Mathlib's real
    closure-minus-interior — the genuine "limits of diagrams in the aeon"
    operator — so `boundary_nonobservable` is a *theorem* (the boundary lies
    in `{A₀ = 0}` by construction), not an assumption. -/
def HorizonFunctor.ofSpace {X : Type} [TopologicalSpace X] {ι : Type}
    (A0 : X → ℝ) (region : ι → Set X) : HorizonFunctor where
  Config := X
  Aeon := ι
  observable c := A0 c ≠ 0
  boundary a := frontier (region a) ∩ {c | A0 c = 0}
  boundary_nonobservable _ _ hc hobs := hobs hc.2

-- Ref: [manuscript] quantum-observable-universe/information-theory/horizon-functor.ts

end QOU
