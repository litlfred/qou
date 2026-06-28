## Local cohomology and topological selection

**The local cohomology connection.**
The [local cohomology group](#def\:local-cohomology-group)
$H^1_{\mathfrak{m}_1}(A)$ at the unit defect $z = 1$ measures
precisely the obstruction to extending sections across the
singularity.  At $q = 1$, the defect locus $\{z = 1\}$ is the
entire base manifold (the substrate parameter is identically
$1$), so:

$$
  H^1_{\mathfrak{m}_1}(A)\big|_{q=1}
  = 
  R^1\Gamma_{\mathfrak{m}_1}(A)
   \neq  0.
$$

This nonvanishing is the algebraic origin of the blowup: the
$\mathfrak{m}_1$-torsion functor has nontrivial derived functor
precisely at the point $q = 1$ where regularity fails.

For $q > 1$, the defect locus $\{z = q^{-1}\} \neq \{z = 1\}$
is separated from the unit, and $H^1_{\mathfrak{m}_1}(A) = 0$
— no obstruction, hence regularity.

**The :refterm[descent]{#descent} condition and vortex reconnection.**
The [twisted 2-cocycle condition](#prop\:descent-condition)

$$
  d(g_{ijk}^{(n)}) = a_{ij}^{(n)} \cdot g_{ijk}^{(n)}
  \cdot (a_{jk}^{(n)})^{-1}
$$

fails at the singular set $\Sigma$ because the transition
functions $g_{ij}^{(n)}$ develop discontinuities there.  In the
fluid picture, these discontinuities correspond to
[vortex reconnection](#rem\:vortex-reconnection) events where the
divisor topology changes.  The obstruction class $\kappa_{n^*}$
measures the total topological change at $\Sigma$: it is the
net "reconnection charge" — the signed count of reconnection
events weighted by their fusion-rule multiplicities.

**Constraint from Berry phase.**
The obstruction class must be consistent with the
$\mathrm{SU}_q(2)$ representation theory.  Specifically,
$\kappa_{n^*}$ must lie in the image of the character map

$$
  \chi \colon
  \mathrm{Rep}(\mathrm{SU}_q(2))
   \to 
  H^2(\Sigma, \mathcal{B}),
$$

which restricts the possible values of $\kappa_{n^*}$ to a
discrete lattice.  This is a **topological selection rule** on
the blowup: not all vorticity concentrations are allowed, only
those whose cohomological charge is compatible with the
categorical structure.
