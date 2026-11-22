/-
  Geometric depletion of vortex stretching — the pointwise algebraic core.

  Ref: [manuscript] docs/audits/2026-10-12-ns-v1-geometric-depletion.md
       (bean qou-fm7s). Literature, not held in `library/`:
       P. Constantin, C. Fefferman, "Direction of vorticity and the problem of
       global regularity for the Navier–Stokes equations", Indiana Univ. Math.
       J. 42 (1993) 775–789; P. Constantin, "Geometric statistics in
       turbulence", SIAM Review 36 (1994) 73–98.

  ## What is proved here, and what is NOT

  For 3D incompressible Navier–Stokes with vorticity `ω` and direction field
  `ξ = ω/|ω|`, the stretching rate `α(x) = ξ·Sξ` has the singular-integral
  representation (Constantin 1994)

      α(x) = (3/4π) P.V. ∫ D(ŷ, ξ(x), ξ(x+y)) |ω(x+y)| dy / |y|³,
      D(e₁, e₂, e₃) = (e₁·e₃) · det(e₁, e₂, e₃).

  This file proves only the **pointwise algebra of the kernel `D`**. It does
  NOT state the representation formula, the Constantin–Fefferman theorem, or
  any PDE statement. No such statement is introduced as an axiom, a class, or
  a carrier. The PDE theorem is cited, not formalized.

  The results:

  * `depletionKernel_self`, `depletionKernel_neg_self` — `D(e₁, e₂, ±e₂) = 0`:
    aligned (or anti-aligned) vorticity contributes nothing to stretching.
  * `depletionKernel_neg_third` — `D` is even in `e₃`, so the kernel sees only
    the **line field** `[ξ(x+y)]`, not the orientation of `ξ(x+y)`.
  * `depletionKernel_neg_neg` — flipping `ξ` globally reverses `D`, as it must,
    because `u ↦ -u` reverses `α`.
  * `triple_sub_second` — `det(e₁, e₂, e₃) = det(e₁, e₂, e₃ − e₂)`.
  * `depletionKernel_sq_le` — the homogeneous Lipschitz-type bound
    `D² ≤ |e₁|⁴ |e₂|² |e₃|² |e₃ − e₂|²`, all norms Euclidean, written as dot
    products so that it holds over any ordered field.
  * `depletionKernel_sq_le_cross_unit` — the sharp unit-vector form:
    `D² ≤ |e₂ × e₃|² = sin²∠(e₂, e₃)`.
  * `depletionKernel_sq_le_unit_sub` / `_add` — for unit vectors,
    `D² ≤ |e₃ − e₂|²` and `D² ≤ |e₃ + e₂|²`.
  * `abs_depletionKernel_le_unit` (over `ℝ`) — `|D| ≤ min(‖e₃ − e₂‖, ‖e₃ + e₂‖)`
    with the Euclidean norm `√(v·v)`.

  Every lemma here is falsifiable. For example, `D(e₁, e₂, e₃) = 0` fails for
  `e₁ = (1,1,1)/√3`, `e₂ = (1,0,0)`, `e₃ = (0,1,0)`, where `D = 1/3`.

  Base ring (§7c): the identities hold over `[CommRing R]` and the bounds over an
  ordered field. Only the square-root form is stated over `ℝ`.
-/
import Mathlib.LinearAlgebra.CrossProduct
import Mathlib.Data.Real.Sqrt

namespace QOU.FluidDynamics.GeometricDepletion

open Matrix

section Algebra

variable {R : Type*} [CommRing R]

/-- The scalar triple product `det(e₁, e₂, e₃) = e₁ · (e₂ × e₃)`. -/
def triple (e₁ e₂ e₃ : Fin 3 → R) : R := e₁ ⬝ᵥ (e₂ ⨯₃ e₃)

/-- Constantin's geometric kernel `D(e₁, e₂, e₃) = (e₁·e₃) · det(e₁, e₂, e₃)`. -/
def depletionKernel (e₁ e₂ e₃ : Fin 3 → R) : R := (e₁ ⬝ᵥ e₃) * triple e₁ e₂ e₃

