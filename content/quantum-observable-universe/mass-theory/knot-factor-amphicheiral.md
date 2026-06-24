**Corollary (knot factor for Markov-amphicheiral knots).**
*Let $\mathcal{K}$ be **Markov-amphicheiral**: its mirror braid
representative $\beta_\mathcal{K}^*$ is conjugate to
$\beta_\mathcal{K}$ in $H_n(R, q)$ — i.e. there exists
$w \in H_n(R, q)^{\times}$ with*

$$
  \beta_\mathcal{K}^* \;=\; w\,\beta_\mathcal{K}\, w^{-1}.
$$

*Then the knot factor is a sum of positive squares weighted by
Plancherel weights:*

$$
  a_\mathcal{K} \;=\;
  \sum_{\lambda \vdash n}\, w_\lambda\,
  \frac{\chi_\lambda(\beta_\mathcal{K})^2}{\chi_\lambda(\mathbf{1})^2}.
$$

**Worked example ($\mathcal{K} = 4_1$ in $B_3$).** Take the
figure-eight braid
$\beta_{4_1} = \sigma_1\,\sigma_2^{-1}\,\sigma_1\,\sigma_2^{-1}$.
Direct computation of the Hoefsmit characters on the three
partitions $\lambda \vdash 3$ at the substrate $q_0$ gives:

| $\lambda$ | $\chi_\lambda(\beta_{4_1})$ | $\chi_\lambda(\beta_{4_1}^*)$ | match? |
|-----------|---:|---:|---|
| $(3)$ | $+1$ | $+1$ | yes |
| $(2,1)$ | $-1$ | $-1$ | yes |
| $(1,1,1)$ | $+1$ | $+1$ | yes |

All three characters agree, so $\beta_{4_1}^*$ is conjugate to
$\beta_{4_1}$ in $H_3(q)$ — i.e. $4_1$ is Markov-amphicheiral.
The displayed formula therefore applies, with

$$
  a_{4_1} \;=\;
  w_{(3)}\cdot 1
  \;+\; w_{(2,1)}\cdot \tfrac{1}{4}
  \;+\; w_{(1,1,1)}\cdot 1.
$$

This is the alternating-block projection used in the
${}^3\mathrm{H}$ and ${}^3\mathrm{He}$ formulas — not a fitted
ansatz.

**Note on the historical formulation.**  An earlier version of
this corollary stated
$\chi_\lambda(\beta_\mathcal{K}^*) = (-1)^{[\lambda = (1^n)]}\chi_\lambda(\beta_\mathcal{K})$
("sign-flip on the alternating block") and collapsed the formula
to $a = 1 - h^2$ with $h := \chi_{(1^n)}/\chi_{(1^n)}(\mathbf{1})$.
The sign-flip claim is empirically false on $4_1$: the
1-dimensional alternating character factors through writhe, which
is $0$ for both $\beta_{4_1}$ and its mirror, so both compute to
$+1$ rather than to opposite signs.  In addition, the collapse to
$1 - h^2$ silently invoked
$\sum_{\lambda \neq (1^n)} w_\lambda (\chi_\lambda/\chi_\lambda(\mathbf{1}))^2 = 1$,
which is a Cauchy–Schwarz bound, not an identity.  The
Markov-amphicheirality framework above replaces both defects with
a single, structural condition (conjugacy of $\beta_K^*$ to
$\beta_K$ in $H_n$) that $4_1$ in fact satisfies, and gives the
clean sum-of-positive-squares formula.  See the resolution
discussion in
[`docs/coordination/i1-probe-author-queue-.md`](../../../../docs/coordination/i1-probe-author-queue-.md)
and the computational verification in
[`computations/probes/knot_factor_amphicheiral_BD_probe.py`](../../../../computations/probes/knot_factor_amphicheiral_BD_probe.py).
