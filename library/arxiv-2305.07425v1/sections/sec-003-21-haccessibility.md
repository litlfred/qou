---
doc_id: arxiv-2305.07425v1
doc_title: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS"
section_id: sec-003-21-haccessibility
section_title: "H–accessibility"
section_number: 2.1
pages: 4-5
source_pdf: 2305.07425v1.pdf
source_sha256: 2f7d2ac5818b6af4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.983
doc_brief: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS — The set of equivalence classes of cobounded actions of a group G on diﬀerent hyperbolic metric spaces carries a natural partial order."
---
[]{#sec:prelim label="sec:prelim"}

In this section, we review the partial order on cobounded group actions introduced in [@ABO19]. Fix a group $G$. If $G$ acts coboundedly on two metric spaces $X$ and $Y$, we say $G\curvearrowright X$ *is dominated by* $G\curvearrowright Y$, written $G\curvearrowright X \preceq G\curvearrowright Y$, if there exists a coarsely $G$--equivariant coarsely Lipschitz map $Y\to X$. The preorder $\preceq$ induces an equivalence relation $G\curvearrowright X\sim G\curvearrowright Y$ if and only if $G\curvearrowright X \preceq G\curvearrowright Y$ and $G\curvearrowright Y \preceq G\curvearrowright X$. It descends to a partial order $\preccurlyeq$ on the set of equivalence classes. We denote the equivalence class of an action by $[G\curvearrowright X]$.

::: defn
Given a group $G$, the *poset of hyperbolic structures on $G$* is defined to be $$\mathcal H(G)\vcentcolon = \{[G\curvearrowright X]\mid G \curvearrowright X \textrm{ is cobounded and } X \textrm{ is hyperbolic}\},$$ equipped with the partial order $\preccurlyeq$.
:::

By [@ABO19 Proposition 3.12], this is equivalent to the original definition of $\mathcal H (G)$ in terms of generating sets. We say that an element of a poset is *largest* when it is greater than or equal to every other element of the poset. Such an element is unique.

::: defn
A group $G$ is *$\mathcal{H}$--accessible* if the poset $\mathcal{H}(G)$ has a largest element. Otherwise, it is *$\mathcal{H}$--inaccesible*.
:::

The following lemma gives a simple criterion to check if a group is $\mathcal{H}$--inaccessible.

::: lem
[]{#lem:key label="lem:key"} Let $G$ be a group. Suppose that there are commuting elements $a, b \in G$ and hyperbolic actions $G \curvearrowright X$ and $G \curvearrowright Y$ such that

1.  $a$ acts loxodromically and $b$ acts elliptically in the action $G \curvearrowright X$; and

2.  $b$ acts loxodromically in the action $G \curvearrowright Y$.

Then there does not exist a hyperbolic action $G\curvearrowright Z$ such that $G \curvearrowright X \preceq G \curvearrowright Z$ and $G \curvearrowright Y \preceq G \curvearrowright Z$.
:::

We will typically apply this lemma to spaces $X$ and $Y$ that are quasi-isometric to lines. These actions on quasi-lines will be constructed using quasimorphisms, which, in turn, will be constructed using hyperbolic actions of $G$ with very weak proper discontinuity properties (see [@BBF15]).

::: defn
Let $G\curvearrowright X$ be a hyperbolic action and $g\in G$ be loxodromic with fixed points $\{g^{\pm}\}\subset \partial X$. The element $g$ is *WWPD* if the orbit of the pair $(g^+,g^-)$ is discrete in the space $\partial X \times \partial X \setminus \Delta$, where $\Delta=\{(x,x) \mid x\in \partial X\}$ is the diagonal subset. A WWPD element $g$ is *WWPD${}^+$* if any $h\in G$ that stabilizes $\{g^{\pm}\}$ as a *set* also fixes $\{g^{\pm}\}$ pointwise.
:::

The following proposition follows from [@BBF16 Corollary 3.2].

::: prop
[]{#prop1 label="prop1"} Suppose that $G\curvearrowright X$ is a hyperbolic action with a WWPD${}^+$ element $g\in G$. There is a homogeneous quasimorphism $q \colon G \to \mathbb R$ such that $q(g) \neq 0$ and $q(h) =0$ for any element $h \in G$ that acts elliptically on $X$.
:::

Homogeneous quasimorphisms, in turn, give rise to actions on quasi-lines.

::: prop
[]{#prop2 label="prop2"} Let $q \colon G \to \mathbb{R}$ be a non-zero homogeneous quasimorphism. Then there is an action of $G$ on a quasi-line $\mathcal{L}$ such that $q(g) \neq 0$ if and only if $g$ acts loxodromically on $\mathcal{L
}$.
:::
