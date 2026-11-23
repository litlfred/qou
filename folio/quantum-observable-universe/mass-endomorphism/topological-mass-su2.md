Continuing the [:refterm[descent]{#descent} eigenspaces for SU(2)](#ex:descent-eigenspaces-su2),
one verifies the [topological mass conjecture](#conj:topological-mass) for
$G = \mathrm{SU}(2)$.

**The decomposition.** By the topological mass theorem, the mass of a
cycle $\varrho$ decomposes according to the eigenspace splitting:

$$
  \mathfrak{m}(\varrho) =  \mathfrak{m}_{\mathrm{desc}}(\varrho) + \mathfrak{m}_{\mathrm{trans}}(\varrho),
$$

where $\mathfrak{m}_{\mathrm{desc}} = \lVert \mathrm{tr}_{\mathrm{desc}}(\varrho) \rVert$
gives the descended (persistent) contribution and
$\mathfrak{m}_{\mathrm{trans}} = \lVert \mathrm{tr}_{\mathrm{trans}}(\varrho) \rVert$
gives the transient contribution.

**Descended mass.** The descended trace $\mathrm{tr}_{\mathrm{desc}}$
factors through the projection $\hat{\tau}$ onto
$\mathfrak{A}^{\mathrm{desc}} \cong \mathfrak{su}(2)$. For the Hopf
fibration $\mathrm{SU}(2) \to \mathbb{CP}^1$, the descended mass of
the fundamental cycle evaluates to:

$$
  \mathfrak{m}_{\mathrm{desc}} =  \chi(\mathbb{CP}^1) =  2,
$$

which is the Euler characteristic of $\mathbb{CP}^1 \cong S^2$. This provides the
topologically protected part. It remains invariant under continuous
deformations of the cycle and the metric.

**Transient mass.** The transient trace
$\mathrm{tr}_{\mathrm{trans}}$ captures fluctuations in the
cotangent directions $\mathfrak{A}^{\mathrm{trans}} \cong \Omega^1(\mathbb{CP}^1) \oplus \mathbb{C}$.
For a cycle $\varrho$ that is $\mathrm{U}(1)$-equivariant,
$\mathfrak{m}_{\mathrm{trans}}(\varrho) = 0$ since the transient eigenspace has
non-zero $\mathrm{U}(1)$-weight. Non-equivariant deformations of
$\varrho$ contribute a non-zero $\mathfrak{m}_{\mathrm{trans}}$ that measures the
departure from the symmetric configuration.

**Total mass.** For the fundamental cycle of the Hopf fibration,
$m = 2 + 0 = 2$, recovering the Euler characteristic. For a deformed
cycle, $m = 2 + \mathfrak{m}_{\mathrm{trans}}$, with the correction depending on
the $L^2$-norm of the cotangent component.
