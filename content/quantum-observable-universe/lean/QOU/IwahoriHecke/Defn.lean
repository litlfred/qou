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

## Scope of this PR (Sprint 1)

Sprint 1 establishes the foundation:
- `IwahoriHecke W q` type (skeleton — quotient construction below)
- Universal-property statement (`R`-algebra map `IwahoriHecke W q →ₐ A`
  characterised by where each `T_s` is sent, modulo the relations)
- `q = 1` reduction (forward direction: there is a canonical map
  `IwahoriHecke W 1 → R[W]`)

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

The skeleton below uses **placeholders** (`sorry`-equivalent
`opaque` definitions and abstract typeclasses) at points where
the full implementation requires Mathlib material not yet
imported here. Each placeholder is tagged `-- Ref: [pending Sprint N]`
or `-- Ref: [Mathlib upstream]` so the implementation gaps are
auditable. Sprint 2 will replace the `opaque` declarations with
concrete constructions.

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

namespace QOU.IwahoriHecke

universe u v

/-- **The Iwahori-Hecke algebra** `IwahoriHecke W q` of a Coxeter
    system `(W, S)` over a commutative ring `R` with parameter
    `q : R`.

    Sprint 1 stub: declared as an abstract `Type` with the
    expected algebra structure. The concrete construction (quotient
    of the free `R`-algebra on `{T_s}_{s ∈ S}` by the Hecke + braid
    relations) lives in Sprint 2.

    The type parameters are intentionally generic: `W` is the
    Coxeter group, `R` is the base ring, `q : R` is the parameter.
    A Type-A specialisation (Sprint 3) instantiates `W = symmetricGroup n`. -/
opaque IwahoriHecke (W : Type u) [Group W] (R : Type v) [CommRing R] (_q : R) : Type (max u v)

/-- The expected `R`-algebra structure on `IwahoriHecke W q`.
    Sprint 1 stub: declared abstractly; Sprint 2 constructs the
    instance via the quotient algebra. -/
instance instCommRing_iwahoriHecke
    (W : Type u) [Group W] (R : Type v) [CommRing R] (q : R) :
    AddCommGroup (IwahoriHecke W R q) := by
  -- Ref: [manuscript] docs/workplans/2026-05-30-iwahori-hecke-mathlib-infra-plan.md Sprint 2 (concrete quotient construction)
  sorry

instance instModule_iwahoriHecke
    (W : Type u) [Group W] (R : Type v) [CommRing R] (q : R) :
    Module R (IwahoriHecke W R q) := by
  -- Ref: [manuscript] docs/workplans/2026-05-30-iwahori-hecke-mathlib-infra-plan.md Sprint 2 (Module instance via concrete quotient)
  sorry

/-- The generators `T : S → IwahoriHecke W q`, one per simple
    reflection. Sprint 1 stub: signature only; the concrete
    embedding lives in Sprint 2. -/
opaque T {W : Type u} [Group W] {R : Type v} [CommRing R] (q : R)
    (_s : W) : IwahoriHecke W R q

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
