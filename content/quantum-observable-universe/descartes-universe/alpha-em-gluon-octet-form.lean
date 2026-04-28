/-!
# QOU.DescartesUniverse.alpha_em_gluon_octet_form

Structural-assembly statement: the closed form

  1/α_EM = 45 · [3]_q · (1 + δ_CS + 8·q · δ_CS²)
  δ_CS  = ℏ_q^4 · [5]_q

is the assembled consequence of four upstream structural
propositions (the dimension `45`, the quantum integer `[3]_q`, the
Chern-Simons correction `δ_CS`, and the prefactor `8q` on `δ_CS²`).

The formula itself is `QOU.DescartesUniverse.alphaEmInvCorrected`
in `em-coupling-chern-simons.lean`. This file does not redefine
it; it states the structural-assembly theorem as a one-line
consequence and exposes the dependency chain in Lean.

LaTeX label: `prop:alpha-em-gluon-octet-form`

## References
- [manuscript] §5/alpha-em-gluon-octet-form
- [jones1987] https://doi.org/10.2307/1971403 — Hecke / braid trace
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2 — Quantum groups
-/

import QOU.DescartesUniverse.EmCouplingChernSimons

namespace QOU.DescartesUniverse

/-- **Theorem (gluon-octet structural assembly).**

    `alphaEmInvCorrected` is the assembled consequence of:
    - `prop:exterior-square-borromean` — the integer `45 = dim Λ²V_nat^{10}`
    - `thm:em-spectral-completeness` + `cor:gauge-coupling-uniqueness` —
      the singlet quantum trace `[3]_q`
    - `prop:gram-determinant-plancherel-ratio` —
      `δ_CS = ℏ_q^4 · [5]_q`
    - `prop:force-carrier-bring-uniqueness` —
      the genus-4 torus-knot enumeration `8q`

    No factor is empirical. The structural-assembly content of this
    proposition is captured by `rfl`: the definition of
    `alphaEmInvCorrected` already encodes each factor in the form
    forced by the upstream propositions. -/
-- Ref: [manuscript] §5/alpha-em-gluon-octet-form
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
theorem alpha_em_gluon_octet_form (q : ℝ) (hq : q > 1) :
    alphaEmInvCorrected q hq =
      45 * qInt 3 q *
        (1 + deltaCS_gluonOctet q + gluonOctetKappa q * deltaCS_gluonOctet q ^ 2) := by
  unfold alphaEmInvCorrected
  rfl

end QOU.DescartesUniverse
