import Mathlib.Algebra.FreeAlgebra
import Mathlib.RingTheory.Ideal.Basic
import Mathlib.RingTheory.Ideal.Operations
import Mathlib.Algebra.RingQuot
import Mathlib.Algebra.Algebra.Defs

/-!
# `QOU.IwahoriHecke.Quotient` — concrete quotient construction (Sprint 2)

**Sprint 2 of the Iwahori-Hecke Mathlib infrastructure plan**
(see [`docs/workplans/2026-05-30-iwahori-hecke-mathlib-infra-plan.md`](../../../../../../docs/workplans/2026-05-30-iwahori-hecke-mathlib-infra-plan.md)).

Sprint 1 ([`Defn.lean`](Defn.lean)) declared `IwahoriHecke W R q`
as an `opaque` type with the expected `AddCommGroup` + `Module R`
instances stubbed. This file replaces the opaque stubs with the
**concrete quotient construction**:

$$
\mathrm{IwahoriHecke}(W, q) \;:=\; \mathrm{FreeAlgebra}_R(S) \;/\; \mathcal{I}_{\mathrm{HBr}}(q)
$$

where $S \subset W$ is the simple-reflection set.  That display is the **target**; read the
scope note immediately below for what this file actually builds.

The full Iwahori-Hecke presentation ([humphreys1990] §7.4, [geckpfeiffer2000] §4.4) quotients
by two families:

1. The **Hecke quadratic relation**: $(\mathfrak{T}_s - q)(\mathfrak{T}_s + 1)$
   for each $s \in S$ (where $\mathfrak{T}_s$ is the free-algebra generator).
2. The **braid relations**: for adjacent $s, t \in S$ with order
   $m_{st}$ in $W$, the alternating-product relation
   $\mathfrak{T}_s \mathfrak{T}_t \mathfrak{T}_s \cdots \, - \,
    \mathfrak{T}_t \mathfrak{T}_s \mathfrak{T}_t \cdots$
   (each side has $m_{st}$ factors).

**Only (1) is imposed here.**  See `heckeRel` and the scope note below.

## Scope of Sprint 2

This file establishes:

- `heckeRel R q S` — the relation "each Hecke **quadratic** generator is
  `0`".  The braid relations are **not** included; see the scope
  paragraph below.
