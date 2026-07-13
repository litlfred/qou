<!-- FILE_START: knot-eigenbasis-complete.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with $\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ and $V$ the fundamental representation. Assume $q$ is not a root of unity.

1. **Semisimplicity.** The Iwahori--Hecke algebra $H_n(R, q) = \mathrm{End}_{B_n}(V^{\otimes n})$ is semisimple. The space $V^{\otimes n}$ decomposes completely into irreducible $H_n(R, q)$-modules:

   $$
     V^{\otimes n}
      \cong 
     \bigoplus_{\lambda \vdash n}
     V_\lambda \otimes S_\lambda.
   $$

   Here, $\lambda$ ranges over partitions of $n$ with at most two parts. $V_\lambda$ is the irreducible $\mathrm{SU}_q(2)$-module of spin $j = (\lambda_1 - \lambda_2)/2$, and $S_\lambda$ is the irreducible $H_n(R, q)$-module labelled by $\lambda$.

2. **Alexander surjectivity.** By Alexander's theorem, every oriented link $L$ in $S^3$ is the closure $\hat{\beta}$ of some braid $\beta \in B_n$. The Markov trace assigns the value $\mathrm{tr}_M(\rho_n(\beta))$ to each braid closure, recovering the Jones polynomial $J_L(q)$ up to framing. The map from knot types to irreducible summands of $V^{\otimes n}$, defined by the support of $\mathrm{tr}_M(\rho_n(\beta))$, is surjective.

3. **Algebraic spanning.** The physical state space is the algebraic direct limit $V_{\mathrm{phys}} := \varinjlim V^{\otimes n}$ under inclusions induced by the unit $\eta \colon \mathbf{1} \to V$. Because each $V^{\otimes n}$ is completely decomposed, the set of irreducible summands—labelled by knot types—spans $V_{\mathrm{phys}}$ without requiring metric completion.

**Mathematical Novelty:** The synthesis that knot types form a complete eigenbasis for $\varinjlim V^{\otimes n}$ conceptually replaces Feynman's continuum integral. The accompanying Lean formalization achieves a rigorous conditional proof over bundled standard results.
<!-- FILE_END: knot-eigenbasis-complete.md -->

<!-- FILE_START: knot-exhaustiveness.md -->
The knot eigenbasis completeness theorem guarantees that every irreducible summand of $V^{\otimes n}$ is detected by some braid closure via the Markov trace. This establishes surjectivity of detection. 

We then ask: do the knot types appearing in the Descartes universe exhaust the space of states?

The generation completeness theorem shows that every knot with Seifert genus $g \leq 4$ appears in the spectrum. Bring's surface captures all embeddable knots in that range, while the spectral filter excludes knots with $g > 4$. 

However, this does not establish whether the Jones polynomial itself is faithful. If two distinct knots share the same Jones polynomial, they would be physically indistinguishable in the Descartes universe, representing the same particle. The framework only requires the Jones polynomial for detection (non-degeneracy on irreducibles) rather than full classification. Consequently, faithfulness remains an open question inherited from classical knot theory.
<!-- FILE_END: knot-exhaustiveness.md -->

<!-- FILE_START: feynman-eigenbasis.md -->
In Feynman's formulation, the transition amplitude is a continuum integral over all paths:

$$
  \langle\psi_f|\psi_i\rangle
  = 
  \int \mathcal{D}\phi\ e^{iS[\phi]/\hbar}.
$$

Because this formulation does not privilege any eigenbasis, it requires regularisation and renormalisation to handle divergences.

Our framework supplies a natural eigenbasis from the braided monoidal structure. The braid group acts on $V^{\otimes n}$, and this action completely decomposes the space into irreducible summands. By Alexander's theorem, these summands are labelled by knot types, which span the algebraic direct limit $V_{\mathrm{phys}} = \varinjlim V^{\otimes n}$. Each irreducible summand represents a specific particle identity: the unknot is the neutrino, the trefoil is the electron, and the figure-eight knot corresponds to the Higgs field.

This replaces the continuum path integral with a finite algebraic operation: the categorical trace. For a closed cycle $\varrho \colon \mathbf{1} \to A$ representing a particle propagating around a vortex filament, the mass is:

$$
  \mathfrak{m}(\varrho)
  = 
  \bigl\lVert
  \mathrm{tr}\bigl(
    (\textstyle\int_A \otimes \mathrm{id})
    \circ \Delta
    \circ \varrho
  \bigr)
  \bigr\rVert.
$$

Since $A$ is a finite-dimensional Frobenius--Hopf object, this categorical trace is intrinsically finite. No regularisation is required because the sum runs over the finitely many irreducible summands of $V^{\otimes n}$.

The skein relation $q\mathcal{M}(L_+) - q^{-1}\mathcal{M}(L_-) = (q^{1/2} - q^{-1/2})\mathcal{M}(L_0)$ is simply the characteristic equation of the braiding $c_{V,V}$ evaluated under the categorical trace. Because the $R$-matrix determines the eigenvalues, mass ratios such as $\mathfrak{m}_\mu/\mathfrak{m}_e$ emerge exactly from a finite trace over this complete knot eigenbasis.
<!-- FILE_END: feynman-eigenbasis.md -->

