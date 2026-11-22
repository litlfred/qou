*Let $\mathcal{K}$ be a knot with braid representative $\beta_\mathcal{K} \in B_n$ and mirror $\beta_\mathcal{K}^*$. Work in the semisimple Hecke algebra $A = H_n(R, q)$ with central idempotents $\{e_\lambda\}_{\lambda \vdash n}$, irreducible characters $\chi_\lambda$, and $d_\lambda := \chi_\lambda(\mathbf{1}) = \dim V_\lambda$. Let $\tau = \sum_\lambda y_\lambda \chi_\lambda$ be the Markov trace, normalised by $\tau(\mathbf{1}) = 1$, and let*

$$
  \pi(x) \;:=\; \sum_{\lambda \,\vdash\, n} \frac{\chi_\lambda(x)}{d_\lambda}\, e_\lambda
$$

*be the projection of $A$ onto its centre. Define the knot factor as the Gram pairing of the central part of $\beta_\mathcal{K}$ with its mirror,*

$$
  a_\mathcal{K} \;:=\; \frac{\tau\bigl(\pi(\beta_\mathcal{K})\, \beta_\mathcal{K}^*\bigr)}{\tau(\mathbf{1})}.
$$

*Then*

$$
  a_\mathcal{K}
  \;=\;
  \tau\bigl(\pi(\beta_\mathcal{K})\,\pi(\beta_\mathcal{K}^*)\bigr)
  \;=\;
  \sum_{\lambda \,\vdash\, n}
    w_\lambda \,
    \frac{\chi_\lambda(\beta_\mathcal{K})\, \chi_\lambda(\beta_\mathcal{K}^*)}
         {d_\lambda^{\,2}},
  \qquad
  w_\lambda \;:=\; \tau(e_\lambda) \;=\; y_\lambda\, d_\lambda ,
$$

*and the weights satisfy $\sum_\lambda w_\lambda = 1$. Taking $\beta_\mathcal{K} = \mathbf{1}$ gives $a_\mathbf{1} = 1$. Under convention D, $w_\lambda = 0$ for every $\lambda$ with three or more rows, so only the two-row blocks contribute. The identity holds exactly in $R$.*
