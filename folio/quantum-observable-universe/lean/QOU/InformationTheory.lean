import QOU.Basic
import QOU.QuantumObservableUniverse
import Mathlib.Data.Real.Basic

/-!
# Chapter 9 — Information-Theoretic Perspective

Formalization of the information-theoretic perspective on the QOU from
Chapter 9 of the manuscript.

LaTeX source: `chapters/information-theory.tex`

## Structure

1. **Local Planck length** — minimal information unit `ℓ_P ∼ ℏ_q`
2. **Information transfer rate** — time as information transfer
3. **Cosmological regime conditions** — local conditions at a point;
   deep-quantum (`q → ∞`) and classical (`q → 1`) regimes.
   Existence of global initial/terminal states is NOT assumed.
-/


namespace QOU.InformationTheory

/-! ## §1  Local Planck Length -/

/-- **Local Planck length**: the minimal quantisable size of an
    information unit at a point `p ∈ M`, proportional to the quantum
    Planck constant `ℏ_q(p)`.

    LaTeX: `\label{sec:planck-info-unit}` -/
noncomputable def localPlanckLength {M : Type*} (sp : ArchimedeanSubstrateField M)
    (p : M) : ℝ :=
  quantumPlanckConstant sp p

/-- The local Planck length is non-negative. -/
theorem localPlanckLength_nonneg {M : Type*} (sp : ArchimedeanSubstrateField M)
    (p : M) : 0 ≤ localPlanckLength sp p :=
  quantumPlanckConstant_nonneg sp p

/-- The local Planck length vanishes at classicality (`q = 1`). -/
theorem localPlanckLength_classical {M : Type*} (sp : ArchimedeanSubstrateField M)
    (p : M) (hq : sp.field p = 1) :
    localPlanckLength sp p = 0 :=
  planck_classical_limit sp p hq

/-! ## §2  Information Transfer Rate -/

/-- **Information transfer rate**: quantifies the rate of information
    propagation at a point, proportional to `ℏ_q`.  Time slows at
    the classical regime (`q → 1`, rate → 0) and runs fast in the
    deep-quantum regime (`q → ∞`, rate → 1).

    LaTeX: `\label{sec:time-info}` -/
noncomputable def informationRate {M : Type*} (sp : ArchimedeanSubstrateField M)
    (p : M) : ℝ :=
  quantumPlanckConstant sp p

/-- The information rate is bounded in `[0, 1)`. -/
theorem informationRate_bounded {M : Type*} (sp : ArchimedeanSubstrateField M)
    (p : M) : 0 ≤ informationRate sp p ∧ informationRate sp p < 1 :=
  ⟨quantumPlanckConstant_nonneg sp p, quantumPlanckConstant_lt_one sp p⟩

/-! ## §3  Cosmological Regime Conditions

    These are **local** conditions on the substrate parameter at a
    single point p in an affine chart.  They describe what happens
    IF such a regime holds at p — not that it holds globally or that
    the universe reaches such a state.  Whether the sequence of
    configurations S_k terminates or extends infinitely in either
    direction is not assumed. -/

/-- **Deep-quantum regime** at a point: `q(p)` is large, corresponding
    to high torsion pressure and near-maximal information transfer rate
    (`ℏ_q → 1`).  This is the regime near a cosmological initial state
    (if one exists in the given affine chart).

    LaTeX: `\label{sec:big-bang-info}` -/
structure DeepQuantumRegime (M : Type*) where
  /-- The substrate parameter. -/
  sp : ArchimedeanSubstrateField M
  /-- The point where the regime holds. -/
  point : M
  /-- The deep-quantum threshold Q > 1 (e.g. Q = φ² ≈ 2.618). -/
  threshold : ℝ
  /-- The threshold exceeds classicality. -/
  threshold_gt_one : threshold > 1
  /-- `q(p) ≥ Q` at this point: genuinely deep-quantum. -/
  deep_quantum : sp.field point ≥ threshold

/-- **Classical regime** at a point: `q(p) = 1`, corresponding to
    vanishing torsion and zero information transfer.  This is the
    regime near a cosmological terminal state (if one exists in the
    given affine chart).  Its existence is not assumed globally.

    LaTeX: `\label{sec:big-bang-info}` (contrast) -/
structure ClassicalRegime (M : Type*) where
  /-- The substrate parameter. -/
  sp : ArchimedeanSubstrateField M
  /-- The point where the regime holds. -/
  point : M
  /-- `q(p) = 1` at this point (classicality). -/
  classical : sp.field point = 1

/-- At a point in the classical regime, the information rate vanishes. -/
theorem classical_regime_no_information {M : Type*} (cr : ClassicalRegime M) :
    informationRate cr.sp cr.point = 0 :=
  planck_classical_limit cr.sp cr.point cr.classical

/-- **Reciprocal relationship between the bare step `(q − 1) / q` and the time-step
factor `q / (q − 1)` (`qou-adwi`).**
Multiplying the bare step `(q − 1) / q` by `q / (q − 1)` yields `1`, and the complement
`1 − (q − 1) / q` equals `1 / q`. -/
theorem unit_product_vs_bare_step_ratio (q : ℝ) (hq0 : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    ((q - 1) / q) * (q / (q - 1)) = 1 ∧ 1 - (q - 1) / q = 1 / q := by
  constructor
  · field_simp
  · field_simp
    ring

/-- **In any `DeepQuantumRegime`, the substrate field strictly exceeds `1`.** -/
theorem deep_quantum_field_gt_one {M : Type*} (dqr : DeepQuantumRegime M) :
    1 < dqr.sp.field dqr.point := by
  have h1 : 1 < dqr.threshold := dqr.threshold_gt_one
  have h2 : dqr.threshold ≤ dqr.sp.field dqr.point := dqr.deep_quantum
  exact lt_of_lt_of_le h1 h2

/-- **Mutual exclusion of `DeepQuantumRegime` and `ClassicalRegime` at the same point.** -/
theorem deep_quantum_contradicts_classical {M : Type*}
    (dqr : DeepQuantumRegime M) (cr : ClassicalRegime M)
    (hsp : dqr.sp = cr.sp) (hpt : dqr.point = cr.point) : False := by
  have hgt : 1 < dqr.sp.field dqr.point := deep_quantum_field_gt_one dqr
  have heq : dqr.sp.field dqr.point = 1 := by
    rw [hsp, hpt, cr.classical]
  linarith

end QOU.InformationTheory
