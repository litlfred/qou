# ⁴He Sub-lemma 2.1 multi-interface extension at H_12 — math + plan

**Date:** 2026-05-16
**Branch:** `claude/crystal-and-he4-combined`
**Status:** Scaffold (math derivation only). Phase 2 substantive
compute deferred — Hoefsmit cold-start at H_12 (77 partitions of 12,
some dim ≥ 297) takes ~minutes per partition × ~5-25 min total per
chi evaluation. F1's full sum took 221 s for canonical ⁴He
([`he4-canonical-tr-m-block-fingerprint.witness.json`](../../computations/he4-canonical-tr-m-block-fingerprint.witness.json)).

## Background — three-fold iterated Sub-lemma 2.1

PR #666 closed the **two-interface** case at H_9 (tritium, ³He) via
the Halley-refined Hecke Wedderburn projector branching basis:

$$
\chi^\lambda(\beta_K) = \sum_{\xi, \nu} c^\lambda_{\xi\nu} \cdot \mathrm{Tr}_{V_\xi \otimes V_\nu}\bigl( A^\lambda_{\xi\nu}(I_2) \cdot (\rho_\xi(W_{\mathrm{inner}}) \otimes \rho_\nu(\beta_3)) \bigr)$$

for $W_{\mathrm{inner}} = \beta_1 \cdot I_1 \cdot \beta_2 \in H_6$.

For ⁴He at canonical pppnnn ordering, the braid has **3 inter-nucleon
interfaces** and lives in $H_{12}$:

$$
\beta_{^4\mathrm{He}} \;=\; \beta_{p_1} \cdot I_{pp} \cdot \beta_{p_2} \cdot I_{pn} \cdot \beta_{n_1} \cdot I_{nn} \cdot \beta_{n_2}
$$

with $\beta_{p_i}, \beta_{n_j} \in H_3$ (3 strands per nucleon),
$I_{pp} = \sigma_2$, $I_{pn} = \sigma_5 - h/2$, $I_{nn} = \sigma_8 - h$.

## Iterated 3-interface formula

Apply Sub-lemma 2.1 at the outermost split $H_{12} \downarrow H_9 \times H_3$:

$$
\chi^\lambda(\beta_{^4\mathrm{He}}) \;=\; \sum_{\eta \vdash 9, \, \nu_4 \vdash 3} c^\lambda_{\eta, \nu_4} \cdot \mathrm{Tr}_{V_\eta \otimes V_{\nu_4}}\bigl( A^\lambda_{\eta, \nu_4}(I_{nn}) \cdot (\rho_\eta(W_{\mathrm{tritium}}) \otimes \rho_{\nu_4}(\beta_{n_2})) \bigr)
$$

where $W_{\mathrm{tritium}} = \beta_{p_1} \cdot I_{pp} \cdot \beta_{p_2} \cdot I_{pn} \cdot \beta_{n_1} \in H_9$.

