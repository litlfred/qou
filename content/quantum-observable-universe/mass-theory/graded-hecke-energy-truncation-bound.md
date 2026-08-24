*Let $\hat{\beta}_K$ be the closure of $\mathcal{B}_K \in B_n$ and $\mathfrak{M}_K$ its highest-weight KLR module. The mass-spectrum generating function:*

$$
  P_K(q) \;=\; \sum_{d \in \mathbb{Z}} \dim_R \mathrm{Hom}_{\mathcal{K}_n}(P_d, \mathfrak{M}_K) \, q^d
$$

*has at most $\ell(K, q_0) + 1$ nonzero terms, where $\ell(K, q_0)$ is the confinement level at $q_0$.*

This bound reduces computational cost. Canonical evaluation only needs to enumerate degrees $d \le \ell(K, q_0)$, instead of all $p(n)$ partitions. It enables stratified caching and limits combinatorial explosion.
