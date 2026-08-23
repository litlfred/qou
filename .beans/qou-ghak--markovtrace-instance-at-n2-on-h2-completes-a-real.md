---
# qou-ghak
title: MarkovTrace instance at n=2 on H2 — completes a real MarkovTraceContext witness
status: completed
type: task
priority: normal
created_at: 2026-08-09T12:04:21Z
updated_at: 2026-08-09T13:35:05Z
---


`QOU/Hecke/InstanceH2.lean` now gives a real `QOU.Hecke.HeckeAlgebra R 2 q
(H2 R q)`, where `H2 R q = R[X]/(X² − (q − q⁻¹)X − 1)`. The remaining piece for
a **non-degenerate** `MarkovTraceContext` is a `QOU.Hecke.MarkovTrace` on it.

Right now the only `MarkovTraceContext` witness is the `n = 0` one from
qou-xzd5, where `Generator 0` is empty and every axiom holds vacuously. That is
fine for refuting over-general statements and useless as mathematics. An `n = 2`
witness would be the first with actual content, which is what downstream results
quantified over `MarkovTraceContext` need in order to mean anything.

## Why this should be straightforward

`heckePoly` is monic of degree 2 over a field, so `H2 R q` is free of rank 2 with
basis `{1, σ}` (`AdjoinRoot.powerBasis`). Define `trace (a + b·σ) = a + b·z` for
a chosen Markov parameter `z`. Then:

| axiom | why it holds |
|---|---|
| `trace : A →ₗ[R] R` | coordinates in the power basis are `R`-linear |
| `normalised : trace 1 = 1` | coordinate of `1` is `(1, 0)` |
| `cyclic : trace (xy) = trace (yx)` | `H2` is **commutative** — `AdjoinRoot` of a commutative ring |
| `z_param`, `trace_gen : trace σ = z` | by construction |
| `trace_prod_gen` | quantifies over `i.idx < j.idx` in `Fin 1` — **vacuous** |

So the only real work is the power-basis coordinate map; every axiom with
content is either linearity or true by definition.

## What it would unblock

- A `MarkovTraceContext` witness with non-empty generator set, so
  `[ctx : MarkovTraceContext]`-quantified results are conditional on something
  inhabited *and* non-trivial.
- A concrete target for the `H2` Wedderburn/Markov material in
  `QOU/Mathlib/HeckeAlgebra.lean` (`H2Carrier`, `H2.markovTrace`,
  `H2.blockSym` / `blockAlt`), which currently computes with `R × R` and is not
  connected to the `QOU.Hecke` class hierarchy at all. Worth checking whether
  `R × R` (the split form, when the quadratic factors) is the better carrier —
  it would make the trace literally a coordinate sum.

## Not this bean

`n ≥ 3`. There the braid relation stops being vacuous and needs a genuine
construction — the open infrastructure the manuscript keeps citing. `n = 2`
does not approach it.

<!-- recovered 2026-08-23 from orphaned file `qou-ghak--markovtrace-instance-at-n-2-on-h2-completes-a-real.md` (no front-matter; invisible to the tracker) -->

## DONE — `QOU/Hecke/MarkovTraceH2.lean`

| declaration | content |
|---|---|
| `h2Basis` | the `AdjoinRoot` power basis `{1, σ}`, reindexed to `Fin 2` along `heckePoly_natDegree` |
| `coord_zero_one` … `coord_one_sigma` | the four coordinate values |
| `traceMap z` | `tr_M(a·1 + b·σ) = a + b·z`, as an `H2 R q →ₗ[R] R` |
| `traceMap_one`, `traceMap_sigma` | `tr_M(1) = 1`, `tr_M(σ) = z` |
| **`markovTraceH2 z`** | **`MarkovTrace 2 q (H2 R q)` for any `z`** |
| **`contextH2`** | **`QOU.Shared.MarkovTraceContext` over `ℚ`, `q = 2`, `n = 2`, `z = 1`** |
| `contextH2_generator_nonempty` | `Nonempty (Generator contextH2.n)` — the one fact separating it from the `n = 0` witness |

All axiom-clean (`propext, Classical.choice, Quot.sound`).

`markovTraceH2` is a `def`, not an `instance`, and deliberately: `MarkovTrace`
does not index on `z`, so an instance would have to invent a value for
`z = 1/(q^{1/2} + q^{-1/2})` — which needs a square root of `q` in `R`. The
honest statement is that *every* `z` gives a Markov trace, and that is what the
`def` says.

## Stated plainly in the module: two of five axioms are free at n = 2

- `cyclic` — `H₂(q)` is commutative (`AdjoinRoot` of a commutative ring), so
  `tr(xy) = tr(yx)` is `mul_comm`.
- `trace_prod_gen` — quantifies over `i.idx < j.idx` in `Fin 1`, vacuous.

Both are real facts about the two-strand algebra, not gaps. But they mean this
witness is **not evidence for `n ≥ 3`**, where cyclicity has content — the same
caveat `InstanceH2` makes about its own braid and far-commutativity fields.
`QOU.Machinery.MarkovTraceH4` carries cyclicity at `n = 4` as a cited `sorry`
precisely because the `Fin 24` brute force is heartbeat-infeasible.
