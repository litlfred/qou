---
name: critical-path-analysis
description: >
  Analyse the critical path of the paper's argument chain, audit statement
  and proof contexts (e.g. archimedean vs categorical), identify blocks that
  need rewriting, and propose cleanups.  Also covers "statement and proof
  context review" — classifying each result by whether its statement, proof,
  or both require specialisation assumptions.
allowed-tools: Read Edit Write Bash Grep Glob Agent
---

# Critical Path Analysis & Context Review

## Overview

This skill traces the logical dependency chain of the paper from axioms
to final results, classifying every block on the critical path by its
**context assumptions**:

- **GENERAL / CATEGORICAL**: Statement and proof work in any rigid
  monoidal category satisfying the QOU axioms.
- **ARCHIMEDEAN STATEMENT**: The statement itself requires the
  archimedean realisation (manifolds, gauge groups, differential forms).
- **ARCHIMEDEAN PROOF**: Statement is categorical, but the proof uses
  archimedean tools (Stokes theorem, Killing forms, spectral sequences
  over manifolds, Haar measure, etc.).
- **MIXED**: Some parts categorical, some archimedean.

## When to Use This Skill

- "What assumptions does this result actually need?"
- "Is this proof archimedean or categorical?"
- "Which results need rewriting for the general case?"
- "Trace the critical path from X to Y"
- "Audit archimedean dependencies"
- "What's the minimal assumption set for theorem Z?"
- "Separate categorical core from archimedean specialisation"

## Workflow

### 1. Identify the critical path

Read the paper manifest and chapter manifests to trace the dependency
chain via `uses[]` fields.  Build the DAG from the target result back
to the axioms.

### 2. Classify each block

For each block on the critical path, read both the `.md` (narrative)
and `.ts` (manifest) files.  Classify by:

| Signal | Likely classification |
|--------|----------------------|
| Mentions only $\mathcal{C}, A, \omega$, categorical trace, Frobenius | GENERAL |
| Uses $M$ (manifold), $E_n$ (total space), $J^1 E$ (jet bundle) | ARCHIMEDEAN |
| Uses $\mathrm{SU}(2)$, $\mathrm{U}(1)$, Killing form, Haar measure | ARCHIMEDEAN |
| Uses Stokes, Leray-Serre, CW-complex, $\pi_1$ monodromy | ARCHIMEDEAN |
| Uses $\mathbb{P}^1(\mathbb{C})$, $S^2$, exceptional divisors | ARCHIMEDEAN |
| Uses multiplicative integral MI∫, holonomy Hol | ARCHIMEDEAN |
| Uses hyperbolic volume, Chern-Simons, CODATA | ARCHIMEDEAN |
| Uses only idempotent splitting, Frobenius trace, Schur in $\mathcal{C}$ | GENERAL |

### 3. Identify mismatches

Flag blocks where:
- Statement is categorical but proof is archimedean → candidate for
  categorical proof rewrite
- Statement mixes categorical and archimedean language → candidate
  for splitting into two blocks
- Proof uses C*-algebra / Haar measure when algebraic arguments suffice

### 4. Propose actions

For each flagged block, propose one of:
- **Rewrite proof** categorically (when the categorical argument exists)
- **Split statement** into categorical theorem + archimedean corollary
- **Move to archimedean section** (keep content, reorganise placement)
- **Add dual proofs** (categorical + archimedean via `proofs[]` array)
- **Accept as archimedean** (when no categorical alternative exists)

### 5. Architectural conventions

The paper follows a **categorical core + archimedean specialisation**
architecture:

- Categorical results (GENERAL) live in the main sections of each chapter.
- Archimedean specialisations live in a dedicated section
  (`sec:archimedean-lifting` in ch3, `sec:archimedean-qou` in ch1).
- The `-C` suffix on block names denotes archimedean specialisation
  (e.g. `jet-prolongation-C`, `mass-identity-C`).
- Statements that have both categorical and archimedean proofs list
  both in the `proofs[]` array of the `.ts` manifest.
- The categorical proof is listed first; the archimedean proof second.

### 6. Key archimedean boundary in the paper

The critical path flows:

```
Categorical QOU axioms (C, A, ω)
  → Jet prolongation (Kähler differentials, algebraic)
  → Brane tower (categorical descent, idempotent splitting)
  → Mass identity (categorical trace + Frobenius norm)
  → Topological mass decomposition (descent eigenspaces)
  ──── ARCHIMEDEAN WALL ────
  → Archimedean realisation (manifolds, gauge theory)
  → Holonomy, multiplicative integrals, Stokes theorem
  → Quantum dilogarithm evaluation
  → Hyperbolic volume / CODATA mass predictions
```

Everything below the wall requires the archimedean realisation.
Everything above is purely categorical.

## Output format

Produce a table with columns:
| Block | Classification | Archimedean signals | Action needed |

Follow with specific recommendations, using AskUserQuestion for
mathematical strategy decisions (with structured options, not
free-text questions).
