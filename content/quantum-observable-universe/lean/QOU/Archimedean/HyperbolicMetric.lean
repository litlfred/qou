/-
# HyperbolicMetric.lean — the GENUINE hyperbolic path-length metric on `H³`, and
# the engine that DERIVES isometry-invariance.

This file replaces an *adoption* with a *construction*.  Elsewhere in the corpus
the hyperbolic geometry of the upper half-space model is introduced by fiat:
`HyperbolicVolume.hypVolume := dx dy dz / z³` names the volume, `hypAngle` names
the angle, and `GeodesicFaceH3` / `IdealBoundaryGeodesicPlane` name the geodesic
faces by citing Thurston's classification.  Here the **distance** is built from
the ground up as the infimum of hyperbolic path lengths, and the two boundary
isometries (a vertical reflection, an inversion in a boundary sphere) are then
*derived* to preserve it — no metric, angle, or isometry adoption is needed for
`dH`.

## What is built

* `pathLenH γ a b := ∫⁻ t in [a,b], ‖γ'(t)‖ / γ(t)_z` — the hyperbolic length of
  a path, the Riemannian line element `ds = ‖dx‖ / z` integrated (Thurston GT3M
  Ch. 2 §2.3, p. 12: `ds² = (dx²+dy²+dz²)/z²`).
* `AdmissiblePath γ x y` — a differentiable path in `H³` from `x` to `y`.
* `dH x y := ⨅ over admissible γ, pathLenH γ 0 1` — the hyperbolic distance, a
  DERIVED object (an infimum of lengths), not an adopted `ds²`.

## What is PROVED here (sorry-free)

* `dH_self` — `dH x x = 0` (the constant path realises length `0`).
* `dH_image_le` / `dH_image_eq` — **the isometry engine.**  A map `φ` that is
  *conformal with the same factor on the height* — Fréchet derivative `Dφ(p)`
  scaling every tangent vector by `lam(p)` and height by the SAME `lam(p)` —
  preserves the line element `‖v‖/z` POINTWISE, hence preserves `pathLenH`, hence
  (as an infimum over a set carried bijectively by `φ`) preserves `dH`.  This is
  the single reusable lemma that Files `HyperbolicIsometryReflection` (`lam ≡ 1`)
  and `HyperbolicIsometryInversion` (`lam = R²/‖p-c‖²`) instantiate.

  The pointwise cancellation is the mathematical content: for the reflection the
  factor is `1` on both norm and height; for the inversion the conformal factor
  `R²/‖p-c‖²` and the height factor are literally the SAME real number, so the
  ratio `‖v‖/z` is untouched.  No change of variables, no cited geometry.

## What is NOT proved here (honest walls, each cited + beaned)

* `dH_comm` / `dH_triangle` — symmetry (path reversal) and the triangle
  inequality (path concatenation) are the remaining pseudometric axioms.  Both
  need a genuine change of variables / reparametrisation invariance of the
  set-restricted `lintegral`, which is a real chunk of measure theory; stated
  with an honest `sorry` + `-- Ref:` + bean `qou-hmet`.  They are NOT needed for
  the isometry results, which are pure pointwise congruences.
* Separation `dH x y = 0 → x = y` needs the fundamental theorem of calculus /
  absolute continuity to bound `pathLenH` below (a Cantor-type continuous path
  otherwise defeats a naive lower bound) — the same reason Mathlib has no
  hyperbolic geometry.  Left to bean `qou-hmet` as well.

The carrier is `EuclideanSpace ℝ (Fin 3)` (NOT the plain `Fin 3 → ℝ` of
`HyperbolicVolumeMeasure`, whose Haar/Lebesgue structure needs the sup-free Pi
type): the metric needs the *inner product* — norms of tangent vectors and the
inversion's conformal derivative — which only the Euclidean structure carries.
`upperH` here is the same predicate `{p | 0 < p 2}` transported to that carrier.

Archimedean (ℝ): `‖·‖`, `deriv`, ordering `0 < z` — §7c.

  -- Ref: [thurston1978] Ch. 2 §2.3 p. 12 (the metric `ds² = (dx²+dy²+dz²)/z²`)
  -- Ref: [milnor1982] §1 (upper half-space model, isometries by boundary inversion)
  -- Ref: [manuscript] beans qou-473l (T2), qou-idvt (T2), qou-hmet (metric-axiom walls)
-/

