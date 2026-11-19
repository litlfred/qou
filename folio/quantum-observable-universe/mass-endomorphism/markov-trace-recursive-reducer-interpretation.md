## Optimisation: memoisation on basis elements

Each $S_n$ has $n!$ basis elements. Memoising the recursive $\mathrm{tr}_M$ evaluation on $(w, n)$ ensures that for repeated atom evaluations within a single run (e.g., in the multi-atom witness pipeline), basis-element traces are computed once and re-used. This yields an asymptotic speed-up proportional to the duplication factor across atoms. Empirically, the cache hit rate exceeds 50% on the proton+neutron+deuteron sweep.

## Categorical interpretation

The recursive reducer forms the algorithmic content of the Markov-trace existence theorem for the Iwahori-Hecke algebra. The axioms uniquely determine the trace. The algorithm constructs the unique value for any input word. This contrasts with seminormal/Hoefsmit ascent, which realises the trace via the explicit Wedderburn decomposition $H_n(q) \cong \bigoplus_\lambda M_{f^\lambda}$. Both routes agree on values. The axiomatic route avoids reliance on Hoefsmit matrix elements.
