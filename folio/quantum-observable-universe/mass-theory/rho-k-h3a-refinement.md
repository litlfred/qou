**Proposition (conditional on [hoefsmit-scattering-pipeline conjecture](#conj:hoefsmit-scattering-pipeline)).**

*Fix an atom $K$ with $A = Z + N$ nucleons and braid word $\mathcal{B}_K \in B_{3A}$, and let $\Lambda$ be the list of partitions $\lambda \vdash 3A$ carried by the Wedderburn decomposition. Suppose the categorical density satisfies the division-free refinement balance*

$$
  \bigl(\rho_K(q) - \rho_K^{\mathrm{LO}}(Z, N)\bigr)\cdot|\mathrm{tr}_M(\mathcal{B}_K)|
  \;=\;
  \sum_{\lambda \in \Lambda}
    y_\lambda(q)\,\chi^\lambda(\mathcal{B}_K)\,\Delta_\lambda(K) .
$$

*Then at any anchor with $|\mathrm{tr}_M(\mathcal{B}_K)| > 0$ the density decomposes as*

$$
  \rho_K(q)
  \;=\;
  \rho_K^{\mathrm{LO}}(Z, N)
  \;+\;
  \frac{1}{|\mathrm{tr}_M(\mathcal{B}_K)|}
  \sum_{\lambda \in \Lambda}
    y_\lambda(q)\,\chi^\lambda(\mathcal{B}_K)\,\Delta_\lambda(K),
$$

*and if $\Delta_\lambda(K) = 0$ for every $\lambda \in \Lambda$ then $\rho_K(q) = \rho_K^{\mathrm{LO}}(Z, N)$. At an anchor with $|\mathrm{tr}_M(\mathcal{B}_K)| = 0$ the balance instead forces the correction sum itself to vanish, and constrains $\rho_K$ not at all.*

The leading-order piece $\rho_K^{\mathrm{LO}}$ isolates the constituent mass. The residual block-binding correction $\Delta_\lambda(K)$ encodes the specific interaction mass added by each Wedderburn block.

The mass formula $M(K) = \rho_K \cdot m_e \cdot |\mathrm{tr}_M(\mathcal{B}_K)|$ defines $\rho_K$, so the decomposition above says where the binding contribution sits rather than how accurate $M(K)$ is: given the balance, the whole of $\rho_K - \rho_K^{\mathrm{LO}}$ is carried by the partition-indexed $\Delta_\lambda$ profile. The collapse at $\Delta_\lambda \equiv 0$ is stated as part of the claim rather than as commentary because it follows from the balance and is not a separate assertion. The result is a decomposition parallel to the phenomenological six-term narrative, conditional on the scattering pipeline.

The partition list $\Lambda$ is fixed with the atom rather than quantified over. That is not a presentational choice: a hypothesis asserting the displayed identity *for every* list of partitions would force the correction sum to be independent of the list it sums over, which fails as soon as a single $y_\lambda \chi^\lambda \Delta_\lambda$ term is nonzero.
