**Proposition.** *For a strand $i$, let $\mathrm{Stab}(i) \cong S_4$ be its stabiliser in $S_5$ and $\mathrm{Alt}(i) = \mathrm{Stab}(i)\cap A_5 \cong A_4$. Then:*

1. *$g\,\mathrm{Stab}(i)\,g^{-1} = \mathrm{Stab}(g i)$ and $g\,\mathrm{Alt}(i)\,g^{-1} = \mathrm{Alt}(g i)$, so the strands are permuted exactly as these subgroups of $\mathrm{Aut}^+(B) = S_5$.*
2. *Under the sign-twisted action on charges, the strand vector $u_i = 5e_i - (1,\dots,1)$ is fixed by $\mathrm{Alt}(i)$ and negated by the odd elements of $\mathrm{Stab}(i)$.*
3. *A traceless charge vector fixed by $\mathrm{Alt}(0)$ is a multiple of $u_0$.*

*Proof.* Part 1: $(g h g^{-1})(g i) = g(h i)$, and conjugation preserves the sign. Parts 2 and 3 are checked over all elements, and by solving the invariance equations for the 3-cycles $(123)$ and $(234)$. $\square$

**Consequence.** By Chevalley–Weil, $\dim H^0(K)^H$ is the genus of $B/H$; $B/A_4$ is a torus and $B/S_4$ a sphere ([`prop:bring-harmonic-types`](../brings-surface/bring-harmonic-types.md)). With [`prop:strand-charges-are-holomorphic-differentials`](strand-charges-are-holomorphic-differentials.md), strand $i$ is the holomorphic differential pulled back from the elliptic quotient $B\to B/\mathrm{Alt}(i)$. The five strands are the five elliptic quotients of Bring's surface, permuted as the strands are. That the physical strands are these quotients is a modelling identification. It is unique up to isomorphism, because every transitive five-point $S_5$-set is the natural one ([`prop:index-five-subgroups-are-point-stabilisers`](index-five-subgroups-are-point-stabilisers.md); its point stabilisers have index five, so it is $S_5/\mathrm{Stab}(i)$).
