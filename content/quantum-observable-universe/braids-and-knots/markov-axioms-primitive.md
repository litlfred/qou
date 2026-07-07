The Markov trace $\tau_M$ on the Iwahori-Hecke algebra $H_n(R, q)$ is the unique linear functional satisfying:

1. **Normalisation:** $\tau_M(1) = 1$.
2. **Cyclicity:** $\tau_M(xy) = \tau_M(yx)$ for all $x, y$.
3. **Stabilisation by $\sigma_n$:** $\tau_M(x \sigma_n) = z \cdot \tau_M(x)$, where $z = 1/(\sqrt q + 1/\sqrt q)$ is the Markov-Jones parameter.
4. **Stabilisation by $\sigma_n^{-1}$:** $\tau_M(x \sigma_n^{-1}) = z \cdot \tau_M(x)$.

These axioms force $\tau_M$ to be the non-degenerate Jones-Markov trace. Iterating the stabilisation axiom implies that the joint Markov trace of two braids acting on disjoint strand sets factorises:
$$
  \tau_M(K_1 \sqcup K_2) \;=\; \tau_M(K_1) \cdot \tau_M(K_2) \cdot z^k,
$$
where $k$ is the number of disjoint strands stabilised. This derives the inter-knot decoupling theorem from primitive Markov axioms.
