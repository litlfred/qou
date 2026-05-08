**Proof.**
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

$\square$
