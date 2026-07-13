<!-- FILE_START: intro-pair-production-anyon.md -->
The symmetric-crystal framework lifts pair production from a fermionic process to a categorical anyon-collapse event. An incoming pair of $0_1$ photonic states meets at a Type-B crystal fixed point. The crystal's involutive structure selects the outgoing particle/antiparticle pair.

This section formulates the symmetric-crystal pair-production mechanism. We identify the anyon-collapse locus as a Demazure sub-crystal. We exhibit the explicit collapse map on the first non-trivial case: the $0_1 + 0_1 \to e^- + e^+$ Breit–Wheeler vertex. We connect this categorical event to its Archimedean counterpart, identifying the crystal-based picture as the substrate-level prototype for Breit–Wheeler kinematics.
<!-- FILE_END: intro-pair-production-anyon.md -->

<!-- FILE_START: symmetric-crystal-pair-production.md -->
**Conjecture (symmetric-crystal pair production).**
*Let $H_n(R, q)$ be the Iwahori–Hecke algebra of type $A_{n-1}$ with Hecke normal forms $\{T_w\}$. Let $\mathrm{Cryst}(\mathfrak{sl}_n)$ be its associated Kashiwara crystal. Fold the $\mathfrak{sl}_n$ Cartan datum into a Type B Cartan datum along the Dynkin involution $i \mapsto \bar i = n - i$. Equivalently, apply the $\mathbb{Z}/2\mathbb{Z}$ bar-involution $T_w \mapsto \overline{T_w}$ that sends $q \mapsto q^{-1}$ and reverses crossings. The resulting symmetric crystal $\mathrm{Cryst}^{\mathrm{sym}}(\mathfrak{so}_{2n+1})$ admits no Kashiwara lowering operator $\tilde f_i$ as a unimodal step from a bar-invariant source. Every step is a paired operator $(\tilde f_i, \tilde f_{\bar i})$. Consequently, a transition*

$$
  v_0 \;\xrightarrow{\;(\tilde f_i, \tilde f_{\bar i})\;}\; v_-\,\sqcup\,v_+,
$$

*from a bar-invariant highest-weight vector $v_0$ produces two descendants $v_-, v_+$ whose Hecke normal forms are bar-conjugates ($\overline{T_{v_-}} = T_{v_+}$). We identify $v_-$ with a chiral particle and $v_+$ with its CPT antiparticle. The symmetric crystal forbids the production of a single chiral excitation from a non-chiral source. Any descendant set is a disjoint union of bar-conjugate pairs.*

**Algorithmic role (charge-conservation kill switch).**
*The Gröbner–Shirshov reduction engine enforces matter–antimatter pairing structurally. At each crystal step, it applies the folded operator pair atomically. An internally generated intermediate carrying a single net chirality is unreachable. The Hecke normal forms produced by the engine are bar-invariant by construction. The engine rejects any candidate normal form failing this test before further expansion. This converts CPT and charge conservation from combinatorial post-conditions into intrinsic invariants of the crystal traversal. No custom $\mathbb{Z}/2\mathbb{Z}$ rules are required.*

**Conjectural status.**
*The Type B folding of $\mathfrak{sl}_n$ Kashiwara crystals into $\mathfrak{so}_{2n+1}$ symmetric crystals is established at the level of generic quantum-group representations. The bar-involution is intrinsic to the KLR canonical basis. We conjecture that the folded operators on the cyclotomic quotient realising $H_n(R, q)$ realise exactly the matter/antimatter pairing of the topological ansatz. The bar-conjugate pair on a single Type B crystal node corresponds to a CPT pair of QOU particles. The empirical evidence is the $\det \rho_\lambda(w) \cdot \det \rho_{\lambda'}(w) = \pm 1$ identity for every conjugate-partition pair $(\lambda, \lambda')$. This identity is the bar-involution acting on Wedderburn blocks.*
<!-- FILE_END: symmetric-crystal-pair-production.md -->

