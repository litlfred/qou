**Proposition.** *On the symmetric (trivial) representation of the braid
monoid — the one-dimensional Wedderburn block that a molecule's $C_{nv}$
assembly projector selects (the $S_n$-symmetric channel of
[`rem:h2o-c2v-from-projector`](#rem:h2o-c2v-from-projector)) — every generator
$\sigma_i$ acts as the scalar $q$. Hence an electron domain represented by a
braid word $w$ of length $\ell$ has weight*

$$
  w_{\mathrm{domain}} = q^{\ell}.
$$

*In particular the lone pair $e^- = \sigma_0\sigma_1\sigma_0$ (length $3$) and
the $\sigma$-bond (length $1$) have weights $q^3$ and $q$, so the lone-pair to
bond weight ratio is*

$$
  \frac{w_{\mathrm{lone}}}{w_{\mathrm{bond}}} = \frac{q^3}{q} = q^2 .
$$

This ratio is **derived** — a ratio of Hecke eigenvalues on the symmetric
channel — with no central-atom input and no fit, and (being a ratio of
eigenvalues, not an angle) it is independent of the repulsion kernel. The
provable core — the weight law $q^{\ell}$ and the corollary $q^3 = q^2\cdot q$ —
is formalized sorry-free in the Lean sibling
(`symmetric_block_domain_weight`, `lone_bond_ratio_q_squared`).
