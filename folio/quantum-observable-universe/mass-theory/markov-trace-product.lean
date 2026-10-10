import QOU.Hecke.MarkovTraceProduct

/-!
# QOU.markov_trace_product — Product factorization of the Markov trace

Content-block sibling of `thm:markov-trace-product`. The block's
`lean.ref` is `qou:QOU.Hecke.markov_trace_product`; the formalisation
lives in the library module `QOU.Hecke.MarkovTraceProduct`.

**One class, not two (bean `qou-ekga`, owner decision C, 2026-10-10).**
This file used to carry a near-verbatim duplicate of the library
development under `QOU.Braiding` — its own `R_q`, `GeneratorChain`,
`vertexVolume`, `MarkovTraceAxioms` and theorems. Two content-bearing
classes with the same name and fields can drift silently, and an
instance of one is not an instance of the other. The duplicate is
retired: this file imports the canonical library module and re-exports
its declarations under `QOU.Braiding`, so every name formerly declared
here (`QOU.Braiding.MarkovTraceAxioms`, `QOU.Braiding.markov_trace_flatten`,
…) still resolves — now to the single canonical declaration.

Two deliberate differences from the retired copy:

- `QOU.Braiding.markov_trace_product` now resolves to the library form
  `(z) (hz) (n) (q) chains`. The retired copy took an implicit `n`, the
  arguments in a different order, and an extra `_traceValue : R_q` that
  its own comment recorded as unused in the conclusion.
- The degree bound is `QOU.Hecke.markovTraceProduct_degree_bound`;
  `QOU.Braiding.degree_bound` is kept as a theorem delegating to it.

**Scope.** The class axiomatises the chain-list model of the Markov
trace and has exactly one inhabitant per `z` (`trace = chainProduct z`);
see the library module docstring.

LaTeX label: `thm:markov-trace-product`

## References

- [jones1987] https://doi.org/10.2307/1971403
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

namespace QOU.Braiding

export QOU.Hecke (R_q q_param q_inv_param GeneratorChain vertexVolume
  MarkovTraceAxioms chainProduct chainProductMarkovTrace MarkovTraceProduct
  markov_trace_product markov_trace_product_recursion chainProduct_append
  markov_trace_nil markov_trace_singleton markov_trace_pair markov_trace_append
  chainProduct_flatten markov_trace_flatten stabChain vertexVolume_stabChain
  markov_trace_stabChains markov_trace_stabilise markov_trace_disjoint_stabilise)

-- Field projections, so `QOU.Braiding.MarkovTraceAxioms.trace` (and
-- `.trace_nil`, `.trace_cons`) keep resolving after the merge.
namespace MarkovTraceAxioms
export QOU.Hecke.MarkovTraceAxioms (trace trace_nil trace_cons)
end MarkovTraceAxioms

/-- **Degree bound `≤ n² − 1`** — the canonical
    `QOU.Hecke.markovTraceProduct_degree_bound`, kept under its former
    content-block name. -/
theorem degree_bound (mtp : MarkovTraceProduct)
    (d k : Fin (mtp.n - 1) → ℕ)
    (hw : ∀ i, d i ≤ 2 * k i + 1)
    (hbudget : (∑ i, (2 * k i + 1)) ≤ mtp.n ^ 2 - 1) :
    (∑ i, d i) ≤ mtp.n ^ 2 - 1 :=
  QOU.Hecke.markovTraceProduct_degree_bound mtp d k hw hbudget

end QOU.Braiding
