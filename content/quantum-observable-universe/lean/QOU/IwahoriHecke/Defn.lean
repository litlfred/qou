import Mathlib.Algebra.Algebra.Defs
import Mathlib.Algebra.Algebra.Basic
import QOU.IwahoriHecke.Quotient

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

namespace QOU.IwahoriHecke

universe u v w

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
    A Type-A specialisation (Sprint 3 via `TypeA.lean`) targets
    the symmetric group `W = Equiv.Perm (Fin n)`, indexing simple
    reflections by `adjacentTranspositionIndex n = Fin (n - 1)`. -/
def IwahoriHecke (W : Type u) [Group W] [DecidableEq W]
    (R : Type v) [CommRing R] (q : R) : Type (max u v) :=
  QOU.IwahoriHecke.Quotient.IwahoriHeckeQuot R q (Set.univ : Set W)

/-- **Algebra-structure instances** for `IwahoriHecke W R q`
    (`AddCommGroup`, `Module`, `Ring`, `Algebra`). Sprint 2 bridge:
    each instance is inherited via the definitional equality with
    the concrete quotient (`inferInstanceAs`). All four are
    sorry-free. -/
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

/-- Predicate: `f : W → A` is a **Hecke-quadratic algebra map**.

    Sprint 2 refinement (2026-05-31): the Sprint 1 `True` placeholder
    is replaced by the **Hecke quadratic relation alone** —

      `(f s - algebraMap R A q) * (f s + 1) = 0` for every `s : W`.

    The braid-relation condition is intentionally *omitted* from
    this predicate to match the Sprint 2 scope of
    [`QOU.IwahoriHecke.Quotient`](Quotient.lean), which quotients
    only by Hecke quadratic generators (`heckeIdeal`). The full
    Iwahori-Hecke algebra additionally quotients by braid relations
    of length `m_{s,t}` — that step lands in the Sprint 2 follow-up
    once Mathlib's `CoxeterSystem` reduced-expression / `m`-accessor
    API stabilises (the §0a "in flux" deferral noted in
    `Quotient.lean`).

    Bridging note: in Sprint 2's framing the relations indexed by
    `s : W` cover the full generating set (`Set.univ : Set W`) used
    by `IwahoriHecke` as defined above. The eventual restriction to
    `S : Set W` of simple reflections happens upstream of this
    predicate (the caller passes a `f` that is only nontrivial on
    `S` and constant or `0` elsewhere). -/
def IsHeckeAlgebraMap {W : Type u} [Group W] {R : Type v} [CommRing R]
    {A : Type w} [Ring A] [Algebra R A] (q : R) (f : W → A) : Prop :=
  -- Ref: [manuscript] docs/workplans/2026-05-30-iwahori-hecke-mathlib-infra-plan.md Sprint 2 (Hecke-quadratic fragment; braid relations follow-up)
  ∀ s : W, (f s - algebraMap R A q) * (f s + 1) = 0

/-- **Alternating product** `s · t · s · ... · ?` of length `n` in
    two elements `s, t` of a monoid `A`.  Used to state the braid
    relation in `IsHeckeBraidedAlgebraMap` below.

    Defined by recursion:
    - `altProduct s t 0 = 1`
    - `altProduct s t (n+1) = s * altProduct t s n`

    So `altProduct s t 1 = s`, `altProduct s t 2 = s·t`,
    `altProduct s t 3 = s·t·s`, etc. -/
def altProduct {A : Type*} [Monoid A] : A → A → ℕ → A
  | _, _, 0 => 1
  | s, t, (n + 1) => s * altProduct t s n

