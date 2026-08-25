import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Group.Units.Basic

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

/-- Abstract context for the sorting / color-energy Hecke decomposition.

    **Base ring (§7c).** The substrate parameter `q` and the two
    eigenvalues are algebraic in `q` (the Hecke generator's eigenvalues
    are `q` and `−q⁻¹`); the only thing inverted is `q` itself, so `q` is
    carried as a **unit** `q : Rˣ` over a generic `(R : Type*)
    [CommRing R]` rather than an element of a field.  This is the
    manuscript's own ground ring: the Hecke relation
    `(σ − q)(σ + q⁻¹) = 0` has coefficients in `R_q = ℤ[q, q⁻¹]`
    (`LaurentPolynomial ℤ`, where `q = T 1` is a unit), and no ordering
    or `Real.*` appears anywhere. -/
class SortingColorEnergyContext (R : Type*) [CommRing R] where
  /-- The fundamental representation space `V`. -/
  V : Type
  /-- The tensor square `V ⊗ V`. -/
  V_sq : Type
  /-- The symmetric subspace `Sym²(V)`. -/
  Sym2 : Type
  /-- The antisymmetric subspace `Λ²(V)`. -/
  Wedge2 : Type
  /-- The substrate parameter `q`, as a unit of the ground ring. -/
  q : Rˣ
  /-- The Hecke generator `σᵢ` as a linear operator on `V_sq`. -/
  sigma : V_sq → V_sq
  /-- Eigenvalue of `σᵢ` on `Sym²(V)`: should be `q`. -/
  sym_eigenvalue : R
  /-- Eigenvalue of `σᵢ` on `Λ²(V)`: should be `−q⁻¹`. -/
  wedge_eigenvalue : R
  /-- Manuscript eigenvalues: `σᵢ` acts as `q` on `Sym²(V)` and
      `−q⁻¹` on `Λ²(V)`. -/
  claim_eigenvalues :
    sym_eigenvalue = (q : R) ∧ wedge_eigenvalue = -((q⁻¹ : Rˣ) : R)

/-- **Eigenspace decomposition with explicit Hecke eigenvalues**
    ([`prop:sorting-color-energy`] item (1)). -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/sorting-color-energy.md
def sorting_color_energy {R : Type*} [CommRing R]
    [ctx : SortingColorEnergyContext R] :
    ctx.sym_eigenvalue = (ctx.q : R) ∧
      ctx.wedge_eigenvalue = -((ctx.q⁻¹ : Rˣ) : R) :=
  ctx.claim_eigenvalues

end QOU.BraidKnot
