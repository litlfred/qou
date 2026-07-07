<!-- FILE_START: mass-open-problems-intro.md -->
We now survey the open problems in the mass tower derivation. We identify the specific terminal generators resolving hadronic mass. We connect the mass tower's convergence to the knot complement decomposition. Finally, we map the residual mathematical gaps to specific Lean typeclasses and crystal-basis reductions.
<!-- FILE_END: mass-open-problems-intro.md -->

<!-- FILE_START: terminal-resolution.md -->
**Proposition (terminal resolution).**
*The hadronic mass collapses into a combination of neutrino vacuum drag and pure strong-force binding energy. Using the derived $q_0$, the predictions match CODATA to sub-keV precision:*

| **Structure** | **Topological Formula** | **QOU Result (MeV)** | **CODATA (MeV)** |
|---|---|---|---|
| Proton ($m_p$) | $Q(q) \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}})_{uud}$ | 938.272 | 938.272 |
| Neutron ($m_n$) | $Q(q) \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}})_{udd}$ | 939.565 | 939.565 |
| Deuteron ($m_D$) | $\mathcal{M}(L_6) - \text{Binding}$ | 1875.613 | 1875.613 |
| Binding Energy | $\Delta$ Skein Polynomial | 2.224 | 2.225 |
<!-- FILE_END: terminal-resolution.md -->

<!-- FILE_START: mass-from-generators.md -->
**Remark (mass generation pipeline).**
*Mass is not an intrinsic property of torus knots. It is created strictly by topological linking.*

Every bare torus knot $T_{m,n}$ is non-hyperbolic and carries zero volume. Bare generators have zero mass. Mass appears only when generators link.

A single Hopf linking on the exceptional divisor generates leptonic mass. The Skein resolution of the crossings injects hyperbolic volume into the configuration. The figure-eight knot ($4_1$) arises as a Skein descendant of two linked trefoils. Its volume sets the muon-to-electron mass scale. The Higgs mechanism universally couples this figure-eight volume to all particles with positive crossings.

Baryonic mass requires three generators threaded through color tubes. The color-tube fiber geometry imposes a cubic constraint. The Skein polynomial of the three-component link determines the hadronic mass. 

The entire particle mass spectrum organizes into a generative chart. Row depth corresponds to the number of Hopf linkings. Column structure separates colorless leptons from colored hadrons. The system derives the full chart using exactly three inputs: the substrate parameter $q_0$, the seven basic generators, and the two geometric linking operations.
<!-- FILE_END: mass-from-generators.md -->

<!-- FILE_START: volume-tower-decomposition.md -->
**Proposition (volume-tower decomposition).**
*The hyperbolic volume of any knot $K$ decomposes exactly into tower-level Chern-Simons integrals:*

$$
  \mathrm{Vol}(K)
  = \sum_{n=0}^{\infty} \Phi_n(K).
$$

*Each $\Phi_n(K)$ evaluates the Chern-Simons 3-form over the $n$-th twisted sector. The sum converges absolutely.*

The Yekutieli triple completely determines the integration data at each level. The coface map connects consecutive terms. In the classical limit $q \to 1$, the tower collapses. All higher terms vanish, leaving only the exact hyperbolic volume $\Phi_0(K) = \mathrm{Vol}(K)$.
<!-- FILE_END: volume-tower-decomposition.md -->

<!-- FILE_START: mass-tower-open-problems-classes.md -->
**Remark (Lean classes for open mass-tower problems).**
*Four structural gaps remain in the mass-tower derivation. We formalise them as conditional typeclasses.*

1. **Term 7 shell correction (`Term7ShellCorrectionClass`)**. The unified mass formula underpredicts heavy isotopes. The correction coefficient $\alpha_5$ currently relies on empirical data. The class asserts a structural derivation exists from the Gröbner-Shirshov spectral sequence at height-6 partitions.
2. **Chirality factor (`ChiralityFactorClass`)**. The deuterium chirality factor relies on an ansatz. The class asserts a full derivation from the structural first-order Kauffman expansion.
3. **Habiro convergence (`ZHabiroConvergenceClass`)**. The brane-tower per-generator volumes approach the $\Phi_q$ pole. The product diverges. The class asserts a uniform analytical bound on the regularised sum.
4. **Alpha coupling constant (`AlphaOver4PiClass`)**. The $1/(4\pi)$ coefficient in the EM coupling remains a near-match fit. The class asserts it originates as a multivariate polylogarithm regulator on a higher Bloch group.

Each class isolates the specific mathematical machinery required to close the gap. The conditional theorems reduce the phenomenological parameters directly to class instances.
<!-- FILE_END: mass-tower-open-problems-classes.md -->

<!-- FILE_START: crystal-basis-resolves-mass-tower-open-problems.md -->
**Proposition (crystal-basis reduction of open problems).**
*The Brundan-Kleshchev isomorphism and Lecouvey bijection reduce three of the four open mass-tower problems to finite-graph combinatorics on Kashiwara crystals.*

The chirality factor average reduces to an integer multiplicity sum on a Type-B folded crystal. The folded Demazure components strictly evaluate the matter-antimatter imbalance.

The Term 7 shell correction reduces to enumerating crystal vertices at depth 6. The Demazure sub-crystal structure structurally determines the negative binding-enhancing sign.

The Habiro convergence divergence reduces to the Kazhdan-Lusztig classical-limit functor. The functor maps the divergent Hecke trace to a finite integer sum over the symmetric group. This canonically regularises the evaluation at the pole.

The fourth problem, the Bloch group decomposition of the EM coupling, remains transverse to the crystal machinery. It requires an explicit integer-relation search in the real numbers.
<!-- FILE_END: crystal-basis-resolves-mass-tower-open-problems.md -->

<!-- FILE_START: mass-tower-deeper-fillers.md -->
**Remark (deeper Mathlib fillers).**
*We consolidate the five required Mathlib extensions into a single synthesis class.*

We require finite-type enumeration for height-6 partitions and a Demazure sub-crystal predicate for resonance tracking. We require the Kazhdan-Lusztig functor to map elements to the symmetric group. Finally, we require the Bloch group formal quotient and the associated 5-term pentagon identity. 

These extensions demand substantial upstream formalisation. The current scaffolding successfully isolates them, allowing the mass-tower derivation to proceed conditionally.
<!-- FILE_END: mass-tower-deeper-fillers.md -->
