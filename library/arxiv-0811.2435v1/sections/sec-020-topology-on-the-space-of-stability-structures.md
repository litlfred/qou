---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-020-topology-on-the-space-of-stability-structures
section_title: "Topology on the space of stability structures"
section_number: null
pages: 56-60
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.995
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 51 sections: Front matter; Introduction; Counting problems for 3-dimensiona"
---
Let $\CC$ be an ind-constructible weakly unital $\A$-category over a field $\k$ of arbitrary characteristic. Let $\op{cl}: Ob(\CC)\to \Gamma\simeq \Z^n$ be a map of ind-constructible sets (where $\Gamma$ is considered as a countable set of points) such that the induced map $Ob(\CC)(\overline{\k})\to \Gamma$ factorizes through a group homomorphism $\op{cl}_{\overline{\k}}: K_0(\CC(\overline{\k}))\to \Gamma$. It is easy to see that for any field extension $\k^{\prime}\supset \k$ we obtain a homomorphism $\op{cl}_{\overline{\k}^{\prime}}: K_0(\CC(\overline{\k}^{\prime}))\to \Gamma$.

In the case when $\CC$ is a Calabi-Yau category we require that $\Gamma$ is endowed with an integer-valued bilinear form $\langle \bullet,\bullet\rangle$ and the homomorphism $\op{cl}_{\overline{\k}}$ is compatible with $\langle \bullet,\bullet\rangle$ and the Euler form on $K_0(\CC(\overline{\k}))$.

For ind-constructible triangulated $\A$-categories the notion of stability structure admits the following version.

::: defn
A constructible stability structure on $(\CC,\op{cl})$ is given by the following data (cf. Introduction, Section 1.2):

-    an ind-constructible subset $$\CC^{ss}\subset Ob(\CC)$$ consisting of objects called semistable, and satisfying the condition that with each object it contains all isomorphic objects,

-   an additive map $Z:\Gamma\to \C$ called central charge, such that $Z(E):=Z(\op{cl}(E))\ne 0$ if $E\in \CC^{ss}$,

-   a choice of the branch of logarithm $\op{Log}Z(E)\in \C$ for any $E\in \CC^{ss}$ which is constructible as a function of $E$.

These data are required to satisfy the corresponding axioms from Section 1.2 for the category $\CC(\overline{\k})$.

In particular

-   the set of $E\in \CC^{ss}(\overline{\k})\subset Ob(\CC)(\overline{\k})$ with the fixed $\op{cl}(E)\in \Gamma\setminus \{0\}$ and fixed $\op{Log}Z(E)$ is a constructible set.
:::

Before we proceed with the topology let us make a comparison with the "Lie-algebraic\" story of Section 2. First, we observe that the set $\CC^{ss}$ can be thought of as an analog of the collection of elements $(a(\gamma))_{\gamma \in \Gamma\setminus \{0\}}$ from Section 2.1. Then we give the following definition of another data and axioms which is equivalent to the one given above and can be thought of as an analog of the collection of the group elements $A_V$.

::: defn
A constructible stability structure on $(\CC,\op{cl})$ is given by the following data:

-   an additive map $Z:\Gamma\to \C$,

-   for any bounded connected set $I\subset \R$ an ind-constructible subset ${\cal P}(I)\subset Ob(\CC)(\kk)$ which contains which every object all isomorphic objects.

These data are required to satisfy the following axioms[^1]:

-   the zero object of the category $\CC(\kk)$ belongs to all ${\cal P}(I)$,

-    $\cup_{n\in \Z_{>0}}{\cal P}([-n,n])=Ob(\CC)(\kk)$,

-   if $I_1<I_2$ in the sense that every element of $I_1$ is strictly less than any element of $I_2$ then for any $E_1\in {\cal P}(I_1)$ and $E_2\in {\cal P}(I_2)$ one has $\op{Ext}^{\le 0}(E_2,E_1)=0$,

-   ${\cal P}(I+1)={\cal P}(I)[1]$ where $[1]$ is the shift functor in $\CC(\kk)$,

-   (Extension Property) If $I=I_1\sqcup I_2$ and $I_1<I_2$ in the above sense then the ind-constructible set ${\cal P}(I)$ is isomorphic to the ind-constructible subset of such objects $E\in Ob(\CC)(\kk)$ which are extensions $E_2\to E\to E_1$ with $E_m\in {\cal P}(I_m), m=1,2$,

-   if $I$ is an interval of the length strictly less than one, $E\in {\cal P}(I), E\ne 0$, then $Z(\op{cl}(E))$ belongs to the strict sector $$V_I=\{z=re^{\pi i\varphi}\in \C^{\ast}|r>0,\varphi \in I\}\,\,,$$

-   there is a non-degenerate quadratic form $Q$ on $\Gamma_{\R}$ such that $Q_{|\op{Ker}Z}<0$, and for any interval $I$ of the length strictly less than $1$ the set $$\{\op{cl}(E)\in \Gamma|E\in {\cal P}(I)\}\subset \Gamma$$ belongs to the convex cone $C(V_I,Z,Q)$ defined in Section 2.2,

-   let $I$ be an interval of the length strictly less than $1$, and $\gamma\in \Gamma$. Then the set $\{E\in {\cal P}(I)| \op{cl}(E)=\gamma\}$ is constructible.
:::

