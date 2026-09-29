---
name: verify-local-substrate
roles: [reader, collaborator, owner]
description: >
  Verify that every observational result block traces back to the local U
  substrate (def:substrate-parameter) through the uses[] dependency graph.
  Identifies gaps where observational claims lack a formal connection to the
  substrate parameter, and suggests fixes.
allowed-tools: Read Edit Write Bash Grep Glob Agent
---

# Verify Local Substrate Connectivity

## Overview

This skill checks a key structural invariant of the paper: **every
observational result must trace back to `def:substrate-parameter`**
through the `uses[]` dependency DAG. The substrate parameter $q$ is the
bridge between the categorical framework (Chapters 1–4) and the physical
predictions (Chapter 7). An observational block that does not connect to
the substrate is either:

1. Missing dependency declarations in its `uses[]` array, or
2. Genuinely independent of the $q$-deformation (rare — flag for review)

## Scope

The verification covers:

| Block kinds checked | Where to look |
|--------------------|---------------|
| `proposition` | Ch7 primarily; also Ch5, Ch6 |
| `conjecture` | Ch7 |
| `remark` with tags containing `"observation"`, `"prediction"`, or `"codata"` | All chapters |
| `definition` with tag `"observation"` | Ch2 (`def:observation`) |

## Algorithm

### Step 1: Collect observational blocks

Scan all `.ts` manifest files under `folio/quantum-observable-universe/`
for blocks matching either criterion:

- **Provable blocks in Chapter 7**: any block with kind `proposition`,
  `theorem`, `lemma`, `corollary`, or `conjecture` located in
  `observations/`
- **Tagged observational blocks** (any chapter): any block whose `tags`
  array includes `"observation"`, `"prediction"`, or `"codata"`

### Step 2: Trace each block's dependency chain

For each observational block, perform a breadth-first traversal of
`uses[]` references, resolving labels to `.ts` files and reading their
`uses[]` arrays in turn. Stop when:

- `def:substrate-parameter` is found → **CONNECTED**
- A leaf node (empty `uses[]` or already-visited node) is reached
  without finding substrate-parameter → continue to next branch
- All branches exhausted → **GAP**

Maximum traversal depth: **6 hops** (the deepest known chain is 5).

### Step 3: Classify results

| Status | Meaning | Action |
|--------|---------|--------|
| CONNECTED | Block traces to `def:substrate-parameter` | None |
| GAP | No path found | Add missing `uses[]` entry or flag for review |
| ISOLATED | Empty `uses[]` on an observational remark | Add dependencies |

### Step 4: Report

Output a table:

```
| Block label | Kind | Status | Shortest path | Action needed |
```

For GAPs, suggest which intermediate block should be added to `uses[]`
to restore connectivity. Common fix patterns:

- Remark about experimental data → add `def:substrate-parameter` directly
- Remark about q-deformed observables → add the relevant `def:q-*` block
- Conjecture about particle structure → check if `def:crossing-energy`
  or `def:skein-binding-lagrangian` provides the link

## Known Dependency Chains

These are the verified paths from key observational results to
`def:substrate-parameter`:

### Direct connections (1 hop)

| Block | Path |
|-------|------|
| `prop:local-substrate-q` | → `def:substrate-parameter` |
| `prop:neutron-prediction-comparison` | → `def:substrate-parameter` |
| `rem:bec-vortex-data` | → `def:substrate-parameter` |
| `rem:entropic-gravity` | → `def:substrate-parameter` |
| `rem:proton-radius-puzzle` | → `def:substrate-parameter` |
| `rem:double-slit-two-modes` | → `def:substrate-parameter` |
| `rem:mass-comparison-table` | → `def:substrate-parameter` |
| `rem:magnetic-friction` | → `def:substrate-parameter` |
| `rem:stability-cubic-plot` | → `def:substrate-parameter` |

### Indirect connections (2+ hops)

| Block | Path |
|-------|------|
| `prop:double-slit-massive-pattern` | → `def:double-slit-q-phase` → `def:substrate-parameter` |
| `conj:borromean-quark` | → `def:crossing-energy` → `def:substrate-parameter` |
| `conj:higgs-t28` | → `def:crossing-energy` → `def:substrate-parameter` |
| `rem:cmb-q-torsion` | → `ex:q-reeb-flow` → ... → `def:categorical-q-lie-bracket` → `def:substrate-parameter` |
| `rem:gravity-emergent` | → `rem:gr-substrate-geometry` → `def:q-yang-mills-levi` → `def:substrate-parameter` |
| `rem:substrate-telescope` | → `ex:q-reeb-flow` → ... → `def:substrate-parameter` |
| `rem:lattice-layout` | → `def:q-harmonic-form` → `def:categorical-q-ext-deriv` → `def:substrate-parameter` |
| `rem:crystal-probe-q` | → `prop:local-substrate-q` → `def:substrate-parameter` |
| `rem:observation-brings` (Ch5) | → `def:substrate-parameter` |
| `rem:observation-archimedean` (Ch6) | → `def:substrate-parameter` |
| `def:observation` (Ch2) | → `def:substrate-parameter` |

## Upstream Foundation

The substrate parameter itself traces to the categorical axioms:

```
def:substrate-parameter
├── def:quantum-observable-universe
│   └── def:quantum-universe
│       └── def:rigid-monoidal-category
│           └── def:snake-identity (leaf)
├── def:weight-decomposition
│   ├── def:quantum-observable-universe (see above)
│   ├── def:maximal-torus
│   └── def:higher-forms
└── def:categorical-reeb
    ├── def:maximal-torus
    └── def:weight-decomposition (see above)
```

## Knot Table Connectivity

Knot tables (formula tables, periodic tables, knot-centric tables) are
observational in nature — they tabulate predicted particle masses and
quantum numbers derived from the $q$-deformed knot invariants. Every
knot table must trace to `def:substrate-parameter` because:

1. Knot crossing energies depend on $q$ via `def:crossing-energy`
2. Particle generation numbers depend on $q$ via `def:knot-particle-generation`
3. Mass predictions depend on the local substrate value $q|_U \approx 1.1097$

Known knot table blocks and their connections:

| Block | Path to substrate |
|-------|-------------------|
| `rem:knot-formula-table` | → `def:knot-particle-generation` → `def:substrate-parameter` |
| `rem:knot-centric-table` | → `def:substrate-parameter` (direct) |
| `knot-periodic-table` (prose) | → `def:substrate-parameter` (direct) |

## Checklist

- [ ] All Ch7 propositions trace to `def:substrate-parameter`
- [ ] All Ch7 conjectures trace to `def:substrate-parameter`
- [ ] All blocks tagged `"observation"` trace to `def:substrate-parameter`
- [ ] All blocks tagged `"prediction"` trace to `def:substrate-parameter`
- [ ] All blocks tagged `"codata"` trace to `def:substrate-parameter`
- [ ] No observational block has an empty `uses[]` array
- [ ] Report table is complete with shortest path for each block
- [ ] GAPs have suggested fixes with specific `uses[]` entries to add
