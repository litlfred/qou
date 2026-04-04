Let $\beta$ be a braid on $n$ strands with $c$ crossings,
$L = \hat{\beta}$ its closure, and
$\mathcal{R}(L)$ the Skein resolution tree — a
binary-ternary tree of depth $c$ with $3^c$ leaves
([Skein Turing machine](#rem:skein-turing-machine)).  Stratify
the tree by **resolution depth**:

$$
  \mathcal{R}_0 = \{L\}
  \;\hookrightarrow\;
  \mathcal{R}_1
  \;\hookrightarrow\;
  \cdots
  \;\hookrightarrow\;
  \mathcal{R}_c = \mathcal{R}(L).
$$

At depth $k$, the partial resolution $\mathcal{R}_k$ consists
of all links obtained by resolving $k$ of the $c$ crossings.
This is a tower — structurally parallel to the brane tower
$A_0 \hookrightarrow A_1 \hookrightarrow \cdots$
([jet prolongation](#prop:jet-prolongation)) — with the
$q$-connection replaced by the Skein relation.

**The computational Yekutieli class.**

Each transition $\mathcal{R}_k \hookrightarrow \mathcal{R}_{k+1}$
defines a central extension of the Hecke module at depth $k$.
The Yekutieli obstruction class
([quantum characteristic classes](#def:quantum-characteristic-classes))
adapted to the resolution tower is

$$
  \kappa_k^{\mathrm{comp}}(L, q)
  \;\in\;
  H^2(\mathcal{R}_k,\, \mathcal{B}_q),
$$

where $\mathcal{B}_q$ is the band of units in the Hecke algebra
$H_n(q)$.  This class measures whether the degree-$0$ answer
$P_L(q)$ can be extracted from the partial resolution at depth
$k$ — whether the Markov trace on $\mathcal{R}_k$ already
determines $P_L(q)$ without resolving the remaining $c - k$
crossings.

**Vanishing criterion.**
The obstruction $\kappa_k^{\mathrm{comp}}$ vanishes at depth $k$
iff the **residual weight** of the unresolved subtree is zero:

$$
  \kappa_k^{\mathrm{comp}}(L, q) = 0
  \quad\Longleftrightarrow\quad
  \sum_{\gamma \in \mathcal{R}_c \setminus \mathcal{R}_k}
  w(\gamma, q) = 0,
$$

where $w(\gamma, q)$ is the Skein weight of the resolution path
$\gamma$ (product of $q^{\pm 1}$ and $s = q^{1/2} - q^{-1/2}$
over crossings in $\gamma$).  The sum vanishes iff the
unresolved crossings produce **complete destructive
interference** — all remaining paths cancel exactly.

**The computational obstruction at polynomial depth.**

Fix $p(c) = c^d$ for some constant $d$ (a polynomial bound).
The **Skein resolution obstruction** for $L$ at substrate
parameter $q$ is

$$
  \kappa_c^{\mathrm{comp}}(L, q)
  \;:=\;
  \kappa_{p(c)}^{\mathrm{comp}}(L, q)
  \;\in\;
  H^2(\mathcal{R}_{p(c)},\, \mathcal{B}_q).
$$

This is the obstruction at polynomial depth.  It vanishes iff
$P_L(q)$ is computable in $\mathrm{poly}(c)$ Planck steps —
iff the problem is in $\mathrm{P}$.

**$q$-dependence: the obstruction is not absolute.**

The Skein weights $w(\gamma, q)$ are rational functions of
$q^{1/2}$.  The residual weight sum is therefore a **rational
function of $q$**, and its zero locus is an algebraic variety
in the $q$-plane.  The obstruction vanishes at those $q$ where
the variety passes through $q$, and persists elsewhere.

This means the **complexity of a problem depends on $q$**:

| Regime | $q$ | Obstruction | Complexity |
|--------|-----|-------------|------------|
| Finite field $\mathbb{F}_p$ | $q \in \mathbb{F}_p^\times$ | Always vanishes (finite orbits) | P = NP |
| Root of unity $q_k$ | $e^{2\pi i/(k+2)}$ | Vanishes for BQP problems | BQP ⊆ NP |
| Real substrate $q_0$ | $\approx 1.1097$ | Non-vanishing conjectured for NP-complete | P $\stackrel{?}{\neq}$ NP |
| Classical limit $q \to 1$ | $1^+$ | Degenerate ($s \to 0$, all weights collapse) | Trivial |

**Structural parallel with the NS obstruction.**

The Skein resolution obstruction mirrors the NS obstruction
tower ([NS obstruction](#prop:ns-obstruction-tower)) point
by point:

| NS obstruction | Skein resolution obstruction |
|----------------|----------------------------|
| Brane tower $A_n \hookrightarrow A_{n+1}$ | Resolution tree $\mathcal{R}_k \hookrightarrow \mathcal{R}_{k+1}$ |
| Yekutieli class $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ | Comp.\ class $\kappa_k^{\mathrm{comp}} \in H^2(\mathcal{R}_k, \mathcal{B}_q)$ |
| Collision locus $\Sigma$ | Polynomial-depth boundary $\mathcal{R}_{p(c)}$ |
| Euler class $e(\xi)$, $\mathrm{tr}(\kappa_0) = \chi(A)$ | Residual Skein weight, $\mathrm{tr}(\kappa_c^{\mathrm{comp}}) = w_{\mathrm{res}}$ |
| NS-singular: blowup ($\kappa_n|_\Sigma \neq 0$) | Super-horizon: NP-hard ($\kappa_c^{\mathrm{comp}} \neq 0$) |
| NS-regular: global smooth flow ($\kappa_n|_\Sigma = 0$) | Sub-horizon: P ($\kappa_c^{\mathrm{comp}} = 0$) |
| Depends on $\chi(A)$ | Depends on $q$ and base field |

**Descent decomposition of the obstruction.**

The descent involution $\hat{\tau}$
([descent involution](#def:descent-involution)) decomposes the
obstruction at each resolution depth:

$$
  \kappa_k^{\mathrm{comp}}
  \;=\;
  \kappa_k^{\mathrm{desc}}
  \;+\;
  \kappa_k^{\mathrm{trans}},
$$

where $\kappa_k^{\mathrm{desc}} \in \mathcal{A}^{\mathrm{desc}}$
is the descended (classical) component and
$\kappa_k^{\mathrm{trans}} \in \mathcal{A}^{\mathrm{trans}}$ is
the transient (quantum) component
([descent eigenspaces](#prop:descent-eigenspaces)).

- **Classical computation** (real $q$): only
  $\kappa_k^{\mathrm{desc}}$ is accessible.  If it is
  non-vanishing, the problem is not in P.
- **Quantum computation** (root of unity $q_k$): both
  components are accessible.  If
  $\kappa_k^{\mathrm{desc}} \neq 0$ but
  $\kappa_k^{\mathrm{trans}} = -\kappa_k^{\mathrm{desc}}$
  (exact cancellation), the problem is in BQP but not in P.
- **Full obstruction**: if $\kappa_k^{\mathrm{comp}} \neq 0$
  even after including the transient modes, the problem is
  not in BQP.
