The [descent involution](#def:descent-involution) on $\mathrm{End}_{\mathbf{C}}(A_1)$ for $A_1 = J^1\mathcal{O}(\mathrm{SU}(2))$ ([jet prolongation for SU(2)](#ex:jet-prolongation-su2)) is constructed as follows.

**The endomorphism algebra.** The space $A_1 \cong \mathcal{O}(\mathrm{SU}(2)) \otimes \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$. The endomorphism algebra $\mathrm{End}_{\mathbf{C}}(A_1)$ has $6$ dimensions: $3$ from the base $\mathrm{SU}(2)$ and $3$ from the cotangent fibre.

**Definition.** The descent involution $\hat{\tau}_1$ on $\mathrm{End}_{\mathbf{C}}(A_1)$ is the composition $\hat{\tau}_1 = \ell \circ \mathfrak{d}$. The map $\mathfrak{d}$ is descent, averaging over $\mathrm{U}(1)$-orbits in the Hopf fibration $\mathrm{SU}(2) \to \mathbb{CP}^1$. The map $\ell$ is ascent, the jet prolongation of the descended endomorphism.

**Idempotence.** Descent averages the $\mathrm{U}(1)$ action. Ascent embeds the result, yielding $\hat{\tau}_1^2 = \hat{\tau}_1$. For $\phi \in \mathrm{End}_{\mathbf{C}}(A_1)$:
$$
  \hat{\tau}_1(\phi)(f \otimes \omega_a) = \frac{1}{2\pi} \int_0^{2\pi} \phi\bigl(e^{i\varTheta} \cdot (f \otimes \omega_a)\bigr) d\varTheta,
$$
where $e^{i\varTheta}$ acts via the maximal torus $\mathrm{U}(1) \hookrightarrow \mathrm{SU}(2)$. The fixed-point set $\mathrm{End}_{\mathbf{C}}(A_1)^{\hat{\tau}_1}$ contains exactly the $\mathrm{U}(1)$-equivariant endomorphisms.
