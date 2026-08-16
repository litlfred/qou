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
* `dH_comm` — `dH x y = dH y x` (symmetry).  DERIVED (no longer a bean): the
  reverse path `t ↦ γ(1−t)` is admissible with equal hyperbolic length, the length
  equality resting on the antitone one-dimensional change of variables
  (`reflect_lintegral_Icc`, from Mathlib's `JacobianOneDim` reflection Jacobian —
  which sidesteps the `IsNegInvariant` route and needs no measurability of the
  integrand).  So `dH y x ≤ pathLenH γ` for every admissible `γ : x → y`, hence
  `dH y x ≤ dH x y`; symmetric.
* `IsDHIsometry φ` + its methods — **the isometry engine.**  A map `φ` that is
  *conformal with the same factor on the height* — Fréchet derivative `Dφ(p)`
  scaling every tangent vector by `lam(p)` and height by the SAME `lam(p)` —
  preserves the line element `‖v‖/z` POINTWISE (`speed_comp`), hence preserves
  `pathLenH` (`pathLenH_comp`), hence `dH` (`dH_le`; `dH_eq` for involutions).
  This is the single reusable interface that Files `HyperbolicIsometryReflection`
  (`lam ≡ 1`) and `HyperbolicIsometryInversion` (`lam = R²/‖p-c‖²`) instantiate,
  and that `HyperbolicGeodesic`'s totally-geodesic classification consumes.

  The pointwise cancellation is the mathematical content: for the reflection the
  factor is `1` on both norm and height; for the inversion the conformal factor
  `R²/‖p-c‖²` and the height factor are literally the SAME real number, so the
  ratio `‖v‖/z` is untouched.  No change of variables, no cited geometry.

## What is NOT proved here (honest walls, tracked as a bean, NOT stubbed)

