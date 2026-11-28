**Proposition.** *Let $c$ be the central orientation-reversing isometry of Bring's surface, so the isometry group is $S_5\times C_2$ and $H^1 = [2,1,1,1]^+ \oplus [2,1,1,1]^-$ ([`prop:bring-reflection-parity`](../brings-surface/bring-reflection-parity.md)). On the copy $\varepsilon \in \{+1,-1\}$ let $(g, c^k)$ act on charge vectors by $(g,c^k)\cdot y = \varepsilon^k \operatorname{sgn}(g)\,(y\circ g^{-1})$. Let $Y = (-2,-2,-2,3,3)$. Then:*

1. *In the $+$ copy, $(01)$ and $(34)$ send $Y$ to $-Y$, with or without $c$.*
2. *In the $-$ copy, $((01),c)$, $((34),c)$ and $((01)(34),1)$ fix $Y$.*
3. *In the $-$ copy, $c$ sends $Y$ to $-Y$.*

*Proof.* Combine $(01)\cdot Y = (34)\cdot Y = -Y$ and $(01)(34)\cdot Y = Y$ under the sign-twisted action ([`prop:bring-twist-flips-hypercharge`](bring-twist-flips-hypercharge.md)) with the factor $\varepsilon^k$. $\square$

**Consequence.** Requiring hypercharge to keep its colour and isospin symmetry, with each odd permutation paired with $c$, selects the reflection-odd copy. In that copy, reversing the orientation of Bring's surface reverses the sign of hypercharge. So the open sign of [`prop:chirality-sign-is-hypercharge-sign`](chirality-sign-is-hypercharge-sign.md) is the orientation of Bring's surface, the choice of complex structure $H^0(K)$ against its conjugate. This does not fix the value of the sign, because the two orientations are isometric. The statements hold for all twelve elements of $S_3\times S_2$, which is exactly the stabiliser of $Y$ among the $120$ permutations.
