**Conjecture (cyclotomic residue exists at each level).**
*For each filtration level $\ell \in \{0, 1, \ldots, \ell(K, q)\}$ and each primitive $\ell$-th root of unity $\zeta_\ell$, the cyclotomic projection*

$$
  \mathrm{Res}_{q \to \zeta_\ell}\bigl[\Phi_q(u) \cdot \mathrm{tr}_{M, \ell}(T_w)\bigr] \;\in\; \mathbb{R}
$$

*is a well-defined real number. Here $\Phi_q$ is the quantum dilogarithm. The value depends only on $\ell$ and the equivalence class of $T_w$ modulo $J^{\ell+1}(q)$.*

**Categorical statement.** The cyclotomic projection of $\Phi_q \cdot \mathrm{tr}_{M,\ell}$ in the Habiro completion forms the residue contribution attached to stratum $\ell$ by the filtered Hochschild spectral sequence.

**What is proved and what is open.** The Habiro-completion projection onto each cyclotomic target ring exists: it is constructed, and [Cyclotomic residues of $\Phi_q \cdot \mathrm{tr}_{M, \ell}$ — algebraic definition](#prop:residue-at-root) proves the residue is its image for any element of the Habiro ring. The conjectural content is the rest: that $\Phi_q \cdot \mathrm{tr}_{M, \ell}(T_w)$ is such an element, that its residue is real, and that it depends only on the class of $T_w$ modulo $J^{\ell+1}(q)$. The archimedean per-level residue values enter downstream as given data.

**Conjectural status.** The analytic literature guarantees the existence and reality of the residue. A proof within the present framework awaits that meromorphic-function infrastructure; downstream results take the residue values as given.

**Empirical witness.** The canonical residues for the proton, neutron, and deuteron at $q_0$ match the Habiro side at machine precision.