These are the remaining pseudometric axioms.  Per AGENTS.md ("if you cannot close
a derivation, CREATE A BEAN — not a `sorry`"), they are NOT stated as sorried
theorems: this file stays 100 % sorry-free, and the gap is tracked in bean
`qou-322e`.  None is needed for the isometry results (pure pointwise congruences)
or the geodesic classification.  `dH_comm` has since been CLOSED (above); the two
below remain open.

* `dH_triangle` (triangle inequality, via path concatenation).  The naive
  concatenation `η(t) = if t ≤ ½ then γ(2t) else δ(2t−1)` is **not** differentiable
  at the join `t = ½` (the one-sided velocities `2γ'(1)` and `2δ'(0)` need not
  match), so it fails `AdmissiblePath`'s everywhere-differentiability.  Closing it
  needs a zero-speed reparametrisation at the endpoints (a monotone `C¹` `φ` with
  `φ'(0)=φ'(1)=0`, e.g. `3t²−2t³`) together with reparametrisation length-invariance
  (a *monotone* Jacobian change of variables, the sibling of `reflect_lintegral_Icc`)
  AND a two-sided `HasDerivAt` glue at the join — a substantial chunk.
* Separation `dH x y = 0 → x = y` needs the fundamental theorem of calculus /
  absolute continuity to bound `pathLenH` below by the endpoint displacement (a
  Cantor-type continuous path otherwise defeats a naive lower bound, and here the
  bound must hold under the *infimum*) — the same reason Mathlib has no hyperbolic
  geometry.

The carrier is `EuclideanSpace ℝ (Fin 3)` (NOT the plain `Fin 3 → ℝ` of
`HyperbolicVolumeMeasure`, whose Haar/Lebesgue structure needs the sup-free Pi
type): the metric needs the *inner product* — norms of tangent vectors and the
inversion's conformal derivative — which only the Euclidean structure carries.
`upperH` here is the same predicate `{p | 0 < p 2}` transported to that carrier.

Archimedean (ℝ): `‖·‖`, `deriv`, ordering `0 < z` — §7c.

  -- Ref: [thurston1978] Ch. 2 §2.3 p. 12 (the metric `ds² = (dx²+dy²+dz²)/z²`)
  -- Ref: [milnor1982] §1 (upper half-space model, isometries by boundary inversion)
  -- Ref: [manuscript] beans qou-473l (T2), qou-idvt (T2), qou-322e (metric-axiom walls)
-/

import Mathlib.MeasureTheory.Integral.Lebesgue.Basic
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.MeasureTheory.Function.JacobianOneDim
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

/-! ### Symmetry `dH_comm` — DERIVED via the reverse path

The reverse path `t ↦ γ(1−t)` of an admissible `γ : x → y` is admissible from `y`
to `x`, and has the same hyperbolic length — the length equality is the antitone
one-dimensional change of variables `∫⁻_{[0,1]} F = ∫⁻_{[0,1]} F(1−·)`.  Hence
`dH` is symmetric.  No `IsNegInvariant` instance and no measurability of the
integrand are needed: the `JacobianOneDim` reflection Jacobian supplies the
change of variables for an arbitrary `u : ℝ → ℝ≥0∞`. -/

/-- **Reflection change of variables on `[0,1]`** — `∫⁻_{[0,1]} u = ∫⁻_{[0,1]}
u(1−·)`, from Mathlib's antitone one-dimensional Jacobian formula applied to the
reflection `t ↦ 1 − t` (whose derivative is `−1`, `|−1| = 1`, and which maps
`[0,1]` onto itself).  Holds for ANY `u`, no measurability required. -/
theorem reflect_lintegral_Icc (u : ℝ → ℝ≥0∞) :
    ∫⁻ t in Set.Icc (0 : ℝ) 1, u t = ∫⁻ t in Set.Icc (0 : ℝ) 1, u (1 - t) := by
  have himg : (fun t : ℝ => 1 - t) '' Set.Icc 0 1 = Set.Icc (0 : ℝ) 1 := by
    ext y; simp only [Set.mem_image, Set.mem_Icc]
    refine ⟨?_, ?_⟩
    · rintro ⟨x, ⟨hx0, hx1⟩, rfl⟩; constructor <;> linarith
    · rintro ⟨hy0, hy1⟩; exact ⟨1 - y, ⟨by linarith, by linarith⟩, by ring⟩
  have hf' : ∀ x ∈ Set.Icc (0 : ℝ) 1,
      HasDerivWithinAt (fun t => 1 - t) (-1) (Set.Icc 0 1) x :=
    fun x _ => ((hasDerivAt_id x).const_sub 1).hasDerivWithinAt
  have hanti : AntitoneOn (fun t : ℝ => 1 - t) (Set.Icc 0 1) := by
    intro a _ b _ hab; simp only; linarith
  have key := lintegral_image_eq_lintegral_deriv_mul_of_antitoneOn measurableSet_Icc hf' hanti u
  rw [himg] at key
  simpa only [neg_neg, ENNReal.ofReal_one, one_mul] using key

/-- The reverse path `t ↦ γ(1−t)` of an admissible `γ : x → y` is admissible from
`y` to `x` (endpoints swap; `H³` and differentiability are preserved because
`1 − t ∈ [0,1]` whenever `t ∈ [0,1]`). -/
theorem reverse_admissible {γ : ℝ → E} {x y : E} (hγ : AdmissiblePath γ x y) :
    AdmissiblePath (fun t => γ (1 - t)) y x where
  source := by show γ (1 - 0) = y; simpa using hγ.target
  target := by show γ (1 - 1) = x; simpa using hγ.source
  mem := fun t ht => hγ.mem (1 - t) ⟨by linarith [ht.2], by linarith [ht.1]⟩
  diff := fun t ht => by
    have h1 : DifferentiableAt ℝ (fun s : ℝ => 1 - s) t :=
      (differentiableAt_const (1 : ℝ)).sub differentiableAt_id
    exact (hγ.diff (1 - t) ⟨by linarith [ht.2], by linarith [ht.1]⟩).comp t h1

/-- The reversed path's speed matches the original at the reflected point:
`‖(γ∘(1−·))'(t)‖ = ‖γ'(1−t)‖` (the chain-rule factor `−1` has norm `1`). -/
theorem norm_deriv_reverse {γ : ℝ → E} {x y : E} (hγ : AdmissiblePath γ x y)
    {t : ℝ} (ht : t ∈ Set.Icc (0 : ℝ) 1) :
    ‖deriv (fun s => γ (1 - s)) t‖ = ‖deriv γ (1 - t)‖ := by
  have h1t : (1 - t) ∈ Set.Icc (0 : ℝ) 1 := ⟨by linarith [ht.2], by linarith [ht.1]⟩
  have hg : HasDerivAt γ (deriv γ (1 - t)) (1 - t) := (hγ.diff (1 - t) h1t).hasDerivAt
  have hf : HasDerivAt (fun s : ℝ => 1 - s) (-1) t := by
    simpa using (hasDerivAt_id t).const_sub 1
  have hcomp : HasDerivAt (fun s => γ (1 - s)) ((-1 : ℝ) • deriv γ (1 - t)) t := hg.scomp t hf
  rw [hcomp.deriv, norm_smul]; simp

/-- **Reverse path length preservation** — the reversed path has the same
hyperbolic length as the original.  The integrand at `t` is the original's
integrand at `1 − t` (`norm_deriv_reverse` for the numerator; the height is
`γ(1−t)_z` on both sides), and the reflection change of variables closes it. -/
theorem pathLenH_reverse {γ : ℝ → E} {x y : E} (hγ : AdmissiblePath γ x y) :
    pathLenH (fun s => γ (1 - s)) 0 1 = pathLenH γ 0 1 := by
  unfold pathLenH
  rw [reflect_lintegral_Icc (fun s => ENNReal.ofReal (‖deriv γ s‖ / (γ s) 2))]
  refine setLIntegral_congr_fun measurableSet_Icc (fun t ht => ?_)
  show ENNReal.ofReal (‖deriv (fun s => γ (1 - s)) t‖ / (γ (1 - t)) 2)
     = ENNReal.ofReal (‖deriv γ (1 - t)‖ / (γ (1 - t)) 2)
  rw [norm_deriv_reverse hγ ht]

/-- **`dH x y ≤ dH y x`** — each admissible `δ : y → x` reverses to an admissible
`x → y` path of equal length. -/
theorem dH_comm_le (x y : E) : dH x y ≤ dH y x := by
  refine le_iInf₂ (fun δ hδ => ?_)
  calc dH x y ≤ pathLenH (fun s => δ (1 - s)) 0 1 := dH_le_pathLenH (reverse_admissible hδ)
    _ = pathLenH δ 0 1 := pathLenH_reverse hδ

/-- **`dH` is symmetric** — `dH x y = dH y x`.  DERIVED (bean `qou-322e`, symmetry
leg), not adopted. -/
theorem dH_comm (x y : E) : dH x y = dH y x :=
  le_antisymm (dH_comm_le x y) (dH_comm_le y x)

/-! ### The isometry engine

A map `φ : E → E` whose Fréchet derivative `Dφ(p)` scales every tangent vector by
`lam(p)` and whose height scales by the SAME `lam(p)` preserves the line element
`‖v‖/z` **pointwise**.  We bundle these four facts as `IsDHIsometry φ` and derive
from them, once and reusably: image-admissibility, length preservation, pointwise
speed preservation, and finally `dH`-invariance.  Both boundary isometries below
(reflection, inversion) and the totally-geodesic classification consume this one
interface. -/

/-- **Conformal height-scaling data for `φ`.**  A choice of derivative field `Dφ`
and conformal factor `lam` witnessing that `φ` is, on `H³`, differentiable with a
derivative that scales every tangent norm by `lam(p)` and scales the height
coordinate by the SAME `lam(p)`.  Carries data (`Dφ`, `lam`), so it is a
`structure`, not a `Prop`. -/
structure IsDHIsometry (φ : E → E) where
  /-- the Fréchet derivative field of `φ`. -/
  Dφ : E → (E →L[ℝ] E)
  /-- the conformal factor. -/
  lam : E → ℝ
  hderiv : ∀ p ∈ upperH, HasFDerivAt φ (Dφ p) p
  hlam : ∀ p ∈ upperH, 0 < lam p
  hconf : ∀ p ∈ upperH, ∀ v, ‖Dφ p v‖ = lam p * ‖v‖
  hheight : ∀ p ∈ upperH, (φ p) 2 = lam p * (p 2)

namespace IsDHIsometry

variable {φ : E → E} (h : IsDHIsometry φ)
include h

/-- A conformal height-scaling map sends `H³` into `H³` (the height stays
positive: `lam·z > 0`). -/
theorem maps {p : E} (hp : p ∈ upperH) : φ p ∈ upperH := by
  rw [mem_upperH, h.hheight p hp]; exact mul_pos (h.hlam p hp) hp

/-- **The pointwise line-element preservation** — the mathematical heart.  At any
point of `H³`, the hyperbolic *speed* `‖γ'‖/z` of `φ ∘ γ` equals that of `γ`: the
conformal factor `lam` multiplies both `‖γ'‖` (via the chain rule + `hconf`) and
`z` (via `hheight`), and cancels. -/
theorem speed_comp {γ : ℝ → E}
    (hdiff : ∀ t ∈ Set.Icc (0 : ℝ) 1, DifferentiableAt ℝ γ t)
    (hmem : ∀ t ∈ Set.Icc (0 : ℝ) 1, γ t ∈ upperH)
    {t : ℝ} (ht : t ∈ Set.Icc (0 : ℝ) 1) :
    ‖deriv (φ ∘ γ) t‖ / ((φ ∘ γ) t) 2 = ‖deriv γ t‖ / (γ t) 2 := by
  have hp := hmem t ht
  have hg : HasDerivAt γ (deriv γ t) t := (hdiff t ht).hasDerivAt
  have hcomp : HasDerivAt (φ ∘ γ) (h.Dφ (γ t) (deriv γ t)) t :=
    (h.hderiv _ hp).comp_hasDerivAt t hg
  have hlp : 0 < h.lam (γ t) := h.hlam _ hp
  have hnorm : ‖deriv (φ ∘ γ) t‖ = h.lam (γ t) * ‖deriv γ t‖ := by
    rw [hcomp.deriv]; exact h.hconf _ hp _
  have hht : ((φ ∘ γ) t) 2 = h.lam (γ t) * (γ t) 2 := h.hheight _ hp
  rw [hnorm, hht, mul_div_mul_left _ _ (ne_of_gt hlp)]

/-- The image of an admissible path under `φ` is admissible (endpoints move by
`φ`, `H³` is preserved, differentiability is by the chain rule). -/
theorem admissiblePath_comp {γ : ℝ → E} {x y : E} (hγ : AdmissiblePath γ x y) :
    AdmissiblePath (φ ∘ γ) (φ x) (φ y) where
  source := by show φ (γ 0) = φ x; rw [hγ.source]
  target := by show φ (γ 1) = φ y; rw [hγ.target]
  mem := fun t ht => h.maps (hγ.mem t ht)
  diff := fun t ht =>
    ((h.hderiv _ (hγ.mem t ht)).comp_hasDerivAt t (hγ.diff t ht).hasDerivAt).differentiableAt

/-- `φ` preserves hyperbolic path length: `len (φ∘γ) = len γ` — the integral of
the pointwise-preserved speed. -/
theorem pathLenH_comp {γ : ℝ → E}
    (hdiff : ∀ t ∈ Set.Icc (0 : ℝ) 1, DifferentiableAt ℝ γ t)
    (hmem : ∀ t ∈ Set.Icc (0 : ℝ) 1, γ t ∈ upperH) :
    pathLenH (φ ∘ γ) 0 1 = pathLenH γ 0 1 := by
  unfold pathLenH
  refine setLIntegral_congr_fun measurableSet_Icc (fun t ht => ?_)
  rw [h.speed_comp hdiff hmem ht]

/-- **`dH (φ x) (φ y) ≤ dH x y`** — for each admissible `γ`, `φ∘γ` is admissible
with equal length. -/
theorem dH_le {x y : E} : dH (φ x) (φ y) ≤ dH x y := by
  refine le_iInf₂ fun γ hγ => ?_
  calc dH (φ x) (φ y) ≤ pathLenH (φ ∘ γ) 0 1 :=
        dH_le_pathLenH (h.admissiblePath_comp hγ)
    _ = pathLenH γ 0 1 := h.pathLenH_comp hγ.diff hγ.mem

/-- **`dH` is invariant under an involutive conformal height-scaling map.**  Both
boundary isometries are involutions, so this is the form they use. -/
theorem dH_eq (hinv : Function.Involutive φ) (x y : E) :
    dH (φ x) (φ y) = dH x y := by
  refine le_antisymm h.dH_le ?_
  have hle := h.dH_le (x := φ x) (y := φ y)
  rwa [hinv x, hinv y] at hle

end IsDHIsometry

end QOU.Archimedean.HyperbolicMetric