theorem triple_eq_det (e₁ e₂ e₃ : Fin 3 → R) :
    triple e₁ e₂ e₃ = Matrix.det ![e₁, e₂, e₃] :=
  triple_product_eq_det e₁ e₂ e₃

/-- Aligned directions: `D(e₁, e₂, e₂) = 0`. -/
theorem depletionKernel_self (e₁ e₂ : Fin 3 → R) : depletionKernel e₁ e₂ e₂ = 0 := by
  simp [depletionKernel, triple, cross_self]

/-- Anti-aligned directions: `D(e₁, e₂, -e₂) = 0`. -/
theorem depletionKernel_neg_self (e₁ e₂ : Fin 3 → R) :
    depletionKernel e₁ e₂ (-e₂) = 0 := by
  simp [depletionKernel, triple, cross_self]

/-- `D` is even in its third slot. The kernel sees only the line `[ξ(x+y)]`. -/
theorem depletionKernel_neg_third (e₁ e₂ e₃ : Fin 3 → R) :
    depletionKernel e₁ e₂ (-e₃) = depletionKernel e₁ e₂ e₃ := by
  simp only [depletionKernel, triple, map_neg, dotProduct_neg]; ring

/-- A global sign flip of the direction field **reverses** `D`. This matches the
PDE: `ω ↦ -ω` is `u ↦ -u`, which reverses the strain `S` and with it the
stretching rate `α = ξ·Sξ`. The sign belongs to the flow, not to the line field. -/
theorem depletionKernel_neg_neg (e₁ e₂ e₃ : Fin 3 → R) :
    depletionKernel e₁ (-e₂) (-e₃) = -depletionKernel e₁ e₂ e₃ := by
  simp only [depletionKernel, triple, map_neg, LinearMap.neg_apply, neg_neg,
    dotProduct_neg]; ring

/-- `det(e₁, e₂, e₃) = det(e₁, e₂, e₃ - e₂)`. -/
theorem triple_sub_second (e₁ e₂ e₃ : Fin 3 → R) :
    triple e₁ e₂ e₃ = triple e₁ e₂ (e₃ - e₂) := by
  simp [triple, map_sub, cross_self]

/-- Lagrange's identity: `|b × c|² = |b|²|c|² - (b·c)²`. -/
theorem cross_dot_self (b c : Fin 3 → R) :
    (b ⨯₃ c) ⬝ᵥ (b ⨯₃ c) = (b ⬝ᵥ b) * (c ⬝ᵥ c) - (b ⬝ᵥ c) ^ 2 := by
  rw [cross_dot_cross, dotProduct_comm c b]; ring

end Algebra

section Bounds

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

theorem dot_self_nonneg (v : Fin 3 → R) : 0 ≤ v ⬝ᵥ v := by
  simp only [dotProduct, Fin.sum_univ_three]
  nlinarith [mul_self_nonneg (v 0), mul_self_nonneg (v 1), mul_self_nonneg (v 2)]

/-- Cauchy–Schwarz for the dot product on `Fin 3 → R`. -/
theorem dot_sq_le (a b : Fin 3 → R) : (a ⬝ᵥ b) ^ 2 ≤ (a ⬝ᵥ a) * (b ⬝ᵥ b) := by
  have h := dot_self_nonneg (a ⨯₃ b)
  rw [cross_dot_self] at h
  linarith

/-- `det(e₁, e₂, e₃)² ≤ |e₁|² |e₂ × e₃|²`. -/
theorem triple_sq_le (e₁ e₂ e₃ : Fin 3 → R) :
    triple e₁ e₂ e₃ ^ 2 ≤ (e₁ ⬝ᵥ e₁) * ((e₂ ⨯₃ e₃) ⬝ᵥ (e₂ ⨯₃ e₃)) :=
  dot_sq_le _ _

