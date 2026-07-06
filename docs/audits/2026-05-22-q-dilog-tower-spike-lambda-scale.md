# q-dilog tower spike: search for substrate-pure $\lambda_\text{scale}$

**Date:** 2026-05-22
**Branch:** `claude/iw-q-dilog-tower-spike-2026-05-22`
**Status:** Negative result — q-dilog leg also empirically refuted in
the tested basis, parallel to the hyperbolic-knot Bloch leg
(PR #888 + #904).

## Context

After PR #888 (`LAMBDA_*_FITTED_FROM_CODATA` truth-in-naming) + PR
#904 (`prop:lambda-scale-bring-bloch-identity` → `conj:`), the
hyperbolic-knot Bloch-basis PSLQ route has been **empirically
refuted** at tier 5 (52-knot basis through 11-crossing prime
hyperbolic knots, coefficient ≤ 10³⁰, dps 100). Per the tier 5
conclusion (`bring_bloch_tier5_search_m_p.py`), the proton's
Bring-decomposition is "**genuinely transcendental** in the tested
basis"; the q-dilog tower is the named remaining research direction.

This spike tests **whether the q-dilog tower closes trivially at
substrate-natural arguments** — i.e., is there a small integer
combination of `Li_2^q(z_i) / Φ_q(z_j)` at z_i ∈ {substrate-natural}
that equals λ_scale or Vol_eff?

## Method

Two PSLQ sweeps:

### Sweep A — 23-element basis, coefficient ≤ 10²⁰, dps 60

Script: [`q_dilog_tower_spike_lambda_scale.py`](../../computations/q_dilog_tower_spike_lambda_scale.py)

Basis:
- `Li_2^q(z)` and `Φ_q(z)` evaluated at 8 substrate-natural arguments:
  `{1/φ, 1/φ², 3/7, 1/[2]_q, h_q, −h_q, h_q², −h_q²}` (16 entries)
- Classical anchors: `{1, G, [2]_q, [3]_q, [4]_q, φ, h_q}` (7 entries)

Targets:
- `λ_p = 2.4599527869`
- `Vol_eff_p = λ_p · 8G ≈ 18.0258569`
- `secondary = Vol_eff_p − 8G ≈ 10.6981` (Option-B-style additive)

### Sweep B — 15-element basis, coefficient ≤ 10³⁰, dps 80

Includes pentagon-identity-compatible arguments `Li_2^q(1−z)` for
each z, to allow PSLQ to discover Rogers-pentagon identities
involving the target.

## Result

**Both sweeps: no non-trivial relation found.**

- Sweep A: explicit "no relation found at coeff ≤ 10²⁰" for all 3 targets.
- Sweep B: PSLQ returns the trivial duplicate-detection `Li_2^q(1/φ) − Li_2^q(1−1/φ²) = 0` (which is mathematically forced since `1 − 1/φ² = 1/φ`); the target coefficient is 0 in this relation.

The proton's λ_scale therefore does **not** admit a $\mathbb{Q}$-linear
relation to the substrate-natural q-dilog values in the tested
basis under coefficient bound 10³⁰. Parallel to PR #888/904's
hyperbolic-knot result.

## What this rules out vs leaves open

**Ruled out (in the tested bases):**
- `λ_scale = Σ_i (a_i / a_0) · Li_2^q(z_i)` for $z_i$ ∈ {1/φ, 1/φ², 3/7, 1/[2]_q, ±h_q, ±h_q²} with $|a_i| ≤ 10^{30}$.
- Analogous claims with `Φ_q` instead of `Li_2^q`.
- Mixed combinations including classical anchors `{G, [n]_q, φ, h_q}`.

**Still open:**
- Larger argument basis — particularly the per-block spectral
  coordinates `|V̂_S|` from
  [`prop:mass-tower-operator-valued`](../../content/quantum-observable-universe/braids-and-knots/mass-tower-operator-valued.md);
  these are the actual targets `bringBlochRegulator(K)` is opaque
  over in the Lean stub.
- Non-linear closure: products `Li_2^q(z_1) · Li_2^q(z_2)` or
  Bloch-Wigner regulators of two-variable arguments.
- Trace-field tower: per `conj:lambda-scale-bring-bloch-identity`
  §"Trace-field tower", the Borel rank in $B(\mathbb{Q}(\zeta_{60}))$
  is 8, so 8 independent regulator values may be needed. The
  current basis is 1-variable Li_2^q only.
- Different normalisation: PSLQ over `λ_scale · 8G − G^k` or
  similar `G`-shifted targets.

## Recommendation

Track as **q-dilog Tier 0** result (parallel to Bring-Bloch Tier 0,
also negative). Future work should:

1. Extend to the operator-valued `|V̂_S|` argument set from the
   mass-tower endomorphism.
2. Include 2-variable Bloch-Wigner regulators
   (`L_2(x, y) := D[x] + D[y] + D[xy/((1-x)(1-y))]` style).
3. Try the full $\mathbb{Q}(\zeta_{60})$ trace-field rank-8 basis
   per `conj:lambda-scale-bring-bloch-identity` §"Trace-field tower".

If all three exhaust to negative, $\lambda_\text{scale}$ is
empirically a CAL-4 anchor in every tested substrate-natural basis,
and the `conj:lambda-scale-bring-bloch-identity` open work would
need to either (a) propose a non-substrate-natural basis or
(b) be retired.

## Witness

[`computations/q-dilog-tower-spike-lambda-scale.witness.json`](../../computations/q-dilog-tower-spike-lambda-scale.witness.json)
records sweep A's basis names, parameters, and per-target results.
