/-
Copyright (c) 2026 Carl Leitner. All rights reserved.
Released under MIT license. Authors: Claude (Anthropic).

# Closed form for the canonical Markov trace of σ_1² (Hopf+ braid)

Under convention D, `z = q³/(q²+1)`, the Markov axiom gives

  tr_M(σ_1²) = h·z + 1 = (q − q⁻¹)·q³/(q²+1) + 1 = (q⁴ + 1)/(q² + 1)

for every n ≥ 2, where tr_M is the canonical Markov trace on the
Iwahori-Hecke algebra H_n(q). The value is rational in `q`, so the
closed form is stated over a generic field `K` (§7c).

This module previously stated the convention-C value
`(q^{5/2} − q^{1/2} + q² + q)/(q² + q) = 1 + (q − 1)·q^{−1/2}`, which needs a
square root of `q`. Convention C is excised (owner ruling 2026-08-09); the
canonical `MarkovTraceTower` instance in `HeckeTemperleyLieb.HnMarkovTrace`
already carries `(q⁴ + 1)/(q² + 1)`, and the block's own author note asked for
this module to follow it onto a generic base.

Ref: [jones1987] https://www.jstor.org/stable/1971403
Ref: [wenzl1988] https://doi.org/10.1007/BF01393699
-/
import HeckeTemperleyLieb.HnMarkovTrace

namespace QOU.Braiding

/-- Closed-form value of the canonical (convention-D) Markov trace of σ_1² in
    H_n(q), over a generic field `K`.

    The propositional content is the algebraic identity
        (q⁴ + 1)/(q² + 1) = (q − q⁻¹)·q³/(q² + 1) + 1,
    i.e. the value is `h·z_D + 1` as the Markov axiom requires. -/
class TrMHopfSigma1SqClosedForm {K : Type*} [Field K] (q : K) where
  /-- Non-degeneracy: `q ≠ 0`. -/
  q_ne_zero : q ≠ 0
  /-- Non-degeneracy of the convention-D denominator: `q² + 1 ≠ 0`. -/
  q_sq_add_one_ne_zero : q ^ 2 + 1 ≠ 0
  /-- Canonical-Markov-trace value of σ_1² in H_n(q) at any n ≥ 2. -/
  trM_sigma1_sq : K
  /-- The closed form: tr_M(σ_1²) = (q⁴ + 1)/(q² + 1). -/
  closed_form : trM_sigma1_sq = (q ^ 4 + 1) / (q ^ 2 + 1)

/-- The closed form equals `h·z_D + 1`, with `h = q − q⁻¹` and
    `z_D = q³/(q² + 1)`. -/
theorem trm_hopf_sigma1_sq_closed_form_simplified {K : Type*} [Field K] (q : K)
    [inst : TrMHopfSigma1SqClosedForm q] :
    inst.trM_sigma1_sq = (q - q⁻¹) * (q ^ 3 / (q ^ 2 + 1)) + 1 := by
  rw [inst.closed_form]
  have h0 := inst.q_ne_zero
  have h1 := inst.q_sq_add_one_ne_zero
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
  exact MarkovTraceTower.trM_sigma1_sq_stabilises (q := q) m n hm hn

/-- Canonical concrete instance of `TrMHopfSigma1SqClosedForm q`, with the same
    value `(q⁴ + 1)/(q² + 1)` as the canonical `MarkovTraceTower` instance. -/
instance trMHopfSigma1SqClosedForm_canonical {K : Type*} [Field K] (q : K)
    (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) : TrMHopfSigma1SqClosedForm q where
  q_ne_zero := hq
  q_sq_add_one_ne_zero := hq2
  trM_sigma1_sq := (q ^ 4 + 1) / (q ^ 2 + 1)
  closed_form := rfl

/-- Agreement with the canonical Markov tower: for `q > 1`, the canonical tower's
    value of tr_M(σ_1²) at any level is the closed form. -/
theorem trm_hopf_sigma1_sq_eq_tower (q : ℝ) (hq : 1 < q) (n : Nat) :
    (markovTraceTower_canonical q hq).trM_sigma1_sq n = (q ^ 4 + 1) / (q ^ 2 + 1) :=
  rfl

end QOU.Braiding
