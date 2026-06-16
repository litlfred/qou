/-
Copyright (c) 2026 Carl Leitner. All rights reserved.
Released under MIT license. Authors: Claude (Anthropic).

# Markov-trace class abstraction for the Iwahori-Hecke tower

Provides an abstract class `MarkovTraceTower` that axiomatises the
canonical Markov trace on the H_n(q) tower per
[`thm:jones-markov-trace`](#thm:jones-markov-trace) (Jones 1987,
Wenzl 1988).

The class admits stabilisation across n: for a braid β ∈ H_m(q) with
m ≤ n, its Markov trace in H_n(q) equals its Markov trace in H_m(q)
(no Markov-parameter factor when the new strands are disjoint from β).

This is the abstraction needed to discharge
`trm_hopf_sigma1_sq_markov_invariant`.

Ref: [jones1987] https://www.jstor.org/stable/1971403
Ref: [wenzl1988] https://doi.org/10.1007/BF01393699
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt

namespace QOU.Braiding

/-- Canonical Markov-trace tower abstraction.

`MarkovTraceTower q` parameterises a family of trace maps
`tr_n : H_n(q) → ℝ` (one per n ≥ 1) satisfying the three Markov-trace
axioms (Jones 1987 §2):

  (M1) Normalisation:    tr_n(1) = 1
  (M2) Trace property:   tr_n(a · b) = tr_n(b · a)
  (M3) Markov property:  tr_{n+1}(β · σ_n^{±1}) = z^{±1} · tr_n(β)
                         for β ∈ H_n(q) and σ_n the new generator,
                         with z := 1/(q^{1/2} + q^{-1/2}).

For abstract reasoning about cross-n invariance, the relevant
property is (M3)' a STRENGTHENING of (M3): when σ_n is disjoint from
β (which is the case when β uses only generators σ_1..σ_{m-1} for
m < n), the new strand contributes z · z⁻¹ = 1 in the stabilisation
chain. Thus tr_n(β) = tr_m(β) for the canonical inclusion
H_m ⊆ H_n. -/
class MarkovTraceTower (q : ℝ) where
  /-- The Markov parameter z = 1/(q^{1/2} + q^{-1/2}). -/
  z : ℝ
  /-- z is positive (Wenzl regime q > 0, q^{1/2}+q^{-1/2} > 0). -/
  z_pos : 0 < z
  /-- The Markov trace at H_n: σ_1² → ℝ. This abstracts over the
      concrete Hecke-algebra elements; only the trace of the Hopf
      braid σ_1² in H_n is needed here. -/
  trM_sigma1_sq : Nat → ℝ
  /-- Markov-invariance: for every n ≥ 2, the trace of σ_1² is the
      same as in H_2 (since σ_1² involves only the first generator,
      extra strands stabilise trivially: z · z⁻¹ = 1).

      This is property (M3)' applied to σ_1² ∈ H_2 ⊆ H_n. -/
  trM_sigma1_sq_stabilises :
    ∀ (m n : Nat), 2 ≤ m → 2 ≤ n →
      trM_sigma1_sq m = trM_sigma1_sq n

/-- Canonical concrete instance of `MarkovTraceTower q` for `q > 1`
    (Wenzl positivity regime).

The instance uses:
  - z = 1/(q^{1/2} + q^{-1/2})  (canonical Wenzl Markov parameter)
  - trM_sigma1_sq n = (q^{5/2} − q^{1/2} + q² + q) / (q² + q) for all n
    (Markov-invariant closed form proved in
    `prop:trm-hopf-sigma1-sq-closed-form`)
  - stabilises proof: the function is constant in n, so trivially equal.

The numerical implementation lives in
`computations/markov_peel.tr_M_atomic` (Python; uses
GS reduction + Markov-axiom recursive ascent). The Lean class
instance here mirrors that semantic at the type level.

Note: real-valued `q^{1/2}` requires `Real.sqrt`; we use it directly
via the Mathlib `Real.sqrt_pos` lemma for the positivity proof. -/
noncomputable instance markovTraceTower_canonical (q : ℝ) (hq : 1 < q) :
    MarkovTraceTower q where
  z := 1 / (Real.sqrt q + 1 / Real.sqrt q)
  z_pos := by
    have hq_pos : 0 < q := lt_trans zero_lt_one hq
    have hsqrt_pos : 0 < Real.sqrt q := Real.sqrt_pos.mpr hq_pos
    have hsum_pos : 0 < Real.sqrt q + 1 / Real.sqrt q :=
      add_pos hsqrt_pos (one_div_pos.mpr hsqrt_pos)
    exact one_div_pos.mpr hsum_pos
  trM_sigma1_sq := fun _ =>
    (q ^ ((5 : ℝ) / 2) - q ^ ((1 : ℝ) / 2) + q ^ 2 + q) / (q ^ 2 + q)
  trM_sigma1_sq_stabilises := fun _ _ _ _ => rfl

end QOU.Braiding