/-- Hadamard in dimension 3, with the depletion shift:
`det(e₁, e₂, e₃)² ≤ |e₁|² |e₂|² |e₃ - e₂|²`. -/
theorem triple_sq_le_sub (e₁ e₂ e₃ : Fin 3 → R) :
    triple e₁ e₂ e₃ ^ 2 ≤ (e₁ ⬝ᵥ e₁) * ((e₂ ⬝ᵥ e₂) * ((e₃ - e₂) ⬝ᵥ (e₃ - e₂))) := by
  rw [triple_sub_second]
  refine (triple_sq_le _ _ _).trans ?_
  apply mul_le_mul_of_nonneg_left _ (dot_self_nonneg e₁)
  rw [cross_dot_self]
  nlinarith [sq_nonneg (e₂ ⬝ᵥ (e₃ - e₂))]

/-- Homogeneous Lipschitz-type bound on the depletion kernel:
`D(e₁, e₂, e₃)² ≤ |e₁|⁴ |e₂|² |e₃|² |e₃ - e₂|²`. -/
theorem depletionKernel_sq_le (e₁ e₂ e₃ : Fin 3 → R) :
    depletionKernel e₁ e₂ e₃ ^ 2 ≤
      (e₁ ⬝ᵥ e₁) * (e₃ ⬝ᵥ e₃) *
        ((e₁ ⬝ᵥ e₁) * ((e₂ ⬝ᵥ e₂) * ((e₃ - e₂) ⬝ᵥ (e₃ - e₂)))) := by
  rw [depletionKernel, mul_pow]
  exact mul_le_mul (dot_sq_le e₁ e₃) (triple_sq_le_sub e₁ e₂ e₃) (sq_nonneg _)
    (mul_nonneg (dot_self_nonneg _) (dot_self_nonneg _))

/-- Sharp unit form: for unit `e₁, e₃`, `D² ≤ |e₂ × e₃|²`, which for unit `e₂`
is `sin² ∠(e₂, e₃)`. -/
theorem depletionKernel_sq_le_cross_unit (e₁ e₂ e₃ : Fin 3 → R)
    (h₁ : e₁ ⬝ᵥ e₁ = 1) (h₃ : e₃ ⬝ᵥ e₃ = 1) :
    depletionKernel e₁ e₂ e₃ ^ 2 ≤ (e₂ ⨯₃ e₃) ⬝ᵥ (e₂ ⨯₃ e₃) := by
  have hc := dot_sq_le e₁ e₃
  rw [h₁, h₃, one_mul] at hc
  have ht := triple_sq_le e₁ e₂ e₃
  rw [h₁, one_mul] at ht
  rw [depletionKernel, mul_pow]
  calc (e₁ ⬝ᵥ e₃) ^ 2 * triple e₁ e₂ e₃ ^ 2
      ≤ 1 * triple e₁ e₂ e₃ ^ 2 := mul_le_mul_of_nonneg_right hc (sq_nonneg _)
    _ ≤ (e₂ ⨯₃ e₃) ⬝ᵥ (e₂ ⨯₃ e₃) := by rw [one_mul]; exact ht

/-- For unit vectors, `|e₂ × e₃|² ≤ |e₃ - e₂|²`. -/
theorem cross_sq_le_sub_unit (e₂ e₃ : Fin 3 → R)
    (h₂ : e₂ ⬝ᵥ e₂ = 1) (h₃ : e₃ ⬝ᵥ e₃ = 1) :
    (e₂ ⨯₃ e₃) ⬝ᵥ (e₂ ⨯₃ e₃) ≤ (e₃ - e₂) ⬝ᵥ (e₃ - e₂) := by
  rw [cross_dot_self, h₂, h₃]
  simp only [dotProduct_sub, sub_dotProduct, h₂, h₃, dotProduct_comm e₃ e₂]
  nlinarith [sq_nonneg (1 - e₂ ⬝ᵥ e₃)]

/-- For unit vectors, `|e₂ × e₃|² ≤ |e₃ + e₂|²`. -/
theorem cross_sq_le_add_unit (e₂ e₃ : Fin 3 → R)
    (h₂ : e₂ ⬝ᵥ e₂ = 1) (h₃ : e₃ ⬝ᵥ e₃ = 1) :
    (e₂ ⨯₃ e₃) ⬝ᵥ (e₂ ⨯₃ e₃) ≤ (e₃ + e₂) ⬝ᵥ (e₃ + e₂) := by
  rw [cross_dot_self, h₂, h₃]
  simp only [dotProduct_add, add_dotProduct, h₂, h₃, dotProduct_comm e₃ e₂]
  nlinarith [sq_nonneg (1 + e₂ ⬝ᵥ e₃)]