Recurse: $\rho_\eta(W_{\mathrm{tritium}})$ as a matrix-valued operator
on $V_\eta$ comes from PR #666's H_9 branching at $H_9 \downarrow H_6 \times H_3$.
And $\rho_\xi(\beta_{p_1} \cdot I_{pp} \cdot \beta_{p_2})$ inside that
uses the inner-most H_6 branching at $H_6 \downarrow H_3 \times H_3$
(the deuteron case, PR #534 / merged).

Three nested LR sums:

$$
\boxed{\quad
\chi^\lambda(\beta_{^4\mathrm{He}}) \;=\;
\sum_{\substack{\eta \vdash 9 \\ \nu_4 \vdash 3}}
\sum_{\substack{\xi \vdash 6 \\ \nu_3 \vdash 3}}
\sum_{\substack{\mu \vdash 3 \\ \nu_2 \vdash 3}}
c^\lambda_{\eta, \nu_4} \cdot c^\eta_{\xi, \nu_3} \cdot c^\xi_{\mu, \nu_2}
\cdot \mathrm{Tr}\bigl[ \dots \bigr]
\quad}
$$

with the trace being the iterated composition of A operators acting
on the tensor product $\rho_\mu(\beta_{p_1}) \otimes \rho_{\nu_2}(\beta_{p_2}) \otimes \rho_{\nu_3}(\beta_{n_1}) \otimes \rho_{\nu_4}(\beta_{n_2})$.

## What's needed for Phase 2

### New A-operator extractions

1. $A^\lambda_{\eta, \nu_4}(I_{nn})$ at $H_{12} \downarrow H_9 \times H_3$ — the outer interface.
2. $A^\eta_{\xi, \nu_3}(I_{pn})$ at $H_9 \downarrow H_6 \times H_3$ — already extracted in PR #666!
3. $A^\xi_{\mu, \nu_2}(I_{pp})$ at $H_6 \downarrow H_3 \times H_3$ — needs new extraction for $I_{pp}$ (PR #534 only did $I_{pn}$).

So **two new substantive extractions**: $H_{12}$ for $I_{nn}$, and $H_6$ for $I_{pp}$.

### Verification

- Path A (truth): direct $\chi^\lambda(\beta_{^4\mathrm{He}})$ via Hoefsmit at $H_{12}$ — F1 already did this (221 s total).
- Path B (derivation): iterated 3-level formula above using the branching-basis algorithm from PR #666.
- Target: max rel residual ≤ machine ε across all 77 λ ⊢ 12.

### Compute scope

Per the PR #666 cost analysis:

| step | cost |
|---|---|
| Hoefsmit at $H_{12}$ per λ (cold start) | 5-60 s |
| Hoefsmit at $H_{12}$ per λ (warm) | 50 ms |
| Path A: 77 λ × Hoefsmit + braid product | ~5-15 min |
| Path B: Halley projector at H_9 × H_3 (cached from #666) + nested LR + matrix multiplies | ~few minutes |

Total Phase 2 compute: **~15-30 minutes** for full H_12 verification.

## Why this matters

⁴He at H_12 is the **first multi-interface case beyond tritium**.
Once closed:

1. Δ_λ is canonically derived at H_12 for ⁴He → completes the four
   atoms in the 1-ppb roadmap (D, T, ³He, ⁴He).
2. The same iterated-Sub-lemma-2.1 machinery extends to ⁵Li, ⁶Li,
   etc. at H_15, H_18, … with K^{A-1} nesting depth.
3. F1's two-row stratum [9,3], [8,4], [10,2] carrying 86.5% of
   $\tau_M(\beta_{^4\mathrm{He}})$ would get its **categorical-derivation
   explanation** via the A-operator structure (the V_ξ ⊗ V_ν blocks
   that dominate are exactly those two-row partitions).

## Cross-references

- [PR #666](https://github.com/litlfred/qou/pull/666) — H_9 multi-interface (tritium), 30/30 at machine ε
- [PR #534](https://github.com/litlfred/qou/pull/534) — H_6 single-interface (deuteron), 11/11 at machine ε
- [`docs/audits/2026-05-15-sublemma-2-1-h9-multi-interface-extension.md`](2026-05-15-sublemma-2-1-h9-multi-interface-extension.md) — H_9 scaffold (companion)
- [`docs/audits/2026-05-04-sublemma-2-1-refined.md`](2026-05-04-sublemma-2-1-refined.md) — single-interface operator-valued
- [`computations/sublemma_2_1_h9_branching_basis.py`](../../computations/sublemma_2_1_h9_branching_basis.py) — algorithm to extend
- [`computations/he4-canonical-tr-m-block-fingerprint.witness.json`](../../computations/he4-canonical-tr-m-block-fingerprint.witness.json) — F1's canonical ⁴He compute (Path A reference)

## CAL discipline

Phase 2 (when implemented) will use only $q_0$ (CAL-2). No $m_e$, $Q_\beta$, AME data.
