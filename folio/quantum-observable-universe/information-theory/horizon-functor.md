Let $\mathrm{Bun}^{\circ}(\mathbb{P}(V))$ be the observable subcategory, and let $\pi_0(\mathrm{Bun}^{\circ})$ be its set of connected components (the [aeons](#def:aeon)). The **horizon functor** is the map

$$
  \partial \colon 
  \pi_0\!\bigl(\mathrm{Bun}^{\circ}(\mathbb{P}(V))\bigr)
  \longrightarrow 
  \mathcal{P}\!\bigl(
    \mathrm{Bun}(\mathbb{P}(V))
    \setminus
    \mathrm{Bun}^{\circ}(\mathbb{P}(V))
  \bigr)
$$

sending each aeon $\mathcal{A}$ to its boundary, the set of configurations $\mathcal{S}$ that appear as limits of diagrams in $\mathcal{A}$ but have $A_0|_{\mathcal{S}} = 0$:

$$
  \partial(\mathcal{A})
  = 
  \bigl\{
    \mathcal{S} \in \mathrm{Bun} \setminus \mathrm{Bun}^{\circ}
    : 
    \mathcal{S} = \varinjlim D
    \text{ for some directed diagram } D \subset \mathcal{A}
  \bigr\}.
$$
