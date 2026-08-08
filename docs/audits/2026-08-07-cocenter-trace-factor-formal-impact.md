# Formal-graph impact analysis — `QOU/Information/CocenterTraceFactor.lean`

Date: 2026-08-07. Skill: `lean-formal-graph` (folio-paper-adapter).

## Scope

The module landed across four commits on this branch's predecessor work:

- `9150b096` — the trace factors through the cocenter `HH_0 = A/[A,A]`
- `a7d0cdbe` — the `K0`/Euler-characteristic wrong-axis corollary
- `e9198f15` — any decision separator must be a non-trace
- `065ee97e` — `CocenterTraceFactor` consumes the shared `BilinearTrace.IsCyclic`

Six declarations:

| decl | kind |
|---|---|
| `commutatorSubmodule` | `def` |
| `cocenter` | `abbrev` |
| `commutatorSubmodule_le_ker_of_trace` | `theorem` |
| `trace_eq_of_sub_mem_commutator` | `theorem` |
| `trace_add_commutator` | `theorem` |
| `not_trace_of_separates_commutator` | `theorem` |

## Graph provenance — read this before quoting the numbers

`content-graph` reported `cache ABSENT — formal graph unavailable`, which
per the skill means **`n/a`, not "no dependencies"**. The cache was
populated with the **`--scan` fallback**, not Lean Atlas:

| `formalSource` | what may be concluded |
|---|---|
| `atlas` | authoritative |
| **`scan` (this run)** | **indicative** — syntactic; misses `simp`/instance/unfolding edges, can over-report a coincidental name |

A missed edge *shrinks* results, which is the dangerous direction. Treat
the cone below as a lower bound.

Corpus totals after ingest: 2959 blocks, 4151 editorial edges
(`uses[]`), 485 formal edges from 1186 block-owned declarations.

## Result: the module is unwired

| probe | result |
|---|---|
| content blocks whose `lean.ref` resolves into the module | **0** |
| other `.lean` files invoking any of the six declarations | **0** |
| Lean-level importers | 1 — `QOU.lean` only (the root aggregator, which imports everything) |
| appearances in the formal-graph cache | 0 |

The formal impact cone is empty in both directions: nothing in the
corpus depends on these declarations, and they back no content block.

The graph-cache zero is partly definitional — `--scan` indexes
*block-owned* declarations, and this module owns no block, so it could
not appear. The load-bearing evidence is the independent one: a grep for
each declaration name across the entire `lean/` tree returns no invoker
outside the defining file.

## What this does and does not mean

It does **not** mean the result is wrong or unimportant. The module is
sorry-free and self-contained, and the mathematical content stands.

It does mean the work is **not consumed** — the same class the
`compute-prop-has-consumer` / `compute-prop-has-probe` criteria exist to
catch, here on the proof side. A result reachable only through the root
aggregator import is invisible to every per-block checker: no
`<block>.qa.json` sidecar covers it, so `proof-*`, `wall-*`, `voice-*`
and the rest never score it. That is the standalone-library-Lean blind
spot AGENTS.md §"QA is agent-owned" already names.

## Honest next step

Wiring is a content decision, not a mechanical one — it needs a block
that genuinely wants to state the cocenter factorisation, with the
narrative to match. Two candidate framings exist in the corpus already
(the P≠NP-in-QOU two-axis map, and the trace-blind-to-`[A,A]`
observation), but choosing between them is an authoring call and is
**not** made here.

Until then the module should be regarded as landed-but-unwired, and any
claim that it "supports" a corpus result would be unsupported by the
formal graph.
