/-
# HyperbolicGeodesicZAxis.lean (WALL-3, upper bound) — the vertical z-axis segment
# realises hyperbolic length `|log(b/a)|`, DERIVED.

The 1-D core of geodesic uniqueness in `H³`.  Between two z-axis points
`(0,0,a)` and `(0,0,b)` (`a,b > 0`) the vertical segment
`γ(t) = (0,0, a·(b/a)^t)` — written here as `single 2 (exp(log a + t·(log b −
log a)))` — is an admissible path of CONSTANT hyperbolic speed `|log b − log a|`,
hence of hyperbolic length exactly `|log b − log a| = |log(b/a)|`.  This gives the
**existence / upper bound** half of the z-axis distance formula:

    dH (0,0,a) (0,0,b) ≤ ofReal |log(b/a)|.

The matching lower bound `dH ≥ |log(b/a)|` is the genuine calculus-of-variations
crux (an FTC/`lintegral` argument bounding every admissible path below by the
z-displacement of `log z`); it is tracked as a bean, NOT stubbed — this file stays
100 % sorry-free.

Archimedean (ℝ): `exp`, `log`, `‖·‖`, ordering `0 < z` — §7c.

  -- Ref: [thurston1978] Ch. 2 §2.3 p. 12 (the metric, vertical geodesics)
  -- Ref: [ratcliffe] §4.6 (geodesics of `H³`; the z-axis is a geodesic)
  -- Ref: [leitner2026] beans qou-6eco (T2 WALL-3), qou-473l (T2), qou-idvt (T2)
-/

import QOU.Archimedean.HyperbolicMetric
import QOU.Archimedean.HyperbolicIsometryAffine
import Mathlib.Analysis.SpecialFunctions.Log.Deriv

namespace QOU.Archimedean

open QOU.Archimedean.HyperbolicMetric
open MeasureTheory Set
open scoped ENNReal

/-- **`single 2` as a continuous linear map** `ℝ →L[ℝ] E` — the injection of the
height coordinate into `H³`'s carrier, used to differentiate z-axis paths. -/
noncomputable def single2CLM : ℝ →L[ℝ] E :=
  ((WithLp.linearEquiv 2 ℝ (Fin 3 → ℝ)).symm.toLinearMap.comp
    (LinearMap.single ℝ (fun _ : Fin 3 => ℝ) 2)).toContinuousLinearMap

@[simp] theorem single2CLM_apply (c : ℝ) : single2CLM c = EuclideanSpace.single 2 c := rfl

/-- A **z-axis point** `(0,0,a)`. -/
noncomputable def zpt (a : ℝ) : E := EuclideanSpace.single 2 a

@[simp] theorem zpt_height (a : ℝ) : (zpt a) 2 = a := by
  simp [zpt, EuclideanSpace.single_apply]

theorem zpt_mem {a : ℝ} (ha : 0 < a) : zpt a ∈ upperH := by
  rw [mem_upperH, zpt_height]; exact ha

/-- The **log-interpolation exponent** `log a + t·(log b − log a)`. -/
noncomputable def logInterp (a b t : ℝ) : ℝ := Real.log a + t * (Real.log b - Real.log a)

/-- The **height profile** `f(t) = exp(log a + t·(log b − log a)) = a·(b/a)^t`. -/
noncomputable def heightProfile (a b t : ℝ) : ℝ := Real.exp (logInterp a b t)

theorem heightProfile_pos (a b t : ℝ) : 0 < heightProfile a b t := Real.exp_pos _

@[simp] theorem heightProfile_zero {a b : ℝ} (ha : 0 < a) : heightProfile a b 0 = a := by
  simp only [heightProfile, logInterp, zero_mul, add_zero]; exact Real.exp_log ha

@[simp] theorem heightProfile_one {a b : ℝ} (hb : 0 < b) : heightProfile a b 1 = b := by
  simp only [heightProfile, logInterp, one_mul]
  rw [add_sub_cancel]; exact Real.exp_log hb

/-- The derivative of the log-interpolation exponent is the constant slope
`log b − log a`. -/
theorem hasDerivAt_logInterp (a b t : ℝ) :
    HasDerivAt (logInterp a b) (Real.log b - Real.log a) t := by
  unfold logInterp
  have h : HasDerivAt (fun t : ℝ => t * (Real.log b - Real.log a))
      (Real.log b - Real.log a) t := by
    simpa using (hasDerivAt_id t).mul_const (Real.log b - Real.log a)
  simpa using h.const_add (Real.log a)

