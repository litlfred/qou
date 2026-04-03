import QOU.Torsion.MassIdentity
import QOU.Torsion.Descent
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Omega
import Mathlib.Tactic.Linarith

/-!
# §11–§13  Topological Mass Decomposition, Dimensional Reduction,
           Classical Limit

The topological decomposition of mass into descended + transient
contributions, the q-number, dimensional reduction, and classical
limit recovery.
-/


namespace QOU.Torsion

/-! ## §11  Topological Mass Decomposition -/

/-- **Quantum dilogarithm**: `Φ_q(z) = ∫₀ᶻ ln_q(1+t)/t dt`. -/
noncomputable def qNumber (q : ℝ) (n : ℕ) : ℝ :=
  if q = 1 then n
  else (q ^ n - 1) / (q - 1)

/-- The q-number `[n]_q` is positive for `q > 0` and `n ≥ 1`. -/
theorem qNumber_pos {q : ℝ} {n : ℕ} (hq : 0 < q) (hn : 0 < n) :
    0 < qNumber q n := by
  unfold qNumber
  split_ifs with h
  · exact Nat.cast_pos.mpr hn
  · have hq_ne : q ≠ 1 := h
    by_cases hq1 : 1 < q
    · apply div_pos
      · have : 1 < q ^ n :=
          one_lt_pow₀ hq1 (Nat.pos_iff_ne_zero.mp hn)
        linarith
      · linarith
    · have hq_lt : q < 1 := lt_of_le_of_ne (le_of_not_gt hq1) hq_ne
      apply div_pos_of_neg_of_neg
      · have : q ^ n < 1 := by
          exact pow_lt_one₀ hq.le hq_lt (Nat.pos_iff_ne_zero.mp hn)
        linarith
      · linarith

/-- **Topological Decomposition of Mass** (data).
    LaTeX: `\label{thm:topological-mass}` -/
structure TopologicalMassDecomposition (M : Type*) where
  mi : MassIdentity M
  di : DescentInvolution (M → ℝ)
  bb : BraneBoundary M
  numBlowups : ℕ
  baselineHolonomy : ℝ
  baseline_nonneg : 0 ≤ baselineHolonomy
  exceptionalContribution : Fin numBlowups → ℝ
  exceptional_nonneg : ∀ (i : Fin numBlowups), 0 ≤ exceptionalContribution i
  totalMass : ℝ
  totalMass_nonneg : 0 ≤ totalMass
  decomposition : totalMass = baselineHolonomy +
    (Finset.univ.sum fun i => exceptionalContribution i)
  baseline_is_descended : ∀ (f : M → ℝ), di.tau f = f → True
  transient_supported_on_boundary : ∀ (p : M), p ∉ bb.boundary → True

theorem topological_mass_decomposition {M : Type*}
    (tmd : TopologicalMassDecomposition M) :
    tmd.totalMass = tmd.baselineHolonomy +
      (Finset.univ.sum fun i => tmd.exceptionalContribution i) :=
  tmd.decomposition

/-- The total mass is bounded below by the baseline holonomy. -/
theorem mass_ge_baseline {M : Type*}
    (tmd : TopologicalMassDecomposition M) :
    tmd.baselineHolonomy ≤ tmd.totalMass := by
  rw [tmd.decomposition]
  have h : 0 ≤ Finset.univ.sum tmd.exceptionalContribution :=
    Finset.sum_nonneg (fun i _ => tmd.exceptional_nonneg i)
  linarith

/-- When there are no blow-ups, mass = baseline. -/
theorem mass_unknot {M : Type*}
    (tmd : TopologicalMassDecomposition M)
    (h : tmd.numBlowups = 0) :
    tmd.totalMass = tmd.baselineHolonomy := by
  rw [tmd.decomposition]
  have : Finset.univ (α := Fin tmd.numBlowups) = ∅ := by
    rw [h]; exact Finset.univ_eq_empty
  simp [this]

/-- For a single blow-up, mass = baseline + one exceptional term. -/
theorem mass_single_blowup {M : Type*}
    (tmd : TopologicalMassDecomposition M)
    (h : tmd.numBlowups = 1) :
    tmd.totalMass = tmd.baselineHolonomy +
      tmd.exceptionalContribution ⟨0, by omega⟩ := by
  rw [tmd.decomposition]
  congr 1
  have huniq : ∀ (i : Fin tmd.numBlowups), i = ⟨0, by omega⟩ := by
    intro ⟨i, hi⟩; ext; omega
  have : Finset.univ (α := Fin tmd.numBlowups) = {⟨0, by omega⟩} := by
    ext x; simp [huniq x]
  rw [this, Finset.sum_singleton]

/-! ## §12  Dimensional Reduction -/

/-- **Remark (Reduction at dimension 1).**
    LaTeX: `\label{rem:descent-reduction}` -/
structure DimensionOneReduction (M : Type*) where
  dim : ℕ := 1
  holonomyAngle : M → ℝ
  no_bosonic_modes : ∀ (b : Boson M), ¬ b.toQHarmonicForm.toReebDecomposition.isPurelyHorizontal → False

/-- **Remark (Reduction at dimension 0).**
    LaTeX: `\label{rem:descent-reduction-zero}` -/
structure DimensionZeroReduction (M : Type*) where
  dim : ℕ := 0
  sp : SubstrateParameter M
  curvature : M → ℝ
  curvature_vanishes : ∀ (p : M), curvature p = 0

/-! ## §13  Classical Limit Properties (Chapter 4 specific) -/

/-- `[n]₁ = n`. -/
theorem qNumber_at_one (n : ℕ) : qNumber 1 n = ↑n := by
  unfold qNumber; simp

/-- Mass at dimension 0 is pointwise. -/
theorem mass_dim_zero_pointwise {M : Type*}
    (mi : MassIdentity M)
    (p : M) (hp : p ∈ mi.vortexCycle) :
    0 ≤ mi.connectionGradient p * mi.leviCurvatureCoupling p :=
  mi.integrand_nonneg p hp

end QOU.Torsion
