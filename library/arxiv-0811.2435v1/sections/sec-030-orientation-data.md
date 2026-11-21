---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-030-orientation-data
section_title: "Orientation data"
section_number: null
pages: 80-83
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.985
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 51 sections: Front matter; Introduction; Counting problems for 3-dimensiona"
---
Let $\CC$ be an ind-constructible $\k$-linear $3$-dimensional Calabi-Yau category.[^1] Then we have a natural ind-constructible super line bundle ${\cal D}$ over $Ob(\CC)$ with the fiber over $E$ given by ${\cal D}_E=\op{sdet}(\op{Ext}^{\bullet}(E,E))$. It follows that on the ind-constructible stack of exact triangles $E_1\to E_2\to E_3$ we have an isomorphism of the pull-backed line bundles which fiberwise reads as $${\cal D}_{E_2}\otimes {\cal D}_{E_1}^{-1}\otimes {\cal D}_{E_3}^{-1}\simeq (\op{sdet}(\op{Ext}^{\bullet}(E_1,E_3)))^{\otimes 2}\,\,.$$ Let us explain this isomorphism. The multiplicativity of superdeterminants on exact triangles gives rise to a canonical isomorphism $$\op{sdet}(\op{Ext}^{\bullet}(E_2,E_2))\simeq \op{sdet}(\op{Ext}^{\bullet}(E_1,E_1))\otimes \op{sdet}(\op{Ext}^{\bullet}(E_1,E_3))\otimes$$ $$\otimes\op{sdet}(\op{Ext}^{\bullet}(E_3,E_1))\otimes \op{sdet}(\op{Ext}^{\bullet}(E_3,E_3))\,\,.$$ By the Calabi-Yau property we have $$\op{sdet}(\op{Ext}^{\bullet}(E_3,E_1))\simeq \op{sdet}(\Pi(\op{Ext}^{\bullet}(E_3,E_1)))^{\ast}\simeq \op{sdet}(\op{Ext}^{\bullet}(E_1,E_3))$$ which implies the desired formula. When $Ob(\CC)=\sqcup_{i\in I}Y_i$ is a decomposition into the union of $GL(N_i)$-invariant constructible sets as at the end of 3.2, then the restriction ${\cal D}_{|Y_i}$ is a $GL(N_i)$-equivariant super line bundle and the above isomorphisms are also equivariant.

::: defn
Orientation data on $\CC$ consists of a choice of an ind-constructible super line bundle $\sqrt{{\cal D}}$ on $Ob(\CC)$ such that its restriction to each $Y_i, i\in I$ is $GL(N_i)$-equivariant, endowed on each $X_i$ with $GL(N_i)$-equivariant isomorphisms $(\sqrt{{\cal D}})^{\otimes 2}\simeq {\cal D}$ and such that for the natural pull-backs to the ind-constructible stack of exact triangles $E_1\to E_2\to E_3$ we are given equivariant isomorphisms: $$\sqrt{{\cal D}}_{E_2}\otimes (\sqrt{{\cal D}}_{E_1})^{-1}\otimes (\sqrt{{\cal D}}_{E_3})^{-1}\simeq \op{sdet}(\op{Ext}^{\bullet}(E_1,E_3))$$ such that the induced equivariant isomorphism $${\cal D}_{E_2}\otimes {\cal D}_{E_1}^{-1}\otimes {\cal D}_{E_3}^{-1}\simeq (\op{sdet}(\op{Ext}^{\bullet}(E_1,E_3)))^{\otimes 2}$$ coincides with the one which we have a priori.
:::

We define the group $J_2(\CC):=\prod_{i\in I} J_2(Y_i,GL(N_i))$. We have a canonical equivariant super line bundle ${\cal D}_{\le 1}$ whose fiber at $E\in Ob(\CC)$ is $${\cal D}_{\le 1,E}:=\op{sdet}(\tau_{\le 1}(\op{Ext}^{\bullet}(E,E)))\,\,,$$ where $\tau_{\le i}, i\in \Z$ denotes the standard truncation functor. It is easy to see that we have an equivariant isomorphism ${\cal D}_{\le 1}^{\otimes 2}\simeq {\cal D}$. Then on the space of exact triangles $E_1\to E_2\to E_3$ we have an equivariant isomorphism of super line bundles fiberwise given by $$({\cal D}_{{\le 1},E_2}\otimes {\cal D}_{{\le 1},E_1}^{-1}\otimes {\cal D}_{{\le 1},E_3}^{-1})^{\otimes 2}\simeq (\op{sdet}(\op{Ext}^{\bullet}(E_1,E_3)))^{\otimes 2}.$$

Let now $Fun({\CC}_3, \CC)$ be the ind-constructible category of $\A$-functors from the the category $\CC_3$ considered in 3.1. Its objects can be thought of as exact triangles $$E_1\to E_2\to E_3=Cone(E_1\to E_2)$$ in $\CC$. There are three functors $Funct({\CC}_3, \CC)\to \CC$ which associate to an exact triangle $E_1\to E_2\to E_3$ the objects $E_1,E_2,E_3$ respectively. These functors induce three homomorphisms $$\phi_i: J_2(\CC)\to J_2(Funct(\CC_3, \CC)), i=1,2,3\,\,.$$ The super line bundle $L$ with the fiber $$L_{E_1\to E_2\to E_3}=({\cal D}_{{\le 1},E_2}\otimes {\cal D}_{{\le 1},E_1}^{-1}\otimes {\cal D}_{{\le 1},E_3}^{-1})\otimes (\op{sdet}(\op{Ext}^{\bullet}(E_1,E_3)))^{-1}$$ defines an element $l\in J_2(Funct({\cal A}_2, \CC))$, since $L^{\otimes 2}\simeq {\bf 1}_{Funct(\CC_3, \CC)}$. Then a choice of orientation data on $\CC$ is equivalent to a choice of $h\in J_2(\CC)$ such that $-\phi_1(h)+\phi_2(h)-\phi_3(h)=l$. Indeed a choice of orientation data gives rise to a super line bundle $\sqrt{\cal D}$ such that $\sqrt{\cal D}^{\otimes 2}\simeq {\cal D}_{\le 1}^{\otimes 2}$. Therefore the quotient $h=\sqrt{\cal D}\otimes {\cal D}_{\le 1}^{-1}$ defines an element in $J_2(\CC)$, and the condition for the tensor squares of the super line bundles $\sqrt{\cal D}_{E_i}, i=1,2,3$ on the space of exact triangles is equivalent to the equation $-\phi_1(h)+\phi_2(h)-\phi_3(h)=l$.

::: rmk
All the above considerations admit a straightforward generalization to the case of Calabi-Yau category of arbitrary odd dimension $d$. In the case $d=1\,(\op{mod} 4)$ we have canonical orientation data given by $$\sqrt{\cal D}_{\cal E}:=\op{sdet}(\tau_{\le {d-1\over{2}}}(\op{Ext}^{\bullet}(E,E)))\,\,.$$ This is due to the observation that in the explicit description of the analog of the obstruction element $l$ defined above in terms of a super vector bundle endowed with a symmetric bilinear form, the super vector bundle turns out to be purely odd, hence the bilinear form is split. It follows that the obstruction element is trivial. In the case $d=3$ considered in this paper the obstruction does not have to vanish.
:::

[^1]: There is a notion of $\Z/2\Z$-graded odd or even Calabi-Yau category, see [@KoSo3]. Some considerations of this section can be generalized to $\Z/2\Z$-graded case.
