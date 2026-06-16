# v9 (1+q)/2 — Categorical Derivation Attempt

**Date:** 2026-05-31
**Branch:** `claude/brave-mendel-FPxFl`
**Sibling PR:** #1581 (Finding C — empirical uniqueness audit)
**Related PR:** #1579 (this audit / probe)
**Status:** PARTIAL — categorical NARRATIVE found, but not a derivation

## Question

Option E v9 (commit `30c5393b7`) closes the (³H, ³He) mirror-pair binding-
energy difference to 0.11% via:

```
B_T − B_³He = m_π · ℏ_q · (1+q)/2 · Σ_λ y_λ · (χ^λ(β_T) + χ^{λᵀ}(β_³He))/2
```

Sibling PR #1581 (Finding C) confirmed `(1+q)/2` is UNIQUE within 0.11%
across 33 q-arithmetic candidates. The OPEN QUESTION carried forward was:

> *"What's STILL OPEN: a categorical derivation that PRODUCES (1+q)/2
> from the Reeb-phase / canonical-cheat-sheet chain."*

This audit attempts that derivation.

## Method

The probe script
[`computations/probes/v9_one_plus_q_categorical_derivation_probe.py`](../../computations/probes/v9_one_plus_q_categorical_derivation_probe.py)
tests 7 candidate categorical derivations at 50 dps:

| # | Candidate | Categorical narrative |
|---|---|---|
| (a) | mirror-symm crossing average | $(q^0 + q^1)/2$ — vacuum + positive crossing |
| (b) | $(1 + \sigma)/2$ symmetric eigenvalue | identity-plus-generator on symmetric block |
| (c) | Reeb phase midpoint | midpoint of trivial-rep $\chi = 1$ and positive-crossing $\chi = q$ |
| (d) | $\mathrm{tr}_M((1+\sigma)/2)$ Hoefsmit $z = q$ | half-trace of identity-plus-generator in Hoefsmit normalisation |
| (e) | p-n mirror-swap projection | $(\sigma + 1)/2$ as one-crossing-to-smoothing average |
| (f) | $[2]_q / 2$ quantum dim averaging | DISTINGUISHING TEST — bar-symmetric $(q + q^{-1})/2$ |
| (g) | antipode-twisted $(1 + \sigma)/2$ | Hopf-algebra averaging across $S(\sigma) = \sigma^{-1}$ |

For each, we check four constraints:

- **C1.** $q \to 1$ limit must equal 1 (classical mirror-pair collapse)
- **C2.** At $q = q_0 \approx 1.10998$, value must equal $(1 + q_0)/2 \approx 1.054989$
- **C3.** Bar-symmetry behaviour consistent with mirror-pair structure
- **C4.** Arises from a specific categorical object (not arbitrary algebra)

## Findings

### Six narratives all algebraically yield $(1+q)/2$

Candidates (a), (b), (c), (d), (e), (g) all evaluate to $(1+q)/2$
**by construction**. They all pass C1 and C2 trivially. So the algebraic
factor is over-determined: many categorical-sounding narratives lead to the
same final algebra. This means **the factor cannot be uniquely "derived"
by uniqueness alone** — the discriminator is whether the proposed
categorical chain is canonical, not whether the algebra works.

### Candidate (f) is the discriminator: $(1+q)/2$ is NOT bar-symmetric

The probe's key finding is that $(1+q)/2$ is the **unique** representative
among quantum-arithmetic naturals that is **NOT** invariant under
$q \mapsto q^{-1}$:

| Form | At $q_0$ | Bar-symmetric? |
|---|---|---|
| $(1 + q)/2$ | $1.05498929\ldots$ | **NO** |
| $(1 + q^{-1})/2$ | $0.95045914\ldots$ | (the conjugate) |
| Difference | $0.10453015\ldots$ | $= h/2 = (q - q^{-1})/2$ |
| $[2]_q/2 = (q + q^{-1})/2$ | $1.00544843\ldots$ | YES |

