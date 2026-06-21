*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). The structure and overlap-weighted sum are generic to any ordered field.*

**Definition.**
*An **embeddable knot operator** is a knot operator $K$ together with an
embedding of its braid into the ambient $3$-manifold, carrying an
**overlap weight** $w \in (0, 1]$ determined by the embedding direction
relative to the bond axis. Its **binding contribution** is*

$$
  \mathfrak{E}(K) = \mathfrak{E}_0(K)\, w ,
$$

*where $\mathfrak{E}_0(K)$ is the un-embedded channel binding.*

### Axial vs transverse channels

*The embedding direction sorts operators into two classes by their angle
to the bond axis:*

- ***Axial*** *($\sigma$-type): the braid runs along the bond axis;
  head-on overlap is maximal, so $w = 1$.*
- ***Transverse*** *($\pi$-type): the braid lies in the plane transverse
  to the bond axis; the lateral overlap is smaller, so $w = w_\perp < 1$.*

*The weight $w_\perp$ is the transverse/axial overlap ratio — the
orbital-overlap integral for the embedding, fixed per system; it is not a
fitted constant.*

### Composite binding

*The binding of a composite is the overlap-weighted sum*

$$
  \mathfrak{E}\Bigl(\textstyle\bigcup_i K_i\Bigr) = \sum_i \mathfrak{E}_0(K_i)\, w_i .
$$

*An order-$k$ bond is one axial $\sigma$ channel and $k-1$ transverse
$\pi$ channels, with total binding
$\mathfrak{E}_0\,\bigl(1 + (k-1)\,w_\perp\bigr)$ (Lean: `multipleBond_binding`).*

### Cardinality versus energy

*Overlap weighting changes only the energy, never the channel count:
every channel with $w > 0$ is occupied, so the active-set cardinality —
the bond order of [the CO LP dual](#prop:co-lp-dual-binding) — is
independent of the weights (Lean: `multipleBond_length`). The
equal-channel model ($w \equiv 1$) overbinds: for the $\sigma + 2\pi$
triple bond it gives $1.42\times$ the observed $D_0(\mathrm{N_2})$, while
a lateral weight $w_\perp \in [0.3, 0.7]$ brackets it (witness
`embeddable-knot-operator`).*

### Spatial-dimension bound

*Each channel embeds as a direction in the ambient $3$-space, with distinct
channels mutually orthogonal. Orthogonal nonzero vectors are linearly
independent, so their number cannot exceed
$\dim_{\mathbb{R}} \mathbb{R}^3 = 3$: at most three mutually-orthogonal
channels embed — one axial $\sigma$ and two transverse $\pi$. Hence the
bond order is bounded by the spatial dimension, so **no $p$-block bond
exceeds order three**. This bound is formalised in Lean as the theorem
`orthogonal_channels_le_dim` (pairwise-orthogonal nonzero vectors in a
space of finrank $3$ number at most $3$).*
