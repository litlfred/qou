The proof proceeds in four steps: decomposition of the mass integral
using the :refterm[descent]{#descent} involution, identification of the descended term
with the unknot-core holonomy, localisation of the transient terms to
exceptional divisors, and evaluation via the quantum dilogarithm.

By
([eigenspace decomposition of the mass integrand](#lem:topological-mass-eigenspace-decomp)),
the :refterm[descent]{#descent} involution $\hat{\tau}_n$ produces an orthogonal
Killing-form decomposition of the multiplicative integral

$$
  \mathfrak{m}(\varrho)
  =
  \bigl\lVert \mathrm{MI}\!\!\int_\Sigma \hat{\tau}_n(\alpha) \bigr\rVert
  +
  \bigl\lVert \mathrm{MI}\!\!\int_\Sigma (\alpha - \hat{\tau}_n(\alpha)) \bigr\rVert.
$$

By
([descended term is the unknot-core holonomy](#lem:topological-mass-holonomy)),
the first summand equals
$\lVert \mathrm{Hol}_{\nabla_A}(\varrho_0; \mathfrak{G}) \rVert$.  By
([transient terms are bounded by exceptional-divisor contributions](#lem:topological-mass-transient-localisation)),
the second summand is at most
$\sum_{i=1}^{N} \lVert \mathrm{MI}\!\!\int_{E_i} (\nabla_A q, L \wedge F^+) \rVert$.
Combining these yields

$$
  \mathfrak{m}(\varrho)
  \le
  \bigl\lVert \mathrm{Hol}_{\nabla_A}(\varrho_0; \mathfrak{G}) \bigr\rVert
  +
  \sum_{i=1}^{N}
  \bigl\lVert \mathrm{MI}\!\!\int_{E_i} (\nabla_A q, L \wedge F^+) \bigr\rVert,
$$

an upper bound for the claimed decomposition
[the topological mass decomposition](#eq:topological-mass-decomp).  This route
gives equality, and hence the decomposition itself, only conditionally on
equality in the transient bound, which is open (it is not forced by the
disc splitting and support hypotheses).  Each
exceptional-divisor summand equals the quantum dilogarithm
$\Phi_q(z_i)$ by
([quantum dilogarithm evaluation](#lem:topological-mass-dilogarithm)),
so the bound reads
$\mathfrak{m}(\varrho) \le \lVert \mathrm{Hol}_{\nabla_A}(\varrho_0; \mathfrak{G}) \rVert + \sum_{i=1}^{N} \Phi_q(z_i)$.  $\square$
