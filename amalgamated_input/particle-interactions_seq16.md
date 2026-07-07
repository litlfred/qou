<!-- FILE_START: intro-pair-production-anyon.md -->
The symmetric-crystal framework lifts pair production from a fermionic process to a categorical anyon-collapse event. An incoming pair of $0_1$ photonic states meets at a Type-B crystal fixed point. The outgoing particle/antiparticle pair is selected by the crystal's involutive structure.

We conjecture the symmetric-crystal pair-production mechanism. We identify the anyon-collapse locus as a Demazure sub-crystal. We then exhibit the explicit collapse map on the first non-trivial case: the $0_1 + 0_1 \to e^- + e^+$ Breit–Wheeler vertex. Finally, we connect this categorical event to its Archimedean counterpart, identifying the crystal-based picture as the substrate-level prototype for Breit–Wheeler kinematics.
<!-- FILE_END: intro-pair-production-anyon.md -->

<!-- FILE_START: symmetric-crystal-pair-production.md -->
**Conjecture (symmetric-crystal pair production).**
*Let $H_n(R, q)$ be the Iwahori–Hecke algebra of type $A_{n-1}$ with [Hecke normal forms](#def:hecke-normal-form) $\{T_w\}$. Let $\mathrm{Cryst}(\mathfrak{sl}_n)$ be its associated Kashiwara crystal under [crystal-graph realisation](#conj:crystal-graph-realization). Fold the $\mathfrak{sl}_n$ Cartan datum into a Type B Cartan datum along the Dynkin involution $i \mapsto \bar i = n - i$. Equivalently, apply the $\mathbb{Z}/2\mathbb{Z}$ bar-involution $T_w \mapsto \overline{T_w}$ that sends $q \mapsto q^{-1}$ and reverses crossings. The resulting symmetric crystal $\mathrm{Cryst}^{\mathrm{sym}}(\mathfrak{so}_{2n+1})$ admits no Kashiwara lowering operator $\tilde f_i$ as a unimodal step from a bar-invariant source. Every step is a paired operator $(\tilde f_i, \tilde f_{\bar i})$. Consequently, a transition*

$$
  v_0 \;\xrightarrow{\;(\tilde f_i, \tilde f_{\bar i})\;}\; v_-\,\sqcup\,v_+,
$$

*from a bar-invariant highest-weight vector $v_0$ produces two descendants $v_-, v_+$ whose Hecke normal forms are bar-conjugates ($\overline{T_{v_-}} = T_{v_+}$). Identify $v_-$ with a chiral particle and $v_+$ with its CPT antiparticle. The symmetric crystal forbids the production of a single chiral excitation from a non-chiral source. Any descendant set is a disjoint union of bar-conjugate pairs.*

**Algorithmic role (charge-conservation kill switch).**
*The Gröbner–Shirshov reduction engine enforces matter–antimatter pairing structurally. At each crystal step, it applies the folded operator pair atomically. An internally generated intermediate carrying a single net chirality is unreachable. The Hecke normal forms produced by the engine are bar-invariant by construction (i.e. fixed under $T_w \mapsto \overline{T_w}$). The engine rejects any candidate normal form failing this test before further expansion. This converts CPT and charge conservation from combinatorial post-conditions into intrinsic invariants of the crystal traversal. No custom $\mathbb{Z}/2\mathbb{Z}$ rules are required in the engine code.*

**Conjectural status.**
*The Type B folding of $\mathfrak{sl}_n$ Kashiwara crystals into $\mathfrak{so}_{2n+1}$ symmetric crystals is established at the level of generic quantum-group representations \cite{kashiwara1991, lecouvey2007}. The bar-involution is intrinsic to the KLR canonical basis \cite{khovanovlauda2009, brundankleshchev2009}. We conjecture that the folded operators on the cyclotomic quotient realising $H_n(R, q)$ realise exactly the matter/antimatter pairing of the topological ansatz. That is, the bar-conjugate pair on a single Type B crystal node corresponds to a CPT pair of QOU particles. The empirical evidence is the $\det \rho_\lambda(w) \cdot \det \rho_{\lambda'}(w) = \pm 1$ identity for every conjugate-partition pair $(\lambda, \lambda')$ ([conjugate-pair det law](computations/det_pair_law.py)). This identity is the bar-involution acting on Wedderburn blocks. It is the strongest available shadow of the conjecture without a full KLR-folding proof.*
<!-- FILE_END: symmetric-crystal-pair-production.md -->

<!-- FILE_START: two-photon-pair-production.md -->
**Remark (concrete example: $\gamma\gamma \to e^- e^+$ in the symmetric crystal).**
*In the QOU topological ansatz, the photon $\gamma$ is the empty knot $\varnothing$ (the identity element on $n$ strands carrying no crossings, which is distinct from the unknot $0_1$ representing the neutrino). The two-photon state $\gamma\gamma$ corresponds to the identity element $T_e \in H_n(R, q)$ on $n = 2$ strands. It has zero crossings, zero graded Hecke energy, and strict bar-invariance. Applying $T_e \mapsto \overline{T_e}$ swaps over- and under-crossings, of which there are none, and returns $T_e$ unchanged. The state sits at the highest-weight node of the trivial component of $\mathrm{Cryst}^{\mathrm{sym}}(\mathfrak{so}_{2n+1})$.*

*Now place this state at the high-energy boundary of a heavy nucleus. This is a fixed external boundary condition that supplies energy to the crystal traversal. The intense local energy density forces the system to step down the crystal graph to absorb energy. However, [symmetric-crystal pair production](#conj:symmetric-crystal-pair-production) forbids a unimodal lowering step $\gamma\gamma \xrightarrow{\tilde f_i} v$ that lands on a single chiral descendant. The only admissible step is the paired operator:*

$$
  \gamma\gamma
  \;\xrightarrow{\;(\tilde f_i,\tilde f_{\bar i})\;}\;
  e^-\,\sqcup\,e^+.
$$

*One operator twists two strands into a left-handed trefoil (the electron $e^-$). The bar-conjugate operator simultaneously twists two strands into the right-handed anti-trefoil (the positron $e^+$). The bar-conjugate descendant pair conserves the bar-invariance of the source state. Thus, charge ($-e + e = 0$) and chirality ($-\tfrac12 + \tfrac12 = 0$) are conserved structurally, rather than by an imposed selection rule.*

**Falsification handle.**
*The [symmetric-crystal pair production](#conj:symmetric-crystal-pair-production) conjecture forbids any single-photon pair-production channel $\gamma \to e^- e^+$ without invoking energy–momentum conservation as a separate axiom. The bar-invariant single-strand source state $\gamma$ carries no crossings to fold into a paired operator. Consequently, the symmetric crystal has no admissible step. The empirical absence of $\gamma \to e^- e^+$ in vacuum is consistent with the conjecture. Observation of this channel without a recoiling external boundary would falsify it.*
<!-- FILE_END: two-photon-pair-production.md -->

<!-- FILE_START: hecke-anyonic-substrate.md -->
**Theorem (Iwahori–Hecke substrate is the anyon algebra).**
*Let $K$ be a closed braid representing a QOU particle. Let $T_w \in H_n(R, q)$ be its [Hecke normal form](#def:hecke-normal-form) at a generic deformation parameter $q$. The topological statistics of $K$ are governed by the braid group $B_n$ acting on $T_w$ via the surjection $B_n \twoheadrightarrow H_n(R, q)$ defined by $\sigma_i \mapsto T_{s_i}$ modulo the Hecke quadratic relation:*

$$
  (T_{s_i} - q)(T_{s_i} + 1) = 0.
$$

*Every particle in the QOU substrate is an anyon \cite{kitaev2006, nayak2008}. Exchanging two particles multiplies the wavefunction by a topological braiding matrix rather than a $\pm 1$ permutation sign. Bosonic and fermionic statistics are not fundamental. They emerge as the image of anyonic braiding under the [observation functor](#def:observation) $\tau$.*

**Algorithmic role.**
*The reduction engine processes every transition as a braid-group element acting on $H_n(R, q)$ via $\sigma_i \mapsto T_{s_i}$. No $\pm 1$ shortcuts exist at intermediate steps. At generic $q$, the braid matrices accumulate geometric information. Only the final trace under $\tau$ collapses this data onto a $\pm 1$ statistic.*

**Conjectural status.**
*The standard Schur–Weyl identification of $H_n(q)$-modules with anyon Hilbert spaces is classical \cite{kassel1995, kitaev2006, nayak2008}. We conjecture that the entire particle spectrum of the QOU substrate realizes exactly as $H_n(R, q)$-modules. No particle escapes the anyonic substrate prior to observation. Closing this conjecture requires either demonstrating a particle outside the Hecke image or proving exhaustion via the cyclotomic-KLR equivalence \cite{khovanovlauda2009}.*
<!-- FILE_END: hecke-anyonic-substrate.md -->

<!-- FILE_START: root-of-unity-mtc-truncation.md -->
**Conjecture (root-of-unity MTC truncation).**
*Let $H_n(R, q)$ be the Iwahori–Hecke algebra of the [anyonic substrate](#conj:hecke-anyonic-substrate), and fix $k \geq 2$. Specialise the deformation parameter at a primitive $k$-th root of unity on the unit circle:*
$$
  q \;=\; e^{2\pi i / k} \;\in\; S^1.
$$
*Then the cyclotomic quotient of the corresponding KLR algebra realising $H_n(R, q)$ becomes finite-dimensional. The infinite Kashiwara crystal $\mathrm{Cryst}(\mathfrak{sl}_n)$ truncates to a finite component supported on partitions with at most $k - 1$ columns. The resulting category of cyclotomic-KLR modules is a Modular Tensor Category $\mathrm{MTC}_k$ \cite{bakalovkirillov2001}. The simple objects of $\mathrm{MTC}_k$ are non-abelian anyons \cite{kitaev2006, nayak2008}. Their fusion rules are determined by the truncated crystal's Littlewood–Richardson coefficients, and their braiding is the action of $B_n$ on $H_n(R, q)$ specialised at $q = e^{2\pi i / k}$.*

**Algorithmic role.**
Switching the substrate parameter from generic to a primitive $k$-th root of unity converts the open-ended Hecke evaluation into a finite-rank fusion calculation. The engine enumerates the truncated crystal nodes and reads off the $F$- and $R$-matrices of $\mathrm{MTC}_k$ directly from the $\sigma_{s_i}$ generators evaluated at the chosen root.

**Conjectural status.**
The Bakalov–Kirillov MTC structure on cyclotomic-KLR modules at a root of unity is established \cite{bakalovkirillov2001, khovanovlauda2009}, as is the truncation of the Kashiwara crystal at roots of unity \cite{kashiwara1991}. What remains conjectural is the identification of the simple $\mathrm{MTC}_k$ objects with the QOU substrate's non-abelian anyon spectrum at the chosen $k$, including the precise correspondence between QOU particle labels and crystal-truncated highest-weight vectors. To falsify this, exhibit a QOU particle at $q = e^{2\pi i / k}$ whose fusion does not match the predicted $\mathrm{MTC}_k$ rule.
<!-- FILE_END: root-of-unity-mtc-truncation.md -->

<!-- FILE_START: kazhdan-lusztig-classical-limit.md -->
**Conjecture (Kazhdan–Lusztig classical limit).**
*Let $\{b_w\} \subset H_n(R, q)$ be the KLR canonical basis
\cite{khovanovlauda2009, kashiwara1991} associated to the
[anyonic Hecke substrate](#conj:hecke-anyonic-substrate), and let
$\{C_w\} \subset \mathbb{Z}[S_n]$ be the Kazhdan–Lusztig basis of the
group algebra of the symmetric group.  Define the classical-limit
functor*

$$
  \mathrm{KL}\colon\;
    \mathrm{mod}\,H_n(R, q)
    \;\longrightarrow\;
    \mathrm{mod}\,\mathbb{Z}[S_n],
  \qquad
  b_w \;\longmapsto\; C_w \quad \text{as } q \to 1,
$$

*sending each KLR canonical basis element to its
$q \to 1$ specialisation in $\mathbb{Z}[S_n]$.  Then $\mathrm{KL}$ is
a :refterm[monoidal functor]{#monoidal-functor} compatible with the
[observation functor](#def:observation) $\tau$, and its action on
QOU particle states is precisely the topological-to-classical
transition: the braid group $B_n$ collapses to $S_n$ via
$\sigma_i^2 \mapsto 1$, the Hecke matrices lose their topological
braiding memory, and the surviving statistics are exactly the
$\pm 1$ permutation signs that govern Pauli exclusion (fermions) and
Bose–Einstein occupation (bosons).*

**Algorithmic role.**
*The reduction engine implements the classical limit by replacing
$\sigma_{s_i}$ with the symmetric-group generator $s_i$ and the canonical
basis element $b_w$ with the Kazhdan–Lusztig basis element $C_w$;
the cyclotomic-KLR Wedderburn decomposition specialises to the
ordinary $S_n$ Wedderburn decomposition, with multiplicities given
by hook-length formulae.  The transition is functorial — no extra
selection rule is introduced for the bosonic vs fermionic split; the
split is the eigenvalue decomposition of $s_i$ acting on the
$q \to 1$ canonical basis.*

**Conjectural status.**
*The $q \to 1$ specialisation of $H_n(R, q)$ to $\mathbb{Z}[S_n]$ is
classical \cite{kassel1995}, as is the $b_w \to C_w$ correspondence
on the level of canonical bases \cite{khovanovlauda2009,
kashiwara1991}.  What remains conjectural is the compatibility of
this specialisation with the observation functor $\tau$ on the full
QOU spectrum: that the macroscopic Pauli/Bose statistics observed in
laboratory frames are exactly the $\mathrm{KL}$-image of the
anyonic Hecke statistics of the substrate.  Falsification is by
exhibiting a macroscopic statistic that is neither bosonic nor
fermionic at the cooled, observed boundary.*
<!-- FILE_END: kazhdan-lusztig-classical-limit.md -->

<!-- FILE_START: anyon-observation-collapse.md -->
**Remark (anyon ladder under the observation functor).**
*The three preceding conjectures organize into a single ladder
indexed by the deformation parameter $q$:*

| $q$ regime | Substrate state | Observation image |
|---|---|---|
| Generic $q$ ([anyonic substrate](#conj:hecke-anyonic-substrate)) | Abelian anyons in $H_n(R, q)$ | Topological braiding matrices |
| $q = e^{2\pi i / k}$ ([MTC truncation](#conj:root-of-unity-mtc-truncation)) | Non-abelian anyons in $\mathrm{MTC}_k$ | Finite fusion / $F$- and $R$-matrices |
| $q \to 1$ ([KL classical limit](#conj:kazhdan-lusztig-classical-limit)) | Symmetric-group representations | Pauli ($\pm 1$) statistics |

*Reading the ladder downwards represents the
[observation functor](#def:observation) $\tau$ acting on a cooling
substrate. Anyonic braiding loses information at each step, yet it never
abandons the categorical algebraic substrate. We use
[Kashiwara crystal traversals](#conj:crystal-graph-realization)
to compute pair production and stable
masses. These map the fusion rules of the appropriate rung: the
generic Hecke fluid for high-energy interactions, $\mathrm{MTC}_k$
for topologically ordered phases, and $\mathbb{Z}[S_n]$ for the
classical-statistics regime accessed by macroscopic detectors.*

**Algorithmic synthesis.**
*The reduction engine selects the rung by the value of $q$ supplied
to the substrate. It uses generic $q$ for the open-ended Hecke evaluation, a root
of unity for fusion-category enumeration, and $q \to 1$ for the
Pauli/Bose decomposition. The same canonical-basis machinery
applies at every rung. Only the specialization map changes.*
<!-- FILE_END: anyon-observation-collapse.md -->

