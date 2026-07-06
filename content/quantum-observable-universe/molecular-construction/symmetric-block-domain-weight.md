**Proposition.** *On the symmetric (trivial) representation of the braid monoid—the one-dimensional Wedderburn block selected by a molecule's $C_{nv}$ assembly projector (the $S_n$-symmetric channel of [`rem:h2o-c2v-from-projector`](#rem:h2o-c2v-from-projector))—every generator $\sigma_i$ acts as the scalar $q$. Thus, an electron domain represented by a braid word $w$ of length $\ell$ possesses weight*

$$
  w_{\mathrm{domain}} = q^{\ell}.
$$

*The lone pair $e^- = \sigma_0\sigma_1\sigma_0$ (length $3$) and the $\sigma$-bond (length $1$) have weights $q^3$ and $q$, respectively. The lone-pair to bond weight ratio evaluates to*

$$
  \frac{w_{\mathrm{lone}}}{w_{\mathrm{bond}}} = \frac{q^3}{q} = q^2 .
$$

This ratio is mathematically derived. It arises as a ratio of Hecke eigenvalues on the symmetric channel. It requires no central-atom input and entails no fitting parameters. Because it is a ratio of eigenvalues rather than an angle, it remains independent of the chosen repulsion kernel. We formalize the provable core—the weight law $q^{\ell}$ and the corollary $q^3 = q^2\cdot q$—in the Lean sibling (`symmetric_block_domain_weight`, `lone_bond_ratio_q_squared`).
