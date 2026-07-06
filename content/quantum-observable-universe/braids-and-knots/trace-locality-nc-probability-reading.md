**Non-commutative probability reading.** Translating via the dictionary ([rem:non-commutative-probability-dictionary](#rem:non-commutative-probability-dictionary)):

- *Markov locality*: The conditional expectation of a new random variable given the past is a fixed scalar. This is the non-commutative analogue of conditional independence.
- *GS non-locality*: The joint distribution depends on the full word. This parallels a classical Markov chain where the joint law depends on the full sample path, even though each step is conditionally independent of the past given the present state.
- *Product factorisation*: The joint law decomposes as a product over states once the chain is in normal form. This is the non-commutative analogue of writing $P(X_1, \ldots, X_N) = P(X_1) \prod_{i \geq 2} P(X_i \mid X_{i-1})$ for a classical Markov chain.

In this reading, Gröbner–Shirshov reduction is the non-commutative analogue of finding the stationary representation of a Markov chain. It is a single global computation that, once completed, permits local stepwise evaluation.