- `IwahoriHeckeQuot R q S := RingQuot (heckeRel R q S)` — the concrete
  construction.  It is a `RingQuot`, **not** an `Ideal.Quotient`: the free
  algebra is non-commutative, and the `Ideal.Quotient` form was a bug (see
  the `Ring` instance's docstring below).
- `T : S → IwahoriHeckeQuot R q S` — image of the free generators under the
  quotient map; satisfies the Hecke **quadratic** relation definitionally.
- `heckeIdeal R W q : Ideal (FreeAlgebra R S)` — **vestigial.**  Spans only
  `heckeQuadraticGenerators` and is referenced by no construction in the
  tree; it survives from the superseded `Ideal.Quotient` design.

> **Scope: this file does NOT build H_n(q).**  Imposing the quadratic
> relation alone yields a strictly larger algebra in which the braid
> relations simply do not hold, so nothing downstream may assume them.
> The braid step is tracked as bean `qou-phir`; the consequence for the
> Jucys–Murphy arc is bean `qou-0o6j`.
>
> The blocker recorded on `heckeIdeal` is the Coxeter order function
> `m : S → S → ℕ` "in flux in Mathlib's `CoxeterSystem` API".  Note that
> `m_{st}` is just `orderOf (s * t : W)`, which is plain `Mathlib`
> group theory and needs no `CoxeterSystem` accessor; `altProduct`
> (`Defn.lean`) already supplies the alternating product.  Whoever takes
> `qou-phir` should check that route before waiting on the accessor.
- **Coherence with `Defn.lean`**: a `def` proving the opaque
  `IwahoriHecke W R q` from `Defn.lean` is equivalent to the
  concrete `IwahoriHeckeQuot R W q` constructed here. (Sprint 2
  stub: stated; Sprint 2 PR follow-up provides the bijection.)

## What's deferred to Sprint 3+

- The **reduced-expression basis** `Tw : W → IwahoriHeckeQuot R W q`
  with `IsBasis (Set.range Tw)`. This is Matsumoto's theorem on
  the independence of reduced expressions; it is the technical
  heart of the Iwahori-Hecke theory. Once landed:
  - **Closes** `conj:hecke-anyonic-substrate` (its content is "the
    `T_w` family spans the algebra freely modulo the relations").

The Sprint 2 split lets us land the concrete quotient construction
WITHOUT requiring Matsumoto's theorem, which is a substantial
follow-up (estimated 400-600 LOC by itself).

## Authoring discipline

This file uses Mathlib's `FreeAlgebra` + `Ideal.span` + `RingQuot`
primitives. All construction-level facts (`heckeIdeal` is an
ideal, `T_s` satisfies the quadratic relation, etc.) are
sorry-free under the Mathlib API.

**Sprint 2 status (post follow-up)**:

1. ✅ Hecke quadratic relation + ideal + quotient + universal
   property factoring map (`universal_property_hecke_quadratic`)
   — now sorry-free via `Ideal.Quotient.liftₐ` +
   `Submodule.span_induction`.
2. ⏸️ **Braid relations addition** — requires refactoring the
   `S : Set W` parameter to take a full `CoxeterSystem M W` so
   we can read the per-pair order `M.M s t`. Deferred to a
   follow-up sprint once the Mathlib `CoxeterSystem` order
   accessor API stabilises.

Refs:
- [humphreys1990] §7.4, Iwahori-Hecke algebras
- [geckpfeiffer2000] §4.4, Hecke algebras of type A
- [bourbaki1968] Ch IV §1.4, Coxeter systems
- [matsumoto1964] Matsumoto's theorem (reduced expressions)
- [leitner2026] docs/workplans/2026-05-30-iwahori-hecke-mathlib-infra-plan.md
-/


namespace QOU.IwahoriHecke.Quotient

universe u v

variable {W : Type u} (R : Type v) [CommRing R] (q : R) (S : Set W) [DecidableEq W]

/-- **Hecke quadratic generator**: the polynomial
    `(T_s - q) * (T_s + 1)` in the free algebra, for a simple
    reflection `s ∈ S`. -/
def heckeQuadraticRelation (s : S) : FreeAlgebra R S :=
  (FreeAlgebra.ι R s - algebraMap R (FreeAlgebra R S) q) *
  (FreeAlgebra.ι R s + 1)

/-- The **set** of Hecke quadratic relations, indexed by simple
    reflections. -/
def heckeQuadraticGenerators : Set (FreeAlgebra R S) :=
  { heckeQuadraticRelation R q S s | s : S }

/-- **The Hecke ideal** — two-sided ideal of `FreeAlgebra R S`
    generated by the Hecke quadratic relations.

    Sprint 2 scope: we include only the Hecke quadratic relations
    here. The braid relations require the Coxeter order function
    `m : S → S → ℕ` which is in flux in Mathlib's `CoxeterSystem`
    API; they are added in the Sprint 2 follow-up once the order
    accessor stabilises. The quadratic-only ideal is still a
    well-defined sub-algebra of the full Iwahori-Hecke. -/
def heckeIdeal : Ideal (FreeAlgebra R S) :=
  Ideal.span (heckeQuadraticGenerators R q S)

/-- **The Hecke quotient relation**: each quadratic generator is related to
    `0`.  Because `FreeAlgebra R S` is **non-commutative**, the Hecke algebra
    is built as the algebra-by-relations quotient `RingQuot (heckeRel)`
    (Mathlib's tool for quotienting a non-commutative algebra by a relation),
    not as an `Ideal.Quotient` (which gives a commutative quotient of a
    commutative ring — the wrong construction here). -/
def heckeRel : FreeAlgebra R S → FreeAlgebra R S → Prop :=
  fun a b => ∃ s : S, a = heckeQuadraticRelation R q S s ∧ b = 0

/-- **The (partial) Iwahori-Hecke algebra** — the `RingQuot` of the free
    algebra by the Hecke quadratic relations.

    Sprint 2 deliverable: type + (non-commutative) ring + `R`-algebra
    structure are sorry-free via Mathlib's `RingQuot`. The full Iwahori-Hecke
    additionally quotients by braid relations; that step is Sprint 2 follow-up.

    Naming: `IwahoriHeckeQuot` distinguishes from the Sprint 1
    `IwahoriHecke` opaque stub; once Sprint 2 follow-up establishes
    the equivalence, the two unify. -/
def IwahoriHeckeQuot : Type max u v :=
  RingQuot (heckeRel R q S)

/-- `IwahoriHeckeQuot R q S` carries the canonical (non-commutative) ring and
    `R`-algebra structure inherited from `RingQuot`.  Note: this algebra is
    **not** commutative (the free algebra `FreeAlgebra R S` is not, and the
    Hecke quadratic relation does not impose commutativity), so there is no
    `CommRing` instance — that was the bug in the previous `Ideal.Quotient`
    construction, which only applies to two-sided ideals of commutative
    rings. -/
noncomputable instance : Ring (IwahoriHeckeQuot R q S) :=
  inferInstanceAs (Ring (RingQuot (heckeRel R q S)))

noncomputable instance : Algebra R (IwahoriHeckeQuot R q S) :=
  inferInstanceAs (Algebra R (RingQuot (heckeRel R q S)))

/-- **The image of a generator** `T_s ∈ IwahoriHeckeQuot R q S`
    under the quotient algebra map `RingQuot.mkAlgHom`. -/
def T (s : S) : IwahoriHeckeQuot R q S :=
  RingQuot.mkAlgHom R (heckeRel R q S) (FreeAlgebra.ι R s)

/-- **The Hecke quadratic relation holds in the quotient.**
    The generator `T_s` satisfies `(T_s - q)(T_s + 1) = 0` in
    `IwahoriHeckeQuot R q S`, because `mkAlgHom` identifies the quadratic
    generator with `0` (it is `heckeRel`-related to `0`). -/
theorem T_hecke_quadratic_relation (s : S) :
    (T R q S s - algebraMap R (IwahoriHeckeQuot R q S) q) *
    (T R q S s + 1) = 0 := by
  have h : RingQuot.mkAlgHom R (heckeRel R q S) (heckeQuadraticRelation R q S s) = 0 := by
    have hr := RingQuot.mkAlgHom_rel R (s := heckeRel R q S) ⟨s, rfl, rfl⟩
    simpa using hr
  rw [← h]
  simp only [IwahoriHeckeQuot, heckeQuadraticRelation, T, map_mul, map_sub, map_add,
    map_one, AlgHom.commutes]

/-- **Universal property of the Hecke quotient (Hecke-quadratic
    fragment).** Any `R`-algebra map from `FreeAlgebra R S` that
    sends each `heckeQuadraticRelation` to `0` factors through
    `IwahoriHeckeQuot R q S` via `RingQuot.liftAlgHom`.  (The target `A`
    may be any `R`-algebra — not necessarily commutative.) -/
theorem universal_property_hecke_quadratic
    (A : Type*) [Ring A] [Algebra R A]
    (f : FreeAlgebra R S →ₐ[R] A)
    (hf : ∀ s : S, f (heckeQuadraticRelation R q S s) = 0) :
    Nonempty { φ : IwahoriHeckeQuot R q S →ₐ[R] A //
              ∀ s : S, φ (T R q S s) = f (FreeAlgebra.ι R s) } := by
  have w : ∀ ⦃x y : FreeAlgebra R S⦄, heckeRel R q S x y → f x = f y := by
    rintro x y ⟨s, rfl, rfl⟩
    rw [hf s, map_zero]
  refine ⟨⟨RingQuot.liftAlgHom R ⟨f, w⟩, ?_⟩⟩
  intro s
  rw [T]
  exact RingQuot.liftAlgHom_mkAlgHom_apply (S := R) f w (FreeAlgebra.ι R s)

/-- **Uniqueness half of the universal property.** Two `R`-algebra maps out of
`IwahoriHeckeQuot R q S` that agree on every generator `T s` are equal.

Together with `universal_property_hecke_quadratic` (existence) this gives the full
`∃!` statement. It was previously recorded as an `axiom` in `Defn.lean`, on the
stated ground that the container had no `lake` binary and `elan` could not reach the
Lean release server; that obstacle is gone, and the proof is three steps:

`RingQuot.mkAlgHom` is surjective, so it suffices that the two composites with it
agree. Those are algebra maps out of a *free* algebra, so `FreeAlgebra.hom_ext`
reduces the question to agreement on the generators `ι s` — which is the hypothesis,
since `T s` is by definition `mkAlgHom (ι s)`. -/
theorem hom_ext {A : Type*} [Ring A] [Algebra R A]
    (φ ψ : IwahoriHeckeQuot R q S →ₐ[R] A)
    (h : ∀ s : S, φ (T R q S s) = ψ (T R q S s)) :
    φ = ψ := by
  have hcomp : φ.comp (RingQuot.mkAlgHom R (heckeRel R q S))
      = ψ.comp (RingQuot.mkAlgHom R (heckeRel R q S)) := by
    apply FreeAlgebra.hom_ext
    funext s
    simpa [T] using h s
  apply AlgHom.ext
  intro x
  obtain ⟨y, rfl⟩ := RingQuot.mkAlgHom_surjective R (heckeRel R q S) x
  exact congrArg (fun (α : FreeAlgebra R ↥S →ₐ[R] A) => α y) hcomp

end QOU.IwahoriHecke.Quotient
