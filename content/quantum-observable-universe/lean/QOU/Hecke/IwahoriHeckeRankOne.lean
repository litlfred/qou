import QOU.Hecke.IwahoriHecke
import Mathlib.RingTheory.AdjoinRoot

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

## What is NOT proved, and exactly why (do not mistake this for the iso)

`fwd` is **not** shown to be an isomorphism, and the missing direction is blocked
on a **named Mathlib gap**, not on effort:

> `AdjoinRoot.liftHom` requires its target to be **commutative**.
> `IwahoriHecke K q 1` carries only `Ring`.  `RingQuot` inherits `CommRing`
> solely from a `CommRing` base (`Mathlib/Algebra/RingQuot.lean:362`), and
> Mathlib has **no** `CommRing (FreeAlgebra K (Fin 1))` — no instance, and no
> `FreeAlgebra K (Fin 1) ≃ₐ[K] K[X]` to transport one along.

So the inverse cannot be built until someone supplies commutativity of the free
algebra on a one-element generating set.  That is a small, self-contained,
independently-worthwhile Mathlib contribution — and it is a *far* better
specified gap than "the `T_w` basis".

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

end QOU.Hecke.IwahoriHecke
