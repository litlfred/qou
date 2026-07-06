**Definition.**
*An **embeddable knot operator** couples a knot operator $K$ with an embedding of its braid into the ambient $3$-manifold. The embedding determines an overlap weight $w \in (0, 1]$ based on its direction relative to the bond axis. Its binding contribution is:*

$$
  \mathfrak{E}(K) = \mathfrak{E}_0(K)\, w
$$

*where $\mathfrak{E}_0(K)$ is the un-embedded channel binding.*

The embedding direction sorts operators into two classes by their angle to the bond axis. Axial channels ($\sigma$-type) run along the bond axis; their head-on overlap is maximal, setting $w = 1$. Transverse channels ($\pi$-type) lie in the plane perpendicular to the bond axis; their lateral overlap is smaller, setting $w = w_\perp < 1$. The weight $w_\perp$ is the transverse-to-axial overlap ratio (the orbital-overlap integral for the embedding), fixed per system rather than acting as a fitted constant.

The binding of a composite is the overlap-weighted sum:

$$
  \mathfrak{E}\Bigl(\textstyle\bigcup_i K_i\Bigr) = \sum_i \mathfrak{E}_0(K_i)\, w_i
$$

An order-$k$ bond consists of one axial $\sigma$ channel and $k-1$ transverse $\pi$ channels. Its total binding is $\mathfrak{E}_0\,\bigl(1 + (k-1)\,w_\perp\bigr)$ (Lean: `multipleBond_binding`).
