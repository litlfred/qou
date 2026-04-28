**Proof.**
The transient component $\alpha - \hat{\tau}_n(\alpha)$ is annihilated by
$\hat{\tau}_n$: it lies in
$\mathcal{A}_{n+1}^{\mathrm{trans}} = \ker\hat{\tau}_n$
([descent eigenspaces](#prop:descent-eigenspaces)).  By the structure of the
defining boundary ([brane boundary](#def:brane-boundary)), the support of
a transient section is contained in a neighbourhood of the boundary
$\partial \mathcal{S}_n$, which has codimension $\geq 2$ in $\mathcal{S}_n$ (item (1)) and
whose fibre at each blow-up centre $p_i$ is the exceptional divisor
$E_i \cong \mathbb{P}^1(\mathbb{C})$ (item (2)).

On the surface $\Sigma$, the transient integrand is therefore supported
on the discs $D_i$ centred at the blow-up points.  Since the $D_i$ are
disjoint (each blow-up introduces a new connected component of
$\partial \mathcal{S}_n$), the multiplicative integral splits as a product:

$$
  \mathrm{MI}\!\!\int_\Sigma
  \bigl(\alpha - \hat{\tau}_n(\alpha)\bigr)
  = 
  \prod_{i=1}^{N}
  \mathrm{MI}\!\!\int_{D_i}
  \bigl(\nabla_A q, L \wedge F^+\bigr).
$$

Since the $D_i$ are geometrically disjoint and the group elements commute
up to the central band $\mathcal{O}_M^{\times}$ of the gerbe
(the transient modes are localised at distinct points, and the central
extension ensures that the group-valued integrals commute modulo the
band), the norm of the product equals the sum of the norms:

$$
  \bigl\lVert
  \prod_{i=1}^{N}
  \mathrm{MI}\!\!\int_{D_i}
  \bigl(\nabla_A q, L \wedge F^+\bigr)
  \bigr\rVert
  = 
  \sum_{i=1}^{N}
  \bigl\lVert
  \mathrm{MI}\!\!\int_{E_i}
  \bigl(\nabla_A q, L \wedge F^+\bigr)
  \bigr\rVert,
$$

where we replace $D_i$ by $E_i$ since the integrand is supported on the
exceptional fibre $E_i \subset D_i$.  $\square$
