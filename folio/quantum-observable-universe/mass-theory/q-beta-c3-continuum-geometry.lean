import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.Analysis.SpecialFunctions.Integrability.Basic
import Mathlib.Analysis.SpecialFunctions.Integrability.LogMeromorphic
import Mathlib.Tactic

/-!
# Continuum Geometry of the $c_3$ Mass Gap

This file formalizes the connection between the discrete $c_3$ topological mass gap 
(extracted empirically from the N=3 operator-valued $Q_\beta$ topology) and the 
continuous geometric hyperbolic volume of the $4_1$ (pion) knot.

Following the exact analytical evaluation of the Faddeev non-compact integration:
1. The continuum limit of the topological state sum converges to the imaginary 
   part of the dilogarithm $V(\theta) = \text{Im}(\text{Li}_2(e^{i\theta}))$.
2. The thermodynamic saddle point of this continuous action occurs strictly at 
   the cyclotomic root $\theta = \pi/3$.
3. The evaluation of $V(\pi/3)$ geometrically constructs the volume of a 
   regular ideal tetrahedron.
4. The continuum mass gap identically limits to $-\text{Vol}(4_1)$.

The continuum geometry below is real and kept. (The earlier framing that this
"rejects the $c_3 = -2$ shadow as a hallucination" is **withdrawn** — see the
CORRECTION note below: $c_3 = -2 = J_{\mathrm{Hopf}}(1)$ is the *canonical* $q=1$
shadow (registry KC10/KC20), and the $c_3 = -\mathrm{Vol}(4_1)$ identification is
over-scoped/anchor-blind. Only the hyperbolic geometry is retained.)

**⚠ CORRECTION (2026-07-11).** The *geometry* below (Lobachevsky derivative,
saddle at $\pi/3$, $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$) is correct.
But (a) the physical identification "$c_3$ limits to $-\mathrm{Vol}(4_1)$" is
**over-scoped**: $-\mathrm{Vol}(4_1) = -2.02988$ is anchor-blind and misses both
substrate anchors (muon +0.48%, proton −1.91%) while $c_3$ swings 2.43% — it is
NOT $c_3$'s limit (see the audit). (b) $c_3 = -2 = J_{\mathrm{Hopf}}(1)$ is the
**canonical** $q=1$ shadow (registry KC10 / KC20), NOT a "hallucination." Ref:
`docs/audits/2026-07-11-gemini-session-c3-overclaim-continuum-and-lean-audit.md`.

**Items (c) and (d) of the 2026-07-11 note are DISCHARGED (2026-08-23).** They
read, correctly at the time: (c) `log_integrable` / `f_integrable` are `axiom`s
changed from `lemma` to make the file compile; (d) the capstone
`c3_continuum_limit_is_hyperbolic_volume` is `: True := by trivial`, carrying its
physical claim only in its name. Neither holds now — the file declares **no**
`axiom`, that capstone no longer exists, and every declaration here is
sorry-free with `#print axioms` = {propext, Classical.choice, Quot.sound}. They
are kept above because a correction that silently disappears is worse than one
that is marked spent.

**The file did not COMPILE until 2026-08-23**, which is how the stale note
survived: `intervalIntegrable_log'` lives in the `intervalIntegral` namespace,
and the `convert` in `f_integrable` left a `log (2 * |s|) = log (2 * s)` goal
that `simp` could not close (`Real.log` already factors through `|·|`, so it
needs `← Real.log_abs` and `abs_mul`, not `Real.log_abs`). Nothing caught
either: this `.lean` is a content-block sibling whose block has **no `.ts`
manifest**, so no gate ever built it. Bean `qou-cauj`.
-/

namespace QOU.MassTheory.ContinuumGeometry

open Complex Real
open scoped Interval

/-- The Lobachevsky function (the imaginary part of the quantum dilogarithm), 
    representing the continuous classical potential of the Faddeev integral.
    Defined formally via Mathlib interval integrals. -/
noncomputable def classical_potential (θ : ℝ) : ℝ :=
  - ∫ t in (0 : ℝ)..θ, Real.log |2 * Real.sin (t / 2)|