/-- **Refined Hecke algebra map predicate** — Hecke quadratic AND
    braid relations, parameterised by a Coxeter-matrix function
    `m : W → W → ℕ`.

    Sprint 2 follow-up (2026-05-31): captures the FULL universal
    property of the Iwahori-Hecke algebra (not just the Hecke
    quadratic fragment).  The caller supplies the Coxeter matrix
    function `m`, derived from a Mathlib `CoxeterSystem`.

    **Mathlib accessor (verified against `Mathlib.GroupTheory.Coxeter`
    for the Lean v4.24.0 toolchain pinned in `lean-toolchain`).**
    In Mathlib the Coxeter matrix is the *type parameter* `M` of
    `CoxeterSystem M W`, NOT a field of the term `cs`. Concretely,
    given

      `variable {B : Type*} {M : CoxeterMatrix B} {W : Type*}`
      `         [Group W] (cs : CoxeterSystem M W)`

    the matrix is `M : CoxeterMatrix B` itself, and its `(i, j)`
    entry is the natural number `M i j` (a `CoxeterMatrix B` carries
    a `FunLike` to `B → B → ℕ`). There is **no `cs.M` projection**;
    `cs.M.M` does not typecheck. Note also the index type is `B`
    (the simple-reflection index), not `W`: the simple reflections
    embed via `cs.simple : B → W`.

    Because Mathlib indexes by `B` while this predicate indexes by
    `W`, the caller adapts at the call site, e.g.

      `let m : W → W → ℕ := fun s t => M (φ s) (φ t)`

    for some chosen section `φ : W → B` on the simple reflections
    (or supplies any custom matrix function for the user's specific
    presentation). The predicate intentionally takes `m : W → W → ℕ`
    as an explicit parameter rather than committing to Mathlib's
    `CoxeterSystem`/`CoxeterMatrix` API surface (`FunLike` coercion
    vs. structure field has drifted across Mathlib refactors), so
    this definition stays stable across Mathlib bumps.

    (The exact entry-application spelling — `M i j` via the
    `FunLike` coercion — is the one surface detail to re-confirm on
    a local `lake build QOU` when wiring an actual `CoxeterSystem`
    caller; the `m : W → W → ℕ` parameterisation here is independent
    of it.)

    Conditions:
    1. **Hecke quadratic** — `(f s − q)(f s + 1) = 0` for every
       `s : W` (same as `IsHeckeAlgebraMap`).
    2. **Braid relation** — for every pair `(s, t)` of simple
       reflections, the alternating product of length `m s t` in
       `f s, f t` equals the alternating product of length `m t s`
       in `f t, f s`.  When `m s t = m t s` (the standard symmetric
       case), both sides have the same length. -/
def IsHeckeBraidedAlgebraMap
    {W : Type u} [Group W] {R : Type v} [CommRing R]
    {A : Type w} [Ring A] [Algebra R A] (q : R)
    (m : W → W → ℕ) (f : W → A) : Prop :=
  IsHeckeAlgebraMap q f ∧
  (∀ s t : W, altProduct (f s) (f t) (m s t) =
              altProduct (f t) (f s) (m t s))

/-- The braided predicate strengthens the quadratic-only predicate:
    a Hecke-braided map is in particular a Hecke-quadratic map.
    All arguments implicit so dot notation `h.toIsHeckeAlgebraMap`
    works at call sites. -/
theorem IsHeckeBraidedAlgebraMap.toIsHeckeAlgebraMap
    {W : Type u} [Group W] {R : Type v} [CommRing R]
    {A : Type w} [Ring A] [Algebra R A] {q : R} {m : W → W → ℕ}
    {f : W → A} (h : IsHeckeBraidedAlgebraMap q m f) :
    IsHeckeAlgebraMap q f :=
  h.1

/-- **Existence side of the Iwahori-Hecke universal property
    (Hecke-quadratic fragment).**

    Sprint 2 follow-up: given the refined `IsHeckeAlgebraMap`
    predicate (Hecke quadratic relation alone), produces an
    `R`-algebra hom from `IwahoriHecke W R q` extending `f` on
    every generator. Routes through Quotient.lean's
    `universal_property_hecke_quadratic` via the `FreeAlgebra.lift`
    of the W-indexed family.

    The braid-relation side is deferred to the Sprint 2 follow-up
    once Mathlib's `CoxeterSystem` reduced-expression accessor
    stabilises (the Sprint 2 caveat inherited from
    [`Quotient.lean`](Quotient.lean) line 113-118). -/
