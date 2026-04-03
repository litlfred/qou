Let $\mathrm{Bun}^{\circ}(\mathbb{P}(V))$ be the observable
subcategory
([observable subcategory](#def:observable-subcategory))
and let $\pi_0(\mathrm{Bun}^{\circ})$ denote its set of
connected components (the aeons, [aeon](#def:aeon)).

The **horizon functor** is the map

$$
  \partial \;\colon\;
  \pi_0\!\bigl(\mathrm{Bun}^{\circ}(\mathbb{P}(V))\bigr)
  \;\longrightarrow\;
  \mathcal{P}\!\bigl(
    \mathrm{Bun}(\mathbb{P}(V))
    \setminus
    \mathrm{Bun}^{\circ}(\mathbb{P}(V))
  \bigr)
$$

that sends each aeon $\mathcal{A}$ to its **boundary** — the
set of configurations $\mathcal{S}$ that are limits of diagrams
in $\mathcal{A}$ but have $A_0|_{\mathcal{S}} = 0$:

$$
  \partial(\mathcal{A})
  \;=\;
  \bigl\{\,
    \mathcal{S}
    \in \mathrm{Bun} \setminus \mathrm{Bun}^{\circ}
    \;:\;
    \mathcal{S} = \varinjlim\, D
    \text{ for some directed diagram }
    D \subset \mathcal{A}
  \,\bigr\}.
$$

Each element of $\partial(\mathcal{A})$ is a jet horizon
([jet horizon](#def:jet-horizon)).

**Functoriality.**
If $\mathcal{A} \hookrightarrow \mathcal{A}'$ is an inclusion
of connected components (i.e.\ $\mathcal{A} = \mathcal{A}'$,
since connected components are maximal), then $\partial$ acts
as the identity.  The non-trivial content is for adjacent
aeons: if $\mathcal{A}$ and $\mathcal{A}'$ are adjacent
([aeon adjacency](#def:aeon)), then
$\partial(\mathcal{A}) \cap \partial(\mathcal{A}') \neq \varnothing$
and the shared boundary objects are the loci where the CCC
transition occurs.

**Relation to the torsion flow.**
The torsion flow $\Phi_t^q$
([torsion-driven knot flow](#def:torsion-knot-flow)) is an
endofunctor of $\mathrm{Bun}(\mathbb{P}(V))$.  Within an aeon,
$\Phi_t^q$ restricts to an endofunctor of $\mathrm{Bun}^{\circ}$
(it preserves $A_0 \neq 0$).  The horizon $\partial(\mathcal{A})$
is the set of fixed points of the limiting behaviour
$\Phi_t^q \to \partial$ as $t$ approaches the aeon boundary.
