---
# qou-ltzf
title: 'GAP: transfer IsSimpleModule across Representation.ofModule / asModule (blocks W1+W3 brick 4c injectivity)'
status: completed
type: task
priority: normal
created_at: 2026-08-15T23:07:27Z
updated_at: 2026-08-15T23:19:12Z
---


## What is blocked

W1+W3 brick 4c: injectivity of the action map
`Φ = Pi.algHom k _ (fun i => (spechtRepAt i.property).asAlgebraHom) :
k[S_n] →ₐ[k] ∏_{μ ⊢ n} End_k(S^μ)`, which would give `n! ≤ Σ_μ (dim S^μ)²` from
`SpechtBlockDimension` (brick 4a). One inequality, not the identity.

## The argument is routine; the plumbing is not

`x ∈ ker Φ` acts as zero on every simple `k[S_n]`-module, because every simple is a Specht
module (`SpechtClassification.specht_exhausts_irreducibles`). `k[S_n]` is semisimple, so
`IsSemisimpleModule.sSup_simples_eq_top` writes it as a sup of simple submodules; hence `x`
acts as zero on `k[S_n]`, and `x = x • 1 = 0`.

## The actual gap

`specht_exhausts_irreducibles` wants `IsSimpleModule (MonoidAlgebra k G) ρ.asModule` for a
`Representation`. A simple submodule `N ≤ k[S_n]` arrives as `IsSimpleModule (MonoidAlgebra k G) ↥N`.
`Representation.ofModule ↥N` supplies a representation, but on
`RestrictScalars k (MonoidAlgebra k G) ↥N`, and **nothing in the pinned Mathlib transfers the
simplicity across that round-trip** — measured, not assumed:

```lean
example (k G : Type) [Field k] [Group G] (M : Type) [AddCommGroup M]
    [Module (MonoidAlgebra k G) M] [IsSimpleModule (MonoidAlgebra k G) M] :
    IsSimpleModule (MonoidAlgebra k G) (Representation.ofModule (k := k) (G := G) M).asModule := by
  exact?   -- `exact?` could not close the goal
```

So the brick needs a hand-built `MonoidAlgebra k G`-linear equivalence
`(ofModule M).asModule ≃ₗ M` (the pieces are `Representation.asModuleEquiv`,
`RestrictScalars.addEquiv`, `Representation.ofModule_asModule_act`), then
`IsSimpleModule.congr` along it. That is the whole cost of 4c.

## Not a blocker for anything already landed

Bricks 1–4b are merged and independent of this. This gap only gates the *inequality*; the
identity `n! = Σ_μ (dim S^μ)²` needs the reverse direction too (isotypic independence), which
is a separate question.

## CLOSED — PR (this branch), sorry-free

`QOU/MathlibExt/OfModuleAsModule.lean`:

- `ofModuleAsModuleEquiv : (ofModule M).asModule ≃ₗ[MonoidAlgebra k G] M`
- `isSimpleModule_ofModule_asModule` — an **instance**, so the transfer happens by typeclass
  inference at the use site rather than by hand at each one.

Every ingredient was already in Mathlib; only the assembly was missing.
`Representation.asModuleEquiv` composed with `RestrictScalars.addEquiv` is the additive
equivalence, and `Representation.smul_ofModule_asModule` is exactly the `k[G]`-linearity
hypothesis `AddEquiv.toLinearEquiv` asks for. Compiled first try.

The `exact?` failure recorded above is kept in the file as a regression-guard `example`, so a
future Mathlib bump that changes the `RestrictScalars` plumbing fails at the source of the gap
instead of at a distant call site.

**Unblocks** W1+W3 brick 4c (injectivity of the Specht action map ⇒ `n! ≤ Σ_μ (dim S^μ)²`).
