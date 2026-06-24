The corollary translates the Hasse–Weil bound through the spectral coordinate mapping $\alpha_i = q^{\rho_i}$, in three steps: compute the modulus of $q^{\rho}$ for a complex exponent, equate it with the Hasse–Weil value, and invert by strict monotonicity.

**Step 1 — modulus of a complex power.** Fix $q > 1$ as a positive real and let $\rho \in \mathbb{C}$. Writing $q^{\rho} = \exp(\rho \log q)$ (legitimate as $q \neq 0$) and using $|\exp z| = \exp(\operatorname{Re} z)$, the modulus depends only on the real part of the exponent. Since $q$ is a positive real, $\log q$ is real, so $\operatorname{Re}(\rho \log q) = \operatorname{Re}(\rho)\log q$ and
$$
|q^{\rho}| = \exp\bigl(\operatorname{Re}(\rho)\log q\bigr) = q^{\operatorname{Re}(\rho)}.
$$
The complex-analytic bookkeeping (the `cpow`/`exp`/`log` rewrites, vanishing imaginary part) is the Lean witness `abs_cpow_ofReal_eq_rpow_re` (with the $q>1$ specialisation `abs_rpow_eq_rpow_re`).

**Step 2 — insert the Hasse–Weil bound.** The bound on the local $q$-zeta eigenvalues gives $|\alpha_i| = q^{1/2}$ for each $i = 1,\ldots,8$. Combined with Step 1 under $\alpha_i = q^{\rho_i}$,
$$
q^{\operatorname{Re}(\rho_i)} = |\alpha_i| = q^{1/2}.
$$

**Step 3 — invert by monotonicity.** Since $q > 1$, $t \mapsto q^{t}$ is strictly monotone, hence injective in the exponent (`Real.rpow_left_injective`, $q \neq 1$). Thus $\operatorname{Re}(\rho_i) = \tfrac12$ for all $i = 1,\ldots,8$ — the Lean witness `spectral_half_line`.

All eight fundamental Reeb modes lie exactly on the critical line $\operatorname{Re}(\rho) = 1/2$: the finite-field Riemann hypothesis, read in the substrate, says each mode's contribution $X^{\rho_i}/[\rho_i]_q$ to the explicit formula has amplitude $X^{1/2}/|[\rho_i]_q|$ — perfect square-root cancellation. $\qquad\blacksquare$
