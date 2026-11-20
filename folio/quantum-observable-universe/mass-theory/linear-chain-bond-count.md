**Proposition (bond-count multiplicity).**
*The canonical atomic braid is a **linear chain** of $A$ nucleon blocks
(consecutive blocks joined by a single inter-nucleon crossing). Consequently, in
the body-order (jet-filtration) binding [Binding many-body series equals the jet-order filtration: $B(K)=\sum_n m_e\,a_D^{(n)}$](#conj:binding-manybody-eq-jet-filtration),*

- *the number of consecutive $n$-nucleon sub-clusters is $A-n+1$, and*
- *each $n$-nucleon sub-chain carries exactly $n-1$ inter-nucleon bonds,*

*so the body-order multiplicity is the **bond count** $M_n = n-1$. The aggregate
bond-weighted cluster measure of the $A$-chain is the tetrahedral (binomial) number*

$$
  \sum_{n=2}^{A} (A-n+1)\,(n-1)
  \;=\; \binom{A+1}{3}
  \;=\; \frac{(A-1)\,A\,(A+1)}{6}.
$$

Reindexed by $k = n-1$ this is $\sum_{k=0}^{A-1}(A-k)\,k$, and the identity
follows by induction on $A$.

The multiplicity $M_n = n-1$ fixes the per-body-order weight of the θ_λ residue
$w_n(K) = M_n\,\mathrm{Vol}_n(K)$ with **no fitted constant** — the count is the
inter-nucleon bond number of the derived linear chain, and $\mathrm{Vol}_n(K)$ is
the hyperbolic volume of the $n$-body sub-link (the isospin carrier).

**Scope.** Only the *combinatorial multiplicity* is asserted here. The binding
*magnitude* $B(K) = \mathfrak{m}_e \sum_{n} M_n\,\mathrm{Vol}_n(K)$ — which
reproduces the tritium binding to $\approx 0.16\%$ with no fit
(`theta_mn_bondcount_linearchain.py`) — is an *empirical* consequence that also
multiplies in the topological link volumes and the electron scale $\mathfrak{m}_e$;
it is **not** part of this proposition, and it carries a $\sim 3\%$ mirror-pair
residual plus a deuteron ($\mathrm{Vol}=0$ Hopf) exception.
