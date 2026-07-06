**Conjecture (First substrate correction to the Casimir force is carried by $4_1$).**

*Assume the plate-constrained mode-count of [`conj:casimir-epsilon-vacuum`](#conj:casimir-epsilon-vacuum). Its leading $1/d^{4}$ term is built from disjoint free-photon modes (the bare photon being the identity $\mathbf{1}$, which is $q$-independent), and is therefore independent of the substrate deformation. The first contribution carrying substrate-$q$ dependence arises from the interacting sector—vacuum modes whose braid words have degree $\geq 2$ and whose closures are hyperbolic. The minimal carrier for this correction is the figure-eight knot $4_1$, entering with relative weight equal to its Markov trace:*

$$
J_{4_1}(q) \;=\; q^{-2} - q^{-1} + 1 - q + q^{2}
\;=\; 1 \;+\; \tfrac{3}{4}\,h^{2} \;+\; O(h^{4}),
\qquad h = q - q^{-1}.
$$

### Absence of $q$ in the Leading Term

The leading parallel-plate term assembles from free photon modes. Each mode is the identity braid, whose Markov closure is a disjoint union of unknots. Degree-$\leq 1$ closures are non-hyperbolic and have vanishing volume ([`lem:degree-one-braid-trivial-volume`](#lem:degree-one-braid-trivial-volume)). A non-braiding mode transmits no substrate deformation. Consequently, the $\zeta(-3)$ prefactor $\pi^{2}/720$ of the parent conjecture is exactly undeformed. Substrate corrections only appear where modes braid (the interacting sector).

### Torus Closures Contribute Nothing

Degree $\geq 2$ is necessary for hyperbolicity, but not sufficient. The minimal degree-$\geq 2$ closures—the Hopf link ($\sigma_1^{2}$), the trefoil $3_1$ ($\sigma_1^{3}$), and the $(2,5)$-torus knot $5_1$ ($\sigma_1^{5}$)—are torus links with $\mathrm{Vol} = 0$. They carry no substrate weight. The first hyperbolic closure is the figure-eight knot $4_1$ ($\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$). It is the unique minimal-volume hyperbolic knot, with $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) \approx 2.0299$.

### The Exact $3/4$ Algebra

Setting $h = q - q^{-1}$, the figure-eight weight satisfies an exact field identity:

$$
J_{4_1}(q) \;=\; 1 + \tfrac{3}{4}\,h^{2}
\;+\; \frac{h^{4}}{4\left(h^{2} + 8 + 4(q + q^{-1})\right)}.
$$

The remainder denominator is strictly positive for $q > 0$. The identity forces the coefficient $3/4$; there is no fitted constant. This expansion is proven sorry-free in `FigureEightCasimirWeight.lean` (`jones41_taylor`, `jones41_three_quarters_cleared`, `jones41_remainder_denom_pos`). At the substrate anchor, the relative weight $\tfrac{3}{4}h^{2}$ evaluates to $\approx 3\%$.

### Self-Consistency with the Substrate

The carrier $4_1$ is not arbitrary. The substrate parameter $q_0$ itself is fixed through $\mathrm{Vol}(4_1)$ via the $m_p/m_e$ mass ratio. The knot defining the framework's single calibrated deformation parameter is exactly the carrier of the vacuum's first substrate correction. This ensures the correction introduces no independent scale.

### Open Conjecture

Two elements remain open. Both require the interacting-mode mode-sum (the Yekutieli-homotopy lift of the parent conjecture's mode-count restricted to degree-$\geq 2$ closures):

1. **The power of $1/d$.** The radiative-correction analogy suggests $1/d^{6}$. This is a structural expectation, not a derivation.
2. **The absolute magnitude.** The relative weight $1 + \tfrac{3}{4}h^{2}$ multiplies an interacting-sector amplitude suppressed by $\sim \alpha\,\lambda_C/d$. This falls far below the precision of current Casimir-force measurements. The conjecture provides a structural prediction target rather than a near-term experimental discriminator.

### Falsification Path

Extract the sector coefficients from the interacting-mode mode-sum. If the first non-vanishing substrate correction is not weighted by $J_{4_1}$, the conjecture is refuted. This happens if a torus-sector contribution survives with nonzero weight, or if a different hyperbolic closure dominates.

### See also

- [`conj:casimir-epsilon-vacuum`](#conj:casimir-epsilon-vacuum): Parent conjecture for the leading $1/d^{4}$ term and the $\varepsilon$-vacuum mechanism.
- [`lem:degree-one-braid-trivial-volume`](#lem:degree-one-braid-trivial-volume): Degree-$\leq 1$ closures carry no volume, thus no substrate weight.
- [`conj:vacuum-epsilon`](#conj:vacuum-epsilon): The $\varepsilon$-relaxed vacuum axiom upstream of both Casimir blocks.
