*For the torus knot $T_{m,p}$ presented on the minimal number of strands (that is, with $m \leq p$, so that $m$ is the braid index by Morton–Williams; see [the box-braid irreducibility proof](#prop:box-braid-irreducibility)), the [top-channel decoration](#def:torus-knot-top-channel-decoration) is $h$ times the quantum integer at the writhe $w = (m-1)p$:*

$$
  \delta^{\mathrm{top}}_q(T_{m,p}) \;=\; q^{w} - q^{-w} \;=\; h\,[w]_q.
$$

By definition the decoration is the bar-odd part of the top-channel twist $q^{w}$; the content of the statement is the factorisation $q^{w} - q^{-w} = h\,[w]_q$. The writhe exponent governs the $h\,[w]_q$ form across all torus knots, matching the $10_{124} = T_{3,5}$ and $8_{19} = T_{3,4}$ force-carrier evaluations.

**The minimal-strand condition is not cosmetic.** $T_{m,p} \cong T_{p,m}$ as knots, but $(m-1)p \neq (p-1)m$ whenever $m \neq p$: the trefoil read as $T_{2,3}$ gives $w = 3$ and read as $T_{3,2}$ gives $w = 4$; $10_{124}$ gives $10$ or $12$. Without the condition the statement would assign two different $\delta_q$ to the same knot. This is the general fact that the writhe is not a link invariant, specialised to the torus family. Fixing the braid index is exactly the framework's "evaluate at the lowest level of the tower", and the compute already presents every force carrier with $m < p$, so no evaluated number changes. As a consistency check, $(w - m) \bmod 2$ (the level-pair parity invariant) agrees across both presentations of each carrier, while $w$ alone does not.
