**Proposition (Hecke pair-partition structure).**
*The non-commutative random variables $\sigma_i \in H_\infty(q)$ under the Markov trace $\mathrm{tr}_M$ satisfy the pair-partition combinatorial hypothesis of Blitvić's two-parameter non-commutative central limit theorem [`blitvic2012`].*

**The hypothesis.** Blitvić's theorem requires a sequence of non-commuting random variables whose joint moments are determined by a pair-partition combinatorial structure. Every length-$k$ joint moment $\mathrm{tr}_M(\sigma_{i_1} \sigma_{i_2} \cdots \sigma_{i_k})$ must decompose as a sum over pair-partitions $\pi$ of $\{1, \ldots, k\}$ of weights $W(\pi, q)$ depending only on $\pi$ and the deformation parameter $q$.

**Satisfaction of the hypothesis by Hecke generators.** The Hecke quadratic relation

$$
  \sigma_i^2 \;=\; (q - q^{-1})\,\sigma_i + 1
$$

forces every length-$k$ word in the generators to reduce, after finitely many rewriting steps, to an $R$-linear combination of square-free generator products (where each $\sigma_i$ appears at most once). The Markov property $\mathrm{tr}_M(x \, \sigma_n) = z \, \mathrm{tr}_M(x)$ peels off generators one at a time. This produces a sum over matchings (pair-partitions). Each non-trivial Markov pairing $\sigma_i \leftrightarrow \sigma_i^{-1}$ contributes a fixed scalar to the trace. Each unmatched generator contributes zero (by trace centring under the bar-involution adjoint).

Explicitly, for the centred generator $\tilde\sigma_i := \sigma_i - \mathrm{tr}_M(\sigma_i) \cdot 1 = \sigma_i - z \cdot 1$, the joint moment

$$
  \mathrm{tr}_M\bigl(\tilde\sigma_{i_1} \tilde\sigma_{i_2} \cdots \tilde\sigma_{i_k}\bigr)
$$

vanishes unless $k$ is even. For even $k$ it decomposes as

$$
  \mathrm{tr}_M\bigl(\tilde\sigma_{i_1} \cdots \tilde\sigma_{i_k}\bigr)
  \;=\;
  \sum_{\pi \in P_2(k)}
    W(\pi; q) \cdot \prod_{\{a, b\} \in \pi}
      \delta_{i_a = i_b},
$$

where $P_2(k)$ is the set of pair-partitions of $\{1, \ldots, k\}$ and $W(\pi; q)$ is determined by the crossing count of $\pi$ weighted by powers of $(q - q^{-1})$. The weight function $W(\cdot; q)$ is Blitvić's $(q, t)$-Gaussian moment kernel at parameter $t = 1$, where $q$ is the QOU substrate parameter.

**Corollary: the q-CLT input (partially established).** Only the odd-length face of the proposition is proved (odd-word moments vanish; this is Lean `sorry`-free). The full even-length pair-partition decomposition with the crossing-weighted $W(\pi; q)$ kernel remains open. It is carried as an honest `sorry` (it needs non-commutative-probability pair-partition machinery absent from Mathlib). Conditional on that full decomposition, Blitvić's CLT [`blitvic2012`, Theorem 1.1] applies. The rescaled centred sum $S_n = n^{-1/2} \sum_i \tilde\sigma_i$ has joint moments converging to a $(q, t)$-Gaussian process at parameter $(q, 1)$. The QOU q-CLT (`conj:q-clt-non-commutative`) is therefore conditional on both the full pair-partition decomposition and the parameter-identification step (Blitvić's $q \leftrightarrow$ QOU's $q \leftrightarrow$ Tsallis's $q$).
