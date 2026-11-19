**Proof.**
The decomposition is assembled from three lemmas.  By
([eigenspace decomposition](#lem:topological-mass-cat-eigenspace)),
the :refterm[descent]{#descent} involution gives an orthogonal Frobenius-norm split

$$
  \mathfrak{m}(\varrho)
  =
  \bigl\lVert \mathrm{tr}(\hat{\tau}_n(\alpha)) \bigr\rVert
  +
  \bigl\lVert \mathrm{tr}(\alpha - \hat{\tau}_n(\alpha)) \bigr\rVert,
$$

where $\alpha = (\int_A \otimes \mathrm{id}) \circ \Delta \circ \varrho$.
By ([descended term equals base mass](#lem:topological-mass-cat-descended)),
the first summand is $\mathfrak{m}(\varrho_0)$.  By
([transient terms localise to blow-ups](#lem:topological-mass-cat-transient)),
the second summand decomposes as $\sum_{i=1}^{N} \mathrm{tr}_{\mathrm{trans}}(\varrho, p_i)$.
Combining yields the claimed decomposition.  $\square$
