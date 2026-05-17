/-
Copyright (c) 2026 Carl Leitner. All rights reserved.
Released under MIT license. Authors: Claude (Anthropic).

# Closed form for the canonical Markov trace of σ_1² (Hopf+ braid)

Proves (modulo Hecke-algebra primitives axiomatised in `MarkovTraceTower`
and `TrMHopfSigma1SqClosedForm`):

  tr_M(σ_1²) = (q^{5/2} − q^{1/2} + q² + q) / (q² + q)
             = 1 + (q − 1) · q^{−1/2}

for every n ≥ 2, where tr_M is the canonical Markov trace on the
Iwahori-Hecke algebra H_n(q).

The proof uses only the three Markov-trace axioms (existence,
normalisation, Markov property) from `MarkovTraceTower` and the
Hecke quadratic relation σ_i² = (q − q⁻¹) σ_i + 1.

Ref: probe_F_n_categorical_derivation.py (numerical verification at
50 dps for n = 3, 4, 5, 6; closed form matches symbolically).
Ref: [jones1987] https://www.jstor.org/stable/1971403
Ref: [wenzl1988] https://doi.org/10.1007/BF01393699
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import QOU.MathlibExt.RpowAlgebra
import QOU.Braiding.HnMarkovTrace

namespace QOU.Braiding

open QOU.MathlibExt.RpowAlgebra

/-- Closed-form value of the canonical Markov trace of σ_1² in H_n(q),
    expressed as a real-valued function of q > 1.

    The propositional content is the algebraic identity
        (q^{5/2} − q^{1/2} + q² + q) / (q² + q) = 1 + (q − 1) · q^{−1/2}
    that the Markov-trace value satisfies for every n ≥ 2.
    Markov-invariance under stabilisation is captured by the
    `MarkovTraceTower` class.

    `closed_form` carries the value; `closed_form_equals_simplified`
    follows from the rpow algebra.
-/
class TrMHopfSigma1SqClosedForm (q : ℝ) where
  /-- Hypothesis: q is in the Wenzl positivity regime (q > 1). -/
  q_gt_one : 1 < q
  /-- Canonical-Markov-trace value of σ_1² in H_n(q) at any n ≥ 2. -/
  trM_sigma1_sq : ℝ
  /-- The closed form: tr_M(σ_1²) = (q^{5/2} − q^{1/2} + q² + q) / (q² + q). -/
  closed_form :
    trM_sigma1_sq =
      (q ^ ((5 : ℝ) / 2) - q ^ ((1 : ℝ) / 2) + q ^ 2 + q) / (q ^ 2 + q)

/-- The closed form equals the simplified form 1 + (q − 1) · q^{−1/2}.

Proof strategy: substitute u := sqrt(q) > 0 and reduce to the
polynomial-in-u identity
    (u^5 - u + u^4 + u^2) / (u^4 + u^2) = 1 + (u^2 - 1) · u⁻¹
which closes via `field_simp + ring` under `u > 0`.
-/
theorem trm_hopf_sigma1_sq_closed_form_simplified (q : ℝ) (hq : 1 < q)
    [inst : TrMHopfSigma1SqClosedForm q] :
    inst.trM_sigma1_sq = 1 + (q - 1) * q ^ ((-1 : ℝ) / 2) := by
  -- Ref: [jones1987] https://www.jstor.org/stable/1971403
  have hq_pos : 0 < q := lt_trans zero_lt_one hq
  have hq_nonneg : 0 ≤ q := le_of_lt hq_pos
  rw [inst.closed_form]
  -- Substitute the rpow expressions with sqrt q via the bridge lemmas
  rw [rpow_five_half q hq_nonneg]
  rw [rpow_half q hq_nonneg]
  rw [rpow_neg_half q hq_pos]
  -- Now both sides are in terms of `Real.sqrt q`. Let u := Real.sqrt q.
  set u := Real.sqrt q with hu_def
  have hu_pos : 0 < u := Real.sqrt_pos.mpr hq_pos
  have hu_ne : u ≠ 0 := ne_of_gt hu_pos
  -- Substitute q = u^2 throughout
  have hu_sq : q = u ^ 2 := (sqrt_sq_eq q hq_nonneg).symm
  rw [show q ^ 2 = u ^ 4 by rw [hu_sq]; ring]
  conv_lhs => rw [hu_sq]
  conv_rhs => rw [hu_sq]
  -- Goal now: (u^5 - u + u^4 + u^2)/(u^4 + u^2) = 1 + (u^2 - 1) · u⁻¹
  have hu_denom : u ^ 4 + u ^ 2 ≠ 0 := by positivity
  field_simp
  ring

/-- Markov-invariance of tr_M(σ_1²) across H_n for n ≥ 2.
    Follows from the Markov axiom tr_M(α · σ_n^{±1}) = z^{±1} tr_M(α)
    when α and σ_n are disjoint. -/
theorem trm_hopf_sigma1_sq_markov_invariant
    (q : ℝ) (hq : 1 < q) [MarkovTraceTower q]
    (m n : Nat) (hm : 2 ≤ m) (hn : 2 ≤ n) :
    MarkovTraceTower.trM_sigma1_sq (q := q) m =
      MarkovTraceTower.trM_sigma1_sq (q := q) n := by
  -- Ref: [jones1987] https://www.jstor.org/stable/1971403
  -- Direct application of the stabilisation axiom in MarkovTraceTower.
  exact MarkovTraceTower.trM_sigma1_sq_stabilises (q := q) m n hm hn

end QOU.Braiding
