**Definition.**
*Let $K_0(\mathrm{Var}_k)$ be the **Grothendieck ring of varieties**
over the base field $k$ — the free abelian group on isomorphism
classes $[X]$ of $k$-varieties modulo the scissor relations
$[X] = [Z] + [X \setminus Z]$ for closed $Z \subseteq X$, with
product $[X] \cdot [Y] = [X \times Y]$. Let $\mathbb{L} = [\mathbb{A}^1_k]
\in K_0(\mathrm{Var}_k)$ denote the **Lefschetz motive**, and write
$\mathcal{M} := K_0(\mathrm{Var}_k)[\mathbb{L}^{-1}]$ for its
localization. The **motivic mass measure** of the QOU brane is the
Kontsevich--Denef--Loeser motivic measure*

$$
  \mu \;:\; \mathcal{B}(\mathcal{L}(X))
  \;\longrightarrow\;
  \widehat{\mathcal{M}}
$$

*on cylindrical (Borel) subsets of the
[arc space](#def:arc-space) $\mathcal{L}(X)$ of a brane variety $X$,
valued in the dimension-completion $\widehat{\mathcal{M}}$ of
$\mathcal{M}$. Volumes of measurable subsets are computed by*

$$
  \mu(A)
  \;=\;
  [\pi_n(A)] \;\mathbb{L}^{-(n+1)\dim X}
  \qquad
  (\pi_n \colon \mathcal{L}(X) \to \mathcal{L}_n(X)),
$$

*independently of $n$ once $A$ is stable at level $n$.*

**Mass from blow-ups.** When the categorical
Gröbner--Shirshov reduction
([three-parameter Wedderburn formula](#thm:wedderburn-mass-formula))
processes a braid $\beta \in H_n(R, q)$, it performs a finite sequence
of algebraic blow-ups of the brane variety $X$ along the crossing
loci, producing exceptional divisors $E_1, \dots, E_r$ with
multiplicities (or codimension weights) $d_1, \dots, d_r$. The
**topological mass** of the reduced state is the motivic integral
of the trivial function over the arc space, computed by Kontsevich's
change-of-variables formula as

$$
  \mathfrak{m}_{\mathrm{mot}}(\beta)
  \;:=\;
  \int_{\mathcal{L}(X)} d\mu
  \;=\;
  \sum_{i=1}^{r}\, [E_i^{\circ}] \, \mathbb{L}^{-d_i}
  \;\in\;\widehat{\mathcal{M}},
$$

*where $[E_i^{\circ}]$ is the class of the smooth open part of the
$i$-th exceptional divisor.*

**Motivic rationale.** The mass endomorphism
([proton--electron mass ratio](#prop:mass-endomorphism-tower))
needs to assign a finite, $q$-discrete weight to a Gröbner-Shirshov
reduction whose intermediate states are singular: there is no smooth
volume form to integrate, no measure-theoretic Lebesgue construction
that survives the blow-up. The motivic measure $\mu$ assigns each
reduction step a value in the Grothendieck ring $\mathcal{M}$,
purely algebraically, by tracking which classes of varieties appear
as exceptional fibers. The categorical analogue of crossing the
$\chi(A) = -6$ topological horizon
([topological mass formula](#prop:topological-mass-formula)) is
exactly the contribution $[E_i^{\circ}] \mathbb{L}^{-d_i}$ of the
exceptional divisor of that blow-up.

The motivic mass $\mathfrak{m}_{\mathrm{mot}}(\beta)$ is a class in
$\widehat{\mathcal{M}}$ — a *motive*, not yet a real number. The
real-valued physical mass is recovered by applying the
[archimedean realization functor](#def:archimedean-realization-functor)
of the next subsection.
