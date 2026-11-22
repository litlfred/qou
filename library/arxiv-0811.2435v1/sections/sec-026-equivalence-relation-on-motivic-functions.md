---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-026-equivalence-relation-on-motivic-functions
section_title: "Equivalence relation on motivic functions"
section_number: null
pages: 73-75
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.966
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 51 sections: Front matter; Introduction; Counting problems for 3-dimensiona"
---
We start with a motivation for this section. There are many examples of pairs of constructible sets (or even varieties) $X_1,X_2$ over a field $\k$ such that their classes $[X_1]$ and $[X_2]$ in $Mot(Spec(\k))$ are different (or at least not obviously coincide), but $X_1$ and $X_2$ coincide in each realization described in Section 4.1 (i)-(vi) (e.g. when $X_1,X_2$ are isogeneous abelian varieties). In particular we will be interested in the case when $X_l,l=1,2$ are affine quadrics given by the equations $\sum_{1\le i\le n}a_{i,l}x_i^2=1$, such that they have equal determinants: $\prod_{1\le i\le n}a_{i,1}=\prod_{1\le i\le n}a_{i,2}\in \k^{\times}$.

Here we propose a modification of the notion of motivic function which is a version of the Grothendieck's approach to the theory of pure motives with numerical equivalence. Let us explain it in the case of $X=Spec(\k)$, where $\k$ is a field of characteristic zero (which we will assume throughout this section).

We start with the symmetric monoidal $\Q$-linear category ${\cal M}^{eff}(\k)$. Its objects are smooth projective varieties over $\k$ and $$\op{Hom}_{{\cal M}^{eff}(\k)}(Y_1,Y_2)=\Q\otimes \op{Im}(Z^{\dim Y_2}(Y_1\times Y_2)\to H_{DR}^{2\dim Y_2}(Y_1\times Y_2))\,\,,$$ where $Z^n(X)$ denotes as usual the space of algebraic cycles in $X$ of codimension $n$, and we take the image of the natural map into the algebraic de Rham cohomology. Then $\op{Hom}_{{\cal M}^{eff}(\k)}(Y_1,Y_2)$ is a finite-dimensional $\Q$-vector space. Instead of de Rham cohomology we can use Betti cohomology (for an embedding $\k\hookrightarrow \C$) or $l$-adic cohomology. Comparison theorems imply that the image of the group of cycles in the cohomology does not depend on a cohomology theory.

Composition of morphisms is given by the usual composition of correspondences, and the tensor product is given by the Cartesian product of varieties. We extend the category ${\cal M}^{eff}(\k)$ by adding formally finite sums (then it becomes an additive category), and finally taking the Karoubian envelope. The $K_0$-ring of the resulting category contains the element ${\mathbb L}=[{\bf P}_{\k}^1]-[Spec(\k)]$. Adding formally the inverse ${\mathbb L}^{-1}$ we obtain the ring which we denote by $Mot_{coh}(Spec(\k))$. It is an easy corollary of Bittner theorem (see [@Bit]) that the natural map $Mot(Spec(\k))\to Mot_{coh}(Spec(\k))$ which assigns to a smooth projective variety its class in $Mot_{coh}(Spec(\k))$ is a homomorphism of rings.

The above considerations can be generalized to the case of motives over constructible sets.

::: defn
Let $X$ be a constructible set over a field $\k, char\,\k=0$. A constructible family of smooth projective varieties over $X$ is represented by a pair consisting of a smooth projective morphism $h:Y\to X_0$ of schemes of finite type over $\k$ and a constructible isomorphism $j:X_0\stackrel{\mathrm constr}{\simeq} X$. Two such representations $$h:Y\to X_0,\,\,j:X_0\stackrel{\mathrm constr}{\simeq}X,\,\,\,\;\,h':Y'\to X_0',\,\,j':X_0'\stackrel{\mathrm constr}{\simeq}X$$ are identified if we are given constructible isomorphisms $f:Y \stackrel{\mathrm constr}{\simeq}Y^{\prime}$, $g: X_0\stackrel{\mathrm constr}{\simeq}X_0^{\prime}$ such that $h^{\prime}\circ f=g\circ h,\,j'\circ g=j$, and for any point $x\in X(\overline{\k})$ the induced constructible isomorphism between smooth projective varieties $(j\circ h)^{-1}(x)$ and $(j'\circ h')^{-1}(x)$ is an isomorphism of schemes.
:::

For a constructible family of smooth projective varieties over $X$ and a point $x\in X$ there is a well-defined smooth projective variety $Y_x$ over the residue field $\k(x)$ called *the fiber over $x$*. Moreover, one can define the notion of constructible family of algebraic cycles of the fixed dimension. We say that such a family is homologically equivalent to zero if for any $x\in X$ the corresponding cycles in $Y_x$ map to zero in $H_{DR}^{\bullet}(Y_x)$. Also, having two constructible families of smooth projective varieties over $X$ one easily defines their product, which is again a constructible family of smooth projective varieties over $X$. All that allows us to generalize our constructions from the case $X=Spec(\k)$ to the general case. In this way we obtain the ring $Mot_{coh}(X)$ as well as the natural homomorphism of rings $Mot(X)\to Mot_{coh}(X)$.

::: defn
We say that two elements of $Mot(X)$ are (cohomologically) equivalent if their images in $Mot_{coh}(X)$ coincide.
:::

The set of equivalence classes (in fact the ring) will be denoted by $\overline{Mot}(X)$. It is isomorphic to the image of $Mot(X)$ in $Mot_{coh}(X)$. In particular, the above-mentioned quadrics define the same element in $\overline{Mot}(Spec(\k))$.

Let now $X$ be a constructible set over $\k$, endowed with an action of an affine algebraic group $G$. We define an equivalence relation on $Mot^G(X)$ in the following way. First we choose an embedding $G\hookrightarrow GL(N)$. We say that $f,g\in Mot^G(X)$ are equivalent if their pull-backs to $Mot((X\times GL(N))/G)$ have the same image in $\overline{Mot}(X\times GL(N))/G)$. Using the fact that all $GL(N)$-torsors over a constructible set are trivial it is easy to show that this equivalence relation does not depend on the embedding $G\hookrightarrow GL(N)$. The ring of equivalence classes is denoted by $\overline{Mot}^G(X)$.[^1] Similarly one defines the ring $\overline{Mot}^{G\times \mu}(X)$, where $\mu=\varprojlim_n\mu_n$. The exotic product descends to $\overline{Mot}^{G\times \mu}(X)$. Hence we obtain the ring $\overline{{\cal M}}^{G,\mu}(X)$ of equivalence classes as well as homomorphism of rings ${\cal M}^{G,\mu}(X)\to \overline{{\cal M}}^{G,\mu}(X)$.

[^1]: In this way we have circumvented the problem of defining the category of $G$-equivariant motivic sheaves.
