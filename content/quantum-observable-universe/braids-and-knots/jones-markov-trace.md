Let $q \in \mathbb{C}^{\times}$ not be a root of unity. The Iwahori--Hecke algebra $H_n(\mathbb{C}, q)$ admits a unique $\mathbb{C}$-linear functional $\mathrm{tr}_M$ satisfying:
1. Normalisation: $\mathrm{tr}_M(1) = 1$.
2. Trace property: $\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$.
3. Markov property: $\mathrm{tr}_M(x \sigma_n) = z\,\mathrm{tr}_M(x)$ for $x \in H_n(\mathbb{C}, q)$, where $z = 1/(q^{1/2} + q^{-1/2}) = \mathrm{tr}_M(\sigma_i)$ is the Markov-trace loop value.

Stabilisation by $\sigma_n^{-1}$ is then forced by the Hecke quadratic relation: $\mathrm{tr}_M(x \sigma_n^{-1}) = z_{-}\,\mathrm{tr}_M(x)$ with $z_{-} = z - (q - q^{-1})$ ([Markov axioms](#rem:markov-axioms-primitive)). The two loop values are distinct, and invariance of the resulting link polynomial under both Markov moves is achieved by a writhe-dependent prefactor outside the trace, not by symmetry of the trace itself. The Jones link-invariant normalisation parameter $z_{\mathrm{J}} = (q-1)\,z^2$ that absorbs this prefactor is distinct from $z$ ([reconciliation of the Markov parameter $z$](#rem:markov-z-reconciliation)).

For each partition $\lambda \vdash n$, the restriction of $\mathrm{tr}_M$ to the irreducible $H_n(\mathbb{C}, q)$-module $S_\lambda$ is a non-zero scalar multiple of the character $\chi_\lambda$. For any braid $\beta$, $\mathrm{tr}_M(\rho_n(\beta))$ computes the Jones polynomial of the closure $\hat{\beta}$ up to framing.
