Let $v$ be the solution of the [q-NS system](#def:q-navier-stokes) with $q > 1$ on $[0, T)$. Let $\omega_q = d_q v$ be the $q$-vorticity. The solution $v$ extends smoothly beyond $T$ if and only if

$$
  \int_0^T \lVert \omega_q(t) \rVert_{L^\infty}dt  <  \infty.
$$

Equivalently, if the solution loses regularity at time $T^*$, then

$$
  \int_0^{T^*} \lVert \omega_q(t) \rVert_{L^\infty}dt
  =  +\infty.
$$

The [well-posedness theorem](#thm:q-ns-wellposedness) shows solutions are global for $q > 1$, so the integral is always finite when $q > 1$. The criterion becomes non-trivial only in the $q \to 1$ limit.
