/-
# TotallyGeodesicFaces.lean — the totally-geodesic classification, DRAINED to the
# CORPUS faces `GeodesicFaceH3.verticalPlane n d` and `hemisphere R`.

`HyperbolicGeodesic` proves the totally-geodesic property (conditional on the
single `HypMinimizerUnique` wall) for the *fixed sets* of the two derived
boundary isometries — `verticalPlaneFix` (the coordinate plane `{x = 0}`) and
`hemisphereFix c R` (a Euclidean sphere).  Those live on the Euclidean carrier
`E = EuclideanSpace ℝ (Fin 3)`.  The faces the ideal tetrahedron actually
intersects are `GeodesicFaceH3.verticalPlane n d` and `GeodesicFaceH3.hemisphere
R` — general vertical planes over the chords and the unit hemisphere — and they
live on the *plain* carrier `Fin 3 → ℝ` (`EuclideanSpace` is `PiLp 2` over that,
a type synonym with a different norm instance).

This file closes that last gap.  It builds a **general** vertical-plane
reflection `vReflect n d` (the coordinate case `n = (1,0), d = 0` is exactly the
merged `verticalReflection`), proves it is a `dH`-isometry via the same
conformal-height-scaling engine, and concludes — *directly from
`fixedSet_isTotallyGeodesic`*, hence still only `[HypMinimizerUnique]`-conditional
— that **every** corpus vertical plane (unit normal, any offset) and the corpus
hemisphere are totally geodesic.  The carrier transport is the identity map
`EuclideanSpace.equiv` (coordinate access agrees `rfl`), so the corpus face
`Set (Fin 3 → ℝ)` is transported to `Set E` by preimage.

Result: `IsTotallyGeodesic` now holds for the EXACT faces `idealTetrahedron`
intersects, not merely the fixed-set variants — the `GeodesicFaceH3` /
`IdealBoundaryGeodesicPlane` classification citation is DERIVED (modulo the one
`HypMinimizerUnique` wall) for the downstream objects themselves.

Archimedean (ℝ): `‖·‖`, inner product, `dist` — §7c.

  -- Ref: [thurston1978] Ch. 2 §2.3 (vertical planes and hemispheres are the
  --   totally-geodesic surfaces of `H³`)
  -- Ref: [ratcliffe] §4.6–4.7 (totally-geodesic surfaces of the upper half-space)
  -- Ref: [milnor1982] §1 (reflections and boundary inversions)
  -- Ref: [leitner2026] beans qou-473l (T2), qou-idvt (T2), qou-r111 (the geodesic-
  --   uniqueness wall), qou-322e (metric-axiom walls)
-/

import QOU.Archimedean.HyperbolicGeodesic
import QOU.Archimedean.GeodesicFaceH3
import Mathlib.Geometry.Euclidean.Inversion.Basic

namespace QOU.Archimedean

open QOU.Archimedean.HyperbolicMetric EuclideanGeometry
open scoped RealInnerProductSpace

/-! ### The Euclidean unit normal — coordinate facts

`verticalPlaneNormal n = ![n.1, n.2, 0]` (from `GeodesicFaceH3`), viewed as an
element of `E`.  Three elementary facts drive everything below. -/

/-- The inner product with the vertical-plane normal is the base-line functional
`n.1·p₀ + n.2·p₁` (the `z`-component of the normal is `0`). -/
theorem inner_verticalPlaneNormal (n : ℝ × ℝ) (p : E) :
    (⟪verticalPlaneNormal n, p⟫ : ℝ) = n.1 * p 0 + n.2 * p 1 := by
  simp only [verticalPlaneNormal, PiLp.inner_apply, RCLike.inner_apply, starRingEnd_apply,
    star_trivial, Fin.sum_univ_three, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.head_cons, Matrix.cons_val_two, Matrix.tail_cons]
  ring

/-- The vertical-plane normal has vanishing height coordinate. -/
theorem verticalPlaneNormal_apply_two (n : ℝ × ℝ) : (verticalPlaneNormal n) 2 = 0 := by
  simp [verticalPlaneNormal]

/-- For a unit base normal, the vertical-plane normal is a unit inner-product
vector: `⟪ñ, ñ⟫ = 1`. -/
theorem inner_verticalPlaneNormal_self {n : ℝ × ℝ} (hn : n.1 ^ 2 + n.2 ^ 2 = 1) :
    (⟪verticalPlaneNormal n, verticalPlaneNormal n⟫ : ℝ) = 1 := by
  rw [real_inner_self_eq_norm_sq, norm_verticalPlaneNormal hn]; norm_num

