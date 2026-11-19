# Canonical $(q^2 - 1)$ factor of the Markov trace difference

Assume a concrete triple of canonical Wenzl–Markov weights on $H_3(q)$ is given, supplying weights $y_{(3)}(q)$, $y_{(2,1)}(q)$, and $y_{(1,1,1)}(q)$ satisfying the dimension-normalisation relation $y_{(3)}(q) + 2 \, y_{(2,1)}(q) + y_{(1,1,1)}(q) = 1$ for $q > 0$. 

Define the canonical trace difference $\Delta\mathrm{tr}_M^{\text{can}}(q)$ as the weighted sum:

$$
  \Delta\mathrm{tr}_M^{\text{can}}(q) =
  y_{(3)}(q) \chi_{(3)}(q)
  + y_{(2,1)}(q) \chi_{(2,1)}(q)
  + y_{(1,1,1)}(q) \chi_{(1,1,1)}(q).
$$

For $q > 0$, the trace difference factors as:

$$
  \Delta\mathrm{tr}_M^{\text{can}}(q) = (q^2 - 1) P^{\text{can}}(q),
$$

where

$$
  P^{\text{can}}(q) = y_{(3)}(q) P_{(3)}(q) + y_{(2,1)}(q) P_{(2,1)}(q) + y_{(1,1,1)}(q) P_{(1,1,1)}(q).
$$

Here $P_\lambda(q)$ form the per-block polynomial factors from [the per-block character closed forms](qbeta-per-block-chi-closed-forms.md). In particular, $\Delta\mathrm{tr}_M^{\text{can}}(1) = 0$.

## Cross-references

- Parent block: [per-block character closed forms](qbeta-per-block-chi-closed-forms.md) (establishes the per-block $\chi_\lambda$ closed forms and the dimension-normalisation hypothesis).
- Sibling: [classical-point vanishing of $\mathfrak{Q}_\beta/E_0$](../mass-theory/q-beta-over-e0-classical-vanishing.md) (shows the classical-point vanishing of the upstream object $S(q) = \mathfrak{Q}_\beta/E_0$).