/-- Lemma 1.1: The singularity of the Lobachevsky integrand at t=0 is bounded by the natural logarithm. 
    This is the core asymptotic bound required for the improper Lebesgue integral. -/
lemma f_integrable_bound (t : ℝ) (h : 0 < t ∧ t < 2 * π) :
  Real.log |2 * Real.sin (t / 2)| ≤ Real.log t := by
  have h_sin_pos : 0 < Real.sin (t / 2) := by
    apply Real.sin_pos_of_mem_Ioo
    constructor
    · linarith
    · linarith
  have h_abs : |2 * Real.sin (t / 2)| = 2 * Real.sin (t / 2) := by
    apply abs_of_pos
    linarith
  rw [h_abs]
  have h_inside_pos : 0 < 2 * Real.sin (t / 2) := by linarith
  have h_t_pos : 0 < t := h.1
  apply (Real.log_le_log_iff h_inside_pos h_t_pos).mpr
  have h_sin_le : Real.sin (t / 2) ≤ t / 2 := Real.sin_le (by linarith)
  linarith

/-- Lemma 1.2: The natural logarithm is improperly integrable at 0.
    Proved using Mathlib's `intervalIntegrable_log'` which handles the
    singularity at 0 via dominated convergence. -/
theorem log_integrable (θ : ℝ) (_h : 0 < θ) :
  IntervalIntegrable (fun t => Real.log t) MeasureTheory.volume 0 θ :=
  intervalIntegral.intervalIntegrable_log'

/-- Lemma 1: The singularity of the Lobachevsky integrand at t=0 is integrable.
    The integrand `log|2 sin(t/2)|` decomposes as `log 2 + log|sin(t/2)|`.
    Mathlib's `intervalIntegrable_log_sin` handles `log ∘ sin` for any
    endpoints; the constant `log 2` is trivially integrable. -/
theorem f_integrable (θ : ℝ) (_h : 0 < θ ∧ θ < 2 * π) :
  IntervalIntegrable (fun t => Real.log |2 * Real.sin (t / 2)|) MeasureTheory.volume 0 θ := by
  -- The function t ↦ 2 * sin(t/2) is analytic, hence meromorphic.
  -- MeromorphicOn.intervalIntegrable_log gives log ∘ f is integrable for meromorphic f.
  -- We rewrite our integrand as (log ∘ ‖·‖) ∘ (fun t => 2 * sin(t/2)).
  have hm : MeromorphicOn (fun t : ℝ => (2 : ℝ) * Real.sin (t / 2)) [[0, θ]] := by
    intro x _
    exact ((analyticAt_const.mul (Real.analyticAt_sin.comp
      (analyticAt_id.div analyticAt_const (by norm_num)))).meromorphicAt)
  convert hm.intervalIntegrable_log using 1
  ext t
  -- `log (2 * |s|) = log (2 * s)`: Mathlib's `Real.log` already factors through
  -- `|·|` (`Real.log_abs`), so push the abs outward and discharge `|2| = 2`.
  rw [Function.comp_apply, ← Real.log_abs (2 * Real.sin (t / 2)), abs_mul,
    abs_two]

lemma f_measurable_global :
  Measurable (fun t : ℝ => Real.log |2 * Real.sin (t / 2)|) := by
  measurability

/-- Lemma 2: The integrand is strongly measurable around the evaluation point. 
    (Derived strictly from its global measurability). -/
lemma f_measurable (θ : ℝ) :
  StronglyMeasurableAtFilter (fun t => Real.log |2 * Real.sin (t / 2)|) (nhds θ) MeasureTheory.volume := by
  apply MeasureTheory.StronglyMeasurable.stronglyMeasurableAtFilter
  exact f_measurable_global.stronglyMeasurable

/-- Lemma 3: The integrand is continuous strictly inside the topological domain 
    (avoiding the roots of unity at 0 and 2π). -/
lemma f_continuousAt (θ : ℝ) (h : 0 < θ ∧ θ < 2 * π) :
  ContinuousAt (fun t => Real.log |2 * Real.sin (t / 2)|) θ := by
  have h_inside_pos : 0 < |2 * Real.sin (θ / 2)| := by
    rw [abs_pos]
    intro h_eq
    have : Real.sin (θ / 2) = 0 := by linarith
    have h_sin_pos : 0 < Real.sin (θ / 2) := by
      apply Real.sin_pos_of_mem_Ioo
      constructor
      · linarith
      · linarith
    linarith
  refine ContinuousAt.log ?_ (by linarith)
  refine ContinuousAt.abs ?_
  refine ContinuousAt.mul continuousAt_const ?_
  exact Real.continuous_sin.continuousAt.comp (Continuous.continuousAt (continuous_id.div_const 2))

/-- The fundamental derivative of the classical topological potential 
    forces the continuous saddle-point geometry. 
    (Verified by reducing to Mathlib's interval integral FTC). -/
theorem potential_derivative (θ : ℝ) (h : 0 < θ ∧ θ < 2 * π) :
  deriv classical_potential θ = - Real.log |2 * Real.sin (θ / 2)| := by
  -- Unfold to the formal interval integral definition
  unfold classical_potential
  
  -- The derivative of -∫ is the negative of the derivative of ∫
  have h_deriv_neg : deriv (fun u => - ∫ t in (0:ℝ)..u, Real.log |2 * Real.sin (t / 2)|) θ = 
    - deriv (fun u => ∫ t in (0:ℝ)..u, Real.log |2 * Real.sin (t / 2)|) θ := by
    exact deriv.neg
    
  rw [h_deriv_neg]
  
  -- Apply the Fundamental Theorem of Calculus from Mathlib
  have h_ftc := intervalIntegral.deriv_integral_right (f_integrable θ h) (f_measurable θ) (f_continuousAt θ h)
  rw [h_ftc]

/-- The analytical saddle point bounding the non-compact contour integration 
    is rigorously pinned to the $\pi/3$ root. -/
theorem saddle_point_root : deriv classical_potential (π / 3) = 0 := by
  have h_bounds : 0 < π / 3 ∧ π / 3 < 2 * π := by
    constructor
    · positivity
    · linarith [Real.pi_pos]
  rw [potential_derivative _ h_bounds]
  have h_sin : Real.sin (π / 3 / 2) = 1 / 2 := by
    have : π / 3 / 2 = π / 6 := by ring
    rw [this, Real.sin_pi_div_six]
  rw [h_sin]
  have h_abs : |2 * (1 / 2 : ℝ)| = 1 := by norm_num
  rw [h_abs]
  have : Real.log 1 = 0 := Real.log_one
  rw [this, neg_zero]

/-- The geometric volume of a regular ideal tetrahedron evaluates identically 
    to the critical saddle limit. -/
noncomputable def vol_regular_ideal_tetrahedron : ℝ :=
  classical_potential (π / 3)

/-- The hyperbolic volume of the $4_1$ (figure-eight) knot manifold, built 
    from exactly two regular ideal tetrahedra. -/
noncomputable def vol_4_1 : ℝ :=
  2 * vol_regular_ideal_tetrahedron

/-- **The retained continuum geometry.**  Only the geometry is kept; the
    earlier physical identification "$c_3$ limits to $-\mathrm{Vol}(4_1)$" is
    **withdrawn as over-scoped** (anchor-blind — see the ⚠ CORRECTION note
    above; and $c_3 = -2 = J_{\mathrm{Hopf}}(1)$ is the canonical $q=1$
    shadow, not $-\mathrm{Vol}(4_1)$).  What *is* true, and is recorded here
    (replacing the former vacuous `: True` placeholder that carried the false
    $c_3$ claim only in its name), is the geometric decomposition:

    - the figure-8 volume `Vol(4₁)` is exactly twice the regular-ideal-
      tetrahedron volume `Λ(π/3)` (built from two ideal tetrahedra), and
    - that tetrahedron volume sits at the `π/3` cyclotomic saddle point of
      the continuum action (`deriv classical_potential (π/3) = 0`,
      `saddle_point_root`). -/
theorem vol_4_1_is_twice_tetrahedron_at_saddle :
    vol_4_1 = 2 * classical_potential (π / 3) ∧
    deriv classical_potential (π / 3) = 0 :=
  ⟨rfl, saddle_point_root⟩

end QOU.MassTheory.ContinuumGeometry
