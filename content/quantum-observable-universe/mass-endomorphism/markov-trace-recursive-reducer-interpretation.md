## Optimisation: memoisation on basis elements

Each $S_n$ has $n!$ basis elements. We memoise the recursive `tr_M` on $(w, n)$ via `functools.lru_cache`. For repeated atom evaluations within a single Python process (e.g., in the multi-atom witness pipeline), we compute basis-element traces once and re-use them. This yields an asymptotic speed-up proportional to the duplication factor across atoms. Empirically, the cache hit rate exceeds 50% on the proton+neutron+deuteron sweep.

## Categorical interpretation

The recursive reducer forms the algorithmic content of the Markov-trace existence theorem for the Iwahori-Hecke algebra. The axioms uniquely determine the trace. The algorithm constructs the unique value for any input word. This contrasts with seminormal/Hoefsmit ascent, which realises the trace via the explicit Wedderburn decomposition $H_n(q) \cong \bigoplus_\lambda M_{f^\lambda}$. Both routes agree on values. The axiomatic route avoids reliance on Hoefsmit matrix elements, which exhibited a known [`IndexError`](https://github.com/litlfred/qou/pull/546) bug on $\sigma_2$ acting on shape $(3)$.
