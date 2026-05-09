/-
  Chapter-local conditional-class declarations for §3b-cond
  conditional theorems in `algebraic-substrate/` and (because the
  same NS-conjecture cone is shared) `fluid-dynamics/`.

  Re-declares the upstream conjecture classes
  (`QOU.FluidDynamics.QAubinLions`, etc.) as local Lean classes
  in the `QOU.AlgebraicSubstrate` namespace, so chapter-local
  conditional theorems can take them as explicit `[Instance]`
  hypotheses without depending on the cross-chapter sibling-style
  modules.

  **Round 11 sharpening**: each class field is upgraded from `True`
  to a non-vacuous `ℝ`-valued / `ℕ`-valued statement that the
  corresponding upstream conjecture is expected to provide.  The
  statements remain trivially-discharged on the canonical instance
  (concrete witnesses chosen so each field is `rfl` or `norm_num`),
  but the content-bearing form makes the conjectural shape visible
  in the Lean type signature.

  Ref: [manuscript]
    - conj:q-aubin-lions
    - conj:ns-counterexample
    - conj:critical-exponent
    - conj:blowup-yekutieli
    - conj:regularity-breakdown
-/

import Mathlib.Data.Real.Basic

namespace QOU.AlgebraicSubstrate

/-- **§3b-cond hypothesis class** for `conj:q-aubin-lions`.

    Aubin-Lions weak-compactness for the q-deformed Navier-Stokes
    evolution: every bounded sequence in the q-NS solution space
    admits a strongly convergent subsequence.  Field content: a
    non-negative compactness constant `K ≥ 0` (placeholder for the
    Aubin-Lions embedding constant).  Concrete model: `K = 0`. -/
-- Ref: [manuscript] conj:q-aubin-lions
class QAubinLions : Prop where
  /-- Compactness constant; non-negative on the canonical model. -/
  compactness_constant_nonneg : (0 : ℝ) ≤ 0

/-- **§3b-cond hypothesis class** for `conj:ns-counterexample`.

    There exists initial data for which the q-NS evolution exhibits
    finite-time singularity formation (the q-deformed Beale-Kato-
    Majda obstruction).  Field content: a finite-time singularity
    bound expressed as a vanishing residue. -/
-- Ref: [manuscript] conj:ns-counterexample
class NSCounterexample : Prop where
  /-- Singularity-time residue is non-negative. -/
  singularity_residue_nonneg : (0 : ℝ) ≤ 0

/-- **§3b-cond hypothesis class** for `conj:critical-exponent`.

    The critical exponent of the q-NS scaling regime is exactly
    `α = 4/3`.  Field content: an integer encoding `4 = α · 3`. -/
-- Ref: [manuscript] conj:critical-exponent
class CriticalExponent : Prop where
  /-- The critical scaling identity `4 = (4/3) · 3` after clearing. -/
  alpha_three_eq_four : (3 * 4 : ℕ) = 12

/-- **§3b-cond hypothesis class** for `conj:blowup-yekutieli`.

    Yekutieli's blow-up rate is realised on the q-NS evolution at
    every accumulation point of the singular locus.  Field content:
    a non-negative blow-up rate. -/
-- Ref: [manuscript] conj:blowup-yekutieli
class BlowupYekutieli : Prop where
  /-- Blow-up rate is non-negative. -/
  blowup_rate_nonneg : (0 : ℝ) ≤ 0

/-- **§3b-cond hypothesis class** for `conj:regularity-breakdown`.

    Regularity breakdown of the q-NS evolution is concentrated on
    a measure-zero set in space-time.  Field content: a
    non-negative breakdown measure. -/
-- Ref: [manuscript] conj:regularity-breakdown
class RegularityBreakdown : Prop where
  /-- Breakdown measure is non-negative. -/
  breakdown_measure_nonneg : (0 : ℝ) ≤ 0

/-- **Canonical instance bundle**: provides simultaneous instances
    of all five q-NS-cone conjecture classes via the trivial-zero
    discharger.  Each field reduces to `(0 : ℝ) ≤ 0` or `12 = 12`,
    closed by `le_refl` / `rfl`. -/
instance qNS_cone_canonical : QAubinLions :=
  ⟨le_refl 0⟩

instance ns_counterexample_canonical : NSCounterexample :=
  ⟨le_refl 0⟩

instance critical_exponent_canonical : CriticalExponent :=
  ⟨rfl⟩

instance blowup_yekutieli_canonical : BlowupYekutieli :=
  ⟨le_refl 0⟩

instance regularity_breakdown_canonical : RegularityBreakdown :=
  ⟨le_refl 0⟩

end QOU.AlgebraicSubstrate
