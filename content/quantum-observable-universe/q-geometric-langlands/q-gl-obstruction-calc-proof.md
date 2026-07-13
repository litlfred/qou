**Item (1).**
The $q$-flatness equation is $\nabla_q^2 = (q-1)\mathcal{F}_q$ ([q-flat connection](#def:q-flat-connection)). The $q$-curvature $\mathcal{F}_q$ is a class in $\mathrm{End}(\mathcal{V}) \otimes \Omega^2_q$. The Hochschild--Kostant--Rosenberg comparison identifies this space with $HH^2(\mathcal{U}_q, \mathrm{Ad})$. The image under $\mathrm{HKR}$ is the gerbe-theoretic obstruction class $\kappa_0 = e(\xi)$ ([Kummer filtration](#rem:kummer-filtration-obstruction)).

**Item (2).**
If $\kappa_0 = 0$ in $H^2(\mathcal{S}, \mathbb{G}_m)$, then $\mathcal{F}_q = \mathrm{HKR}^{-1}(0) = 0$. Thus, $\nabla_q$ is $q$-flat. Conversely, $\mathcal{F}_q = 0$ implies $\mathrm{HKR}(\mathcal{F}_q) = \kappa_0 = 0$.

**Item (3).**
The Kummer exact sequence $1 \to \mu_n \to \mathbb{G}_m \xrightarrow{(\cdot)^n} \mathbb{G}_m \to 1$ yields the reduction $\kappa_0 \bmod n$. We know $\mathrm{tr}(\kappa_0) = \chi(A)$. By the [Kummer filtration](#rem:kummer-filtration-obstruction), $\kappa_0 \bmod n = 0$ if and only if $n \mid \chi(A)$. Lifting through the brane tower from level $n$ to $n+1$ requires $\kappa_n = 0$ ([Quantum lifting condition](#def:yekutieli-lifting-condition)). The complementary subgroup structure $\kappa_n = \kappa_0 + \delta_n$ prevents cancellation.

**Item (4).**
The set $\{n : n \mid \chi(A)\}$ has exactly $d(\chi(A))$ elements, where $d$ is the divisor function. This set is finite. Its complement in $\mathbb{Z}_{>0}$ has density $1$. $\square$