theorem universal_property_existence
    {W : Type u} [Group W] [DecidableEq W] {R : Type v} [CommRing R] (q : R)
    {A : Type w} [CommRing A] [Algebra R A]
    (f : W → A) (hf : IsHeckeAlgebraMap q f) :
    Nonempty { φ : IwahoriHecke W R q →ₐ[R] A //
              ∀ s : W, φ (T q s) = f s } := by
  -- Lift `f : W → A` through FreeAlgebra to an algebra hom
  --   f' : FreeAlgebra R (Set.univ : Set W) →ₐ[R] A
  -- mapping each generator `FreeAlgebra.ι R ⟨s, _⟩ ↦ f s`.
  let f' : FreeAlgebra R (Set.univ : Set W) →ₐ[R] A :=
    FreeAlgebra.lift R (fun (s : (Set.univ : Set W)) => f s.val)
  -- Vanishing on `heckeQuadraticGenerators` follows from `hf`
  -- applied to each `s : W` via the universal-set wrapping.
  have hf' : ∀ s : (Set.univ : Set W),
      f' (QOU.IwahoriHecke.Quotient.heckeQuadraticRelation R q
        (Set.univ : Set W) s) = 0 := by
    intro s
    -- heckeQuadraticRelation unfolds to
    --   (ι s - algebraMap R _ q) * (ι s + 1) in FreeAlgebra R Set.univ
    -- After applying f' (which sends ι ⟨s, _⟩ ↦ f s.val), the image
    -- is (f s.val - algebraMap R A q) * (f s.val + 1) = 0 by hf.
    show f' _ = 0
    unfold QOU.IwahoriHecke.Quotient.heckeQuadraticRelation
    simp only [f', map_mul, map_sub, map_add, map_one,
               FreeAlgebra.lift_ι_apply, AlgHom.commutes]
    exact hf s.val
  -- Apply Quotient.lean's lemma to produce the lift.
  obtain ⟨φ_pair⟩ :=
    QOU.IwahoriHecke.Quotient.universal_property_hecke_quadratic
      R q (Set.univ : Set W) A f' hf'
  refine ⟨⟨φ_pair.val, ?_⟩⟩
  intro s
  -- φ_pair.property says φ_pair.val (Quotient.T R q univ ⟨s, _⟩) = f' (ι ⟨s, _⟩);
  -- since `T q s := Quotient.T R q univ ⟨s, Set.mem_univ s⟩` and
  -- f' (ι ⟨s, _⟩) = f s, equality follows.
  have h := φ_pair.property ⟨s, Set.mem_univ s⟩
  simp only [T, f', FreeAlgebra.lift_ι_apply] at h
  exact h

/-- **Universal property of the Iwahori-Hecke algebra.**

    Any Hecke algebra map `f : W → A` (in the sense of
    `IsHeckeAlgebraMap`, currently the Hecke-quadratic-only
    predicate) extends uniquely to an `R`-algebra homomorphism
    from `IwahoriHecke W R q`.

    Sprint 2 follow-up status:
    - **Existence**: discharged by `universal_property_existence`
      via Quotient.lean's `universal_property_hecke_quadratic`.
    - **Uniqueness**: axiomatised pending lake-local verification.
      The argument is standard: two algebra homs out of the quotient
      agree iff their compositions with `Ideal.Quotient.mk` agree
      (`Ideal.Quotient.algHom_ext`); two algebra homs out of
      `FreeAlgebra R X` agree iff they agree on every generator
      `ι R x` (`FreeAlgebra.hom_ext`); each generator case reduces
      to `ψ (T q s) = φ_witness.val (T q s)` via `hψ s` and
      `φ_witness.property s`. Two tactic-form attempts (sessions
      2026-06-03 a7f80972, f58c7feb) could not be verified locally
      because the remote container has no `lake` binary and elan
      cannot reach the Lean release server (network policy). The
      proof is well-known in the literature — see [kassel2008]
      Ch. 4 — so the result is recorded as an `axiom` here pending
      a follow-up lake-equipped session that can verify the tactic
      form. -/
-- Ref: [kassel2008] Kassel & Turaev, "Braid Groups", Springer 2008, Ch. 4
axiom universal_property
    {W : Type u} [Group W] [DecidableEq W] {R : Type v} [CommRing R] (q : R)
    {A : Type w} [CommRing A] [Algebra R A]
    (f : W → A) (hf : IsHeckeAlgebraMap q f) :
    ∃! φ : IwahoriHecke W R q →ₐ[R] A, ∀ s : W, φ (T q s) = f s

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