/-- The derivative of the height profile: `f'(t) = (log b − log a)·f(t)`. -/
theorem hasDerivAt_heightProfile (a b t : ℝ) :
    HasDerivAt (heightProfile a b)
      ((Real.log b - Real.log a) * heightProfile a b t) t := by
  have h := (hasDerivAt_logInterp a b t).exp
  simpa [heightProfile, mul_comm] using h

/-- **The vertical z-axis segment** `γ(t) = (0,0, f(t))` from `(0,0,a)` to
`(0,0,b)`. -/
noncomputable def vseg (a b t : ℝ) : E := EuclideanSpace.single 2 (heightProfile a b t)

@[simp] theorem vseg_zero {a b : ℝ} (ha : 0 < a) : vseg a b 0 = zpt a := by
  simp [vseg, zpt, heightProfile_zero ha]

@[simp] theorem vseg_one {a b : ℝ} (hb : 0 < b) : vseg a b 1 = zpt b := by
  simp [vseg, zpt, heightProfile_one hb]

@[simp] theorem vseg_height (a b t : ℝ) : (vseg a b t) 2 = heightProfile a b t := by
  simp [vseg, EuclideanSpace.single_apply]

theorem vseg_mem (a b t : ℝ) : vseg a b t ∈ upperH := by
  rw [mem_upperH, vseg_height]; exact heightProfile_pos a b t

/-- The derivative of the vertical segment: `γ'(t) = (0,0, f'(t))`. -/
theorem hasDerivAt_vseg (a b t : ℝ) :
    HasDerivAt (vseg a b)
      (EuclideanSpace.single 2 ((Real.log b - Real.log a) * heightProfile a b t)) t := by
  have h1 : HasDerivAt (fun s => single2CLM (heightProfile a b s))
      (single2CLM ((Real.log b - Real.log a) * heightProfile a b t)) t :=
    single2CLM.hasFDerivAt.comp_hasDerivAt t (hasDerivAt_heightProfile a b t)
  simpa [vseg] using h1

theorem differentiableAt_vseg (a b t : ℝ) : DifferentiableAt ℝ (vseg a b) t :=
  (hasDerivAt_vseg a b t).differentiableAt

@[simp] theorem deriv_vseg (a b t : ℝ) :
    deriv (vseg a b) t
      = EuclideanSpace.single 2 ((Real.log b - Real.log a) * heightProfile a b t) :=
  (hasDerivAt_vseg a b t).deriv

/-- The Euclidean norm of the segment's velocity: `‖γ'(t)‖ = f(t)·|log b − log a|`. -/
theorem norm_deriv_vseg (a b t : ℝ) :
    ‖deriv (vseg a b) t‖ = heightProfile a b t * |Real.log b - Real.log a| := by
  rw [deriv_vseg, EuclideanSpace.norm_single, Real.norm_eq_abs, abs_mul,
    abs_of_pos (heightProfile_pos a b t), mul_comm]

/-- **The vertical segment has constant hyperbolic speed** `|log b − log a|`: the
height factor `f(t)` cancels between `‖γ'‖` and `z`. -/
theorem hypSpeed_vseg_eq (a b t : ℝ) :
    ‖deriv (vseg a b) t‖ / (vseg a b t) 2 = |Real.log b - Real.log a| := by
  rw [norm_deriv_vseg, vseg_height, mul_comm,
    mul_div_assoc, div_self (ne_of_gt (heightProfile_pos a b t)), mul_one]

/-- **The vertical segment is an admissible path** from `(0,0,a)` to `(0,0,b)`. -/
theorem admissiblePath_vseg {a b : ℝ} (ha : 0 < a) (hb : 0 < b) :
    AdmissiblePath (vseg a b) (zpt a) (zpt b) where
  source := vseg_zero ha
  target := vseg_one hb
  mem := fun t _ => vseg_mem a b t
  diff := fun t _ => differentiableAt_vseg a b t

/-- **The vertical segment's hyperbolic length is exactly `|log b − log a|`.**  The
integrand is the constant speed `|log b − log a|`, and `volume (Icc 0 1) = 1`. -/
theorem pathLenH_vseg (a b : ℝ) :
    pathLenH (vseg a b) 0 1 = ENNReal.ofReal |Real.log b - Real.log a| := by
  unfold pathLenH
  have hcongr : ∀ t ∈ Set.Icc (0 : ℝ) 1,
      ENNReal.ofReal (‖deriv (vseg a b) t‖ / (vseg a b t) 2)
        = ENNReal.ofReal |Real.log b - Real.log a| := by
    intro t _; rw [hypSpeed_vseg_eq]
  rw [setLIntegral_congr_fun measurableSet_Icc hcongr, setLIntegral_const]
  rw [Real.volume_Icc, sub_zero, ENNReal.ofReal_one, mul_one]

