*Step 1 — :refterm[Descent]{#descent} is idempotent.* By construction
([:refterm[descent]{#descent} involution](#def\:descent-involution)),
$\hat\tau_n = \ell_n \circ \mathfrak{d}_{n+1}$ with
$\mathfrak{d}_{n+1} \circ \ell_n = \mathrm{id}_{\mathrm{End}(A_n)}$,
so

$$
  \hat\tau_n^2 = \ell_n \circ (\mathfrak{d}_{n+1} \circ \ell_n)
    \circ \mathfrak{d}_{n+1}
    = \ell_n \circ \mathfrak{d}_{n+1} = \hat\tau_n.
$$

The descended subalgebra is the fixed-point subspace:
$\hat\tau_n|_{\mathcal{A}^{\mathrm{desc}}_{n+1}} = \mathrm{id}$.

*Step 2 — :refterm[Descent]{#descent} factors through the base.* For any
$\alpha \in \mathrm{End}(A_{n+1})$,

$$
  \hat\tau_n(\alpha)
  = \ell_n\bigl(\mathfrak{d}_{n+1}(\alpha)\bigr)
  \;\in\; \ell_n\bigl(\mathrm{End}(A_n)\bigr)
  \cong \mathrm{End}(A_n).
$$

Writing $\alpha_n := \mathfrak{d}_{n+1}(\alpha)$ for the
descended representative at level $n$, the compatibility of
the categorical trace with $\ell_n$
([topological mass proof](#prf\:topological-mass), Step 2) gives

$$
  \mathrm{tr}\bigl(\hat\tau_n(\alpha)\bigr)
  = \mathrm{tr}\bigl(\ell_n(\alpha_n)\bigr)
  = \mathrm{tr}_n(\alpha_n).
$$

The descended trace at level $n+1$ therefore equals the level-$n$
trace of the descended representative — a level-lowering step.

*Step 3 — Recursion to the base.* Apply Step 2 iteratively.
Let $\alpha^{(k)} := \mathfrak{d}_k(\alpha^{(k+1)})$ be the
recursive :refterm[descent]{#descent} to level $k$. Then for all $0 \le k \le n$,

$$
  \mathrm{tr}\bigl(\hat\tau_n \circ \hat\tau_{n-1} \circ \cdots
    \circ \hat\tau_k\,(\alpha^{(n+1)})\bigr)
  \;=\;
  \mathrm{tr}_k\bigl(\alpha^{(k)}\bigr).
$$

At the base level $k = 0$, $\alpha^{(0)}$ is the mass integrand
$(\int_A \otimes \mathrm{id}) \circ \Delta \circ \varrho_0$ of
the base-level cycle $\varrho_0$. The iterated descended trace
therefore equals the base-level mass:

$$
  \lVert \mathrm{tr}(\hat\tau_n(\alpha^{(n+1)})) \rVert
  \;=\; \lVert \mathrm{tr}_0(\alpha^{(0)}) \rVert
  \;=\; \mathfrak{m}(\varrho_0).
$$

*Step 4 — Independence from $n$.* Step 3 holds for every
$n \ge 0$. The descended norm is therefore a **single
$n$-independent quantity**, namely the level-$0$ base-cycle
mass. In the explicit formula
([mass endomorphism tower](#prop\:mass-endomorphism-tower)):

$$
  \mathfrak{m}(\varrho_0)
  \;=\;
  \Bigl\lvert \textstyle\prod_i \hat V_i^{(0)} \Bigr\rvert,
$$

the right-hand side of which involves only the level-$0$ Hecke
traced volumes. The desc term entering at each jet level is
therefore **the same object**, not a new per-level contribution.
$\square$
