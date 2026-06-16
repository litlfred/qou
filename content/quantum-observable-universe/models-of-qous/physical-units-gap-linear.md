**Proposition.** *Let $q \in \mathbb{R}$ with $q \neq 0, 1$, let
$\mathfrak{E}_\times(q) = \tfrac{1}{2}(q - q^{-1})$ be the
[crossing energy](#def:crossing-energy), and let
$\hbar_q = (q-1)/q$.  Then the crossing-energy gap bound
$\Delta_q = \mathfrak{E}_\times(q)\,(q-1)^2$ satisfies the exact
identity*

$$
  \frac{\Delta_q}{\hbar_q^{\,2}}
  \;=\;
  \frac{q\,(q-1)(q+1)}{2},
$$

*so the physically normalised gap vanishes **linearly** in
$h = q - 1$ as $q \to 1$, while the categorical bound $\Delta_q$
itself vanishes cubically.  Both vanish identically at $q = 1$.*

**Proof.** Direct computation:
$\Delta_q / \hbar_q^2
= \tfrac{1}{2}(q - q^{-1})(q-1)^2 \cdot q^2/(q-1)^2
= \tfrac{1}{2}\,q^2\,(q - q^{-1})
= \tfrac{1}{2}\,q\,(q^2 - 1)$. $\square$

The identity separates two rates that are easily conflated: the
archimedean normalisation $1/\hbar_q^2$ in the mass formula buys back
exactly two of the three vanishing orders of $\Delta_q$, no more.  A
mass gap in physical units is therefore a first-order-in-$h$
phenomenon, in agreement with the first-order Reeb coupling
$(1 - q^{-1})$ of the
[categorical Dirac operator](#def:categorical-dirac-operator).  The
identity is verified numerically to fifty digits in the witness
[`q1-mass-gap-probe.witness.json`](../../../computations/q1-mass-gap-probe.witness.json).
