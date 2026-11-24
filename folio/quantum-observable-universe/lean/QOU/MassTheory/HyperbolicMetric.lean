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
or the geodesic classification.  `dH_comm` and `dH_triangle` have since been
CLOSED (below), and separation is now CLOSED too: `dH_eq_zero_eq` in
`QOU.Archimedean.HyperbolicMetricSeparation` (sorry-free). The notes below record
the route as it stood when this file was written.

* Separation `dH x y = 0 → x = y` is **half proved**: the *height coordinate*
  is CLOSED unconditionally — `dH_eq_zero_height` derives `y₂ = x₂` from the
  vertical lower bound `dH x y ≥ |log(y₂/x₂)|` (`dH_ge_logHeight`,
  `pathLenH_ge_logHeight`), via the FTC applied to `t ↦ log(γ(t)₂)`.  Finite
  length makes `deriv γ` integrable (`hasFiniteIntegral_iff_ofReal`), defeating
  the Cantor obstruction; `measurable_deriv` supplies measurability with no
  global-differentiability hypothesis.  The *horizontal coordinates* remain
  open (bean `qou-v8u3`): they need the height bound `γ(t)₂ ≤ x₂·e^L` (FTC on
  `[0,t]`) plus the infimum-sequence argument `‖y_h − x_h‖ ≤ x₂·e^L·L → 0`.
  This vertical half is unconditional — independent of the sibling z-axis route
  (`HyperbolicGeodesicZAxis`), which reaches separation only through the
  `HypMinimizerUnique` conjecture.

The carrier is `EuclideanSpace ℝ (Fin 3)` (NOT the plain `Fin 3 → ℝ` of
`HyperbolicVolumeMeasure`, whose Haar/Lebesgue structure needs the sup-free Pi
type): the metric needs the *inner product* — norms of tangent vectors and the
inversion's conformal derivative — which only the Euclidean structure carries.
`upperH` here is the same predicate `{p | 0 < p 2}` transported to that carrier.

Archimedean (ℝ): `‖·‖`, `deriv`, ordering `0 < z` — §7c.

  -- Ref: [thurston1978] Ch. 2 §2.3 p. 12 (the metric `ds² = (dx²+dy²+dz²)/z²`)
  -- Ref: [milnor1982] §1 (upper half-space model, isometries by boundary inversion)
  -- Ref: [leitner2026] beans qou-473l (T2), qou-idvt (T2), qou-322e (metric-axiom walls)
-/

import Mathlib.MeasureTheory.Integral.Lebesgue.Basic
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.MeasureTheory.Function.JacobianOneDim
import Mathlib.Analysis.InnerProductSpace.PiL2
import Mathlib.Analysis.Calculus.Deriv.Comp
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.Analysis.Calculus.FDeriv.Measurable
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.Calculus.Deriv.MeanValue

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

/-- Smooth monotone reparametrisation profile `s(t) = 3t² − 2t³`. -/
noncomputable def sprof (t : ℝ) : ℝ := 3 * t ^ 2 - 2 * t ^ 3
theorem hasDerivAt_sprof (t : ℝ) : HasDerivAt sprof (6 * t * (1 - t)) t := by
  unfold sprof
  have p2 : HasDerivAt (fun t : ℝ => t ^ 2) (2 * t) t := by simpa using hasDerivAt_pow 2 t
  have p3 : HasDerivAt (fun t : ℝ => t ^ 3) (3 * t ^ 2) t := by simpa using hasDerivAt_pow 3 t
  have h1 : HasDerivAt (fun t : ℝ => 3 * t ^ 2) (3 * (2 * t)) t := p2.const_mul (3:ℝ)
  have h2 : HasDerivAt (fun t : ℝ => 2 * t ^ 3) (2 * (3 * t ^ 2)) t := p3.const_mul (2:ℝ)
  have := h1.sub h2
  convert this using 1; ring
theorem sprof_zero : sprof 0 = 0 := by unfold sprof; ring
theorem sprof_one : sprof 1 = 1 := by unfold sprof; ring