/-- Unit-vector depletion: `D(e₁, e₂, e₃)² ≤ |e₃ - e₂|²`. -/
theorem depletionKernel_sq_le_unit_sub (e₁ e₂ e₃ : Fin 3 → R)
    (h₁ : e₁ ⬝ᵥ e₁ = 1) (h₂ : e₂ ⬝ᵥ e₂ = 1) (h₃ : e₃ ⬝ᵥ e₃ = 1) :
    depletionKernel e₁ e₂ e₃ ^ 2 ≤ (e₃ - e₂) ⬝ᵥ (e₃ - e₂) :=
  (depletionKernel_sq_le_cross_unit e₁ e₂ e₃ h₁ h₃).trans (cross_sq_le_sub_unit e₂ e₃ h₂ h₃)

/-- Unit-vector depletion, anti-aligned side: `D(e₁, e₂, e₃)² ≤ |e₃ + e₂|²`. -/
theorem depletionKernel_sq_le_unit_add (e₁ e₂ e₃ : Fin 3 → R)
    (h₁ : e₁ ⬝ᵥ e₁ = 1) (h₂ : e₂ ⬝ᵥ e₂ = 1) (h₃ : e₃ ⬝ᵥ e₃ = 1) :
    depletionKernel e₁ e₂ e₃ ^ 2 ≤ (e₃ + e₂) ⬝ᵥ (e₃ + e₂) :=
  (depletionKernel_sq_le_cross_unit e₁ e₂ e₃ h₁ h₃).trans (cross_sq_le_add_unit e₂ e₃ h₂ h₃)

end Bounds

section Real

/-- Euclidean norm on `Fin 3 → ℝ` (the ambient `‖·‖` on this type is the sup
norm, so the Euclidean one is written out). -/
noncomputable def euclidNorm (v : Fin 3 → ℝ) : ℝ := Real.sqrt (v ⬝ᵥ v)

/-- **Pointwise geometric depletion.** For unit vectors,
`|D(e₁, e₂, e₃)| ≤ min(‖e₃ - e₂‖, ‖e₃ + e₂‖)` in the Euclidean norm. This is
the kernel-level reason a direction field that is Lipschitz *as a line field*
depletes vortex stretching. -/
theorem abs_depletionKernel_le_unit (e₁ e₂ e₃ : Fin 3 → ℝ)
    (h₁ : e₁ ⬝ᵥ e₁ = 1) (h₂ : e₂ ⬝ᵥ e₂ = 1) (h₃ : e₃ ⬝ᵥ e₃ = 1) :
    |depletionKernel e₁ e₂ e₃| ≤ min (euclidNorm (e₃ - e₂)) (euclidNorm (e₃ + e₂)) :=
  le_min (Real.abs_le_sqrt (depletionKernel_sq_le_unit_sub e₁ e₂ e₃ h₁ h₂ h₃))
    (Real.abs_le_sqrt (depletionKernel_sq_le_unit_add e₁ e₂ e₃ h₁ h₂ h₃))

/-- Non-vacuity witness: `D` is not identically zero on unit vectors.
With `e₁ = (1,1,1)/√3`, `e₂ = (1,0,0)`, `e₃ = (0,1,0)` the value is `1/3`.
`D` is homogeneous of degree 2 in `e₁`, so the unnormalised `e₁ = (1,1,1)` gives `D = 1`,
which stays rational. -/
theorem depletionKernel_witness :
    depletionKernel (![1, 1, 1] : Fin 3 → ℝ) ![1, 0, 0] ![0, 1, 0] = 1 := by
  simp [depletionKernel, triple, cross_apply, dotProduct, Fin.sum_univ_three]

end Real

end QOU.FluidDynamics.GeometricDepletion
