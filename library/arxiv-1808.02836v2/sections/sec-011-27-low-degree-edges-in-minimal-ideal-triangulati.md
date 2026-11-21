---
doc_id: arxiv-1808.02836v2
doc_title: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds Introduction"
section_id: sec-011-27-low-degree-edges-in-minimal-ideal-triangulati
section_title: "Low degree edges in minimal ideal triangulations"
section_number: 2.7
pages: 10-15
source_pdf: 1808.02836v2.pdf
source_sha256: 0224a296253122a2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.98
doc_brief: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds Introduction — Previous work of the authors studies minimal triangulations of closed 3–manifolds using a characterisation of low"
---
We now show that there are no edges of degree one or two in a minimal triangulation of a cusped hyperbolic 3--manifold, and that edges of degree three must be contained in layered $\partial$--punctured solid tori.

::: lemma
[]{#thm:degone label="thm:degone"} If $\mathcal{T}$ is a minimal ideal triangulation of a cusped hyperbolic 3--manifold $M,$ then $\mathcal{T}$ has no edge of degree one.
:::

::: proof
*Proof.* Suppose $e_1$ is an edge of $\mathcal{T}$ of degree 1. Let $\tilde{\Delta}_1$ be the single tetrahedron containing $e_1.$ Then $\tilde{\Delta}_1 = e_1\ast e$ is the join of $e_1$ and the edge $e$ opposite $e_1.$ The edge $e$ of $\mathcal{T}$ bounds a disc. This contradicts Corollary [\[cor-min-bddry-eff\]](#cor-min-bddry-eff){reference-type="ref" reference="cor-min-bddry-eff"}. ◻
:::

::: lemma
[]{#lem:degree two label="lem:degree two"} If $\mathcal{T}$ is a minimal ideal triangulation of a cusped hyperbolic 3--manifold $M,$ then $\mathcal{T}$ has no edge of degree two.
:::

::: proof
*Proof.* The *figure-eight* knot complement `m004`[^1] and its sister `m003` are the only cusped hyperbolic 3--manifold having an ideal triangulation with two ideal tetrahedra. Neither of these triangulations has an edge of degree two. Hence, we may assume $\mathcal{T}$ has at least three tetrahedra and that the preimage of an edge $e$ of degree two consists of two edges $e'$ and $e''$ in two distinct tetrahedra, $\tilde{\Delta}'$ and $\tilde{\Delta}'',$ respectively (note that an edge of degree two cannot be contained in a single tetrahedron).

We fix the following notation. The vertices of $\tilde{\Delta}'$ are denoted by $A',B',C',$ and $D'$ with $e' = A'D'.$ The vertices of $\tilde{\Delta}''$ are denoted by $A'',B'',C'',$ and $D''$ with $e'' = A''D''.$ The face identifications are $(A'B'D')\leftrightarrow (A''B''D'')$ and $(A'C'D')\leftrightarrow (A''C''D''),$ with $(A'D') = (A''D'') = e.$

<figure id="f-edge-degree-2">
<div class="center">
<img src="deg2edge" style="height:4cm" />
</div>
<figcaption>Edge of degree two. <span id="f-edge-degree-2" label="f-edge-degree-2"></span></figcaption>
</figure>

Typically, in such a case of an edge of degree two, one can discard the two tetrahedra $\tilde{\Delta}'$ and $\tilde{\Delta}''$ and make new identifications $(A'B'C')\leftrightarrow (A''B''C'')$ and $(B'C'D')\leftrightarrow (B''C''D'').$

If this is possible, then there is a triangulation of $M$ having fewer tetrahedra than $\mathcal{T},$ contradicting that $\mathcal{T}$ is minimal. It follows that under the assumption of $\mathcal{T}$ minimal and $e$ an edge of degree two, there must be an obstruction to such a re-identification, that is, some of the faces to be identified must already be identical. This can happen on the level of edges (Obstruction 1 below), or on the level of triangles (Obstruction 2 below). We consider both obstructions and show that each leads to a contradiction, establishing that there are no edges of degree two.

The edges $B'C'$ and $B''C''$ are identified, preventing the collapse, see Figure [2](#fig:obstruction1){reference-type="ref" reference="fig:obstruction1"}. In this situation we have two subcases:

1.  Edges are identified with opposite orientation (i.e., $B'C'$ is identified with $C''B''$). If this is the case, then in the truncated 3--manifold $M^c$ of $M$ with an open neighbourhood of the vertices removed, we have a properly embedded Möbius band $\mathcal{N} \subset M^c.$ If $\partial \mathcal{N}$ is an inessential curve on the vertex linking torus $T_0 \subset \partial M^c$, $M$ admits an embedded projective plane and we have a connected summand of $\mathbb{R}P^3$ in $M,$ contradiction to $M$ being hyperbolic. Hence, assume that $\partial \mathcal{N}$ is an essential curve on $T_0$. From this situation we can construct a Seifert fibred space properly embedded in $M$ which is impossible since our manifold is hyperbolic. To see this, note that the boundary of a small regular neighbourhood of $T_0 \cup  \mathcal{N}$ is a torus. Since our manifold is hyperbolic this torus must be inessential, and thus it must bound a solid torus outside $T_0 \cup  \mathcal{N}.$ Hence the Seifert structure on $T_0 \cup  \mathcal{N}$ extends to a Seifert fibering over this solid torus with at most two exceptional fibres, one at the centre line of the Möbius band $\mathcal{N}.$

2.  Edges are identified with coinciding orientation (i.e., $B'C'$ is identified with $B''C''$). In this case we have a properly embedded annulus $\mathcal{A} \subset  M^c.$ Note that, since $M$ is hyperbolic, $\mathcal{A}$ must be either compressible or boundary-parallel. Hence, if one boundary component of $\mathcal{A}$ is an essential curve, the other one is, too, and both are parallel curves on the same torus boundary component $T_0 \subset \partial M^c.$ In this case the annulus $\mathcal{A}$ runs parallel to $T_0$ with either $AB$ and $AC$ or $BD$ and $CD$ contained in the region between $\mathcal{A}$ and $T_0$. Now consider a torus running parallel to $T_0$ and bounding a collar neighbourhood of $T_0$ in $M^c$ containing $\mathcal{A}$. Normalising this torus cannot result in a surface normally isotopic to $T_0$ because $\mathcal{A}$ acts as a barrier. Accordingly, the triangulation is not boundary efficient. This gives a contradiction to the triangulation being minimal due to Theorem [\[lem:bdEfficient\]](#lem:bdEfficient){reference-type="ref" reference="lem:bdEfficient"}.

    If the boundary components are inessential, colour the bounding discs in the respective torus boundary components. More precisely, colour the disc near vertex $B$ *purple*, and the one near vertex $C$ *green*. W.l.o.g, edges $AB$ and $AC$ (truncated to run inside $M^c$) run inside the solid torus bounded by $\mathcal{A}.$ By construction, the endpoint near $B$ is purple and the endpoint near $C$ is green. Moreover, the endpoints near $A$ must either both be purple or both be green (note that $\mathcal{A}$ must be compressible). It follows that one of the edges $AB$ and $AC$ has endpoints with equal colours. It thus follows that this edge must be in the neighbourhood of the respective torus boundary components of $M^c,$ see Figure [3](#fig:obstruction1_2){reference-type="ref" reference="fig:obstruction1_2"}. Again, we use Theorem [\[lem:bdEfficient\]](#lem:bdEfficient){reference-type="ref" reference="lem:bdEfficient"} to produce a contradiction to the fact that the triangulation is minimal.

It follows that Obstruction 1. cannot occur.

<figure id="fig:obstruction1">
<div class="center">
<img src="moebiusannulus" style="height:4cm" />
</div>
<figcaption>Obstruction 1 (1). Edge <span class="math inline"><em>B</em>′<em>C</em>′</span> identified with edge <span class="math inline"><em>C</em>″<em>B</em>″</span> forming a punctured <span class="math inline">ℝ<em>P</em><sup>2</sup>,</span> or Möbius strip <span class="math inline">𝒩</span> (left). Obstruction 1 (2). Edge <span class="math inline"><em>B</em>′<em>C</em>′</span> identified with edge <span class="math inline"><em>B</em>″<em>C</em>″</span> forming an annulus <span class="math inline">𝒜</span> (right).</figcaption>
</figure>

<figure id="fig:obstruction1_2">
<div class="center">
<img src="obstruction_1" />
</div>
<figcaption>Obstruction 1 (2). Both boundary components of <span class="math inline">𝒜</span> are inessential <span class="math inline">∂<em>M</em><sup><em>c</em></sup></span>.</figcaption>
</figure>

Faces from the front are identified with faces of the back (cf. Figure [1](#f-edge-degree-2){reference-type="ref" reference="f-edge-degree-2"}). As a result of such a face identification, the two edges $B'C'$ and $B''C''$ may become identified. If this the case we fall back onto the cases dealt with in Obstruction 1. Again, we have two subcases:

1.  Face $(A'B'C')$ is identified with the face $(B''C''D'')$ or $(A''B''C'')$ is identified with the face $(B'C'D').$ These situations are symmetric. As explained above we may assume that $B'C'$ and $B''C''$ are not identified. Suppose we flatten the two tetrahedra so that $(A'B'C')$ is identified with $(A''B''C'')$ and $(B'C'D')$ is identified with $(B''C''D'').$ Since the interiors of $B'C'$ and $B''C''$ were initially disjoint, the preimage of a point under this operation is either a point or an interval. In particular this flattening operation is cell-like and hence preserves the homeomorphism type of the manifold $M.$ This gives a new triangulation of $M$ with fewer tetrahedra which contradicts our assumption that the triangulation $\mathcal{T}$ is minimal.

2.  The face $(A'B'C')$ is identified with the face $(A''B''C'')$ or the face $(B'C'D')$ is identified with the face $(B''C''D'').$ Again, these situations are symmetric. However, if face $(A'B'C')$ is glued to face $(A''B''C'')$ without a twist, $B'C'$ is glued to $B''C''$ and we are done (alternatively, if $(A'B'C')\leftrightarrow (A''B''C''),$ then the vertex at $A' =A''$ is a manifold point and $\mathcal{T}$ is not an ideal triangulation). If the two faces are identified with a twist, all edges of the two triangles become identified. In particular $B'C'$ and $B''C''$ are identified and, again, we are done.

Since we have that $\mathcal{T}$ contains at least three tetrahedra, and that all possibilities of having an edge of degree two lead to a contradiction, there are no edges of degree two. ◻
:::

::: lemma
[]{#lem:lst no folds label="lem:lst no folds"} Let $\mathcal{T}$ be a minimal ideal triangulation of a cusped hyperbolic 3--manifold $M.$ Suppose $\operatorname{LST}^{\star}$ is a layered $\partial$--punctured solid torus and there is a combinatorial map $\varphi\co\operatorname{LST}^{\star}\to M.$ Then $\varphi$ is an embedding.
:::

::: proof
*Proof.* We need to show that no identifications of the boundary faces of $\operatorname{LST}^{\star}$ are possible in $\mathcal{T}.$ If the two triangles of $\partial \operatorname{LST}^{\star}$ are identified, then $M$ is a punctured lens space, contrary to the assumption that $M$ is hyperbolic.

Hence, identifications can occur at most at the edges of $\partial \operatorname{LST}^{\star}.$ But it follows from Theorem [\[thm:no3fold\]](#thm:no3fold){reference-type="ref" reference="thm:no3fold"} that not all three edges of $\partial \operatorname{LST}^{\star}$ can be identified, and thus we only need to consider the case that two edges of $\partial \operatorname{LST}^{\star}$ are glued together.

A priori there are a total of six choices of how two boundary edges of $\partial \operatorname{LST}^{\star}$ can be identified (three pairs of edges and two possible orientations each). Ignoring the third edge, all of them result in a quadrilateral with all of its edges identified in the pattern shown in Figure [4](#fig:lstbdrglued){reference-type="ref" reference="fig:lstbdrglued"} in the centre and the third boundary edge is one of he two diagonals of the quadrilateral. Denote the unique boundary edge of the quadrilateral by $e$.

We now pass to a small regular neighbourhood $N = \mathop{\mathrm{Nhd}}(\operatorname{LST}^{\star} \cap M^c)$ of $\operatorname{LST}^{\star}$ in the compact core $M^c$ of $M$. By construction, its boundary $\partial N$ must be a surface with boundary properly embedded in $M^c$. We can think of $\partial N$ as the surface consisting of the octagon lying in the interior of the quadrilateral of $\partial \operatorname{LST}^{\star}$, and two quadrilaterals from the annulus that is the regular neighbourhood of the ideal edge $e$ in $M^c,$ see Figure [4](#fig:lstbdrglued){reference-type="ref" reference="fig:lstbdrglued"} on the right. The surface is obtained by gluing the dotted edges of the octagon to the dotted edges of the quadrilateral. The solid edges then denote the boundary of $\partial N$.

<figure id="fig:lstbdrglued">
<div class="center">
<img src="bdrylst" />
</div>
<figcaption>Left: Boundary of <span class="math inline">LST<sup>⋆</sup>.</span> Centre: Boundary of <span class="math inline">LST<sup>⋆</sup></span> after disregarding the third boundary edge with two boundary edges identified. Right: Octagon and two quadrilaterals making up the boundary <span class="math inline">∂<em>N</em></span> of a regular neighbourhood of <span class="math inline">LST<sup>⋆</sup></span> in <span class="math inline"><em>M</em><sup><em>c</em></sup></span>. Dotted edges are identified, solid edges denote the boundary of <span class="math inline">∂<em>N</em></span>.</figcaption>
</figure>

Up to symmetry, there are three ways two perform these gluings (notice that the red edges of the octagon can be paired with the red edges of the two quadrilaterals arbitrarily, but the orientation of the gluings is fixed). All of them are shown in Figure [5](#fig:bdrs){reference-type="ref" reference="fig:bdrs"}. The first set of gluings results in a once-punctured torus. This type of identification implies that the only identifications of $e$ are the ones from inside $\operatorname{LST}^{\star}$, a contradiction to the assumption that a pair of boundary edges of $\operatorname{LST}^{\star}$ are identified in $\mathcal{T}$. The second results in $\partial N$ a once-punctured Klein bottle, and the third results in $\partial N$ a thrice-punctured sphere.

<figure id="fig:bdrs">
<div class="center">
<img src="bdrs" style="height:4cm" />
</div>
<figcaption>Three possible ways to obtain <span class="math inline">∂<em>N</em></span>. Left: a once-punctured solid torus. Centre: a once-punctured Klein bottle. Right: a thrice-punctured sphere.</figcaption>
</figure>

Since $\partial N$ is separating it cannot be a once-punctured Klein bottle. Hence, it is a separating thrice-punctured sphere with all boundary components on the same boundary component $T_0$ of $M^c$. A parity argument shows that the number of essential boundary components of $\partial N$ must be even. Moreover, note that, by construction, $T_0 \cap N$ is the neighbourhood of a pinched disc in $T_0$ and thus connected.

It follows that $T_0 \cap N$ must fall into one of two categories.

1.  Two boundary components of $\partial N$ are essential and hence $T_0 \cap N$ must be equal to an annulus with a disc removed. Since $N$ is separating, this disc must be outside $N$ and thus disjoint from $e$. Hence, pasting this disc into $T_0 \cap N$ yields a necessarily boundary-parallel annulus.

2.  No boundary component of $\partial N$ is essential and hence $T_0 \cap N$ must be equal to a subsurface of $T_0$ with two discs removed. Again, these discs must be outside $N$ and thus disjoint from $e$. Pasting the discs into $T_0 \cap N$ results in a necessarily boundary-parallel disc.

Now, as in earlier arguments, consider a torus running parallel to $T_0$ and bounding a collar neighbourhood of $T_0$ in $M^c$ containing the annulus or disc. Normalising this torus cannot result in a surface normally isotopic to $T_0$ because it must be disjoint from $e$. Accordingly, the triangulation is not boundary efficient. This gives a contradiction to the triangulation being minimal due to Theorem [\[lem:bdEfficient\]](#lem:bdEfficient){reference-type="ref" reference="lem:bdEfficient"} and thus $\varphi\co\operatorname{LST}^{\star}\to M$ must be an embedding. ◻
:::

::: lemma
[]{#lem:degreethree label="lem:degreethree"} Let $\mathcal{T}$ be a minimal ideal triangulation of a cusped hyperbolic 3--manifold $M$ and $e$ be an ideal edge of degree three. Then $e$ is contained in an embedded two tetrahedron subcomplex of $\mathcal{T}$ combinatorially equivalent to the layered $\partial$--punctured solid torus $\operatorname{LST}^\star(1, 3, 4).$ In particular, $e$ is contained in a maximal layered $\partial$--punctured solid torus $\operatorname{LST}^\star$, twice in its core tetrahedron and once in the tetrahedron adjacent to the core, and no other edge in $\operatorname{LST}^\star$ is of degree three.

Moreover, $\mathcal{T}$ contains at least three ideal tetrahedra and each ideal edge of degree three is contained in its own subcomplex of this type.
:::

::: proof
*Proof.* We may and will work with the pseudo-manifold $\widehat{M}.$ Let $e \in \mathcal{T}$ be an edge of degree $3.$ If $e$ is incident with three distinct tetrahedra, then a $3$-2--move produces a triangulation with fewer tetrahedra, contradicting minimality of the triangulation. If $e$ is incident with exactly one tetrahedron, it cannot be of degree $3.$ Hence, $e$ is incident with exactly two tetrahedra. A brute-force enumeration shows that there exists only one 2--tetrahedra complex with an edge of degree $3$ in its interior -- the layered solid torus $\operatorname{LST}(1,3,4)$ (see case $|\tilde{\Delta}_e|=2$ in the proof of [@Jaco-minimal-2009 Proposition 9] for details). Moreover, $\operatorname{LST}(1,3,4)$ has exactly one such degree $3$ edge in its interior. This edge occurs twice in its core tetrahedron and once in the other tetrahedron (i.e., the tetrahedron adjacent to the core tetrahedron).

It follows from Lemma [\[lem:lst no folds\]](#lem:lst no folds){reference-type="ref" reference="lem:lst no folds"} that no identifications between the faces of this layered solid torus are possible, hence the subcomplex is embedded, contained in a maximal layered $\partial$--punctured solid torus and, in particular, the triangulation contains at least three tetrahedra. ◻
:::

We remark that an analysis of edges of degree four and five can be carried out following [@Jaco-minimal-2009], but this is not needed for the main applications of this paper and hence omitted.

[^1]: We include the names of manifolds from the cusped hyperbolic manifold census of SnapPea.
