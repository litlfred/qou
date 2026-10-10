import QOU.Hecke.IwahoriHecke
import Mathlib.RingTheory.AdjoinRoot
import Mathlib.RingTheory.Ideal.Quotient.Operations

/-!
# QOU.Hecke.IwahoriHeckeRankOne — the uniform family, identified at its smallest rank

`QOU.Hecke.IwahoriHecke` builds `H_{n+1}(q)` for **general `n`** as a `RingQuot`
of a free algebra.  Until this file it was **orphaned**: no other module in the
tree imported it, nothing consumed it, and no declaration anywhere related it to
the concrete rank objects (`H2 R q`, `H3A`, `H4A`) on which the corpus's actual
semisimplicity theorems live.  Those three are three *unrelated carrier types*,
so the proved rank ladder and the uniform family had no point of contact at all.

This file supplies the first one, at the smallest rank.  At `n = 1` the braid and
commutation relations are **vacuous** (`braid` needs `i + 1 < 1` and `commute`
needs `j + 2 ≤ i`, both uninhabited over `Fin 1`), so only the quadratic survives
and the algebra should be `K[X]/(X² - (q-1)X - q)`.  We prove the forward half of
that identification.

## What is proved here (sorry-free, generic `[CommRing K]` per §7c)

* `root_quad` — the `AdjoinRoot` generator satisfies the Hecke quadratic in the
  exact `smul` form the `HeckeRel` constructor uses.
* `fwd` — the algebra map `IwahoriHecke K q 1 →ₐ[K] AdjoinRoot (X²-(q-1)X-q)`.
* `fwd_sigma` — it sends the Hecke generator `σ₀` to `root`, so it is not the
  zero-information map.

## The rank-1 identification, proved

`rankOneEquiv : IwahoriHecke K q 1 ≃ₐ[K] AdjoinRoot (X² - (q-1)X - q)`, together
with `commute_rankOne` — so the rank-1 member of the uniform family **is** `H₂(q)`,
and it is commutative.  Semisimplicity now transports along `rankOneEquiv` from
any `AdjoinRoot`-side statement.

### A retraction worth reading before you trust an API-level "blocked"

The first version of this file stopped at the forward map and recorded the
inverse as **blocked on a Mathlib gap**: `AdjoinRoot.liftHom` requires a
*commutative* target, `IwahoriHecke K q 1` carries only `Ring`, `RingQuot`
inherits `CommRing` solely from a `CommRing` base, and Mathlib has no
`CommRing (FreeAlgebra K (Fin 1))`.  Every one of those statements is **true**,
and the conclusion drawn from them was **wrong**.

`AdjoinRoot.liftHom` is not the only way out of an `AdjoinRoot`.  Mathlib carries
`Polynomial.eval₂AlgHom'`, which evaluates into a **noncommutative** algebra given
only that the scalars commute with the chosen element — supplied here by
`Algebra.commutes` — and `Ideal.Quotient.liftₐ`, which descends it through the
quotient.  Composing the two builds the inverse with no commutativity hypothesis
anywhere.  Commutativity of `IwahoriHecke K q 1` then falls out as a *corollary*
of the isomorphism rather than being a prerequisite for it.

The lesson is the one AGENTS.md states for durable refutations: *"this
construction, via this API, does not go through"* is a scope-(a) negative about a
route.  It is not a structural exclusion, and it must not be written down as one.
No invariant forbade the inverse; only the obvious lemma did not apply.

## What this still does NOT do

**This file does not, and cannot, discharge `WenzlCriterion`.**  The consumer
`QOU.Information.PNeqNpEquivalence.counting_faithfulness_of_one_lt` instantiates
the cited layer's `semisimple` parameter at `(∀ n, ss n)` — *every* rank — and
Jaeger–Vertigan–Welsh genuinely needs unbounded rank, since the `#P`-hard link
family has unboundedly many strands.  No finite collection of proved ranks
entails a `∀ n` statement.  See
`docs/audits/2026-08-29-pneqnp-gap-inventory-refresh.md`.
-/

open Polynomial

namespace QOU.Hecke.IwahoriHecke

variable (K : Type*) [CommRing K] (q : K)

/-- The Hecke quadratic `X² - (q-1)X - q` as a polynomial over `K`. -/
noncomputable def heckePoly : K[X] := X ^ 2 - C (q - 1) * X - C q

/-- **The `AdjoinRoot` generator satisfies the Hecke quadratic (sorry-free).**
    Stated in the `smul` form used by `HeckeRel.quadratic`, so it plugs directly
    into the `RingQuot` lift below. -/
theorem root_quad :
    AdjoinRoot.root (heckePoly K q) * AdjoinRoot.root (heckePoly K q)
      = (q - 1) • AdjoinRoot.root (heckePoly K q)
        + q • (1 : AdjoinRoot (heckePoly K q)) := by
  have h : aeval (AdjoinRoot.root (heckePoly K q)) (heckePoly K q) = 0 := by
    rw [AdjoinRoot.aeval_eq, AdjoinRoot.mk_self]
  simp only [heckePoly, map_sub, map_mul, map_pow, aeval_X, aeval_C] at h
  simp only [heckePoly, Algebra.smul_def, map_sub, map_one] at h ⊢
  linear_combination h

