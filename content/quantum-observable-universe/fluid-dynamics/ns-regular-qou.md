Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe) with [brane tower](#def:recursive-brane-tower) $\{A_n\}_{n \geq 0}$ and [quantum characteristic classes](#def:quantum-characteristic-classes) $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$.

The **NS obstruction** of $(\mathbf{C}, A, \tau)$ is the class

$$
  \mathrm{NS}(A)
  = 
  \kappa_0\big|_\Sigma
   \in 
  H^2(\Sigma, \mathcal{B}),
$$

where $\Sigma$ is the collision locus of a generic vortex pair and $\kappa_0 = e(\xi)$ is the Euler class of the Reeb bundle with $\mathrm{tr}(\kappa_0) = \chi(A)$.

We classify $(\mathbf{C}, A, \tau)$ by the vanishing of this obstruction:

- **NS-regular** if $\mathrm{NS}(A) = 0$. The classical Navier--Stokes equation (the $q = 1$ specialisation of the [q-NS system](#def:q-navier-stokes)) admits smooth global solutions for all smooth initial data.
- **NS-singular** if $\mathrm{NS}(A) \neq 0$. The classical Navier--Stokes equation admits smooth initial data that develop finite-time singularities.

The obstruction $\mathrm{NS}(A)$ depends strictly on the categorical Euler characteristic $\chi(A)$. It does not depend on the substrate section $q$ or on initial data.

| $\chi(A)$ | $\mathrm{NS}(A)$ | Status |
|---|---|---|
| $\neq 0$ | $\neq 0$ (Kummer non-divisibility) | **NS-singular** |
| $= 0$ | $= 0$ | **NS-regular** |

The observability axiom $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ provides a sufficient condition for $\chi(A) \neq 0$. It forces irreducibility of the adjoint representation, ensuring a nonzero Euler class. We treat it as a diagnostic rather than an assumption here.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs (real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$). Generic categorical identities remain valid over an abstract coefficient ring; we specialise only their archimedean realisation.
