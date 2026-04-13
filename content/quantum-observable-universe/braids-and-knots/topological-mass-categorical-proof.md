
*Step 1: Eigenspace decomposition of the mass integrand.*
By the ([mass identity](#def:mass-identity)), the mass of $\varrho$ is

$$
  \mathfrak{m}(\varrho)
  = 
  \bigl\lVert
  \mathrm{tr}\bigl(
    (\int_A \otimes \mathrm{id})
    \circ \Delta
    \circ \varrho
  \bigr)
  \bigr\rVert.
$$

The integrand $\alpha = (\int_A \otimes \mathrm{id}) \circ \Delta \circ \varrho$ is an element of $\mathrm{End}_{\mathbf{C}}(A_{n+1})$.
The descent involution $\hat{\tau}_n$
([descent involution](#def:descent-involution)) decomposes this algebra
into the direct sum
$\mathcal{A}_{n+1}^{\mathrm{desc}} \oplus \mathcal{A}_{n+1}^{\mathrm{trans}}$
([descent eigenspaces](#prop:descent-eigenspaces)):

$$
  \alpha =  \hat{\tau}_n(\alpha) +  (\alpha - \hat{\tau}_n(\alpha)).
$$

When the [Frobenius pairing](#def:frobenius-pairing) is compatible with the $*$-involution
($\langle \alpha^*, \beta \rangle = \overline{\langle \alpha, \beta \rangle}$),
the idempotent decomposition is orthogonal with respect to the
Frobenius norm.  Therefore:

$$
  \lVert \alpha \rVert^2
  = 
  \lVert \hat{\tau}_n(\alpha) \rVert^2
  + 
  \lVert \alpha - \hat{\tau}_n(\alpha) \rVert^2,
$$

and by the linearity of the categorical trace:

$$
  \mathfrak{m}(\varrho)
  = 
  \bigl\lVert
  \mathrm{tr}(\hat{\tau}_n(\alpha))
  \bigr\rVert
  + 
  \bigl\lVert
  \mathrm{tr}(\alpha - \hat{\tau}_n(\alpha))
  \bigr\rVert.
$$

*Step 2: Descended term is the base-level mass.*
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

*Step 3: Transient terms localise to blow-up centres.*
The transient component $\alpha - \hat{\tau}_n(\alpha) \in \mathcal{A}_{n+1}^{\mathrm{trans}} = \ker\hat{\tau}_n$.  By the structure
of the brane boundary ([brane boundary](#def:brane-boundary)), the
support of a transient endomorphism is contained in the union of the
kernels $\ker(\mathfrak{d}_{n+1}|_{p_i})$ at the blow-up centres
$p_1, \ldots, p_N$.  These kernels are mutually disjoint submodules
(each arises from a distinct extension step), so the transient trace
decomposes as a sum:

$$
  \mathrm{tr}(\alpha - \hat{\tau}_n(\alpha))
  = 
  \sum_{i=1}^{N} \mathrm{tr}_{\mathrm{trans}}(\varrho, p_i),
$$

and the norm of the sum equals the sum of the norms (by disjointness
of the supports).

Combining Steps 1--3 gives the claimed decomposition.
