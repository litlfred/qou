import Mathlib.LinearAlgebra.Lagrange

/-!
# QOU.Mathlib.LagrangeCoeffSum — coefficient extraction as a sum over interpolation nodes

Two facts about Lagrange interpolation that Mathlib states only implicitly.

| | |
|---|---|
| `coeff_lagrangeBasis` | the top coefficient of `Lagrange.basis s v i` is `∏_{j ≠ i} (v i − v j)⁻¹` |
| `sum_eval_div_prod_eq_coeff` | for `deg f < |s|`, `∑_i f(v i) / ∏_{j≠i}(v i − v j) = f.coeff (|s| − 1)` |

The second is the algebraic form of "the sum of the residues of `f/∏(X − v j)` over its poles reads
off the top coefficient of `f`".  It is the workhorse: with a well-chosen `f` it turns a sum of
products over nodes into a single coefficient.

## Base ring (§7c)

Generic `[Field F]` — Mathlib's `Lagrange` API needs the inverses.  No ordering, no `ℝ`.

LaTeX label: `lem:lagrange-coeff-sum`
-/

namespace QOU.Mathlib

open Polynomial Finset

variable {F : Type*} [Field F] {ι : Type*} [DecidableEq ι]

/-- The top coefficient of a Lagrange basis polynomial. -/
theorem coeff_lagrangeBasis {s : Finset ι} {v : ι → F} {i : ι}
    (hv : Set.InjOn v s) (hi : i ∈ s) :
    (Lagrange.basis s v i).coeff (s.card - 1) = ∏ j ∈ s.erase i, (v i - v j)⁻¹ := by
  rw [← Lagrange.natDegree_basis hv hi, Polynomial.coeff_natDegree, Lagrange.basis,
    Polynomial.leadingCoeff_prod]
  refine Finset.prod_congr rfl fun j _ => ?_
  rw [Lagrange.basisDivisor, Polynomial.leadingCoeff_mul, Polynomial.leadingCoeff_C,
    Polynomial.leadingCoeff_X_sub_C, mul_one]

/-- **Coefficient extraction as a node sum.**

For a polynomial of degree less than the number of nodes,

`∑_{i ∈ s} f(v i) / ∏_{j ∈ s \ {i}} (v i − v j) = f.coeff (|s| − 1)`.

Proof: `f` equals its own Lagrange interpolant, and the top coefficient of the `i`-th basis
polynomial is `∏_{j ≠ i}(v i − v j)⁻¹`. -/
theorem sum_eval_div_prod_eq_coeff {s : Finset ι} {v : ι → F} (hv : Set.InjOn v s)
    {f : F[X]} (hdeg : f.degree < s.card) :
    ∑ i ∈ s, eval (v i) f / ∏ j ∈ s.erase i, (v i - v j) = f.coeff (s.card - 1) := by
  conv_rhs => rw [Lagrange.eq_interpolate hv hdeg]
  rw [Lagrange.interpolate_apply, Polynomial.finset_sum_coeff]
  refine Finset.sum_congr rfl fun i hi => ?_
  rw [Polynomial.coeff_C_mul, coeff_lagrangeBasis hv hi, Finset.prod_inv_distrib,
    ← div_eq_mul_inv]

end QOU.Mathlib
