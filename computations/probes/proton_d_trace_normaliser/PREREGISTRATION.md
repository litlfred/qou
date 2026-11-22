# Pre-registration: the proton from the convention-D trace alone

Written and committed before the probe runs. Diagnostics only: no arm is
adopted on these numbers, and nothing here changes production.

## Question

The production nucleon formula is

    m_p = 2·(m_μ·F_Bor − 6·m_e),   F_Bor = |tr_M(β_Bor)|·N(q),   N = [3]_q!/q³,

with `m_μ = m_e·Vol(4₁)/ℏ_q²`. Can `N` be replaced by a normaliser that the
convention-D Markov trace itself supplies, so that no hand-chosen factor is
left?

## Measured before registering (not a prediction)

At the proton pin, the production `tr_M` formula
`|(4 + h² − 3h⁴ − h⁶)/(h² + 4)|`, `h = q − q⁻¹`, evaluates to
`0.99856216383678726595…`. That is the registry's convention-D Borromean value
(`computations/audits/borromean_convention_by_evaluation.py`), not the
convention-C value `0.99836662…`. So production already uses the D trace, and
the whole question is the normaliser `N`.

## Arms (fixed now)

The trace is the normalised D Markov trace, `tr(1) = 1`. Each arm multiplies it
by a factor that a closure convention supplies. None is tuned.

| arm | N(q) | origin |
|---|---|---|
| B0 | 1 | normalised trace, `tr(1) = 1` |
| B1 | `[2]_q²` | closure of 3 strands with loop value `[2]_q`, `n − 1 = 2` loops |
| B2 | `[2]_q³` | unnormalised quantum trace, `δⁿ` with `δ = [2]_q`, `n = 3` |
| B3 | `(1/z_D)²`, `z_D = q³/(q²+1)` | Ocneanu closure with loop `1/z_D`, `n − 1 = 2` |
| A0 | `[3]_q!/q³` | production (gate: must reproduce production q₀) |

## What is computed

For each arm: the root `q₀` of `m_p/m_e = 2·Vol(4₁)/ℏ_q²·|tr|·N − 12` nearest
the production pin, its shift in ppb, and `m_p` at the muon pin with its error.
mpmath, 50 dps, no float64.

## Expectations, recorded before running

- At `q ≈ 1.11`: `[3]!/q³ ≈ 4.48`, `[2]² ≈ 4.04`, `[2]³ ≈ 8.1`, `(1/z_D)² ≈ 2.3`.
  So I expect B1 to miss `m_p` by roughly −10 %, B2 by about +80 %, B3 by about
  −50 %, and B0 to land near 200 MeV. I expect no arm to reproduce `m_p`.
- If an arm does land within 0.1 %, that is a coincidence to examine, not a
  derivation: the closure convention would still have to be justified for the
  Borromean observable before it could replace `N`.