So $(1+q)/2 = 1 + h/2$ exactly — it is the **first-order chirality
correction** in $h$. The bar-symmetric analogue $[2]_q/2$ misses by
$-4.70\%$ at $q_0$.

### The proposed categorical chain

The probe argues the candidate chain is:

```
step 1 (Cat action)        σ_i → q  on the symmetric eigenspace V_(n)
step 3 (Markov trace)      tr_M((1 + σ)/2 · 𝟙) = (1 + q)/2 (Hoefsmit z = q)
step 6 (Frobenius pairing) chirality factor 1 + h/2 on antipode-twisted average
step 9 (Archimedean)       evaluate at q₀ → numerical 1.054989
```

This routes through three of the canonical-derivation cheat-sheet steps;
it is **not** the Reeb-phase route originally proposed in the question.

## Gap — the missing justification

The chain ASSUMES that the canonical averaging operator on the p-n
interface for **mirror-pair differences** is $(1+\sigma)/2$ — NOT
$(\sigma + \sigma^{-1})/2$ which is the canonical-cheat-sheet's documented
**production** convention (§5q v2: "uniform bar-invariant projection"
$\sigma_{\mathrm{avg}} = (\sigma + \sigma^{-1})/2 = \sigma - h/2$).

The argument for $(1+\sigma)/2$ instead of $(\sigma + \sigma^{-1})/2$ is:

- The mirror-pair difference $B_T - B_{³He}$ is **chirality-odd by isospin
  parity** — ³H and ³He are related by Z↔N swap, which under the Hopf
  antipode action becomes $\sigma \leftrightarrow \sigma^{-1}$ on each
  p-n interface.
- The chirality-odd component of the canonical averaging operator is
  $(\sigma - \sigma^{-1})/2 = h/2$ (an h-coefficient, not an averaging
  factor). But $(\sigma + 1)/2 = 1 + (\sigma - 1)/2$ on the symmetric
  eigenspace contributes an additive shift $1 + h/2$ that matches
  $(1+q)/2$ at $q = q_0$.

This is a **NARRATIVE**, not a derivation, because the choice between
$(\sigma + \sigma^{-1})/2$ (bar-invariant, gives $[2]_q/2$) and
$(\sigma + 1)/2$ (chirality-odd, gives $(1+q)/2$) is not forced by the
canonical chain. The chain SUPPORTS both; production picked the former
for SCALAR isotope mass, and v9 implicitly picks the latter for ISOTOPE-
PAIR DIFFERENCES.

## Verdict

**PARTIAL.** The probe identifies a categorical narrative
that lands on $(1+q)/2$ via the cheat-sheet chain (steps 1, 3, 6, 9), and
identifies the distinguishing structural feature: $(1+q)/2$ is the unique
**chirality-odd** averaging compatible with the substrate Hecke action
that does NOT collapse to the bar-symmetric $[2]_q/2$.

But **the derivation is incomplete** because the choice of $(1+\sigma)/2$
(chirality-odd) over $(\sigma + \sigma^{-1})/2$ (bar-symmetric) on the
p-n interface for mirror-pair differences is currently a NEW ad-hoc
choice — the production-canonical convention is the latter.

To upgrade from PARTIAL to DERIVED, the missing step is a categorical
proof that **mirror-pair differences project onto the chirality-odd
component of the canonical averaging operator** — perhaps via:

1. **Hopf-antipode S-action.** The mirror swap $Z \leftrightarrow N$
   acts on Hecke generators via $\sigma \mapsto \sigma^{-1}$ (the Hopf
   antipode $S$). The mirror-pair difference is then projected onto
   the anti-S-fixed component, which is the chirality-odd part.
2. **Reeb-phase difference at the mirror axis.** Per the cheat-sheet's
   "Binding carrier = per-rep q-Reeb phase $\theta_\lambda$" finding,
   the mirror pair closes when each chiral pair $(\lambda, \lambda^T)$
   contributes a phase difference $\Delta\theta_\lambda$ projected onto
   the chirality-odd component.
