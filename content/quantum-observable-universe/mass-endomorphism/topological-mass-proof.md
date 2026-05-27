The proof proceeds in four steps: decomposition of the mass integral
using the :refterm[descent]{#descent} involution, identification of the descended term
with the unknot-core holonomy, localisation of the transient terms to
exceptional divisors, and evaluation via the quantum dilogarithm.

By
([eigenspace decomposition of the mass integrand](#lem\:topological-mass-eigenspace-decomp)),
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
([descended term is the unknot-core holonomy](#lem\:topological-mass-holonomy)),
the first summand equals
$\lVert \mathrm{Hol}_{\nabla_A}(\varrho_0; \mathfrak{G}) \rVert$.  By
([transient terms localise to exceptional divisors](#lem\:topological-mass-transient-localisation)),
the second summand decomposes as
$\sum_{i=1}^{N} \lVert \mathrm{MI}\!\!\int_{E_i} (\nabla_A q, L \wedge F^+) \rVert$.
Combining these yields

$$
  \mathfrak{m}(\varrho)
  =
  \bigl\lVert \mathrm{Hol}_{\nabla_A}(\varrho_0; \mathfrak{G}) \bigr\rVert
  +
  \sum_{i=1}^{N}
  \bigl\lVert \mathrm{MI}\!\!\int_{E_i} (\nabla_A q, L \wedge F^+) \bigr\rVert,
$$

which is the claimed decomposition
[eq:topological-mass-decomp](#eq\:topological-mass-decomp).  Each
exceptional-divisor summand equals the quantum dilogarithm
$\Phi_q(z_i)$ by
([quantum dilogarithm evaluation](#lem\:topological-mass-dilogarithm)),
completing the proof.  $\square$
