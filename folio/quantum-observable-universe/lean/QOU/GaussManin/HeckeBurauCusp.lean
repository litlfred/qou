import Mathlib.Tactic
import QOU.MassTheory.BorromeanWordForcing

/-!
# The Hecke fundamental representation at `q² = −1` is the elliptic monodromy (epic `08a2`, germ route)

Owner ruling 2026-11-28 01:55Z: Φ stays an open hypothesis, and the germ route is the one to try.
This file is the algebraic anchor of that route.

**The representation.** Over a field `K` with `q ≠ 0`, put

  `σ₀ ↦ b₀ = q·[[−q⁻², 1], [0, 1]]`,  `σ₁ ↦ b₁ = q·[[1, 0], [q⁻², −q⁻²]]`,

which is `q` times the reduced Burau representation of `B₃` at `t = q⁻²`. Proved here:

* `b_braid`: `b₀b₁b₀ = b₁b₀b₁` (for `q ≠ 0`);
* `b0_hecke`, `b1_hecke`: `(bᵢ − q)(bᵢ + q⁻¹) = 0`, the corpus's Hecke relation (no hypothesis on `q` is needed: at `q = 0` both sides read `0` in Lean's field convention);
* `b0_at_cusp`, `b1_at_cusp`: if `q² = −1` then `bᵢ = q · burauGen i`, where `burauGen` is the
  integer Burau representation at `t = −1` on `main`, `σ₀ ↦ [[1,1],[0,1]]`,
  `σ₁ ↦ [[1,0],[−1,1]]`. `QOU.Mass.BorromeanWordForcing.KernelProof` shows that this map
  `B₃ → SL(2, ℤ)` is onto, with kernel `⟨Δ⁴⟩`.

**Why this matters for Φ.** `[[1,1],[0,1]]` and `[[1,0],[−1,1]]` are the Picard–Lefschetz
monodromies of `H¹` of the Legendre elliptic family `y² = x(x−1)(x−λ)` around two of its nodes,
i.e. the Gauss–Manin monodromy of the family whose cusp `TateCurveCusp` models. So at `q² = −1`
the Hecke representation *is* the elliptic Gauss–Manin local system, up to the scalar `q`. Here
`q² = −1` is a root-of-unity condition, stated algebraically. It is also the locus where
`[2]_q = 0` (`EmGermMomentVanishing.qInt2_eq_zero_iff`), which matches the fact that this
monodromy is unipotent, not semisimple.

**What is not proved here (germ route, next steps).** Away from `q² = −1`, reduced Burau at
`t = e^{2πiα}` is the monodromy of the rank-2 hypergeometric local system with periods
`∫ ∏(x − zᵢ)^{−α} dx` (Kohno, `library/kohno1987-aif`). At `α = ½` that integrand is `dx/y`, the
period `ω` of M1/M2. So the candidate Φ is the period map of this family: `q` fixes the
exponent, and `τ` is the period ratio over the configuration of branch points. That
identification is analytic and is not formalised. Nothing here gives `GermPeriodShare` an
instance.

-- Ref: [leitner2026] Ch. mass-theory, per-loop measure (R2 / Φ, epic 08a2)
-/

set_option autoImplicit false

namespace QOU.GaussManin
namespace HeckeBurauCusp

open Matrix

variable {K : Type*} [Field K]

/-- `σ₀ ↦ q·[[−q⁻², 1], [0, 1]]`. -/
def b0 (q : K) : Matrix (Fin 2) (Fin 2) K := !![-q⁻¹, q; 0, q]

/-- `σ₁ ↦ q·[[1, 0], [q⁻², −q⁻²]]`. -/
def b1 (q : K) : Matrix (Fin 2) (Fin 2) K := !![q, 0; q⁻¹, -q⁻¹]

theorem b_braid (q : K) (hq : q ≠ 0) : b0 q * b1 q * b0 q = b1 q * b0 q * b1 q := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [b0, b1, Matrix.mul_apply, Fin.sum_univ_two, hq]

theorem b0_hecke (q : K) :
    (b0 q - q • 1) * (b0 q + q⁻¹ • 1) = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [b0, Matrix.mul_apply, Fin.sum_univ_two]
  all_goals ring

theorem b1_hecke (q : K) :
    (b1 q - q • 1) * (b1 q + q⁻¹ • 1) = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [b1, Matrix.mul_apply, Fin.sum_univ_two]
  all_goals ring

open QOU.Mass.BorromeanWordForcing in
/-- The integer Burau image of `σᵢ`, read in `K`. -/
def burauK (i : Fin 2) : Matrix (Fin 2) (Fin 2) K :=
  ((burauGen i : Matrix (Fin 2) (Fin 2) ℤ)).map (Int.castRingHom K)

theorem inv_of_sq_eq_neg_one (q : K) (h : q ^ 2 = -1) : q⁻¹ = -q := by
  exact inv_eq_of_mul_eq_one_right (by linear_combination -h)

/-- At `q² = −1`, `b₀ = q · [[1, 1], [0, 1]]`. -/
theorem b0_at_cusp (q : K) (h : q ^ 2 = -1) : b0 q = q • burauK 0 := by
  have hi := inv_of_sq_eq_neg_one q h
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [b0, burauK, QOU.Mass.BorromeanWordForcing.burauGen, hi]

/-- At `q² = −1`, `b₁ = q · [[1, 0], [−1, 1]]`. -/
theorem b1_at_cusp (q : K) (h : q ^ 2 = -1) : b1 q = q • burauK 1 := by
  have hi := inv_of_sq_eq_neg_one q h
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [b1, burauK, QOU.Mass.BorromeanWordForcing.burauGen, hi]

end HeckeBurauCusp
end QOU.GaussManin
