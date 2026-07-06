**Proposition (confinement Frobenius reciprocity).**
*Let $T \in H_n(q)$ be a confined bound-state operator selected by the operator-selection LP ([operator-selection LP](#prop:operator-selection-lp)) with primal optimum $T = \sum_i x_i^* b_i$ and dual optimum $(y_0^*, y^*)$. Here, $\{b_1, \ldots, b_d\}$ is the normal form (NF) basis, $G_{ij} = \mathrm{tr}_M(b_i b_j)$ is the Frobenius Gram matrix ([Frobenius Gram matrix](#prop:frobenius-gram-matrix)), and the LP-active set is:*

$$
  A^*(T) \;=\; \{\, i \in \{1, \ldots, d\} \;:\; y_i^* > 0 \,\}.
$$

*For every observable $O \in H_n(q)$, interpreted as a linear functional $b \mapsto \langle O, b\rangle = \mathrm{tr}_M(O \cdot b)$ on the algebra, the physical expectation value of $O$ in the bound state $T$ is the **Gram-inverse dual pairing weighted by LP-active shadow prices**:*

$$
  \boxed{\;
    \langle O \rangle_T
    \;\equiv\;
    O(T)
    \;=\;
    \sum_{i,\,j \,\in\, A^*(T)}
      u_i^*\,(G^{-1})_{ij}\,\langle O,\, b_j\rangle
  \;}
$$

*where $u_i^* = y_i^*$ are the LP shadow prices on the active channels and $(G^{-1})_{ij}$ is the Frobenius dual-basis matrix on the $|A^*(T)|$-dimensional active subspace. Equivalently, in compact notation:*

$$
  \langle O \rangle_T
  \;=\;
  \langle O,\, G^{-1}\,u^*\rangle_{A^*}
  \;=\;
  \langle O,\, T^\vee\rangle,
$$

*where $T^\vee = \sum_{i,j \in A^*} u_i^* (G^{-1})_{ij}\,b_j$ is the **Frobenius dual** of $T$ on the active subspace.*

## Sketch of Proof

The proof has two parts.

**Part 1: Frobenius reciprocity on $H_n(q)$.**
The Markov trace $\mathrm{tr}_M$ is a non-degenerate Frobenius form on $H_n(q)$ ([Frobenius Gram matrix](#prop:frobenius-gram-matrix)). The Frobenius dual $T^\vee$ of any element $T$ is defined by the equation $\langle T^\vee,\, b_j\rangle = x_j^*$ for the NF coefficients of $T$. Solving this linear system on the NF basis gives $T^\vee = \sum_{i,j} x_i^* (G^{-1})_{ij}\, b_j$. Frobenius reciprocity then asserts $\langle O, T\rangle_{\text{phys}} = \langle O, T^\vee\rangle$ for every observable $O$.

**Part 2: LP-active reduction.**
The operator-selection LP ([operator-selection LP](#prop:operator-selection-lp)) yields the primal–dual pair $(x^*, y^*)$ with strong duality $\sum_i t_i x_i^* = n_{\mathrm{target}} y_0^*$. Complementary slackness forces $y_i^* x_i^{(\text{slack})} = 0$ for every $i$. Thus, on the LP-inactive set $\{i : y_i^* = 0\}$, either the constraint is slack and $x_i^*$ is unconstrained, or $x_i^* = 0$. Substituting $x_i^* = (G^{-1} u^*)_i$ on the active set $A^*(T)$ (the precise KKT stationarity condition for the dualised LP) gives the boxed formula.

For binding energy, the observable is the Hamiltonian $O = H$ acting diagonally on the NF basis. In this case, the formula reduces to the known expression in [knot-factor-frobenius-pairing](#conj:knot-factor-frobenius-pairing). That conjecture is therefore the special case $O = H$ of this proposition. Conversely, the same reciprocity governs any other bound-state observable.
