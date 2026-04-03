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
| Mentions only $\mathbf{C}, A, \omega$, categorical trace, Frobenius | GENERAL |
| Uses $M$ (manifold), $E_n$ (total space), $J^1 E$ (jet bundle) | ARCHIMEDEAN |
| Uses $\mathrm{SU}(2)$, $\mathrm{U}(1)$, Killing form, Haar measure | ARCHIMEDEAN |
| Uses Stokes, Leray-Serre, CW-complex, $\pi_1$ monodromy | ARCHIMEDEAN |
| Uses $\mathbb{P}^1(\mathbb{C})$, $S^2$, exceptional divisors | ARCHIMEDEAN |
| Uses multiplicative integral MI∫, holonomy Hol | ARCHIMEDEAN |
| Uses hyperbolic volume, Chern-Simons, CODATA | ARCHIMEDEAN |
| Uses only idempotent splitting, Frobenius trace, Schur in $\mathbf{C}$ | GENERAL |

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

## Audited critical paths

### Path 1: thm:qu-to-qou (Main theorem — QU → QOU)

14 objects, 7 tiers. All .lean files exist, 0 sorry, all SU(2) examples present.

```
Tier 0 (terminal):
  def:rigid-monoidal-category          GENERAL
  def:yekutieli-lifting-condition      GENERAL

Tier 1:
  def:quantum-universe                 GENERAL
  thm:su2-emergence                    GENERAL (statement), ARCHIMEDEAN (proof via Tannaka-Krein)

Tier 2:
  def:quantum-observable-universe      GENERAL
  prop:spin-labels                     GENERAL

Tier 3:
  def:maximal-torus                    GENERAL
  prop:jet-prolongation                GENERAL

Tier 4:
  def:projective-line-object           GENERAL
  def:recursive-brane-tower            GENERAL

Tier 5:
  prop:fiber-adjoint-involution        GENERAL
  def:quantum-characteristic-classes   GENERAL
  prop:yekutieli-lifting               GENERAL

Tier 6 (target):
  thm:qu-to-qou                       GENERAL (statement), MIXED (proof items 4-5 use P(V) geometry)
```

### Path 2: cor:mass-identity-C (Archimedean mass corollary)

9 unique objects. Crosses the archimedean wall at the `-C` suffix.

```
Tier 0 (terminal):
  def:rigid-monoidal-category          GENERAL

Tier 1:
  def:quantum-universe                 GENERAL

Tier 2:
  def:substrate-parameter              GENERAL
  def:quantum-observable-universe      GENERAL

Tier 3:
  ex:c-quantum-universe                ARCHIMEDEAN (SU(2) / manifold realisation)
  prop:jet-prolongation                GENERAL

Tier 4:
  def:c-quantum-observable-universe    ARCHIMEDEAN (CR manifold + gauge bundle)
  def:recursive-brane-tower            GENERAL

Tier 5:
  def:mass-identity                    GENERAL (categorical trace)

Tier 6 (target):
  cor:mass-identity-C                  ARCHIMEDEAN (applies mass-identity to C-QOU)
```

### Path 3: thm:topological-mass (Topological decomposition of mass)

22 unique objects, 7 tiers. Largest critical path. Entirely above the
archimedean wall (categorical).

```
Tier 0 (terminal):
  def:rigid-monoidal-category          GENERAL
  def:yekutieli-lifting-condition      GENERAL

Tier 1:
  def:quantum-universe                 GENERAL
  def:substrate-parameter              GENERAL
  thm:su2-emergence                    GENERAL / ARCHIMEDEAN PROOF

Tier 2:
  def:quantum-observable-universe      GENERAL
  def:quantum-gauge-group              GENERAL
  rem:j1e-local-states                 ARCHIMEDEAN (jet bundle geometry)

Tier 3:
  prop:jet-prolongation                GENERAL
  lem:descent                          GENERAL

Tier 4:
  def:recursive-brane-tower            GENERAL
  def:descent-involution               GENERAL
  def:brane-boundary                   GENERAL
  def:direct-limit-algebra             GENERAL
  def:quantum-characteristic-classes   GENERAL

Tier 5:
  def:mass-identity                    GENERAL
  rem:q-harmonic-basis-brane           GENERAL
  rem:weight-space-decomposition-brane GENERAL
  rem:betti-numbers-brane              GENERAL
  rem:algebraic-filter                 GENERAL

Tier 6:
  prop:descent-eigenspaces             GENERAL

Tier 7 (target):
  thm:topological-mass                 GENERAL (statement + categorical proof)
                                       ARCHIMEDEAN (second proof via manifolds)
```

### Cross-path overlap

Objects shared across all three paths (the "backbone"):
- `def:rigid-monoidal-category` → `def:quantum-universe` →
  `def:quantum-observable-universe` → `prop:jet-prolongation` →
  `def:recursive-brane-tower` → `def:mass-identity`

Objects unique to `thm:topological-mass`:
- `def:descent-involution`, `def:brane-boundary`, `lem:descent`,
  `prop:descent-eigenspaces`, `rem:algebraic-filter`,
  `rem:weight-space-decomposition-brane`, `rem:q-harmonic-basis-brane`,
  `rem:betti-numbers-brane`, `def:direct-limit-algebra`

Objects unique to `cor:mass-identity-C`:
- `def:c-quantum-observable-universe`, `ex:c-quantum-universe`,
  `def:substrate-parameter`

## Audit checklist

When auditing a critical path, check every object for:

1. **Lean completeness**: .lean file exists? sorry count? status accurate?
2. **SU(2) example**: *-su2.ts/.md pair exists? Listed in `examples[]`?
3. **Logical consistency**: `uses[]` matches actual .md cross-references?
4. **Notational consistency**: $\mathbf{C}$ (bold, Herrlich–Strecker style)
   for categories, Frobenius--Hopf hyphenation, $n \geq 0$ vs $n \geq 1$, etc.
5. **Context classification**: GENERAL vs ARCHIMEDEAN — flag mismatches
6. **Cross-references**: all `(#label)` links resolve to existing blocks?

## Output format

Produce a table with columns:
| Block | Classification | Archimedean signals | Action needed |

Follow with specific recommendations, using AskUserQuestion for
mathematical strategy decisions (with structured options, not
free-text questions).
