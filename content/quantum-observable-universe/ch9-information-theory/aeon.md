Let $\mathrm{Bun}(\mathbb{P}(V))$ be the category of finite
bundles over the projective line
([bundle category](#rem:bundle-category)), and let
$A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$
be the brane tower
([jet prolongation](#prop:jet-prolongation)).

**The observable subcategory.**
Define the **observable subcategory**
$\mathrm{Bun}^{\circ}(\mathbb{P}(V))$ as the full subcategory
of $\mathrm{Bun}(\mathbb{P}(V))$ on objects $\mathcal{S}$ for
which the degree-$0$ algebra is non-trivial:

$$
  \mathrm{Ob}\bigl(\mathrm{Bun}^{\circ}\bigr)
  \;=\;
  \bigl\{\,
    \mathcal{S} \in \mathrm{Bun}(\mathbb{P}(V))
    \;:\;
    \Gamma(\mathcal{S},\, A_0) \neq 0
  \,\bigr\}.
$$

This is the subcategory where degree-$0$ observations are
well-defined — where the Frobenius pairing is non-degenerate
on $A_0$.

**Definition.**
An **aeon** is a connected component of
$\mathrm{Bun}^{\circ}(\mathbb{P}(V))$.

Concretely, an aeon $\mathcal{A}$ is a maximal full subcategory
of $\mathrm{Bun}^{\circ}$ such that any two objects $\mathcal{S}$,
$\mathcal{S}'$ in $\mathcal{A}$ are connected by a zigzag of
morphisms (flow maps, inclusions, or their inverses) that stays
entirely within $\mathrm{Bun}^{\circ}$.  Each light cone is a
directed diagram within the aeon; the aeon is the union of all
light cones that can be connected without crossing a jet horizon
([jet horizon](#def:jet-horizon)).

**Boundary.**
The **boundary** $\partial\mathcal{A}$ of an aeon is the set of
objects $\mathcal{S} \in \mathrm{Bun}(\mathbb{P}(V))$ that are
limits of diagrams in $\mathcal{A}$ but do not themselves lie in
$\mathrm{Bun}^{\circ}$:

$$
  \partial\mathcal{A}
  \;=\;
  \overline{\mathcal{A}} \setminus \mathcal{A}^{\circ}
  \;\subset\;
  \bigl\{\,
    \mathcal{S} : \Gamma(\mathcal{S}, A_0) = 0
  \,\bigr\}.
$$

Each boundary object is a jet horizon or a big bang state
([big bang state](#def:big-bang-state)).  The **boundary datum**
at $\mathcal{S} \in \partial\mathcal{A}$ is the colimit of the
degree $\geq 1$ data over all diagrams in $\mathcal{A}$
approaching $\mathcal{S}$:

$$
  \mathrm{CMB}(\partial\mathcal{A})
  \;=\;
  \varinjlim_{\mathcal{S}' \to \mathcal{S}}
  \bigl(A_1/A_0 \oplus A_2/A_0\bigr)\big|_{\mathcal{S}'}
$$

([CMB boundary datum](#def:cmb-boundary-datum)).

**Aeon adjacency.**
Two aeons $\mathcal{A}$ and $\mathcal{A}'$ are **adjacent** if
their boundaries share a common object:
$\partial\mathcal{A} \cap \partial\mathcal{A}' \neq \varnothing$.
The shared boundary object is simultaneously the terminal horizon
of one aeon and the initial configuration of the next.

**Maximality.**
The connected-component definition automatically gives maximality:
no larger subcategory of $\mathrm{Bun}^{\circ}$ containing
$\mathcal{A}$ is connected.  This avoids the need for an
explicit interval $(a, b) \subset \mathbb{Z}$ — the aeon is
defined over the full structure of the category, encompassing
all intersecting light cones.
