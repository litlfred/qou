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

## Lean formalization

The companion Lean states `physical_units_gap_linear` and `gap_bound_vanishes_at_one`; the elementary algebraic discharge (`field_simp; ring`) is deferred via `sorry` (`-- Ref: [manuscript]`).
