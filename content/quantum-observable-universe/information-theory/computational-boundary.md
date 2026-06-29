*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

Let $\mathcal{R}^{\circ}(L, q)$ be the polynomial observable
subcategory of the resolution tree
([polynomial observable subcategory](#def:polynomial-observable-subcategory)).

**Definition.**
The **computational boundary** is the frontier

$$
  \mathcal{H}_c(L, q)
  = 
  \overline{\mathcal{R}^{\circ}}
  \setminus
  \mathcal{R}^{\circ},
$$

equivalently the vanishing locus of the computational
horizon ideal:

$$
  \mathcal{H}_c(L, q)
  = 
  V\!\bigl(\mathfrak{h}_c\bigr),
  \qquad
  \mathfrak{h}_c
  = 
  \bigl\{
    s \in \Gamma\bigl(\mathcal{R}, A_0^{\mathrm{comp}}\bigr)
     : 
    s\big|_{\mathcal{H}_c} = 0
  \bigr\}.
$$

This is the locus in the resolution tree where every
polynomial-time degree-$0$ section vanishes — the exact
analog of the jet horizon
$\mathcal{H} = V(\mathfrak{h})$
([jet horizon](#def:jet-horizon)), with the brane tower
replaced by the resolution tower and the Frobenius algebra
replaced by the Iwahori--Hecke algebra.
