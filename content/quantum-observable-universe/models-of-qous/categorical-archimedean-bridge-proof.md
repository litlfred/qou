
We compute the image of the categorical differential $d_q$ under the
fibre functor $\tau$, showing that $\tau(d_q)$ equals the archimedean
$q$-exterior derivative. The functor $\tau$ maps:

- the Frobenius form $\int_A$ to the contact integral
  $\int_M \alpha \wedge (d\varTheta)^n$,
- the maximal torus generator $\xi$ to the Reeb vector field
  satisfying $\iota_\xi\varTheta = 1$ and $\iota_\xi d\varTheta = 0$,
- the weight decomposition $\pi_H, \pi_V$ to the splitting
  $\Omega^k(M) = \Omega^k_H(M) \oplus \varTheta \wedge \Omega^{k-1}_H(M)$ induced by the Reeb direction.

For a form $\alpha \in \Omega^k(M)$, the vertical projection
$\pi_V(d\alpha)$ extracts the component of $d\alpha$ carrying
non-zero weight under the $T$-action. In the geometric
realisation, the $T$-action is the Reeb flow
$\phi_t \colon M \to M$, whose infinitesimal generator is
$\mathcal{L}_\xi$. The non-zero-weight part of $d\alpha$ is
precisely the component along the Reeb direction:

$$
  \pi_V(d\alpha) = \varTheta \wedge \iota_\xi(d\alpha)
  = \varTheta \wedge (\mathcal{L}_\xi\alpha - d(\iota_\xi\alpha)).
$$

On horizontal forms ($\iota_\xi\alpha = 0$), this reduces to
$\varTheta \wedge \mathcal{L}_\xi\alpha$. For general forms,
writing $\alpha = \alpha_H + \varTheta \wedge \beta$ and using
$\mathcal{L}_\xi\varTheta = 0$, we obtain
$\pi_V(d\alpha) = \varTheta \wedge \mathcal{L}_\xi\alpha$ in all
cases. Therefore

$$
  \tau(d_q) = q^{-1} d + (1 - q^{-1})\varTheta \wedge
  \mathcal{L}_\xi,
$$

which is precisely the archimedean formula for $d_q$
([archimedean $q$-exterior derivative](#ex:q-ext-deriv)).
