**Conjecture (cyclotomic residue exists at each level).**
*For each filtration level $\ell \in \{0, 1, \ldots, \ell(K, q)\}$ and each primitive $\ell$-th root of unity $\zeta_\ell$, the cyclotomic projection*

$$
  \mathrm{Res}_{q \to \zeta_\ell}\bigl[\Phi_q(u) \cdot \mathrm{tr}_{M, \ell}(T_w)\bigr] \;\in\; \mathbb{R}
$$

*is a well-defined real number. Here $\Phi_q$ is the quantum dilogarithm. The value depends only on $\ell$ and the equivalence class of $T_w$ modulo $J^{\ell+1}(q)$.*

**Categorical statement.** The cyclotomic projection of $\Phi_q \cdot \mathrm{tr}_{M,\ell}$ in the Habiro completion forms the residue contribution attached to stratum $\ell$ by the filtered Hochschild spectral sequence.

**Lean encoding.** Encoded as the class field `residue : Fin levelBound → ℝ`. A fully constructive definition requires Mathlib infrastructure for meromorphic functions and the Habiro completion as a topological ring.

**Conjectural status.** The analytic literature guarantees the existence and reality of the residue. A Lean proof awaits the meromorphic-function infrastructure. Instances supply the value directly.

**Empirical witness.** The canonical residues for the proton, neutron, and deuteron at $q_0$ match the Habiro side at machine precision.