3. **Two-class normalization** distinguishing "isotope-scalar" (bar-
   symmetric, $(σ + σ^{-1})/2 → [2]_q/2$) from "isotope-difference"
   (chirality-odd, $(σ + 1)/2 → (1+q)/2$).

None of these three justifications is currently formal; they are the
research-grade follow-up direction.

## Constraints any valid categorical derivation must satisfy

Per the probe's analysis:

| Constraint | Requirement |
|---|---|
| C1 | $f(q \to 1) = 1$ |
| C2 | $f(q_0) = (1 + q_0)/2 = 1.05498929\ldots$ |
| C3 (chirality) | $f$ must be **chirality-odd**: $f(q) - f(q^{-1}) \neq 0$ at $q \neq 1$ |
| C4 | $f$ must arise from a canonical Hecke / Markov-trace / Hopf-algebra construction |

Of the 7 candidates, all 6 chirality-odd ones (a, b, c, d, e, g)
satisfy C1, C2, C3; only the bar-symmetric (f) violates C3. So
the chirality-odd structure is **necessary** but the specific Hecke
construction is over-determined.

## Status classification

Per CLAUDE.md "Production-vs-Exploratory" discipline and PR #1581's
TIERED reporting convention:

| Tier | Claim |
|---|---|
| **fit** | (1+q)/2 found by 33-candidate q-arithmetic scan (PR #1581 Finding C) |
| **near-match (categorical)** | (1+q)/2 = first-order chirality correction $1 + h/2$; this audit |
| **proved** | not reached — requires categorical justification of $(1+σ)/2$ vs $(σ+σ^{-1})/2$ choice |

The v9 formula remains in the **"near-match"** tier — promoted from
"fit-selected" (#1581) to "near-match with categorical narrative"
(this audit) — but not yet "categorically derived".

## Cross-references

- Probe script:
  [`computations/probes/v9_one_plus_q_categorical_derivation_probe.py`](../../computations/probes/v9_one_plus_q_categorical_derivation_probe.py)
- Witness:
  `computations/probes/v9-one-plus-q-categorical-derivation-probe.witness.json`
- v9 baseline:
  [`computations/option_e_v9_all_symmetries.py`](../../computations/option_e_v9_all_symmetries.py)
  (commit `30c5393b7`)
- #1581 audit (empirical uniqueness):
  [`computations/audits/option_e_v9_one_plus_q_structural_audit.py`](../../computations/audits/option_e_v9_one_plus_q_structural_audit.py)
- Canonical chain:
  [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
- CLAUDE.md §7a (Hecke-Skein eigenvalue conventions)
- Cheat-sheet §5q v2 (production averaging $\sigma_{\mathrm{avg}} = (\sigma + \sigma^{-1})/2$)
- Audit
  [`2026-05-27-pion-half-figure-eight.md`](2026-05-27-pion-half-figure-eight.md)
  (half-Reeb-rotation precedent)

## Follow-up work

1. **Hopf-antipode justification of chirality-odd averaging.** Prove that
   the mirror-swap $Z \leftrightarrow N$ acts on the p-n interface via
   the Hopf antipode $S(\sigma) = \sigma^{-1}$ (not just as a labeling
   change), and that the **isotope-pair difference** projects onto the
   anti-S-fixed component.
2. **Per-block Reeb-phase difference at chirality-odd projection.**
   Re-derive the v9 formula starting from the q-Reeb phase
   $\theta_\lambda = \arccos(\chi^\lambda(\mathcal{B})/d_\lambda)$
   (per `option_e_q_reeb_phase_probe_v4.py`) and check whether the
   chirality-odd projection naturally pulls out $(1 + q)/2$ as a
   global prefactor.
3. **Cross-check against `closed_form_tau_M.py` Phase 5q.** That module
   exposes `pn_convention="strict_averaged"` (math-correct $z - h/2$
   averaging) and `pn_convention="bring_color_weighted"` (the open
   research direction). The chirality-odd derivation could be a third
   `pn_convention` option for ISOTOPE-PAIR DIFFERENCES.
