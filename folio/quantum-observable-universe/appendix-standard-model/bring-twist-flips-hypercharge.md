**Proposition.** *Let $S_5$ act on charge vectors $y \in \mathbb{Q}^5$ by the sign-twisted relabelling $g\cdot y = \operatorname{sgn}(g)\,(y\circ g^{-1})$, the action of [`prop:strand-charges-are-holomorphic-differentials`](strand-charges-are-holomorphic-differentials.md). Let $Y = (-2,-2,-2,3,3)$ be hypercharge in units of $1/6$. Then:*

1. *Plain relabelling by the colour swap $(01)$ or the isospin swap $(34)$ fixes $Y$.*
2. *Under the twisted action, $(01)\cdot Y = (34)\cdot Y = -Y$, and the even element $(01)(34)$ fixes $Y$. So $S_3\times S_2$ acts on the line $\mathbb{Q}Y$ by its sign character.*
3. *A vector fixed by the twisted action of $(01)$ and $(12)$ is zero.*

*Proof.* Each statement is checked componentwise. For 3, invariance under $(01)$ gives $y_2 = y_3 = y_4 = 0$ and $y_0 = -y_1$, and invariance under $(12)$ gives $y_0 = -y_0$. $\square$

**Consequence.** If the strand charges carry Bring's $H^0(K)$ rather than the standard representation, the colour and isospin symmetries exchange $Y$ and $-Y$. The sign of hypercharge is then not invariant data of the $S_3\times S_2$-module, and choosing it breaks the symmetry to the even subgroup. So the twisted $S_3\times S_2$ action cannot be the source of the sign in [`prop:chirality-sign-is-hypercharge-sign`](chirality-sign-is-hypercharge-sign.md). Other upstream sources are not excluded, and the sign stays open.
