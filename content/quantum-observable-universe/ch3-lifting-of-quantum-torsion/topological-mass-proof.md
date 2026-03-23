
The proof proceeds in four steps: decomposition of the mass integral
using the descent involution, identification of the descended term with
holonomy, localisation of the transient terms to exceptional divisors,
and evaluation via the quantum dilogarithm.

*Step 1: Eigenspace decomposition of the mass integrand.*
By the ([mass identity](#def:mass-identity)), the mass of
the vortex $\gamma$ is
$$
  m(\gamma)
  \;=\;
  \bigl\lVert\,
  \mathrm{MI}\!\!\int_\Sigma
  \bigl(\nabla_A q,\; L \wedge F^+\bigr)
  \,\bigr\rVert,
$$
where $\Sigma$ is a surface with $\partial\Sigma = \gamma$.  The
integrand $(\nabla_A q,\; L \wedge F^+)$ is a section of the
connection--curvature bundle over $\Sigma$, and as such it is an element
of the section algebra $\Gamma(J^1 E_{n+1},\, \mathrm{SU}_{q_{n+1}}(2))$
at whatever level $n{+}1$ accommodates the vortex.

The descent involution $\tau_n$ ([descent involution](#def:descent-involution))
decomposes this section algebra into the direct sum
$\mathcal{A}_{n+1}^{\mathrm{desc}} \oplus \mathcal{A}_{n+1}^{\mathrm{trans}}$
([descent eigenspaces](#prop:descent-eigenspaces)).  Since $\tau_n$ is an
idempotent $*$-endomorphism, the Killing-form norm
$\lVert\cdot\rVert$ on $\mathfrak{su}(2)$ respects the orthogonal
decomposition:
$$
  \lVert \alpha \rVert^2
  \;=\;
  \lVert \tau_n(\alpha) \rVert^2
  \;+\;
  \lVert \alpha - \tau_n(\alpha) \rVert^2
$$
for every section $\alpha$.  Applying this to the mass integrand and
using the additivity of the nonabelian multiplicative integral over
orthogonal direct sums [Proposition 5.3, yekutieli2015]:

```tex
\begin{equation}\label{eq:mi-decomp}
  \mathrm{MI}\!\!\int_\Sigma \alpha
  \;=\;
  \mathrm{MI}\!\!\int_\Sigma \tau_n(\alpha)
  \;\cdot\;
  \mathrm{MI}\!\!\int_\Sigma
  \bigl(\alpha - \tau_n(\alpha)\bigr),
\end{equation}
```

where the product is in the group $\mathrm{SU}_{q}(2)$.  Taking norms
and using the submultiplicativity of $\lVert\cdot\rVert$ (which is an
equality for the orthogonal decomposition of an idempotent):
$$
  m(\gamma)
  \;=\;
  \bigl\lVert\,
  \mathrm{MI}\!\!\int_\Sigma \tau_n(\alpha)
  \,\bigr\rVert
  \;+\;
  \bigl\lVert\,
  \mathrm{MI}\!\!\int_\Sigma
  \bigl(\alpha - \tau_n(\alpha)\bigr)
  \,\bigr\rVert.
$$

*Step 2: Descended term is the unknot-core holonomy.*
The projection $\tau_n(\alpha)$ lies in
$\mathcal{A}_{n+1}^{\mathrm{desc}} = \mathrm{im}\,\tau_n$, which is
isomorphic to the level-$n$ section algebra via the ascent embedding
$\ell_n$ ([descent involution](#def:descent-involution)).  The surface
$\Sigma$ with $\partial\Sigma = \gamma$ decomposes under the topological
blow-up as $\Sigma = \Sigma_0 \cup \bigcup_{i=1}^N D_i$, where
$\Sigma_0$ is a disc spanning the unknot core $\gamma_0$ and each
$D_i$ is the disc (exceptional divisor) inserted at the $i$-th blow-up.
On $\Sigma_0$ the transient component vanishes
($\alpha - \tau_n(\alpha) = 0$ on the unknot complement, since $\gamma_0$
has trivial topology and all sections there factor through level $n$).
Hence:
$$
  \mathrm{MI}\!\!\int_\Sigma \tau_n(\alpha)
  \;=\;
  \mathrm{MI}\!\!\int_{\Sigma_0} \alpha
  \;=\;
  \mathrm{Hol}_{\nabla_A}\!\bigl(\gamma_0;\, \mathfrak{G}\bigr),
$$
where the second equality is the nonabelian Stokes
theorem [yekutieli2015] applied to the disc $\Sigma_0$.

*Step 3: Transient terms localise to exceptional divisors.*
The transient component $\alpha - \tau_n(\alpha)$ is annihilated by
$\tau_n$: it lies in
$\mathcal{A}_{n+1}^{\mathrm{trans}} = \ker\,\tau_n$
([descent eigenspaces](#prop:descent-eigenspaces)).  By the structure of the
defining boundary ([brane boundary](#def:brane-boundary)), the support of
a transient section is contained in a neighbourhood of the boundary
$\partial E_n$, which has codimension $\geq 2$ in $E_n$ (item (1)) and
whose fibre at each blow-up centre $p_i$ is the exceptional divisor
$E_i \cong \mathbb{P}^1(\mathbb{C})$ (item (2)).

On the surface $\Sigma$, the transient integrand is therefore supported
on the discs $D_i$ centred at the blow-up points.  Since the $D_i$ are
disjoint (each blow-up introduces a new connected component of
$\partial E_n$), the multiplicative integral splits as a product:
$$
  \mathrm{MI}\!\!\int_\Sigma
  \bigl(\alpha - \tau_n(\alpha)\bigr)
  \;=\;
  \prod_{i=1}^{N}\;
  \mathrm{MI}\!\!\int_{D_i}
  \bigl(\nabla_A q,\; L \wedge F^+\bigr).
$$
Since the $D_i$ are geometrically disjoint and the group elements commute
up to the central band $\mathcal{O}_M^{\times}$ of the gerbe
(the transient modes are localised at distinct points, and the central
extension ensures that the group-valued integrals commute modulo the
band), the norm of the product equals the sum of the norms:
$$
  \bigl\lVert\,
  \prod_{i=1}^{N}\;
  \mathrm{MI}\!\!\int_{D_i}
  \bigl(\nabla_A q,\; L \wedge F^+\bigr)
  \,\bigr\rVert
  \;=\;
  \sum_{i=1}^{N}
  \bigl\lVert\,
  \mathrm{MI}\!\!\int_{E_i}
  \bigl(\nabla_A q,\; L \wedge F^+\bigr)
  \,\bigr\rVert,
$$
where we replace $D_i$ by $E_i$ since the integrand is supported on the
exceptional fibre $E_i \subset D_i$.

*Step 4: Quantum dilogarithm evaluation.*
Combining Steps 1--3:
$$
  m(\gamma)
  \;=\;
  \bigl\lVert\,
  \mathrm{Hol}_{\nabla_A}\!\bigl(\gamma_0;\, \mathfrak{G}\bigr)
  \,\bigr\rVert
  \;+\;
  \sum_{i=1}^{N}
  \bigl\lVert\,
  \mathrm{MI}\!\!\int_{E_i}
  \bigl(\nabla_A q,\; L \wedge F^+\bigr)
  \,\bigr\rVert.
$$
This is the claimed decomposition [eq:topological-mass-decomp](#eq:topological-mass-decomp).
The identification of each summand with the quantum dilogarithm
$\Phi_q(z_i)$ follows from the Corollary below: integration of the
$q$-deformed expansion flow over the resolved defect $E_i$ in the
spectral coordinates of the Briggs--Klein chart yields
$\Phi_q(z_i) = \int_0^{z_i} \ln_q(1+t)/t\, dt$.
