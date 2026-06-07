/-
# `prop:borromean-h4-categorical-derivation`

Borromean h⁴ = -3/4 derived as (-3) · (1/4) via R-matrix + Markov normalisation.

The h⁴ coefficient of the Borromean Markov trace
`tr_M(β_Bor) = (4 + h² - 3h⁴ - h⁶)/(h² + 4)` factorises as
`(-3) · (1/4)` where `-3` is the h⁴ coefficient of the standard-irrep
character `χ^{(2,1)}(β_Bor) = 2 - 3h⁴ - h⁶` (derived from the R-matrix
on V_{1/2}^⊗3 via Schur-Weyl), and `1/4 = 1/[2]_q²|_{q=1}` is the
standard Markov-trace normalisation for c=3-component link closure.

This file is currently a **numeric lemma** stating the arithmetic
factorisation identity `(-3) · (1/4) = -3/4` and proving it by
`norm_num`. The full **categorical statement** — that this identity
arises as the Frobenius-expansion + R-matrix-derivation decomposition
of the Markov trace coefficient — is deferred to a follow-up Lean PR
since it requires q-Schur duality + Markov-trace existence theorems
not yet formalised in Mathlib at the needed depth.

Computational verification (50 dps) lives in the probe scripts
referenced in the `.ts` manifest:
- T15 (`gap_a4_T15_character_polynomial_probe.py`) — algebraic
  derivation of `χ^{(2,1)}(β_Bor) = 2 − 3h⁴ − h⁶`.
- T18 (`gap_a4_T18_markov_normalization_probe.py`) — Markov
  normalisation derivation of `y_{(2,1)}(q=1) = 1/4`.
-/

import Mathlib

namespace QOU.BraidsAndKnots

/-- **Numeric factorisation lemma** for the Borromean h⁴ coefficient.

States the arithmetic identity `(-3) · (1/4) = -3/4` — the
combinatorial core of the categorical chain:

  h⁴(tr_M(β_Bor)) = [χ^{(2,1)} R-matrix coeff] · [Markov normalisation]
                  = (-3) · (1/4)
                  = -3/4

This is **not** a categorical statement about Markov traces or
R-matrices; it is the numeric kernel that the (deferred) full
categorical derivation reduces to once the structural factors are
extracted. The accompanying `.md` proof provides the full categorical
chain narrative; the computational probes T15 + T18 verify the
identity at 50 dps. -/
theorem borromean_h4_numeric_factorisation :
    (-3 : ℝ) * (1/4 : ℝ) = -3/4 := by
  norm_num

-- Ref: [murasugi1996] https://doi.org/10.1007/978-3-642-58947-1
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Full categorical Lean derivation (deferred — requires q-Schur duality
-- + Markov-trace existence theorems): the statement would be
--
--   theorem BorromeanH4CategoricalDerivation :
--     h4_coefficient (markov_trace (closure beta_Bor)) =
--       chi_standard_irrep_h4_coeff * markov_normalisation_3_components
--     := sorry
--
-- where `chi_standard_irrep_h4_coeff = -3` derives from the R-matrix
-- on V_{1/2}^⊗3 via Schur-Weyl, and `markov_normalisation_3_components
-- = 1/[2]_q²|_{q=1} = 1/4`.

end QOU.BraidsAndKnots