/-- **WALL-3 (upper bound / existence).** The hyperbolic distance between two
z-axis points is AT MOST `|log(b/a)|`, realised by the vertical segment. -/
theorem dH_zpt_le {a b : ℝ} (ha : 0 < a) (hb : 0 < b) :
    dH (zpt a) (zpt b) ≤ ENNReal.ofReal |Real.log (b / a)| := by
  have hle := dH_le_pathLenH (admissiblePath_vseg ha hb)
  rw [pathLenH_vseg] at hle
  rwa [Real.log_div (ne_of_gt hb) (ne_of_gt ha)]

/-- **WALL-3 (lower bound).** Every admissible path between two z-axis points has
hyperbolic length at least `|log(b/a)|`, so the distance is bounded below by it.
DERIVED by specialising the unconditional vertical log-drop bound
`dH_ge_logHeight` to the z-axis points, whose heights are exactly `a` and `b`. -/
theorem dH_zpt_ge {a b : ℝ} (ha : 0 < a) (hb : 0 < b) :
    ENNReal.ofReal |Real.log (b / a)| ≤ dH (zpt a) (zpt b) := by
  have h := dH_ge_logHeight (zpt a) (zpt b)
  rw [zpt_height, zpt_height] at h
  rwa [Real.log_div (ne_of_gt hb) (ne_of_gt ha)]

/-- **WALL-3 (exact z-axis distance).** `dH (0,0,a) (0,0,b) = |log(b/a)|`, from the
upper bound (`dH_zpt_le`, the vertical segment realises it) and the lower bound
(`dH_zpt_ge`, the FTC vertical log-drop).  The 1-D core of geodesic uniqueness:
the vertical segment is a genuine length-minimiser between z-axis points. -/
theorem dH_zpt {a b : ℝ} (ha : 0 < a) (hb : 0 < b) :
    dH (zpt a) (zpt b) = ENNReal.ofReal |Real.log (b / a)| :=
  le_antisymm (dH_zpt_le ha hb) (dH_zpt_ge ha hb)

/-- **The vertical segment is a length-minimiser** between two z-axis points: its
hyperbolic length equals `dH (zpt a) (zpt b)`.  (Existence of a minimiser on the
z-axis, DERIVED — the length equality is `pathLenH_vseg` matched to `dH_zpt`.) -/
theorem pathLenH_vseg_eq_dH {a b : ℝ} (ha : 0 < a) (hb : 0 < b) :
    pathLenH (vseg a b) 0 1 = dH (zpt a) (zpt b) := by
  rw [pathLenH_vseg, dH_zpt ha hb, Real.log_div (ne_of_gt hb) (ne_of_gt ha)]

/-! ### WALL-2 (partial) — one-point normalization to the z-axis

The full two-point normalization (bean `qou-0a0z`) reduces geodesic uniqueness
between two arbitrary points of `H³` to the z-axis case, and needs a boundary
inversion in addition to the boundary-similarity generators.  Its **one-point
half** is elementary and DERIVED here from WALL-1: a single point `p ∈ H³` is
carried to the z-axis point `(0,0,p_z)` by the horizontal translation by
`b = (0,0,p_z) − p` (its height is `p_z − p_z = 0`, so it is genuinely
horizontal), and that translation preserves `dH` (`dH_horizTranslation`). -/

/-- The horizontal displacement `zpt (p_z) − p` carrying `p` onto the z-axis is
horizontal (`_z = 0`). -/
theorem zAxisShift_height (p : E) : (zpt (p 2) - p) 2 = 0 := by
  rw [PiLp.sub_apply, zpt_height, sub_self]

/-- **WALL-2, one-point half (DERIVED).** Every point `p ∈ H³` is carried onto the
z-axis point `(0,0,p_z)` by a horizontal translation, which preserves `dH`.  This
is the elementary half of the normalization; the two-point reduction (bean
`qou-0a0z`) additionally requires a boundary inversion. -/
theorem exists_horizTranslation_to_zAxis (p : E) :
    ∃ b : E, b 2 = 0 ∧ p + b = zpt (p 2) ∧
      ∀ x y : E, dH (x + b) (y + b) = dH x y := by
  refine ⟨zpt (p 2) - p, zAxisShift_height p, ?_, ?_⟩
  · rw [add_sub_cancel]
  · exact fun x y => dH_horizTranslation (zAxisShift_height p) x y

end QOU.Archimedean
