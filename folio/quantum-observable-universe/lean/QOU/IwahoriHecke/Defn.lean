import Mathlib.Algebra.Algebra.Defs
import Mathlib.Algebra.Algebra.Basic
import QOU.IwahoriHecke.Quotient
import QOU.MathlibExt.IwahoriHeckeAlgebra
import Mathlib.GroupTheory.OrderOfElement

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
- [geckpfeiffer2000] Geck–Pfeiffer, "Characters of finite Coxeter
  groups and Iwahori–Hecke algebras"
- [leitner2026] docs/workplans/2026-05-30-iwahori-hecke-mathlib-infra-plan.md
-/

namespace QOU.IwahoriHecke

universe u v w

/-! ## The algebra

**Rebuilt 2026-08-30.**  This definition used to read

```
def IwahoriHecke (W) [Group W] [DecidableEq W] (R) [CommRing R] (q : R) :=
  Quotient.IwahoriHeckeQuot R q (Set.univ : Set W)
```

which had two defects, one on top of the other.

* `IwahoriHeckeQuot` imposes the **quadratic relation only** — its braid relations were
  deferred — so the object was the free product of one copy of `R[x]/((x−q)(x+1))` per
  generator.
* Worse, passing `Set.univ : Set W` imposed that relation on **every element of the
  group**, not on the simple reflections.  In the actual Hecke algebra `T_w` satisfies
  the quadratic relation exactly when `ℓ(w) = 1`; for `w = st` of order three it does
  not.  So the object was not the "quadratic-only intermediate" its docstring claimed,
  and it admitted no natural map to or from a Hecke algebra.

Both are fixed by building on `QOU.MathlibExt.IwahoriHecke.HeckeAlgebra`, which imposes
**both** relation families, and by taking the simple-reflection set as a parameter
rather than hard-coding all of `W`.

The Coxeter matrix comes from the group itself: `m(s,t) = orderOf (s * t)`.  The long-
standing blocker recorded here — that the order accessor was *"in flux in Mathlib's
`CoxeterSystem` API"* — did not apply: `orderOf` is plain Mathlib group theory and needs
no accessor at all. -/

/-- The Coxeter matrix carried by a subset of a group: `m(s,t) = orderOf (s · t)`.

For a genuine Coxeter system this is the Coxeter matrix on the nose.  Nothing downstream
requires that `S` be one — the construction is well-defined for any subset, and a caller
that has a `CoxeterSystem` may pass its matrix instead. -/
noncomputable def coxeterMatrixOn {W : Type u} [Group W] (S : Set W) : S → S → ℕ :=
  fun s t => orderOf ((s : W) * (t : W))

/-- **The Iwahori–Hecke algebra** of `(W, S)` over `R` at parameter `q`, in the Iwahori
normalisation `(T_s − q)(T_s + 1) = 0` together with the braid relations. -/
def IwahoriHecke (W : Type u) [Group W] [DecidableEq W]
    (R : Type v) [CommRing R] (q : R) (S : Set W) : Type (max u v) :=
  QOU.MathlibExt.IwahoriHecke.HeckeAlgebra R q (coxeterMatrixOn S)

noncomputable instance instRing_iwahoriHecke
    (W : Type u) [Group W] [DecidableEq W] (R : Type v) [CommRing R] (q : R) (S : Set W) :
    Ring (IwahoriHecke W R q S) :=
  inferInstanceAs (Ring (QOU.MathlibExt.IwahoriHecke.HeckeAlgebra R q (coxeterMatrixOn S)))

noncomputable instance instAlgebra_iwahoriHecke
    (W : Type u) [Group W] [DecidableEq W] (R : Type v) [CommRing R] (q : R) (S : Set W) :
    Algebra R (IwahoriHecke W R q S) :=
  inferInstanceAs (Algebra R (QOU.MathlibExt.IwahoriHecke.HeckeAlgebra R q (coxeterMatrixOn S)))

/-- The generator `T_s`, for `s` a **simple reflection**.

