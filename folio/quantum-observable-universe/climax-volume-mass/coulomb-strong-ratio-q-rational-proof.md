## Proof

The proof has two steps:

1. **Algebraic identity**: for any real
   $q \ne 0$,

   $$
     \frac{q - q^{-1}}{q + q^{-1}} = \frac{q^2 - 1}{q^2 + 1}.
   $$

   Clearing denominators reduces it to a polynomial identity.

2. **Transcendental bridge**: for any real
   $q > 0$,

   $$
     \tanh(\ln q) = \frac{q - q^{-1}}{q + q^{-1}}.
   $$

   Follows from $e^{\ln q} = q$ and the definitions of $\sinh$, $\cosh$,
   $\tanh$.

The composite ([Coulomb/strong ratio $\tanh(\ln q)$ is the q-rational $(q^2-1)/(q^2+1)$](#prop:coulomb-strong-ratio-q-rational)) is the immediate
corollary: $\tanh(\ln q) = (q^2-1)/(q^2+1)$ for $q > 0$.

## q-usage discipline

The identity is stated and proved over $\mathbb{R}_{>0}$ (the archimedean
substrate-anchor regime). The fibre-level q-rational form
$(q-q^{-1})/(q+q^{-1})$ is a Laurent-polynomial ratio over $\mathbb{Z}[q,q^{-1}]$,
realised at $q = q_0 \in \mathbb{R}_{>0}$ where it agrees with the
archimedean $\tanh(\ln q_0)$. There is no $|q| = 1$ step (the identity
involves $q^{-1}$ algebraically, not as conjugation; both $q_0$ and $q_0^{-1}$
are real positive points). Compliant with the requirement that $q_0$ have
vanishing imaginary part.
