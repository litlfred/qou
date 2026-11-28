**Proposition.** *Let $S_5$ act on charge vectors $y \in \mathbb{Q}^5$ with $\sum_i y_i = 0$ by permuting the five strands. This is the standard representation $[4,1]$, with character $\chi_{[4,1]}(g) = \#\{i : g(i) = i\} - 1$. The space of holomorphic differentials on Bring's surface, $H^0(B, K) = [2,1,1,1]$, has character*

$$
\chi_{H^0(K)}(g) = \operatorname{sgn}(g)\,\bigl(\#\{i : g(i) = i\} - 1\bigr)
$$

*on every conjugacy class. So $H^0(B, K) \cong [4,1] \otimes \operatorname{sgn}$ is the traceless strand charge space twisted by the sign character. The only $4$-dimensional irreducibles of $S_5$ are $[4,1]$ and $[2,1,1,1]$. If the traceless charges on $n$ strands have the dimension of $H^0(B,K)$, then $n - 1 = 4$, so $n = 5$.*

*Proof.* The character of $H^1(B)$ is $2\chi_{[2,1,1,1]}$, by the Hopf trace formula on the cells of Bring's map ([`prop:bring-harmonic-types`](../brings-surface/bring-harmonic-types.md)). Hodge theory gives $H^1 = H^0(K) \oplus \overline{H^0(K)}$, and the characters are real, so $\chi_{H^0(K)} = \chi_{[2,1,1,1]}$. The identity $\chi_{[2,1,1,1]} = \operatorname{sgn}\cdot\chi_{[4,1]}$ and the fixed-point count are checked on the seven class representatives $1, (01), (01)(23), (012), (012)(34), (0123), (01234)$. The dimension list of the seven irreducibles is $1, 1, 4, 4, 5, 5, 6$. $\square$

**Scope.** This shows the two $S_5$-modules agree up to the sign character. It does not show that relabelling strands *is* an automorphism of Bring's surface. It also does not identify the sign twist with the open hypercharge sign of [`prop:chirality-sign-is-hypercharge-sign`](chirality-sign-is-hypercharge-sign.md): the twist is the sign of a strand permutation, and the open sign is which parity of strand subsets is matter. It replaces the bare hypothesis $n - 1 = g$ in [`prop:strand-count-from-bring`](strand-count-from-bring.md) with a statement about the $S_5$-module.
