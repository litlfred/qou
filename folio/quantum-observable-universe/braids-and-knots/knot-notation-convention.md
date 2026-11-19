Particles in this framework are identified with their knots, written $\mathfrak{K}_x^{\pm}$, where $x$ designates the particle and $\pm$ designates the knot's chirality. The superscript denotes **mirror reflection**, $T_{m,n}^{\sigma} = T_{m,-n}$; what that mirror *means* physically depends on the sector. In the lepton sector it exchanges a particle with its antiparticle (charge conjugation): $\mathfrak{K}_e^- = T_{2,3}$ is the electron, $\mathfrak{K}_e^+ = T_{2,3}^{\sigma}$ the positron. In the quark sector it exchanges a quark with its **weak-isospin partner**, not with its antiquark: $\mathfrak{u} = T_{2,3}$ and $\mathfrak{d} = T_{2,3}^{\sigma}$ are the up and down quarks of one doublet, and likewise $(\mathfrak{c}, \mathfrak{s})$ at $n = 5$. Concretely the mirror flips the sign of the writhe, and the weak isospin is that sign: $T_3 = \tfrac{1}{2}\mathrm{sgn}\,\kappa$ with $\kappa(\mathfrak{u},\mathfrak{c},\mathfrak{t}) = +(3,5,7)$ and $\kappa(\mathfrak{d},\mathfrak{s},\mathfrak{b}) = -(3,5,7)$. Reading the quark rows as charge conjugation instead would assert $\mathfrak{d} = \bar{\mathfrak{u}}$, identifying charge $-1/3$ with charge $-2/3$.

See [Table 1](#tbl:knot-notation-convention-table1-data).

For amphichiral knots like $\mathfrak{K}_H$ and $\mathfrak{K}_\gamma$, the sign is trivial since $K \cong K^{\sigma}$; these are the entries whose antiparticle column reads *(self)*. The cinquefoil $\mathfrak{K}_\mu = T_{2,5}$ is **not** among them: no nontrivial torus knot is amphichiral, which is why $\mu^-$ and $\mu^+$ carry distinct knots just as $e^-$ and $e^+$ do. 

While the unknot $\mathfrak{K}_\nu$ is amphichiral unoriented, the left-handed neutrino $\nu_L$ and right-handed antineutrino $\nu_R^{\sigma}$ are distinguished by framing rather than knot type.

Torus knots are denoted by $T_{m,n}$, with mirror image $T_{m,n}^{\sigma} = T_{m,-n}$.

See [Table 2](#tbl:knot-notation-convention-table2-data).

The connected sum is $\mathfrak{K}_1 \mathbin{\#} \mathfrak{K}_2$. A hadron is written $[\mathfrak{K}_1, \mathfrak{K}_2, \mathfrak{K}_3]_p \oplus \mathcal{L}_H$, where the subscript designates colour-tube coupling and $\oplus$ denotes linking. The proton is:
$$
  \mathfrak{p} = [\mathfrak{K}_u, \mathfrak{K}_u, \mathfrak{K}_d]_p
  \oplus \mathcal{L}_H.
$$

The symbol $\sigma_i$ denotes both the braid generator and its image in $H_n(R, q)$, which satisfies $\sigma_i^{2} = (q - q^{-1})\sigma_i + 1$. The Jones polynomial is always denoted $J_K(q)$. Topological masses are evaluated via $\mathfrak{m}(K) = \mathrm{Vol}(K) / \hbar_q^{2}$, where $\hbar_q = 1 - q^{-1}$.
