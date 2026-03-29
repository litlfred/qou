Continuing the [descent eigenspaces for SU(2)](#ex:descent-eigenspaces-su2),
we verify the [topological mass theorem](#thm:topological-mass) for
$G = \mathrm{SU}(2)$.

**The decomposition.** By the topological mass theorem, the mass of a
cycle $\varrho$ decomposes according to the eigenspace splitting:
$$
  m(\varrho) \;=\; m_{\mathrm{desc}}(\varrho) + m_{\mathrm{trans}}(\varrho),
$$
where $m_{\mathrm{desc}} = \lVert \operatorname{tr}_{\mathrm{desc}}(\varrho) \rVert$
is the descended (persistent) contribution and
$m_{\mathrm{trans}} = \lVert \operatorname{tr}_{\mathrm{trans}}(\varrho) \rVert$
is the transient contribution.

**Descended mass.** The descended trace $\operatorname{tr}_{\mathrm{desc}}$
factors through the projection $\hat{\tau}$ onto
$\mathfrak{A}^{\mathrm{desc}} \cong \mathfrak{su}(2)$. For the Hopf
fibration $\mathrm{SU}(2) \to \mathbb{CP}^1$, the descended mass of
the fundamental cycle is
$$
  m_{\mathrm{desc}} \;=\; \chi(\mathbb{CP}^1) \;=\; 2,
$$
the Euler characteristic of $\mathbb{CP}^1 \cong S^2$. This is the
topologically protected part: it is invariant under continuous
deformations of the cycle and the metric.

**Transient mass.** The transient trace
$\operatorname{tr}_{\mathrm{trans}}$ captures fluctuations in the
cotangent directions $\mathfrak{A}^{\mathrm{trans}} \cong \Omega^1(\mathbb{CP}^1) \oplus \mathbb{C}$.
For a cycle $\varrho$ that is $\mathrm{U}(1)$-equivariant,
$m_{\mathrm{trans}}(\varrho) = 0$ since the transient eigenspace has
non-zero $\mathrm{U}(1)$-weight. Non-equivariant deformations of
$\varrho$ contribute a non-zero $m_{\mathrm{trans}}$ that measures the
departure from the symmetric configuration.

**Total mass.** For the fundamental cycle of the Hopf fibration,
$m = 2 + 0 = 2$, recovering the Euler characteristic. For a deformed
cycle, $m = 2 + m_{\mathrm{trans}}$, with the correction depending on
the $L^2$-norm of the cotangent component.
