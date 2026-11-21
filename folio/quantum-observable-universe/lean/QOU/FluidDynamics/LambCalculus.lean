import Mathlib.LinearAlgebra.BilinearMap
import Mathlib.Tactic

/-!
# Lamb calculi: "Beltrami ⇒ steady Euler" as algebra

The Lamb identity `(u·∇)u = ∇(|u|²/2) − u × curl u` is the vector-calculus form of the
Cartan/Koszul identity `∇_u u♭ = ι_u du♭ + ½ d|u|²`. Once it holds, the step
"a Beltrami field `curl u = λ u` solves steady Euler with pressure `−|u|²/2`" uses only
that `×` is bilinear and alternating, and that `∇` commutes with negation.

`LambCalculus` packages exactly those inputs over a commutative ring `F` of scalar
fields acting on a module `V` of vector fields. The analytic content (that the coordinate
calculus on ℝ³, or the Levi-Civita calculus on left-invariant fields of `sl₂(ℝ)`, satisfies
the Lamb identity) lives in the instances in `LambCalculusArchimedean`; this file has none.

Audit: `/mnt/project-files/qou-categorify-audit/analytic-steps-ranked-2026-11-15.md`, item 6.
-/

namespace QOU.FluidDynamics

/-- **A Lamb calculus** over the scalar ring `F`, on the `F`-module `V` of vector fields.
`good u` restricts the Lamb identity to the fields for which the instance proves it
(for example, fields with differentiable coordinate slices). -/
structure LambCalculus (F : Type*) [CommRing F] (V : Type*) [AddCommGroup V] [Module F V] where
  /-- The fields on which the Lamb identity is asserted. -/
  good : V → Prop
  /-- Self-advection `u ↦ (u·∇)u`. -/
  adv : V → V
  /-- Kinetic-energy density `|u|²/2`. -/
  ke : V → F
  /-- Gradient of a scalar field. -/
  grad : F → V
  /-- Curl of a vector field. -/
  curl : V → V
  /-- The cross product, `F`-bilinear. -/
  cross : V →ₗ[F] V →ₗ[F] V
  /-- `×` is alternating. -/
  cross_self : ∀ u, cross u u = 0
  /-- `∇` commutes with negation. -/
  grad_neg : ∀ f, grad (-f) = -grad f
  /-- **The Lamb identity.** -/
  lamb : ∀ u, good u → adv u = grad (ke u) - cross u (curl u)

variable {F : Type*} [CommRing F] {V : Type*} [AddCommGroup V] [Module F V]
variable (L : LambCalculus F V)

/-- For a Beltrami field the self-advection is a pure gradient. -/
theorem LambCalculus.adv_eq_grad_of_beltrami {u : V} (hu : L.good u) {lam : F} (hb : L.curl u = lam • u) :
    L.adv u = L.grad (L.ke u) := by
  rw [L.lamb u hu, hb, map_smul, L.cross_self, smul_zero, sub_zero]

/-- **Beltrami ⇒ steady Euler.** If `curl u = λ u` then `(u·∇)u + ∇p = 0` with
`p = −|u|²/2`. -/
theorem LambCalculus.steady_euler_of_beltrami {u : V} (hu : L.good u) {lam : F} (hb : L.curl u = lam • u) :
    L.adv u + L.grad (-L.ke u) = 0 := by
  rw [L.adv_eq_grad_of_beltrami hu hb, L.grad_neg, add_neg_cancel]

/-- The cross product on `Fin 3 → R`, as an `R`-bilinear map. -/
def LambCalculus.crossLin {R : Type*} [CommRing R] : (Fin 3 → R) →ₗ[R] (Fin 3 → R) →ₗ[R] (Fin 3 → R) :=
  LinearMap.mk₂ R
    (fun u w => ![u 1 * w 2 - u 2 * w 1, u 2 * w 0 - u 0 * w 2, u 0 * w 1 - u 1 * w 0])
    (fun _ _ _ => by ext i; fin_cases i <;> simp <;> ring)
    (fun _ _ _ => by ext i; fin_cases i <;> simp <;> ring)
    (fun _ _ _ => by ext i; fin_cases i <;> simp <;> ring)
    (fun _ _ _ => by ext i; fin_cases i <;> simp <;> ring)

theorem LambCalculus.crossLin_apply {R : Type*} [CommRing R] (u w : Fin 3 → R) :
    LambCalculus.crossLin u w = ![u 1 * w 2 - u 2 * w 1, u 2 * w 0 - u 0 * w 2, u 0 * w 1 - u 1 * w 0] := rfl

theorem LambCalculus.crossLin_self {R : Type*} [CommRing R] (u : Fin 3 → R) : LambCalculus.crossLin u u = 0 := by
  ext i; fin_cases i <;> simp [LambCalculus.crossLin_apply] <;> ring

end QOU.FluidDynamics
