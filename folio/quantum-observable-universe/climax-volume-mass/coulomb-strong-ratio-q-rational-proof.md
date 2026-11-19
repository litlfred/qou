The proof proceeds in two steps:

1. **Algebraic identity**: for any real $q \ne 0$,

   $$
     \frac{q - q^{-1}}{q + q^{-1}} = \frac{q^2 - 1}{q^2 + 1},
   $$

   obtained by multiplying numerator and denominator by $q$.

2. **Transcendental bridge**: for any real $q > 0$, substituting $q = \exp(\ln q)$ and $q^{-1} = \exp(-\ln q)$ into the definitions of $\sinh$, $\cosh$, and $\tanh$ gives

   $$
     \tanh(\ln q) = \frac{q - q^{-1}}{q + q^{-1}}.
   $$

Combining the two steps yields [the Coulomb-strong ratio identity](#prop:coulomb-strong-ratio-q-rational): $\tanh(\ln q) = (q^2-1)/(q^2+1)$ for $q > 0$.

The identity holds over $\mathbb{R}_{>0}$ (the archimedean substrate-anchor regime). The fibre-level $q$-rational form $(q-q^{-1})/(q+q^{-1})$ is a Laurent-polynomial ratio over $\mathbb{Z}[q,q^{-1}]$, realised at $q = q_0 \in \mathbb{R}_{>0}$ where it agrees with the archimedean $\tanh(\ln q_0)$. No $|q| = 1$ step is involved: the identity uses $q^{-1}$ algebraically rather than as complex conjugation, and both $q_0$ and $q_0^{-1}$ are positive real points.
