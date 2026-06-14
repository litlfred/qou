*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
Let $\iota \colon \mathbb{R}_{>0} \to \mathbb{R}_{>0}$ be the bar
involution $\iota(q) = q^{-1}$.  The open interval

$$
  \mathcal{B}  :=  \bigl(1/\varphi^2,\,\varphi^2\bigr)
   \subset  \mathbb{R}_{>0}
$$

is the **maximal connected $\iota$-invariant open subinterval** of
$\mathbb{R}_{>0}$ that excludes both golden nodes
$\{1/\varphi^2,\,\varphi^2\}$
([skew-dual golden node](#prop:golden-skew-dual-node)).
Equivalently, $\mathcal{B}$ is the largest interval on which the
deconfinement criterion $q > 1/\varphi^2$
([deconfinement threshold](#rem:deconfinement-golden-threshold))
and its bar conjugate $q < \varphi^2$ hold simultaneously.

*Proof.*
The fixed point of $\iota$ on $\mathbb{R}_{>0}$ is $q = 1$, lying
in $\mathcal{B}$.  For $a > 0$, the interval $(a, 1/a)$ is
$\iota$-invariant iff $a < 1$ (so that $1/a > a$).  Among intervals
$(a, 1/a)$ contained in $\mathbb{R}_{>0} \setminus \{1/\varphi^2,
\varphi^2\}$, the maximal one is $(1/\varphi^2, \varphi^2)$, since
any larger choice $(a, 1/a)$ with $a < 1/\varphi^2$ would contain
the node $1/\varphi^2$.  Hence $\mathcal{B}$ is maximal. $\square$

**Bar-symmetric phase diagram (replaces three asymmetric tables).**

The single statement $\mathcal{B} = (1/\varphi^2, \varphi^2)$
unifies three previously asymmetric phase tables:

| Side | $q$ regime | Sub-band | Phase | Order parameter |
|------|------------|----------|-------|-----------------|
| sub-classical | $q < 1/\varphi^2$ | below $\mathcal{B}$ | low-density deconfined (QGP) | $\Delta(\mathcal{E}_q) > 0$ |
| classical band | $q \in \mathcal{B}$ | inside $\mathcal{B}$ | confined hadronic | $\Delta(\mathcal{E}_q) < 0$ |
| super-classical | $q > \varphi^2$ | above $\mathcal{B}$ | high-density deconfined (CFL/strangelet limit) | $\Delta(\mathcal{E}_{1/q}) > 0$ |

Both deconfined regimes are governed by the **same** algebraic
threshold $s^2 - s - 1 = 0$ (whose roots are $\varphi$ and
$-1/\varphi$) — applied directly on the super-classical side and
via $\iota$ (giving $s^2 + s - 1 = 0$) on the sub-classical side.

**Two-sided substrate stability margin (consolidated).**

Our universe sits at $q_0 \approx 1.1097 \in \mathcal{B}$, with

$$
  d_-(q_0)  :=  q_0 - 1/\varphi^2 \approx 0.728,
  \qquad
  d_+(q_0)  :=  \varphi^2 - q_0 \approx 1.508.
$$

The bar-image $\iota(q_0) = 1/q_0 \approx 0.901$ also lies in
$\mathcal{B}$, with margins

$$
  d_-\bigl(\iota(q_0)\bigr) \approx 0.519,
  \qquad
  d_+\bigl(\iota(q_0)\bigr) \approx 1.717.
$$

The pair $(q_0, \iota(q_0))$ — substrate and its bar-conjugate —
defines a **bar-orbit** in $\mathcal{B}$.  Confinement statements
that hold at $q_0$ automatically hold at $\iota(q_0)$ by bar-applying
the proof.

**Replaces.**
The asymmetric phase tables in
[golden-ratio degeneration](#rem:golden-ratio-degeneration)
("sub-golden / classical / physical")
and [deconfinement threshold](#rem:deconfinement-golden-threshold)
("$q < q_{\mathrm{gold}}$ / intermediate / confined") are now
two faces of the single bar-symmetric structure
$\mathcal{B} = (1/\varphi^2, \varphi^2)$.
Any future phase-boundary argument should be stated **once for
$\mathcal{B}$** and applied to both endpoints by bar symmetry,
rather than re-derived on each side.


**Remark on Mathematical Novelty:** This formulation collapses three historically disjoint asymmetric phase regimes into a single unified bar-self-dual confinement band. While utilizing standard involution bounds, the structural consolidation is highly novel, offering a rigid phase boundary for the QOU framework.
