Let $q \in \mathbb{C}^{\times}$ not be a root of unity. The Iwahori--Hecke algebra $H_n(\mathbb{C}, q)$ admits a unique $\mathbb{C}$-linear functional $\mathrm{tr}_M$ satisfying:
1. Normalisation: $\mathrm{tr}_M(1) = 1$.
2. Trace property: $\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$.
3. Markov property: $\mathrm{tr}_M(x \sigma_n^{\pm 1}) = z_{\mathrm{J}}^{\pm 1}\mathrm{tr}_M(x)$, where $z_{\mathrm{J}} = (q - 1)/(q^{1/2} + q^{-1/2})^2$.

The parameter $z_{\mathrm{J}}$ is the Jones (1987) link-invariant normalisation; it is distinct from the Markov-trace loop value $z = 1/(q^{1/2} + q^{-1/2}) = \mathrm{tr}_M(\sigma_i)$ used in all mass and volume computations, and the two are related by $z_{\mathrm{J}} = (q-1)\,z^2$ ([reconciliation of the Markov parameter $z$](#rem:markov-z-reconciliation)).

For each partition $\lambda \vdash n$, the restriction of $\mathrm{tr}_M$ to the irreducible $H_n(\mathbb{C}, q)$-module $S_\lambda$ is a non-zero scalar multiple of the character $\chi_\lambda$. For any braid $\beta$, $\mathrm{tr}_M(\rho_n(\beta))$ computes the Jones polynomial of the closure $\hat{\beta}$ up to framing.
