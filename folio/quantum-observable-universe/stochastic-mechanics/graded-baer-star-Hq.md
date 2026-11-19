**Conjecture (graded Baer-* on $\mathcal{H}_q$ across the depth filtration).**

*Let $\mathcal{H}_q$ be the substrate convolution Hopf algebra ([Frobenius–Hopf substrate](#def:frobenius-hopf-substrate)), filtered by iterated-integral depth:*

$$
  G^{(0)}(\mathcal{H}_q) \;\subseteq\; G^{(1)}(\mathcal{H}_q)
  \;\subseteq\; G^{(2)}(\mathcal{H}_q) \;\subseteq\; \cdots.
$$

*Each filtration piece $G^{(n)}(\mathcal{H}_q)$ is a Baer-*-ring under the bar involution, and the inclusions $G^{(n)} \hookrightarrow G^{(n+1)}$ are **Baer-*-morphisms**: they send projections to projections and preserve the annihilator-generation property. Equivalently, $\mathcal{H}_q$ admits a system of orthogonal projections $\{p_n^{(i)}\}_{n,i}$ indexed by depth $n$ and intra-depth label $i$, with*

- *each $p_n^{(i)}$ self-adjoint under $* \colon q \mapsto q^{-1}$,*
- *$p_n^{(i)} p_m^{(j)} = 0$ when $(n, i) \neq (m, j)$,*
- *$\sum_{i} p_n^{(i)} \cdot \mathrm{id}_{G^{(n)}} = \mathrm{id}_{G^{(n)}}$.*

### Structural justification

Three free consequences follow if discharged:
1. **Explicit Goncharov-period witnesses.** Each projection $p_n^{(i)} \cdot \mathrm{Li}_n^q(z)$ under $\tau_{\mathrm{arch}}$ generates a specific element of $\mathcal{P}_n / \mathcal{P}_{n-1}$.
2. **Graded Mikusiński localisation.** The field-of-fractions tower $\mathcal{M}_q^{(n)}$ inherits a graded Baer-* structure.
3. **Bar-involution-equivariant period theory.** Self-adjoint $p_n^{(i)}$ generate real periods; bar-swapped pairs generate chirality-twisted periods.

### Reduction to known structure

At depth 0: Baer-* is trivial, $G^{(0)}$ is a field. At depth 1: corresponds to the linear independence of logarithms of multiplicatively independent algebraics (Baker). At depth 2: reduces to the [generic Hecke Baer-* proposition](#prop:hecke-baer-star-generic). At depth $\geq 3$: open.