/-- **The rank-1 comparison map (sorry-free).**  `H₂(q) = IwahoriHecke K q 1`
    maps to `K[X]/(X² - (q-1)X - q)`.  The braid and commutation constructors are
    discharged by `omega`: both are uninhabited at `n = 1`. -/
noncomputable def toAdjoinRoot :
    IwahoriHecke K q 1 →ₐ[K] AdjoinRoot (heckePoly K q) :=
  RingQuot.liftAlgHom K
    ⟨FreeAlgebra.lift K (fun _ : Fin 1 => AdjoinRoot.root (heckePoly K q)), by
      rintro x y (⟨i⟩ | ⟨i, hi⟩ | ⟨i, j, h⟩)
      · simp only [map_mul, map_add, map_smul, map_one, FreeAlgebra.lift_ι_apply]
        exact root_quad K q
      · exact absurd hi (by omega)
      · exact absurd h (by omega)⟩

/-- **The comparison map is non-degenerate (sorry-free):** it carries the Hecke
    generator `σ₀` to the adjoined root.  Without this the map above would be
    compatible with being constant. -/
theorem toAdjoinRoot_σ :
    toAdjoinRoot K q (σ K q 1 0) = AdjoinRoot.root (heckePoly K q) :=
  (RingQuot.liftAlgHom_mkAlgHom_apply _ _ _ _).trans (FreeAlgebra.lift_ι_apply _ _)

/-! ### The inverse, and the identification

Built with `Polynomial.eval₂AlgHom'` (noncommutative target) and descended via
`Ideal.Quotient.liftₐ`. -/

/-- Evaluation `K[X] →ₐ[K] H` at the Hecke generator.  Uses the
    **noncommutative-target** eval: the only hypothesis is that scalars commute
    with `σ₀`, which `Algebra.commutes` supplies. -/
noncomputable def evalSigma : K[X] →ₐ[K] IwahoriHecke K q 1 :=
  Polynomial.eval₂AlgHom' (Algebra.ofId K (IwahoriHecke K q 1)) (σ K q 1 0)
    (fun a => Algebra.commutes a (σ K q 1 0))

@[simp] theorem evalSigma_X : evalSigma K q X = σ K q 1 0 := by
  simp [evalSigma]

@[simp] theorem evalSigma_C (a : K) :
    evalSigma K q (C a) = algebraMap K (IwahoriHecke K q 1) a := by
  simp [evalSigma]

/-- **The Hecke quadratic dies in `H` (sorry-free).**  This is what lets the
    evaluation descend through the quotient. -/
theorem evalSigma_heckePoly : evalSigma K q (heckePoly K q) = 0 := by
  rw [heckePoly, map_sub, map_sub, map_mul, map_pow, evalSigma_X, evalSigma_C, evalSigma_C,
      pow_two, σ_quadratic K q 1 0]
  simp only [Algebra.smul_def, map_sub, map_one]
  noncomm_ring

/-- The inverse comparison map, via `Ideal.Quotient.liftₐ`. -/
noncomputable def fromAdjoinRoot :
    AdjoinRoot (heckePoly K q) →ₐ[K] IwahoriHecke K q 1 :=
  Ideal.Quotient.liftₐ _ (evalSigma K q) (by
    intro a ha
    obtain ⟨b, rfl⟩ := Ideal.mem_span_singleton.mp ha
    rw [map_mul, evalSigma_heckePoly, zero_mul])

@[simp] theorem fromAdjoinRoot_root :
    fromAdjoinRoot K q (AdjoinRoot.root (heckePoly K q)) = σ K q 1 0 :=
  evalSigma_X K q

/-- **The rank-1 identification (sorry-free).**  The rank-1 member of the uniform
    Iwahori–Hecke family *is* `H₂(q) = K[X]/(X² - (q-1)X - q)`.  This is the first
    isomorphism in the corpus between the general-`n` family and a concrete rank
    object. -/
noncomputable def rankOneEquiv :
    IwahoriHecke K q 1 ≃ₐ[K] AdjoinRoot (heckePoly K q) :=
  AlgEquiv.ofAlgHom (toAdjoinRoot K q) (fromAdjoinRoot K q)
    (AdjoinRoot.algHom_ext (by
      rw [AlgHom.comp_apply, fromAdjoinRoot_root, toAdjoinRoot_σ]; rfl))
    (RingQuot.ringQuot_ext' K _ _ (FreeAlgebra.hom_ext (funext fun i => by
      fin_cases i
      show fromAdjoinRoot K q (toAdjoinRoot K q (σ K q 1 0)) = σ K q 1 0
      rw [toAdjoinRoot_σ, fromAdjoinRoot_root])))

/-- **`H₂(q)` is commutative (sorry-free)** — a *corollary* of the identification,
    not a prerequisite for it.  This is the statement the first version of this
    file recorded as blocked. -/
theorem commute_rankOne (x y : IwahoriHecke K q 1) : x * y = y * x := by
  apply (rankOneEquiv K q).injective
  simp only [map_mul]
  ring

end QOU.Hecke.IwahoriHecke
