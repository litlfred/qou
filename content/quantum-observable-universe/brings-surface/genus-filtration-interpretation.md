## Formal coordinates: unwinding $d_q^2 \neq 0$

The non-nilpotence $d_q^2 \alpha = q^{-1}(1-q^{-1}) \omega_V \wedge_q [\xi, \alpha]$
([categorical $d_q^2$](#prop:categorical-dq-squared)) provides
the differential-geometric mechanism.

Associate to $T_{2,p}$ the form
$\alpha_p = a_p(u) \cdot \omega_T \in \Omega^1(A)$, where
$\omega_T$ is the Hecke $1$-form (the $T$-component of the
Maurer--Cartan form on $H_2(q)$) and $u = s^2$ acts as a
grading parameter.

The weight decomposition assigns degree $k$ in $u$ to the
$k$-th Seifert cycle: $\alpha_p = \sum_{k=0}^{g_p} c_k  u^k \omega_T$, with $[\xi, u^k \omega_T] = k \cdot u^k \omega_T$
(the Lie derivative counts Seifert cycles).

Applying $d_q^2$ iteratively:

1. **At genus level $k \leq g$:** The component $c_k u^k \omega_T$
   maps under $\iota_*$ to a class in $H^1(\Sigma_g)$.
   The obstruction $d_q^2(c_k u^k \omega_T) \propto k \cdot \omega_V \wedge c_k u^k \omega_T$ is absorbed by
   the available $H^2(\Sigma_g)$ pairing --- it vanishes on the
   horizontal subcomplex ($\xi$-invariant forms project the
   surplus away).

2. **At genus level $k = g + 1$:** The component
   $c_{g+1} u^{g+1} \omega_T$ has no target in $H^1(\Sigma_g)$.
   The obstruction

   $$
     d_q^2(c_{g+1} u^{g+1} \omega_T)
     = 
     q^{-1}(1-q^{-1})(g+1) c_{g+1} u^{g+1}
     \omega_V \wedge_q \omega_T
   $$

   is a **nonzero class in $\Omega^2(A)$** that does not pair
   to zero against $H_2(\Sigma_g)$.  The coefficient
   $(g+1) \cdot c_{g+1} \cdot q^{-1}(1-q^{-1})$ is nonzero
   for all $q > 1$, and $c_{g+1} = 1$ (the leading Chebyshev
   coefficient is always $1$).

3. **The obstruction class.** The $d_q^2$-obstruction at level
   $g + 1$ descends to the Yekutieli class:

   $$
     \kappa(T_{2,p})
     = 
     (g+1) \cdot q^{-1}(1-q^{-1}) \cdot [\omega_V \wedge_q \omega_T]
      \in  H^2(\Sigma_g, \mathbb{Z})
   $$

   which is nonzero for $q \neq 1$.  At $q = 1$ (the classical
   limit), $d_q^2 = 0$ and all obstructions vanish ---
   consistent with classical de Rham cohomology having no
   genus constraint on embeddings.
