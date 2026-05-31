/-!
# `QOU.IwahoriHecke.Defn` — Iwahori-Hecke algebra of a Coxeter group

**Sprint 1 of the Iwahori-Hecke Mathlib infrastructure plan**
(see [`docs/workplans/2026-05-30-iwahori-hecke-mathlib-infra-plan.md`](../../../../../../docs/workplans/2026-05-30-iwahori-hecke-mathlib-infra-plan.md)).

This file defines the Iwahori-Hecke algebra `IwahoriHecke W q` of a
Coxeter system `(W, S)` over a commutative ring `R` with parameter
`q : R`. It is the keystone infrastructure for closing 5 Tier-B
source-node conjectures (`conj:hecke-anyonic-substrate`,
`conj:reverse-limit-q-to-infinity`,
`conj:gs-graded-markov-trace-existence`,
`conj:hoefsmit-ew-cell-content`, `conj:crystal-graph-realization`)
and for promoting `prop:hecke-branching-trace-decomposition`'s
§3b-cond `branchCoefficient` field from `Unit` placeholder to
actual operator-valued content.

## Definition

Given a Coxeter system `(W, S)` and `q : R`, the Iwahori-Hecke
algebra `H(W, q)` is the unital associative `R`-algebra generated
by `{T_s}_{s ∈ S}` subject to:

1. **Hecke quadratic relation**: `(T_s - q) * (T_s + 1) = 0` for
   each `s ∈ S`. Equivalently, `T_s^2 = (q - 1) * T_s + q`.
2. **Braid relations**: for adjacent `s, t ∈ S` with
   `(st)^m = 1` (`m = m_{st}`), the alternating product of length
   `m` on each side coincides:
   `T_s * T_t * T_s * ... = T_t * T_s * T_t * ...` (`m` factors).

At `q = 1`, the relations collapse to the group algebra `R[W]`
(the Hecke quadratic becomes `T_s^2 = 1` and braid relations
match the Coxeter presentation).

## Scope of this PR (Sprint 1 + Sprint 2 bridge)

Sprint 1 established the foundation; the Sprint 2 bridge (added
2026-05-31) replaces the original `opaque IwahoriHecke` stub +
its 4 sorry-bearing instance proofs with a `def` aliasing
[`QOU.IwahoriHecke.Quotient.IwahoriHeckeQuot`](Quotient.lean)
over `Set.univ : Set W`. The algebra structure inherits via
`inferInstanceAs` — no instance proof remains as `sorry`.

