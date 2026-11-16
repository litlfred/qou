In the VOA formalism, each vertex volume $\hat{V}_i$ is the correlation function of a single vertex operator insertion:

$$
  \hat{V}_i(q) = \bigl\langle Y(\sigma_i, z_i) \bigr\rangle_{\mathrm{Markov}}.
$$

For a generator-monotone braid, the product formula represents the exact factorization of the $n$-point correlation function into one-point functions. This factorization is a direct consequence of the Markov property, and it fails for words whose generators interleave ([Markov trace product](#thm:markov-trace-product)). Each generator acts at a distinct insertion point on $\mathcal{S}_p$, ensuring their independence because they occupy distinct points on $\mathbb{P}^1(\mathbb{C})$.

The degree bound $\deg P_\beta \leq n^2 - 1$ follows from the conformal weight. The total conformal weight of the product is bounded by $\sum_i (2k_i + 1) \leq (n-1)(n+1) = n^2 - 1$.

## The factorization chain

$$
  \mathbb{Z}[B_n] \to H_n(R, q) \to \prod_{i} (a_i \sigma_i + b_i) \to \prod_{i} \hat{V}_i(q) = P_\beta(q)
$$

The chain applies to generator-monotone $\beta$. The value $P_\beta(q) = \mathrm{tr}_M(\rho(\beta))$ is invariant under conjugation of $\beta$, but it is not a link invariant of $\hat{\beta}$: stabilisation multiplies the raw trace by $z$, so a link invariant needs the writhe normalisation.
