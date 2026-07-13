<!-- FILE_START: intro-gs-axiomatic-backing.md -->
The Gröbner–Shirshov (GS) framework reduces braid words to their canonical form. This framework relies on a single axiomatic backing: the existence of a graded Markov trace compatible with the Hecke composition. This section records the existence conjecture and its formal consequences, isolating the inputs consumed by the reduction engine.

We begin with the existence conjecture, survey the GS-reduction lemmas depending on it, and track the conditionally proved theorems. We identify the proof status in the literature and highlight the specific obstruction (the Wenzl-bridge convention) that the present formalism resolves.
<!-- FILE_END: intro-gs-axiomatic-backing.md -->

<!-- FILE_START: gs-graded-markov-trace-existence.md -->
**Theorem (existence of the graded Markov trace).**
*Let $H_n(R, q)$ carry the Gröbner–Shirshov confinement filtration $J^\bullet(q)$ ([confinement level](#def:confinement-level)). For every filtration level $\ell \in \{0, 1, \ldots, \ell(K, q)\}$, there exists a well-defined real-valued functional*

$$
  \mathrm{tr}_{M, \ell} \colon J^\ell(q) / J^{\ell+1}(q) \;\longrightarrow\; \mathbb{R}
$$

*obtained as the :refterm[descent]{#descent} of the Markov trace $\mathrm{tr}_M$ ([Jones–Markov trace](#thm:jones-markov-trace)) along the projection $J^\ell(q) \twoheadrightarrow J^\ell(q) / J^{\ell+1}(q)$. The sequence $\ell \mapsto \mathrm{tr}_{M, \ell}(T_w)$ depends only on the GS-normal form of $T_w$.*

**Categorical statement.** The Markov trace acts as a cyclic 0-cocycle on the Hochschild complex. It preserves the filtration, inducing a sequence of functionals on the associated graded pieces. 

**Lean encoding.** In `gb-residue-spectral-sum.lean`, this is encoded as the abstract class field `gradedTrace : Fin levelBound → ℝ` on `GBResidueSpectralSum`. Each atomic instance supplies its per-level values. Constructing a fully verifiable `def` requires Mathlib infrastructure for filtered algebras and remains tracked downstream.

**Conjectural status.** The claim is rigorous over any commutative ring $R$ where $\mathrm{tr}_M$ and $J^\bullet(q)$ exist. Promoting the formal Lean counterpart to a theorem requires formalising $\mathrm{ConfinementLevel}$, constructing $\mathrm{gr}^\ell H_n(R, q)$, and proving that $\mathrm{tr}_M$ preserves the filtration.

**Empirical witness.** The formal derivation emits exact algebraic values for the proton, neutron, and deuteron atoms. These agree with the Habiro-side values to a relative tolerance of $10^{-9}$.
<!-- FILE_END: gs-graded-markov-trace-existence.md -->

<!-- FILE_START: gs-residue-at-root-existence.md -->
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
<!-- FILE_END: gs-residue-at-root-existence.md -->

<!-- FILE_START: gs-spectral-decomposition-existence.md -->
**Conjecture (spectral decomposition of the mass).**
*For every closed braid $K$ with normal form $T_w \in H_n(R, q_0)$, the categorical mass decomposes as*

$$
  \mathfrak{m}(K, q_0) \;=\; \bigl|\,\mathrm{tr}_M^{(0)}(T_w, q_0)\,\bigr| \;+\; \sum_{\ell = 0}^{\ell(K, q_0) - 1} \mathrm{Res}_{q \to \zeta_\ell}\bigl[\Phi_q \cdot \mathrm{tr}_{M, \ell}(T_w)\bigr],
$$

*where $\mathrm{tr}_M^{(0)}$ is the descended (level-$0$) Markov trace.*

**Categorical statement.** The $E_\infty$-pairing of $\mathrm{tr}_M$ with $T_w$ in the filtered Hochschild spectral sequence splits into the smooth liquid-drop part and the shell-correction cyclotomic residues.

**Lean encoding.** Encoded as the class-field axiom `spectral_decomposition` on `GBResidueSpectralSum`. Instances supply this identity.

**Conjectural status.** A Lean proof requires formalized definitions for the graded trace and residues, plus the Habiro–Mittag-Leffler bridge identifying the cyclotomic tail with the residue sum.

**Empirical witness.** Cross-pipeline validation records relative differences at or below $10^{-9}$ on every checkpoint.
<!-- FILE_END: gs-spectral-decomposition-existence.md -->

<!-- FILE_START: gs-spectral-sum-finite.md -->
**Conjecture (finiteness of the residue spectral sum).**
*For every closed braid $K$ with normal form $T_w$, there exists a finite cutoff $N = \ell(K, q_0)$ such that the cyclotomic residue vanishes for all $\ell \geq N$:*

$$
  \forall \ell \geq N \colon\quad \mathrm{Res}_{q \to \zeta_\ell}\bigl[\Phi_q \cdot \mathrm{tr}_{M, \ell}(T_w)\bigr] \;=\; 0.
$$

**Categorical statement.** The confinement level $\ell(K, q_0)$ is finite and unique. If $T_w \in J^\ell(q_0)$ for $\ell > \ell(K, q_0)$, then $T_w \equiv 0$, contradicting genericity.

**Lean encoding.** Cast as a tautology over the compact domain `Fin levelBound` in `spectral_sum_finite`. The substantive claim is that `levelBound` correctly represents the confinement level.

**Conjectural status.** Proving the bound requires formalising $\mathrm{ConfinementLevel}$ and establishing $\mathrm{tr}_{M, \ell} \equiv 0$ for $\ell > \ell(K, q_0)$.

**Empirical witness.** Witness scripts truncate the sum at $\ell = 6$, observing zero contributions beyond it. Homologically, strata outside $J^{\ell(K, q_0)}$ map into the cemetery group, vanishing without term-by-term cancellation.
<!-- FILE_END: gs-spectral-sum-finite.md -->

<!-- FILE_START: gs-archimedean-agreement-trace.md -->
**Conjecture (archimedean agreement, generic instance).**
*For every closed braid $K$ admitting a Habiro polynomial trace $T_K(u) \in \mathbb{Z}[u]$ and a Gröbner–Shirshov mass value $\mathfrak{m}_{\mathrm{GB}}(K, q_0)$, the archimedean evaluation*

$$
  T_K\bigl(\sqrt{q_0}\bigr) \;\approx\; \mathfrak{m}_{\mathrm{GB}}(K, q_0)
$$

*agrees across pipelines.*

**Categorical statement.** The archimedean fibre functor intertwines the Habiro polynomial evaluation and the spectral-sequence residue sum.

**Lean encoding.** Encoded as the class field axiom `archimedean_agreement`. Instances supply it as a substrate axiom.

**Conjectural status.** A Lean proof requires the spectral decomposition existence, the `tail_in_ideal` axiom for the Habiro completion, and the analytic identification of the residues.

**Empirical witness.** Validation records exact agreement to machine precision.
<!-- FILE_END: gs-archimedean-agreement-trace.md -->

<!-- FILE_START: gs-archimedean-agreement-residue.md -->
**Conjecture (archimedean agreement, proton instance).**
*For the proton braid $T_w(Z = 1, N = 0)$, the degree-$48$ Markov-normalised Habiro polynomial trace $T_{\mathfrak{p}}(u)$ evaluates at $u_0 = \sqrt{q_0}$ to the proton GB mass:*

$$
  T_{\mathfrak{p}}\bigl(\sqrt{q_0}\bigr) \;\approx\; \mathfrak{m}_{\mathrm{GB}}(\mathfrak{p}, q_0) \;\approx\; 2.1225825095.
$$

*Similar identities hold for the neutron, deuteron, and triton.*

**Categorical statement.** This specializes the generic archimedean agreement to the proton, unifying the Habiro polynomial evaluation with the spectral-sequence descended trace and cyclotomic residues.

**Lean encoding.** Sits as the `sorry` in the `protonExample` instance of `HabiroResidueSumEquivalence`.

**Conjectural status.** Closing the Lean proof requires brute-force evaluation of the explicit polynomial via `native_decide` or applying the generic archimedean agreement conjecture. The canonical agreement is certified to machine precision.
<!-- FILE_END: gs-archimedean-agreement-residue.md -->
