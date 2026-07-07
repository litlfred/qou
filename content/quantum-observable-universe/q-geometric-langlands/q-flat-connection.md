Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe and let $\mathcal{V}$ be a $G_q$-equivariant object in $\mathbf{C}$ over the brane curve $X$. A **$q$-flat connection** on $\mathcal{V}$ is a $q$-connection $\nabla_q \colon \mathcal{V} \to \Omega^1_q \otimes \mathcal{V}$ ([categorical $q$-connection](#def:categorical-q-connection)) whose total curvature equals the intrinsic $q$-curvature dictated by $d_q^2$:

$$
  \nabla_q^2 = (q - 1)\mathcal{F}_q^{\mathrm{intr}}.
$$

Here, $\mathcal{F}_q^{\mathrm{intr}} \in \mathrm{End}(\mathcal{V}) \otimes \Omega^2_q$ is the **intrinsic $q$-curvature**, defined as the image of the obstruction class $\kappa_0$ under the Hochschild--Kostant--Rosenberg map ([Kummer filtration](#rem:kummer-filtration-obstruction)):

$$
  \mathcal{F}_q^{\mathrm{intr}}
  = 
  \mathrm{HKR}^{-1}(\kappa_0)
   \in 
  HH^2(\mathcal{U}_q, \mathrm{Ad}).
$$

In general, a $q$-connection has total curvature $\nabla_q^2 = (q - 1)\mathcal{F}_q^{\mathrm{intr}} + \mathcal{F}_q^{\mathrm{conn}}$, where $\mathcal{F}_q^{\mathrm{conn}}$ is the connection-dependent curvature. A connection is $q$-flat when $\mathcal{F}_q^{\mathrm{conn}} = 0$. In this state, all curvature is intrinsic and arises solely from the $d_q^2 \neq 0$ obstruction ([non-vanishing of $d_q^2$](#prop:categorical-dq-squared)). A $q$-flat connection minimizes curvature rather than vanishing it. The category of $q$-flat connections on $X$ with structure group $G_q$ is equivalent to the category of $q$-local systems $\mathrm{LocSys}_{G_q}(X)$ ([q-local system](#def:q-local-system)).
