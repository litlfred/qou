**Non-commutative probability reading.** Translating to the
dictionary
([rem:non-commutative-probability-dictionary](#rem:non-commutative-probability-dictionary)):

- *Markov locality* = the conditional expectation of a new
  random variable given the past is a fixed scalar (the analogue
  of conditional independence for non-commutative random variables).
- *GS non-locality* = the joint distribution depends on the *full*
  word — analogous to a Markov chain's joint law depending on
  the full sample path even though each step is conditionally
  independent of the past given the present state.
- *Product factorisation* = the joint law decomposes as a product
  over states once the chain is in normal form — the
  non-commutative analogue of writing $P(X_1, \ldots, X_N) =
  P(X_1) \prod_{i \geq 2} P(X_i \mid X_{i-1})$ for a classical
  Markov chain.

In this reading, GS reduction is the non-commutative analogue of
*finding the stationary representation* of a Markov chain: a
single global computation that, once done, permits local stepwise
evaluation.
