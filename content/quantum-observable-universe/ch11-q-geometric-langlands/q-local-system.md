Let $(\mathbf{C}, \theta, G, \mathcal{S})$ be a QOU with substrate
parameter $q$ and let $X$ denote the brane curve.  A **$q$-local system**
on $X$ with structure group $G_q$ is a functor

$$
  \mathcal{L}_q \colon \Pi_1(X) \longrightarrow \mathbf{Rep}(G_q)
$$

from the fundamental groupoid $\Pi_1(X)$ to the category of
finite-dimensional representations of the quantum group $G_q$, subject
to the **$q$-monodromy condition**: for every contractible loop
$\varrho \colon \mathbf{1} \to \mathbf{1}$ in $\Pi_1(X)$, the
monodromy satisfies

$$
  \mathcal{L}_q(\varrho) = \mathrm{id} + (q - 1)\,\Omega_q(\varrho),
$$

where $\Omega_q(\varrho) \in \mathrm{End}(\tau(\mathcal{L}_q))$ is the
**$q$-holonomy residue** determined by the $q$-connection
(Definition \ref{def:q-flat-connection}).

When $q = 1$ the residue vanishes and $\mathcal{L}_1$ is a classical
local system (flat bundle).  For $q \neq 1$ the non-vanishing of
$d_q^2$ (Proposition \ref{prop:categorical-dq-squared}) obstructs
trivial monodromy, so every $q$-local system carries non-trivial
parallel transport even on contractible domains.

We denote by $\mathrm{LocSys}_{G_q}(X)$ the moduli stack of $q$-local
systems on $X$.
