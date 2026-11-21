**Conjecture (conditional on stationarity).** *Let $T \in H_n(q)$ be a confined bound-state operator selected by the operator-selection LP with primal optimum $T = \sum_i x_i^* b_i$ and dual optimum $(y_0^*, y^*)$. Here, $\{b_1, \ldots, b_d\}$ is the normal form basis, $G_{ij} = \mathrm{tr}_M(b_i b_j)$ is the Frobenius Gram matrix, and the LP-active set is:*

$$
  A^*(T) \;=\; \{\, i \in \{1, \ldots, d\} \;:\; y_i^* > 0 \,\}.
$$

*For every observable $O \in H_n(q)$, the physical expectation value of $O$ in the bound state $T$ is the **Gram-inverse dual pairing weighted by LP-active shadow prices**:*

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

*where $u_i^* = y_i^*$ are the LP shadow prices on the active channels and $(G^{-1})_{ij}$ is the Frobenius dual-basis matrix on the $|A^*(T)|$-dimensional active subspace. Equivalently:*

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
The Markov trace $\mathrm{tr}_M$ is a non-degenerate Frobenius form on $H_n(q)$. The Frobenius dual $T^\vee$ of any element $T$ is defined by $\langle T^\vee,\, b_j\rangle = x_j^*$. Solving this linear system gives $T^\vee = \sum_{i,j} x_i^* (G^{-1})_{ij}\, b_j$. Frobenius reciprocity asserts $\langle O, T\rangle_{\text{phys}} = \langle O, T^\vee\rangle$.

**Part 2: LP-active reduction.**
The operator-selection LP yields the primal–dual pair $(x^*, y^*)$ with strong duality $\sum_i t_i x_i^* = n_{\mathrm{target}} y_0^*$. Complementary slackness forces $y_i^* x_i^{(\text{slack})} = 0$ for every $i$. Substituting $x_i^* = (G^{-1} u^*)_i$ on the active set $A^*(T)$ gives the boxed formula.

**The open step.** The substitution $x_i^* = (G^{-1} u^*)_i$ on $A^*(T)$, with $x_i^* = 0$ off it, is not a consequence of the linear program. The optimality conditions of a linear program are feasibility and complementary slackness; $x^* = G^{-1} u^*$ is the stationarity condition of a quadratic program. Granting that stationarity, together with the linearity $\langle O \rangle_T = \sum_j x_j^* \langle O, b_j \rangle$ and the symmetry of $G^{-1}$, the boxed formula follows, as do $i \in A^*(T) \Leftrightarrow u_i^* > 0$ and $A^*(T) \neq \emptyset$ for a nonzero optimum. Strong duality for this program is part of [LP dual stability](#prop:lp-dual-stability).
