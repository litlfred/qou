*Lean sibling: structural, over a generic commutative ring $R$ (AGENTS.md §7c).*

**Proposition.** Let $\mathcal{F}_A, \mathcal{F}_B$ be two [one-dimensional QOU channels](#def:one-dim-qou-channel) placed in parallel. Because each is bounded by its cladding, the joint configuration is a **split link**: the surface boundary suppresses every crossing between a strand of $\mathcal{F}_A$ and a strand of $\mathcal{F}_B$. The Markov trace is multiplicative over split links, so the transmitted datum of the joint channel factorises,
$$
  \mathrm{tr}_M(\mathcal{F}_A \parallel \mathcal{F}_B) \;=\; \mathrm{tr}_M(\mathcal{F}_A)\,\mathrm{tr}_M(\mathcal{F}_B).
$$

Moreover parallel placement is **associative** and **commutative**, with the vacuum channel as identity. Non-interacting fibres therefore form a commutative monoid under the multiplicative trace: they compose as **independent multiplicative information sources**. This is the same decoupling that governs composite knots — a product over decoupled constituents — and it is precisely why parallel optical fibres carry information without cross-talk.

**Proof.** Split-link multiplicativity of the Markov trace — equivalently the disjoint-union rule for the Kauffman bracket and the Jones polynomial — gives the factorisation directly. Associativity, commutativity, and the identity law are then the corresponding ring identities for the product of trace values. The Lean sibling proves all four over a generic commutative ring $R$ (the factorisation is definitional; commutativity uses only $\mathrm{propext}$). $\qquad\blacksquare$
