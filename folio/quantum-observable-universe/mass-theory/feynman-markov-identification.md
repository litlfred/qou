*Let $q$ be real, not a root of unity, with $q^2 + 1 \neq 0$, and let $\mathrm{tr}_M$ be a Markov trace on the Hecke tower at the convention-D parameter $z = q^3/(q^2+1)$. For $x \in H_n(R, q)$, the transition amplitude on the eigenbasis is the Markov-weighted sum of partial traces:*

$$
  \langle\psi_f|\psi_i\rangle_{\mathrm{eigenbasis}}
  :=
  \sum_{\lambda \vdash n}
  w_\lambda \cdot \mathrm{tr}_{S_\lambda}(x),
$$

*where $w_\lambda$ is the Ocneanu weight of $\lambda$ at $z$ and $\mathrm{tr}_{S_\lambda}$ is the trace of the seminormal representation $S_\lambda$. This amplitude equals $\mathrm{tr}_M(x)$. The weight $w_\lambda$ vanishes whenever $\lambda$ has three or more rows, so only the partitions with $\ell(\lambda) \leq 2$ contribute, and for those*

$$
  w_\lambda = \frac{\dim_q(V_\lambda)}{\dim_q(V^{\otimes n})}
  = \frac{[\lambda_1 - \lambda_2 + 1]_q}{[2]_q^{\,n}}.
$$
