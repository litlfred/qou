---
doc_id: arxiv-1808.02836v2
doc_title: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds Introduction"
section_id: sec-012-28-layered-punctured-solid-tori-in-ideal-triangu
section_title: "Layered punctured solid tori in ideal triangulations"
section_number: 2.8
pages: 15-16
source_pdf: 1808.02836v2.pdf
source_sha256: 0224a296253122a2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.989
doc_brief: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds Introduction — Previous work of the authors studies minimal triangulations of closed 3–manifolds using a characterisation of low"
---
The argument for closed 3--manifolds in [@Jaco-Z2-2013] hinged on an understanding of the intersections of *maximal* layered solid tori. We now carry such an analysis out in the case of cusped hyperbolic 3--manifolds. This requires a different approach due to the fact that the combinatorics of minimal ideal triangulations is less restricted than the combinatorics of minimal and 0--efficient (material) triangulations.

As in [@Jaco-Z2-2013] we focus on subcomplexes in triangulations that are maximal layered $\partial$--punctured solid tori (see Section [\[sec:lst\]](#sec:lst){reference-type="ref" reference="sec:lst"} for a brief introduction).

::: lemma
[]{#lem:intersection label="lem:intersection"} Let $\mathcal{T}$ be a minimal ideal triangulation of a cusped hyperbolic 3--manifold $M.$ Then the intersection of any two maximal layered $\partial$--punctured solid tori is either empty, an ideal vertex, or an ideal edge of $\mathcal{T}.$
:::

::: proof
*Proof.* Let $\operatorname{LST}_a, \operatorname{LST}_b \subset \mathcal{T}$ be two maximal $\partial$--layered solid tori. If their boundaries $\partial \operatorname{LST}_a$ and $\partial \operatorname{LST}_b$ meet in two faces, $\mathcal{T}$ must be homeomorphic to a punctured lens space. A contradiction. If $\operatorname{LST}_a$ and $\operatorname{LST}_b$ share a common tetrahedron, remove the tetrahedra in the intersection from one of them and observe, that they now meet in two faces. Again, a contradiction. Hence, we can assume that two maximal $\partial$--layered solid tori meet along a single face, three edges, or two edges.

1.  Assume that $\partial \operatorname{LST}_a$ and $\partial \operatorname{LST}_b$ meet along exactly two edges. It follows, that they must be identified along a spine of each of $\partial \operatorname{LST}_a$ and $\partial \operatorname{LST}_b,$ referred to as their *common spine*. Let $\mathcal{D}_a$ and $\mathcal{D}_b$ be the discs obtained by taking the interior of $\partial \operatorname{LST}_a$ and $\partial \operatorname{LST}_b$ after truncating their vertex and removing their common spine. $\mathcal{D}_a$ and $\mathcal{D}_b$ can be glued together along sections of the exchange annuli in a neighbourhood of the common spine yielding a 4--punctured sphere $\mathcal{S}$ properly embedded in $M^c$ (the truncated compact core of $M$) and disjoint from the two edges of the common spine.

    By construction, the four boundary components of $\mathcal{S}$ in one of the torus boundary components $T_0\subset \partial M^c$ bound a regular neighbourhood of the intersection of the maximal layered solid tori $\operatorname{LST}_a$ and $\operatorname{LST}_b$ with $T_0$ -- a regular neighbourhood of two discs pinched along four points (the four points being the intersection of the common spine with $T_0$). Since this regular neighbourhood is connected, of Euler characteristic $-2,$ and with four boundary components, it must be a 4--punctured sphere contained in $T_0.$ There are two cases: either all components of $\partial\mathcal{S}$ are trivial in $T_0$ (that is, $\mathcal{S}$ equals a disc of $T_0$ with three points removed), or two components of $\partial\mathcal{S}$ are non-trivial (that is, $\mathcal{S}$ equals an annulus of $T_0$ with two points removed).

    First suppose $(\operatorname{LST}_a \cup \operatorname{LST}_b) \cap T_0$ is contained in a disc on $T_0$ and hence three of its boundary components bound discs in the complement of the intersection. Pasting these three discs of $T_0$ into $\mathcal{S}$ and pushing them slightly off $T_0$ yields a disc properly embedded in $M^c.$ This disc can be extended to a torus parallel to boundary component $T_0$ of $M^c$. Moreover, this torus is disjoint from the two edges of $\mathcal{T}$ of the common spine, which both are incident to $T_0$. It follows that a normalised version of this torus cannot be equal to the vertex linking torus $T_0$ and thus $\mathcal{T}$ cannot be boundary efficient. A contradiction to Theorem [\[lem:bdEfficient\]](#lem:bdEfficient){reference-type="ref" reference="lem:bdEfficient"}.

    Hence suppose $(\operatorname{LST}_a \cup \operatorname{LST}_b) \cap T_0$ is contained in an annulus on $T_0$ and hence two of its boundary components bound discs in the complement of the intersection. Pasting these two discs of $T_0$ into $\mathcal{S}$ and pushing them slightly off $T_0$ yields an annulus properly embedded in $M^c$ and disjoint from the two edges of $\mathcal{T}$ of the common spine (which are both incident to $T_0$). This annulus together with the annulus in $T_0$ complementary to $(\operatorname{LST}_a \cup \operatorname{LST}_b) \cap T_0$ extends to a boundary parallel torus since otherwise $M$ would contain a non-trivial Seifert fibred space. Again, this boundary parallel torus leads to a contradiction to the assumption that $\mathcal{T}$ is boundary efficient (cf. Theorem [\[lem:bdEfficient\]](#lem:bdEfficient){reference-type="ref" reference="lem:bdEfficient"}).

2.  Assume that $\partial \operatorname{LST}_a$ and $\partial \operatorname{LST}_b$ meet along exactly three edges. Following an analogous procedure as in the previous case, we arrive at two 3--punctured spheres $\mathcal{S}_1$ and $\mathcal{S}_2$ (instead of one 4--punctured sphere $\mathcal{S}$), both properly embedded in $M^c,$ both meeting the same boundary component $T_0 \subset \partial M^c.$ Again, it follows that a regular neighbourhood of $(\operatorname{LST}_a \cup \operatorname{LST}_b) \cap T_0$ is connected, of Euler characteristic $-4$ with six boundary components and thus a $6$--punctured sphere.

    Pasting in some of the boundary discs of this $6$--punctured sphere, analogously to the procedure carried out in the previous case, yields a torus parallel to boundary component $T_0$ and disjoint from three edges of the triangulation which are all incident to $T_0$ -- and we conclude as before by using Theorem [\[lem:bdEfficient\]](#lem:bdEfficient){reference-type="ref" reference="lem:bdEfficient"}.

3.  Assume that $\partial \operatorname{LST}_a$ and $\partial \operatorname{LST}_b$ meet along a single face. Again, we argue as in the previous cases. Here, we end up with one 3--punctured sphere $\mathcal{S}$ (the other one being filled in as a result of the face identification). A regular neighbourhood of $(\operatorname{LST}_a \cup \operatorname{LST}_b) \cap T_0$ now is connected, of Euler characteristic $-1,$ has three boundary components, and thus is contained in a disc or an annulus on $T_0.$ We again obtain a disc or an annulus that can be extended to a torus running parallel to $T_0$ which is disjoint of three edges of the triangulation incident to $T_0$ and we use Theorem [\[lem:bdEfficient\]](#lem:bdEfficient){reference-type="ref" reference="lem:bdEfficient"} once again to finish the proof.

This completes the proof of the lemma. ◻
:::
