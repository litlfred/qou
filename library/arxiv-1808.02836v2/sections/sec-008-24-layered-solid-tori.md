---
doc_id: arxiv-1808.02836v2
doc_title: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds Introduction"
section_id: sec-008-24-layered-solid-tori
section_title: "Layered solid tori"
section_number: 2.4
pages: 5-6
source_pdf: 1808.02836v2.pdf
source_sha256: 0224a296253122a2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 1.0
doc_brief: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds Introduction — Previous work of the authors studies minimal triangulations of closed 3–manifolds using a characterisation of low"
---
[]{#sec:lst label="sec:lst"}

A *layered solid torus* $\operatorname{LST}$ is a triangulation of a solid torus iteratively constructed in the following way: Start with a one-triangle Möbius strip as shown in Figure [\[fig:faces\]](#fig:faces){reference-type="ref" reference="fig:faces"}(c). Then attach additional tetrahedra without a twist along pairs of (unpaired) faces of the existing complex sharing an edge $e$. This operation is called a *layering* on $e$, where the first layering onto the Möbius strip must always go on the interior edge of the Möbius strip, see Figure [1](#fig:layering){reference-type="ref" reference="fig:layering"}. Layered solid tori are close cousins of the monodromy ideal triangulations of once-punctured torus bundles defined in Section [\[sec:mit\]](#sec:mit){reference-type="ref" reference="sec:mit"}, since both types of triangulations are obtained from layering tetrahedra onto an existing complex. See [@Jaco-layered-2006] for a comprehensive introduction into layered solid tori and, more generally, layered triangulations. Here, we summarise material of [@Jaco-minimal-2009 Section 2.3].

<figure id="fig:layering">

<figcaption>Layering tetrahedron <span class="math inline"><em>Δ</em></span> to triangulation <span class="math inline">𝒯</span> on edge <span class="math inline"><em>e</em></span>. Identifications of the triangles are indicated by the vertex labels. <span id="fig:layering" label="fig:layering"></span></figcaption>
</figure>

By construction, the boundary of a layered solid torus containing at least one tetrahedron is always the standard triangulation of a torus with one vertex, two triangles, and three edges. Layered solid tori are distinguished by how often their meridional disc intersects their three boundary edges geometrically and we write $\operatorname{LST}(a,b,c)$ for a layered solid torus with meridional disc intersecting the boundary edges $a$, $b$ and $c$ times respectively. Assuming $a\leq b\leq c$ it is straightforward to see that $a+b = c$ and that a layered solid torus $\operatorname{LST}(a,b,c)$ can be turned into a layered solid torus of type $\operatorname{LST}(a,b,b-a)$, $\operatorname{LST}(a,c,a+c)$ or $\operatorname{LST}(b,c,b+c)$ by layering an additional tetrahedron on the edge with label $c$, $b$, or $a$ respectively.

There exists only one layered solid torus with one tetrahedron, $\operatorname{LST}(1,2,3)$. Hence, by construction, every layered solid torus with at least one tetrahedron contains this layered solid torus, termed its *core tetrahedron*.

Let $\operatorname{LST}$ be a layered solid torus occurring as a subcomplex of some triangulation $\mathcal{T}$ of a $3$-manifold. We say that $\operatorname{LST}$ is *maximal with respect to $\mathcal{T}$* if it is not strictly contained in any other layered solid torus subcomplex in $\mathcal{T}.$ By a *layered $\partial$--punctured solid torus*, we mean a *layered solid torus* with its vertex removed. Whenever we talk about the punctured version of a layered solid torus $\operatorname{LST}(a,b,c)$ we denote it by $\operatorname{LST}^{\star} (a,b,c)$ to emphasise the difference. The notion of a layered $\partial$--punctured solid torus is very convenient when discussing the combinatorial structure of an ideal triangulation. For instance, they play a role in [@Gueritaud-canonical-2010].
