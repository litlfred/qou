## Proof

1. **The pre-$\tau$ object.** By definition
   $\mathrm{Vol}_q(\beta) = \mathrm{tr}_M(\beta)$. The
   [cleared mass trace](#prop:full-pole-structure-mass-trace) writes it as a
   polynomial in $z = q^{3}/(q^{2}+1)$ with coefficients in $\mathbb{Z}[h]$,
   $h = q - q^{-1}$. Since $z$ and $h$ lie in
   $\mathbb{Z}[q^{\pm 1}][(q^{2}+1)^{-1}]$, so does $\mathrm{Vol}_q(\beta)$.
   No absolute value, logarithm or limit is used at this stage.
2. **The specialisation.** $\tau_{\mathrm{arch}}$ evaluates this element at
   $q = q_0$, which is defined because $q_0^{2} + 1 \neq 0$. Only then are the
   archimedean operations applied: the absolute value and, since $\mathrm{Vol}_{q_0}(\beta)\neq0$ by hypothesis, the logarithm give
   $\Phi_1(\beta) = \ln\lvert\mathrm{Vol}_{q_0}(\beta)\rvert$, and dividing by
   $\hbar_{q_0}^{2}$ gives $\mathfrak{m}_{\mathrm{alg}}(\beta)$.

This proves the displayed identity, which is a definition of
$\mathfrak{m}_{\mathrm{alg}}$ together with the claim that its only pre-$\tau$
input is algebraic. The tower terms $\Phi_q(|\hat V_i|)$ of the
[unified knot mass formula](#thm:knot-mass-formula-unified) are not used: they
contain an absolute value and are themselves archimedean.

The identification of $\Phi_1(\beta)$ with the hyperbolic volume
$\mathrm{Vol}(K)$ is not proved here. It is conditional on the volume
conjecture and is recorded separately in
[topological-mass-formula proposition](#prop:topological-mass-formula).
$\square$
