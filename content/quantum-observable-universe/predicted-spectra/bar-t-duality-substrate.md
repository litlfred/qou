*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
The bar involution $\iota \colon q \mapsto q^{-1}$ on the substrate
parameter line lifts to a **substrate-level T-duality** between
elliptic curves of the Descartes family
([Descartes elliptic curve](#prop:descartes-elliptic-curve)):

$$
  \iota_*\,\mathcal{E}_q  =  \mathcal{E}_{q^{-1}},
$$

where $\iota_*$ is the pull-back of $\iota$ along the substrate
parametrization $q \mapsto \mathcal{E}_q$.  Under $\iota_*$:

1. **Discriminant locus:** $\Delta(\mathcal{E}_q) = 0$ at
   $q = 1/\varphi^2$ pairs with $\Delta(\mathcal{E}_{1/q}) = 0$ at
   $q = \varphi^2$ ([skew-dual golden node](#prop:golden-skew-dual-node)).
2. **$j$-invariant:** $j(\mathcal{E}_q)$ and $j(\mathcal{E}_{1/q})$
   are related by the rational involution $j \mapsto j^*$ induced by
   $q \mapsto q^{-1}$ on the Weierstrass coefficients.
3. **Confinement band:** $\mathcal{E}_q$ is non-degenerate iff
   $q \in \mathcal{B}$ ([bar-self-dual band](#prop:bar-self-dual-confinement-band)),
   and the band is fixed setwise by $\iota$.

This is **distinct from** the existing target-space T-duality
([self-duality of $\mathcal{E}_z$](#rem:t-duality-elliptic)),
which exchanges $X \leftrightarrow z$ on a single curve.  Bar
T-duality acts on the **moduli parameter** $q$, not on the curve's
own coordinates.  The two dualities commute and together generate
a $\mathbb{Z}/2 \times \mathbb{Z}/2$-action on the moduli stack of
Descartes-family curves.
