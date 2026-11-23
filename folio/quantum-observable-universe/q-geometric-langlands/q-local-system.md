Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with substrate parameter $q \in \mathbb{G}_m^{\mathrm{nt}}(k)$ ([substrate parameter](#def:substrate-parameter)), and let $X$ be a brane curve. A **$q$-local system** on $X$ with structure group $G_q$ is a functor

$$
  \mathcal{L}_q \colon \Pi_1(X) \longrightarrow \mathbf{Rep}(G_q)
$$

from the fundamental groupoid $\Pi_1(X)$ to the category of finite-dimensional representations of $G_q$. This functor must satisfy the **$q$-monodromy condition**: for every contractible loop $\varrho \colon \mathbf{1} \to \mathbf{1}$ in $\Pi_1(X)$, the monodromy obeys

$$
  \mathcal{L}_q(\varrho) = \mathrm{id} + (q - 1)\Omega_q(\varrho),
$$

where $\Omega_q(\varrho) \in \mathrm{End}(\tau(\mathcal{L}_q))$ is the **$q$-holonomy residue** determined by the underlying $q$-connection.

The $q$-monodromy condition reflects the local geometry of the $\mathbb{G}_m$-family. At $q = 1$, the residue vanishes and $\mathcal{L}_1$ reduces to a classical flat bundle. For $q \neq 1$, the non-vanishing curvature $d_q^2 \neq 0$ ([non-vanishing of $d_q^2$](#prop:categorical-dq-squared)) obstructs trivial monodromy. The Kummer reduction of the obstruction class $\kappa_0$ at level $n$ ([Kummer filtration](#rem:kummer-filtration-obstruction)) controls lifting through the brane tower. A $q$-local system $\mathcal{L}_q$ lifts from level $n$ to $n+1$ if and only if $\kappa_0 \equiv 0 \pmod n$, which occurs precisely when $n \mid \chi(A)$. The moduli stack of $q$-local systems on $X$ is denoted $\mathrm{LocSys}_{G_q}(X)$.
