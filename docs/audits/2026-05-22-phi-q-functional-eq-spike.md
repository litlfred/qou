# Φ_q functional-equation spike for λ_scale

**Date:** 2026-05-22
**Branch:** `claude/iw-phi-q-functional-eq-spike-2026-05-22`
**Predecessors:**
- PR #888 — `LAMBDA_*_FITTED_FROM_CODATA` literal truth-in-naming
- PR #892 — `conj:mobius-limit-from-thimble` curve-fit demotion
- PR #904 — `conj:lambda-scale-bring-bloch-identity` demotion
- PR #923 — substrate-natural q-dilog basis exhausted (negative)
- PR #928 — V̂_S + ℚ(ζ_60) + Tier-0-knot basis exhausted (negative)
- PR #939 — curve-fit-ansatz disguise hunt (CI tooling)

**Status:** Negative — closest substrate-natural functional-equation back-solve target (`z_* = 1 − 1/λ_p ≈ 0.5935`) is 4.1% from `1/φ`. No ppb-precision Φ_q ratio or pentagon-like identity at substrate-natural arguments produces λ_scale.

## Context

PR #928 + #939 left only ONE structurally distinct path open for
deriving λ_scale ≈ 2.4599527869 from substrate data: the
**non-linear** route via Φ_q (Faddeev quantum dilogarithm)
functional equations / pentagon identities. PSLQ-style linear
searches over q-dilog, Bloch-Wigner, hyperbolic-knot, and ℚ(ζ_60)
trace-field bases have all exhausted to negative at coefficient
bound 10³⁰.

Faddeev's Φ_q satisfies a key functional equation:

$$
  \Phi_q(q \cdot z) = \frac{1}{1 - z} \cdot \Phi_q(z),
$$

so ratios `Φ_q(qz)/Φ_q(z) = 1/(1−z)` give a *non-linear* family of
relations PSLQ cannot see. If `λ_p = Φ_q(qz_*)/Φ_q(z_*)` for some
substrate-natural `z_* ∈ (0, 1)`, then `λ_p = 1/(1 − z_*)`, so
`z_* = 1 − 1/λ_p`.

## Method

Script: [`phi_q_functional_eq_spike.py`](../../computations/phi_q_functional_eq_spike.py).

Three tests at dps = 80:

| # | Test | Detail |
|---|---|---|
| (1) | Back-solve `z_* = 1 − 1/λ_p` and compare to substrate-natural z-candidates | 11 candidates: `{h_q, h_q², 1/φ, 1/φ², 1/[2]_q, 1/[3]_q, 1/[4]_q, (q-1)/q, (q-1)/(q+1), z_c^Re, 3/7}` |
| (2) | `Φ_q(z) / Φ_q(w)` ratios for substrate-natural (z, w) pairs | 9² − 9 = 72 ratios, filtered by `|z|, |w| < q` convergence |
| (3) | Commutative pentagon-like `Φ_q(z) Φ_q(w) / Φ_q(z + w − zw)` | 36 (z, w) pairs |

## Result

**Negative — no ppb match across all three tests.**

### Test (1): `z_* = 1 − 1/λ_p ≈ 0.5935`

| Candidate | Value | `|Δ| / z_*` |
|---|---|---|
| **1/φ** | **0.61803** | **0.0414** (closest) |
| 1/[2]_q | 0.49729 | 0.1621 |
| 3/7 | 0.42857 | 0.2779 |
| 1/φ² | 0.38197 | 0.3564 |
| h_q | 0.20906 | 0.6477 |
| z_c^Re | 0.10583 | 0.8217 |
| h_q² | 0.04371 | 0.9264 |

The closest substrate-natural candidate to `z_*` is `1/φ`, with a
relative error of **4.14%**. Equivalently, `λ_p ≈ 1/(1 − 1/φ) = φ`
fails: `φ = 1.618` vs `λ_p = 2.460` (no — `1/(1 − 1/φ) = φ/(φ−1)
= φ² = 2.618` which is 6.4% over `λ_p`).

