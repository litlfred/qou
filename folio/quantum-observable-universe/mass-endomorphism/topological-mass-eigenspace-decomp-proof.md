**Proof.**
By the ([mass identity](#def:mass-identity)), the mass of
the vortex $\varrho$ is

$$
  \mathfrak{m}(\varrho)
  = 
  \bigl\lVert
  \mathrm{MI}\!\!\int_\Sigma
  \bigl(\nabla_A q, L \wedge F^+\bigr)
  \bigr\rVert,
$$

where $\Sigma$ is a surface with $\partial\Sigma = \varrho$.  The
integrand $(\nabla_A q, L \wedge F^+)$ is a section of the
connection--curvature bundle over $\Sigma$, and as such it is an element
of the section algebra $\Gamma(J^1 \mathcal{S}_{n+1}, \mathrm{SU}_{q_{n+1}}(2))$
at whatever level $n{+}1$ accommodates the vortex.

The :refterm[descent]{#descent} involution $\hat{\tau}_n$ ([:refterm[descent]{#descent} involution](#def:descent-involution))
decomposes this section algebra into the direct sum
$\mathcal{A}_{n+1}^{\mathrm{desc}} \oplus \mathcal{A}_{n+1}^{\mathrm{trans}}$
([:refterm[descent]{#descent} eigenspaces](#prop:descent-eigenspaces)).  Since $\hat{\tau}_n$ is an
idempotent $*$-endomorphism, the Killing-form norm
$\lVert\cdot\rVert$ on $\mathfrak{su}(2)$ respects the orthogonal
decomposition:

$$
  \lVert \alpha \rVert^2
  = 
  \lVert \hat{\tau}_n(\alpha) \rVert^2 +
  \lVert \alpha - \hat{\tau}_n(\alpha) \rVert^2
$$

for every section $\alpha$.  Applying this to the mass integrand and
using the additivity of the nonabelian multiplicative integral over
orthogonal direct sums:

```tex
\begin{equation}\label{eq:mi-decomp}
  \mathrm{MI}\!\!\int_\Sigma \alpha
  = 
  \mathrm{MI}\!\!\int_\Sigma \hat{\tau}_n(\alpha)
   \cdot 
  \mathrm{MI}\!\!\int_\Sigma
  \bigl(\alpha - \hat{\tau}_n(\alpha)\bigr),
\end{equation}
```

where the product is in the group $\mathrm{SU}_{q}(2)$.  Taking norms,
the triangle inequality for the norm on $\mathrm{SU}_{q}(2)$ gives

$$
  \mathfrak{m}(\varrho)
  \le
  \bigl\lVert
  \mathrm{MI}\!\!\int_\Sigma \hat{\tau}_n(\alpha)
  \bigr\rVert +
  \bigl\lVert
  \mathrm{MI}\!\!\int_\Sigma
  \bigl(\alpha - \hat{\tau}_n(\alpha)\bigr)
  \bigr\rVert.
$$

The orthogonality above gives additivity of squared norms only. It does not
make this inequality an equality: for two non-zero orthogonal vectors the
triangle inequality is strict.  $\square$
