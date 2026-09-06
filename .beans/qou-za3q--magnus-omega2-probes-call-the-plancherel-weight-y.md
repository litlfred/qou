---
# qou-za3q
title: magnus-Omega2 probes call the Plancherel weight y_lambda; 91% of their work is on shapes tr_M annihilates
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T10:49:41Z
updated_at: 2026-09-06T10:50:06Z
---

## What is there

`deltalambda/{deuteron,triton}_magnus_omega2_sign_probe.py` and
`he4_magnus_omega2_sign_sparse_probe.py` each define

    def wedderburn_weight(shape, q):
        """y_λ = d_q(λ)² / [n]_q!  (symmetric q-integers) — same as the A=2 probe."""

and aggregate `P_total = Σ_λ y_λ · tr(ρΩ₂)` over **every** partition. Fifteen
files under `computations/` compute this same form, `substrate/hecke_core.py`
among them.

That is the **quantum Plancherel** weight. It is not the Wenzl Schur principal
specialisation the production Markov trace uses, and the two are not close:

| | (3,) | (2,1) | (1,1,1) |
|---|---:|---:|---:|
| Wenzl y_λ (production) | 0.50540423 | 0.24729789 | **0** |
| d_q²/[n]_q! (these probes) | 0.16338323 | 0.66067377 | 0.16338323 |

At H₉ the divergence is structural, not a rescaling: Plancherel's **largest**
weights sit on shapes production annihilates — (4,3,1,1) and (4,2,2,1) at
0.1463 each, (5,2,1,1) at 0.1063, (4,3,2) at 0.0910 — while the five surviving
≤2-row shapes carry 0.0000017 to 0.0065. Under the Wenzl weight those same
≥3-row shapes are all exactly 0 (row cap, level r = 2; see `qou-fq0f`).

## What I am NOT claiming

That the weight is wrong. `computations/audits/y_lambda_convention_c_fingerprint_audit.py`
already states the row-cap test and flags precisely this trap:

> AGENTS.md is explicit that the three partition-weight families y_λ / w_λ /
> w̃_λ are DISTINCT at q ≠ 1 and must never be conflated, so a hit on a field
> that is not the Wenzl y_λ is a false positive this cannot rule out by itself.

`d_q²/[n]_q!` may well be the right pairing measure for a Magnus Ω₂ sign
question, which is not a Markov trace. I cannot settle that from here.

What IS wrong regardless is the **name**: these docstrings call it `y_λ`, and
the aggregation field in the witness is `y_lambda`. That is the conflation
AGENTS.md forbids, and it is what makes the fingerprint audit unable to
discriminate — it keys on a field *named* `y_lambda`, so these probes are
permanent false-positive candidates in a corpus-wide convention scan.

## Decision needed

1. **Is the Plancherel measure intended here?** If yes, rename it — `w_planch`
   or similar — in all three probes and the twelve other call sites, so the
   corpus has one name per object and the fingerprint audit stops tripping.
   If no, these three probes' results are computed against the wrong measure.
2. **Does the sign survive either way?** Both weight families are strictly
   positive, so a conclusion that is only about the SIGN of `P_total` may be
   robust to the choice. If so, the probes' headline claim stands while the
   naming is fixed — worth checking before treating this as urgent.

## Side finding: the same 91% waste, and a classification

`he4_magnus_omega2_sign_sparse_probe` dispatches over all 77 partitions of 12
and builds `sigma_csr`/`germ_csr` for each, at dimensions to d_λ = 7700. Under
the production weight 70 of those 77 carry weight exactly zero — the same waste
`qou-fq0f` removed from the Wenzl bridge (99.5x). It cannot be removed here
until item 1 is settled: with the Plancherel weight nothing vanishes, so there
is nothing to skip.

**Classification for `qou-hu1f`:** forced to the OLD `grouped` ordering, this
probe ran 33+ CPU-minutes without completing inside a 2700 s budget — the same
outcome it has under `borromean`. It does not complete either way, so its
failure is **pre-existing, not caused by the intra-ordering ruling.** That
closes the last undecided producer from the regeneration pass.
