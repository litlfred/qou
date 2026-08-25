/-
Empirical variance records for the depth-stratified Frobenius-reciprocity
conjecture — the **archimedean** half of the §7c split.

This module holds the measured, decimal-valued variance scoreboards that
accompany `QOU.BraidKnot.DepthStratifiedFrobeniusReciprocity`. They are
ordered comparisons of `ℝ` literals (empirical max/min ratios), so they sit
on the observation side of the substrate→archimedean wall and are separated
from the FR-weight algebra, which is stated over a generic
`{R : Type*} [Field R]` in the sibling module (AGENTS.md §7c: a block belongs
to the algebraic substrate or the archimedean specialisation, never both).

Ref: conj:depth-stratified-frobenius-reciprocity.md
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import QOU.BraidKnot.DepthStratifiedFrobeniusReciprocity

namespace QOU.BraidKnot

/-- Empirical record of falsifications.

    The |χ^λ|^β weighting (β ∈ [-2, 2]) was tested and gave
    variance worsening from 1.82× (uniform baseline) to 2.30-3.00×
    at β > 0, falsifying the simple magnitude-weight hypothesis.

    The self-conjugate restriction gave variance 5.94×,
    falsifying the Wenzl-bridge-stratum hypothesis.

    These observed variance values exceed the uniform baseline
    1.82×, recorded here as a verified comparison. -/
theorem fr_simpler_forms_variance_records :
    (1.82 : ℝ) < 2.30 ∧ (1.82 : ℝ) < 5.94 := by
  refine ⟨?_, ?_⟩ <;> norm_num

/-! ## Variance record across the categorical chain on PR #801 -/

/-- The variance scoreboard on PR #801: each baseline's max/min
    ratio is recorded.

    - tensor-product baseline (rejected): 3.96× — wrong sign on T/³He
    - mass-endomorphism blow-up (D/T/³He): 2.31×
    - depth-stratified α_k·Φ_k (D/T/³He/⁴He): 1.82× — best
    - block-multiplicative scaling (16 atoms): 5.47-10.99×

    The depth-stratified result is the tightest categorical
    structure on the chain; the FR refinement (this conjecture) is
    the proposed mechanism to close further. -/
theorem variance_ordering_records :
    (3.96 : ℝ) > 2.31 ∧ (2.31 : ℝ) > 1.82 ∧ (1.82 : ℝ) < 5.47 := by
  refine ⟨?_, ?_, ?_⟩ <;> norm_num

end QOU.BraidKnot
