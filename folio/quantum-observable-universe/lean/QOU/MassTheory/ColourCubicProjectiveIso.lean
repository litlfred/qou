/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import MathlibExt.ColourCubicHomogeneous
import Mathlib.AlgebraicGeometry.EllipticCurve.Projective.Point

/-!
# The colour cubic is projectively isomorphic to the elliptic curve 50a1

`ColourCubicElliptic` gives a degree-2 birational map from the colour cubic `h₃(X, z, w) = 0`
to `E : y² + xy + y = x³ − x − 2`. That map is in fact **linear**. With

  `M = [[−1, −1, −3], [2, −3, 1], [2, 2, 1]]`,   `det M = −25`,

the cubic form of `E` (in Mathlib's projective coordinates `[x : y : Z]`) satisfies

  `E(M·v) = 25 · h₃(v)`          (`weierPoly_toE`),

as an identity of cubic forms. The adjugate `N = [[1, 1, 2], [0, −1, 1], [−2, 0, −1]]` has
`M·N = N·M = 5·I`. So whenever `5` is a unit, `v ↦ M·v` is an automorphism of the projective
plane that carries the colour cubic onto `E`. This file proves:

* `W50a1`: the curve as a Mathlib `WeierstrassCurve` (`a₁ = 1, a₂ = 0, a₃ = 1, a₄ = −1, a₆ = −2`),
  with `c₄ = 25`, `c₆ = 1475`, `Δ = −1250` over any commutative ring, and over a field with
  `2 ≠ 0`, `5 ≠ 0`: `IsElliptic` and `j = −25/2`.
* `toE_toC`, `toC_toE`: `M·N = N·M = 5·I`.
* `equation_toE_iff`, `colour_toC_iff`: `v` is on the colour cubic iff `M·v` is on `E`, and `p`
  is on `E` iff `N·p` is on the colour cubic (when `5` is a unit).
* `planeEquiv`: the induced bijection of projective point classes, for any commutative ring with
  `5` a unit.
* `colourPointEquiv`: over a field with `2 ≠ 0`, `5 ≠ 0`, a bijection between the points of the
  colour cubic and the points `W50a1.Point` of the elliptic curve (Mathlib's group of points).
  Every point of either curve is nonsingular (`nonsingular_of_equation`).
* `toC_zero`: the identity `O = [0 : 1 : 0]` of `E` corresponds to `[1 : −1 : 0]`, the point the
  birational map of `ColourCubicElliptic` projected from.

So the earlier caveat "birational ⇒ isomorphic is not formalised" is discharged: the isomorphism
is explicit and global. The Cremona label "50a1" itself is a database fact; what is proved here is
that the curve has the invariants `c₄ = 25`, `c₆ = 1475`, `Δ = −1250` that the label records.

Base ring §7c: `CommRing` (with `IsUnit (5 : R)` where needed), and `Field` for the point
equivalence. No ordering, no `ℝ`.
-/

namespace QOU.Mass.ColourCubicProjectiveIso

open QOU.Mass.ColourCubicHomogeneous WeierstrassCurve WeierstrassCurve.Projective

section Generic

variable {R : Type*} [CommRing R]

/-- The Weierstrass curve `y² + xy + y = x³ − x − 2` (Cremona 50a1). -/
def W50a1 (R : Type*) [CommRing R] : WeierstrassCurve R := ⟨1, 0, 1, -1, -2⟩

theorem W50a1_b₂ : (W50a1 R).b₂ = 1 := by simp [W50a1, b₂]
theorem W50a1_b₄ : (W50a1 R).b₄ = -1 := by simp [W50a1, b₄]; ring
theorem W50a1_b₆ : (W50a1 R).b₆ = -7 := by simp [W50a1, b₆]; ring
theorem W50a1_b₈ : (W50a1 R).b₈ = -2 := by simp only [W50a1, b₈]; ring

theorem W50a1_c₄ : (W50a1 R).c₄ = 25 := by
  rw [c₄, W50a1_b₂, W50a1_b₄]; ring

theorem W50a1_c₆ : (W50a1 R).c₆ = 1475 := by
  rw [c₆, W50a1_b₂, W50a1_b₄, W50a1_b₆]; ring

theorem W50a1_Δ : (W50a1 R).Δ = -1250 := by
  rw [Δ, W50a1_b₂, W50a1_b₄, W50a1_b₆, W50a1_b₈]; ring

/-- The colour cubic evaluated at a representative `v = (X, z, w)`. -/
def colourAt (v : Fin 3 → R) : R := colourCubicHom (v 0) (v 1) (v 2)

/-- The cubic form of `E` in Mathlib's projective coordinates `[x : y : Z]`. -/
def weierPoly (p : Fin 3 → R) : R :=
  p 1 ^ 2 * p 2 + p 0 * p 1 * p 2 + p 1 * p 2 ^ 2 - (p 0 ^ 3 - p 0 * p 2 ^ 2 - 2 * p 2 ^ 3)

theorem equation_iff_weierPoly (p : Fin 3 → R) :
    (W50a1 R).toProjective.Equation p ↔ weierPoly p = 0 := by
  rw [equation_iff]
  simp only [W50a1, weierPoly]
  constructor <;> intro h <;> linear_combination h

/-- `v ↦ M·v`, colour coordinates `(X, z, w)` to Weierstrass coordinates `[x : y : Z]`. -/
def toE (v : Fin 3 → R) : Fin 3 → R :=
  ![-(v 0 + v 1 + 3 * v 2), 2 * v 0 - 3 * v 1 + v 2, 2 * v 0 + 2 * v 1 + v 2]

/-- `p ↦ N·p`, the adjugate direction. -/
def toC (p : Fin 3 → R) : Fin 3 → R :=
  ![p 0 + p 1 + 2 * p 2, -p 1 + p 2, -2 * p 0 - p 2]

theorem toC_toE (v : Fin 3 → R) : toC (toE v) = (5 : R) • v := by
  ext i; fin_cases i <;> simp [toC, toE] <;> ring

theorem toE_toC (p : Fin 3 → R) : toE (toC p) = (5 : R) • p := by
  ext i; fin_cases i <;> simp [toC, toE] <;> ring

theorem toE_smul (u : R) (v : Fin 3 → R) : toE (u • v) = u • toE v := by
  ext i; fin_cases i <;> simp [toE] <;> ring

theorem toC_smul (u : R) (p : Fin 3 → R) : toC (u • p) = u • toC p := by
  ext i; fin_cases i <;> simp [toC] <;> ring

/-- **The key identity.** `E(M·v) = 25·h₃(v)` as cubic forms. -/
theorem weierPoly_toE (v : Fin 3 → R) : weierPoly (toE v) = 25 * colourAt v := by
  simp [weierPoly, toE, colourAt, colourCubicHom]; ring

/-- `h₃(N·p) = 5·E(p)`. -/
theorem colourAt_toC (p : Fin 3 → R) : colourAt (toC p) = 5 * weierPoly p := by
  simp [weierPoly, toC, colourAt, colourCubicHom]; ring

/-- The identity `O = [0 : 1 : 0]` of `E` corresponds to `[1 : −1 : 0]` on the colour cubic. -/
theorem toC_zero : toC (![0, 1, 0] : Fin 3 → R) = ![1, -1, 0] := by
  ext i; fin_cases i <;> simp [toC]

variable (h5 : IsUnit (5 : R))
include h5

theorem equation_toE_iff (v : Fin 3 → R) :
    (W50a1 R).toProjective.Equation (toE v) ↔ colourAt v = 0 := by
  rw [equation_iff_weierPoly, weierPoly_toE]
  have h25 : IsUnit (25 : R) := by simpa [show (25 : R) = 5 * 5 by norm_num] using h5.mul h5
  exact h25.mul_right_eq_zero

theorem colour_toC_iff (p : Fin 3 → R) :
    colourAt (toC p) = 0 ↔ (W50a1 R).toProjective.Equation p := by
  rw [equation_iff_weierPoly, colourAt_toC]
  exact h5.mul_right_eq_zero

omit h5 in
theorem toE_equiv {v v' : Fin 3 → R} (h : v ≈ v') : toE v ≈ toE v' := by
  obtain ⟨u, rfl⟩ := h
  exact ⟨u, by simp [Units.smul_def, toE_smul]⟩

omit h5 in
theorem toC_equiv {p p' : Fin 3 → R} (h : p ≈ p') : toC p ≈ toC p' := by
  obtain ⟨u, rfl⟩ := h
  exact ⟨u, by simp [Units.smul_def, toC_smul]⟩

/-- **The projective-plane automorphism** `[v] ↦ [M·v]`, inverse `[p] ↦ [N·p]`, when `5` is a
unit. -/
def planeEquiv : PointClass R ≃ PointClass R where
  toFun := Quotient.map toE fun _ _ => toE_equiv
  invFun := Quotient.map toC fun _ _ => toC_equiv
  left_inv := by
    intro P; induction P using Quotient.inductionOn with
    | h v => simp only [Quotient.map_mk, toC_toE]; exact smul_eq v h5
  right_inv := by
    intro P; induction P using Quotient.inductionOn with
    | h p => simp only [Quotient.map_mk, toE_toC]; exact smul_eq p h5

omit h5 in
theorem colourAt_smul (u : R) (v : Fin 3 → R) : colourAt (u • v) = u ^ 3 * colourAt v := by
  simp [colourAt, colourCubicHom]; ring

end Generic

section Field

variable {F : Type*} [Field F]

/-- Over a field with `2 ≠ 0` and `5 ≠ 0`, `W50a1` is an elliptic curve (`Δ = −1250 = −2·5⁴`). -/
theorem isElliptic (h2 : (2 : F) ≠ 0) (h5 : (5 : F) ≠ 0) : (W50a1 F).IsElliptic := by
  refine ⟨?_⟩
  rw [W50a1_Δ, show (-1250 : F) = -(2 * 5 ^ 4) by norm_num]
  exact (IsUnit.mk0 _ (mul_ne_zero h2 (pow_ne_zero 4 h5))).neg

/-- `j(W50a1) = −25/2`. -/
theorem j_eq (h2 : (2 : F) ≠ 0) (h5 : (5 : F) ≠ 0) :
    @WeierstrassCurve.j F _ (W50a1 F) (isElliptic h2 h5) = -25 / 2 := by
  letI := isElliptic h2 h5
  rw [WeierstrassCurve.j, Units.val_inv_eq_inv_val, coe_Δ', W50a1_Δ, W50a1_c₄]
  have h1250 : (-1250 : F) = -(2 * 5 ^ 4) := by norm_num
  rw [h1250]
  field_simp
  norm_num

/-- Every nonzero solution of the equation of `W50a1` is a nonsingular point (`2, 5 ≠ 0`). -/
theorem nonsingular_of_equation (h2 : (2 : F) ≠ 0) (h5 : (5 : F) ≠ 0) {p : Fin 3 → F}
    (hp : p ≠ 0) (he : (W50a1 F).toProjective.Equation p) :
    (W50a1 F).toProjective.Nonsingular p := by
  by_cases hz : p 2 = 0
  · have hx : p 0 = 0 := X_eq_zero_of_Z_eq_zero he hz
    have hy : p 1 ≠ 0 := by
      intro hy; apply hp; ext i; fin_cases i <;> simp [hx, hy, hz]
    rw [nonsingular_of_Z_eq_zero hz]
    refine ⟨he, Or.inr ?_⟩
    simpa [W50a1, hx] using pow_ne_zero 2 hy
  · rw [nonsingular_of_Z_ne_zero hz]
    rw [equation_of_Z_ne_zero hz] at he
    letI := isElliptic h2 h5
    exact (Affine.equation_iff_nonsingular).mp he

/-- The points of the colour cubic: nonzero classes with `h₃ = 0`. -/
def ColourLift (P : PointClass F) : Prop :=
  P.lift (fun v => v ≠ 0 ∧ colourAt v = 0) fun v v' h => by
    obtain ⟨u, rfl⟩ := h
    simp only [Units.smul_def, colourAt_smul, ne_eq, smul_eq_zero, Units.ne_zero, false_or,
      mul_eq_zero, pow_eq_zero_iff, three_ne_zero, not_false_eq_true, Units.ne_zero]

/-- The points of the colour cubic over `F`. -/
def ColourPoint (F : Type*) [Field F] := {P : PointClass F // ColourLift P}

/-- **The colour cubic and 50a1 have the same points.** Over a field with `2 ≠ 0`, `5 ≠ 0`, the
linear map `v ↦ M·v` is a bijection from the points of `h₃ = 0` onto the points of the elliptic
curve `W50a1` (Mathlib's `Point`, which carries the group law). -/
noncomputable def colourPointEquiv (h2 : (2 : F) ≠ 0) (h5 : (5 : F) ≠ 0) :
    ColourPoint F ≃ (W50a1 F).toProjective.Point where
  toFun P := ⟨(show (W50a1 F).toProjective.NonsingularLift (planeEquiv (IsUnit.mk0 _ h5) P.1) by
    obtain ⟨P, hP⟩ := P
    induction P using Quotient.inductionOn with
    | h v =>
      obtain ⟨hv, hc⟩ := hP
      refine nonsingular_of_equation h2 h5 ?_ ((equation_toE_iff (IsUnit.mk0 _ h5) v).mpr hc)
      intro h0
      apply hv
      have := congrArg toC h0
      rw [toC_toE] at this
      have h0' : toC (0 : Fin 3 → F) = 0 := by ext i; fin_cases i <;> simp [toC]
      rw [h0'] at this
      exact (smul_eq_zero.mp this).resolve_left h5)⟩
  invFun Q := ⟨(planeEquiv (IsUnit.mk0 _ h5)).symm Q.point, by
    rcases Q with @⟨Q, hQ⟩
    induction Q using Quotient.inductionOn with
    | h p =>
      change (W50a1 F).toProjective.Nonsingular p at hQ
      change toC p ≠ 0 ∧ colourAt (toC p) = 0
      refine ⟨?_, (colour_toC_iff (IsUnit.mk0 _ h5) p).mpr hQ.1⟩
      intro h0
      have := congrArg toE h0
      rw [toE_toC] at this
      have h0' : toE (0 : Fin 3 → F) = 0 := by ext i; fin_cases i <;> simp [toE]
      rw [h0'] at this
      have hp : p = 0 := (smul_eq_zero.mp this).resolve_left h5
      rw [hp, nonsingular_iff] at hQ
      simp at hQ⟩
  left_inv P := Subtype.ext ((planeEquiv (IsUnit.mk0 _ h5)).left_inv P.1)
  right_inv Q := Point.ext ((planeEquiv (IsUnit.mk0 _ h5)).right_inv Q.point)

end Field

end QOU.Mass.ColourCubicProjectiveIso
