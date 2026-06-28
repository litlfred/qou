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
