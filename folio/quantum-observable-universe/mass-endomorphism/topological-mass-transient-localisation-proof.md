**Proof.**
The transient component $\alpha - \hat{\tau}_n(\alpha)$ is annihilated by
$\hat{\tau}_n$: it lies in
$\mathcal{A}_{n+1}^{\mathrm{trans}} = \ker\hat{\tau}_n$
([:refterm[descent]{#descent} eigenspaces](#prop:descent-eigenspaces)).  By the structure of the
defining boundary ([brane boundary](#def:brane-boundary)), the support of
a transient section is contained in a neighbourhood of the boundary
$\partial \mathcal{S}_n$, which has codimension $\geq 2$ in $\mathcal{S}_n$ (item (1)) and
whose fibre at each blow-up centre $p_i$ is the exceptional divisor
$E_i \cong \mathbb{P}^1(\mathbb{C})$ (item (2)).

On the surface $\Sigma$, the transient integrand is therefore supported
on the discs $D_i$ centred at the blow-up points.  Since the $D_i$ are
disjoint (each blow-up introduces a new connected component of
$\partial \mathcal{S}_n$), the multiplicative integral splits as an
ordered product:

$$
  \mathrm{MI}\!\!\int_\Sigma
  \bigl(\alpha - \hat{\tau}_n(\alpha)\bigr)
  = 
  \prod_{i=1}^{N}
  \mathrm{MI}\!\!\int_{D_i}
  \bigl(\nabla_A q, L \wedge F^+\bigr).
$$

Since the integrand is supported on the exceptional fibre
$E_i \subset D_i$, each disc integral equals the corresponding
exceptional-divisor integral.  The norm on the structure group is a group
seminorm, so it satisfies the triangle inequality
$\lVert gh \rVert \le \lVert g \rVert + \lVert h \rVert$, and induction
on $N$ gives

$$
  \bigl\lVert
  \prod_{i=1}^{N}
  \mathrm{MI}\!\!\int_{D_i}
  \bigl(\nabla_A q, L \wedge F^+\bigr)
  \bigr\rVert
  \le
  \sum_{i=1}^{N}
  \bigl\lVert
  \mathrm{MI}\!\!\int_{E_i}
  \bigl(\nabla_A q, L \wedge F^+\bigr)
  \bigr\rVert.
$$

$\square$

The splitting and support hypotheses do not yield equality.  Commutation
of the disc integrals modulo the central band $\mathcal{O}_M^{\times}$ of
the gerbe does not make the norm additive: the group
$\mathrm{Multiplicative}\,\mathbb{R}$ is commutative, and its elements
$\mathrm{ofAdd}(1)$ and $\mathrm{ofAdd}(-1)$ have norms summing to $2$
while their product $\mathrm{ofAdd}(0)$ has norm $0$.  Equality would
require a further structural input, for instance that the disc integrals
lie on a common ray on which the norm is additive.  No such phase-alignment condition is
established here, so exact additivity is unproved.
