*Fix one coupled spectral datum $D = (\zeta_D, \psi_D, \rho_D)$ consisting of a candidate zeta function $\zeta_D$, its Chebyshev counting function $\psi_D$, and an indexed family of spectral exponents $\rho_D(n, i)$. The conjecture posits the pairwise equivalence of:*

1. **Square-root counting error.** $\psi_D(X) = X + O(X^{1/2 + \delta})$ for every $\delta > 0$.
2. **Critical-line zeros.** Every zero of $\zeta_D$ in the critical strip $0 < \mathrm{Re}(s) < 1$ satisfies $\mathrm{Re}(s) = 1/2$.
3. **Uniform spectral alignment.** Every exponent $\rho_D(n, i)$ satisfies $\mathrm{Re}(\rho_D(n, i)) = 1/2$.

**Epistemic separation.** For the classical pair $(\zeta, \psi)$, the equivalence $(1) \Leftrightarrow (2)$ is a theorem of analytic number theory \cite{vonkoch1901}. By contrast, the equivalence $(2) \Leftrightarrow (3)$ is speculative: no Reeb operator $\xi_q$ whose eigenvalue family $\rho_D$ is coupled to the zeros of the [Riemann zeta function](#conj:classical-riemann-hypothesis) has been constructed.

**Bundling requirement.** The three predicates must be quantified over a single coupled datum $D$: quantifying over $\psi$, $\zeta$, and $\rho$ independently would force the critical-line predicate on $\zeta$ to be constant across all complex functions, contradicting vacuous satisfaction on $\zeta \equiv 1$ and failure at $s = 1/4$ on $\zeta \equiv 0$.
