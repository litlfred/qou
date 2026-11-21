/-
# HyperbolicIsometryAffine.lean (WALL-1) — the boundary-similarity generators are
# `dH`-isometries, DERIVED.

The reflection (`HyperbolicIsometryReflection`) and the boundary inversion
(`HyperbolicIsometryInversion`) generate the isometry group of `H³`, but the
`normalization` argument that reduces geodesic uniqueness between two arbitrary
points to the z-axis case needs the *boundary similarity group* explicitly:
**dilations** `p ↦ s·p` (`s > 0`), **horizontal translations** `p ↦ p + b`
(`b_z = 0`), and **horizontal rotations** (linear isometries fixing the height
coordinate).  This file derives each of them to preserve the DERIVED hyperbolic
distance `dH`, reusing the conformal-height-scaling engine `IsDHIsometry` — no
metric, angle, or isometry adoption.

## The mechanism (all three share it)

Each generator is *conformal with the same factor on the height*:

* **Dilation** `p ↦ s·p`: derivative `v ↦ s·v` scales every norm by `s`; the
  height scales by `s` too — `(s·p)_z = s·p_z`.  Line element `‖v‖/z` untouched.
* **Horizontal translation** `p ↦ p + b` with `b_z = 0`: derivative is the
  identity (`lam ≡ 1`); the height is unchanged (`(p+b)_z = p_z + 0 = p_z`).
* **Horizontal rotation** = any linear isometry `L` with `(L p)_z = p_z`:
  derivative `L` scales norms by `1` (isometry) and fixes the height (`lam ≡ 1`).
  The vertical reflection is the special orientation-reversing case; every
  horizontal `SO(2)`/`O(2)` rotation of the `(x,y)`-plane is covered.

None of the three is involutive (unlike the reflection/inversion), so `dH`
preservation is obtained from `IsDHIsometry.dH_le` in **both directions** via a
mutually-inverse partner (the general `dH_eq_of_leftInverse` helper below): the
dilation's partner is the reciprocal dilation, the translation's is the opposite
translation, the rotation's is `L.symm`.

## What is PROVED here (sorry-free)

* `dH_eq_of_leftInverse` — two mutually-inverse `dH`-isometries preserve `dH`.
* `heightFixingLinearIsom` / `dH_heightFixingLinearIsom` — a height-fixing linear
  isometry is a `dH`-isometry, and preserves `dH` (covers horizontal rotations).
* `dilationIsom` / `dH_dilation` — dilation by `s > 0`.
* `horizTranslationIsom` / `dH_horizTranslation` — horizontal translation.

`#print axioms` on each shows no `sorryAx` and no new axiom.

Archimedean (ℝ): `‖·‖`, inner product, ordering `0 < s` — §7c.

  -- Ref: [thurston1978] Ch. 2 §2.4 (isometries of the upper half-space model)
  -- Ref: [milnor1982] §1 (the boundary similarity group: dilations, translations)
  -- Ref: [ratcliffe] §4.6 (similarities are hyperbolic isometries)
  -- Ref: [leitner2026] beans qou-ztp3 (T2 WALL-1), qou-473l (T2), qou-idvt (T2)
-/

import QOU.Archimedean.HyperbolicMetric
import Mathlib.Analysis.Calculus.FDeriv.Add
import Mathlib.Analysis.Calculus.FDeriv.Mul

namespace QOU.Archimedean

open QOU.Archimedean.HyperbolicMetric

/-- **`dH` is preserved by a pair of mutually-inverse `dH`-isometries.**  Neither
generator here is involutive, so `IsDHIsometry.dH_eq` (which needs an involution)
does not apply; instead we sandwich `dH (φ x) (φ y)` between `dH x y` (from `φ`)
and itself (from a left inverse `ψ`).  If `ψ` is also a `dH`-isometry and
`ψ ∘ φ = id`, then `dH (φ x) (φ y) = dH x y`. -/
theorem dH_eq_of_leftInverse {φ ψ : E → E}
    (hφ : IsDHIsometry φ) (hψ : IsDHIsometry ψ)
    (hlinv : Function.LeftInverse ψ φ) (x y : E) :
    dH (φ x) (φ y) = dH x y := by
  refine le_antisymm hφ.dH_le ?_
  have hle := hψ.dH_le (x := φ x) (y := φ y)
  rwa [hlinv x, hlinv y] at hle

/-! ### Horizontal rotations — height-fixing linear isometries -/

/-- **The conformal height-scaling data of a height-fixing linear isometry**
(`lam ≡ 1`).  Any linear isometry `L` whose action fixes the height coordinate
(`(L p)_z = p_z`) scales every tangent norm by `1` (it is an isometry) and scales
the height by `1` (it fixes it), so it preserves the line element `‖v‖/z`.
Horizontal rotations of the `(x,y)`-plane are exactly this. -/
noncomputable def heightFixingLinearIsom (L : E ≃ₗᵢ[ℝ] E)
    (hL : ∀ p : E, (L p) 2 = p 2) : IsDHIsometry (L : E → E) where
  Dφ := fun _ => (L : E →L[ℝ] E)
  lam := fun _ => (1 : ℝ)
  hderiv := fun _ _ => (L : E →L[ℝ] E).hasFDerivAt
  hlam := fun _ _ => one_pos
  hconf := by
    intro _ _ v
    have hnorm : ‖(L : E →L[ℝ] E) v‖ = ‖v‖ := by
      have : (L : E →L[ℝ] E) v = L v := rfl
      rw [this]; exact LinearIsometryEquiv.norm_map _ _
    rw [one_mul, hnorm]
  hheight := by
    intro p _
    show (L p) 2 = 1 * (p 2)
    rw [one_mul]; exact hL p

