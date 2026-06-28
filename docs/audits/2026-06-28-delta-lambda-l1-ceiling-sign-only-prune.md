# Δ_λ ℓ¹-ceiling: sign-only fixes are structurally excluded

**Date:** 2026-06-28
**Branch:** `claude/delta-lambda-l1-ceiling-prune-2026-06-28`
**Goal:** Δ_λ binding-closure (Option-E / Track-A)
**Scope tag:** (b) structural-exclusion — invariant cited (triangle / ℓ¹ bound)
**Witness:** [`computations/delta-lambda-l1-ceiling-sign-prune.witness.json`](../../computations/delta-lambda-l1-ceiling-sign-prune.witness.json)
**Producer:** [`computations/delta_lambda_l1_ceiling_sign_prune.py`](../../computations/delta_lambda_l1_ceiling_sign_prune.py)

## Summary

The per-block binding closure (Track D / Option-E) is

$$
\frac{B(K)}{m_e} \;=\; \sum_{\lambda \vdash 3A} y_\lambda(q_0)\,\chi^\lambda(\beta_K)\,\Delta_\lambda(K),
\qquad
\Delta_\lambda \;=\; \operatorname{sgn}\!\big(w_0^{S_{\lambda'}}\big)\cdot \dim_\lambda ,
$$

with the chirality form **proven** sorry-free in Lean (PR #2416,
`S5SO3FiberAction.lean`; `PartitionOf5.deltaSign_mixed`). The published
evaluation undershoots every light isotope (D −82.9 %, T −77.5 %,
³He −69.6 %, ⁴He −89.3 %).

This audit records a **formalize-first** structural bound that prunes one
sub-class of the remaining search. It does **not** propose a closure (the
closure remains open; no 7th fit-based ansatz is offered).

## The invariant

Hold $\{y_\lambda\}$ and $\{\chi^\lambda\}$ at their canonical values and
hold the *magnitude* $|\Delta_\lambda| = \dim_\lambda$ fixed; let only the
per-block **sign** vary — i.e. replace the proven
$\operatorname{sgn}(w_0^{S_{\lambda'}})$ by an arbitrary chirality rule
$s_\lambda \in \{\pm 1\}$. Write $a_\lambda := y_\lambda\,\chi^\lambda\,\dim_\lambda$.
Since $|s_\lambda a_\lambda| = |a_\lambda|$, the triangle inequality gives,
for **every** sign assignment,

$$
\Big| \sum_\lambda s_\lambda\, a_\lambda \Big| \;\le\; \sum_\lambda |a_\lambda| \;=:\; \|c\|_1 .
$$

$\|c\|_1$ is therefore a **hard ceiling** on the binding magnitude
reachable by *any* sign- or chirality-only re-derivation acting on the
existing term set.

## The measurement

| isotope | net $\Sigma$ / target | $\|c\|_1$ / \|target\| | net / $\|c\|_1$ |
|---------|----------------------:|----------------------:|----------------:|
| D       | 0.171 | **0.516** | −0.331 |
| T       | 0.225 | **0.358** | −0.629 |
| ³He     | 0.304 | **0.592** | −0.513 |
| ⁴He     | 0.107 | **0.406** | −0.265 |

- **net / target** = the published undershoot (fraction of target the
  signed sum achieves).
- **$\|c\|_1$ / |target|** = the ℓ¹ ceiling — the most any sign-only fix
  can reach. **Below 1 for all four isotopes (0.36–0.59).**
- **net / $\|c\|_1$** = magnitude surviving cancellation (≈ 0.3–0.6 of the
  available ℓ¹ mass is retained; the remainder cancels).

The reconstruction reproduces the canonical per-atom witness
(`delta-lambda-binding-full-evaluation.witness.json`): D net = −0.7438 vs
−0.7439, B_pred = −0.380 MeV, −82.9 %.

## Conclusion (scope (b), invariant cited)

> **No sign- or chirality-only re-derivation of $\Delta_\lambda$ — keeping
> $y_\lambda$, $\chi^\lambda$ and $|\Delta_\lambda| = \dim_\lambda$ fixed —
> can close the binding deficit.** The ℓ¹ ceiling is 36–59 % of target for
> every light isotope. A **magnitude-adding** ingredient is *necessary*:
> one of
> 1. a re-derived block magnitude $|\Delta_\lambda| \neq \dim_\lambda$
>    (e.g. a different Wedderburn weight),
> 2. a re-weighting of $y_\lambda$, or
> 3. an additional term beyond the single $\Sigma_\lambda$ sum — the T2–T6
>    many-body terms / the A=4 interface operator (PROBE-2).

This is the **magnitude-side mirror of the PROBE-4 KL-positivity prune**
([`docs/audits/2026-06-16-option-e-probe4-kl-positivity-prune.md`](2026-06-16-option-e-probe4-kl-positivity-prune.md)):

| prune | holds fixed | shows the *other* axis cannot be supplied |
|-------|-------------|-------------------------------------------|
| PROBE-4 (KL positivity) | non-negative KL multiplicities supply $|\Delta_\lambda|=\dim$ | …never the chirality **sign** (mixed-sign target) |
| **this (ℓ¹ ceiling)** | the proven sign structure $\operatorname{sgn}(w_0^{S_{\lambda'}})$, optimally reassigned | …never the **magnitude** (ℓ¹ ceiling < target) |

Together they bound the {sign-only} and {current-magnitude-only}
sub-classes from both sides: the missing ingredient must add ℓ¹ mass to
the per-block vector, not merely re-sign or re-order it.

## What this does *not* exclude (anti-over-claim)

Per the (a)/(b) discipline, the exclusion is narrow — it bars only the
sign-only sub-class. It does **not** touch the active magnitude-side
levers, all of which add or reshape ℓ¹ mass and so escape the ceiling:

- **z2bn** (Lever 1, fibre $R(q,x)$ kernel) — re-derives a generating
  function; reshapes magnitude. Not excluded.
- **w5tg** (Lever 2, edge-set/occupancy) — occupancy re-weights terms.
  Not excluded.
- **thb7** (Lever 3, universal-ρ) — a multiplicative scale. The ceiling
  ratios are *non-constant* across isotopes (0.52/0.36/0.59/0.41), so a
  single universal scalar on the per-λ-summed vector cannot hit all four
  — consistent with the C_knot 2.8× spread — but thb7 builds ρ on a
  different (q-Reeb) object, so this is **informative, not a refutation**.
- **PROBE-2** (ae4b/ae42/ae43, A=4 interface operator) — a genuinely new
  many-body term; adds magnitude. Not excluded.

## Reproduction / provenance

Inputs are **read** from canonical pinned witnesses — $y_\lambda(q_0)$
from `y-lambda-at-q0.witness.json`, $\chi^\lambda(\beta_K)$ from
`atom-chi-rust-{d,t,3he,4he}.witness.json`. $\dim_\lambda$ and the sign are
exact combinatorics (hook-length formula + Young-subgroup longest-element
sign $(-1)^{m(m-1)/2}$). The diagnostic is pure ℓ¹ arithmetic on
already-canonical values: no $q_0$ re-solve, no $\mathrm{tr}_M$ recompute,
no `pyhecke`. It is therefore reproducible in any environment and **immune
to the ad-hoc-env witness skew**. The 0.36–0.59 ceiling margin is bounded
away from 1 by ≥ 0.41, far beyond any float64 concern.
