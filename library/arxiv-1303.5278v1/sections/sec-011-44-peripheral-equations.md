---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-011-44-peripheral-equations
section_title: "Peripheral equations"
section_number: 4.4
pages: 18-19
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.906
latex_coverage_ratio: 0.95
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
[]{#sub.peripheral label="sub.peripheral"}

Assume first, for simplicity, that $\partial M$ consists of a single torus, and let $\varpi$ be an oriented simple closed curve in $\partial M$ that is in *normal position* with respect to the induced triangulation $\mathcal{T}_\partial$ of $\partial M$. Let $$(\overline{a}_{\varpi}|\overline{b}_{\varpi}|\overline{c}_{\varpi})=
(\bar a_{\varpi,1} \ldots, \bar a_{\varpi,N} \mid  \bar b_{\varpi,1}, \ldots, \bar b_{\varpi,N} \mid \bar c_{\varpi,1}, \ldots, \bar c_{\varpi,N})$$ denote the vector in $\mathbb Z^{3N}$ computed as follows. See Figure [1](#truncated_tetra2){reference-type="ref" reference="truncated_tetra2"}.

<figure id="truncated_tetra2">
<p>at 300 280 at 0 280 at 0 30 at 300 30 <span class="math inline"><em>Z</em></span> at 150 18 <span class="math inline"><em>Z</em></span> at 150 284 <span class="math inline"><em>Z</em>′</span> at 139 176 <span class="math inline"><em>Z</em>′</span> at 178 165 <span class="math inline"><em>Z</em>″</span> at 19 155 <span class="math inline"><em>Z</em>″</span> at 281 155</p>
<p><span class="math inline"><em>b̄</em><sub>ϖ</sub><sup>0</sup></span> at 208 212 <span class="math inline"><em>ā</em><sub>ϖ</sub><sup>0</sup></span> at 199 272 <span class="math inline"><em>c̄</em><sub>ϖ</sub><sup>0</sup></span> at 268 207</p>
<p><span class="math inline"><em>c̄</em><sub>ϖ</sub><sup>3</sup></span> at 254 106 <span class="math inline"><em>b̄</em><sub>ϖ</sub><sup>3</sup></span> at 194 108 <span class="math inline"><em>ā</em><sub>ϖ</sub><sup>3</sup></span> at 200 50</p>
<p><span class="math inline"><em>c̄</em><sub>ϖ</sub><sup>2</sup></span> at 30 99 <span class="math inline"><em>b̄</em><sub>ϖ</sub><sup>2</sup></span> at 95 93 <span class="math inline"><em>ā</em><sub>ϖ</sub><sup>2</sup></span> at 102 31</p>
<p><span class="math inline"><em>ā</em><sub>ϖ</sub><sup>1</sup></span> at 100 256 <span class="math inline"><em>b̄</em><sub>ϖ</sub><sup>1</sup></span> at 106 194 <span class="math inline"><em>c̄</em><sub>ϖ</sub><sup>1</sup></span> at 45 199</p>
<img src="draws_eps/truncated_tetra2" style="width:45.0%" />
<figcaption>Each term of the “turning number” vector <span class="math inline">$(\overline{a}_{\varpi}|\overline{b}_{\varpi}|\overline{c}_{\varpi})$</span> is calculated as a sum of the signed number of times the curve <span class="math inline">ϖ</span> turns anticlockwise around the corners of the triangular ends of the truncated tetrahedra. Edges and arcs on the back side of the tetrahedron are drawn with dashed lines.</figcaption>
</figure>

The term $\bar a_\varpi^l$ counts the signed number of normal arcs of $\varpi$ that turn anticlockwise around the corner of the truncated triangle associated to the variable $Z$, at vertex number $l$ of this tetrahedron. The entry in the vector $\overline{a}_{\varpi}$ for this tetrahedron is $\sum_{l=0}^3 \bar a_\varpi^l$, and similarly for the $\overline{b}_{\varpi}$ and $\overline{c}_{\varpi}$ terms. We suppress the vertex number superscripts from now on, since this data is implied by the location of the labels in the figures.

If we eliminate $Z'_j$ using $Z_j+Z'_j+Z''_j = \pi$, then we obtain the vector in $\mathbb{Z}^{2N}$ $$(a_{\varpi}|b_{\varpi})=(\overline{a}_{\varpi}-\overline{b}_{\varpi}|
\overline{c}_{\varpi}-\overline{b}_{\varpi})$$ as well as the scalar $$\nu_{\varpi}=-\sum_{i=1}^N \overline{b}_{\varpi,j}.$$ Similarly, we can define "turning number" vectors $(\overline{a}_{\varpi}|\overline{b}_{\varpi}|\overline{c}_{\varpi}) \in \mathbb{Z}^{3N}$ and $(a_{\varpi}|b_{\varpi}) \in \mathbb{Z}^{2N}$ for any oriented multi-curve $\varpi$ on $\partial M$ (i.e. a disjoint union of oriented simple closed normal curves on $\partial M$).

More generally, suppose that $M$ is a 3-manifold whose boundary $\partial M$ consists of $r \ge 1$ tori $T_1, \ldots, T_r$. Let $\varpi=(\varpi_1, \ldots, \varpi_r)$ where $\varpi_i$ is an oriented multi-curve on $T_i$ for each $h=1, \ldots , r$. Then we will use the notation $$\label{eq.nupi}
(\overline{a}_{\varpi}|\overline{b}_{\varpi}|\overline{c}_{\varpi}) = \sum_{h=1}^r 
(\overline{a}_{\varpi_h}|\overline{b}_{\varpi_h}|\overline{c}_{\varpi_h}),~~
(a_{\varpi}|b_{\varpi})= \sum_{h=1}^r  (a_{\varpi_h}|b_{\varpi_h}), \text{ and }
\nu_{\varpi} = \sum_{h=1}^r \nu_{\varpi_h}.$$

::: rmk
[]{#edge_eqn_as_holonomy label="edge_eqn_as_holonomy"}

Suppose that $\varpi=C_i$ is a small linking circle on $\partial M$ around one of the two vertices at the ends of the $i$th edge, with $C_i$ oriented anticlockwise as viewed from a cusp of $M$. Then $$(\overline{a}_{\varpi}|\overline{b}_{\varpi}|\overline{c}_{\varpi}) = 
(\bar a_{i1} \ldots, \bar a_{iN} \mid  \bar b_{i1}, \ldots, \bar b_{iN} \mid \bar c_{i1}, \ldots, \bar c_{iN})$$ gives the coefficients of the $i$th edge equation as a special case of this construction.
:::
