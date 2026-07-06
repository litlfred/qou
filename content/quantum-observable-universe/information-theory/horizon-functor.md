Let $\mathrm{Bun}^{\circ}(\mathbb{P}(V))$ denote the observable subcategory ([observable subcategory](#def:observable-subcategory)). Let $\pi_0(\mathrm{Bun}^{\circ})$ denote its set of connected components (the aeons, [aeon](#def:aeon)).

The **horizon functor** is the map

$$
  \partial \colon 
  \pi_0\!\bigl(\mathrm{Bun}^{\circ}(\mathbb{P}(V))\bigr)
  \longrightarrow 
  \mathcal{P}\!\bigl(
    \mathrm{Bun}(\mathbb{P}(V))
    \setminus
    \mathrm{Bun}^{\circ}(\mathbb{P}(V))
  \bigr).
$$

It sends each aeon $\mathcal{A}$ to its boundary. This boundary comprises configurations $\mathcal{S}$ that appear as limits of diagrams in $\mathcal{A}$ but have $A_0|_{\mathcal{S}} = 0$:

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

Every element of $\partial(\mathcal{A})$ defines a jet horizon ([jet horizon](#def:jet-horizon)).

**Functoriality.**
If $\mathcal{A} \hookrightarrow \mathcal{A}'$ is an inclusion of connected components, then $\mathcal{A} = \mathcal{A}'$ by maximality, and $\partial$ acts as the identity. For adjacent aeons $\mathcal{A}$ and $\mathcal{A}'$ ([aeon adjacency](#def:aeon)), the intersection $\partial(\mathcal{A}) \cap \partial(\mathcal{A}') \neq \varnothing$. These shared boundary objects specify the loci where the CCC transition occurs.

**Relation to the torsion flow.**
The torsion flow $\Phi_t^q$ ([torsion-driven knot flow](#def:torsion-knot-flow)) provides an endofunctor of $\mathrm{Bun}(\mathbb{P}(V))$. Within an aeon, $\Phi_t^q$ restricts to an endofunctor of $\mathrm{Bun}^{\circ}$ (preserving $A_0 \neq 0$). The horizon $\partial(\mathcal{A})$ constitutes the set of fixed points of the limiting behaviour $\Phi_t^q \to \partial$ as $t$ approaches the aeon boundary.
