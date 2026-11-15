/-
# HyperbolicIsometryReflection.lean (C1) — reflection in a vertical plane is a
# `dH`-isometry, DERIVED.

A reflection across a vertical plane of `H³` — here the coordinate plane
`{x = 0}`, realised as the orthogonal reflection `(ℝ ∙ e₀)ᗮ.reflection` that
negates the first coordinate and fixes the other two (in particular the height
`z`) — preserves the derived hyperbolic distance `dH`.

This is the *easy* generator (the boundary similarity group), and the `lam ≡ 1`
special case of the conformal-height-scaling engine: the reflection is a genuine
Euclidean isometry, so it scales every tangent norm by `1`, and it fixes the
height coordinate, so it scales the height by `1` too.  The line element `‖v‖/z`
is therefore preserved verbatim, and the reflection is involutive.

Together with the inversion (`HyperbolicIsometryInversion`), these two generate
the isometry group of `H³` — both now DERIVED from `dH`, neither adopted.

Archimedean (ℝ): `‖·‖`, inner product — §7c.

  -- Ref: [thurston1978] Ch. 2 §2.4 (isometries of the upper half-space model)
  -- Ref: [milnor1982] §1 (reflections in vertical planes)
  -- Ref: [leitner2026] beans qou-473l (T2 C1), qou-idvt (T2)
-/

import QOU.Archimedean.HyperbolicMetric
import Mathlib.Analysis.InnerProductSpace.Projection.Reflection
import Mathlib.Analysis.Calculus.FDeriv.Linear

namespace QOU.Archimedean

open QOU.Archimedean.HyperbolicMetric
open scoped RealInnerProductSpace

/-- The vertical coordinate plane `{x = 0}`, as the subspace orthogonal to the
first basis vector `e₀ = single 0 1`.  Reflection across it negates `x` and fixes
`(y, z)` — a vertical-plane reflection (it contains the height axis `e₂`). -/
noncomputable def verticalReflection : E ≃ₗᵢ[ℝ] E :=
  (ℝ ∙ (EuclideanSpace.single (0 : Fin 3) (1 : ℝ)))ᗮ.reflection

/-- **The conformal height-scaling data of the vertical reflection** (`lam ≡ 1`).
The reflection is a Euclidean isometry, so its derivative — itself, as a linear
map — scales every norm by `1`; and it fixes the height coordinate, so the height
scales by `1` too. -/
noncomputable def verticalReflectionIsom : IsDHIsometry (verticalReflection : E → E) where
  Dφ := fun _ => (verticalReflection : E →L[ℝ] E)
  lam := fun _ => (1 : ℝ)
  hderiv := by
    -- a continuous linear map is its own Fréchet derivative
    intro p _
    exact (verticalReflection : E →L[ℝ] E).hasFDerivAt
  hlam := fun _ _ => one_pos
  hconf := by
    -- an isometry scales every norm by `1`
    intro _ _ v
    have hrefl : ‖(verticalReflection : E →L[ℝ] E) v‖ = ‖v‖ := by
      have : (verticalReflection : E →L[ℝ] E) v = verticalReflection v := rfl
      rw [this]; exact LinearIsometryEquiv.norm_map _ _
    rw [one_mul, hrefl]
  hheight := by
    -- the reflection fixes the height coordinate `z`
    intro p _
    set e2 : E := EuclideanSpace.single (2 : Fin 3) (1 : ℝ) with he2
    -- `e₂` lies in the reflecting plane `(ℝ ∙ e₀)ᗮ` (it is orthogonal to `e₀`).
    have hmem : e2 ∈ (ℝ ∙ (EuclideanSpace.single (0 : Fin 3) (1 : ℝ)))ᗮ := by
      rw [Submodule.mem_orthogonal_singleton_iff_inner_right, EuclideanSpace.inner_single_left]
      simp [he2, EuclideanSpace.single_apply]
    have hfix : verticalReflection e2 = e2 :=
      Submodule.reflection_mem_subspace_eq_self hmem
    -- express the height coordinate through the inner product with `e₂`.
    have hcoord : ∀ w : E, w 2 = ⟪w, e2⟫ := by
      intro w; rw [he2, EuclideanSpace.inner_single_right]; simp
    have key : (⟪verticalReflection p, e2⟫ : ℝ) = ⟪p, e2⟫ := by
      conv_lhs => rw [← hfix]
      exact LinearIsometryEquiv.inner_map_map _ _ _
    show (verticalReflection p) 2 = 1 * (p 2)
    rw [one_mul, hcoord (verticalReflection p), hcoord p, key]

/-- The vertical reflection is involutive. -/
theorem verticalReflection_involutive : Function.Involutive (verticalReflection : E → E) :=
  Submodule.reflection_involutive _

/-- **C1 — reflection in a vertical plane preserves the hyperbolic distance.**
DERIVED from the conformal-height-scaling engine (`IsDHIsometry.dH_eq`) at
`lam ≡ 1`: norms and height both scale by `1`, so the line element `‖v‖/z` is
preserved, and the reflection is involutive. -/
theorem dH_verticalReflection (x y : E) :
    dH (verticalReflection x) (verticalReflection y) = dH x y :=
  verticalReflectionIsom.dH_eq verticalReflection_involutive x y

end QOU.Archimedean
