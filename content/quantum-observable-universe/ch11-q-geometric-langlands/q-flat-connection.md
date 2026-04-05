Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe and let
$\mathcal{V}$ be a $G_q$-equivariant object in $\mathbf{C}$ over the
brane curve $X$.  A **$q$-flat connection** on $\mathcal{V}$ is a
$q$-connection
$\nabla_q \colon \mathcal{V} \to \Omega^1_q \otimes \mathcal{V}$
([categorical $q$-connection](#def:categorical-q-connection))
satisfying the **$q$-flatness equation**:

$$
  \nabla_q^2 = (q - 1)\,\mathcal{F}_q,
$$

where $\mathcal{F}_q \in \mathrm{End}(\mathcal{V}) \otimes \Omega^2_q$
is the **$q$-curvature**.  The $q$-curvature is determined by
the $d_q^2$ obstruction
([non-vanishing of $d_q^2$](#prop:categorical-dq-squared)):
explicitly,

$$
  \mathcal{F}_q(s) = (q-1)^{-1}\,\nabla_q(\nabla_q(s))
  \quad \text{for local sections } s \in \Gamma(\mathcal{V}).
$$

Via the Hochschild--Kostant--Rosenberg comparison
([Kummer filtration](#prop:kummer-filtration-obstruction)),
the $q$-curvature is the image of the Yekutieli class under the
HKR map:

$$
  \mathcal{F}_q
  \;=\;
  \mathrm{HKR}^{-1}(\kappa_0)
  \;\in\;
  HH^2(\mathcal{U}_q,\, \mathrm{Ad}).
$$

A $q$-flat connection has $\mathcal{F}_q = 0$, carrying the
*minimal possible curvature* compatible with $d_q^2 \neq 0$.
The category of $q$-flat connections on $X$ with structure group
$G_q$ is equivalent to the category of $q$-local systems
$\mathrm{LocSys}_{G_q}(X)$
([q-local system](#def:q-local-system)).
