**Proposition (conditional on
[`conj:q-aubin-lions`](#conj:q-aubin-lions),
[`conj:ns-counterexample`](#conj:ns-counterexample),
[`conj:critical-exponent`](#conj:critical-exponent),
[`prop:blowup-yekutieli`](#prop:blowup-yekutieli),
and
[`conj:regularity-breakdown`](#conj:regularity-breakdown);
"Core Levi form").**

Let $\varrho$ be a [geodesic vortex](#rem:geodesic-vortices) in
the [state bundle](#ex:c-quantum-observable-universe) $(\mathcal{S}, \varTheta)$
with contact form $\varTheta$ and
[Levi form](#def:levi-form-defect)
$\mathcal{L}_\varTheta(V, W) = -id\varTheta(V, \bar{W})$.  At each
point $p \in \varrho$, let $N_p\varrho \subset \ker(\varTheta_p)$ be
the horizontal normal plane.  Define:

- $\lambda_\parallel(p)$, $\lambda_\perp(p)$: eigenvalues of
  $\mathcal{L}_\varTheta|_{N_p\varrho}$ (the Levi form restricted to
  the normal plane), with $\lambda_\parallel$ in the direction
  toward a second filament and $\lambda_\perp$ perpendicular to it.

- $a_\parallel(p)$, $a_\perp(p)$: core radii of the vortex
  cross-section in the corresponding directions, defined as the
  widths at half-maximum of $|\psi|^2$ in $N_p\varrho$.

Then:

**(a)** The core aspect ratio is controlled by the Levi
eigenvalue ratio:

$$
  \frac{a_\perp(p)}{a_\parallel(p)}
  = 
  \sqrt{\frac{\lambda_\parallel(p)}{\lambda_\perp(p)}}
   \cdot 
  \bigl(1 + O(\hbar_q^2)\bigr).
$$

**(b)** The Levi form condition number on $N_p\varrho$ is

$$
  \mathrm{cond}(\mathcal{L}_\varTheta|_{N_p})
  \equiv
  \frac{\max(\lambda_\parallel, \lambda_\perp)}
       {\min(\lambda_\parallel, \lambda_\perp)}
  = 
  \max\!\left(
    \frac{a_\perp}{a_\parallel},
    \frac{a_\parallel}{a_\perp}
  \right)^2
  \cdot
  \bigl(1 + O(\hbar_q^2)\bigr).
$$

**(c)** The following are equivalent:

1. The core aspect ratio is bounded:
   $\sup_{t < T^*} a_\perp(t) / a_\parallel(t) \leq C$.

2. The Levi form condition number is bounded:
   $\sup_{t < T^*} \mathrm{cond}(\mathcal{L}_\varTheta|_{N_p}) \leq C^2$.

3. The contact structure $\ker(\varTheta)$ remains
   **non-degenerate** at the collision locus $\Sigma$: both
   eigenvalues $\lambda_\parallel, \lambda_\perp > 0$ on $\Sigma$.

4. The [observability axiom](#def:quantum-observable-universe)
   $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
   holds locally at every $p \in \Sigma$.

5. No 2-dimensional integral submanifold of $\ker(\varTheta)$
   forms at $\Sigma$ (Frobenius integrability does not hold).

**(d)** For $q > 1$, the [quantum pressure](#rem:madelung-fluid)
enforces

$$
  \mathrm{cond}(\mathcal{L}_\varTheta|_{N_p})
   \leq 
  1 + C_0\hbar_q^2
   <  \infty,
$$

so conditions (1)--(5) hold.  The
[well-posedness theorem](#thm:q-ns-wellposedness) is consistent.

**(e)** At $q = 1$: $\hbar_q = 0$ and there is no isotropic
resistance.  The [vorticity lower
bound](#prop:vorticity-lower-bound) and the
[counter-example](#conj:ns-counterexample) hold if and only
if condition (3) holds at $q = 1$.
