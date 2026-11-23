**Proof.**
One assembles the bound from three lemmas. Put $\alpha = (\int_A \otimes \mathrm{id}) \circ \Delta \circ \varrho$. By ([eigenspace decomposition](#lem:topological-mass-cat-eigenspace)), the :refterm[descent]{#descent} involution splits $\alpha$ as $\hat{\tau}_n(\alpha) + (\alpha - \hat{\tau}_n(\alpha))$. Since the trace is linear, the trace value splits the same way:

$$
  \mathrm{tr}(\alpha)
  =
  \mathrm{tr}(\hat{\tau}_n(\alpha)) +
  \mathrm{tr}(\alpha - \hat{\tau}_n(\alpha)).
$$

By ([descended term equals base mass](#lem:topological-mass-cat-descended)), the first summand is $\mathrm{tr}_{\mathrm{desc}}(\varrho)$, the trace of the base-level cycle $\varrho_0$. By ([transient terms localise to blow-ups](#lem:topological-mass-cat-transient)), the second summand is $\sum_{i=1}^{N} \mathrm{tr}_{\mathrm{trans}}(\varrho, p_i)$. Taking norms, the triangle inequality gives

$$
  \mathfrak{m}(\varrho)
  = \lVert \mathrm{tr}(\alpha) \rVert
  \le
  \bigl\lVert \mathrm{tr}_{\mathrm{desc}}(\varrho) \bigr\rVert +
  \sum_{i=1}^{N} \bigl\lVert \mathrm{tr}_{\mathrm{trans}}(\varrho, p_i) \bigr\rVert .
$$

Orthogonality of the splitting with respect to the Frobenius norm would add squared norms, not norms, so it does not upgrade this bound to the equality of [the topological decomposition of mass](#conj:topological-mass). $\square$