/-- For a unit base normal, the normal is nonzero. -/
theorem verticalPlaneNormal_ne_zero {n : ℝ × ℝ} (hn : n.1 ^ 2 + n.2 ^ 2 = 1) :
    verticalPlaneNormal n ≠ 0 := by
  intro h
  have : (⟪verticalPlaneNormal n, verticalPlaneNormal n⟫ : ℝ) = 0 := by rw [h]; simp
  rw [inner_verticalPlaneNormal_self hn] at this; norm_num at this

/-! ### The general vertical-plane reflection `vReflect n d`

Reflection across the affine plane `{p | ⟪ñ, p⟫ = d}` where `ñ =
verticalPlaneNormal n`: the Householder map `p ↦ p − 2(⟪ñ,p⟫ − d)·ñ`.  A genuine
Euclidean isometry that fixes the height coordinate (because `ñ_z = 0`), so it is
the `lam ≡ 1` case of the conformal-height-scaling engine. -/

/-- **The general vertical-plane reflection.**  Householder reflection across
`{p | ⟪ñ, p⟫ = d}`.  At `n = (1,0), d = 0` this is the merged `verticalReflection`
(reflection across `{x = 0}`). -/
noncomputable def vReflect (n : ℝ × ℝ) (d : ℝ) (p : E) : E :=
  p - (2 * ((⟪verticalPlaneNormal n, p⟫ : ℝ) - d)) • verticalPlaneNormal n

