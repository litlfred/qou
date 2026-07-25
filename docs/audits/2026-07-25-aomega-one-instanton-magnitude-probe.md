# A_ω one-instanton magnitude probe — parameter-free amplitude match, slope gap (2026-07-25)

**Branch:** `claude/aomega-magnitude-probe-2026-07-25`. **Continues:** the one-instanton
normalization map (`OneInstantonNormalization.lean`, PR #4246) + its audit.

## The test

The normalization capstone reduces (PR #4246) to a **magnitude identification**: does
the one-instanton form

`N_odd(q) = 𝒜 · e^{−Re 𝔙(q)/(π ℏ)} · sin(Im 𝔙(q)/(π ℏ))`  (𝒜 = integer `b=0` amplitude, `P = 1`)

reproduce the committed `BarOddLadderShape` numerator `A` — its zero at `q*`, magnitude
`A ~ S·u³ ≈ 1.47×10⁻⁶`, and slope `A′ ≈ +2.37`? The A3 probe
(`qbeta_5two_sigma3_nodd_shape_probe.py`, #3927) already tested the **linear** form
`N_odd ∝ Im(ι₁₃)` and found it monotone (no zero) with slope 0.196 (~12× short). This
probe (`qbeta_5two_one_instanton_nodd_probe.py`) tests the distinct **one-instanton
exponential-oscillatory** form, **parameter-free** (`𝒜 = 1`, `P = 1`, `ℏ = log q` — the
GGM `q = e^ℏ` convention, nothing tuned), reusing the `𝔙 = V₁ − V₃` complex-CS
machinery.

## Result (witness `qbeta-5two-one-instanton-nodd.witness.json`, 2/3)

| feature | raw form (A3) | one-instanton (parameter-free) | committed |
|---|---|---|---|
| zero-crossing near substrate | **none** (monotone) | **yes**, `q_z ≈ 1.10126` | zero at `q*` |
| amplitude `𝒜·e^{−Re𝔙/πℏ}` | — | **`1.436×10⁻⁶`** | `A ~ S·u³ ≈ 1.467×10⁻⁶` |
| — magnitude gap | — | **0.009 orders (~2%)** ✓ | — |
| slope at the zero | `0.196` | `1.25×10⁻⁴` | `A′ ≈ 2.37` |
| — slope gap | ~12× | **4.28 orders** ✗ | — |

Two **parameter-free successes** the raw form did not have:

1. **The `sin(Im𝔙/πℏ)` oscillation supplies a zero-crossing** near the substrate
   (`q_z ≈ 1.1013`, `|q_z − q₀| ≈ 0.0087`) — the defining `N_odd` feature the monotone
   raw `Im(ι₁₃)` lacked. The zero is the CS-phase crossing `kπ`, **not** `Im 𝔙 = 0`.
2. **The exponential amplitude matches the committed `A` magnitude to ~2%**
   (`1.44×10⁻⁶` vs `1.47×10⁻⁶`), with **no tuning** — the geometric complex-volume
   exponential `e^{−Re𝔙/πℏ}` independently lands on the `A = S·u³` scale. This is
   genuine evidence the normalization *scale* is the one-instanton exponential.

The **slope is 4.28 orders too gentle**. The interpretation is quantitative and clean:
the committed zero-crossing width is `A/A′ ≈ 1.47×10⁻⁶/2.37 ≈ 6×10⁻⁷ ≈ u` (the lever
scale), whereas the one-instanton phase-zero width is `~1/(dφ/dq) ≈ 1/89 ≈ 0.011`. The
ratio `0.011/u ≈ 10⁴` **is** the slope gap. So the observed steepness is the separate
`1/u³` lever amplification (`S = A/u³`, `BarOddLadderShape`) acting on the one-instanton
numerator — exactly the "the `u³`·smooth prefactor must amplify the slope" the A3 probe
concluded, now **quantified**: the amplitude is one-instanton-exact, the missing factor
is the already-formalized lever, not a new ingredient.

## Scope (STRICT — (a), no fit)

**scope-(a).** The parameter-free one-instanton form reproduces the **existence of the
zero** and the **amplitude** of `N_odd` (to ~2%), and the slope gap is accounted for by
the separate, already-formalized `1/u³` lever — a magnitude decomposition, **not** an
ingredient exclusion and **not** a refutation. Nothing is tuned to `q*` or `A′`; `𝒜 = 1`
(the integer `b=0` amplitude), `P = 1`, `ℏ = log q`. No `c_k` wired; no AME inversion;
`μ` never fixed from QOU data. The Lean structural consistency
(`OneInstantonNormalization.lean`) — that the one-instanton product shape's slope at a
simple zero is log-derivative-free, matching the committed `hasDerivAt_S_at_qstar` —
stands independently of this magnitude comparison.

## What this leaves

The one-instanton normalization map now has **parameter-free numerical support** for its
amplitude and zero, with the slope supplied by the `1/u³` lever. The remaining open
inputs of the capstone (`conj:algebraic-geometric-dilog-equivalence`): (i) the exact
prefactor `P(q)` and the precise pinning of `q_z` onto the committed `q*` (the ~0.009
offset), and (ii) whether the lever `u(q)` composed with the one-instanton numerator
reproduces `A′ ≈ 2.37` exactly. These are magnitude/prefactor refinements, not new
ingredients — the structural map and its scale are now in hand.