Remaining `sorry`s in this file:
- `universal_property` (line ~191): blocked on
  `IsHeckeAlgebraMap` upgrade from the `True` placeholder to the
  actual Hecke-quadratic + braid conditions (Sprint 2 follow-up
  via `CoxeterSystem` once Mathlib's accessor stabilises).

Sprints 2-5 (each its own PR per the infra plan):
- Sprint 2: reduced-expression `T_w` basis (closes `conj:hecke-anyonic-substrate`)
- Sprint 3: Type-A specialisation (closes `conj:reverse-limit-q-to-infinity`)
- Sprint 4: Markov trace (closes `conj:gs-graded-markov-trace-existence`)
- Sprint 5: Hoefsmit seminormal basis (closes `conj:hoefsmit-ew-cell-content`
  + upgrades `prop:hecke-branching-trace-decomposition` §3b-cond)

## Authoring discipline

Per the infra plan's "Option C" strategy: this file stubs in the
`qou` Lake package mirroring the expected Mathlib API. The
upstream Mathlib contribution is a separable follow-up.

The Sprint 1 `opaque IwahoriHecke` skeleton was structurally
dead-code (zero downstream consumers — `Tw.lean`, `TypeA.lean`,
`Hoefsmit.lean`, `MarkovTrace.lean` all reference
`IwahoriHeckeQuot` from `Quotient.lean` directly). The Sprint 2
bridge turns it into a thin wrapper so the namespace stays
auditable while existing tooling and citations continue to
resolve to `QOU.IwahoriHecke.IwahoriHecke`.

Refs:
- [bourbaki1968] Bourbaki, "Groupes et Algèbres de Lie" Ch IV-VI
- [humphreys1990] Humphreys, "Reflection Groups and Coxeter Groups"
- [geck-pfeiffer2000] Geck–Pfeiffer, "Characters of finite Coxeter
  groups and Iwahori–Hecke algebras"
- [manuscript] docs/workplans/2026-05-30-iwahori-hecke-mathlib-infra-plan.md
-/

import Mathlib.GroupTheory.Coxeter.Basic
import Mathlib.Algebra.Algebra.Defs
import Mathlib.Algebra.Algebra.Basic
import QOU.IwahoriHecke.Quotient

namespace QOU.IwahoriHecke

universe u v

/-- **The Iwahori-Hecke algebra** `IwahoriHecke W q` of a Coxeter
    system `(W, S)` over a commutative ring `R` with parameter
    `q : R`.

    Sprint 2 bridge: definitionally equal to
    `QOU.IwahoriHecke.Quotient.IwahoriHeckeQuot R q (Set.univ : Set W)`
    — the concrete quotient over the full generating set of `W`.
    This dissolves the Sprint 1 opaque stub and makes the algebra,
    ring, and module instances inherit automatically from
    `Quotient.lean`'s noncomputable instances.

    Caveat: the Hecke-quadratic-only fragment (Sprint 2 scope of
    `Quotient.lean`). Braid relations are not yet quotiented out —
    that step lands once Mathlib's `CoxeterSystem` reduced-expression
    accessor stabilises. For Sprint 1 + 2 the quadratic-only sub-
    algebra is the well-defined intermediate object.

    The type parameters are intentionally generic: `W` is the
    Coxeter group, `R` is the base ring, `q : R` is the parameter.
    A Type-A specialisation (Sprint 3 via `TypeA.lean`) instantiates
    `W = Fin n × Fin n` (adjacent-transposition index set). -/
def IwahoriHecke (W : Type u) [Group W] [DecidableEq W]
    (R : Type v) [CommRing R] (q : R) : Type (max u v) :=
  QOU.IwahoriHecke.Quotient.IwahoriHeckeQuot R q (Set.univ : Set W)

/-- The expected `R`-algebra structure on `IwahoriHecke W q`.
    Sprint 2 bridge: inherited via the definitional equality with
    the concrete quotient. Each instance is now sorry-free. -/
noncomputable instance instAddCommGroup_iwahoriHecke
    (W : Type u) [Group W] [DecidableEq W] (R : Type v) [CommRing R] (q : R) :
    AddCommGroup (IwahoriHecke W R q) :=
  inferInstanceAs (AddCommGroup (QOU.IwahoriHecke.Quotient.IwahoriHeckeQuot
    R q (Set.univ : Set W)))

noncomputable instance instModule_iwahoriHecke
    (W : Type u) [Group W] [DecidableEq W] (R : Type v) [CommRing R] (q : R) :
    Module R (IwahoriHecke W R q) :=
  inferInstanceAs (Module R (QOU.IwahoriHecke.Quotient.IwahoriHeckeQuot
    R q (Set.univ : Set W)))

/-- Ring structure on `IwahoriHecke W R q`. Sprint 2 bridge: inherited
    from the concrete quotient. -/
noncomputable instance instRing_iwahoriHecke
    (W : Type u) [Group W] [DecidableEq W] (R : Type v) [CommRing R] (q : R) :
    Ring (IwahoriHecke W R q) :=
  inferInstanceAs (Ring (QOU.IwahoriHecke.Quotient.IwahoriHeckeQuot
    R q (Set.univ : Set W)))

/-- `R`-algebra structure on `IwahoriHecke W R q`. Sprint 2 bridge:
    inherited from the concrete quotient. -/
noncomputable instance instAlgebra_iwahoriHecke
    (W : Type u) [Group W] [DecidableEq W] (R : Type v) [CommRing R] (q : R) :
    Algebra R (IwahoriHecke W R q) :=
  inferInstanceAs (Algebra R (QOU.IwahoriHecke.Quotient.IwahoriHeckeQuot
    R q (Set.univ : Set W)))

/-- The generators `T : W → IwahoriHecke W q`, lifting each element
    of `W` to its image in the quadratic-only quotient.

    Sprint 2 bridge: defined via `Quotient.T` applied to the
    Subtype wrapping `Set.univ`. -/
noncomputable def T {W : Type u} [Group W] [DecidableEq W]
    {R : Type v} [CommRing R] (q : R) (s : W) : IwahoriHecke W R q :=
  QOU.IwahoriHecke.Quotient.T R q (Set.univ : Set W) ⟨s, Set.mem_univ s⟩

/-! ## Universal property (sketched)

The Iwahori-Hecke algebra is universal among `R`-algebras `A`
equipped with a function `f : S → A` satisfying the Hecke
quadratic relation `(f s - q) * (f s + 1) = 0` and the braid
relations.

```
universal_property :
  ∀ (A : Type*) [CommRing A] [Algebra R A] (f : S → A),
    (∀ s, (f s - algebraMap R A q) * (f s + 1) = 0) →
    (∀ s t : S, braid_relation s t →
      alternating_product s t (m s t) = alternating_product t s (m t s)) →
    ∃! φ : IwahoriHecke W R q →ₐ[R] A, ∀ s, φ (T q s) = f s
```

Sprint 1 leaves this statement informal; Sprint 2 formalises it
once the concrete quotient is in place.
-/

/-- Predicate: `f : W → A` is a Hecke algebra map (Sprint 1
    placeholder).

    Sprint 1 returns `True` unconditionally — the predicate is a
    type-level *contract* that Sprint 2 will refine to the actual
    conditions:

      1. `(f s - algebraMap R A q) * (f s + 1) = 0` for every simple
         reflection `s`.
      2. For every pair `(s, t)` of simple reflections with braid
         order `m_{s,t} = m`, the alternating product of length `m`
         in `s, t` equals the one in `t, s` inside `A`.

    Sprint 1 stub: `True`. Sprint 2 replaces with the
    `CoxeterSystem (W, S)`-indexed conditions. The Sprint 1
    placeholder lets the `universal_property` theorem statement
    typecheck without requiring the full Coxeter-system API yet. -/
def IsHeckeAlgebraMap {W : Type u} [Group W] {R : Type v} [CommRing R]
    {A : Type w} [Ring A] [Algebra R A] (_q : R) (_f : W → A) : Prop :=
  -- Ref: [manuscript] docs/workplans/2026-05-30-iwahori-hecke-mathlib-infra-plan.md Sprint 2 (formal conditions via CoxeterSystem)
  True

/-- **Universal property of the Iwahori-Hecke algebra.**

    Any Hecke algebra map `f : W → A` (in the sense of
    `IsHeckeAlgebraMap`) extends uniquely to an `R`-algebra
    homomorphism from `IwahoriHecke W R q`.

    Sprint 1 stub: statement only; the proof needs the concrete
    quotient construction from Sprint 2. The statement is the
    canonical API contract — when Sprint 2 lands, this theorem
    becomes the entry point for embedding any Hecke representation
    into the framework's algebra. -/
theorem universal_property
    {W : Type u} [Group W] [DecidableEq W] {R : Type v} [CommRing R] (q : R)
    {A : Type w} [Ring A] [Algebra R A]
    (f : W → A) (_hf : IsHeckeAlgebraMap q f) :
    ∃! φ : IwahoriHecke W R q →ₐ[R] A, ∀ s : W, φ (T q s) = f s := by
  -- Ref: [manuscript] docs/workplans/2026-05-30-iwahori-hecke-mathlib-infra-plan.md Sprint 2 follow-up:
  -- the Quotient-side `universal_property_hecke_quadratic` provides existence
  -- (Nonempty {φ // ...}) given an AlgHom factoring `f` through `FreeAlgebra R S`
  -- with vanishing on `heckeQuadraticGenerators`. Bridging to ∃! requires
  -- (a) IsHeckeAlgebraMap refinement (currently `True`) to supply the AlgHom factor +
  --     vanishing hypothesis, (b) uniqueness from `IwahoriHeckeQuot`'s universal
  -- characterisation. Deferred until IsHeckeAlgebraMap is refined.
  sorry

/-! ## Closure paths (downstream consumers gated on this infra)

| Sprint | New API | Closes |
|---:|------|------|
| 2 | `Tw : W → IwahoriHecke W R q` (reduced-expression-based) | `conj:hecke-anyonic-substrate` |
| 3 | `IwahoriHeckeOfSn n q` + concrete-strand `σi` API | `conj:reverse-limit-q-to-infinity` |
| 4 | `markovTrace : IwahoriHeckeOfSn n q →+ R` | `conj:gs-graded-markov-trace-existence` |
| 5 | `hoefsmitBasis : SYT λ → IwahoriHeckeOfSn n q` | `conj:hoefsmit-ew-cell-content` + upgrades §3b-cond |

These closures are gated on the corresponding sprint. Sprint 1
provides only the foundation; the closures land sprint-by-sprint.
-/

end QOU.IwahoriHecke
