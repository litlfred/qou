## Proof

By the Markov property
([Jones–Markov trace](#thm:jones-markov-trace)), applying
$\mathrm{tr}_M$ to $\sigma_0 \sigma_1 \sigma_0$:

1. $\mathrm{tr}_M(\sigma_0 \sigma_1 \sigma_0)
   = z \cdot \mathrm{tr}_M(\sigma_1 \sigma_0)$
   (Markov property on rightmost $\sigma_0$, which has
   maximal index in the word)

2. $\mathrm{tr}_M(\sigma_1 \sigma_0)
   = z \cdot \mathrm{tr}_M(\sigma_0)$
   (Markov property on $\sigma_1$)

3. $\mathrm{tr}_M(\sigma_0) = z$
   (single generator)

Therefore $\mathrm{tr}_M(\sigma_0 \sigma_1 \sigma_0) = z^3$.

The vertex volume product formula assumes that the Hecke
reduction of each generator is independent — this holds
when generators are **non-adjacent** (commuting), but fails
for the trefoil $\sigma_0 \sigma_1 \sigma_0$ where $\sigma_0$
and $\sigma_1$ satisfy the Yang–Baxter relation
$\sigma_0 \sigma_1 \sigma_0 = \sigma_1 \sigma_0 \sigma_1$.

## Impact

With $\mathrm{tr}_M(e^-) = z^3$:
- The Gram matrix is corrected
- The mass ordering $\mathfrak{m}_{\mathfrak{n}} >
  \mathfrak{m}_{\mathfrak{p}}$ is restored
  ([mass ordering](#rem:mass-ordering-corrected))
- The confinement LP solution is modified
  ([confinement LP](#prop:confinement-lp))
