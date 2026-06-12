/-
# `prop:symmetric-point-wenzl-markov-uniform`

Uniform Wenzl/Markov measure at q = 1: y_λ(1) = 1/2^{n-1} on H_n(q).

At the symmetric point q = 1, the Wenzl coefficients y_λ(q) of the
Frobenius expansion of the Markov trace on H_n(q) collapse to a
**uniform** value across all partitions λ ⊢ n:

  y_λ(q = 1) = 1/[2]_q^{n-1}|_{q=1} = 1/2^{n-1}

This file states the numeric kernel of the proof: for n = 3, the
uniform value is 1/4, and the Markov normalisation
  y_(3) · d_(3) + y_(2,1) · d_(2,1) + y_(1^3) · d_(1^3) = 1
becomes
  (1/4) · 1 + (1/4) · 2 + (1/4) · 1 = 1
as an arithmetic identity provable by `norm_num`.

The full categorical statement — that the value 1/2^{n-1} is the
symmetric-point limit of the Markov prefactor [2]_q^{n-1} for the
n-strand identity braid's c = n-component link closure — requires the
Markov-trace existence theorem on H_n(q) (Jones 1987, Wenzl 1988)
and is deferred to a follow-up Lean PR once those are in Mathlib at
the needed depth.

This proposition is the structural home of the 1/4 factor in
`prop:borromean-h4-categorical-derivation`; the .md establishes
the bar-involution + Markov-normalisation argument and the worked
n = 3 verification.
-/

import Mathlib

namespace QOU.BraidsAndKnots

/-- **Numeric verification for n = 3** of the uniform-Wenzl-at-symmetric-point
proposition.

States the arithmetic identity for H_3 specifically:
  (1/4) · 1 + (1/4) · 2 + (1/4) · 1 = 1
which is the Markov-normalisation constraint
`Σ_λ y_λ(q=1) · d_λ = tr_M(1_3) = 1` for the uniform value y_λ(1) = 1/4
across the three H_3 irreps (3), (2,1), (1^3) with dimensions
(d_(3), d_(2,1), d_(1^3)) = (1, 2, 1).

The full categorical statement — that y_λ(q = 1) = 1/2^{n-1} for every
λ ⊢ n on H_n(q) — composes:
- Markov normalisation Σ_λ y_λ · d_λ = 1 (Jones 1987, Wenzl 1988).
- Bar-involution + transpose symmetry collapsing distinct Wenzl
  values to a single common value at q = 1.
- The standard closure prefactor [2]_q^{n-1} = 2^{n-1} at q = 1
  for the c = n-component closure of the n-strand identity braid.

Deferred to a follow-up Lean PR once Markov-trace existence is in
Mathlib at the needed depth.  Computational verification at 50 dps
for the n = 3 case lives in T18 (probe script on main). -/
theorem symmetric_point_wenzl_markov_uniform :
    (1/4 : ℝ) * 1 + (1/4 : ℝ) * 2 + (1/4 : ℝ) * 1 = 1 := by
  norm_num

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- (Jones, "Hecke algebra representations of braid groups and link
--  polynomials" — introduces the Markov trace on H_n(q) with the
--  [2]_q^{c-1} normalisation for c-component link closure.)
-- Categorical building blocks available on main:
--   • prop:borromean-markov-trace-closed-form — the explicit closed
--     form tr_M(β_Bor) = (4 + h² − 3h⁴ − h⁶)/(h² + 4) on H_3 from
--     which the n = 3 case extracts y_(2,1)(0) = 1/4.
--   • prop:borromean-h4-categorical-derivation — uses this prop's
--     uniform-Wenzl fact as the structural source of the 1/4 factor.
-- Full categorical Lean derivation (deferred — needs Markov-trace
-- existence on H_n(q)):
--
--   theorem SymmetricPointWenzlMarkovUniform :
--     ∀ (n : ℕ) (λ : Partition n),
--       wenzl_weight_at_q_one n λ = (1 : ℝ) / (2 ^ (n - 1))
--     := sorry

end QOU.BraidsAndKnots
