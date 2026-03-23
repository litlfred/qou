Continuing the [brane tower for SU(2)](#ex:recursive-brane-tower-su2), we
compute the [mass identity](#def:mass-identity) for
$G = \mathrm{SU}(2)$.

**Setup.** Take $A = \mathcal{O}(\mathrm{SU}(2))$ with Frobenius form
$\lambda = \int_{\mathrm{SU}(2)} (-)\, d\mu$, where $\mu$ is the
normalised Haar measure. The comultiplication is
$\Delta(f)(x, y) = f(xy)$, and the categorical trace is
$\operatorname{tr}(\phi) = (\lambda \otimes \mathrm{id}) \circ \Delta \circ \phi$.

**The mass formula.** For a cycle $\gamma \in A$, the
[mass identity](#def:mass-identity) gives
$$
  m(\gamma)
  \;=\; \bigl\lVert \operatorname{tr}\bigl((\lambda \otimes \mathrm{id})
  \circ \Delta \circ \gamma\bigr) \bigr\rVert.
$$
Since $\Delta(f)(x, y) = f(xy)$, the inner composition evaluates to
$(\lambda \otimes \mathrm{id})(\Delta(\gamma)) = \int_{\mathrm{SU}(2)} \gamma(xy)\, d\mu(x)$,
which is the convolution of $\gamma$ with the Haar measure.

**Fundamental representation.** For the spin-$\tfrac{1}{2}$
representation $V_{1/2}$, a cycle $\gamma$ encircling a vortex in
$\mathbb{CP}^1 \cong \mathrm{SU}(2)/\mathrm{U}(1)$ has mass
$$
  m(\gamma)
  \;=\; \biggl\lVert \int_{\mathrm{SU}(2)}
  \operatorname{tr}_{V_{1/2}}\!\bigl(\Delta(\gamma)\bigr)\, d\mu
  \biggr\rVert.
$$
The comultiplication maps $f(x) \mapsto f(xy)$, so the trace picks out
the character $\chi_{1/2}(g) = 2\cos(\theta/2)$ of the fundamental
representation. Integrating the character against a winding-number-$1$
cycle yields $m(\gamma) = 1$.