/-- Householder norm preservation: `‖v − 2⟪ñ,v⟫·ñ‖ = ‖v‖` for a unit `ñ`. -/
theorem householder_norm {nn : E} (hnn : (⟪nn, nn⟫ : ℝ) = 1) (v : E) :
    ‖v - (2 * (⟪nn, v⟫ : ℝ)) • nn‖ = ‖v‖ := by
  have hsq : ‖v - (2 * (⟪nn, v⟫ : ℝ)) • nn‖ ^ 2 = ‖v‖ ^ 2 := by
    rw [norm_sub_sq_real, inner_smul_right, norm_smul]
    have hnn' : ‖nn‖ ^ 2 = 1 := by rw [← real_inner_self_eq_norm_sq]; exact hnn
    have hcomm : (⟪v, nn⟫ : ℝ) = ⟪nn, v⟫ := real_inner_comm _ _
    simp only [Real.norm_eq_abs]
    rw [hcomm, mul_pow, sq_abs, hnn']
    ring
  have := congrArg Real.sqrt hsq
  rwa [Real.sqrt_sq (norm_nonneg _), Real.sqrt_sq (norm_nonneg _)] at this

/-- **The conformal height-scaling data of the general vertical reflection**
(`lam ≡ 1`).  Its Fréchet derivative is the Householder linear map (norm-preserving,
factor `1`), and it fixes the height coordinate (factor `1`). -/
noncomputable def verticalPlaneReflectionIsom {n : ℝ × ℝ} (hn : n.1 ^ 2 + n.2 ^ 2 = 1)
    (d : ℝ) : IsDHIsometry (vReflect n d) where
  Dφ := fun _ => ContinuousLinearMap.id ℝ E
    - ((2 : ℝ) • innerSL ℝ (verticalPlaneNormal n)).smulRight (verticalPlaneNormal n)
  lam := fun _ => (1 : ℝ)
  hderiv := by
    intro p _
    unfold vReflect
    have hg : HasFDerivAt (fun q : E => (⟪verticalPlaneNormal n, q⟫ : ℝ))
        (innerSL ℝ (verticalPlaneNormal n)) p := (innerSL ℝ (verticalPlaneNormal n)).hasFDerivAt
    have h1 : HasFDerivAt (fun q : E => 2 * ((⟪verticalPlaneNormal n, q⟫ : ℝ) - d))
        ((2 : ℝ) • innerSL ℝ (verticalPlaneNormal n)) p := by
      have := (hg.sub_const d).const_mul (2 : ℝ); simpa using this
    exact (hasFDerivAt_id p).sub (h1.smul_const (verticalPlaneNormal n))
  hlam := fun _ _ => one_pos
  hconf := by
    intro _ _ v
    rw [one_mul]
    show ‖(ContinuousLinearMap.id ℝ E
      - ((2 : ℝ) • innerSL ℝ (verticalPlaneNormal n)).smulRight (verticalPlaneNormal n)) v‖ = ‖v‖
    simp only [ContinuousLinearMap.sub_apply, ContinuousLinearMap.id_apply,
      ContinuousLinearMap.smulRight_apply, ContinuousLinearMap.smul_apply, innerSL_apply,
      smul_eq_mul]
    exact householder_norm (inner_verticalPlaneNormal_self hn) v
  hheight := by
    intro p _
    show (vReflect n d p) 2 = 1 * (p 2)
    rw [one_mul]
    simp only [vReflect, PiLp.sub_apply, PiLp.smul_apply, smul_eq_mul,
      verticalPlaneNormal_apply_two, mul_zero, sub_zero]

/-- The general vertical reflection is involutive. -/
theorem vReflect_involutive {n : ℝ × ℝ} (hn : n.1 ^ 2 + n.2 ^ 2 = 1) (d : ℝ) :
    Function.Involutive (vReflect n d) := by
  intro p
  have hself : (⟪verticalPlaneNormal n, verticalPlaneNormal n⟫ : ℝ) = 1 :=
    inner_verticalPlaneNormal_self hn
  simp only [vReflect, inner_sub_right, real_inner_smul_right, hself, mul_one]
  module

/-- **Fixed-set characterisation.**  For a unit normal, `vReflect n d` fixes `p`
iff `p` lies on the corpus vertical plane `p₀·n.1 + p₁·n.2 = d`. -/
theorem vReflect_fixed_iff {n : ℝ × ℝ} (hn : n.1 ^ 2 + n.2 ^ 2 = 1) (d : ℝ) (p : E) :
    vReflect n d p = p ↔ p 0 * n.1 + p 1 * n.2 = d := by
  rw [vReflect, sub_eq_self, smul_eq_zero, inner_verticalPlaneNormal]
  constructor
  · rintro (hs | hz)
    · have h2 : (2 : ℝ) ≠ 0 := by norm_num
      rcases mul_eq_zero.mp hs with h | h
      · exact absurd h h2
      · linear_combination h
    · exact absurd hz (verticalPlaneNormal_ne_zero hn)
  · intro hp
    left
    linear_combination 2 * hp

/-! ### Carrier transport and the DRAINED corpus-face theorems -/

/-- The corpus vertical plane, transported to the Euclidean carrier `E` by the
(coordinate-identity) equivalence `EuclideanSpace.equiv`. -/
def verticalPlaneE (n : ℝ × ℝ) (d : ℝ) : Set E :=
  (EuclideanSpace.equiv (Fin 3) ℝ) ⁻¹' verticalPlane n d

@[simp] theorem mem_verticalPlaneE {n : ℝ × ℝ} {d : ℝ} {p : E} :
    p ∈ verticalPlaneE n d ↔ p 0 * n.1 + p 1 * n.2 = d := Iff.rfl

/-- **The corpus vertical plane is totally geodesic** (conditional on the
geodesic-uniqueness wall `HypMinimizerUnique`), for ANY unit base normal `n` and
ANY offset `d` — the exact vertical faces the ideal tetrahedron intersects.

DERIVED from the general reflection `vReflect n d`'s isometry via
`fixedSet_isTotallyGeodesic`; it strictly generalises the merged
`verticalPlaneFix_isTotallyGeodesic` (the `n = (1,0), d = 0` instance). -/
theorem verticalPlane_isTotallyGeodesic [HypMinimizerUnique] {n : ℝ × ℝ}
    (hn : n.1 ^ 2 + n.2 ^ 2 = 1) (d : ℝ) :
    IsTotallyGeodesic (verticalPlaneE n d) := by
  intro x hx y hy γ hγ t ht
  have hfx : vReflect n d x = x := (vReflect_fixed_iff hn d x).mpr (mem_verticalPlaneE.mp hx)
  have hfy : vReflect n d y = y := (vReflect_fixed_iff hn d y).mpr (mem_verticalPlaneE.mp hy)
  have hfix : vReflect n d (γ t) = γ t :=
    fixedSet_isTotallyGeodesic (verticalPlaneReflectionIsom hn d) hfx hfy hγ ht
  exact mem_verticalPlaneE.mpr ((vReflect_fixed_iff hn d (γ t)).mp hfix)

/-! ### The hemisphere -/

/-- The corpus hemisphere, transported to `E` by `EuclideanSpace.equiv`. -/
def hemisphereE (R : ℝ) : Set E :=
  (EuclideanSpace.equiv (Fin 3) ℝ) ⁻¹' hemisphere R

@[simp] theorem mem_hemisphereE {R : ℝ} {p : E} :
    p ∈ hemisphereE R ↔ (p 0) ^ 2 + (p 1) ^ 2 + (p 2) ^ 2 = R ^ 2 ∧ 0 < p 2 := Iff.rfl

/-- `dist p 0 = ‖p‖`, and `‖p‖² = ∑ (p i)²` on the Euclidean carrier — the bridge
between the inversion's `dist`-language and the corpus sphere equation. -/
theorem dist_zero_sq (p : E) :
    (dist p (0 : E)) ^ 2 = (p 0) ^ 2 + (p 1) ^ 2 + (p 2) ^ 2 := by
  rw [dist_zero_right, ← real_inner_self_eq_norm_sq]
  simp only [PiLp.inner_apply, RCLike.inner_apply, starRingEnd_apply, star_trivial,
    Fin.sum_univ_three]
  ring

/-- The origin has vanishing height coordinate (it is a boundary centre). -/
theorem zero_apply_two : (0 : E) 2 = 0 := rfl

/-- **The corpus hemisphere is totally geodesic** (conditional on the geodesic-
uniqueness wall `HypMinimizerUnique`), for any radius `R > 0` — the exact
hemispherical face the ideal tetrahedron intersects.

DERIVED from the boundary inversion in the sphere of radius `R` centred at the
origin (`c = 0`, which lies on `∂H³`): its fixed set is that Euclidean sphere, and
a minimiser between two `H³` points stays in `H³` (`z > 0`), so it stays in the
hemisphere `sphere ∩ {z > 0}`. -/
theorem hemisphere_isTotallyGeodesic [HypMinimizerUnique] {R : ℝ} (hR : 0 < R) :
    IsTotallyGeodesic (hemisphereE R) := by
  intro x hx y hy γ hγ t ht
  -- endpoints lie on the sphere ‖·‖ = R, hence are fixed by the inversion.
  have hxsphere : x ∈ Metric.sphere (0 : E) R := by
    rw [Metric.mem_sphere]
    have hd2 : (dist x (0 : E)) ^ 2 = R ^ 2 := by rw [dist_zero_sq]; exact (mem_hemisphereE.mp hx).1
    have hd : 0 ≤ dist x (0 : E) := dist_nonneg
    have e : |dist x (0 : E)| = |R| := by rw [← Real.sqrt_sq_eq_abs, ← Real.sqrt_sq_eq_abs, hd2]
    rwa [abs_of_nonneg hd, abs_of_nonneg hR.le] at e
  have hysphere : y ∈ Metric.sphere (0 : E) R := by
    rw [Metric.mem_sphere]
    have hd2 : (dist y (0 : E)) ^ 2 = R ^ 2 := by rw [dist_zero_sq]; exact (mem_hemisphereE.mp hy).1
    have hd : 0 ≤ dist y (0 : E) := dist_nonneg
    have e : |dist y (0 : E)| = |R| := by rw [← Real.sqrt_sq_eq_abs, ← Real.sqrt_sq_eq_abs, hd2]
    rwa [abs_of_nonneg hd, abs_of_nonneg hR.le] at e
  have hfx : inversion (0 : E) R x = x := inversion_of_mem_sphere hxsphere
  have hfy : inversion (0 : E) R y = y := inversion_of_mem_sphere hysphere
  -- the fixed set of the inversion is totally geodesic.
  have hfix : inversion (0 : E) R (γ t) = γ t :=
    fixedSet_isTotallyGeodesic (boundaryInversionIsom zero_apply_two hR) hfx hfy hγ ht
  -- from the fixed point, recover the sphere equation on `γ t`.
  have hgt_upper : γ t ∈ upperH := hγ.admissible.mem t ht
  have hz : 0 < (γ t) 2 := hgt_upper
  have hne : γ t ≠ (0 : E) := by
    intro h
    have hz' := hz; rw [h, zero_apply_two] at hz'; exact absurd hz' (lt_irrefl 0)
  have hdc : dist (inversion (0 : E) R (γ t)) (0 : E) = R ^ 2 / dist (γ t) (0 : E) :=
    dist_inversion_center (0 : E) (γ t) R
  rw [hfix] at hdc
  have hdpos : 0 < dist (γ t) (0 : E) := dist_pos.mpr hne
  -- dist = R²/dist ⇒ dist² = R² ⇒ dist = R.
  have hdsq : (dist (γ t) (0 : E)) ^ 2 = R ^ 2 := by
    have hne' : dist (γ t) (0 : E) ≠ 0 := ne_of_gt hdpos
    field_simp [hne'] at hdc
    nlinarith [hdc]
  have hspheq : (γ t) 0 ^ 2 + (γ t) 1 ^ 2 + (γ t) 2 ^ 2 = R ^ 2 := by
    rw [← dist_zero_sq]; exact hdsq
  exact mem_hemisphereE.mpr ⟨hspheq, hz⟩

end QOU.Archimedean
