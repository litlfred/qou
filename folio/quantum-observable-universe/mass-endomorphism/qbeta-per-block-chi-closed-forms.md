# Per-block character closed forms and antipode pairing

For all $q > 0$, the per-block characters over $H_3(q)$ take the exact rational forms:

$$
  \chi_{(3)}(\Delta_{T_\beta})(q)
  \;=\; -\frac{(q^2 - 1)(q^2 + 1)^2}{4q},
$$
$$
  \chi_{(2,1)}(\Delta_{T_\beta})(q)
  \;=\; \frac{(q^2 - 1)(q^4 + 1)\,P(q)}{4q^{9}},
  \qquad
  P(q) = 2q^{12} - 5q^{10} + 5q^{8} - 5q^{6} + 5q^{4} - 5q^{2} + 2,
$$
$$
  \chi_{(1,1,1)}(\Delta_{T_\beta})(q)
  \;=\; -\frac{(q^2 - 1)(q^2 + 1)^2}{4q^5}.
$$

**Only $\chi_{(2,1)}$ depends on the order in which the two nucleon strands are braided, and it is the only two-dimensional block.** In $V_{(3)}$ and $V_{(1,1,1)}$ the generators act by scalars, so they commute and the intra-nucleon ordering cannot reach those characters: the two orderings give literally the same rational function there. In $V_{(2,1)}$ the generators do not commute, and the character moves. The forms above are those of the canonical borromean word $(\sigma_0\sigma_1^{-1})^3$; the grouped word — all $\sigma_0$ crossings, then all $\sigma_1$ — gives $(q^2-1)(-q^4-1)/(4q^3)$ instead, and the two are related by

$$
  q^{6}\,\chi_{(2,1)}^{\mathrm{bor}}(q)
  \;=\; -P(q)\,\chi_{(2,1)}^{\mathrm{grp}}(q).
$$

Since $P(1) = -1$, the two frames **agree at the classical point**, so everything resting on the vanishing below is independent of the ordering. $P$ is palindromic, $q^{12}P(1/q) = P(q)$ — a consistency check that appeals to no numerical anchor.

Each block vanishes at the classical point $q = 1$. The antipode pairing relates the sign and trivial representations for all $q > 0$:

$$
  \chi_{(1,1,1)}(\Delta_{T_\beta})(q)
  \;=\; q^{-4} \chi_{(3)}(\Delta_{T_\beta})(q).
$$

