# χ(P)|q₀ vs r* — the decisive A=3 magnitude evaluation (scope-(a) negative)

**Date:** 2026-08-08
**Branch:** `claude/chi-p-magnitude-evaluation-2026-08-08`
**Beans:** qou-wgnx, qou-wiub
**Witness:** [`computations/qbeta/c1-chi-magnitude-vs-r-star.witness.json`](../../computations/qbeta/c1-chi-magnitude-vs-r-star.witness.json)
**Script:** [`computations/qbeta/c1_chi_magnitude_vs_r_star.py`](../../computations/qbeta/c1_chi_magnitude_vs_r_star.py)

## The check

The A=3 magnitude keystone reduced (this week, all merged) to: the
anti-self-adjoint amplitude `E` = the gauge-invariant Birkhoff cross-ratio
`χ(P)` of C1 (`BirkhoffAmplitudeWellPosed` #4820, `BirkhoffAmplitudeE` #4823),
and `χ(P)` is derived in **closed form** already on main
([`C1ConnectionPoles.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/C1ConnectionPoles.lean),
sorry-free):

$$
\chi(z) = \frac{\theta_p(z/\alpha)\,\theta_p(-z/\bar\alpha)}
               {\theta_p(-z/\alpha)\,\theta_p(z/\bar\alpha)},
\qquad \alpha = t_2/T,\quad |\alpha| = q^{3/4},\quad C = 1,
$$

with `T = √((p²−1)/p³) = √(q−1)/q^{3/4}`, `p = √q`, and `t₂` a root of C1's
0-side indicial equation `t² + (q−1)t + (q−1) = 0` (conjugate pair for `1<q<5`).

The genuinely open, decisive item nobody had done: **evaluate this closed-form
`χ(P)` at C1's substrate parameters** (proton `q₀`, hence `α` and the theta
nome, all derived from C1's operator `L1`, no tuning) **and compare the number
to the observed lift `r* = μ₃/c₃ ≈ 1.585`.**

Corpus-grep (docs/audits, content, computations, beans wgnx/wiub/jqof) confirmed
this evaluation did not exist. Done here.

## q₀ pin

Experimental / proton (owner directive 2026-08-07):
`q₀ = 1.1099785827513808075916690956…` (`q_parameter.Q`, `m_p/m_e`-pinned).
Recorded in the witness.

## Result — scope-(a) negative

`χ(P)` on the real axis is a **pure unit-modulus phase**:

| z | \|χ(P)\| | arg χ(P) | \|\|χ\|−r*\| |
|---|---|---|---|
| 0.30 | 1.0 (dev 0.0) | −0.4883212517 | 0.585 |
| 0.45 | 1.0 (dev 0.0) | −1.9212291778 | 0.585 |
| 0.60 | 1.0 (dev 0.0) | +1.3100992647 | 0.585 |
| 0.75 | 1.0 (dev 0.0) | +3.0518568647 | 0.585 |

- `|α| = q^{3/4} = 1.0813989643…` exactly (derived, no tuning).
- Closed form vs the direct merged connection matrix `P = Y₀⁻¹Y_∞`: agree to
  `1.1e-5` at this truncation (same object; the Lean docstring's `5.3e-63` uses
  more series terms).
- `|χ(P)| = 1` **exactly** (dev 0.0; matches `exp(2i(arg c₊−arg c₋))` to `1e-121`
  in the parent invariant witness).
- `χ(P)` is **not a single number** — it is a `z`-dependent elliptic function on
  the unit circle.

`r* = μ₃/c₃ ≈ 1.585` is a real magnitude `> 1`. **A unit-modulus phase cannot
equal a real magnitude `> 1`.** So `χ(P)|q₀` does **not** numerically supply
`r*`: the naive identity `χ(P) = r* ⟹ A=3 magnitude closed` does **not** hold.

This is a clean **scope-(a) negative** for the *direct identity* `χ(P) = r*`. It
is fully consistent with the whole A=3 magnitude program, where every trace /
cross-ratio object comes out modulus 1 and `r* ≈ 1.585 ≠ 1` is not supplied
([`option-e.md`](../coordination/option-e.md), "r* ≈ 1.585 ≠ 1 is NOT supplied").

## What this does and does NOT refute

- It does **NOT** refute the gauge-invariance / well-posedness argument
  `E = χ(P)` (`BirkhoffAmplitudeWellPosed`, `BirkhoffAmplitudeE`). That argument
  says the amplitude `E` is the *unique gauge invariant* of the connection
  matrix; it never claimed `χ(P)` equals the *magnitude* `r*`.
- It **sharpens** the open item. The A=3 lift is *affine* in `E`
  ([`A3AntiSelfAdjointLift.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/A3AntiSelfAdjointLift.lean)):
  `lift = factor_sa − (B·D⁻¹/A)·E`, with `factor_sa ≤ 1` (the proved
  self-adjoint reduction). So `r*` is *not* `χ(P)` itself — at most a real
  functional of it fed through that affine map.
- **The cross-ratio's numeric value is NO LONGER open** — it is a computed unit
  phase (elliptic in `z`). What remains genuinely open is the *bridge*: which
  real anti-self-adjoint amplitude `E` the unit-phase `χ(P)` supplies (a
  phase→real-amplitude map is unspecified), at which `z`, and whether feeding
  that through `factor_sa − (B·D⁻¹/A)·E` reproduces `r*`. That chain — not the
  χ value — is the wall. There is a genuine **type tension** to reconcile:
  `A3AntiSelfAdjointLift` takes `E` as a single free *real* amplitude entering a
  real affine lift, whereas the connection cross-ratio delivers a *unit-modulus
  complex phase*; the corpus supplies no derived reconciliation.

## Discipline

Derive-then-check, mpmath ≥ 50 dps (120 dps compute), proton `q₀`, witness
records the pin. `χ(P)` was never tuned to hit `r*`; nothing wired to
production; no `q₀`-derivation routed through. A scope-(a) negative on the
direct identity is a real, valuable result: it closes the "is χ(P) the
magnitude?" question (no) and relocates the open work to the phase→amplitude→lift
bridge.
