## Proof

The slot indices $1, 3, 5$ are pairwise far apart. Thus $\sigma_1, \sigma_3, \sigma_5$ pairwise commute. Consequently, the subalgebra $\mathcal{A}_{\mathrm{slot}} = \langle \sigma_1, \sigma_3, \sigma_5 \rangle$ is commutative. Every commutator $\lbrack x, y \rbrack = xy - yx$ vanishes for $x, y \in \mathcal{A}_{\mathrm{slot}}$. The three carriers $W \leftrightarrow \sigma_1^{4}$, $Z \leftrightarrow \sigma_3^{6}$, $H \leftrightarrow \sigma_5^{8}$ pairwise commute.

The obstruction is the incompatibility of two facts:

1. **Commuting operators have vanishing bracket.** For $x, y \in \mathcal{A}_{\mathrm{slot}}$, $\lbrack x, y \rbrack = 0$.
2. **The $\mathfrak{su}(2)_L$ adjoint is non-abelian.** Its generators satisfy $\lbrack J_a, J_b \rbrack = \varepsilon_{abc} J_c \ne 0$. A nonzero bracket forbids commutation.

If both $J_1, J_2 \in \mathcal{A}_{\mathrm{slot}}$, then $\lbrack J_1, J_2 \rbrack = 0$ by (1), contradicting $J_3 \ne 0$ by (2). At least one $\mathfrak{su}(2)_L$ generator must escape the slot subalgebra. $\square$
