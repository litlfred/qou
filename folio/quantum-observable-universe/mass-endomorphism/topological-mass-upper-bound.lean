import Mathlib.Analysis.Normed.Group.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

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

end QOU.Torsion
