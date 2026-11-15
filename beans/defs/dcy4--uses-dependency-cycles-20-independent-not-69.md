---
# dcy4
title: 'uses[] dependency cycles: 20 independent, not 69 — 16 are mutual pairs'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T13:46:44Z
updated_at: 2026-10-04T15:25:20Z
parent: qou-hqo3
---

`detangler-no-dependency-cycle` reports **69 failing blocks**, surfaced when the
detangler axis went live in #4867 (it had returned `n/a` almost everywhere
before, so these had never been triaged).

**69 reports is not 69 problems.** Every block sitting on a cycle reports the
same cycle. Building the graph from the reported chains and running Tarjan:

| | count |
|---|---|
| failing blocks (reports) | 69 |
| distinct nodes involved | 69 |
| **true independent cycles (SCCs)** | **20** |

Sizes: one 14-node SCC, one 9-node, three 4-node, four 3-node, and eleven
2-node.

## Why this is unambiguous, unlike the forward-ref backlog

The sibling finding — 294 `detangler-no-forward-ref` edges — turns on an
editorial question: whether a long-range `uses[]` edge means "the reader must
have read this first" or is being used loosely as "related to". That needs an
owner ruling before it is actionable.

**A cycle needs no such ruling.** If A requires B and B requires A, there is no
reading order that satisfies both, under either interpretation of `uses[]`. All
20 are defects.

## Cheapest first: 16 mutual pairs

Each is a single either/or — one direction is the real prerequisite, the other
is backwards or should not be a `uses[]` edge at all:

- `conj:bring-hyperbolic-knot-bloch-decomposition` <-> `prop:em-coupling-bring-zero-mode`
- `conj:crossing-graded-mass-expansion` <-> `conj:lifted-crossing-locality`
- `def:adelic-substrate` <-> `def:classical-limit-functor`
- `def:classical-limit-functor` <-> `def:classical-limit-obstruction`
- `def:q-flat-connection` <-> `def:q-local-system`
- `prop:braiding-eigenvalue-extraction` <-> `prop:tannaka-krein-reconstruction`
- `prop:explicit-central-idempotent` <-> `prop:hecke-baer-star-generic`
- `prop:graded-hecke-energy-truncation-bound` <-> `rem:mass-spectrum-generating-function`
- `prop:hecke-convergence-bound` <-> `rem:body-asymptotics-catalog`
- `prop:pn-averaging-uniqueness` <-> `thm:averaging-resonance-rule`
- `prop:q-beta-categorical-precision-ladder` <-> `prop:tau-M-asymptotic-rep-theory`
- `prop:spectral-chart-correspondence` <-> `rem:affine-chart-origin-of-i-and-q`
- `rem:hausdorff-dimension-classical-comparison` <-> `rem:hausdorff-dimension-recurrence`
- `rem:hyperbolic-overlap-saturation` <-> `rem:townsend-biot-savart-strain`
- `rem:information-theoretic-time-arrow` <-> `rem:information-theoretic-time-properties`
- `rem:information-theoretic-time-julia-microscopic` <-> `rem:information-theoretic-time-properties`

Note `rem:information-theoretic-time-properties` appears in two of them, and
`def:classical-limit-functor` in two — those two blocks are worth reading first.

## Highest-leverage edges in the larger SCCs

Edge frequency across all reported cycles. Cutting the top four breaks the
14-node component:

| appears in | edge |
|---|---|
| 14 | `prop:q-beta-categorical-precision-ladder` -> `prop:tau-M-asymptotic-rep-theory` |
| 12 | `rem:markov-trace-inductive-limit` -> `rem:braid-group-n-strand` |
| 12 | `prop:tau-M-asymptotic-rep-theory` -> `prop:q-beta-c-k-recursion-from-habiro-q-difference` |
| 12 | `prop:q-beta-c-k-recursion-from-habiro-q-difference` -> `rem:markov-trace-inductive-limit` |
| 9 | `rem:knot-particle-dictionary` -> `rem:building-block-knots` |
| 9 | `rem:building-block-knots` -> `def:antineutrino-knot` |
| 9 | `def:antineutrino-knot` -> `prop:parity-violation-skein` |
| 9 | `prop:parity-violation-skein` -> `def:beta-decay-skein` |

The 9-node beta-decay/particle component is a single cycle through
`rem:knot-particle-dictionary` -> `rem:building-block-knots` ->
`def:antineutrino-knot` -> `prop:parity-violation-skein` -> `def:beta-decay-skein`.

## Not done here, deliberately

`uses[]` is authored editorial content — the agent/human-maintained reader
relation, not the machine-derived `lean.ref` graph. Per AGENTS.md it is the
signal every ordering metric is computed from, and #4673 left it to the owner on
the same grounds. This bean is the diagnosis; the edge-direction calls are the
owner's.

Reproduce: parse `detangler-no-dependency-cycle` evidence out of
`folio/quantum-observable-universe/**/*.qa.json`, split each chain on `->`,
build the digraph, run Tarjan for SCCs with more than one node.
