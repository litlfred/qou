Let $(\mathcal{C}, A, \omega)$ be a quantum observable universe with
$\mathcal{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ and $V$ the fundamental
representation.  Suppose $q$ is not a root of unity.  Then:

1. **(Semisimplicity.)**  The Hecke algebra
   $H_n(q) = \mathrm{End}_{B_n}(V^{\otimes n})$ is semisimple, and
   $V^{\otimes n}$ admits a complete decomposition into irreducible
   $H_n(q)$-modules:
   $$
     V^{\otimes n}
     \;\cong\;
     \bigoplus_{\lambda \,\vdash\, n}
     V_\lambda \otimes S_\lambda,
   $$
   where $\lambda$ ranges over partitions of $n$ with at most two parts
   (the $q$-analogue of Schur--Weyl duality), $V_\lambda$ is the
   irreducible $\mathrm{SU}_q(2)$-module of spin
   $j = (\lambda_1 - \lambda_2)/2$, and $S_\lambda$ is the irreducible
   $H_n(q)$-module labelled by $\lambda$.
2. **(Alexander surjectivity.)**  By Alexander's theorem, every
   oriented link $L$ in $S^3$ is the closure $\hat{\beta}$ of some braid
   $\beta \in B_n$ for some $n$.  The Markov trace
   $\mathrm{tr}_M \colon \bigcup_n H_n(q) \to R$ assigns to each braid
   closure $\hat{\beta}$ the value
   $\mathrm{tr}_M(\rho_n(\beta))$, which equals the Jones polynomial
   $J_L(q)$ up to a framing factor.  In particular, the map
   $$
     \{\text{knot types}\}
     \;\longrightarrow\;
     \{\text{irreducible summands of } V^{\otimes n},\; n \geq 1\}
   $$
   given by $L \mapsto$ the summand in which $\mathrm{tr}_M(\rho_n(\beta))$
   is supported, has image containing every irreducible summand.
3. **(Density in the physical Hilbert space.)**  In the
   archimedean realisation, the physical state space is the direct limit
   $\mathcal{H}_{\mathrm{phys}} = \varinjlim\, V^{\otimes n}$ along
   the inclusion maps
   $V^{\otimes n} \hookrightarrow V^{\otimes (n+1)}$ induced by the
   unit $\eta \colon \mathbf{1} \to V$.  Since each $V^{\otimes n}$ is
   completely decomposed by (1), the set of irreducible summands ---
   labelled by knot types via (2) --- spans a dense subspace of
   $\mathcal{H}_{\mathrm{phys}}$ in the Hilbert completion.

---

*Part (1).*  When $q$ is not a root of unity, the Hecke algebra
$H_n(q)$ is isomorphic to $\mathbb{C}[S_n]$ as an abstract algebra
(Jimbo's theorem), hence semisimple.  The $q$-Schur--Weyl
decomposition of $V^{\otimes n}$ is the standard result for
$\mathrm{SU}_q(2)$; see e.g. Chari--Pressley, Chapter 10.  The
restriction to partitions with at most two parts reflects
$\mathrm{rank}(\mathrm{SU}(2)) = 1$: the Young diagrams are at most
two-rowed.

*Part (2).*  Alexander's theorem guarantees surjectivity of the
braid closure map $\beta \mapsto \hat{\beta}$.  The Markov trace on
$H_n(q)$ is the unique trace satisfying the Markov property
$\mathrm{tr}_M(x \sigma_n^{\pm 1}) = z^{\pm 1}\,\mathrm{tr}_M(x)$ for
$x \in H_n(q)$ and a parameter $z$ determined by $q$.  On each
irreducible summand $S_\lambda$, the trace restricts to a non-zero
scalar multiple of the character, so every summand is detected by
some braid closure.

*Part (3).*  The direct limit $\varinjlim\, V^{\otimes n}$ is a
pre-Hilbert space whose completion $\mathcal{H}_{\mathrm{phys}}$ is
separable (each $V^{\otimes n}$ is finite-dimensional).  The union of
the finite-dimensional subspaces $V^{\otimes n}$ is dense by
construction, and each is completely decomposed by (1).  Hence the
irreducible summands, indexed by knot types via the closure map,
span a dense subspace.
