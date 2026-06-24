Let $v$ be the solution of the [q-NS system](#def:q-navier-stokes)
with $q > 1$ on $[0, T)$ and let $\omega_q = d_q v$ be the
$q$-vorticity.  Then $v$ extends smoothly beyond $T$ if and only if

$$
  \int_0^T \lVert \omega_q(t) \rVert_{L^\infty}dt  <  \infty.
$$

Equivalently: if the solution loses regularity at time $T^*$, then

$$
  \int_0^{T^*} \lVert \omega_q(t) \rVert_{L^\infty}dt
  =  +\infty.
$$

Since the [well-posedness theorem](#thm:q-ns-wellposedness) shows
solutions are global for $q > 1$, the integral is always finite
when $q > 1$.  The criterion becomes non-trivial only in the
$q \to 1$ limit.

The $q$-vorticity estimate is a direct algebraic translation of the classical Beale-Kato-Majda criterion; here the bound functions as a diagnostic limit check in the observable universe. Because the deformed Navier-Stokes system is unconditionally globally regular for $q > 1$, the integral is finite in the bulk, so the BKM condition shifts from a PDE survival test to an obstruction indicator at the $q \to 1$ substrate boundary.
