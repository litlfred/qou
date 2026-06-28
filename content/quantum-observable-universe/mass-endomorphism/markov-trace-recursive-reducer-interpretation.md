## Optimisation: memoisation on basis elements

Each $S_n$ has $n!$ basis elements; the recursive `tr_M` is
memoised on $(w, n)$ via `functools.lru_cache`. For repeated atom
evaluations within a single Python process (e.g. in the multi-atom
witness pipeline), basis-element traces are computed once and
re-used, giving an asymptotic speed-up proportional to the
duplication factor across atoms. Empirically, on the
proton+neutron+deuteron sweep the cache hit rate exceeds 50%.

## Categorical interpretation

The recursive reducer is the algorithmic content of the
**Markov-trace existence theorem** for the Iwahori-Hecke algebra:
the trace is uniquely determined by the axioms, and the algorithm
*constructs* the unique value for any input word. This contrasts
with the seminormal/Hoefsmit ascent
, which
realises the trace via the explicit Wedderburn decomposition
$H_n(q) \cong \bigoplus_\lambda M_{f^\lambda}$. Both routes
agree on values; the axiomatic route avoids any reliance on the
Hoefsmit matrix elements (which had a known
[`IndexError`](https://github.com/litlfred/qou/pull/546) bug on
$\sigma_2$ acting on shape $(3)$).
