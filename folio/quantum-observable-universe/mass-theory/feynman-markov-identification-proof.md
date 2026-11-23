**Proof.**
Every Markov trace at $z = q^3/(q^2+1)$ equals the Ocneanu-weighted sum of the seminormal block traces,

$$
  \mathrm{tr}_M(x) = \sum_{\lambda \vdash n} w_\lambda \cdot \mathrm{tr}_{S_\lambda}(x),
$$

for every $n$ and every $x \in H_n(R, q)$. This is the uniqueness of the Markov trace on the Hecke tower, proved for the seminormal representations in `QOU.SchurWeyl.MarkovTraceInstance.eq_wtrace_of_markov`. The left side is the eigenbasis amplitude by definition, so the identity holds.

A partition with three or more rows contains the cell $(2, 0)$, whose factor in the numerator of the Ocneanu weight vanishes at this $z$. Hence $w_\lambda = 0$ for $\ell(\lambda) \geq 3$, and the sum runs over $\ell(\lambda) \leq 2$ alone.

For the closed form, the Ocneanu weight at this $z$ equals $s_\lambda(1, q^2)/(1 + q^2)^n$, where $s_\lambda(1, q^2)$ is the Schur polynomial in two variables evaluated at $(1, q^2)$ (`ocneanuWeight_conventionD_eq_schurPrincipal`). For $\lambda = (\lambda_1, \lambda_2)$,

$$
  s_\lambda(1, q^2)
  = q^{2\lambda_2}\,\frac{q^{2(\lambda_1 - \lambda_2 + 1)} - 1}{q^2 - 1}
  = q^{\lambda_1 + \lambda_2}\,[\lambda_1 - \lambda_2 + 1]_q,
$$

and $(1 + q^2)^n = q^n [2]_q^{\,n}$. Since $\lambda_1 + \lambda_2 = n$, the powers of $q$ cancel, and $w_\lambda = [\lambda_1 - \lambda_2 + 1]_q / [2]_q^{\,n} = \dim_q(V_\lambda)/\dim_q(V^{\otimes n})$. $\square$