The equivalence of Definitions 9,10 can be proved similarly to the proof of Theorem 2.

With this equivalent description of a constructible stability condition we observe that the collection of sets ${\cal P}(I)$ considered for all intervals $I$ with the length less than $1$ are analogous to the collection of elements $A_V$ where $V=V_I$ (see Section 2.2) and the Extension Property is analogous to the Factorization Property.

One has the following result.

::: prp
For any constructible stability structure on $\CC$ and any field extension $\k\subset \k^{\prime}$ the category $\CC(\k^{\prime})$ carries a locally finite stability structure in the sense of [@Br1] with the central charge given by $Z\circ \op{cl}_{{\k}^{\prime}}$ and the collection of additive subcategories ${\cal P}(I)({\k}^{\prime})$, where $I$ runs through the set of bounded connected subsets of $\R$ as above.
:::

*Proof.* The proof is straightforward. Local finiteness in the sense of [@Br1] follows from our (stronger) assumption on the quadratic form $Q$. $\blacksquare$

Let us denote by $Stab(\CC,\op{cl})$ the set of constructible stability structures on $\CC$ with a fixed class map $\op{cl}$. Our goal is to introduce a topology on $Stab(\CC,\op{cl})$.

Let $\Delta\subset \C$ be a triangle with one vertex at the origin. We choose a branch of the function $z\mapsto \op{Log} z$ for $z\in \Delta$. We denote the corresponding argument function by $\op{Arg}(z)$. We denote by ${\CC}_{{\Delta},\op{Log}}$ an $\A$-subcategory of $\CC$ generated by the zero object ${\bf 0}$, semistable objects $E$ with $Z(E)\in \Delta, \op{Arg}(E)\in \op{Arg}(\Delta)$ as well as extensions $J$ of such objects satisfying the condition $Z(J)\in \Delta$. We allow the case $\Delta=V$ where $V$ is a sector, in which case we will use the notation $\CC_{V,\op{Log}}$. It is easy to see that $\CC_{{\Delta},\op{Log}}$ is an ind-constructible category. Notice that in the language of ind-constructible sets ${\cal P}(I)$ we have $Ob(\CC_{{V_I},\op{Log}})={\cal P}(I)$ for some choice of the branch $\op{Log}$. The condition of genericity of the sector $V_I$ corresponding to a closed interval $I=[a,b]$ of the length less than $1$ corresponds to the following genericity condition of the set ${\cal P}(I)$: both ${\cal P}(\{a\})$ and ${\cal P}(\{b\})$ are zero categories (equivalently ${\cal P}([a,b])={\cal P}((a,b))$).

Let us fix a non-degenerate quadratic form $Q$ on $\Gamma_{\R}$ such that $Q_{|\op{Ker} Z}<0$ and $Q(\op{cl}(E))>0$ for any $E\in \CC^{ss}$. We introduce the topology on $Stab(\CC,\op{cl})$ in the following way. Let us consider a family $\sigma_x=(Z_x,\CC^{ss}_x,\dots), x\in X$ of stability structures in a neighborhood of $x_0\in X$. Then for every point $x$, a generic closed interval $I=[a,b]$ of the length less than $1$ we have the full category ${\cal P}(I)_x\subset Ob(\CC)$. For a given $\gamma\in \Gamma\setminus\{0\}$ we denote by ${\cal P}(I)_{x,\gamma}$ the constructible subset of objects $E\in {\cal P}(I)_x$ such that $\op{cl}(E)=\gamma$.

We say that a family $\sigma_x=(Z_x,\CC^{ss}_x,\dots), x\in X$ of stability structures parametrized by a topological space $X$ is *continuous at a given stability structure $\sigma_{x_0}=(Z_0,\CC^{ss}_0,\dots)$* if:

a\) The map $x\to Z_x$ is continuous at $x=x_0$.

b\) There exists a neighborhood $U$ of $x_0$ such that for any $E\in \CC^{ss}_x, x\in U$ we have $Q(\op{cl}(E))\geqslant 0$.

c\) For any generic closed interval $I$ of the length strictly less than $1$ the constructible set ${\cal P}(I)_{x,\gamma}$ is locally constant near $x_0$ (cf. Definition 3c)).

In this way we obtain a Hausdorff topology on $Stab(\CC,\op{cl})$. We can define a parallel transport along a path $\sigma_t$ in the space $Stab(\CC,\op{cl})$ similarly to the case of stability structures in graded Lie algebras discussed in Section 2. Each time when we cross the wall of first kind we use the above property c) in order to "recalculate\" the set of semistable objects. In order to do this we use the following property: $E\in Ob(\CC_{{\Delta},\op{Log}})$ is semistable iff there is no extension $E_2\to E\to E_1$ where $E_i,i=1,2$ are non-zero objects of $\CC_{{\Delta},\op{Log}}$ such that $\op{Arg}(E_2)>\op{Arg}(E_1)$. These considerations also ensure that the Theorem 1 from Introduction holds (i.e. the natural projection of the space of stability conditions to the space of central charges is a local homeomorphism).

[^1]: One should read expressions $Ob(\CC),{\cal P}(I)$ etc. in this list of axioms as sets of $\kk$-points.
