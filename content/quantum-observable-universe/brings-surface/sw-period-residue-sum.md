Let $\mathcal{S}_c \cong \mathbb{P}^1(\mathbb{C})$ be the exceptional divisor at a branch point $z_c$ ([Bring's surface smoothness](#rem:brings-smoothness)). Let $\lambda_{\mathrm{SW}}^{(n)}$ be the $n$-th prolonged Seiberg--Witten differential of the [MI--SW abelianisation](#prop:mi-sw-abelianisation), a meromorphic $1$-form with poles only at the branch points. Let $\gamma$ be a cycle enclosing a subset $E$ of those poles. Then

$$
\oint_{\gamma}\lambda_{\mathrm{SW}}^{(n)}
\;=\;
2\pi i \sum_{p\,\in\,E}\mathrm{Res}_p\,\lambda_{\mathrm{SW}}^{(n)}.
$$

**The enclosed set $E$ is part of the claim, not a bookkeeping detail** (corrected 2026-08-29, bean `qou-6v5l`). This statement previously ranged the sum over *all* $p \in \mathcal{S}_c$ and justified it as "the residue theorem on the compact Riemann surface". That is backwards: on a **compact** surface the residue theorem says the residues of a meromorphic $1$-form **sum to zero**, so summing over every pole would force $a_D^{(n)} = 0$ at every jet level — see `QOU.Brings.period_eq_zero_of_total_residue_vanishes`. Relatedly, $\mathbb{P}^1(\mathbb{C})$ has $H_1 = 0$ and so has no generating cycle for a period to be taken over; only a *bounding* cycle has a residue-sum value at all. Identifying $E$ — which poles the prolongation's contour actually encloses — is open, and is the geometric content the keystone `conj:sw-prolongation-period-eq-mean-qdim` still needs.

In particular, the prolonged Seiberg--Witten period $a_D^{(n)} = \oint_{\mathcal{S}_c}\lambda_{\mathrm{SW}}^{(n)}$ functions as an **algebraic residue sum**. We evaluate it by collecting the local residues at the branch-point poles; no contour integration is required.

**Residue support and body order.** The branch-point poles support the residues. The vertical (jet) degree $n$ governs the number of contributing poles. The $n$-th prolongation lifts the connection to the $n$-jet bundle $J^n E$, so the weight data of rank $n$ indexes the residue family at level $n$. The residue sum therefore carries the **body-order grading**. The period at vertical degree $n$ yields the $n$-body contribution. Each residue constitutes a per-block quantum-dimensional weight on the Wedderburn decomposition restricted to that level.
