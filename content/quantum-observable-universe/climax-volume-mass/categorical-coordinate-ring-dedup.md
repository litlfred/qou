**Remark ($R[i, q^{\pm 1}]$ as the ambient deformation ring).**

**Downstream applications of $R[i, q^{\pm 1}]$.**  Recognising the
categorical-coordinate ring as the ambient deformation ring
([prop:categorical-coordinate-ring](#prop:categorical-coordinate-ring))
deduplicates four ad-hoc complexification patterns elsewhere in the
paper:

1. *This block.*  The substitution $q = e^{i\varTheta}$ used in the
   [commutative-limit remark](#rem:commutative-crossing-energy) is no
   longer an external complexification.  $e^{i\varTheta} = \cos\varTheta + i\sin\varTheta$
   is a unit *in* $R[i]$ via the Euler identity, so $q - q^{-1} = 2i\sin\varTheta$
   is computed entirely inside $R[i, q^{\pm 1}]$ — no enlargement of
   the categorical ground ring is invoked.

2. *Witness computations.*  The complex arithmetic in
   `isospin-mass-tower-collapse` and the broader mass-tower
   pipeline is justified categorically as a single specialisation
   $R[i, q^{\pm 1}] \to \mathbb{C}$ via $q \mapsto q_0$, applying the
   universal property of the categorical-coordinate ring once rather
   than complexifying ad hoc per script.

3. *Wick-rotation and complex-substrate remarks.*  The blocks
   [rem:laplace-fourier-wick-rotation](#rem:laplace-fourier-wick-rotation)
   and [rem:complex-substrate-interpretation](#rem:complex-substrate-interpretation)
   each currently complexify in isolation (introducing $i$ for the
   half-plane swap, the CR structure, and the substrate value).
   Both invocations of $i$ are now realisations of the single
   categorical coordinate of
   [prop:categorical-coordinate-ring](#prop:categorical-coordinate-ring),
   under the $\mathrm{Gal}(R[i]/R) = \mathbb{Z}_2$ orientation choice
   of [rem:i-as-braiding-orientation](#rem:i-as-braiding-orientation).

4. *Curves over the substrate.*  The hyperelliptic quintic
   $\mathcal{X}_5: y^2 = x^5 - 1$
   ([def:hyperelliptic-quintic](#def:hyperelliptic-quintic)) and the
   Descartes elliptic curve $\mathcal{E}_q$
   ([prop:descartes-elliptic-curve](#prop:descartes-elliptic-curve))
   are normally introduced "over $\mathbb{C}$" with $\zeta_5 = e^{2\pi i/5}$
   as a complex root of unity.  In the categorical-coordinate
   framework these curves live over $R[i, q^{\pm 1}]$ at $q = q_0$;
   the fifth roots of unity $\zeta_5^k$ are the five geometric points
   of $\mathrm{Spec}(R[i, q^{\pm 1}])$ where the chart-transition
   coefficient hits $\zeta_5^k$, recovering the branch-phase
   localisation of [rem:u1-phase-tube](#rem:u1-phase-tube).

In each case the simplification is *categorical justification*, not
algorithmic: computations and proofs do not change, but their
ambient ring becomes a single named object instead of an ad-hoc
complexification.
