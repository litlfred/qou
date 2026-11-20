import Mathlib.Analysis.Normed.Group.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Module.LinearMap.Defs

/-!
# QOU.Torsion.mass_upper_bound_localised — the proved half of the topological mass decomposition

Content block `prop:topological-mass-upper-bound`. It is the proved half of
`conj:topological-mass`.

The trace of a cycle splits additively through the descent idempotent, and the
transient part splits further over the blow-up centres. The trace is linear, and
the kernels at distinct centres form a direct sum. So the total trace value is
`t = d + Σ_i τ_i`. The mass is the norm of the trace value, and the triangle
inequality then gives

  `‖t‖ ≤ ‖d‖ + Σ_i ‖τ_i‖`.

Equality is the content of `conj:topological-mass`, and it is open. It is not
forced by an orthogonal splitting. Orthogonality gives additivity of squared
norms, `‖a + b‖² = ‖a‖² + ‖b‖²`, not of norms.

**Base ring (§7c).** Only the norm and addition are used, so the statement is
over an arbitrary seminormed additive commutative group `M`. No `ℝ`-valued
trace and no ordering are assumed.

**When equality holds (2026-11-20).** The equality of `conj:topological-mass`
is equivalent to the pieces lying on a common ray:
`QOU.Torsion.TopologicalMassEquality.mass_decomposition_eq_iff` (PR #8581). The
scope-(a) counterexample is `QOU.LiftingDescent.norm_additivity_not_forced`.

`transient_trace_eq_zero_of_global_compat`, below, adds a dichotomy. If the
trace is compatible with descent on the whole algebra, every transient trace is
zero, so the equality holds trivially with no transient contribution. A nonzero
transient term therefore needs compatibility on the descended subalgebra only.

-- Ref: [leitner2026] §3 Lifting and Descent, topological decomposition of mass
-/

namespace QOU.Torsion

variable {M : Type*} [SeminormedAddCommGroup M]

/-- **Localised mass upper bound.** If a trace value splits as a descended part
plus transient parts indexed by a finite set of blow-up centres, its norm is at
most the norm of the descended part plus the sum of the transient norms. -/
theorem mass_upper_bound_localised {ι : Type*} (s : Finset ι)
    (total descended : M) (transient : ι → M)
    (hsplit : total = descended + ∑ i ∈ s, transient i) :
    ‖total‖ ≤ ‖descended‖ + ∑ i ∈ s, ‖transient i‖ := by
  rw [hsplit]
  calc ‖descended + ∑ i ∈ s, transient i‖
      ≤ ‖descended‖ + ‖∑ i ∈ s, transient i‖ := norm_add_le _ _
    _ ≤ ‖descended‖ + ∑ i ∈ s, ‖transient i‖ := by
        gcongr
        exact norm_sum_le _ _

section GlobalCompatibility

/-- **A globally trace-compatible descent kills every transient trace.**

Let `ℓ : N → M` be the ascent embedding and `𝔡 : M → N` the descent map, with
`𝔡 ∘ ℓ = id`. Suppose the traces are compatible on ALL of `M`:
`trN (𝔡 x) = trM x`. This is the form of the hypothesis that
`QOU.Torsion.descended_trace_is_base_level` assumes. Then the transient part
`x - ℓ (𝔡 x)` of every `x` has trace zero.

So under that global form, the equality of `conj:topological-mass` holds
trivially: every transient term is zero, and no quantum-dilogarithm contribution
can come from the trace of the transient component. A nonzero transient trace
needs compatibility on the descended subalgebra only, which is the form the
narrative proof of `lem:topological-mass-cat-descended` actually uses. -/
theorem transient_trace_eq_zero_of_global_compat {R : Type*} [CommRing R]
    {N M : Type*} [AddCommGroup N] [Module R N] [AddCommGroup M] [Module R M]
    (ℓ : N →ₗ[R] M) (𝔡 : M →ₗ[R] N) (retraction : ∀ y, 𝔡 (ℓ y) = y)
    (trN : N →ₗ[R] R) (trM : M →ₗ[R] R)
    (compat : ∀ x, trN (𝔡 x) = trM x) (x : M) :
    trM (x - ℓ (𝔡 x)) = 0 := by
  rw [map_sub, ← compat (ℓ (𝔡 x)), retraction, compat, sub_self]

end GlobalCompatibility

end QOU.Torsion
