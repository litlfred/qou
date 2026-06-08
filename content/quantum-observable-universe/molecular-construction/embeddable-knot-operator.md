*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). The structure and overlap-weighted sum are generic to any ordered field.*

**Definition.**
*An **embeddable knot operator** is a knot operator $K$ together with an
embedding of its braid into the ambient $3$-manifold, carrying a geometric
**overlap weight** $w \in (0, 1]$ determined by the embedding direction
relative to the Reeb axis. Its **binding contribution** is*

$$
  \mathfrak{E}(K) = \mathfrak{E}_0(K)\, w ,
$$

*where $\mathfrak{E}_0(K)$ is the un-embedded channel binding.*

### Axial vs transverse channels

*The embedding direction sorts operators into two geometric classes:*

- ***Axial*** *($\sigma$-type, Reeb-aligned): the braid runs along the
  bond / Reeb axis; head-on overlap is maximal, so $w = 1$.*
- ***Transverse*** *($\pi$-type, contact-plane): the braid lies in the
  $2$-dimensional contact plane transverse to the Reeb axis; the lateral
  overlap is reduced, so $w = w_\perp < 1$.*

*The weight $w_\perp$ is the transverse/axial overlap ratio — a geometric
property of the embedding (the orbital-overlap integral, per system), not
a fitted constant.*

### Composite binding

*The binding of a composite is the overlap-weighted sum*

$$
  \mathfrak{E}\Bigl(\textstyle\bigcup_i K_i\Bigr) = \sum_i \mathfrak{E}_0(K_i)\, w_i .
$$

*An order-$k$ bond is one axial $\sigma$ channel and $k-1$ transverse
$\pi$ channels, with total binding
$\mathfrak{E}_0\,\bigl(1 + (k-1)\,w_\perp\bigr)$.*

### Cardinality versus energy

*Weighting changes only the energy, never the channel count: every channel
with $w > 0$ is occupied, so the active-set cardinality (the bond order of
[the CO LP dual](#prop:co-lp-dual-binding)) is **independent of the
weights**. The equal-channel model ($w \equiv 1$) overbinds; a physical
$w_\perp < 1$ reduces the total toward the observed dissociation energy.
For the $\sigma + 2\pi$ triple bond the equal-channel total is $1.42\times$
the observed $D_0(\mathrm{N_2})$, while a lateral weight $w_\perp \in
[0.3, 0.7]$ brackets it (witness `embeddable-knot-operator`).*

### Geometric origin (Reeb / contact)

*The overlap weight is grounded in the Reeb embedding: $\sigma$ runs along
the $1$-dimensional Reeb direction and $\pi$ in the $2$-dimensional contact
plane, so $w_\perp$ is the geometric ratio between contact-plane and
Reeb-axis overlap. This identification is an interpretive layer; its
formalization against the Reeb-derivation content is open.*
