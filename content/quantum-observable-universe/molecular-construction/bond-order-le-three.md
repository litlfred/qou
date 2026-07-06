**Proposition.**
*Each bond channel embeds as a direction in the ambient 3-space, with distinct channels mutually orthogonal. Orthogonal nonzero vectors are linearly independent. Their count cannot exceed $\dim_{\mathbb{R}} \mathbb{R}^3 = 3$. At most three mutually orthogonal channels embed—one axial $\sigma$ and two transverse $\pi$. The spatial dimension therefore bounds the bond order. Consequently, **no $p$-block bond exceeds order three.***

This bound is formalized in Lean via the theorem `orthogonal_channels_le_dim`. It states that pairwise-orthogonal nonzero vectors in a space of `finrank` 3 number at most 3.
