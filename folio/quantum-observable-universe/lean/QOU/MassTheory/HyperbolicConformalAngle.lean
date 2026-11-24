/-
# File 1 (LINCHPIN) — the upper half-space metric is CONFORMAL: hyperbolic
# angle = Euclidean angle.

This is the single geometric fact that makes "hyperbolic dihedral angle =
Euclidean dihedral angle" true, and hence the whole T2 dihedral-angle bridge
(Files 3–4) work.  It is PROVED here from Mathlib's inner-product geometry
alone — no manifold theory, no cited hyperbolic geometry.

## The statement

In the upper half-space model `H³ = {(x,y,z) : z > 0}` with Riemannian metric
`ds² = (dx² + dy² + dz²)/z²`, the inner product on the tangent space at a point
of height `z` is the Euclidean inner product rescaled by `z⁻²`, and the induced
norm is rescaled by `z⁻¹`.  The angle between two tangent vectors `u, v` at
height `z` is therefore

    hypAngle z u v = arccos( (z⁻²⟪u,v⟫) / (√(z⁻²‖u‖²)·√(z⁻²‖v‖²)) ).

**`hypAngle_eq_angle` proves the `z⁻²` cancels completely**: for every `z > 0`,

    hypAngle z u v = InnerProductGeometry.angle u v          (the Euclidean angle)

so the hyperbolic angle does not depend on the height `z` at all — it equals the
Euclidean angle between the same tangent vectors.  This is CONFORMALITY, and it
is the reason a dihedral angle read off from Euclidean face normals is the true
hyperbolic dihedral angle.

This is genuinely non-vacuous: it is a statement about the actual arccos of the
actual rescaled inner-product ratio, and it would be FALSE for a non-conformal
rescaling (e.g. scaling only the `⟪u,v⟫` numerator).  The proof turns on the
`z⁻²` appearing to the SAME power in numerator and denominator — the defining
feature of a conformal metric.

Archimedean (ℝ): `Real.sqrt`, `arccos`, ordering `0 < z` — §7c.

-- Ref: [thurston1978] Ch. 7 (the upper half-space model and its conformal metric)
-- Ref: [milnor1982] §1 (the metric `ds² = (dx²+dy²+dz²)/z²`)
-- Ref: [leitner2026] beans qou-473l (T2 File 1), qou-idvt (T2)
-/

import Mathlib.Geometry.Euclidean.Angle.Unoriented.Basic

namespace QOU.Archimedean

open RealInnerProductSpace

variable {V : Type*} [NormedAddCommGroup V] [InnerProductSpace ℝ V]

/-- **The hyperbolic angle between tangent vectors `u, v` at height `z`** in the
upper half-space model.  The conformal factor `z⁻²` multiplies the Euclidean
inner product; the induced norms carry the same factor under a square root. -/
noncomputable def hypAngle (z : ℝ) (u v : V) : ℝ :=
  Real.arccos
    (((z ^ 2)⁻¹ * ⟪u, v⟫) /
      (Real.sqrt ((z ^ 2)⁻¹ * ‖u‖ ^ 2) * Real.sqrt ((z ^ 2)⁻¹ * ‖v‖ ^ 2)))

/-- **CONFORMALITY (the linchpin).**  For every `z > 0`, the hyperbolic angle at
height `z` equals the Euclidean angle between the same tangent vectors — the
`z⁻²` conformal factor cancels between numerator and denominator.

In particular the right-hand side does not mention `z`, so the hyperbolic angle
is **height-independent**: the same two tangent directions subtend the same
hyperbolic angle at every height. -/
theorem hypAngle_eq_angle {z : ℝ} (hz : 0 < z) (u v : V) :
    hypAngle z u v = InnerProductGeometry.angle u v := by
  have hz2 : ((z : ℝ) ^ 2)⁻¹ ≠ 0 := inv_ne_zero (pow_ne_zero 2 (ne_of_gt hz))
  have su : Real.sqrt ((z ^ 2)⁻¹ * ‖u‖ ^ 2) = z⁻¹ * ‖u‖ := by
    rw [Real.sqrt_mul (by positivity), Real.sqrt_sq (norm_nonneg _), Real.sqrt_inv,
      Real.sqrt_sq_eq_abs, abs_of_pos hz]
  have sv : Real.sqrt ((z ^ 2)⁻¹ * ‖v‖ ^ 2) = z⁻¹ * ‖v‖ := by
    rw [Real.sqrt_mul (by positivity), Real.sqrt_sq (norm_nonneg _), Real.sqrt_inv,
      Real.sqrt_sq_eq_abs, abs_of_pos hz]
  unfold hypAngle InnerProductGeometry.angle
  congr 1
  rw [su, sv,
    show z⁻¹ * ‖u‖ * (z⁻¹ * ‖v‖) = (z ^ 2)⁻¹ * (‖u‖ * ‖v‖) by rw [pow_two, mul_inv]; ring,
    mul_div_mul_left _ _ hz2]

/-- **Height-independence, stated on its own** (immediate from
`hypAngle_eq_angle`): the hyperbolic angle at any two positive heights agrees.
This is what lets a dihedral angle along a vertical edge be measured at any
convenient height. -/
theorem hypAngle_height_independent {z z' : ℝ} (hz : 0 < z) (hz' : 0 < z')
    (u v : V) : hypAngle z u v = hypAngle z' u v := by
  rw [hypAngle_eq_angle hz, hypAngle_eq_angle hz']

end QOU.Archimedean
