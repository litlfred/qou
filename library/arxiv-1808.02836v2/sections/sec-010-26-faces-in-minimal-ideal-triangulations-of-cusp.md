---
doc_id: arxiv-1808.02836v2
doc_title: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds Introduction"
section_id: sec-010-26-faces-in-minimal-ideal-triangulations-of-cusp
section_title: "Faces in minimal ideal triangulations of cusped hyperbolic 3–manifolds"
section_number: 2.6
pages: 7-10
source_pdf: 1808.02836v2.pdf
source_sha256: 0224a296253122a2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 1.0
doc_brief: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds Introduction — Previous work of the authors studies minimal triangulations of closed 3–manifolds using a characterisation of low"
---
<figure id="fig:faces">
<div class="center">

</div>
<figcaption>Types of faces. The Möbius, 3–fold and dunce faces only have one vertex due to the edge identifications. A cone face may have one or two vertices and a triangle face may have up to 3 vertices.</figcaption>
</figure>

An ideal triangle in an ideal triangulation of a cusped hyperbolic 3--manifold $M$ may have some of its edges identified. There are eight possible types of triangular faces in the triangulation of the end-compactification $\widehat{M},$ depending on how vertices or edges are identified (see Figure 1 in [@Jaco-0-efficient-2003]). Ignoring possible identifications of vertices as in [@Luo-combinatorial-2017], this reduces to five types in $M$ based on edge identifications only (see Figure [1](#fig:faces){reference-type="ref" reference="fig:faces"}). We name the faces in $M$ according to their topology in $\widehat{M}.$ A face with no edge-identifications is termed a *triangle face*; it is a 2--simplex, possibly with some or all of its vertices identified. If a pair of edges is identified, the face is either a cone (possibly with the tip identified with the vertex on the boundary) and called a *cone face* or it is a Möbius band and called a *Möbius face*. In a Möbius face, we distinguish the *boundary edge* and the *core edge*. If all three edges are identified, the face is either a 3--fold or a dunce hat, and called a *3--fold face* or *dunce face* respectively.

For minimal ideal triangulations, we can prove the following statement.

::: theorem
[]{#thm:no3fold label="thm:no3fold"} Let $\mathcal{T}$ be a minimal ideal triangulation of a cusped hyperbolic 3--manifold $M.$ Then there is no 3--fold face and there is no dunce face.
:::

::: proof
*Proof.* Choose a compact core $M^c$ of $M$ with the property that each boundary component of $M^c$ is a vertex linking surface. Let $t$ be a triangle of $\mathcal{T}.$

**Case 1: $t$ is a 3--fold face.** Refer to Figure [2](#fig:threefold){reference-type="ref" reference="fig:threefold"}. Let $e$ be the edge of $t,$ $N(e)$ a small regular neighbourhood of $e$ in $M$ and $N^c(e) = N(e) \cap M^c.$ The frontier of $N^c(e)$ in $M^c$ is an annulus; we call this the *exchange annulus around $e.$* Let $N(t)$ be a regular neighbourhood of $t$ in $M.$ Then the boundary of $N^c(t) = N(t) \cap M^c$ has a natural cell decomposition into two hexagons corresponding to the two sides of $t$ and three quadrilaterals that are subsurfaces of the exchange annulus around $e.$ The edges of the hexagons through the interior of $M^c$ are termed the *long edges*. Seen with respect to $(t\cap M^c) \setminus N(e)$ the long edges of the hexagons have a natural labelling $1, 2, 3$ in cyclic order. See Figure [2](#fig:threefold){reference-type="ref" reference="fig:threefold"} on the right for a drawing of $N^c(t),$ in particular the two hexagons and their long edges.

Give $t$ a transverse orientation. This allows us to refer to one of the hexagons as the *top* hexagon and to the other as the *bottom* hexagon. The intersection $t \cap N^c(e)$ is a tripod times $[0,1].$ Figure [2](#fig:threefold){reference-type="ref" reference="fig:threefold"} on the left depicts a cross-section of the tripod times $[0,1]$ at some $x \in (0,1).$ The transverse orientation of $t$ is in the same direction at the legs of the tripod (either all clockwise or all anti-clockwise around the vertex of the tripod). It follows that the quadrilaterals join each long edge of the top hexagon to a long edge of the bottom hexagon. Moreover, on the labels this induces a 3--cycle. Thus, modulo orientation, the identification must be as shown in Figure [2](#fig:threefold){reference-type="ref" reference="fig:threefold"} (both on the left and on the right).

After collapsing the sections of the exchange annulus to the long edges of the hexagons, we obtain a connected, orientable, bounded surface $\mathcal{S}$ decomposed into two hexagons, nine edges and six vertices -- and thus of Euler characteristic $-1.$ As can be deduced from the vertex labels, the surface has three boundary components and thus must be a 3--punctured sphere.

<figure id="fig:threefold">
<div class="center">
<img src="threefold_2" />
</div>
<figcaption>Left: Cross-section through the neighbourhood <span class="math inline"><em>N</em><sup><em>c</em></sup>(<em>t</em>)</span> of an ideal 3–fold <span class="math inline"><em>t</em></span> near its boundary edge <span class="math inline"><em>e</em>.</span> The cross-section through the top and bottom hexagon of the right picture appear as green and purple lines respectively. Their endpoints mark the cross-section through the long edges of the respective hexagons. Labels coincide with the ones on the right. Right: Truncated boundary <span class="math inline"><em>N</em><sup><em>c</em></sup>(<em>t</em>)</span> of regular neighbourhood of the 3–fold face <span class="math inline"><em>t</em></span> (drawn in the centre in black). Its boundary surface is connected, of Euler characteristic <span class="math inline"> − 1</span> with three boundary components (each containing two edges, as indicated by the edge labels) and thus a 3–punctured sphere. The dotted blue lines with labels represent the intersection of <span class="math inline"><em>t</em></span> with the boundary torus <span class="math inline"><em>T</em><sub>0</sub></span> – a triple arc between nodes <span class="math inline">1</span> and <span class="math inline">2,</span> or the <span class="math inline"><em>Θ</em></span>–graph.</figcaption>
</figure>

Because $t$ is a 3--fold, the intersection of $t$ with a boundary torus $T_0 \subset \partial M^c$ consists of two nodes and three (normal) arcs, all running between the two nodes, also known as the *$\Theta$--graph*, see the dotted arcs in Figure [2](#fig:threefold){reference-type="ref" reference="fig:threefold"}. Since $\mathcal{S}$ has three boundary components meeting $T_0$ along the boundary of a neighbourhood of $t \cap T_0,$ the complement of the embedding of the $\Theta$--graph into $T_0$ must have three boundary components.

If no two arcs form a separating (i.e., inessential) curve on $T_0,$ then the $\Theta$--graph forms a spine of $T_0.$ In particular, its complement is a disc with a single boundary component, a contradiction. Hence, two arcs must bound a disc in $T_0.$ The remaining arc now either runs parallel to the first two, or completes each of the other two to an essential curve on $T_0.$ In both cases the complement has three boundary components. Both embeddings are shown in Figure [3](#fig:embeddings_1){reference-type="ref" reference="fig:embeddings_1"}.

Assume that we are in the latter situation and the $\Theta$--graph contains an essential curve on $T_0$. Since the embedding features two parallel arcs, one of the boundary curves of $\mathcal{S}$ bounds a disc in $T_0$. Pasting in this disc and pushing it into the interior of the manifold yields a properly embedded annulus which, because $M$ is hyperbolic, must be compressible or boundary parallel. If it is compressible, then $T_0$ is compressible. We conclude that $\mathcal{S}$ must be boundary parallel.

Hence assume that the $\Theta$--graph consists of three parallel arcs and is thus contained in a disc of $T_0$. This time two of the boundary curves of $\mathcal{S}$ bound discs in $T_0$ and pasting them in and pushing them into the manifold yields a properly embedded disc, and we conclude again that $\mathcal{S}$ must be boundary parallel.

In both cases, uniting $\mathcal{S}$ with the complement of $N(t \cap T_0)$ in $T_0$ thus produces a torus $$T_0 \setminus N(t \cap T_0) \cup \mathcal{S}$$ boundary parallel to $T_0$ and disjoint from $e$ (which is itself incident to $T_0$). It follows that normalising this boundary parallel torus cannot result in a surface normally isotopic to $T_0$ and thus $\mathcal{T}$ cannot be boundary efficient. This is impossible since we assume that $\mathcal{T}$ is minimal and thus boundary efficient by Theorem [\[lem:bdEfficient\]](#lem:bdEfficient){reference-type="ref" reference="lem:bdEfficient"}.

<figure id="fig:embeddings_1">
<div class="center">
<img src="embeddings_1" />
</div>
<figcaption>Two embeddings of the intersection of the 3–fold face <span class="math inline"><em>t</em></span> with torus boundary component <span class="math inline"><em>T</em><sub>0</sub>.</span> Left: trivial embedding contained in a disc of <span class="math inline"><em>T</em><sub>0</sub>;</span> in this case the boundary parallel torus is made up of a once-punctured torus and two discs that are subsurfaces of <span class="math inline"><em>T</em><sub>0</sub></span> and the 3–punctured sphere <span class="math inline">𝒮.</span> Right: two parallel essential loops; in this case the boundary parallel torus is made of a disc and an annulus that are subsurfaces of <span class="math inline"><em>T</em><sub>0</sub></span> and the 3–punctured sphere <span class="math inline">𝒮.</span></figcaption>
</figure>

**Case 2: $t$ is a dunce face.** Refer to Figure [4](#fig:duncehat){reference-type="ref" reference="fig:duncehat"}. Let $e$ be the edge of $t.$ We use the notation and set-up as in the previous case. The intersection of $t$ with $N^c(e)$ is again a tripod times an interval (see Figure [4](#fig:duncehat){reference-type="ref" reference="fig:duncehat"} on the left for a cross-section). However, now the transverse orientations do not all agree: two are in one direction and the last is in the opposite direction. In particular, this implies that each of the hexagons has two of its long edges connected by a quadrilateral on the exchange annulus, and exactly one long edge of the top hexagon is joined to a long edge of the bottom hexagon (and these edges do not share the same label). It follows that, up to symmetry, there is only a single way to identify the long edges of the hexagons, shown in Figure [4](#fig:duncehat){reference-type="ref" reference="fig:duncehat"} (both on the left and on the right).

<figure id="fig:duncehat">
<div class="center">
<img src="duncehat_2" />
</div>
<figcaption>Left: Cross-section through the neighbourhood <span class="math inline"><em>N</em><sup><em>c</em></sup>(<em>t</em>)</span> of an ideal dunce hat <span class="math inline"><em>t</em></span> near its boundary edge <span class="math inline"><em>e</em>.</span> Labels coincide with the ones on the right. Right: Truncated boundary <span class="math inline"><em>N</em><sup><em>c</em></sup>(<em>t</em>)</span> of regular neighbourhood of the dunce hat <span class="math inline"><em>t</em></span> (drawn in the centre in black). The boundary surface is connected, of Euler characteristic <span class="math inline"> − 1</span> with three boundary components (one containing four edges and two containing a single edge, as indicated by the edge labels) and thus a 3–punctured sphere. The dotted lines with vertex labels represent the intersection of <span class="math inline"><em>t</em></span> with the boundary torus <span class="math inline"><em>T</em><sub>0</sub>,</span> two disjoint loops and a connecting arc.</figcaption>
</figure>

The two hexagons again form a properly embedded 3--punctured sphere $\mathcal{S} \subset M^c.$ The dunce hat $t$ itself meets $\partial M^c$ in two nodes and three normal arcs: two loops, one at each node, and one arc connecting the two nodes -- also known as the *barbell graph*. Up to the action of the mapping class group, there are four possibilities of embedding the barbell graph into a torus boundary component $T_0 \subset \partial M^c,$ producing three boundary components in a regular neighbourhood of the graph: One where both loops are essential in $T_0$ and thus necessarily parallel; one where one loop is inessential and the other one is an arbitrary essential curve in $T_0;$ and two where both loops are inessential. See Figure [5](#fig:embeddings_2){reference-type="ref" reference="fig:embeddings_2"} for a picture of all four cases. Using the same pasting argument as in Case 1 we can conclude that $\mathcal{S}$ is boundary parallel. Again, uniting $\mathcal{S}$ with the complement of $N(t \cap T_0)$ produces a torus boundary parallel to $T_0$ and disjoint from $e.$ Thus, Theorem [\[lem:bdEfficient\]](#lem:bdEfficient){reference-type="ref" reference="lem:bdEfficient"} produces a contradiction. ◻
:::

<figure id="fig:embeddings_2">
<div class="center">
<img src="embeddings_2" />
</div>
<figcaption>Four embeddings of the intersection of the dunce hat <span class="math inline"><em>t</em></span> with torus boundary component <span class="math inline"><em>T</em><sub>0</sub>.</span> Top left: two inessential loops, not nested. Bottom left: two inessential loops, nested. Top right: two parallel essential loops. Bottom right: one essential loop and one inessential loop.</figcaption>
</figure>

::: remark
[]{#rem:fmp label="rem:fmp"} The preconditions of Theorem [\[thm:no3fold\]](#thm:no3fold){reference-type="ref" reference="thm:no3fold"} are necessary: the minimal triangulation of the Gieseking manifold has dunce faces, and there exists a minimal 2-tetrahedron triangulation of a 3--manifold with two Klein-bottle cusps, in which one of the four faces is a 3--fold face.

Moreover, Frigerio, Martelli and Petronio describe classes of orientable hyperbolic manifolds $\mathcal{M}_{g,k}$ with $k$ torus cusps and one end of type an orientable surface of genus $g$ [@Frigerio-Dehn-2003]. They show, that these manifolds admit minimal $(g+k)$--tetrahedra ideal triangulations if and only if $g>k,$ or $g=k$ and $g$ even, see [@Frigerio-Dehn-2003 Proposition 1.4]. Such triangulations must necessarily have $3k$ cone faces, and $(2g-k)$ dunce- or 3--fold faces, see [@Frigerio-Dehn-2003 Lemma 2.1]. Hence, for $g$ large enough, there exist minimal ideal triangulations of orientable hyperbolic 3--manifolds with all but an arbitrarily small portion of faces being dunce- or 3--fold-faces.
:::
