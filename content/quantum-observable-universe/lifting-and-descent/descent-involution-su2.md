Continuing the [jet prolongation for SU(2)](#ex:jet-prolongation-su2),
we construct the [:refterm[descent]{#descent} involution](#def:descent-involution) on
$\mathrm{End}_{\mathbf{C}}(A_1)$ where
$A_1 = J^1\mathcal{O}(\mathrm{SU}(2))$.

**The endomorphism algebra.** Since
$A_1 \cong \mathcal{O}(\mathrm{SU}(2)) \otimes \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$,
the endomorphism algebra $\mathrm{End}_{\mathbf{C}}(A_1)$ is
$6$-dimensional: $3$ dimensions from the base $\mathrm{SU}(2)$
directions and $3$ from the cotangent fibre directions.

**Definition.** The :refterm[descent]{#descent} involution $\hat{\tau}_1$ on
$\mathrm{End}_{\mathbf{C}}(A_1)$ is the composition
$\hat{\tau} = \ell \circ \mathfrak{d}$, where $\mathfrak{d}$ is the :refterm[descent]{#descent}
map (averaging over $\mathrm{U}(1)$-orbits in the Hopf fibration
$\mathrm{SU}(2) \to \mathbb{CP}^1$) and $\ell$ is the ascent
(jet prolongation of the descended endomorphism).

**Idempotence.** Since :refterm[descent]{#descent} is averaging over the $\mathrm{U}(1)$
action and ascent re-embeds the result, we have $\hat{\tau}^2 = \hat{\tau}$. That
is, $\hat{\tau}$ is a projection, not only an involution of order $2$.
Explicitly, for $\phi \in \mathrm{End}_{\mathbf{C}}(A_1)$,

$$
  \hat{\tau}(\phi)(f \otimes \omega_a)
  =  \frac{1}{2\pi} \int_0^{2\pi}
  \phi\bigl(e^{i\varTheta} \cdot (f \otimes \omega_a)\bigr) d\varTheta,
$$

where $e^{i\varTheta}$ acts via the $\mathrm{U}(1) \hookrightarrow \mathrm{SU}(2)$
maximal torus. The fixed-point set $\mathrm{End}_{\mathbf{C}}(A_1)^{\hat{\tau}}$
consists of the $\mathrm{U}(1)$-equivariant endomorphisms.
