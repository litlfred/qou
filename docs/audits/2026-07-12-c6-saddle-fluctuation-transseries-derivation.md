# C6 built — the saddle-fluctuation transseries derives the κ ladder exactly (κ₁..κ₇)

**Date:** 2026-07-12 · **Axis:** Borel/alien-calculus C6 ("the wall") + G2
("bridge arithmetic") · **Tier:** symbolic-exact (sympy derivation; Stirling
control; 40/33-digit numerical cross-checks) · **Discipline:** no fit to QOU
data, no Q_β c_k wired, no tier change. PR #3683 pickup item 3.

## What was built

The [utilization audit](2026-07-12-borel-alien-calculus-utilization-audit.md)
§C6 named the one compute item with no script: *"the resurgent transseries
around that saddle produces its fluctuation orders one by one (the i·t·κ₁
finite-b correction already in use is the leading term). No script computes
it — pure opportunity, and the audits call it 'the wall'."*

[`computations/probes/qbeta_phib_saddle_fluctuation_transseries_probe.py`](../../computations/probes/qbeta_phib_saddle_fluctuation_transseries_probe.py)
now computes those fluctuation orders **as exact arithmetic** (32 s wall).
Three exactly-known layers are assembled at the saddle s* = 5/6 of the 4₁
Kashaev sum J_N = Σ_k ∏_{j≤k}(2 sin(πj/N))²:

1. **Potential:** Φ(s) = −Cl₂(2πs)/π, Φ′ = 2 log(2 sin πs) — the full
   derivative tower at s* lies in ℚ(√3)·πᵏ because cot(5π/6) = −√3 (the
   ℚ(√−3) trace field made concrete);
2. **Euler–Maclaurin layer** of the inner sum after splitting off the exactly
   summable singular part Σ 2log(2πj/N) = 2k·log(2π/N) + 2·log k! (E–M then
   applies to the smooth g₀(s) = log(sin(πs)/(πs)), g₀(0) = 0);
3. **Stirling layer** of the 2·log k! piece.

The assembled N-graded exponent is saddle-expanded by a generic Wick engine
(formal steepest descent, Gaussian moments), and log of the fluctuation
series gives the Ohtsuki rungs κ_n exactly.

## Results

| check / rung | value | status |
|---|---|---|
| Wick-engine control | Stirling series 1, 1/12, 1/288, −139/51840, −571/2488320 | **exact match** |
| amplitude a₀ | −(1/4)·log 3 (Andersen–Hansen 3^{−1/4}, with N^{3/2}) | **exact** |
| κ₁..κ₄ | (11/108)√3π, (2/27)π², (1081/21870)√3π³, (98/729)π⁴ | **reproduced exactly** (#3606/#3628 priors) |
| κ₅ | (110011/688905)·√3·π⁵ | **reproduced exactly** (same-day 40-digit identification → now a computed theorem) |
| **κ₆** | **(207892/295245)·π⁶** (295245 = 3¹⁰·5) | **NEW**; matches the same-day 33-digit extraction to < 10⁻³⁰ |
| **κ₇** | **(32729683/26572050)·√3·π⁷** (26572050 = 2·3¹²·5²) | **NEW** |

The √3-parity alternation and the 3-power-dominated denominators (torsion-3
signature of the trace field) continue through weight 7 — now as *derived*
facts, not PSLQ recognitions.

**Side effect — the κ₆ PSLQ "miss" adjudicated.** The extraction run had
reported no ℚ·π⁶ hit at 33 digits within a 5·10¹⁴ budget; the derived height
is only 3·10⁵. The miss was a fixed-4-digit tolerance-slack artifact in the
inherited PSLQ call; the extraction script now uses height-tiered
tolerances and re-identifies κ₆ within budget (see the
[κ₅ audit](2026-07-12-kappa5-exact-identification.md), updated in place).

## Honest scope

- **Root-of-unity face.** The generator runs at the Kashaev/root-of-unity
  face of the figure-eight saddle — the face with exact ground truth. The
  Φ_b state-integral face at (complex) meridian m consumes the *same*
  generator fed the deformed-saddle derivative tower from the gluing
  solution z(m) (`qbeta_c3_barodd_gluing_newton_solve.vol_of_m`); its
  leading finite-b correction i·t·κ₁ (in
  `qbeta_c3_phib_saddle_state_integral_probe.py`) is literally rung 1.
  That wiring is the natural follow-up; per the bridge growth-obstruction
  audit, the ħ ↔ 2πi/N channels relate by **resummation**, not term-by-term
  reparametrisation — nothing here claims otherwise.
- **These are 4₁ topological facts.** The 4₁ ↔ Q_β bridge remains the open
  keystone. NO fit to QOU data; NO c_k value wired; NO tier change.
- The E–M/Stirling assembly is an asymptotic identity used to fixed order
  (errors O(N⁻⁸) beyond κ₇); every emitted rung is independently
  cross-checked against the 40/33-digit Richardson extractions and the
  #3606/#3628 exact priors.

## What this closes / feeds

- **C6 (the wall): built** — fluctuation orders produced one by one, exactly.
- **G2 (bridge arithmetic): realized** in its compute face — the tail is
  *generated arithmetically*, not recognized numerically; the κ-ladder
  entropy block is dissolved rung by rung (each new rung costs symbolic
  computation, not precision).
- The G2+C3 one-instanton large-order test can be re-anchored on exact
  κ₅..κ₇; the C1 conformal-Borel action estimate gains three exact rungs of
  input.

## Cross-references

- Utilization audit (C6, G2): [`2026-07-12-borel-alien-calculus-utilization-audit.md`](2026-07-12-borel-alien-calculus-utilization-audit.md)
- Same-day κ₅ identification + κ₆ adjudication: [`2026-07-12-kappa5-exact-identification.md`](2026-07-12-kappa5-exact-identification.md)
- Exact κ₂..κ₄ + parity rule: [`2026-07-12-ohtsuki-higher-rungs-exact.md`](2026-07-12-ohtsuki-higher-rungs-exact.md)
- Witness: [`computations/probes/qbeta-phib-saddle-fluctuation-transseries.witness.json`](../../computations/probes/qbeta-phib-saddle-fluctuation-transseries.witness.json)
