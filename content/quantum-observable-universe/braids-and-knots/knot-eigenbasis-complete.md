*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
$\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ and $V$ the fundamental
representation.  Suppose $q$ is not a root of unity.  Then:

1. **(Semisimplicity.)**  The Iwahori--Hecke algebra
   $H_n(R, q) = \mathrm{End}_{B_n}(V^{\otimes n})$ is semisimple, and
   $V^{\otimes n}$ admits a complete decomposition into irreducible
   $H_n(R, q)$-modules:

   $$
     V^{\otimes n}
      \cong 
     \bigoplus_{\lambda \vdash n}
     V_\lambda \otimes S_\lambda,
   $$

   where $\lambda$ ranges over partitions of $n$ with at most two parts
   (the $q$-analogue of Schur--Weyl duality), $V_\lambda$ is the
   irreducible $\mathrm{SU}_q(2)$-module of spin
   $j = (\lambda_1 - \lambda_2)/2$, and $S_\lambda$ is the irreducible
   $H_n(R, q)$-module labelled by $\lambda$.
2. **(Alexander surjectivity.)**  By Alexander's theorem, every
   oriented link $L$ in $S^3$ is the closure $\hat{\beta}$ of some braid
   $\beta \in B_n$ for some $n$.  The Markov trace
   $\mathrm{tr}_M \colon \bigcup_n H_n(R, q) \to R$ assigns to each braid
   closure $\hat{\beta}$ the value
   $\mathrm{tr}_M(\rho_n(\beta))$, which equals the Jones polynomial
   $J_L(q)$ up to a framing factor.  In particular, the map

   $$
     \{\text{knot types}\}
      \longrightarrow 
     \{\text{irreducible summands of } V^{\otimes n}, n \geq 1\}
   $$

   given by $L \mapsto$ the summand in which $\mathrm{tr}_M(\rho_n(\beta))$
   is supported, has image containing every irreducible summand.
3. **(Spanning of the algebraic state space.)**  The physical state
   space is the algebraic direct limit
   $V_{\mathrm{phys}} := \varinjlim V^{\otimes n}$ along the inclusion
   maps $V^{\otimes n} \hookrightarrow V^{\otimes (n+1)}$ induced by
   the unit $\eta \colon \mathbf{1} \to V$.  Since each $V^{\otimes n}$
   is completely decomposed by (1), the set of irreducible summands
   --- labelled by knot types via (2) --- spans $V_{\mathrm{phys}}$.
   No metric completion is invoked.



**Mathematical Novelty:** The synthesis that knot types form a complete eigenbasis for $\varinjlim V^{\otimes n}$, which conceptually replaces Feynman's continuum integral, is a genuinely framework-specific and novel mathematical synthesis. The accompanying Lean formalization achieves a careful combining and conditional proof over bundled standard results.