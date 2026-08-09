
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
