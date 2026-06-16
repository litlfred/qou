# Extended q-dilog spike: V̂_S, ℚ(ζ_60) Bloch-Wigner, Tier-0 knot volumes

**Date:** 2026-05-22
**Branch:** `claude/iw-q-dilog-vhat-spike-2026-05-22`
**Predecessor:** [PR #923](https://github.com/litlfred/qou/pull/923) — original q-dilog spike, negative in substrate-natural-argument basis.
**Status:** Extended negative result — no integer relation found for λ_scale in the tested 23-element basis at coefficient bound 10³⁰. Strengthens the empirical case from PR #923 (this is **not** a mathematical transcendence result; PSLQ negatives only rule out integer relations within the tested basis and coefficient bound).

## Context

PR #923 closed out the basic q-dilog tower path with a negative
empirical result and left three open paths:

> (a) Operator-valued $|\hat V_S|$ spectral coordinates from the
> mass-tower endomorphism.
> (b) 2-variable Bloch-Wigner regulators (Rogers-pentagon style).
> (c) Full ℚ(ζ_60) rank-8 trace-field basis per
> `conj:lambda-scale-bring-bloch-identity` §"Trace-field tower".

This spike tests all three in one consolidated 23-element basis at
PSLQ tolerance dps = 80, coefficient ≤ 10³⁰ (matching
`bring_bloch_tier5_search_m_p.py`).

## Method

Script: [`q_dilog_vhat_spike_lambda_scale.py`](../../computations/q_dilog_vhat_spike_lambda_scale.py).

### Path (a) — operator-valued $\hat V_S$ (signed)

For the canonical proton braid in $H_3$ (Z=1, N=0, A=1), extract
$\hat V_i^\lambda$ values via
[`canonical_tower.per_irrep_V_hat`](../../computations/canonical_tower.py).
Per partition $\lambda \vdash 3$ and generator $i \in \{0, 1\}$
(values are signed):

| $\lambda$ | $\hat V_0$ | $\hat V_1$ |
|---|---|---|
| $(3)$ | $+1.8804$ (skipped; $|V| \ge q_0$) | $+0.7352$ |
| $(2, 1)$ | $+0.6714$ | $+1.0551$ |
| $(1, 1, 1)$ | $-0.5376$ | $+1.3750$ (skipped; $|V| \ge q_0$) |

The four in-range values feed $\mathrm{Li}_2^q(\hat V)$ directly
(signed argument; $\mathrm{Li}_2^q$ converges for any $|z| < q$).

### Path (b) — Bloch-Wigner at primitive $\zeta_n$ (ℚ(ζ_60) trace-field tower, 1-variable)

$D(\zeta_n) = D(e^{2\pi i / n})$ for $n \in \{3, 4, 5, 6, 8, 10, 12, 15, 20, 60\}$ — 10
anchors covering the full ℚ(ζ_60) trace-field tower
$\{\mathbb{Q}(\zeta_3), \mathbb{Q}(\zeta_4), \mathbb{Q}(\zeta_5), \mathbb{Q}(\zeta_{60})\}$.
**This is the 1-variable basis** — true 2-variable Bloch-Wigner / 5-term
Rogers-pentagon pairings are deferred (listed in §"What this does
NOT rule out" item 2).

### Path (c) — hyperbolic-knot trace-field volumes

$\{4_1, \mathcal{B}_3, 5_2, 6_1, 7_4, \text{Whitehead}\}$ — the Tier 0
hyperbolic knots matching `bring_bloch_tier0_search.py`.

### Classical anchors

$\{1, G, \pi, h_q, h_q^2\}$ — 5 elements.

### Combined basis

23 elements: 4 (path a) + 8 (path b) + 6 (path c) + 5 (classical).

### PSLQ

Tolerance $10^{-50}$, max coefficient $10^{30}$, against three
targets:

- $\lambda_p = 2.4599527869$
- $\mathrm{Vol}_{\text{eff}, p} = \lambda_p \cdot 8G \approx 18.0259$
- $\mathrm{Vol}_{\text{eff}, p} - 8G \approx 10.6981$ (the Option-B-style additive form)

## Result

**No relation found for any target across the combined 23-element
basis at coefficient bound 10³⁰.**

| Target | PSLQ outcome |
|---|---|
| $\lambda_p$ | no relation at coeff $\le 10^{30}$ |
| $\mathrm{Vol}_{\text{eff}, p}$ | no relation at coeff $\le 10^{30}$ |
| $\mathrm{Vol}_{\text{eff}, p} - 8G$ | no relation at coeff $\le 10^{30}$ |

## What this rules out

The combined basis covers:

- $\mathrm{Li}_2^q$ at the H_3 spectral coordinates of the canonical proton braid.
- Bloch-Wigner $D$ at all primitive roots of unity in the ℚ(ζ_60) trace-field tower.
- The Tier 0 hyperbolic-knot volume basis (matching the bring_bloch tier 0 negative).
- Classical anchors $\{1, G, \pi, h_q, h_q^2\}$.

No $\mathbb{Q}$-linear combination of these elements with integer
coefficients of absolute value $\le 10^{30}$ produces $\lambda_p$,
$\mathrm{Vol}_{\text{eff}, p}$, or the secondary form.

## What this does NOT rule out

This is an extended substrate-natural exhaustion, not a full
exhaustion. Remaining open:

1. **Higher Hecke levels for $|\hat V_S|$.** This spike used only
   $H_3$ proton coordinates. Extending to $|\hat V|$ at $H_4$,
   $H_5$, $\ldots$ for the proton's atomic braid through
   higher-arc-crossing canonical forms gives a much larger
   spectral-coordinate basis. (The mass-tower-operator-valued
   framework already computes these.)
2. **True 2-variable Bloch-Wigner.** This spike used only
   1-variable $D(z)$ at roots of unity. The Rogers 5-term pentagon
   $D(x) + D(y) + D((1-x)/(1-xy)) + D((1-y)/(1-xy)) + D(1-xy) = 0$
   would give a richer basis when paired arguments span the
   trace-field tower.
3. **Operator-valued $D[Z]$.** The Lean stub of
   `conj:lambda-scale-bring-bloch-identity` has
   `bringBlochRegulator` as `opaque ℝ` — its actual value is
   $D[\sum_i n_i^{(K)}[Z_{K_i}]] \in B(\mathbb{Q}(\zeta_{60})) \otimes \mathbb{Q}$,
   not a 1-component sum. The integer-combination existence is the
   open structural content; PSLQ over individual $D(\zeta_n)$
   values does not capture it.
4. **Non-PSLQ structural identities.** $\lambda_p$ might satisfy a
   transcendental functional equation (e.g. via $\Phi_q$'s
   pentagon identity or the Faddeev quantum-dilog modular
   transformation) that is not captured by linear PSLQ over
   numerical values.

## Cumulative negative tally

| Search | Basis | Coeff bound | Result |
|---|---|---|---|
| `bring_bloch_tier{0..5}_search_m_p.py` | 52 hyperbolic knots through 11-crossing | $10^{30}$ | negative |
| `q_dilog_tower_spike_lambda_scale.py` (PR #923) | 23 elements: $\mathrm{Li}_2^q + \Phi_q$ at substrate-natural | $10^{20}/10^{30}$ | negative |
| **`q_dilog_vhat_spike_lambda_scale.py`** (this spike) | 23 elements: $\hat V_S$ (signed) + ℚ(ζ_60) trace-field $D$ + Tier-0 knots | $10^{30}$ | **negative** |

Three independent searches, all negative. **No integer relation
exists for $\lambda_p$ in any of the tested bases at coefficient
bound $10^{30}$** — note this is an empirical PSLQ-bound finding
and does **not** establish mathematical transcendence (a $\lambda_p$
satisfying a relation with coefficients $> 10^{30}$ or with a
non-tested basis element would not be caught).

## Recommendation

Track as a third consistent-negative tier. The remaining productive
research directions per CLAUDE.md cheat-sheet Migration Backlog #1
are:

1. **Extend $|\hat V_S|$ to higher Hecke levels** — the
   straightforward next spike; basis grows roughly $O(n^2)$ in $n$.
2. **Compute $D[Z]$ for explicit integer combinations** of the
   Tier 0 + 1 hyperbolic knots — this is the path that
   `bring_bloch_tier{1..5}` already exhausted but in a different
   basis structure (PSLQ over $D$ rather than over Vol).
3. **Functional-equation route** — try to derive $\lambda_p$ from
   a $\Phi_q$ modular-transformation identity directly, rather
   than from a linear sum of $\Phi_q$ values.

If 1+2 also exhaust to negative, the empirical case that
`conj:lambda-scale-bring-bloch-identity` is unrealisable in any
hyperbolic-knot or substrate-natural basis would be effectively
closed; the open work would move to direction 3 (functional
equations) or the conjecture should be retired in favour of an
explicit acknowledged-CAL-4 anchor.

## Witness

[`computations/q-dilog-vhat-spike-lambda-scale.witness.json`](../../computations/q-dilog-vhat-spike-lambda-scale.witness.json)
