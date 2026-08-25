---
# dtg7
title: 'forward-ref backlog: 294 edges, diffuse — needs a uses[] semantics ruling first'
status: todo
type: task
priority: normal
created_at: 2026-08-09T13:46:44Z
updated_at: 2026-08-09T13:46:44Z
---
`detangler-no-forward-ref` reports **257 failing blocks / 294 edges**, surfaced
when the detangler axis went live in #4867. The axis had returned `n/a` almost
everywhere before, so this backlog has never been triaged.

The findings are **genuine and precise**, e.g.

```
braids-and-knots/coxeter-parabolic-transversal.ts:
  forward ref: uses def:hecke-normal-form (manifest pos 46)
  which appears after this block (pos 32) in the chapter
```

Since `uses[]` is the reader relation, that tells a reader at block 32 to have
already read block 46.

## Do not expect a quick win — it is diffuse

| | |
|---|---|
| edges | 294 |
| failing blocks | 257 |
| top-10 referenced targets | **only 10% of edges** |
| median position gap | 19 |
| max position gap | **611** |

There is **no small set of "move these blocks earlier" fixes**. Concentration by
chapter:

| chapter | edges |
|---|---|
| mass-theory | 103 (35%) |
| quantum-observable-universes | 34 |
| information-theory | 23 |
| predicted-spectra | 22 |
| fluid-dynamics | 16 |
| observations | 14 |

## The extremes suggest a semantics problem, not an ordering problem

The largest gaps are all in `mass-theory`:

| gap | block (pos) | uses (pos) |
|---|---|---|
| 611 | `hoefsmit-ew-cell-content` (140) | `prop:knot-operator-lp-selection` (751) |
| 542 | `hoefsmit-scattering-pipeline` (128) | `conj:geom-yekutieli-alignment` (670) |
| 521 | `toroidal-harmonics-delta-lambda` (214) | `prop:interface-knot-markov-z` (735) |
| 511 | `motivic-mass-rationale` (10) | `prop:mass-endomorphism-tower` (521) |
| 496 | `gram-determinant-plancherel-ratio` (84) | `rem:gram-matrix-spectral-connection` (580) |

`motivic-mass-rationale` at position 10 declaring it `uses` the mass-endomorphism
tower 511 blocks later does not read like a prerequisite. It reads like a block
that **motivates** the tower — i.e. `uses[]` being used to mean "related to"
rather than "the reader must have read this first".

## The ruling this needs

Which is it, for long-range edges?

1. **Genuine prerequisites** -> the fix is reordering, and it is large structural
   work concentrated in `mass-theory`.
2. **Mis-typed "related to" links** -> the fix is removing or re-directing those
   `uses[]` entries, which is cheaper and also improves every ordering metric
   computed from the relation.

The answer changes what the work is, so triage should not start before it is
settled. AGENTS.md is explicit that `uses[]` is the editorial signal every
ordering metric derives from and that it must never be populated mechanically —
so this is an owner call, as #4673 also concluded.

## Related

- `dcy4` — the 69 dependency-cycle reports. Those collapse to 20 real cycles and
  are **unambiguous** defects needing no ruling, so they are the better place to
  start.
