**Proposition.** Label a state of several strands of $5 = C \oplus V$ by the subset
$S \subseteq \{0,\dots,4\}$ of strands it carries, read as the wedge $e_S \in \Lambda^{|S|} K^5$.
Let $y$ be a diagonal charge with $\sum_i y_i = 0$ and $y_S = \sum_{i \in S} y_i$. Then

1. the even part $\Lambda^0 \oplus \Lambda^2 \oplus \Lambda^4$ has $1 + 10 + 5$ states and no
   state of degree $1$; the odd part $\Lambda^1 \oplus \Lambda^3 \oplus \Lambda^5$ has
   $5 + 10 + 1$ and no state of degree $4$;
2. $S \mapsto S^c$ is a bijection from the even part to the odd part, and
   $y_{S^c} = -y_S$; in particular the degree-$4$ state missing $j$ has charge $-y_j$;
3. $\sum_{|S| \text{ even}} y_S = 0$ and $\sum_{|S| \text{ even}} y_S^3 = 0$, and the same
   for the odd part.

With $y = Q(\alpha) = T_3 + \alpha Y_0$, the even part is
$1 \oplus \Lambda^2 5 \oplus \bar 5$: one generation and a singlet, the $\mathrm{Spin}(10)$
spinor of \cite{baez-huerta2010}. The odd part is its charge conjugate.

**Proof.** Items 1 and 2 (the bijection) are finite checks over the $32$ subsets. For the
charge, $y_S + y_{S^c} = \sum_i y_i = 0$. Item 3 follows from item 2 and the odd-part
identities $\sum_{|S|\text{ odd}} y_S = 8 p_1$ and
$\sum_{|S|\text{ odd}} y_S^3 = p_1(2p_1^2 + 6p_2)$, with $p_1 = \sum_i y_i$ and
$p_2 = \sum_i y_i^2$. $\square$

**Scope.** Each part contains exactly one of $\Lambda^1 = 5$ and $\Lambda^4 \cong \bar 5$, so
neither contains a vector-like $5 \oplus \bar 5$. With odd strands, a two-strand state is a
wedge, which is the Fermi channel of
[`prop:hecke-sign-channel-is-fermi`](hecke-sign-channel-is-fermi.md). The $\mathbb{Z}/2$
grading by strand count is free. Two things are still inputs: that strands are odd, and the
sign that takes the even part (rather than the odd part) as matter.
