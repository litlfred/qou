<!-- FILE_START: framing-arc-intro.md -->
Five structural steps map the logical arc of this paper. Every quantum observable universe realises these steps. The sequence runs from categorical foundations to physical prediction.

1. **Categorical step.** A rigid braided monoidal category with a Frobenius–Hopf object, parametrised by the substrate $q$.
2. **Algebraic step.** The braid group $B_n$ and its Hecke quotient $H_n(q)$, equipped with a Markov trace.
3. **Geometric step.** Knot complements realised as $q$-hyperbolic structures. The Reeb-bundle complement equals the volume invariant.
4. **Archimedean step.** Specialisation $R \to R[i] \to R[i][q, q^{-1}]$ at $q = q_0$. The non-abelian Stokes mass identity closes the arc.
5. **Physical step.** Predicted spectra and observations.

This chapter outlines each step, fixes the standard terminology, and catalogues alternative models (Calabi–Yau, ALE, $p$-adic, characteristic $p$). These models realise the common axioms across different arithmetic settings.
<!-- FILE_END: framing-arc-intro.md -->

<!-- FILE_START: step-categorical.md -->
**Categorical step.** The substrate parameter $q$ requires a structure to deform. At $q = 1$, the classical symmetric tensor category appears. For $q \neq 1$, the action resolves into a braided one. The substrate is a rigid braided monoidal category $(\mathbf{C}, A, \tau)$ equipped with a Frobenius–Hopf object $A$ and a fibre functor $\tau$. The parameter $q$ records the deformation of this categorical action. The Reeb derivation $\delta_q$ promotes $q$ to a connection on the categorical bundle; its curvature is the Yekutieli MI tower. We develop the axioms and derive the Reeb derivation in subsequent chapters. We develop descent, jets, and the Gröbner–Shirshov filtration to provide the categorical infrastructure.
<!-- FILE_END: step-categorical.md -->

<!-- FILE_START: step-algebraic.md -->
**Algebraic step.** To turn the categorical action into a computable knot invariant, we pass from braids to a trace-carrying quotient. The braid group $B_n$ acts on $A^{\otimes n}$. The quotient by the Hecke relation $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ is the Iwahori–Hecke algebra $H_n(q)$. This algebra controls the combinatorics of the categorical action. The Markov trace $\mathrm{tr}_M$ packages braid words into a class function. Evaluation on $\beta_K$ yields the Jones polynomial $J_K(q) = \mathrm{tr}_M(\rho(\beta_K))$. We develop braids, knot groups, the Hecke algebra, and the Skein-relation translation.
<!-- FILE_END: step-algebraic.md -->

<!-- FILE_START: step-geometric.md -->
**Bring's surface — the canonical geometric object.** The geometric step realises the mass of every knot on one fixed surface. The canonical geometric realisation is Bring's surface $\Sigma_4$. This is the genus-4 smooth projective curve with Euler characteristic $\chi = -6$ and automorphism group $\mathrm{Aut}(\Sigma_4) \cong S_5$. It is the vanishing locus on $\mathbb{P}^4$ of the first three power sums:

$$
  \Sigma_4 = \mathrm{Proj}\!\left(
    R[x_0,\dots,x_4]\Big/\bigl(\textstyle\sum x_j,
    \textstyle\sum x_j^2, \textstyle\sum x_j^3\bigr)
  \right).
$$

Structural facts include:
- $\Sigma_4$ has genus $g = 4$ and Euler characteristic $\chi(\Sigma_4) = 2 - 2g = -6$.
- The automorphism group is $\mathrm{Aut}(\Sigma_4) \cong S_5$. The orientation-preserving subgroup $A_5 \subset S_5$ acts faithfully and supplies the symmetry group of the canonical particle assignment.
- $\Sigma_4$ is the canonical archimedean model. The substrate parameter $q_0$ is fixed by its $\chi = -6$ structure. The Reeb derivation produces a $q$-hyperbolic structure on $\Sigma_4$ with five $S_5$-equivalent fibres.
- The cohomological defect of $\Sigma_4$ — the discrepancy between its first Betti number and the rank of the natural three-colour bundle — supplies the origin of the three-colour SU(3) charge of QCD.

**Geometric step.** The Reeb derivation lifts a braid word $\beta_K$ to a Reeb flow. The complement $S^3 \setminus K$ is a $q$-hyperbolic 3-manifold. By a theorem of Yekutieli, this complement carries a tessellation by ideal $q$-tetrahedra indexed by $k = 0, 1, 2, 3$ with cell coefficients $(1, 4, 16, 64)$. The volume $\mathrm{Vol}(K)$ of the complement is the central geometric invariant. This volume realises the topological mass of the knot. Evaluating it on $\Sigma_4$ assigns each knot its mass. The cohomological defect of $\Sigma_4$ supplies the three-colour charge. The surface fixes both the mass and the colour structure. We derive the volume identity, the tangle-energy decomposition, and the mass-endomorphism statement.
<!-- FILE_END: step-geometric.md -->

<!-- FILE_START: step-archimedean.md -->
**Archimedean step.** Specialisation at the substrate value $q_0$ produces archimedean (real-valued, dimensional) quantities and yields a dimensional mass. The machinery is a chain of extensions of the generic categorical content. Stated over a commutative ring $R$, it specialises through $R \to R[i] \to R[i][q, q^{-1}]$. The $\chi = -6$ structure of Bring's surface fixes the substrate value $q = q_0$.

The mass endomorphism $\mathfrak{m}(K) = \mathrm{Vol}(K) \cdot c_q^{-2}$ is the non-abelian Stokes integration of the Reeb flow against the categorical action. We evaluate it using Wedderburn decomposition, partition channels $y_\lambda \chi^\lambda$, crystal bases, and $\Delta_\lambda$ gating.

Alternatives to the archimedean specialisation include $p$-adic ($R \to \mathbb{Q}_p$) and characteristic-$p$ ($R \to \mathbb{F}_p[T]$) substrate completions. These are non-archimedean and do not produce dimensional masses.
<!-- FILE_END: step-archimedean.md -->

<!-- FILE_START: step-physical.md -->
**Physical step.** The archimedean specialisation at $q_0$ fixed on Bring's surface predicts a particle spectrum from three calibration inputs ($m_e$, $m_\mu/m_e$, $\mathfrak{Q}_\beta$). We develop the particle-generation mechanism (LP/SDP confinement, operator-valued folding/unfolding). We derive Pauli exclusion and the fermion/boson split from the rigid-braided structure. We catalogue these predictions (leptons, quarks, baryons, nuclei, $\mathfrak{Q}_\beta$, magnetic moments) and compare them to observations. We extend the framework to atomic, molecular, and organic chemistry.

We develop fluid dynamics of the brane, stochastic mechanics of the Markov trace, categorical information theory, quantum measurement as fibre-functor behaviour, and the $q$-geometric Langlands correspondence.
<!-- FILE_END: step-physical.md -->
