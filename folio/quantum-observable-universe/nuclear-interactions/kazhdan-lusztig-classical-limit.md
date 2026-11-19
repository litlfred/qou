**Conjecture (Kazhdan–Lusztig classical limit).**
*Let $\{b_w\} \subset H_n(R, q)$ be the KLR canonical basis associated to the anyonic Hecke substrate. Let $\{C_w\} \subset \mathbb{Z}[S_n]$ be the Kazhdan–Lusztig basis of the group algebra of the symmetric group. Define the classical-limit functor*

$$
  \mathrm{KL}\colon\;
    \mathrm{mod}\,H_n(R, q)
    \;\longrightarrow\;
    \mathrm{mod}\,\mathbb{Z}[S_n],
  \qquad
  b_w \;\longmapsto\; C_w \quad \text{as } q \to 1,
$$

*sending each KLR canonical basis element to its $q \to 1$ specialisation in $\mathbb{Z}[S_n]$. Then $\mathrm{KL}$ is a monoidal functor compatible with the observation functor $\tau$. Its action on QOU particle states represents the topological-to-classical transition. The braid group $B_n$ collapses to $S_n$ via $\sigma_i^2 \mapsto 1$. The Hecke matrices lose their topological braiding memory. The surviving statistics are exactly the $\pm 1$ permutation signs that govern Pauli exclusion (fermions) and Bose–Einstein occupation (bosons).*

**Algorithmic role.**
*The reduction engine implements the classical limit by replacing $\sigma_{s_i}$ with the symmetric-group generator $s_i$ and the canonical basis element $b_w$ with the Kazhdan–Lusztig basis element $C_w$. The cyclotomic-KLR Wedderburn decomposition specialises to the ordinary $S_n$ Wedderburn decomposition, with multiplicities given by hook-length formulae. The transition is functorial. No extra selection rule is introduced for the bosonic vs fermionic split. The split is the eigenvalue decomposition of $s_i$ acting on the $q \to 1$ canonical basis.*

**Conjectural status.**
*The $q \to 1$ specialisation of $H_n(R, q)$ to $\mathbb{Z}[S_n]$ is classical, as is the $b_w \to C_w$ correspondence on canonical bases. The conjecture here asserts the compatibility of this specialisation with the observation functor $\tau$ on the full QOU spectrum. The macroscopic Pauli/Bose statistics observed in laboratory frames are exactly the $\mathrm{KL}$-image of the anyonic Hecke statistics of the substrate.*
