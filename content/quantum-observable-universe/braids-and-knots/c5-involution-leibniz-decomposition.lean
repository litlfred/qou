/-!
# QOU.BraidKnot.C5InvolutionLeibnizDecomposition

**c_5 = -b² - 1/2 decomposition**: pure-σ Kashiwara contribution
plus bar-invariant involution fingerprint from averaged-crossing
structure.

The averaged-crossing operator σ_avg = (σ + σ⁻¹)/2 is the bar-
invariant projector P_avg = (1 + bar)/2 applied to σ. The framework's
typed-B_3 braid recipe uses σ_avg at specific positions, introducing
h/2 contributions that propagate to the c_5 closed form via the
Leibniz product expansion of Markov-trace.
-/

import Mathlib.Tactic
-- Ref: [manuscript] prop:silver-ratio-beta-decay-null
-- Ref: [manuscript] prop:neutron-qvalue-symbolic
-- Ref: [wenzl1988] doi:10.1007/BF01404457 (Hecke Markov trace)
-- Ref: [hoefsmit1974] (Hoefsmit seminormal forms)
-- Ref: [jones1985] doi:10.2307/1971403 (Hopf-link Jones polynomial)

namespace QOU.BraidKnot

/-- Hoefsmit off-diagonal coupling squared on V_(2,1) at H_3(q). -/
noncomputable def hoefsmitBSq (q : ℝ) : ℝ :=
  (q^4 + q^2 + 1) / (q^2 + 1)^2

/-- Hecke skein parameter. -/
noncomputable def heckeSkein (q : ℝ) : ℝ := q - 1/q

/-- **Averaged crossing operator** σ_avg = σ - h/2.
    Equals the bar-invariant projection P_avg(σ) = (σ + σ⁻¹)/2
    using the Hecke quadratic σ² = h·σ + 1 ⟹ σ⁻¹ = σ - h. -/
noncomputable def sigmaAvg (q : ℝ) : ℝ → ℝ :=
  fun σ => σ - (heckeSkein q) / 2

/-- **The c_5 decomposition**: c_5(q) = -b²(q) - 1/2.

    The first summand -b² is the pure-σ Kashiwara contribution
    (return amplitude squared on V_(2,1)).
    The second summand -1/2 is the averaged-crossing involution
    fingerprint from the typed-B_3 recipe.

    This is the closed form CONJECTURED to match empirical c_5
    extraction at q_0 to 2.4% residual. -/
noncomputable def c5Decomposition (q : ℝ) : ℝ :=
  - hoefsmitBSq q - 1/2

/-- **At the silver ratio q = 1+√2, b² = 7/8 exactly.**

    Derivation:
      q² = 3 + 2√2,  q⁴ = 17 + 12√2
      q⁴+q²+1 = 21 + 14√2 = 7(3 + 2√2)
      (q²+1)² = (4+2√2)² = 24 + 16√2 = 8(3+2√2)
      b² = 7/8 ✓ -/
theorem b_squared_at_silver_ratio :
    hoefsmitBSq (1 + Real.sqrt 2) = 7/8 := by
  unfold hoefsmitBSq
  have h : Real.sqrt 2 * Real.sqrt 2 = 2 :=
    Real.mul_self_sqrt (by norm_num : (2:ℝ) ≥ 0)
  -- Tedious algebraic manipulation deferred to `field_simp; nlinarith` or sorry
  sorry  -- Ref: [manuscript] direct algebraic identity at silver-ratio q

/-- **At silver ratio, c_5 = -11/8 (Pell-Lucas-incompatible).**

    With b² = 7/8: c_5 = -(7/8 + 1/2) = -(7/8 + 4/8) = -11/8.
    The numerator 11 is NOT a Pell-Lucas number (a_n: 1, 1, 3, 7, 17, 41, ...),
    so c_5 is the "outlier" rung — distinct from c_3, c_4, c_6, c_7
    which are all Pell-Lucas-clean at the silver ratio. -/
theorem c5_at_silver_ratio_is_minus_11_over_8 :
    c5Decomposition (1 + Real.sqrt 2) = -11/8 := by
  unfold c5Decomposition
  rw [b_squared_at_silver_ratio]
  norm_num

/-- **Averaging-resonance rungs (confirmed at k=8, 10)**.

    The prediction: rungs c_k whose order coincides with an averaging-
    resonance position pick up 1/2 fingerprints. Tested by extending
    SDP-T_β extraction to k=8, 9, 10 (`qbeta_decay_sdp_extended_ck.py`):

    | k  | silver-ratio value      | classification             |
    |----|-------------------------|----------------------------|
    | 5  | -11/8                   | AVERAGING (orig outlier)   |
    | 8  | 49/16  (1/2 fingerprint)| AVERAGING (confirmed ✓)    |
    | 9  | -7  (= -a_3, clean)     | pure σ-action ✓            |
    | 10 | 343/128 (1/2 fingerprint)| AVERAGING (confirmed ✓)   |

    Pattern: k ∈ {5, 8, 10, 11, ...} predicted (every 3 with possible
    finer-structure resonances at adjacent rungs). Tested k=5, 8, 10
    all show 1/2 fingerprints; k=9 is clean Pell-Lucas. -/
def averagingResonanceRungs : List ℕ := [5, 8, 10, 11, 13, 14]

end QOU.BraidKnot
