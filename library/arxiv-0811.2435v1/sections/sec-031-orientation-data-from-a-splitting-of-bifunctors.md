---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-031-orientation-data-from-a-splitting-of-bifunctors
section_title: "Orientation data from a splitting of bifunctors"
section_number: null
pages: 83-84
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 0.911
latex_coverage_ratio: 0.991
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 51 sections: Front matter; Introduction; Counting problems for 3-dimensiona"
---
Let $\cal C$ be a triangulated ind-constructive category over a field $\k$. We will assume that all functors, bifunctors etc. respect this structure. In this section we are going to discuss a special framework in which orientation data is easy to construct.

Let $F:\CC\times \CC^{op}\to Perf(Spec(\k))$ be a biadditive bifunctor and $d$ be an integer. We define the *dual bifunctor of degree $d$* as a bifunctor $F^{\vee}=F^{\vee,d}$ given by $$F^{\vee}(E_2,E_1):=F(E_1,E_2)^{\ast}[-d]\,\,.$$ Clearly $F\mapsto F^{\vee}$ is an involution.

::: defn
A self-duality structure on $F$ of degree $d$ is an isomorphism $F\to F^{\vee}$ of bifunctors such that for any two objects $E_1,E_2$ the induced non-degenerate pairing $$F(E_1,E_2)\otimes F(E_1,E_2)\to \k[-d]$$ is symmetric on the level of cohomology $H^\bullet(F(E_1,E_2))$. If $F$ is endowed with a self-duality structure of degree $d$ then we call it self-dual.
:::

For a Calabi-Yau category of dimension $d$ the bifunctor $(E_1,E_2)\mapsto \op{Hom}^{\bullet}(E_1,E_2)$ is self-dual.

For any self-dual bifunctor $F$ of odd degree $d$ we can repeat considerations of Section 5.2. Namely, we define an ind-constructible super line bundle ${\cal D}^F$ with the fiber ${\cal D}^F_E:=\op{sdet}(F(E,E))$. Then for any exact triangle $E_1\to E_2\to E_3$ we have a canonical isomorphism

$$\sqrt{{\cal D}}_{E_2}^F\otimes (\sqrt{{\cal D}}_{E_1}^F)^{-1}\otimes (\sqrt{{\cal D}}_{E_3}^F)^{-1}\simeq \op{sdet}(F(E_1,E_3))^{\otimes 2}.$$

Then one can ask the same question: *is there an ind-constructible super line bundle $\sqrt{{\cal D}^F}$ which is compatible with the above isomorphism in the sense of Definition 15?*

The answer is positive for any bifunctor of the form $F\simeq H\oplus H^{\vee}$, with the obvious self-duality structure. In this case we set $$\sqrt{{\cal D}^F}_E:=\op{sdet}(H(E,E))\,\,.$$ More generally we can use an ${\bf A}^1$-homotopy in this special case. More precisely, suppose we are given a bifunctor[^1] $G: \CC\times \CC^{op}\to Perf({\bf A}^1_{\k})$. It can be thought of as a family $G_t: \CC\times \CC^{op}\to Perf(Spec(\k))$ of bifunctors, parametrized by $t\in {\bf A}^1(\k)$, namely $G_t=i_t^{\ast}\circ G$, where $i_t: Spec(\k)\to {\bf A}^1$ is the embedding corresponding to $t$. Since the category $Perf({\bf A}^1_{\k})$ has an obvious duality functor (taking dual to a complex of vector bundles) then the definition of self-duality structure extends naturally to families. Suppose that we have a family of self-dual bifunctors $G_t, t\in {\bf A}^1(\k)$ such that $G_0\simeq \op{Hom}^{\bullet}(\bullet,\bullet)$ and $G_1\simeq H\oplus H^{\vee}$ for some bifunctor $H$, and the isomorphisms preserve the self-duality structures. Then we have a canonical orientation data on $\CC$, since any super line bundle over ${\bf A}^1_{\k}$ is trivial and all fibers are canonically isomorphic.

[^1]: In fact we would like to say that $G$ is "ind-constructible" in some sense. A sufficient, but not necessary condition would be the existence of an ind-constructible functor $G'$ from $\CC\times \CC^{op}$ to $Perf({\bf P}^1_{\k})$ such that $G$ is isomorphic to the composition of $G'$ and the restriction functor $Perf({\bf P}^1_{\k})\to Perf({\bf A}^1_{\k})$.
