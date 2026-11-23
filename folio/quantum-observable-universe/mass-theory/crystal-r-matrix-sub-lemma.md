*Let $\mathbf{H}_n(q)$ be the Iwahori–Hecke algebra over a field with $q$ generic, $\lambda \vdash n$, and $\beta_1 \in \mathbf{H}_{n_1}(q)$, $\beta_2 \in \mathbf{H}_{n_2}(q)$ with $n = n_1 + n_2$. Let $\sigma_i \in \mathbf{H}_n(q)$ be a boundary generator and let $A^\lambda_{\mu, \nu}(\sigma_i)$ be its $(\mu, \nu)$-block in the Wenzl LR decomposition. For a standard Young tableau $T \in \mathrm{SYT}(\lambda)$ in the $(\mu, \nu)$-block, let $\rho_T(i) = c(i+1) - c(i)$ be the axial distance, with $c = \mathrm{col} - \mathrm{row}$ the content of the cell holding the entry.*

*The diagonal entry of $A^\lambda_{\mu, \nu}(\sigma_i)$ at $T$ has pole order at $q = 0$*

$$
  \boxed{\;\;
    \mathrm{pole}\bigl(A^\lambda_{\mu, \nu}(\sigma_i),\, T\bigr)
    \;=\;
    \mathbf{1}\bigl[\rho_T(i) \le -1\bigr].
  \;\;}
$$

In Hoefsmit's seminormal form \cite{hoefsmit1974} the boundary generator acts on the basis vector $v_T$ with diagonal entry

$$
  a_T(i) \;=\; \frac{q - q^{-1}}{1 - q^{-2\rho}}, \qquad \rho = \rho_T(i),
$$

which is $-q^{-1}$ on a column tableau ($\rho = -1$) and $q$ on a row tableau ($\rho = 1$). For $\rho = -(m+1)$,

$$
  a_T(i) \;=\; q^{-1}\,\frac{q^2 - 1}{1 - q^{2(m+1)}},
$$

and the second factor takes the value $-1$ at $q = 0$, so the pole is simple. For $\rho = m+1$,

$$
  a_T(i) \;=\; q^{2m+1}\,\frac{q^2 - 1}{q^{2(m+1)} - 1},
$$

and the second factor takes the value $1$ at $q = 0$, so there is no pole. Both factorisations hold over any field.

The statement concerns the diagonal entry only; the off-diagonal entries of the seminormal form are not covered. The column-tableau count it gives, $k(p-1)$ poles for $(\sigma_1 \cdots \sigma_{p-1})^k$ on $V_{(1^p)}$, is checked for seven torus-knot interfaces and six non-column shapes.
