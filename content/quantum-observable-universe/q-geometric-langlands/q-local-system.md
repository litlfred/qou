Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q$ and let $X$ denote the brane curve.  The
substrate $q \in \mathbb{G}_m^{\mathrm{nt}}(k)$ determines a fibre
in the $\mathbb{G}_m$-family of deformations
([substrate parameter](#def:substrate-parameter)).  A **$q$-local
system** on $X$ with structure group $G_q$ is a functor

$$
  \mathcal{L}_q \colon \Pi_1(X) \longrightarrow \mathbf{Rep}(G_q)
$$

from the fundamental groupoid $\Pi_1(X)$ to the category of
finite-dimensional representations of the quantum group $G_q$, subject
to the **$q$-monodromy condition**: for every contractible loop
$\varrho \colon \mathbf{1} \to \mathbf{1}$ in $\Pi_1(X)$, the
monodromy satisfies

$$
  \mathcal{L}_q(\varrho) = \mathrm{id} + (q - 1)\Omega_q(\varrho),
$$

where $\Omega_q(\varrho) \in \mathrm{End}(\tau(\mathcal{L}_q))$ is the
**$q$-holonomy residue** determined by the $q$-connection
([q-flat connection](#def:q-flat-connection)).

The $q$-monodromy condition is the local manifestation of the
$\mathbb{G}_m$-family structure: at $q = 1$ the residue vanishes and
$\mathcal{L}_1$ is a classical local system (flat bundle), while for
$q \neq 1$ the non-vanishing of $d_q^2$
([non-vanishing of $d_q^2$](#prop:categorical-dq-squared))
obstructs trivial monodromy.  The Kummer reduction of the Yekutieli
class $\kappa_0$ at level $n$
([Kummer filtration](#rem:kummer-filtration-obstruction))
controls which $q$-local systems admit lifts through the brane tower:
$\mathcal{L}_q$ lifts from level $n$ to $n+1$ iff
$\kappa_0 \bmod n = 0$, equivalently $n \mid \chi(A)$.

We denote by $\mathrm{LocSys}_{G_q}(X)$ the moduli stack of $q$-local
systems on $X$.
