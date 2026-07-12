The Markov trace $\mathrm{tr}_M$ on the Iwahori-Hecke algebra $H_n(R, q)$ is the unique linear functional satisfying:

1. **Normalisation:** $\mathrm{tr}_M(1) = 1$.
2. **Cyclicity:** $\mathrm{tr}_M(xy) = \mathrm{tr}_M(yx)$ for all $x, y$.
3. **Stabilisation by $\sigma_n$:** $\mathrm{tr}_M(x \sigma_n) = z \cdot \mathrm{tr}_M(x)$, where $z = 1/(q^{1/2} + q^{-1/2})$ is the Markov-trace loop value.
4. **Stabilisation by $\sigma_n^{-1}$:** $\mathrm{tr}_M(x \sigma_n^{-1}) = z \cdot \mathrm{tr}_M(x)$.

These axioms force $\mathrm{tr}_M$ to be the non-degenerate Jones-Markov trace. Iterating the stabilisation axiom implies that the joint Markov trace of two braids acting on disjoint strand sets factorises:
$$
  \mathrm{tr}_M(K_1 \sqcup K_2) \;=\; \mathrm{tr}_M(K_1) \cdot \mathrm{tr}_M(K_2) \cdot z^k,
$$
where $k$ is the number of disjoint strands stabilised. This derives the inter-knot decoupling theorem from primitive Markov axioms.
