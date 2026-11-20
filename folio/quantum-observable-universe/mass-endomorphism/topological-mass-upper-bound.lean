import Mathlib.Analysis.Normed.Group.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Analysis.Convex.StrictConvexSpace
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

**When equality holds (2026-11-20).** The second half of this file
characterises the equality of `conj:topological-mass` for real normed spaces:
- `mass_eq_of_common_ray`: if the descended part and every transient part are
  nonnegative multiples of one vector, then equality holds. This is sufficient.
- `sameRay_of_mass_eq`: in a strictly convex space, equality forces the
  descended part and the total transient part onto a common ray. This is necessary.
- `mass_eq_iff_sameRay`: the exact two-term statement.
So the conjecture is equivalent to an alignment (common-ray) condition on the
trace values, and that condition is not established in the corpus. The
counterexample showing it is not automatic is already on record:
`QOU.LiftingDescent.norm_additivity_not_forced`.

`transient_trace_eq_zero_of_global_compat` records a dichotomy. If the trace is
compatible with descent on the whole algebra, every transient trace is zero.
Then the equality holds trivially, but with no transient contribution.

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

section Equality

variable {E : Type*}

/-- **Sufficient condition for equality.** If the descended part and every
transient part are nonnegative real multiples of one vector `u`, the localised
mass bound is an equality. -/
theorem mass_eq_of_common_ray [SeminormedAddCommGroup E] [NormedSpace ℝ E]
    {ι : Type*} (s : Finset ι) (total descended u : E) (transient : ι → E)
    (c : ℝ) (cs : ι → ℝ) (hc : 0 ≤ c) (hcs : ∀ i ∈ s, 0 ≤ cs i)
    (hd : descended = c • u) (ht : ∀ i ∈ s, transient i = cs i • u)
    (hsplit : total = descended + ∑ i ∈ s, transient i) :
    ‖total‖ = ‖descended‖ + ∑ i ∈ s, ‖transient i‖ := by
  have hsum : ∑ i ∈ s, transient i = (∑ i ∈ s, cs i) • u := by
    rw [Finset.sum_smul]
    exact Finset.sum_congr rfl ht
  have hnorms : ∑ i ∈ s, ‖transient i‖ = (∑ i ∈ s, cs i) * ‖u‖ := by
    rw [Finset.sum_mul]
    refine Finset.sum_congr rfl fun i hi => ?_
    rw [ht i hi, norm_smul_of_nonneg (hcs i hi)]
  have hsum_nonneg : 0 ≤ ∑ i ∈ s, cs i := Finset.sum_nonneg hcs
  rw [hsplit, hsum, hd, ← add_smul, norm_smul_of_nonneg (add_nonneg hc hsum_nonneg),
    norm_smul_of_nonneg hc, hnorms]
  ring

/-- **Two-term characterisation.** In a strictly convex real normed space, the
mass of `descended + transient` is the sum of the two norms exactly when the two
lie on a common ray. -/
theorem mass_eq_iff_sameRay [NormedAddCommGroup E] [NormedSpace ℝ E]
    [StrictConvexSpace ℝ E] (total descended transient : E)
    (hsplit : total = descended + transient) :
    ‖total‖ = ‖descended‖ + ‖transient‖ ↔ SameRay ℝ descended transient := by
  rw [hsplit]
  exact sameRay_iff_norm_add.symm

/-- **Necessary condition for equality.** In a strictly convex real normed
space, equality in the localised mass bound forces the descended part and the
total transient part `∑ i ∈ s, transient i` onto a common ray. -/
theorem sameRay_of_mass_eq [NormedAddCommGroup E] [NormedSpace ℝ E]
    [StrictConvexSpace ℝ E] {ι : Type*} (s : Finset ι)
    (total descended : E) (transient : ι → E)
    (hsplit : total = descended + ∑ i ∈ s, transient i)
    (heq : ‖total‖ = ‖descended‖ + ∑ i ∈ s, ‖transient i‖) :
    SameRay ℝ descended (∑ i ∈ s, transient i) := by
  rw [sameRay_iff_norm_add]
  have h1 : ‖descended + ∑ i ∈ s, transient i‖
      ≤ ‖descended‖ + ‖∑ i ∈ s, transient i‖ := norm_add_le _ _
  have h2 : ‖∑ i ∈ s, transient i‖ ≤ ∑ i ∈ s, ‖transient i‖ := norm_sum_le _ _
  rw [hsplit] at heq
  linarith

end Equality

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
