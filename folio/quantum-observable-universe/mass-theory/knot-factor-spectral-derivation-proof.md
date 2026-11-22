*Proof.*
The $e_\lambda$ are orthogonal central idempotents, so
$e_\lambda x = x e_\lambda$ and $\chi_\mu(e_\lambda x) = \delta_{\lambda\mu}\,\chi_\lambda(x)$
for every $x \in A$. Hence

$$
  \tau(e_\lambda x) \;=\; \sum_\mu y_\mu\, \chi_\mu(e_\lambda x) \;=\; y_\lambda\, \chi_\lambda(x).
$$

With $x = \mathbf{1}$ this gives $w_\lambda = \tau(e_\lambda) = y_\lambda d_\lambda$, and
$\sum_\lambda w_\lambda = \tau\bigl(\sum_\lambda e_\lambda\bigr) = \tau(\mathbf{1}) = 1$.
With $x = \beta_\mathcal{K}^*$ and linearity of $\tau$,

$$
  \tau\bigl(\pi(\beta_\mathcal{K})\,\beta_\mathcal{K}^*\bigr)
  \;=\; \sum_\lambda \frac{\chi_\lambda(\beta_\mathcal{K})}{d_\lambda}\, y_\lambda\, \chi_\lambda(\beta_\mathcal{K}^*)
  \;=\; \sum_\lambda w_\lambda\, \frac{\chi_\lambda(\beta_\mathcal{K})\,\chi_\lambda(\beta_\mathcal{K}^*)}{d_\lambda^{\,2}}.
$$

Since $\chi_\lambda(\pi(x)) = \chi_\lambda(x)$, the same computation with $\pi(\beta_\mathcal{K}^*)$
in place of $\beta_\mathcal{K}^*$ gives the same sum. For $\beta_\mathcal{K} = \mathbf{1}$ every ratio is
$1$ and the sum is $\sum_\lambda w_\lambda = 1$. Under convention D, $y_\lambda = 0$ for three-row
$\lambda$, so $w_\lambda = 0$ there. $\square$

**Scope.** The projection $\pi$ is essential. The uncentred entry $\tau(\beta_\mathcal{K}\,\beta_\mathcal{K}^*)$
equals $\sum_\lambda y_\lambda\,\chi_\lambda(\beta_\mathcal{K}\beta_\mathcal{K}^*)$, the character of a product,
which is not the product of characters unless one factor is central. The earlier statement of this
block used that uncentred entry with weights $\dim_q^2 V_\lambda / [n]_q!$; at $\beta_\mathcal{K} = \mathbf{1}$
it gave $1 = \sum_\lambda \dim_q^2 V_\lambda/[n]_q!$, which is false for $q \neq 1$.
