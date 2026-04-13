The Markov trace of the trefoil braid
$\sigma_0 \sigma_1 \sigma_0$ is $z^3$, **not** $hz^2 + z$
as would be obtained from the vertex volume product formula.
The product factorization
([Markov trace product](#thm:markov-trace-product))
is invalid when generators are **adjacent**.

## Statement

**Proposition.**

$$
  \mathrm{tr}_M(\sigma_0 \sigma_1 \sigma_0) = z^3
$$

*where $z = (1 + h\delta)^{-1}$ is the Markov parameter
and $h = q - q^{-1}$.  The vertex volume product
$\hat{V}_0 \cdot \hat{V}_1 \cdot \hat{V}_0 = hz^2 + z \neq z^3$
does not apply here.*

## Proof

By the Markov property
([Jones–Markov trace](#thm:jones-markov-trace)), applying
$\mathrm{tr}_M$ to $\sigma_0 \sigma_1 \sigma_0$:

1. $\mathrm{tr}_M(\sigma_0 \sigma_1 \sigma_0)
   = z \cdot \mathrm{tr}_M(\sigma_0 \sigma_1)$
   (apply cyclicity to reorder, then Markov property)

2. $\mathrm{tr}_M(\sigma_0 \sigma_1)
   = z \cdot \mathrm{tr}_M(\sigma_0)$
   (Markov property on $\sigma_1$,
   with $\sigma_0 \in H_1(q)$)

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
