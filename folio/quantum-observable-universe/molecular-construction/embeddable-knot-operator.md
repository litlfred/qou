**Definition.**
*An **embeddable knot operator** is a knot operator $K$ together with an embedding of its braid into the ambient $3$-manifold, carrying an **overlap weight** $w \in (0, 1]$ determined by the embedding direction relative to the bond axis. Its **binding contribution** is*

$$
  \mathfrak{E}_{\mathrm{bind}}(K) = \mathfrak{E}_0(K)\, w ,
$$

*where $\mathfrak{E}_0(K)$ is the un-embedded channel binding.*

### Axial vs transverse channels

*The embedding direction sorts operators into two classes by their angle to the bond axis:*

- ***Axial*** *($\sigma$-type): the braid runs along the bond axis. Head-on overlap is maximal, so $w = 1$.*
- ***Transverse*** *($\pi$-type): the braid lies in the plane transverse to the bond axis. Lateral overlap is smaller, so $w = w_\perp < 1$.*

*The weight $w_\perp$ is the transverse/axial overlap ratio, fixed per system.*

### Composite binding

*The binding of a composite is the overlap-weighted sum*

$$
  \mathfrak{E}_{\mathrm{bind}}\Bigl(\textstyle\bigcup_i K_i\Bigr) = \sum_i \mathfrak{E}_0(K_i)\, w_i .
$$

*An order-$k$ bond is one axial $\sigma$ channel and $k-1$ transverse $\pi$ channels, with total binding $\mathfrak{E}_0\,\bigl(1 + (k-1)\,w_\perp\bigr)$.*
