The non-commutative random variables $\sigma_i \in H_\infty(q)$ under the Markov trace $\mathrm{tr}_M$ satisfy the pair-partition combinatorial hypothesis of Blitvić's non-commutative central limit theorem. 

Blitvić's theorem applies when joint moments $\mathrm{tr}_M(\sigma_{i_1} \sigma_{i_2} \cdots \sigma_{i_k})$ decompose as a sum over pair-partitions $\pi$ with weights depending only on $\pi$ and $q$. The Hecke relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ reduces every generator word to a combination of square-free products. The Markov property then evaluates the trace as a sum over matchings. 

Explicitly, for the centred generator $\tilde\sigma_i := \sigma_i - \mathrm{tr}_M(\sigma_i) \cdot 1$, the joint moment vanishes for odd $k$. For even $k$, it decomposes as:
$$
  \mathrm{tr}_M\bigl(\tilde\sigma_{i_1} \cdots \tilde\sigma_{i_k}\bigr)
  \;=\;
  \sum_{\pi \in P_2(k)}
    W(\pi; q) \cdot \prod_{\{a, b\} \in \pi}
      \delta_{i_a = i_b}.
$$
The weight function $W(\pi; q)$ depends on the crossing count of $\pi$ and aligns with Blitvić's $(q, t)$-Gaussian moment kernel at $t = 1$. This structural decomposition provides the required input for the QOU q-CLT.
