**Proof.**
The projection $\hat{\tau}_n(\alpha)$ lies in
$\mathcal{A}_{n+1}^{\mathrm{desc}} = \mathrm{im}\hat{\tau}_n$, which is
isomorphic to $\mathrm{End}_{\mathbf{C}}(A_n)$ via the ascent embedding
$\ell_n$ ([descent involution](#def:descent-involution)).  The
compatibility of the categorical trace with descent
($\mathrm{tr}_n \circ \mathfrak{d}_{n+1} = \mathrm{tr}_{n+1}$ on
$\mathrm{im}\hat{\tau}_n$) gives:

$$
  \mathrm{tr}(\hat{\tau}_n(\alpha))
  = 
  \mathrm{tr}(\ell_n(\mathfrak{d}_{n+1}(\alpha)))
  = 
  \mathrm{tr}_n(\mathfrak{d}_{n+1}(\alpha))
  = 
  \mathrm{tr}_n(\alpha_0),
$$

where $\alpha_0 = (\int_A \otimes \mathrm{id}) \circ \Delta \circ \varrho_0$ is the mass integrand of the base-level cycle.  Hence
$\lVert \mathrm{tr}(\hat{\tau}_n(\alpha)) \rVert = \mathfrak{m}(\varrho_0)$.
$\square$