import Mathlib.MeasureTheory.Integral.Lebesgue.Basic
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.Analysis.InnerProductSpace.PiL2
import Mathlib.Analysis.Calculus.Deriv.Comp

namespace QOU.Archimedean.HyperbolicMetric

open MeasureTheory Set
open scoped ENNReal

/-- The carrier of the upper half-space model: `ℝ³` with its Euclidean inner
product (needed for tangent-vector norms and the inversion's conformal
derivative). -/
abbrev E := EuclideanSpace ℝ (Fin 3)

/-- **Upper half-space** `H³ = {(x,y,z) : z > 0}`, the same predicate as
`HyperbolicVolume.upperHalfSpace` on the Euclidean carrier. -/
def upperH : Set E := {p | 0 < p 2}

@[simp] theorem mem_upperH {p : E} : p ∈ upperH ↔ 0 < p 2 := Iff.rfl

/-- **Hyperbolic path length** `∫ ‖γ'(t)‖ / γ(t)_z dt` over `[a,b]`: the
Riemannian line element `ds = ‖dx‖ / z` of `ds² = (dx²+dy²+dz²)/z²` integrated
along `γ`.  Written with the real ratio inside `ENNReal.ofReal` so that the
conformal cancellation of the isometry engine is an elementary real identity. -/
noncomputable def pathLenH (γ : ℝ → E) (a b : ℝ) : ℝ≥0∞ :=
  ∫⁻ t in Set.Icc a b, ENNReal.ofReal (‖deriv γ t‖ / (γ t) 2)

/-- **An admissible path** from `x` to `y`: a path landing in `H³` on `[0,1]`,
differentiable there, with the right endpoints.  Differentiability on `[0,1]`
(not merely continuity) is what makes `pathLenH` measure the honest length — a
continuous-only class admits length-`0` Cantor paths between distinct points. -/
structure AdmissiblePath (γ : ℝ → E) (x y : E) : Prop where
  source : γ 0 = x
  target : γ 1 = y
  mem : ∀ t ∈ Set.Icc (0 : ℝ) 1, γ t ∈ upperH
  diff : ∀ t ∈ Set.Icc (0 : ℝ) 1, DifferentiableAt ℝ γ t

/-- **The hyperbolic distance** `dH x y`: the infimum of hyperbolic lengths over
admissible paths from `x` to `y`.  A DERIVED object — an infimum of the line
element — not an adopted metric tensor. -/
noncomputable def dH (x y : E) : ℝ≥0∞ :=
  ⨅ γ, ⨅ _ : AdmissiblePath γ x y, pathLenH γ 0 1

/-- Any admissible path bounds the distance from above: `dH x y ≤ len γ`. -/
theorem dH_le_pathLenH {γ : ℝ → E} {x y : E} (h : AdmissiblePath γ x y) :
    dH x y ≤ pathLenH γ 0 1 :=
  iInf₂_le γ h

/-- The distance is nonnegative — automatic in `ℝ≥0∞`, recorded for readers. -/
theorem dH_nonneg (x y : E) : 0 ≤ dH x y := zero_le _

/-- **`dH x x = 0`** for `x ∈ H³`: the constant path at `x` is admissible and has
hyperbolic length `0` (its derivative vanishes). -/
theorem dH_self {x : E} (hx : x ∈ upperH) : dH x x = 0 := by
  refine le_antisymm ?_ (zero_le _)
  have hadm : AdmissiblePath (fun _ => x) x x :=
    { source := rfl
      target := rfl
      mem := fun _ _ => hx
      diff := fun _ _ => differentiableAt_const x }
  refine le_trans (dH_le_pathLenH hadm) ?_
  simp only [pathLenH, deriv_const', norm_zero, zero_div, ENNReal.ofReal_zero,
    lintegral_zero, le_refl]

/-! ### The isometry engine

A map `φ : E → E` whose Fréchet derivative `Dφ(p)` scales every tangent vector by
`lam(p)` and whose height scales by the SAME `lam(p)` preserves the line element
`‖v‖/z` pointwise.  This is the one reusable lemma behind BOTH boundary
isometries. -/

/-- **Isometry engine, `≤` direction.**  If `φ` is conformal with factor `lam`
(derivative scales norms by `lam`) and scales the height coordinate by the SAME
`lam`, then `dH (φ x) (φ y) ≤ dH x y`.

