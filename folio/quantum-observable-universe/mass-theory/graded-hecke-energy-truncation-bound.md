*Let $\mathcal{B}_K \in B_n$ be a braid, $\hat{\beta}_K$ its closure, and $\mathfrak{M}_K$ its highest-weight KLR module. The mass-spectrum generating function:*

> **Scope.** The hypothesis is a genuine braid, and that is not vacuous but it is also not the atomic object. The atomic Hecke word $W(Z,N) \in H_{3A}(q)$ carries `averaged` letters $\sigma_g - (h/2)\cdot\mathbf{1} = (\sigma_g + \sigma_g^{-1})/2$, which lie outside the image of $\rho : B_n \to H_n(q)$ — measured, no atom from protium to ${}^{56}$Fe is free of them — so it has **no closure** and $\hat{\beta}_K$ is undefined for it. This statement therefore applies to the fundamental knots, whose words are genuine braids, and to a resolved branch of an atomic word, but not to the atomic word itself.

$$
  P_K(q) \;=\; \sum_{d \in \mathbb{Z}} \dim_R \mathrm{Hom}_{\mathcal{K}_n}(P_d, \mathfrak{M}_K) \, q^d
$$

*has at most $\ell(K, q_0) + 1$ nonzero terms, where $\ell(K, q_0)$ is the confinement level at $q_0$.*

This bound reduces computational cost. Canonical evaluation only needs to enumerate degrees $d \le \ell(K, q_0)$, instead of all $p(n)$ partitions. It enables stratified caching and limits combinatorial explosion.