Note the index: `s : S`, not `s : W`.  That is the substance of the rebuild — the old
`T` accepted any group element and asserted a quadratic relation for it. -/
noncomputable def T {W : Type u} [Group W] [DecidableEq W]
    {R : Type v} [CommRing R] (q : R) {S : Set W} (s : S) : IwahoriHecke W R q S :=
  QOU.MathlibExt.IwahoriHecke.T R q (coxeterMatrixOn S) s

variable {W : Type u} [Group W] [DecidableEq W] {R : Type v} [CommRing R] {q : R} {S : Set W}

/-- **The quadratic relation holds.** -/
theorem T_quadratic (s : S) :
    (T q s - algebraMap R (IwahoriHecke W R q S) q) * (T q s + 1) = 0 :=
  QOU.MathlibExt.IwahoriHecke.T_quadratic s

/-- **The braid relation holds** — the half the old construction was missing. -/
theorem T_braid (s t : S) :
    QOU.MathlibExt.IwahoriHecke.altProd (T q s) (T q t) (coxeterMatrixOn S s t)
      = QOU.MathlibExt.IwahoriHecke.altProd (T q t) (T q s) (coxeterMatrixOn S t s) :=
  QOU.MathlibExt.IwahoriHecke.T_braid s t

/-! ## Universal property

Both halves now come straight from the `HeckeAlgebra` construction, so the hand-rolled
existence proof and the `axiom` that used to stand in for uniqueness are both gone. -/

/-- **Hecke algebra map**: a family on the simple reflections satisfying *both* defining
families.

The old predicate of this name asserted only the quadratic relation, and asserted it for
every `s : W`.  Its docstring defended the over-quantification by saying the restriction
to simple reflections "happens upstream ... the caller passes an `f` that is only
nontrivial on `S`" — a constraint on callers, not on the predicate. -/
def IsHeckeAlgebraMap {A : Type w} [Ring A] [Algebra R A] (q : R) (S : Set W) (f : S → A) :
    Prop :=
  (∀ s : S, (f s - algebraMap R A q) * (f s + 1) = 0) ∧
  (∀ s t : S, QOU.MathlibExt.IwahoriHecke.altProd (f s) (f t) (coxeterMatrixOn S s t)
      = QOU.MathlibExt.IwahoriHecke.altProd (f t) (f s) (coxeterMatrixOn S t s))

/-- **The universal property of the Iwahori–Hecke algebra.**

Previously: existence proved by hand, uniqueness recorded as `axiom universal_property`
on the ground that the container had no `lake` binary.  Both are now discharged by
`QOU.MathlibExt.IwahoriHecke.exists_unique_lift`, and the target may be any `R`-algebra
rather than a commutative one. -/
-- Ref: [kassel2008] Kassel & Turaev, "Braid Groups", Springer 2008, Ch. 4
theorem universal_property {A : Type w} [Ring A] [Algebra R A]
    (f : S → A) (hf : IsHeckeAlgebraMap q S f) :
    ∃! φ : IwahoriHecke W R q S →ₐ[R] A, ∀ s : S, φ (T q s) = f s :=
  QOU.MathlibExt.IwahoriHecke.exists_unique_lift R q (coxeterMatrixOn S) f hf.1 hf.2

/-- Two algebra maps agreeing on the simple reflections are equal. -/
theorem hom_ext {A : Type w} [Ring A] [Algebra R A]
    (φ ψ : IwahoriHecke W R q S →ₐ[R] A) (h : ∀ s : S, φ (T q s) = ψ (T q s)) :
    φ = ψ :=
  QOU.MathlibExt.IwahoriHecke.hom_ext R q (coxeterMatrixOn S) φ ψ h

/-- **Each generator is invertible** whenever `q` is, so the presentation factors through
the braid group and `σ_s⁻¹` in the skein dictionary (§7a) denotes an actual element. -/
theorem isUnit_T (hq : IsUnit q) (s : S) : IsUnit (T q s) :=
  QOU.MathlibExt.IwahoriHecke.isUnit_T hq s

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
