**Proposition (conditional on
[`conj:q-aubin-lions`](#conj:q-aubin-lions),
[`conj:ns-counterexample`](#conj:ns-counterexample),
[`conj:critical-exponent`](#conj:critical-exponent),
[`prop:blowup-yekutieli`](#prop:blowup-yekutieli),
and
[`conj:regularity-breakdown`](#conj:regularity-breakdown);
"Core Levi form").**

Let $\varrho$ track a [geodesic vortex](#rem:geodesic-vortices) on the [state bundle](#ex:c-quantum-observable-universe) $(\mathcal{S}, \varTheta)$ with [Levi form](#def:levi-form-defect) $\mathcal{L}_\varTheta(V, W) = -id\varTheta(V, \bar{W})$. At $p \in \varrho$ take the horizontal normal plane $N_p\varrho \subset \ker(\varTheta_p)$, with Levi eigenvalues $\lambda_\parallel(p), \lambda_\perp(p)$ ($\lambda_\parallel$ toward an adjacent filament, $\lambda_\perp$ perpendicular) and core radii $a_\parallel(p), a_\perp(p)$ from the half-maximum boundaries of $|\psi|^2$ along $N_p\varrho$. Then:

*(a)* The Levi eigenvalue ratio tightly bounds the core aspect ratio:

$$
  \frac{a_\perp(p)}{a_\parallel(p)}
  = 
  \sqrt{\frac{\lambda_\parallel(p)}{\lambda_\perp(p)}}
   \cdot 
  \bigl(1 + O(\hbar_q^2)\bigr).
$$

*(b)* The Levi form condition number over $N_p\varrho$ evaluates as

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

*(c)* The following assertions are strictly equivalent:

1. Core aspect ratio stays bounded: $\sup_{t < T^*} a_\perp(t) / a_\parallel(t) \leq C$.
2. Levi form condition number stays bounded: $\sup_{t < T^*} \mathrm{cond}(\mathcal{L}_\varTheta|_{N_p}) \leq C^2$.
3. Contact structure $\ker(\varTheta)$ remains **non-degenerate** exactly at the collision locus $\Sigma$ (both $\lambda_\parallel, \lambda_\perp > 0$ globally on $\Sigma$).
4. The local [observability axiom](#def:quantum-observable-universe) $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ holds at all $p \in \Sigma$.
5. Frobenius integrability fails cleanly: no 2-dimensional integral submanifold of $\ker(\varTheta)$ nucleates at $\Sigma$.

*(d)* Evaluated for $q > 1$, the continuous [quantum pressure](#rem:madelung-fluid) mechanically enforces

$$
  \mathrm{cond}(\mathcal{L}_\varTheta|_{N_p})
   \leq 
  1 + C_0\hbar_q^2
   <  \infty.
$$

Conditions (1)--(5) uniformly hold. The [well-posedness theorem](#thm:q-ns-wellposedness) remains intact.

*(e)* Evaluated at $q = 1$, $\hbar_q = 0$ and isotropic resistance zeroes out. The [vorticity lower bound](#prop:vorticity-lower-bound) and the [counter-example](#conj:ns-counterexample) trigger if and only if condition (3) holds rigidly at $q = 1$.

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
