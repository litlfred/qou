Let $\mathcal{V}$ be a $G_q$-equivariant bundle on the brane curve $X$.
A **$q$-flat connection** on $\mathcal{V}$ is a $q$-connection
$\nabla_q \colon \mathcal{V} \to \Omega^1_q \otimes \mathcal{V}$
(in the sense of Definition \ref{def:categorical-q-connection})
satisfying the **$q$-flatness equation**:

$$
  \nabla_q^2 = (q - 1)\,\mathcal{F}_q,
$$

where $\mathcal{F}_q \in \mathrm{End}(\mathcal{V}) \otimes \Omega^2_q$
is the **$q$-curvature**, a canonically determined endomorphism-valued
$2$-form.  Explicitly, $\mathcal{F}_q$ is the image of $d_q^2$ acting
on sections of $\mathcal{V}$:

$$
  \mathcal{F}_q(s) = \nabla_q(\nabla_q(s)) - (q-1)^{-1}\,d_q^2(s)
  \quad \text{for local sections } s \in \Gamma(\mathcal{V}).
$$

A $q$-flat connection is one for which $\mathcal{F}_q = 0$, i.e.
$\nabla_q^2 = (q-1)\,\mathcal{F}_q$ holds with $\mathcal{F}_q$
*minimal* (determined entirely by the intrinsic $d_q^2$ obstruction).

The category of $q$-flat connections on $X$ with structure group $G_q$
is equivalent to the category of $q$-local systems
$\mathrm{LocSys}_{G_q}(X)$.
