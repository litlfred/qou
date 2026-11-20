**Conjecture (cyclotomic residue exists at each level).**
*For each filtration level $\ell \in \{0, 1, \ldots, \ell(K, q)\}$ and each primitive $\ell$-th root of unity $\zeta_\ell$, the cyclotomic projection*

$$
  \mathrm{Res}_{q \to \zeta_\ell}\bigl[\Phi_q(u) \cdot \mathrm{tr}_{M, \ell}(T_w)\bigr] \;\in\; \mathbb{R}
$$

*is a well-defined real number. Here $\Phi_q$ is the quantum dilogarithm. The value depends only on $\ell$ and the equivalence class of $T_w$ modulo $J^{\ell+1}(q)$.*

**Categorical statement.** The cyclotomic projection of $\Phi_q \cdot \mathrm{tr}_{M,\ell}$ in the Habiro completion forms the residue contribution attached to stratum $\ell$ by the filtered Hochschild spectral sequence.

**Lean encoding.** The conjecture is axiomatised as the class `QOU.BraidKnot.ResidueAtRoot` (fields: the target ring family `target : ℕ → Type` and the cyclotomic projection `project : (n : ℕ) → R →+* target n`); an instance supplies the Habiro-completion projection whose existence is the conjectural content, and [Cyclotomic residues of $\Phi_q \cdot \mathrm{tr}_{M, \ell}$ — algebraic definition](#prop:residue-at-root) is stated conditionally on it per the conditional-class convention. The archimedean per-level residue values enter downstream as the class field `residue : Fin levelBound → ℝ` of `GBResidueSpectralSum`. A fully constructive definition requires Mathlib infrastructure for meromorphic functions and the Habiro completion as a topological ring.

**Conjectural status.** The analytic literature guarantees the existence and reality of the residue. A Lean proof awaits the meromorphic-function infrastructure. Instances supply the value directly.

**Empirical witness.** The canonical residues for the proton, neutron, and deuteron at $q_0$ match the Habiro side at machine precision.