<!-- FILE_START: two-photon-pair-production.md -->
**Remark (concrete example: $\gamma\gamma \to e^- e^+$ in the symmetric crystal).**
*In the topological ansatz, the photon $\gamma$ is the empty knot $\varnothing$. This identity element on $n$ strands carries no crossings. It is distinct from the unknot $0_1$ representing the neutrino. The two-photon state $\gamma\gamma$ corresponds to the identity element $T_e \in H_n(R, q)$ on $n = 2$ strands. It has zero crossings, zero graded Hecke energy, and strict bar-invariance. Applying $T_e \mapsto \overline{T_e}$ swaps over- and under-crossings, of which there are none, returning $T_e$ unchanged. The state sits at the highest-weight node of the trivial component of $\mathrm{Cryst}^{\mathrm{sym}}(\mathfrak{so}_{2n+1})$.*

*We place this state at the high-energy boundary of a heavy nucleus. This fixed external boundary condition supplies energy to the crystal traversal. The intense local energy density forces the system to step down the crystal graph to absorb energy. However, symmetric-crystal pair production forbids a unimodal lowering step $\gamma\gamma \xrightarrow{\tilde f_i} v$ landing on a single chiral descendant. The only admissible step is the paired operator:*

$$
  \gamma\gamma
  \;\xrightarrow{\;(\tilde f_i,\tilde f_{\bar i})\;}\;
  e^-\,\sqcup\,e^+.
$$

*One operator twists two strands into a left-handed trefoil (the electron $e^-$). The bar-conjugate operator simultaneously twists two strands into the right-handed anti-trefoil (the positron $e^+$). The bar-conjugate descendant pair conserves the bar-invariance of the source state. Charge ($-e + e = 0$) and chirality ($-\tfrac12 + \tfrac12 = 0$) are conserved structurally.*

**Falsification handle.**
*The symmetric-crystal pair production conjecture forbids any single-photon pair-production channel $\gamma \to e^- e^+$ without invoking energy–momentum conservation as a separate axiom. The bar-invariant single-strand source state $\gamma$ carries no crossings to fold into a paired operator. Consequently, the symmetric crystal has no admissible step. The empirical absence of $\gamma \to e^- e^+$ in vacuum is consistent with the conjecture. Observation of this channel without a recoiling external boundary falsifies it.*
<!-- FILE_END: two-photon-pair-production.md -->

<!-- FILE_START: hecke-anyonic-substrate.md -->
**Theorem (Iwahori–Hecke substrate is the anyon algebra).**
*Let $K$ be a closed braid representing a QOU particle. Let $T_w \in H_n(R, q)$ be its Hecke normal form at a generic deformation parameter $q$. The topological statistics of $K$ are governed by the braid group $B_n$ acting on $T_w$ via the surjection $B_n \twoheadrightarrow H_n(R, q)$ defined by $\sigma_i \mapsto T_{s_i}$ modulo the Hecke quadratic relation:*

$$
  (T_{s_i} - q)(T_{s_i} + 1) = 0.
$$

*Every particle in the substrate is an anyon \cite{kitaev2006, nayak2008}. Exchanging two particles multiplies the wavefunction by a topological braiding matrix rather than a $\pm 1$ permutation sign. Bosonic and fermionic statistics are not fundamental. They emerge as the image of anyonic braiding under the observation functor $\tau$.*

**Algorithmic role.**
*The reduction engine processes every transition as a braid-group element acting on $H_n(R, q)$ via $\sigma_i \mapsto T_{s_i}$. No $\pm 1$ shortcuts exist at intermediate steps. At generic $q$, the braid matrices accumulate geometric information. Only the final trace under $\tau$ collapses this data onto a $\pm 1$ statistic.*

**Conjectural status.**
*The Schur–Weyl identification of $H_n(q)$-modules with anyon Hilbert spaces is classical. We conjecture that the entire particle spectrum of the substrate realizes exactly as $H_n(R, q)$-modules. No particle escapes the anyonic substrate prior to observation. Proving exhaustion requires the cyclotomic-KLR equivalence \cite{khovanovlauda2009}.*
<!-- FILE_END: hecke-anyonic-substrate.md -->

