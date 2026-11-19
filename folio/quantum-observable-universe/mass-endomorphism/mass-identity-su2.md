Continuing the [brane tower for SU(2)](#ex:recursive-brane-tower-su2), the [mass identity](#def:mass-identity) is evaluated for $G = \mathrm{SU}(2)$.

**Setup.** Let $A = \mathcal{O}(\mathrm{SU}(2))$ with Frobenius form $\int_A = \int_{\mathrm{SU}(2)} (-) d\mu$, where $\mu$ is the normalised Haar measure. The comultiplication is $\Delta(f)(x, y) = f(xy)$. The categorical trace is $\mathrm{tr}(\phi) = (\int_A \otimes \mathrm{id}) \circ \Delta \circ \phi$.

**The mass formula.** For a cycle $\varrho \in A$, the [mass identity](#def:mass-identity) gives:

$$
  \mathfrak{m}(\varrho)
  =  \bigl\lVert \mathrm{tr}\bigl((\int_A \otimes \mathrm{id})
  \circ \Delta \circ \varrho\bigr) \bigr\rVert.
$$

Since $\Delta(f)(x, y) = f(xy)$, the inner composition evaluates to $(\int_A \otimes \mathrm{id})(\Delta(\varrho)) = \int_{\mathrm{SU}(2)} \varrho(xy) d\mu(x)$. This forms the convolution of $\varrho$ with the Haar measure.

**Fundamental representation.** For the spin-$\tfrac{1}{2}$ representation $V_{1/2}$, a cycle $\varrho$ encircling a vortex in $\mathbb{CP}^1 \cong \mathrm{SU}(2)/\mathrm{U}(1)$ has mass:

$$
  \mathfrak{m}(\varrho)
  =  \biggl\lVert \int_{\mathrm{SU}(2)}
  \mathrm{tr}_{V_{1/2}}\!\bigl(\Delta(\varrho)\bigr) d\mu
  \biggr\rVert.
$$

The comultiplication maps $f(x) \mapsto f(xy)$, so the trace extracts the character $\chi_{1/2}(g) = 2\cos(\varTheta/2)$ of the fundamental representation. Integrating this character against a winding-number-$1$ cycle yields $\mathfrak{m}(\varrho) = 1$.
