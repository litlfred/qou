Let $R$ be a commutative ring and $q \in R^{\times}$ an invertible element with a chosen square root $q^{1/2}$. The Markov trace $\mathrm{tr}_M$ on the Iwahori-Hecke algebra $H_n(R, q)$ is the unique linear functional satisfying:

1. **Normalisation:** $\mathrm{tr}_M(1) = 1$.
2. **Cyclicity:** $\mathrm{tr}_M(xy) = \mathrm{tr}_M(yx)$ for all $x, y$.
3. **Stabilisation by $\sigma_n$:** $\mathrm{tr}_M(x \sigma_n) = z \cdot \mathrm{tr}_M(x)$ for $x \in H_n(R, q)$, where $z = 1/(q^{1/2} + q^{-1/2})$ is the Markov-trace loop value.

Stabilisation by $\sigma_n^{-1}$ — often listed as a fourth axiom — is not an independent condition. Substituting the Hecke quadratic relation $\sigma_n^{-1} = \sigma_n - (q - q^{-1})$ into axiom 3 and using linearity with axiom 1 forces
$$
  \mathrm{tr}_M(x \sigma_n^{-1}) \;=\; z_{-} \cdot \mathrm{tr}_M(x),
  \qquad
  z_{-} \;:=\; z - (q - q^{-1}),
$$
so the negative-crossing loop value $z_{-}$ differs from $z$ whenever $q \neq \pm 1$. No choice of trace parameter makes the two stabilisations scale by mutually inverse factors either: $z \cdot z_{-} = 1$ has the sole solutions $z = q$ and $z = -q^{-1}$, the one-dimensional characters of $H_n(R, q)$, both of which are degenerate. Link invariance of the Jones polynomial is instead restored by the writhe prefactor outside the trace ([Jones–Markov trace](#thm:jones-markov-trace)).

Axioms 1–3 force $\mathrm{tr}_M$ to be the non-degenerate Jones-Markov trace. Iterating the stabilisation axiom implies that the joint Markov trace of two braids acting on disjoint strand sets factorises:
$$
  \mathrm{tr}_M(K_1 \sqcup K_2) \;=\; \mathrm{tr}_M(K_1) \cdot \mathrm{tr}_M(K_2) \cdot z^k,
$$
where $k$ is the number of disjoint strands stabilised. This derives the inter-knot decoupling theorem from primitive Markov axioms.
