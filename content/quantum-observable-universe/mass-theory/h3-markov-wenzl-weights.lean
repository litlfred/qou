/-
# `prop:h3-markov-wenzl-weights`

Closed-form Wenzl/Markov weights on H_3(q):
  y_(3)(q)   = [4]_q / [2]_q^3
  y_(2,1)(q) = 1 / [2]_q^2
  y_(1^3)(q) = 0   (identically — Temperley-Lieb quotient)

At q = 1: (1/2, 1/4, 0) — NOT uniform.  (An earlier draft claimed
uniformity via a bar-involution argument; that was wrong — the
Jones-normalised Markov trace is chiral, not invariant under the
sign-twist automorphism σ ↦ −q·σ⁻¹.  Caught in review.)

This file proves two structural kernels of the proposition:

1. `h3_tl_quotient_identity` — the algebraic identity
   [2]³ − 2[2] = [4] (in the symmetric q-integer convention
   [2] = q + q⁻¹, [4] = q³ + q + q⁻¹ + q⁻³), which is exactly the
   statement that y_(1^3) ≡ 0 is CONSISTENT with the Markov
   normalisation: the weight 1 − 2·y_(2,1) assigned to (3) lands on
   [4]/[2]³ identically.  Proved by field_simp + ring over ℝ.

2. `h3_markov_wenzl_weights` — the q = 1 evaluation: the weight
   vector (1/2, 1/4, 0) satisfies the Markov normalisation
   Σ_λ y_λ(1) · d_λ = (1/2)·1 + (1/4)·2 + 0·1 = 1.  Proved by
   norm_num.

The full categorical statement — that these ARE the Frobenius
coefficients of the Jones-normalised Markov trace (requiring the
Markov-trace existence/uniqueness theorem on H_n(q) and the
TL-factorisation of the Jones polynomial) — is deferred until those
theorems are available in Mathlib at the needed depth.  Steps 1–3 of
the narrative proof in the `.md` give the rigorous argument; the
Borromean closed form `prop:borromean-markov-trace-closed-form`
pins y_(2,1)(q) = 1/[2]_q² uniquely.
-/

import Mathlib

namespace QOU.BraidsAndKnots

/-- **Temperley-Lieb quotient kernel identity** for H_3:
`[2]³ − 2[2] = [4]` in the symmetric q-integer convention
(`[2] = q + q⁻¹`, `[4] = q³ + q + q⁻¹ + q⁻³`).

This identity is the algebraic content of `y_(1^3) ≡ 0`: with the
sign-channel weight identically zero, the Markov-normalisation
residual `1 − 2/[2]²` assigned to the trivial channel equals
`[4]/[2]³` exactly.  Equivalently: `([2]² − 2)/[2]² = [4]/[2]³`. -/
theorem h3_tl_quotient_identity (q : ℝ) (hq : q ≠ 0) :
    (q + q⁻¹) ^ 3 - 2 * (q + q⁻¹) = q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹ := by
  have h3 : q ^ 3 ≠ 0 := pow_ne_zero 3 hq
  field_simp
  ring

/-- **Markov normalisation at q = 1** for the closed-form H_3 Wenzl
weights `(y_(3), y_(2,1), y_(1^3))|_{q=1} = (1/2, 1/4, 0)` with
dimensions `(d_(3), d_(2,1), d_(1^3)) = (1, 2, 1)`:

  Σ_λ y_λ(1) · d_λ = (1/2)·1 + (1/4)·2 + 0·1 = 1.

The weights are NOT uniform — `y_(1^3)(q) ≡ 0` (Temperley-Lieb
quotient: the Jones polynomial factors through TL_3, killing the
3-row partition), and `y_(3)(1) = 1/2 ≠ 1/4 = y_(2,1)(1)`. -/
theorem h3_markov_wenzl_weights :
    (1/2 : ℝ) * 1 + (1/4 : ℝ) * 2 + (0 : ℝ) * 1 = 1 := by
  norm_num

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- (Jones, "Hecke algebra representations of braid groups and link
--  polynomials" — the Markov trace on H_n(q), its [2]_q^{c-1}
--  closure normalisation, and the Temperley-Lieb factorisation of
--  the Jones polynomial.)
-- Deferred full categorical statement (needs Markov-trace existence
-- + TL factorisation in Mathlib):
--
--   theorem H3MarkovWenzlWeights :
--     ∀ q ≠ 0,  wenzl_weight (3:Partition) q = qint 4 q / (qint 2 q)^3
--             ∧ wenzl_weight (2,1) q = 1 / (qint 2 q)^2
--             ∧ wenzl_weight (1,1,1) q = 0
--     := sorry

end QOU.BraidsAndKnots
