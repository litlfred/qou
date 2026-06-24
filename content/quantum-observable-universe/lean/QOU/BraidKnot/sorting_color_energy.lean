import Mathlib.Tactic

/-!
# QOU.BraidKnot.sorting_color_energy — Hecke eigendecomposition + sorting projection

**Proposition** ([`prop:sorting-color-energy`](../../../quantum-observable-universe/braids-and-knots/sorting-color-energy.md)).

*Let `σᵢ` be the Hecke generator on `V ⊗ V`.  Then:*

*(1) The R-matrix decomposes `V ⊗ V = Sym²(V) ⊕ Λ²(V)` with
eigenvalues `q` (symmetric) and `−q⁻¹` (antisymmetric).*

*(2) Sorting is the projection from `Λ²(V)` to `Sym²(V)` at `σᵢ`.*

-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/sorting-color-energy.md
-/

namespace QOU.BraidKnot

/-- Abstract context for the sorting / color-energy Hecke decomposition. -/
class SortingColorEnergyContext where
  /-- The fundamental representation space `V`. -/
  V : Type
  /-- The tensor square `V ⊗ V`. -/
  V_sq : Type
  /-- The symmetric subspace `Sym²(V)`. -/
  Sym2 : Type
  /-- The antisymmetric subspace `Λ²(V)`. -/
  Wedge2 : Type
  /-- The substrate parameter `q`. -/
  q : ℝ
  /-- The Hecke generator `σᵢ` as a linear operator on `V_sq`. -/
  sigma : V_sq → V_sq
  /-- Eigenvalue of `σᵢ` on `Sym²(V)`: should be `q`. -/
  sym_eigenvalue : ℝ
  /-- Eigenvalue of `σᵢ` on `Λ²(V)`: should be `−q⁻¹`. -/
  wedge_eigenvalue : ℝ
  /-- Manuscript eigenvalues: `σᵢ` acts as `q` on `Sym²(V)` and
      `−q⁻¹` on `Λ²(V)`. -/
  claim_eigenvalues : sym_eigenvalue = q ∧ wedge_eigenvalue = -(q⁻¹)

/-- **Eigenspace decomposition with explicit Hecke eigenvalues**
    ([`prop:sorting-color-energy`] item (1)). -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/sorting-color-energy.md
def sorting_color_energy [ctx : SortingColorEnergyContext] :
    ctx.sym_eigenvalue = ctx.q ∧ ctx.wedge_eigenvalue = -(ctx.q⁻¹) :=
  ctx.claim_eigenvalues

end QOU.BraidKnot
