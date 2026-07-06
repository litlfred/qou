**Remark ($R[i, q^{\pm 1}]$ as the ambient deformation ring).**

Recognising the categorical-coordinate ring as the ambient deformation ring ([prop:categorical-coordinate-ring](#prop:categorical-coordinate-ring)) consolidates four ad hoc complexifications into a single structure:

1. **Internal substitution.** The commutative limit ([rem:commutative-crossing-energy](#rem:commutative-crossing-energy)) sets $q = e^{i\varTheta}$. The Euler identity makes $e^{i\varTheta}$ a unit in $R[i]$. Thus $q - q^{-1} = 2i\sin\varTheta$ evaluates entirely within $R[i, q^{\pm 1}]$, without artificially enlarging the categorical ground ring.

2. **Witness computations.** The complex arithmetic in `isospin-mass-tower-collapse` and the mass-tower pipeline reduces to a single specialisation $R[i, q^{\pm 1}] \to \mathbb{C}$ via $q \mapsto q_0$. This applies the universal property of the categorical-coordinate ring globally.

3. **Wick rotation and complex substrates.** Instead of introducing isolated complex structures for the half-plane swap ([rem:laplace-fourier-wick-rotation](#rem:laplace-fourier-wick-rotation)) and substrate values ([rem:complex-substrate-interpretation](#rem:complex-substrate-interpretation)), both instances of $i$ manifest as the categorical coordinate of [prop:categorical-coordinate-ring](#prop:categorical-coordinate-ring), governed by the $\mathrm{Gal}(R[i]/R) = \mathbb{Z}_2$ orientation choice ([rem:i-as-braiding-orientation](#rem:i-as-braiding-orientation)).

4. **Curves over the substrate.** The hyperelliptic quintic $\mathcal{X}_5: y^2 = x^5 - 1$ ([def:hyperelliptic-quintic](#def:hyperelliptic-quintic)) and the Descartes elliptic curve $\mathcal{E}_q$ ([prop:descartes-elliptic-curve](#prop:descartes-elliptic-curve)) traditionally live over $\mathbb{C}$. Here, they live over $R[i, q^{\pm 1}]$ at $q = q_0$. The roots $\zeta_5^k$ denote the five geometric points of $\mathrm{Spec}(R[i, q^{\pm 1}])$ where the chart-transition coefficient matches $\zeta_5^k$, recovering the branch-phase localisation ([rem:u1-phase-tube](#rem:u1-phase-tube)).

This simplification is purely structural. The algorithms and proofs remain unchanged, but their ambient ring is rigorously unified.
