/-
  `Real.sqrt` bracket on `substrate_q`, split out of
  `QOU.MassTheory.MassDerivation`.  Same namespace, original names kept.
-/
import QOU.MassTheory.MassDerivation
import QOU.Transcendental.RpowSqrtHelpers

namespace QOU.MassDerivation

/-! ### Substrate-`q` `Real.sqrt` bracket

The numerical witness `1.05341 < Real.sqrt substrate_q < 1.05343`
discharges the half-denominator
`Real.sqrt substrate_q + 1 / Real.sqrt substrate_q ≈ 2.00228`
required by every QOU pair-skein bound. -/

/-- `Real.sqrt substrate_q > 1.05341`. Proof: `1.05341² ≈
    1.10967 < 1.1097`, so by monotonicity of `Real.sqrt`. -/
lemma sqrt_substrate_q_gt :
    (1.05341 : ℝ) < Real.sqrt substrate_q := by
  apply QOU.MathlibExt.Real.lt_sqrt_of_sq_lt
  · norm_num
  · unfold substrate_q
    norm_num

/-- `Real.sqrt substrate_q < 1.05343`. Proof: `1.05343² ≈
    1.1097148 > 1.1097`, so by monotonicity of `Real.sqrt`.
    (The previous bound `1.05342` was false: `1.05342² ≈ 1.1096937
    < 1.1097`, i.e. `√substrate_q ≈ 1.0534228` exceeds it.) -/
lemma sqrt_substrate_q_lt :
    Real.sqrt substrate_q < 1.05343 := by
  apply QOU.MathlibExt.Real.sqrt_lt_of_lt_sq
  · norm_num
  · unfold substrate_q; norm_num
  · unfold substrate_q
    norm_num

/-- Two-sided bracket on `Real.sqrt substrate_q`. -/
lemma sqrt_substrate_q_bracket :
    (1.05341 : ℝ) < Real.sqrt substrate_q ∧
    Real.sqrt substrate_q < 1.05343 :=
  ⟨sqrt_substrate_q_gt, sqrt_substrate_q_lt⟩

end QOU.MassDerivation