/-- **Reparametrisation length invariance (segment form).** -/
theorem pathLenH_reparam_segment {γ : ℝ → E} {x y : E} (hγ : AdmissiblePath γ x y)
    {a b : ℝ} (hab : a ≤ b) {ρ ρ' : ℝ → ℝ}
    (hρd : ∀ t ∈ Set.Icc a b, HasDerivAt ρ (ρ' t) t)
    (hρnn : ∀ t ∈ Set.Icc a b, 0 ≤ ρ' t)
    (hρmem : ∀ t ∈ Set.Icc a b, ρ t ∈ Set.Icc (0:ℝ) 1)
    (hρmono : MonotoneOn ρ (Set.Icc a b))
    (hρa : ρ a = 0) (hρb : ρ b = 1) :
    ∫⁻ t in Set.Icc a b,
        ENNReal.ofReal (‖deriv (fun s => γ (ρ s)) t‖ / (γ (ρ t)) 2)
      = pathLenH γ 0 1 := by
  set u : ℝ → ℝ≥0∞ := fun w => ENNReal.ofReal (‖deriv γ w‖ / (γ w) 2) with hu
  have hcont : ContinuousOn ρ (Set.Icc a b) :=
    fun t ht => ((hρd t ht).differentiableAt.continuousAt).continuousWithinAt
  have himg : ρ '' (Set.Icc a b) = Set.Icc (0:ℝ) 1 := by
    apply Set.Subset.antisymm
    · rintro w ⟨t, ht, rfl⟩; exact hρmem t ht
    · have := intermediate_value_Icc hab hcont
      rw [hρa, hρb] at this; exact this
  have hcov := lintegral_image_eq_lintegral_deriv_mul_of_monotoneOn
    (f := ρ) (f' := ρ') measurableSet_Icc
    (fun t ht => (hρd t ht).hasDerivWithinAt) hρmono u
  rw [himg] at hcov
  have hLHS : ∫⁻ w in Set.Icc (0:ℝ) 1, u w = pathLenH γ 0 1 := rfl
  have hpt : ∀ t ∈ Set.Icc a b,
      ENNReal.ofReal (‖deriv (fun s => γ (ρ s)) t‖ / (γ (ρ t)) 2)
        = ENNReal.ofReal (ρ' t) * u (ρ t) := by
    intro t ht
    have hγd : HasDerivAt γ (deriv γ (ρ t)) (ρ t) := (hγ.diff (ρ t) (hρmem t ht)).hasDerivAt
    have hcomp : HasDerivAt (fun s => γ (ρ s)) (ρ' t • deriv γ (ρ t)) t :=
      hγd.scomp t (hρd t ht)
    have hd : deriv (fun s => γ (ρ s)) t = ρ' t • deriv γ (ρ t) := hcomp.deriv
    have hnn := hρnn t ht
    rw [hd, norm_smul, Real.norm_eq_abs, abs_of_nonneg hnn, hu]
    simp only []
    rw [mul_div_assoc, ENNReal.ofReal_mul hnn]
  rw [setLIntegral_congr_fun measurableSet_Icc hpt, ← hcov, hLHS]

/-- `sprof` maps `[0,1]` into `[0,1]`: `sprof w = w²(3−2w) ≥ 0` and
`1 − sprof w = (1−w)²(1+2w) ≥ 0`. -/
theorem sprof_mem {w : ℝ} (hw : w ∈ Set.Icc (0:ℝ) 1) : sprof w ∈ Set.Icc (0:ℝ) 1 := by
  obtain ⟨h0, h1⟩ := hw
  constructor
  · have : sprof w = w ^ 2 * (3 - 2 * w) := by unfold sprof; ring
    rw [this]; have : (0:ℝ) ≤ 3 - 2 * w := by linarith
    positivity
  · have : (1:ℝ) - sprof w = (1 - w) ^ 2 * (1 + 2 * w) := by unfold sprof; ring
    nlinarith [sq_nonneg (1 - w), h0, h1]

/-- `MonotoneOn` on `Icc a b` from a nonnegative pointwise derivative. -/
theorem monotoneOn_of_hasDerivAt {a b : ℝ} {ρ ρ' : ℝ → ℝ}
    (hρd : ∀ t ∈ Set.Icc a b, HasDerivAt ρ (ρ' t) t)
    (hρnn : ∀ t ∈ Set.Icc a b, 0 ≤ ρ' t) : MonotoneOn ρ (Set.Icc a b) := by
  apply monotoneOn_of_deriv_nonneg (convex_Icc a b)
  · exact fun t ht => ((hρd t ht).differentiableAt.continuousAt).continuousWithinAt
  · intro t ht
    exact (hρd t (interior_subset ht)).differentiableAt.differentiableWithinAt
  · intro t ht
    have hmem := interior_subset ht
    rw [(hρd t hmem).deriv]; exact hρnn t hmem


/-- The zero-speed reparametrised concatenation of `γ` and `δ`. -/
noncomputable def concat (γ δ : ℝ → E) (t : ℝ) : E :=
  if t ≤ 1/2 then γ (sprof (2*t)) else δ (sprof (2*t - 1))

/-- Left branch as a standalone function. -/
noncomputable def concatL (γ : ℝ → E) : ℝ → E := fun s => γ (sprof (2*s))
/-- Right branch as a standalone function. -/
noncomputable def concatR (δ : ℝ → E) : ℝ → E := fun s => δ (sprof (2*s - 1))

/-- HasDerivAt for the left branch at points where `sprof (2s) ∈ [0,1]`. -/
theorem hasDerivAt_concatL {γ : ℝ → E} {x y : E} (hγ : AdmissiblePath γ x y) {s : ℝ}
    (hs : sprof (2*s) ∈ Set.Icc (0:ℝ) 1) :
    HasDerivAt (concatL γ) (((6 * (2*s) * (1 - 2*s)) * 2) • deriv γ (sprof (2*s))) s := by
  have hin : HasDerivAt (fun t : ℝ => 2*t) 2 s := by simpa using (hasDerivAt_id s).const_mul (2:ℝ)
  have hρ := (hasDerivAt_sprof (2*s)).comp s hin
  have hγd : HasDerivAt γ (deriv γ (sprof (2*s))) (sprof (2*s)) := (hγ.diff _ hs).hasDerivAt
  exact hγd.scomp s hρ

/-- HasDerivAt for the right branch at points where `sprof (2s-1) ∈ [0,1]`. -/
theorem hasDerivAt_concatR {δ : ℝ → E} {y z : E} (hδ : AdmissiblePath δ y z) {s : ℝ}
    (hs : sprof (2*s - 1) ∈ Set.Icc (0:ℝ) 1) :
    HasDerivAt (concatR δ) (((6 * (2*s-1) * (1 - (2*s-1))) * 2) • deriv δ (sprof (2*s-1))) s := by
  have hin : HasDerivAt (fun t : ℝ => 2*t - 1) 2 s := by
    simpa using ((hasDerivAt_id s).const_mul (2:ℝ)).sub_const 1
  have hρ := (hasDerivAt_sprof (2*s - 1)).comp s hin
  have hδd : HasDerivAt δ (deriv δ (sprof (2*s-1))) (sprof (2*s-1)) := (hδ.diff _ hs).hasDerivAt
  exact hδd.scomp s hρ

/-- The left branch has zero derivative at the join `s = 1/2`. -/
theorem hasDerivAt_concatL_half {γ : ℝ → E} {x y : E} (hγ : AdmissiblePath γ x y) :
    HasDerivAt (concatL γ) 0 (1/2) := by
  have hs : sprof (2*(1/2)) ∈ Set.Icc (0:ℝ) 1 := by
    have : (2:ℝ)*(1/2) = 1 := by ring
    rw [this]; exact sprof_mem (by norm_num)
  have h := hasDerivAt_concatL hγ hs
  have hz : ((6 * (2*(1/2:ℝ)) * (1 - 2*(1/2))) * 2) = 0 := by ring
  rw [hz, zero_smul] at h; exact h

/-- The right branch has zero derivative at the join `s = 1/2`. -/
theorem hasDerivAt_concatR_half {δ : ℝ → E} {y z : E} (hδ : AdmissiblePath δ y z) :
    HasDerivAt (concatR δ) 0 (1/2) := by
  have hs : sprof (2*(1/2) - 1) ∈ Set.Icc (0:ℝ) 1 := by
    have : (2:ℝ)*(1/2) - 1 = 0 := by ring
    rw [this]; exact sprof_mem (by norm_num)
  have h := hasDerivAt_concatR hδ hs
  have hz : ((6 * (2*(1/2:ℝ)-1) * (1 - (2*(1/2)-1))) * 2) = 0 := by ring
  rw [hz, zero_smul] at h; exact h


theorem concat_eq_L (γ δ : ℝ → E) {t : ℝ} (ht : t ≤ 1/2) :
    concat γ δ t = concatL γ t := by simp only [concat, concatL, if_pos ht]

theorem concat_eq_R (γ δ : ℝ → E) {t : ℝ} (ht : ¬ t ≤ 1/2) :
    concat γ δ t = concatR δ t := by simp only [concat, concatR, if_neg ht]

/-- On `[1/2, ∞)` the concatenation agrees with the right branch, using the
join-matching `γ 1 = δ 0`. -/
theorem concat_eq_R_ge (γ δ : ℝ → E) (hmatch : γ 1 = δ 0) {t : ℝ} (ht : 1/2 ≤ t) :
    concat γ δ t = concatR δ t := by
  rcases eq_or_lt_of_le ht with h | h
  · subst h
    rw [concat_eq_L γ δ (le_refl _)]
    simp only [concatL, concatR]
    rw [show (2:ℝ)*(1/2) = 1 by norm_num, sprof_one, show (1:ℝ) - 1 = 0 by norm_num,
       sprof_zero, hmatch]
  · exact concat_eq_R γ δ (by linarith)

/-- **The concatenation is differentiable at the join `1/2`** (both one-sided
derivatives vanish). -/
theorem hasDerivAt_concat_half {γ δ : ℝ → E} {x y z : E}
    (hγ : AdmissiblePath γ x y) (hδ : AdmissiblePath δ y z) :
    HasDerivAt (concat γ δ) 0 (1/2) := by
  have hmatch : γ 1 = δ 0 := by rw [hγ.target, hδ.source]
  have hIic : HasDerivWithinAt (concat γ δ) 0 (Set.Iic (1/2)) (1/2) :=
    (hasDerivAt_concatL_half hγ).hasDerivWithinAt.congr
      (fun z hz => concat_eq_L γ δ hz) (concat_eq_L γ δ (le_refl _))
  have hIci : HasDerivWithinAt (concat γ δ) 0 (Set.Ici (1/2)) (1/2) :=
    (hasDerivAt_concatR_half hδ).hasDerivWithinAt.congr
      (fun z hz => concat_eq_R_ge γ δ hmatch hz)
      (concat_eq_R_ge γ δ hmatch (le_refl _))
  have := hIic.union hIci
  rw [Set.Iic_union_Ici, hasDerivWithinAt_univ] at this
  exact this

/-- **The concatenation is admissible** from `x` to `z`. -/
theorem concat_admissible {γ δ : ℝ → E} {x y z : E}
    (hγ : AdmissiblePath γ x y) (hδ : AdmissiblePath δ y z) :
    AdmissiblePath (concat γ δ) x z where
  source := by
    rw [concat_eq_L γ δ (by norm_num)]
    show γ (sprof (2*0)) = x
    rw [show (2:ℝ)*0 = 0 by ring, sprof_zero, hγ.source]
  target := by
    rw [concat_eq_R γ δ (by norm_num)]
    show δ (sprof (2*1 - 1)) = z
    rw [show (2:ℝ)*1 - 1 = 1 by ring, sprof_one, hδ.target]
  mem := by
    intro t ht
    rcases le_or_gt t (1/2) with h | h
    · rw [concat_eq_L γ δ h]
      have h2t : (2*t) ∈ Set.Icc (0:ℝ) 1 := ⟨by linarith [ht.1], by linarith⟩
      exact hγ.mem _ (sprof_mem h2t)
    · rw [concat_eq_R γ δ (by linarith)]
      have h2t : (2*t - 1) ∈ Set.Icc (0:ℝ) 1 := ⟨by linarith, by linarith [ht.2]⟩
      exact hδ.mem _ (sprof_mem h2t)
  diff := by
    intro t ht
    rcases lt_trichotomy t (1/2) with h | h | h
    · -- t < 1/2 : agrees with concatL near t
      have hEq : concat γ δ =ᶠ[nhds t] concatL γ :=
        Filter.eventuallyEq_of_mem (isOpen_Iio.mem_nhds h)
          (fun y hy => concat_eq_L γ δ (le_of_lt hy))
      have h2t : sprof (2*t) ∈ Set.Icc (0:ℝ) 1 :=
        sprof_mem ⟨by linarith [ht.1], by linarith⟩
      exact (hEq.differentiableAt_iff).mpr (hasDerivAt_concatL hγ h2t).differentiableAt
    · subst h; exact (hasDerivAt_concat_half hγ hδ).differentiableAt
    · -- t > 1/2 : agrees with concatR near t
      have hEq : concat γ δ =ᶠ[nhds t] concatR δ :=
        Filter.eventuallyEq_of_mem (isOpen_Ioi.mem_nhds h)
          (fun y hy => concat_eq_R γ δ (by simp only [Set.mem_Ioi] at hy; linarith))
      have h2t : sprof (2*t - 1) ∈ Set.Icc (0:ℝ) 1 :=
        sprof_mem ⟨by linarith, by linarith [ht.2]⟩
      exact (hEq.differentiableAt_iff).mpr (hasDerivAt_concatR hδ h2t).differentiableAt


theorem hasDerivAt_rhoL (t : ℝ) :
    HasDerivAt (fun s => sprof (2*s)) ((6 * (2*t) * (1 - 2*t)) * 2) t := by
  have hin : HasDerivAt (fun s : ℝ => 2*s) 2 t := by simpa using (hasDerivAt_id t).const_mul (2:ℝ)
  exact (hasDerivAt_sprof (2*t)).comp t hin

theorem hasDerivAt_rhoR (t : ℝ) :
    HasDerivAt (fun s => sprof (2*s - 1)) ((6 * (2*t-1) * (1 - (2*t-1))) * 2) t := by
  have hin : HasDerivAt (fun s : ℝ => 2*s - 1) 2 t := by
    simpa using ((hasDerivAt_id t).const_mul (2:ℝ)).sub_const 1
  exact (hasDerivAt_sprof (2*t - 1)).comp t hin

/-- `deriv (concat γ δ) = deriv (concatL γ)` on `[0, 1/2]` (both `0` at the join). -/
theorem deriv_concat_eq_L {γ δ : ℝ → E} {x y z : E}
    (hγ : AdmissiblePath γ x y) (hδ : AdmissiblePath δ y z) {t : ℝ}
    (ht : t ∈ Set.Icc (0:ℝ) (1/2)) : deriv (concat γ δ) t = deriv (concatL γ) t := by
  rcases eq_or_lt_of_le ht.2 with h | h
  · rw [h, (hasDerivAt_concat_half hγ hδ).deriv, (hasDerivAt_concatL_half hγ).deriv]
  · have hEq : concat γ δ =ᶠ[nhds t] concatL γ :=
      Filter.eventuallyEq_of_mem (isOpen_Iio.mem_nhds h)
        (fun w hw => concat_eq_L γ δ (le_of_lt hw))
    exact hEq.deriv_eq

/-- `deriv (concat γ δ) = deriv (concatR δ)` on `(1/2, 1]`. -/
theorem deriv_concat_eq_R {γ δ : ℝ → E} {t : ℝ} (ht : 1/2 < t) :
    deriv (concat γ δ) t = deriv (concatR δ) t := by
  have hEq : concat γ δ =ᶠ[nhds t] concatR δ :=
    Filter.eventuallyEq_of_mem (isOpen_Ioi.mem_nhds ht)
      (fun w hw => concat_eq_R γ δ (by simp only [Set.mem_Ioi] at hw; linarith))
  exact hEq.deriv_eq

/-- **Length additivity of the concatenation.** -/
theorem pathLenH_concat {γ δ : ℝ → E} {x y z : E}
    (hγ : AdmissiblePath γ x y) (hδ : AdmissiblePath δ y z) :
    pathLenH (concat γ δ) 0 1 = pathLenH γ 0 1 + pathLenH δ 0 1 := by
  have hsplit : Set.Icc (0:ℝ) 1 = Set.Icc 0 (1/2) ∪ Set.Ioc (1/2) 1 :=
    (Set.Icc_union_Ioc_eq_Icc (by norm_num) (by norm_num)).symm
  have hdisj : Disjoint (Set.Icc (0:ℝ) (1/2)) (Set.Ioc (1/2) 1) := by
    rw [Set.disjoint_left]; rintro a ha hb; exact absurd ha.2 (not_le.mpr hb.1)
  -- left segment reparam
  have hLeft : ∫⁻ t in Set.Icc (0:ℝ) (1/2),
      ENNReal.ofReal (‖deriv (concatL γ) t‖ / (concatL γ t) 2) = pathLenH γ 0 1 := by
    have := pathLenH_reparam_segment hγ (a := 0) (b := 1/2) (by norm_num)
      (ρ := fun s => sprof (2*s)) (ρ' := fun t => (6 * (2*t) * (1 - 2*t)) * 2)
      (fun t _ => hasDerivAt_rhoL t)
      (fun t ht => by
        have : 0 ≤ 1 - 2*t := by linarith [ht.2]
        have : (0:ℝ) ≤ 2*t := by linarith [ht.1]
        positivity)
      (fun t ht => sprof_mem ⟨by linarith [ht.1], by linarith [ht.2]⟩)
      (monotoneOn_of_hasDerivAt (fun t _ => hasDerivAt_rhoL t)
        (fun t ht => by
          have h1 : 0 ≤ 1 - 2*t := by linarith [ht.2]
          have h2 : (0:ℝ) ≤ 2*t := by linarith [ht.1]
          positivity))
      (by simp only []; rw [show (2:ℝ)*0 = 0 by ring, sprof_zero])
      (by simp only []; rw [show (2:ℝ)*(1/2) = 1 by norm_num, sprof_one])
    simpa only [concatL] using this
  -- right segment reparam
  have hRightIcc : ∫⁻ t in Set.Icc (1/2:ℝ) 1,
      ENNReal.ofReal (‖deriv (concatR δ) t‖ / (concatR δ t) 2) = pathLenH δ 0 1 := by
    have := pathLenH_reparam_segment hδ (a := 1/2) (b := 1) (by norm_num)
      (ρ := fun s => sprof (2*s - 1)) (ρ' := fun t => (6 * (2*t-1) * (1 - (2*t-1))) * 2)
      (fun t _ => hasDerivAt_rhoR t)
      (fun t ht => by
        have h1 : 0 ≤ 1 - (2*t-1) := by linarith [ht.2]
        have h2 : (0:ℝ) ≤ 2*t-1 := by linarith [ht.1]
        positivity)
      (fun t ht => sprof_mem ⟨by linarith [ht.1], by linarith [ht.2]⟩)
      (monotoneOn_of_hasDerivAt (fun t _ => hasDerivAt_rhoR t)
        (fun t ht => by
          have h1 : 0 ≤ 1 - (2*t-1) := by linarith [ht.2]
          have h2 : (0:ℝ) ≤ 2*t-1 := by linarith [ht.1]
          positivity))
      (by simp only []; rw [show (2:ℝ)*(1/2) - 1 = 0 by norm_num, sprof_zero])
      (by simp only []; rw [show (2:ℝ)*1 - 1 = 1 by norm_num, sprof_one])
    simpa only [concatR] using this
  -- assemble
  rw [pathLenH, hsplit, lintegral_union measurableSet_Ioc hdisj]
  congr 1
  · -- left piece
    rw [← hLeft]
    refine setLIntegral_congr_fun measurableSet_Icc (fun t ht => ?_)
    rw [deriv_concat_eq_L hγ hδ ht, concat_eq_L γ δ ht.2]
  · -- right piece: Ioc → Icc, then match concatR
    rw [MeasureTheory.setLIntegral_congr Ioc_ae_eq_Icc, ← hRightIcc]
    refine setLIntegral_congr_fun measurableSet_Icc (fun t ht => ?_)
    rcases eq_or_lt_of_le ht.1 with h | h
    · -- t = 1/2 boundary (null, but prove pointwise anyway)
      rw [← h, deriv_concat_eq_L hγ hδ (by constructor <;> norm_num),
         concat_eq_L γ δ (by norm_num)]
      -- concatL γ (1/2) vs concatR δ (1/2): both derivs 0, values equal via match
      rw [(hasDerivAt_concatL_half hγ).deriv, (hasDerivAt_concatR_half hδ).deriv]
      have : concatL γ (1/2) = concatR δ (1/2) := by
        simp only [concatL, concatR]
        rw [show (2:ℝ)*(1/2) = 1 by norm_num, sprof_one, show (1:ℝ) - 1 = 0 by norm_num,
           sprof_zero, hγ.target, hδ.source]
      rw [this]
    · rw [deriv_concat_eq_R h, concat_eq_R γ δ (by linarith)]


/-- **Triangle inequality** `dH x z ≤ dH x y + dH y z`.  DERIVED via the
zero-speed reparametrised concatenation: the concatenation of an admissible
`x → y` path and an admissible `y → z` path is admissible `x → z` and has
hyperbolic length the sum of the two, so the infimum is subadditive. -/
theorem dH_triangle (x y z : E) : dH x z ≤ dH x y + dH y z := by
  refine ENNReal.le_iInf₂_add_iInf₂ (fun γ hγ δ hδ => ?_)
  calc dH x z ≤ pathLenH (concat γ δ) 0 1 := dH_le_pathLenH (concat_admissible hγ hδ)
    _ = pathLenH γ 0 1 + pathLenH δ 0 1 := pathLenH_concat hγ hδ

/-- Component `p ↦ p i` as a continuous linear functional on `E`. -/
noncomputable def coordCLM (i : Fin 3) : E →L[ℝ] ℝ :=
  (ContinuousLinearMap.proj i).comp (EuclideanSpace.equiv (Fin 3) ℝ).toContinuousLinearMap

@[simp] theorem coordCLM_apply (i : Fin 3) (p : E) : coordCLM i p = p i := rfl

/-- `|p i| ≤ ‖p‖` in Euclidean space. -/
theorem abs_coord_le_norm (p : E) (i : Fin 3) : |p i| ≤ ‖p‖ := by
  have := EuclideanSpace.norm_eq p
  rw [this]
  have hmem : i ∈ Finset.univ := Finset.mem_univ i
  have hle : ‖p i‖ ^ 2 ≤ ∑ j, ‖p j‖ ^ 2 :=
    Finset.single_le_sum (f := fun j => ‖p j‖ ^ 2) (fun j _ => sq_nonneg _) hmem
  calc |p i| = ‖p i‖ := (Real.norm_eq_abs _).symm
    _ = Real.sqrt (‖p i‖ ^ 2) := (Real.sqrt_sq (norm_nonneg _)).symm
    _ ≤ Real.sqrt (∑ j, ‖p j‖ ^ 2) := Real.sqrt_le_sqrt hle

/-- Component derivative: `d/dt (γ t) i = (deriv γ t) i`. -/
theorem deriv_coord {γ : ℝ → E} {t : ℝ} (hγ : DifferentiableAt ℝ γ t) (i : Fin 3) :
    HasDerivAt (fun s => (γ s) i) ((deriv γ t) i) t := by
  have h := hγ.hasDerivAt
  have := (coordCLM i).hasFDerivAt.comp_hasDerivAt t h
  simpa [coordCLM_apply] using this

/-- **z-component length lower bound.**  Every admissible path from `x` to `y`
has hyperbolic length at least `|log (y₂/x₂)|` — the vertical drop is a lower
bound for the hyperbolic length, via the FTC applied to `t ↦ log (γ(t)₂)`
(finite length ⇒ the derivative is integrable, defeating the Cantor obstruction).
Unconditional (no geodesic-uniqueness hypothesis). -/
theorem pathLenH_ge_logHeight {γ : ℝ → E} {x y : E} (hγ : AdmissiblePath γ x y) :
    ENNReal.ofReal |Real.log ((y) 2) - Real.log ((x) 2)| ≤ pathLenH γ 0 1 := by
  by_cases hL : pathLenH γ 0 1 = ∞
  · rw [hL]; exact le_top
  -- finite length
  set g : ℝ → ℝ := fun t => ‖deriv γ t‖ / (γ t) 2 with hg
  set φ' : ℝ → ℝ := fun t => (deriv γ t) 2 / (γ t) 2 with hφ'
  set φ : ℝ → ℝ := fun t => Real.log ((γ t) 2) with hφ
  have hLlt : ∫⁻ t in Set.Icc (0:ℝ) 1, ENNReal.ofReal (g t) < ∞ := lt_top_iff_ne_top.mpr hL
  -- continuity of γ on Icc, hence of the height coordinate
  have hγc : ContinuousOn γ (Set.Icc (0:ℝ) 1) :=
    fun t ht => (hγ.diff t ht).continuousAt.continuousWithinAt
  have hheightC : ContinuousOn (fun t => (γ t) 2) (Set.Icc (0:ℝ) 1) :=
    (coordCLM 2).continuous.comp_continuousOn hγc
  -- measurability of g and φ'
  have hnumNorm : AEStronglyMeasurable (fun t => ‖deriv γ t‖) (volume.restrict (Set.Icc (0:ℝ) 1)) :=
    ((measurable_deriv γ).norm).aestronglyMeasurable
  have hnumCoord : AEStronglyMeasurable (fun t => (deriv γ t) 2) (volume.restrict (Set.Icc (0:ℝ) 1)) :=
    (((coordCLM 2).measurable.comp (measurable_deriv γ)).aestronglyMeasurable)
  have hden : AEStronglyMeasurable (fun t => (γ t) 2) (volume.restrict (Set.Icc (0:ℝ) 1)) :=
    hheightC.aestronglyMeasurable measurableSet_Icc
  have hgm : AEStronglyMeasurable g (volume.restrict (Set.Icc (0:ℝ) 1)) :=
    (hnumNorm.aemeasurable.div hden.aemeasurable).aestronglyMeasurable
  have hφ'm : AEStronglyMeasurable φ' (volume.restrict (Set.Icc (0:ℝ) 1)) :=
    (hnumCoord.aemeasurable.div hden.aemeasurable).aestronglyMeasurable
  -- g ≥ 0 a.e. on Icc
  have hgnn : 0 ≤ᵐ[volume.restrict (Set.Icc (0:ℝ) 1)] g :=
    (ae_restrict_iff' measurableSet_Icc).mpr
      (ae_of_all _ (fun t ht => div_nonneg (norm_nonneg _) (le_of_lt (hγ.mem t ht))))
  -- g integrable on Icc
  have hgint : IntegrableOn g (Set.Icc (0:ℝ) 1) := by
    refine ⟨hgm, ?_⟩
    rw [hasFiniteIntegral_iff_ofReal hgnn]
    exact hLlt
  -- |φ' t| ≤ g t on Icc
  have hbound : ∀ t ∈ Set.Icc (0:ℝ) 1, ‖φ' t‖ ≤ g t := by
    intro t ht
    have hz : 0 < (γ t) 2 := hγ.mem t ht
    rw [hg, hφ', Real.norm_eq_abs, abs_div, abs_of_pos hz, div_le_div_iff_of_pos_right hz]
    exact abs_coord_le_norm _ 2
  -- φ' integrable on Icc (dominated by g)
  have hφ'int : IntegrableOn φ' (Set.Icc (0:ℝ) 1) := by
    refine Integrable.mono' hgint hφ'm ?_
    exact (ae_restrict_iff' measurableSet_Icc).mpr (ae_of_all _ hbound)
  -- FTC
  have hderiv : ∀ t ∈ Set.uIcc (0:ℝ) 1, HasDerivAt φ (φ' t) t := by
    intro t ht
    rw [Set.uIcc_of_le (by norm_num)] at ht
    exact (deriv_coord (hγ.diff t ht) 2).log (ne_of_gt (hγ.mem t ht))
  have hii : IntervalIntegrable φ' volume 0 1 := by
    rw [intervalIntegrable_iff_integrableOn_Icc_of_le (by norm_num)]
    exact hφ'int
  have hftc : ∫ t in (0:ℝ)..1, φ' t = φ 1 - φ 0 :=
    intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hii
  -- |φ 1 - φ 0| ≤ ∫_Ioc g
  have hIoc : ∫ t in (0:ℝ)..1, φ' t = ∫ t in Set.Ioc (0:ℝ) 1, φ' t :=
    intervalIntegral.integral_of_le (by norm_num)
  have hgintIoc : IntegrableOn g (Set.Ioc (0:ℝ) 1) :=
    hgint.mono_set Set.Ioc_subset_Icc_self
  have hφ'intIoc : IntegrableOn φ' (Set.Ioc (0:ℝ) 1) :=
    hφ'int.mono_set Set.Ioc_subset_Icc_self
  have habs : |φ 1 - φ 0| ≤ ∫ t in Set.Ioc (0:ℝ) 1, g t := by
    rw [← hftc, hIoc, ← Real.norm_eq_abs]
    calc ‖∫ t in Set.Ioc (0:ℝ) 1, φ' t‖ ≤ ∫ t in Set.Ioc (0:ℝ) 1, ‖φ' t‖ :=
          norm_integral_le_integral_norm _
      _ ≤ ∫ t in Set.Ioc (0:ℝ) 1, g t := by
          refine setIntegral_mono_on hφ'intIoc.norm hgintIoc measurableSet_Ioc (fun t ht => ?_)
          exact hbound t (Set.Ioc_subset_Icc_self ht)
  -- bridge real integral to lintegral
  have hgnnIoc : 0 ≤ᵐ[volume.restrict (Set.Ioc (0:ℝ) 1)] g :=
    (ae_restrict_iff' measurableSet_Ioc).mpr
      (ae_of_all _ (fun t ht => div_nonneg (norm_nonneg _)
        (le_of_lt (hγ.mem t (Set.Ioc_subset_Icc_self ht)))))
  have hbridge : ENNReal.ofReal (∫ t in Set.Ioc (0:ℝ) 1, g t)
      = ∫⁻ t in Set.Icc (0:ℝ) 1, ENNReal.ofReal (g t) := by
    rw [ofReal_integral_eq_lintegral_ofReal hgintIoc hgnnIoc]
    exact MeasureTheory.setLIntegral_congr Ioc_ae_eq_Icc
  -- assemble
  have : ENNReal.ofReal |φ 1 - φ 0| ≤ ENNReal.ofReal (∫ t in Set.Ioc (0:ℝ) 1, g t) :=
    ENNReal.ofReal_le_ofReal habs
  rw [hbridge] at this
  have hφ1 : φ 1 = Real.log ((y) 2) := by rw [hφ]; simp only []; rw [hγ.target]
  have hφ0 : φ 0 = Real.log ((x) 2) := by rw [hφ]; simp only []; rw [hγ.source]
  rw [hφ1, hφ0] at this
  exact this


/-- **`dH` dominates the vertical log-drop** — `ofReal |log(y₂/x₂)| ≤ dH x y`. -/
theorem dH_ge_logHeight (x y : E) :
    ENNReal.ofReal |Real.log ((y) 2) - Real.log ((x) 2)| ≤ dH x y :=
  le_iInf₂ (fun _ hγ => pathLenH_ge_logHeight hγ)

/-- **Height-coordinate separation** (unconditional): `dH x y = 0` forces the
heights to agree, `y₂ = x₂`.  The vertical half of the full separation axiom. -/
theorem dH_eq_zero_height {x y : E} (hx : x ∈ upperH) (hy : y ∈ upperH)
    (h : dH x y = 0) : (y) 2 = (x) 2 := by
  have hle := dH_ge_logHeight x y
  rw [h, nonpos_iff_eq_zero, ENNReal.ofReal_eq_zero] at hle
  have hd : Real.log ((y) 2) - Real.log ((x) 2) = 0 := abs_nonpos_iff.mp hle
  have hlog : Real.log ((y) 2) = Real.log ((x) 2) := by linarith
  calc (y) 2 = Real.exp (Real.log ((y) 2)) := (Real.exp_log hy).symm
    _ = Real.exp (Real.log ((x) 2)) := by rw [hlog]
    _ = (x) 2 := Real.exp_log hx

end QOU.Archimedean.HyperbolicMetric