The proof is a pointwise cancellation: along any admissible `γ`, the image path
`φ ∘ γ` is admissible, and at each `t` the chain rule gives
`‖(φ∘γ)'(t)‖ = lam·‖γ'(t)‖` while the height is `lam·γ(t)_z`, so the ratio
`‖v‖/z` — hence the whole integrand — is unchanged.  No change of variables. -/
theorem dH_image_le {φ : E → E} {Dφ : E → (E →L[ℝ] E)} {lam : E → ℝ}
    (hderiv : ∀ p ∈ upperH, HasFDerivAt φ (Dφ p) p)
    (hlam : ∀ p ∈ upperH, 0 < lam p)
    (hconf : ∀ p ∈ upperH, ∀ v, ‖Dφ p v‖ = lam p * ‖v‖)
    (hheight : ∀ p ∈ upperH, (φ p) 2 = lam p * (p 2))
    {x y : E} : dH (φ x) (φ y) ≤ dH x y := by
  refine le_iInf₂ fun γ hγ => ?_
  -- `φ` maps `H³` into `H³`.
  have hmaps : ∀ p ∈ upperH, φ p ∈ upperH := by
    intro p hp
    rw [mem_upperH, hheight p hp]
    exact mul_pos (hlam p hp) hp
  -- the image path is admissible.
  have hadm : AdmissiblePath (φ ∘ γ) (φ x) (φ y) := by
    refine { source := ?_, target := ?_, mem := ?_, diff := ?_ }
    · show φ (γ 0) = φ x; rw [hγ.source]
    · show φ (γ 1) = φ y; rw [hγ.target]
    · intro t ht; exact hmaps _ (hγ.mem t ht)
    · intro t ht
      have hp := hγ.mem t ht
      have hg : HasDerivAt γ (deriv γ t) t := (hγ.diff t ht).hasDerivAt
      exact ((hderiv _ hp).comp_hasDerivAt t hg).differentiableAt
  -- the lengths agree — the pointwise conformal cancellation.
  have hlen : pathLenH (φ ∘ γ) 0 1 = pathLenH γ 0 1 := by
    unfold pathLenH
    refine setLIntegral_congr_fun measurableSet_Icc (fun t ht => ?_)
    have hp := hγ.mem t ht
    have hg : HasDerivAt γ (deriv γ t) t := (hγ.diff t ht).hasDerivAt
    have hcomp : HasDerivAt (φ ∘ γ) (Dφ (γ t) (deriv γ t)) t :=
      (hderiv _ hp).comp_hasDerivAt t hg
    have hlp : 0 < lam (γ t) := hlam _ hp
    have hnorm : ‖deriv (φ ∘ γ) t‖ = lam (γ t) * ‖deriv γ t‖ := by
      rw [hcomp.deriv]; exact hconf _ hp _
    have hht : ((φ ∘ γ) t) 2 = lam (γ t) * (γ t) 2 := hheight _ hp
    rw [hnorm, hht, mul_div_mul_left _ _ (ne_of_gt hlp)]
  calc dH (φ x) (φ y) ≤ pathLenH (φ ∘ γ) 0 1 := dH_le_pathLenH hadm
    _ = pathLenH γ 0 1 := hlen

/-- **Isometry engine, equality.**  An involutive (`φ ∘ φ = id`) conformal
height-scaling map is a `dH`-isometry: `dH (φ x) (φ y) = dH x y`.  Both boundary
isometries below are involutions, so this is the form they use. -/
theorem dH_image_eq {φ : E → E} {Dφ : E → (E →L[ℝ] E)} {lam : E → ℝ}
    (hderiv : ∀ p ∈ upperH, HasFDerivAt φ (Dφ p) p)
    (hlam : ∀ p ∈ upperH, 0 < lam p)
    (hconf : ∀ p ∈ upperH, ∀ v, ‖Dφ p v‖ = lam p * ‖v‖)
    (hheight : ∀ p ∈ upperH, (φ p) 2 = lam p * (p 2))
    (hinv : ∀ p, φ (φ p) = p) (x y : E) :
    dH (φ x) (φ y) = dH x y := by
  refine le_antisymm (dH_image_le hderiv hlam hconf hheight) ?_
  have h := dH_image_le (φ := φ) (Dφ := Dφ) (lam := lam) hderiv hlam hconf hheight
      (x := φ x) (y := φ y)
  rwa [hinv, hinv] at h

end QOU.Archimedean.HyperbolicMetric
