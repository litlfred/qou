The archimedean normalisation $1/\hbar_q^2$ in the mass formula cancels exactly two of the three vanishing orders of $\Delta_q$. This separates two distinct rates and leaves a physical-units mass gap at first order in $h$.

**Proof.** Direct computation:
$\Delta_q / \hbar_q^2
= \tfrac{1}{2}(q - q^{-1})(q-1)^2 \cdot q^2/(q-1)^2
= \tfrac{1}{2}\,q^2\,(q - q^{-1})
= \tfrac{1}{2}\,q\,(q^2 - 1)$. $\square$

A mass gap in physical units is therefore a first-order phenomenon in $h$. This agrees with the first-order Reeb coupling $(1 - q^{-1})$ of the [categorical Dirac operator](#def:categorical-dirac-operator). We verify this identity numerically to fifty digits in [`q1-mass-gap-probe.witness.json`](../../../computations/q1-mass-gap-probe.witness.json).
