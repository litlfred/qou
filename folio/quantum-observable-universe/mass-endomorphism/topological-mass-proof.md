The proof proceeds in four steps: decomposition of the mass integral
using the :refterm[descent]{#descent} involution, identification of the descended term
with the unknot-core holonomy, localisation of the transient terms to
exceptional divisors, and evaluation via the quantum dilogarithm.

By
([eigenspace decomposition of the mass integrand](#lem:topological-mass-eigenspace-decomp)),
the :refterm[descent]{#descent} involution $\hat{\tau}_n$ produces an orthogonal
Killing-form decomposition of the multiplicative integral. Orthogonality makes
squared norms add, not norms; for the norms themselves the triangle inequality gives

$$
  \mathfrak{m}(\varrho)
  \le
  \bigl\lVert \mathrm{MI}\!\!\int_\Sigma \hat{\tau}_n(\alpha) \bigr\rVert +
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
  \bigl\lVert \mathrm{Hol}_{\nabla_A}(\varrho_0; \mathfrak{G}) \bigr\rVert +
  \sum_{i=1}^{N}
  \bigl\lVert \mathrm{MI}\!\!\int_{E_i} (\nabla_A q, L \wedge F^+) \bigr\rVert,
$$

the upper bound of [prop:topological-mass-upper-bound](#prop:topological-mass-upper-bound) in its archimedean form, and an upper bound for the conjectured decomposition
[eq:topological-mass-decomp](#eq:topological-mass-decomp).  Equality, and hence the conjectured decomposition itself, would need equality
in both inequalities above. Both are open: neither is forced by the disc
splitting and support hypotheses.  If each
exceptional-divisor summand equals the symmetric $q$-dilogarithm
$-\mathrm{Li}_2^q(-z_i)$, as the
[quantum dilogarithm evaluation](#conj:topological-mass-dilogarithm) conjectures,
then the bound reads
$\mathfrak{m}(\varrho) \le \lVert \mathrm{Hol}_{\nabla_A}(\varrho_0; \mathfrak{G}) \rVert + \sum_{i=1}^{N} \bigl(-\mathrm{Li}_2^q(-z_i)\bigr)$.  $\square$
