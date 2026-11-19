Let $\check{G}_q$ be the $q$-Langlands dual group ([q-Langlands dual](#def:q-langlands-dual)) and let $\check{\mathfrak{b}}_q \subset \check{\mathfrak{g}}_q$ be a Borel subalgebra. A **$q$-oper** on $X$ is a $q$-flat connection ([q-flat connection](#def:q-flat-connection))

$$
  (\mathcal{P}_{\check{G}_q}, \nabla_q)
$$

on a $\check{G}_q$-bundle $\mathcal{P}_{\check{G}_q} \to X$, equipped with a $\check{B}_q$-reduction $\mathcal{P}_{\check{B}_q} \subset \mathcal{P}_{\check{G}_q}$. This data must satisfy the **$q$-oper condition**: the $q$-connection $\nabla_q$ is strictly transverse to the Borel reduction. Specifically, for each simple root $\alpha_i$ of $\check{G}_q$, the component of $\nabla_q$ along $\check{\mathfrak{g}}_{-\alpha_i}$ must not vanish:

$$
  \mathrm{pr}_{-\alpha_i}(\nabla_q \bmod \check{\mathfrak{b}}_q)
  \neq 0.
$$

We denote the moduli stack of $q$-opers by $\mathrm{Op}_{\check{G}_q}(X)$.