/-- The inverse of a height-fixing linear isometry is again height-fixing:
`(L.symm p)_z = p_z` (apply `hL` at `L.symm p` and cancel `L (L.symm p) = p`). -/
theorem heightFixing_symm (L : E ≃ₗᵢ[ℝ] E) (hL : ∀ p : E, (L p) 2 = p 2)
    (p : E) : (L.symm p) 2 = p 2 := by
  have h := hL (L.symm p)
  rw [LinearIsometryEquiv.apply_symm_apply] at h
  exact h.symm

/-- **Horizontal rotations preserve the hyperbolic distance.**  A height-fixing
linear isometry `L` (a horizontal rotation, or the vertical reflection) is a
`dH`-isometry, and `L.symm` is a height-fixing linear isometry inverse to it, so
`dH (L x) (L y) = dH x y`. -/
theorem dH_heightFixingLinearIsom (L : E ≃ₗᵢ[ℝ] E) (hL : ∀ p : E, (L p) 2 = p 2)
    (x y : E) : dH (L x) (L y) = dH x y :=
  dH_eq_of_leftInverse (heightFixingLinearIsom L hL)
    (heightFixingLinearIsom L.symm (heightFixing_symm L hL))
    (fun p => L.symm_apply_apply p) x y

/-! ### Dilations `p ↦ s·p` (`s > 0`) -/

/-- **The conformal height-scaling data of a dilation** `p ↦ s·p` (`s > 0`).  The
derivative is the scalar map `v ↦ s·v`, scaling every norm by `s`; and the height
scales by the SAME `s`: `(s·p)_z = s·p_z`. -/
noncomputable def dilationIsom {s : ℝ} (hs : 0 < s) :
    IsDHIsometry (fun p : E => s • p) where
  Dφ := fun _ => s • ContinuousLinearMap.id ℝ E
  lam := fun _ => s
  hderiv := fun p _ => (hasFDerivAt_id p).const_smul s
  hlam := fun _ _ => hs
  hconf := by
    intro _ _ v
    rw [ContinuousLinearMap.smul_apply, ContinuousLinearMap.id_apply, norm_smul,
      Real.norm_eq_abs, abs_of_pos hs]
  hheight := by
    intro p _
    show (s • p) 2 = s * (p 2)
    rw [PiLp.smul_apply, smul_eq_mul]

/-- **Dilations preserve the hyperbolic distance.**  DERIVED via the reciprocal
dilation as the mutual inverse: `s⁻¹·(s·x) = x`. -/
theorem dH_dilation {s : ℝ} (hs : 0 < s) (x y : E) :
    dH (s • x) (s • y) = dH x y := by
  have hs' : 0 < s⁻¹ := inv_pos.mpr hs
  refine dH_eq_of_leftInverse (dilationIsom hs) (dilationIsom hs') ?_ x y
  intro p
  show s⁻¹ • (s • p) = p
  rw [smul_smul, inv_mul_cancel₀ (ne_of_gt hs), one_smul]

/-! ### Horizontal translations `p ↦ p + b` (`b_z = 0`) -/

/-- **The conformal height-scaling data of a horizontal translation** `p ↦ p + b`
with `b_z = 0`.  The derivative is the identity (`lam ≡ 1`), and the height is
unchanged: `(p + b)_z = p_z + b_z = p_z`. -/
noncomputable def horizTranslationIsom {b : E} (hb : b 2 = 0) :
    IsDHIsometry (fun p : E => p + b) where
  Dφ := fun _ => ContinuousLinearMap.id ℝ E
  lam := fun _ => (1 : ℝ)
  hderiv := fun p _ => (hasFDerivAt_id p).add_const b
  hlam := fun _ _ => one_pos
  hconf := by
    intro _ _ v
    rw [ContinuousLinearMap.id_apply, one_mul]
  hheight := by
    intro p _
    show (p + b) 2 = 1 * (p 2)
    rw [PiLp.add_apply, hb, add_zero, one_mul]

/-- The opposite of a horizontal vector is horizontal: `(-b)_z = 0`. -/
theorem horiz_neg {b : E} (hb : b 2 = 0) : (-b) 2 = 0 := by
  rw [PiLp.neg_apply, hb, neg_zero]

/-- **Horizontal translations preserve the hyperbolic distance.**  DERIVED via the
opposite translation as the mutual inverse: `(x + b) + (-b) = x`. -/
theorem dH_horizTranslation {b : E} (hb : b 2 = 0) (x y : E) :
    dH (x + b) (y + b) = dH x y := by
  refine dH_eq_of_leftInverse (horizTranslationIsom hb) (horizTranslationIsom (horiz_neg hb)) ?_ x y
  intro p
  show (p + b) + -b = p
  rw [add_neg_cancel_right]

end QOU.Archimedean
