Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with substrate parameter $q \in \mathbb{G}_m^{\mathrm{nt}}(k)$ ([substrate parameter](#def:substrate-parameter)), and let $X$ be a brane curve. A **$q$-local system** on $X$ with structure group $G_q$ is a functor

$$
  \mathcal{L}_q \colon \Pi_1(X) \longrightarrow \mathbf{Rep}(G_q)
$$

from the fundamental groupoid $\Pi_1(X)$ to the category of finite-dimensional representations of $G_q$. It must satisfy the **$q$-monodromy condition**: for every contractible loop $\varrho \colon \mathbf{1} \to \mathbf{1}$ in $\Pi_1(X)$, the monodromy obeys

$$
  \mathcal{L}_q(\varrho) = \mathrm{id} + (q - 1)\Omega_q(\varrho),
$$

where $\Omega_q(\varrho) \in \mathrm{End}(\tau(\mathcal{L}_q))$ is the **$q$-holonomy residue** determined by the underlying $q$-connection ([q-flat connection](#def:q-flat-connection)).

Write $\mathrm{LocSys}_{G_q}(X)$ for the moduli stack of $q$-local systems on $X$.
