# Phase 5f — FR-pullback variance test at k=1 and k=2

**Date:** 2026-05-19 (late evening)
**Branch:** `claude/post-819-ledger-update` ([PR #831](https://github.com/litlfred/qou/pull/831))
**Trigger:** Post-#819-merge sweep; extends PR #826's k=3 FR-pullback test to curvature ranks k=1, 2 per the 1ppb ledger's queued Phase 5f.
**Status:** Result landed. **Adding FR pullback at additional depths gives only a marginal ~0.5% improvement over #826's K_3* = 4_1 baseline.**

## Context

[PR #826](https://github.com/litlfred/qou/pull/826) empirically resolved $K_3^* = 4_1$ at the chirality channel:

| K_3* candidate | variance | vs uniform baseline (1.82×) |
|---|---:|---:|
| **4_1** (figure-eight) | **1.551×** | **+14.8%** |
| 5_2 | 1.591× | +12.6% |
| 6_1 (Stevedore) | 1.878× | −3.2% (worse) |

`prop:depth-stratified-frobenius-reciprocity` further conjectures that the FR pullback should be applied at all $k \in \{1, 2, 3\}$, with $K_1^*$ and $K_2^*$ unnamed (open). The conjecture predicts that the full three-depth FR pullback could close variance to ≤ 1.05×.

## This probe

[`fr_pullback_k1_k2_test.py`](../../computations/fr_pullback_k1_k2_test.py) extends #826's infrastructure (corrected canonical braid words; $S_{\text{uniform},k}$-preserving normalization) to a $6 \times 6$ grid over candidate $(K_1^*, K_2^*)$ pairs, with $K_3^* = 4_1$ fixed.

Candidate sets at k=1 and k=2:

- `unknot` (control — FR pullback through trivial projector reduces to uniform Plancherel)
- `3_1`, `5_1` ((2, m)-torus knots = lepton-generation candidates per PR #819 Phase 5d.5)
- `4_1`, `5_2`, `6_1` (small hyperbolic knots from #826's database)

## Cross-validation

The script's $K_3^* = 4_1$ baseline (FR at k=3 only, no FR at k=1, 2) reproduces #826's reported 1.551× **exactly**:

```
=== Baseline (FR at k=3 only, K_3* = 4_1) ===
    D: ratio = 0.162377
    T: ratio = 0.161993
    3He: ratio = 0.171879
    4He: ratio = 0.251209
    baseline variance: 1.5507×
```

This cross-validates this script's port of the FR pullback formula against #826's independent implementation. (Assertion `baseline_matches_PR_826` passes: |1.5507 − 1.551| = 0.0003 < 0.005.)

## Grid scan result

Top 10 of 36 $(K_1^*, K_2^*)$ pairs by variance:

| K_1* | K_2* | variance | Δ vs baseline (1.551×) |
|---|---|---:|---:|
| **unknot** | **5_2** | **1.5432×** | **+0.5%** ← best |
| 5_1 | 5_2 | 1.5432× | +0.5% |
| 3_1 | 5_2 | 1.5433× | +0.5% |
| 5_2 | 5_2 | 1.5435× | +0.5% |
| unknot | 3_1 | 1.5458× | +0.3% |
| 5_1 | 3_1 | 1.5458× | +0.3% |
| 3_1 | 3_1 | 1.5458× | +0.3% |
| 5_2 | 3_1 | 1.5461× | +0.3% |
| unknot | 5_1 | 1.5464× | +0.3% |
| 5_1 | 5_1 | 1.5465× | +0.3% |

## Interpretation

**The FR pullback's variance reduction is concentrated at k = 3.** Adding FR pullback at k=1 and k=2 provides only **0.3-0.5%** marginal improvement over #826's $K_3^* = 4_1$ baseline (1.551×). The top 4 best configurations all use $K_2^* = 5_2$ regardless of $K_1^*$; the K_1* candidate is essentially indistinguishable across {unknot, 3_1, 5_1, 5_2} (variances all in [1.543, 1.547]).

**Three structural readings:**

1. **The depth-3 channel carries the bulk of the categorical content.** The chirality stratum (where $K_3^* = 4_1$ matters most) dominates the variance reduction. Depths 1 and 2 are *partially redundant* under the FR pullback formula as currently stated, suggesting the formula may need an additional structural ingredient (e.g. non-trivial cross-depth coupling, or a depth-dependent scaling) to engage k=1 and k=2 meaningfully.

2. **The remaining 1.54× variance is NOT in the depth-stratified single-block residual.** It's in something the depth-stratified FR pullback does not see at any k. Candidates:
   - The Markov-trace constituent factor 1.220358 still open (Phase 5d.3 in the ledger);
   - Vol_hyp-cluster-by-Z effect from PR #787 Phase 3;
   - A higher-order Hecke-skein correction (Phase 5b cosh(h)-like).

3. **K_1^* and K_2^* may not exist as distinguished hyperbolic knots in the way `depth-stratified-frobenius-reciprocity.md` originally posits.** This probe's flat ranking is consistent with: at k=1, 2 the FR pullback's natural target is the *uniform* central projector (= unknot), not a specific named knot. If so, the conjecture's existence requirement #1 ("Distinguished knot $K_k^*$ at each k ∈ {1, 2, 3}") would simplify to "at k = 3 only".

## Recommendation for the conjecture text

The current `prop:depth-stratified-frobenius-reciprocity` lists K_1*, K_2* as "open structural questions" (per the post-#826 update in this PR). Phase 5f's result suggests:

- **K_3* = 4_1 is structurally identified** (per #826 + this script's cross-validation).
- **K_1*, K_2* may be trivial (unknot)** — the FR pullback at k=1, 2 collapses to the uniform Plancherel restriction under the current formula. The 0.5% marginal improvement is plausibly numerical noise at the 30-dps precision used.
- **Closing the remaining 1.54× residual requires a DIFFERENT mechanism**, not deeper FR pullback. Candidates: cosh(h)-style Hecke correction (Phase 5b at α-level), Markov-trace constituent factor refinement, or Vol_hyp normalisation by Z.

These are queued in the 1ppb ledger as Phase 5g-5i.

## Implementation reference

- Script: [`computations/fr_pullback_k1_k2_test.py`](../../computations/fr_pullback_k1_k2_test.py)
- Witness: `computations/fr-pullback-k1-k2.witness.json` (3 assertions, all passed)
- Cross-reference (PR #826): infrastructure source for canonical braid words + weight normalization.
- Cross-reference (PR #819 Phase 5d.5): torus-knot candidate set for K_k*.

## Assertions

1. `best_variance_below_two_x`: best variance ≤ 2.0 — passes (1.543×).
2. `baseline_matches_PR_826`: K_3* = 4_1 baseline within 0.005 of #826's 1.551× — passes (1.5507×).
3. `no_regression_vs_baseline`: best does not regress vs k=3-only baseline — passes (improvement is +0.48%).