So neither `λ_p = φ²` nor `λ_p = 1/(1 − z_*)` for `z_*` at any
tested substrate-natural value lands within ppb precision.

### Test (2): `Φ_q(z) / Φ_q(w)` ratios

Smallest relative error from `λ_p`: **9.98%** across 72 ratios. No
candidate within 1% of `λ_p`.

### Test (3): Pentagon-like `Φ_q(z) Φ_q(w) / Φ_q(z+w−zw)`

Smallest relative error: **3.07%** across 36 pairs. No candidate
within 1% of `λ_p`.

## Cumulative empirical tally

| Search | Approach | Basis size | Coeff bound | Result |
|---|---|---|---|---|
| `bring_bloch_tier{0..5}` | linear PSLQ on hyperbolic-knot Bloch-Wigner | 52 knots ≤ 11 crossings | 10³⁰ | negative |
| `q_dilog_tower_spike` (#923) | linear PSLQ on Li_2^q + Φ_q at substrate-natural | 23 elements | 10³⁰ | negative |
| `q_dilog_vhat_spike` (#928) | linear PSLQ on V̂_S + ℚ(ζ_60) D + Tier-0 vols | 23 elements | 10³⁰ | negative |
| **`phi_q_functional_eq_spike`** (this) | **non-linear** Φ_q functional-equation + pentagon ratios | 11 + 72 + 36 = 119 tested values | n/a (ppb match) | **negative** |

Four independent searches, four negative results. The empirical
case that `λ_p` is unobtainable via any natural substrate-q-dilog /
Bloch-Wigner construction up to PSLQ-coefficient `10³⁰` and to
ppb precision under non-linear Φ_q identities is now strong.

## What this does NOT rule out

1. **Non-substrate-natural Φ_q arguments**: e.g. `z_* = 1 − 1/λ_p ≈
   0.5935` might still equal some non-obvious substrate quantity
   (a combination of V̂_S, hyperbolic-knot vol ratios, or other
   structural data not in the tested list).
2. **Higher-order operator-theoretic identities**: the genuine
   Faddeev pentagon `Φ_q(U)Φ_q(V) = Φ_q(V)Φ_q(UV)Φ_q(U)` for
   Heisenberg-paired (U, V) is a quantum identity, not a
   commutative ratio. Implementing this in the spike would
   require the Stone-von Neumann unique representation; out of
   scope here.
3. **Modular transformations**: Faddeev's Φ_q is well-defined on
   the upper half-plane / on |q| = 1 via the modular dual `q̃ =
   exp(−2πi/b²)`. For real `q_0 > 1`, the modular framework is
   not directly applicable.
4. **Different `z_*` parametrization**: this spike used
   `λ_p = Φ_q(qz)/Φ_q(z)`. Alternative parametrizations like
   `λ_p = Φ_q(z)^k / Φ_q(w)^l` for small integer `k, l` may close
   where simple ratios don't.

## Recommendation

Track as a fourth consistent-negative empirical tier. The
remaining genuinely-open directions (per cumulative audit):

1. **Operator-theoretic Faddeev pentagon** with Heisenberg-paired
   arguments — requires the Stone-von Neumann representation
   framework; this is the most structural direction but
   computationally heavier than spike work.
2. **z_* ≈ 0.5935 identification** — does this constant equal a
   non-obvious substrate quantity? Numerically search a larger
   basis at ppb tolerance.
3. **Retire `conj:lambda-scale-bring-bloch-identity`** in favour of
   an explicit acknowledged CAL-4 anchor if all empirical
   directions exhaust. (Per AGENTS.md three-calibration discipline,
   only `m_e`, `q_0`, and `Q_β` are calibration inputs; CAL-4
   anchors are documented as falsifiable predictions that
   numerically agree with CODATA but are not derived.)

## Witness

[`computations/phi-q-functional-eq-spike.witness.json`](../../computations/phi-q-functional-eq-spike.witness.json)
