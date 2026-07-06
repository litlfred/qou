Let $\mathrm{Bun}(\mathbb{P}(V))$ be the category of finite
bundles over the projective line
([bundle category](#rem:bundle-category)), with objects the
bundle initial conditions
([bundle initial conditions](#def:bundle-initial-conditions))
and morphisms the permutation-isotopy pairs.

The **observable subcategory**
$\mathrm{Bun}^{\circ}(\mathbb{P}(V))$ is the full subcategory
on objects where the degree-$0$ algebra is non-trivial:

$$
  \mathrm{Bun}^{\circ}(\mathbb{P}(V))
  = 
  \bigl\{
    \mathcal{S} \in \mathrm{Bun}(\mathbb{P}(V))
     : 
    \Gamma(\mathcal{S}, A_0) \neq 0
  \bigr\}.
$$

**Observability of the subcategory.**
The observability axioms of the QOU
([observation](#def:observation)) require a non-degenerate
Frobenius pairing to define degree-$0$ measurements.  When
$A_0|_{\mathcal{S}} = 0$, the pairing degenerates on the
lowest floor of the brane tower and no degree-$0$ observable
is well-defined.  The subcategory $\mathrm{Bun}^{\circ}$ is
precisely the regime where the full observational apparatus
functions.

**Complement.**
The complement
$\mathrm{Bun}(\mathbb{P}(V)) \setminus \mathrm{Bun}^{\circ}(\mathbb{P}(V))$
consists of configurations with $A_0 = 0$ — the jet horizons
([jet horizon](#def:jet-horizon)) and big bang states
([big bang state](#def:big-bang-state)).

**Connected components.**
The connected components $\pi_0(\mathrm{Bun}^{\circ})$ are the
aeons ([aeon](#def:aeon)).  Each aeon is a maximal connected
full subcategory of $\mathrm{Bun}^{\circ}$, encompassing all
light cones that can be reached from one another without
crossing a jet horizon.
