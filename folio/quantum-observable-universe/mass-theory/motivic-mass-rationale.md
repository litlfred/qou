The mass endomorphism
([proton--electron mass ratio](#prop:mass-endomorphism-tower))
must assign a finite, $q$-discrete weight to a Gröbner--Shirshov
reduction whose intermediate states are singular: there is no smooth
volume form to integrate, no measure-theoretic Lebesgue construction
that survives the blow-up. The motivic measure $\mu$ of
[def:motivic-mass-measure](#def:motivic-mass-measure) assigns each
reduction step a value in the Grothendieck ring $\mathcal{M}$, purely
algebraically, by tracking which classes of varieties appear as
exceptional fibers. The categorical analogue of crossing the
$\chi(A) = -6$ topological horizon
([topological mass formula](#prop:topological-mass-formula)) is
exactly the contribution $[E_i^{\circ}] \mathbb{L}^{-d_i}$ of the
exceptional divisor of that blow-up.

The motivic mass $\mathfrak{m}_{\mathrm{mot}}(\beta)$ is a class in
$\widehat{\mathcal{M}}$ — a *motive*, not yet a real number. The
real-valued physical mass is recovered by applying the
[archimedean realization functor](#def:archimedean-realization-functor),
constructed later in this chapter once the adelic substrate it projects
from is in place.

**Mass from blow-ups.** When the categorical
Gröbner--Shirshov reduction
([three-parameter Wedderburn formula](#thm:wedderburn-mass-formula))
processes a braid $\beta \in H_n(R, q)$, it performs a finite sequence
of algebraic blow-ups of the brane variety $X$ along the crossing
loci, producing exceptional divisors $E_1, \dots, E_r$ with
multiplicities (or codimension weights) $d_1, \dots, d_r$. The
topological mass of the reduced state is the motivic integral
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

where $[E_i^{\circ}]$ is the class of the smooth open part of the
$i$-th exceptional divisor.
