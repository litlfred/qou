*Proof.*
By trace cyclicity,
$\chi_\lambda(\beta_\mathcal{K}^*) = \chi_\lambda(w\,\beta_\mathcal{K}\, w^{-1}) = \chi_\lambda(\beta_\mathcal{K})$
for every $\lambda$.  Substituting in
([knot factor](#prop:knot-factor-spectral-form))
$a_\mathcal{K} = \sum_\lambda w_\lambda \cdot
\chi_\lambda(\beta_\mathcal{K})\,\chi_\lambda(\beta_\mathcal{K}^*) / \chi_\lambda(\mathbf{1})^2$
yields the displayed expression.
$\square$

**Worked example ($\mathcal{K} = 4_1$ in $B_3$).** Take the
figure-eight braid
$\beta_{4_1} = \sigma_1\,\sigma_2^{-1}\,\sigma_1\,\sigma_2^{-1}$.
Direct computation of the Hoefsmit characters on the three
partitions $\lambda \vdash 3$ at the aether $q_0$ gives:

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

