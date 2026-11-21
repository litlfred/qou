Let $\mathbf{C}$ be a rigid braided monoidal category and let $\mathfrak{H} \in \mathrm{Sym}^n(K)$ be a hadron with constituent knots $K_1, \ldots, K_n$.

1. **Braiding closure.** The braiding $\beta_{K_i, K_j}$ descends to an involution on $\mathrm{Sym}^n(K)$. For the antisymmetric product, exchanging identical constituents produces the sign

$$
  \beta_{K_i, K_i}\big|_{\mathrm{alt}} = -1 .
$$
2. **Hopf linking closure.** The linking operation $\ell_{ij} \colon K_i \otimes K_j \to K_i \mathbin{\#_{\mathrm{Hopf}}} K_j$ is an endomorphism of $\mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}}$ with a two-sided inverse when the linking number is trivial.
3. **Skein closure.** The $q$-deformed skein relation resolves any linked composite into a polynomial in $q$ times unlinked constituents, yielding the mass formula

$$
  \mathcal{M}(\mathfrak{H}) = Q(q) \cdot \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}}) + \sum_i \mathcal{M}(K_i).
$$

4. **Fusion closure.** For hadrons $\mathfrak{H}_1 \in \mathrm{Sym}^{n_1}(K)$ and $\mathfrak{H}_2 \in \mathrm{Sym}^{n_2}(K)$, the fusion $\mathfrak{H}_1 \star \mathfrak{H}_2 \in \mathrm{Sym}^{n_1 + n_2}(K)$ is again a hadron, with associative constituent composition across $(n_1 + n_2) + n_3$ and additive mass $\mathcal{M}(\mathfrak{H}_1 \star \mathfrak{H}_2) = \mathcal{M}(\mathfrak{H}_1) + \mathcal{M}(\mathfrak{H}_2)$.
