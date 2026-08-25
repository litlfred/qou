import Mathlib.RepresentationTheory.Basic
import Mathlib.RingTheory.SimpleModule.Basic

/-!
# QOU.MathlibExt.OfModuleAsModule — the `ofModule` / `asModule` round-trip

Closes bean `qou-ltzf`.

Mathlib turns a `k[G]`-module `M` into a representation (`Representation.ofModule M`, on the
type synonym `RestrictScalars k (MonoidAlgebra k G) M`) and a representation back into a
`k[G]`-module (`Representation.asModule`). What it does **not** provide at this pin is the
round-trip: that `(ofModule M).asModule` is `M` *as a `k[G]`-module*. Measured, not assumed —
`exact?` cannot close

```lean
example [IsSimpleModule (MonoidAlgebra k G) M] :
    IsSimpleModule (MonoidAlgebra k G) (Representation.ofModule (k := k) (G := G) M).asModule
```

The ingredients are all there; only the assembly is missing. `Representation.asModuleEquiv`
and `RestrictScalars.addEquiv` compose to an additive equivalence
`(ofModule M).asModule ≃+ M`, and `Representation.smul_ofModule_asModule` says that composite
is `k[G]`-linear — which is exactly the hypothesis `AddEquiv.toLinearEquiv` wants.

## Why it is wanted

Any argument that takes a simple submodule of `k[G]` and feeds it to a theorem stated about
representations needs this. Concretely it is what stands between the covariance-kernel epic's
W1+W3 bricks and the injectivity of the Specht action map
`k[S_n] →ₐ[k] ∏_μ End_k(S^μ)`: simple submodules of `k[S_n]` arrive as
`IsSimpleModule (MonoidAlgebra k G) ↥N`, while
`SpechtClassification.specht_exhausts_irreducibles` wants `IsSimpleModule … ρ.asModule`.

## Base ring (§7c)

Generic: `[CommSemiring k]` / `[Monoid G]` for the equivalence, strengthened to
`[Ring]`-level typeclasses only where `IsSimpleModule` requires them. No `ℝ`, no ordering.
-/

namespace QOU.MathlibExt.OfModuleAsModule

open Representation

variable {k G : Type*} [CommSemiring k] [Monoid G]

/-- **The `ofModule` / `asModule` round-trip is the identity, `k[G]`-linearly.**

`(ofModule M).asModule ≃ₗ[k[G]] M`. The underlying additive equivalence is
`asModuleEquiv` followed by `RestrictScalars.addEquiv`; `smul_ofModule_asModule` supplies the
`k[G]`-linearity. -/
noncomputable def ofModuleAsModuleEquiv (M : Type*) [AddCommMonoid M]
    [Module (MonoidAlgebra k G) M] :
    (ofModule (k := k) (G := G) M).asModule ≃ₗ[MonoidAlgebra k G] M :=
  AddEquiv.toLinearEquiv
    (((ofModule (k := k) (G := G) M).asModuleEquiv.toAddEquiv).trans
      (RestrictScalars.addEquiv k (MonoidAlgebra k G) M))
    (fun r m => smul_ofModule_asModule M r m)

/-- **Simplicity transfers across the round-trip.**

If `M` is a simple `k[G]`-module then so is `(ofModule M).asModule` — which is the form every
`Representation`-stated theorem asks for. Stated as an `instance` so that
`specht_exhausts_irreducibles`-shaped hypotheses are discharged by typeclass inference at the
use site. -/
instance isSimpleModule_ofModule_asModule {k G : Type*} [Field k] [Group G] (M : Type*)
    [AddCommGroup M] [Module (MonoidAlgebra k G) M]
    [IsSimpleModule (MonoidAlgebra k G) M] :
    IsSimpleModule (MonoidAlgebra k G) (ofModule (k := k) (G := G) M).asModule :=
  IsSimpleModule.congr (ofModuleAsModuleEquiv (k := k) (G := G) M)

/-- Regression guard: the goal that `exact?` could not close before this file existed is now
discharged by instance search alone. Kept as an `example` so a future Mathlib bump that changes
the `RestrictScalars` plumbing fails here, at the source of the gap, rather than at a distant
call site. -/
example (k G : Type) [Field k] [Group G] (M : Type) [AddCommGroup M]
    [Module (MonoidAlgebra k G) M] [IsSimpleModule (MonoidAlgebra k G) M] :
    IsSimpleModule (MonoidAlgebra k G) (ofModule (k := k) (G := G) M).asModule :=
  inferInstance

end QOU.MathlibExt.OfModuleAsModule
