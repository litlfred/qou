## Optimisation: memoisation on basis elements

Each $S_n$ has $n!$ basis elements; the recursive `tr_M` is
memoised on $(w, n)$ via `functools.lru_cache`. For repeated atom
evaluations within a single Python process (e.g. in the multi-atom
witness pipeline), basis-element traces are computed once and
re-used, giving an asymptotic speed-up proportional to the
duplication factor across atoms. Empirically, on the
proton+neutron+deuteron sweep the cache hit rate exceeds 50%.
