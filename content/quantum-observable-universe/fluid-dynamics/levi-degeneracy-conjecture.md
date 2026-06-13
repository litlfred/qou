Let $\{q_\kappa = e^{i\pi/\kappa}\}_{\kappa \geq 2}$ be the
sequence of roots of unity converging to $q = 1$. For each
$\kappa$, let $v_\kappa$ be the q-NS solution for anti-parallel
vortex pair initial data, and let

$$
  \mathcal{C}_L(\kappa)
  = 
  \sup_{0 \leq t < T^*_\kappa}
  \mathrm{cond}\bigl(
    \mathcal{L}_\varTheta\big|_{N_p\gamma(t)}
  \bigr)
$$

be the maximum [Levi form condition
number](#prop:core-levi-form) over the evolution.

By the [root-of-unity truncation](#prop:root-of-unity-truncation),
$\mathcal{C}_L(\kappa) \leq 1 + C(\kappa - 1)$ for a universal
constant $C > 0$ (Bernstein inequality on trigonometric
polynomials of degree $\leq (\kappa-1)/2$).

**Conjecture (Levi degeneracy).**
Exactly one of the following holds:

**(A) Sub-linear growth (NS blows up).**

$$
  \mathcal{C}_L(\kappa) = O(1)
  \quad\text{as } \kappa \to \infty.
$$

The condition number stays bounded. The Levi form remains
non-degenerate at the collision locus $\Sigma$ in the
$q \to 1$ limit. The contact structure does not degenerate.
The [observability axiom](#def:quantum-observable-universe)
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ holds locally
on $\Sigma$. The [vorticity lower
bound](#prop:vorticity-lower-bound) holds, the
[q-BKM criterion](#thm:q-bkm) diverges, and the
[counter-example](#conj:ns-counterexample) is established.
Classical 3d Navier--Stokes admits finite-time blowup.

**(B) Linear growth (NS is regular).**

$$
  \mathcal{C}_L(\kappa) \sim \kappa
  \quad\text{as } \kappa \to \infty.
$$

The condition number grows at the same rate as the truncation
level relaxes. The Levi form degenerates in the $\parallel$
direction: $\lambda_\parallel \to 0$ while $\lambda_\perp$
stays bounded. The contact structure becomes partially
integrable at $\Sigma$. The observability axiom fails locally
— a gauge mode acts as the identity in the integrable direction.
The vortex core flattens into a sheet, the vorticity spreads,
and the lower bound fails. Classical 3d Navier--Stokes is
globally regular.

**Equivalent formulations.**

1. **Contact geometry:** Does the
 [Levi form](#def:levi-form-defect) $\mathcal{L}_\varTheta$
 degenerate at the collision locus when $q \to 1$?

2. **Representation theory:** Does the finite-dimensional
 approximation of $\mathrm{SU}_q(2)$ at roots of unity
 preserve the isotropy of the Frobenius inner product in
 the $\kappa \to \infty$ limit?

3. **Observability:** Does the QOU observability axiom
 $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ hold
 locally on the collision locus at $q = 1$?

4. **Integrability:** Does the horizontal distribution
 $\ker(\varTheta)$ remain maximally non-integrable at the
 collision point, or does a 2-dimensional integral
 submanifold form?

5. **Fluid dynamics:** Do colliding anti-parallel vortex
 filaments maintain tubular cores ($\kappa = O(1)$), or
 flatten into sheets ($\kappa \to \infty$)?
