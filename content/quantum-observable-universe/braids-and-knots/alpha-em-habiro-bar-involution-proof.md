Write $H = [2]_q\,(1 - h^2\alpha) = (q + q^{-1})\bigl(1 - (q - q^{-1})^2\alpha\bigr)$ over a generic commutative ring with $q$ a formal variable. Following the Lean witness, treat $q$ and $q^{-1}$ as independent ring variables $q, q_i$ (the relation $q\,q_i = 1$ is not needed here), so
$$H(q, q_i, \alpha) = (q + q_i)\bigl(1 - (q - q_i)^2\alpha\bigr).$$

**1. Bar-involution fixed point.** The bar involution $q \mapsto q^{-1}$ acts as the swap $q \leftrightarrow q_i$. The factor $q + q_i$ is symmetric, and $(q - q_i)^2 = (q_i - q)^2$ since squaring absorbs the sign change. Hence every factor of $H$ is fixed:
$$H(q^{-1}) = H(q_i, q, \alpha) = H(q, q_i, \alpha) = H(q),$$
the content of `alphaEmHabiro_bar_invariant` (by `ring`). No reality or archimedean hypothesis enters — the symmetry is the formal $q \leftrightarrow q^{-1}$ swap, so $H$ lies in the bar-fixed sector.

**2. Special values.** At the first two roots of unity $q = q_i = \pm 1$, $h = q - q_i = 0$ and the deformation term drops:
$$H(1) = 2\,(1 - 0) = 2, \qquad H(-1) = -2\,(1 - 0) = -2,$$
i.e. `alphaEmHabiro_at_one` and `alphaEmHabiro_at_neg_one` (each by `ring`, for arbitrary $\alpha$). The value $H(\zeta_1) = 2$ is the classical leading term reproducing $\alpha/(4\pi)$; $H(\zeta_2) = -2$ is the bar mode.

All three are ring identities over a generic `CommRing`, with no appeal to $\mathbb{R}$, ordering, or complex structure — the fibre-level regime where the bar involution, not a reality constraint, is the operative symmetry. $\qquad\blacksquare$