<!-- FILE_START: root-of-unity-mtc-truncation.md -->
**Conjecture (root-of-unity MTC truncation).**
*Let $H_n(R, q)$ be the Iwahori–Hecke algebra of the anyonic substrate. Fix $k \geq 2$. Specialise the deformation parameter at a primitive $k$-th root of unity on the unit circle:*
$$
  q \;=\; e^{2\pi i / k} \;\in\; S^1.
$$
*The cyclotomic quotient of the KLR algebra realising $H_n(R, q)$ becomes finite-dimensional. The infinite Kashiwara crystal $\mathrm{Cryst}(\mathfrak{sl}_n)$ truncates to a finite component supported on partitions with at most $k - 1$ columns. The category of cyclotomic-KLR modules is a Modular Tensor Category $\mathrm{MTC}_k$ \cite{bakalovkirillov2001}. The simple objects of $\mathrm{MTC}_k$ are non-abelian anyons \cite{kitaev2006, nayak2008}. Their fusion rules match the truncated crystal's Littlewood–Richardson coefficients. Their braiding is the action of $B_n$ on $H_n(R, q)$ specialised at $q = e^{2\pi i / k}$.*

**Algorithmic role.**
Switching the substrate parameter to a primitive $k$-th root of unity converts the open-ended Hecke evaluation into a finite-rank fusion calculation. The engine enumerates the truncated crystal nodes and reads the $F$- and $R$-matrices of $\mathrm{MTC}_k$ directly from the $\sigma_{s_i}$ generators evaluated at the chosen root.

**Conjectural status.**
The Bakalov–Kirillov MTC structure on cyclotomic-KLR modules at a root of unity is established \cite{bakalovkirillov2001, khovanovlauda2009}. The truncation of the Kashiwara crystal at roots of unity is also established \cite{kashiwara1991}. We conjecture the identification of the simple $\mathrm{MTC}_k$ objects with the substrate's non-abelian anyon spectrum at the chosen $k$. To falsify this, exhibit a QOU particle at $q = e^{2\pi i / k}$ whose fusion does not match the predicted $\mathrm{MTC}_k$ rule.
<!-- FILE_END: root-of-unity-mtc-truncation.md -->

<!-- FILE_START: kazhdan-lusztig-classical-limit.md -->
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
*The $q \to 1$ specialisation of $H_n(R, q)$ to $\mathbb{Z}[S_n]$ is classical, as is the $b_w \to C_w$ correspondence on canonical bases. We conjecture the compatibility of this specialisation with the observation functor $\tau$ on the full QOU spectrum. The macroscopic Pauli/Bose statistics observed in laboratory frames are exactly the $\mathrm{KL}$-image of the anyonic Hecke statistics of the substrate.*
<!-- FILE_END: kazhdan-lusztig-classical-limit.md -->

<!-- FILE_START: anyon-observation-collapse.md -->
**Remark (anyon ladder under the observation functor).**
*The three preceding conjectures organize into a single ladder indexed by the deformation parameter $q$:*

| $q$ regime | Substrate state | Observation image |
|---|---|---|
| Generic $q$ | Abelian anyons in $H_n(R, q)$ | Topological braiding matrices |
| $q = e^{2\pi i / k}$ | Non-abelian anyons in $\mathrm{MTC}_k$ | Finite fusion / $F$- and $R$-matrices |
| $q \to 1$ | Symmetric-group representations | Pauli ($\pm 1$) statistics |

*Reading the ladder downwards represents the observation functor $\tau$ acting on a cooling substrate. Anyonic braiding loses information at each step, yet it never abandons the categorical algebraic substrate. We use Kashiwara crystal traversals to compute pair production and stable masses. These map the fusion rules of the appropriate rung: the generic Hecke fluid for high-energy interactions, $\mathrm{MTC}_k$ for topologically ordered phases, and $\mathbb{Z}[S_n]$ for the classical-statistics regime accessed by macroscopic detectors.*

**Algorithmic synthesis.**
*The reduction engine selects the rung by the value of $q$ supplied to the substrate. It uses generic $q$ for the open-ended Hecke evaluation, a root of unity for fusion-category enumeration, and $q \to 1$ for the Pauli/Bose decomposition. The same canonical-basis machinery applies at every rung. Only the specialization map changes.*
<!-- FILE_END: anyon-observation-collapse.md -->
