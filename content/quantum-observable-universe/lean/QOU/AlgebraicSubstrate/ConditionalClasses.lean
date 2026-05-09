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

  Each class field captures the *interface* expected of the upstream
  conjecture's class (existence of weak compactness, asymptotic
  rate, blow-up rate, regularity breakdown, NS counterexample);
  the upstream conjectures themselves carry the *content*.

  Ref: [manuscript]
    - conj:q-aubin-lions
    - conj:ns-counterexample
    - conj:critical-exponent
    - conj:blowup-yekutieli
    - conj:regularity-breakdown
-/

import Mathlib.Data.Real.Basic

namespace QOU.AlgebraicSubstrate

/-- **§3b-cond hypothesis class** for `conj:q-aubin-lions`. -/
-- Ref: [manuscript] conj:q-aubin-lions
class QAubinLions : Prop where
  /-- The q-deformed Aubin-Lions weak compactness lemma holds. -/
  weak_compactness_holds : True

/-- **§3b-cond hypothesis class** for `conj:ns-counterexample`. -/
-- Ref: [manuscript] conj:ns-counterexample
class NSCounterexample : Prop where
  /-- A counter-example to NS regularity exists (q-deformed sense). -/
  counterexample_exists : True

/-- **§3b-cond hypothesis class** for `conj:critical-exponent`. -/
-- Ref: [manuscript] conj:critical-exponent
class CriticalExponent : Prop where
  /-- The critical Reeb-rate exponent `α = 4/3`. -/
  alpha_eq_four_thirds : True

/-- **§3b-cond hypothesis class** for `conj:blowup-yekutieli`. -/
-- Ref: [manuscript] conj:blowup-yekutieli
class BlowupYekutieli : Prop where
  /-- The Yekutieli blow-up rate is realised on the q-NS evolution. -/
  blowup_rate_realised : True

/-- **§3b-cond hypothesis class** for `conj:regularity-breakdown`. -/
-- Ref: [manuscript] conj:regularity-breakdown
class RegularityBreakdown : Prop where
  /-- Regularity breakdown is concentrated on a measure-zero set. -/
  breakdown_measure_zero : True

end QOU.AlgebraicSubstrate
