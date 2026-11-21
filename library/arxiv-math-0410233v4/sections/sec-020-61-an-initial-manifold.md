---
doc_id: arxiv-math-0410233v4
doc_title: "CUSP SHAPES UNDER CONE DEFORMATION"
section_id: sec-020-61-an-initial-manifold
section_title: "An initial manifold"
section_number: 6.1
pages: 31-39
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.996
doc_brief: "CUSP SHAPES UNDER CONE DEFORMATION — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp shape."
---
[]{#subsec:init label="subsec:init"}

Begin with a prime, twist reduced diagram of the knot $K$. At each twist region of the diagram, add a closed curve encircling two strands, called a *crossing circle*. We now have a diagram of a link, which we call $J$. The link complement $S^3-J$ is homeomorphic to the complement of the link $L$ obtained from $J$ by removing pairs of crossings from each twist region. See Figure [1](#fig:knot-decomp){reference-type="ref" reference="fig:knot-decomp"}.

<figure id="fig:knot-decomp">
<div class="center">
<embed src="figures/knot-decomp.eps" />
</div>
<figcaption>Left to right: The link <span class="math inline"><em>K</em></span>. The link <span class="math inline"><em>K</em></span> with crossing circles added. The link <span class="math inline"><em>L</em></span>.</figcaption>
</figure>

These links with crossing circles added have been studied by many people, including Adams [@adams:aug]; Lackenby, Agol and Thurston [@lackenby:alt-volume]. Many of the properties of these links were addressed in previous papers (see [@purcell:volume], and [@futer-purcell] with Futer).

The links are useful to us in the cone manifold setting because first, symmetries of the diagram of $L$ allow us to determine the hyperbolic structure on $S^3-L$ explicitly. Secondly, $S^3-L$ is related to the original knot complement via Dehn filling. In particular, if $2m_i$ crossings were removed from the $i$-th twist region to go from the diagram of $J$ to that of $L$, then by performing a $1/m_i$ Dehn filling on the corresponding $i$-th crossing circle of $S^3-L$, we re-insert these crossings and put back the crossing circle, obtaining $S^3-K$ (see e.g. [@rolfsen-book], Chapter 9).

Thus, starting with a hyperbolic augmented link $L$, we can determine information including shapes of the cusps. Next, we can find conditions which will ensure the Dehn filling above can be obtained by a hyperbolic Dehn filling via cone deformation. Hence we will have the first two pieces needed to bound the normalized height of the cusp $K$: The initial manifold $M$ with hyperbolic structure will be $S^3-L$. It will be connected by cone deformation to $S^3-K$.

### The geometry of $S^3-L$

We note in [@futer-purcell] that if $K$ has at least $2$ twist regions, then the augmented link complement $S^3-L$ will admit a complete, finite volume hyperbolic structure. This can be shown by work of Adams [@adams:aug], using the geometrization of Haken manifolds. It can also be shown more directly using Andreev's theorem. The proof using Andreev's theorem gives a packing of circles related to $S^3-L$ which we will need again in Section [\[subsec:2bridge\]](#subsec:2bridge){reference-type="ref" reference="subsec:2bridge"}, so we include it here.

::: theorem
If $K$ has a prime, twist reduced diagram with at least $2$ twist regions, then the augmented link complement $S^3-L$ will admit a complete, finite volume hyperbolic structure. []{#thm:Lhyp label="thm:Lhyp"}
:::

::: proof
*Proof.* We prove the lemma by finding the hyperbolic structure. To do so, we decompose $S^3-L$ into two ideal polyhedra, as in [@lackenby:alt-volume] and [@futer-purcell]. We then find a hyperbolic structure on the polyhedra which gives a nonsingular hyperbolic structure on $S^3-L$ after gluing.

To find the polyhedra, first remove all remaining single crossings at crossing circles. That is, if the number of crossings in a twist region of the diagram of $K$ was odd, then $S^3-L$ will still have a single crossing at that twist region. Remove it. The new link has components lying flat in the projection plane bound together by crossing circles. Call it $L'$.

Slice $S^3-L'$ along the projection plane. This cuts the manifold into two identical pieces, one on either side of the plane. Each 2--punctured disk encircled by a crossing circle has been sliced in half. Slice along these remaining halves of disks, opening them up into two faces. This gives an ideal polyhedral decomposition of the manifold. The edges are given by the intersection of the 2--punctured disks with the projection plane. On each of the two polyhedra, we have one face per planar region of the diagram of $L'$, and two triangular faces per 2--punctured disk. Shade the faces arising from 2--punctured disks, giving each polyhedron a checkerboard coloring. The edges meet in 4--valent ideal vertices. At each vertex, two white faces are separated by two shaded faces. (See [@futer-purcell] or [@lackenby:alt-volume] for pictures.)

The gluing pattern on the polyhedra is given by following the above process in reverse: First, on each polyhedron fold the pairs of triangular shaded faces together at their common vertex. Then glue each white face to its corresponding face on the opposite polyhedron via the identity map. This gives back $S^3-L'$.

To obtain $S^3-L$, we use the same two polyhedra, but make the following change in gluing. For crossing circles encircling a single crossing of the diagram of $L$, rather than glue shaded triangles across their common vertex on a single polyhedron, we insert a half--twist by gluing each triangle of one polyhedron to the opposite triangle of the other. See Figure [2](#fig:half-twist){reference-type="ref" reference="fig:half-twist"}.

<figure id="fig:half-twist">
<div class="center">
<embed src="figures/half-twist.eps" />
</div>
<figcaption>Left: Gluing 2–punctured discs with no crossings. Right: Gluing 2–punctured discs with a single crossing.</figcaption>
</figure>

Now our goal is to find a hyperbolic structure on these two polyhedra. We show the two polyhedra actually have totally geodesic faces in ${\mathbb{H}}^3$, meeting in dihedral angles of $\pi/2$. Since faces are glued in pairs, and edges in 4's, the gluing will give a complete hyperbolic structure on $S^3-L$.

Note any totally geodesic plane in ${\mathbb{H}}^3$ extends to give a circle on the boundary $S^2$ at infinity. Conversely, given a collection of circles on $S^2$, we can view those circles as boundaries of planes in ${\mathbb{H}}^3$. We obtain our polyhedra by finding appropriate circle packings, then cutting away half--spaces bounded by hemispheres in ${\mathbb{H}}^3$. Our tool is a corollary of Andreev's theorem noted by Thurston in [@thurston]:

::: theorem
Let $\gamma$ be a triangulation of $S^2$ such that each edge has distinct ends and no two vertices are joined by more than one edge. Then there is a packing of circles in $S^2$ whose nerve is isotopic to $\gamma$. This circle packing is unique up to Möbius transformation.
:::

Recall that the *nerve* of a circle packing is the graph obtained by adding a vertex for each circle, and an edge connecting two vertices if and only if the corresponding circles are tangent.

We begin by finding a triangulation of $S^2$ associated with one of the polyhedra described above. For each white face, take a vertex. Connect two vertices by an edge if and only if the two corresponding white faces meet at a vertex of the polyhedron. This gives a triangulation $\gamma$ of $S^2$. Note if we draw vertices of $\gamma$ on top of white faces of the polyhedron, and edges of $\gamma$ through the vertices of the polyhedron, that each triangle of $\gamma$ circumscribes a shaded face of the polyhedron.

To apply Andreev's theorem, we need to show this triangulation $\gamma$ satisfies the conditions: each edge has distinct ends, and no two vertices are joined by more than one edge. To show these conditions, we consider the graph dual to $\gamma$, as follows.

Consider the original link diagram. We view it as a 4--valent graph. Replace each twist region of the graph by a single edge, as in Figure [3](#fig:twist-to-edge){reference-type="ref" reference="fig:twist-to-edge"}.

<figure id="fig:twist-to-edge">
<div class="center">
<embed src="figures/twist_to_edge.eps" />
</div>
<figcaption>Create a trivalent graph by replacing each twist region with an edge.</figcaption>
</figure>

Since each crossing is part of some twist region, this gives a trivalent graph $\Gamma$.

Note the dual graph to $\Gamma$ is isotopic to the triangulation $\gamma$. We use properties of the dual $\Gamma$ to show the triangulation $\gamma$ satisfies the conditions necessary for Andreev's theorem.

::: lemma
No edge of $\gamma$ has a single vertex at both endpoints. []{#lemma:andreev1 label="lemma:andreev1"}
:::

::: proof
*Proof.* Consider the graph $\Gamma$. If its dual $\gamma$ has an edge with one vertex at both endpoints, then the graph $\Gamma$ must be of the form in Figure [4](#fig:Andr_double_end){reference-type="ref" reference="fig:Andr_double_end"} (a).

<figure id="fig:Andr_double_end">
<div class="center">
<p>(a)</p>
<p>(b)</p>
</div>
<figcaption>(a.) Form of <span class="math inline"><em>Γ</em></span> if <span class="math inline"><em>γ</em></span> has an edge with a single vertex at both endpoints. (b.) Corresponding form of original link diagram. </figcaption>
</figure>

Note then if the edge $e$ was an original edge of the 4--valent link diagram, then we have a simple closed curve intersecting the link diagram transversely in a single point. This is impossible.

If instead the edge $e$ replaced a twist region in the original 4-valent link diagram, then the original diagram had the form of Figure [4](#fig:Andr_double_end){reference-type="ref" reference="fig:Andr_double_end"} (b). However, note one of the subdiagrams $D$ and $D'$ must contain crossings else the original diagram has at most one twist region. Without loss of generality, say $D$ contains crossings. Then the dashed simple closed curve enclosing $D$ intersects the link diagram transversely in two points, but both its interior and its exterior contain crossings. This contradicts the fact that the original diagram was prime. ◻
:::

::: lemma
No two vertices of $\gamma$ are joined by more than one edge. []{#lemma:andreev2 label="lemma:andreev2"}
:::

::: proof
*Proof.* Suppose two vertices of $\gamma$ are joined by two distinct edges. Then consider the dual graph $\Gamma$. $\Gamma$ must be of the form shown in Figure [5](#fig:Andr_double_edge){reference-type="ref" reference="fig:Andr_double_edge"} (a), where region $B$ and region $B'$ are the same.

<figure id="fig:Andr_double_edge">
<div class="center">
<p>(a)</p>
<p>(b)</p>
</div>
<figcaption>Form of <span class="math inline"><em>Γ</em></span> when <span class="math inline"><em>γ</em></span> has two vertices connected by two distinct edges. In (a), the edges of <span class="math inline"><em>γ</em></span> are the dashed lines, with one of the vertices in <span class="math inline"><em>A</em></span> and the other at <span class="math inline">∞</span>.</figcaption>
</figure>

Give the edge $e_1$ an orientation, say $e_1$ points in the direction of the edge $a$. This gives the region $A$ an orientation, and hence assigns to the edge $e_2$ an orientation. Now, trace a path of edges around the region $B$, listing the edges in the order they occur. Our list begins with $e_1$, then $a$, etc. Note $e_2$ must appear in the list before the edge $d$, else region $B$ would be cut off from region $B'$. Also, edge $b$ must occur before edge $c$, by the orientation on $e_2$. Hence the graph $\Gamma$ has the form illustrated in Figure [5](#fig:Andr_double_edge){reference-type="ref" reference="fig:Andr_double_edge"} (b).

Case 1: Edges $e_1$ and $e_2$ both were edges of the original 4--valent link diagram. Then there is a simple closed curve intersecting $e_1$ and $e_2$ transversely in the original link diagram and intersecting the diagram in no other points. Since the original diagram has crossings on either side of the region $A$, this contradicts the fact that we started with a prime diagram.

Case 2: Edges $e_1$ and $e_2$ both replaced twist regions in the original link diagram. Then the original link diagram must have been of the form in Figure [6](#fig:Andr_double_diag1){reference-type="ref" reference="fig:Andr_double_diag1"} (a). Then since the original diagram was twist reduced, either the subdiagram $D$ or $D'$ must be a string of bigons. But then rather than two distinct twist regions, our diagram must have had only one twist region. Thus edges $e_1$ and $e_2$ would not have been distinct.

<figure id="fig:Andr_double_diag1">
<div class="center">
<p>(a) (b)</p>
</div>
<figcaption>Possible forms of the original link diagram if <span class="math inline"><em>γ</em></span> contains two vertices connected by two distinct edges.</figcaption>
</figure>

Case 3: One of edge $e_1$ or $e_2$ is from the original link diagram, the other replaced a twist region. Then the original link diagram must have been of the form shown in Figure [6](#fig:Andr_double_diag1){reference-type="ref" reference="fig:Andr_double_diag1"} (b). Now note that the simple closed curve bounding subdiagram $D$ intersects the link transversely in only three points. This is impossible.

Since these are the only three cases, these contradictions prove the lemma. ◻
:::

Now Lemmas [\[lemma:andreev1\]](#lemma:andreev1){reference-type="ref" reference="lemma:andreev1"} and [\[lemma:andreev2\]](#lemma:andreev2){reference-type="ref" reference="lemma:andreev2"} are enough to show that Andreev's theorem applies, and there is a circle packing of $S^2$ whose nerve is $\gamma$.

Complete the proof of Theorem [\[thm:Lhyp\]](#thm:Lhyp){reference-type="ref" reference="thm:Lhyp"} by slicing off half--spaces bounded by geodesic hemispheres in $\mathbb H^3$ corresponding to each circle in the circle packing. These give the geodesic white faces of the polyhedron. The shaded faces are obtained by slicing off hemispheres in $\mathbb H^3$ corresponding to each circle of the dual circle packing. Note white and shaded hemispheres meet at right angles.

Thus the polyhedron for the flat augmented link is totally geodesic in $\mathbb H^3$, and hence the flat augmented link is hyperbolic. ◻
:::

### Normalized lengths on cusps

To apply results on cone deformations, we will need the following information on normalized lengths of particular curves on the cusps of $S^3-L$.

::: prop
Let $K$ and $L$ be as above. In the prime, twist reduced diagram of $K$, let $n$ be the number of twist regions. Let $c_i$ be the number of crossings in the $i$-th twist region. Then on cusps of $L$, we have the following normalized lengths.

1.  For a cusp corresponding to a crossing circle, let $s_i$ be the slope such that Dehn filling $S^3-L$ along $s_i$ re-inserts the $c_i$ crossings at that twist region. Then the normalized length of $s_i$ is at least $\sqrt{c_i}$.

2.  For the cusp corresponding to the link component in the projection plane, the normalized height (i.e. the normalized length of the curve orthogonal to a meridian) is at least $\sqrt{n}$, and at most $\sqrt{n(n-1)}$.

[]{#prop:proj-height label="prop:proj-height"}
:::

::: proof
*Proof.* This can be deduced from results of [@futer-purcell]. However, given the circle packing associated to $S^3-L$ developed in the previous section, we are able to streamline the proof somewhat.

First, recall the polyhedra obtained in the proof of Theorem [\[thm:Lhyp\]](#thm:Lhyp){reference-type="ref" reference="thm:Lhyp"}. Note each cusp will be tiled by rectangles given by the intersection of the cusp with the totally geodesic white and shaded faces of the polyhedra. Two opposite sides of each of these rectangles come from the intersection of the cusp with shaded faces of the polyhedra, or from the 2--punctured disks in the diagram of $L$, and the other two sides come from white faces. Call the sides shaded sides and white sides, respectively.

For part (1), note any crossing circle intersects a single 2--punctured disk in a longitude. Half of the longitude is given by the intersection with one polyhedron, the other half by intersection with the other. The crossing circle intersects no other shaded faces. Thus the crossing circle cusp is tiled by exactly two identical rectangles.

When the crossing circle encircles no single crossing, or half twist, then two white faces intersect the cusp in meridians. In this case, $c_i$ is even, $c_i=2m_i$, and the slope $s_i$ is $1/m_i$. It is given by one step along a white side of a rectangle (a meridian), plus $2m_i=c_i$ steps along shaded sides of the rectangle.

When the crossing circle encircles a single crossing, then the two rectangles tiling the cusp are sheared. In this case, a meridian is given by one step along a white side, plus (or minus) a step along a shaded side. Now $c_i =2m_i+1$ is odd, and the slope $s_i =1/m_i$ is given by a step along a white side, plus (or minus) a step along a shaded side, plus (or minus) $2m_i$ steps along shaded sides.

In either case, the slope is given by a single step along a white side plus (or minus) $c_i$ steps along a shaded side. Let $w$ denote the length of a white side, and let $s$ denote the length of a shaded side. Thus the normalized length of $s_i$ is: $$\frac{\sqrt{w^2+c_i^2s^2}}{\sqrt{2ws}} =
  \sqrt{\frac{w}{2s}+c_i^2\frac{s}{2w}}.$$ Let $u=w/(2s)$. Then for constant $c_i$, this quantity is minimized when $u=c_i/2$, and the minimum value is $\sqrt{c_i}$.

For part (2), we need to know more about the possible lengths of the white sides of rectangles tiling the cusp. For a given rectangle, consider the corresponding vertex in one of the polyhedra. On the sphere $S^2$ at infinity, this vertex will look like a point of tangency of two circles in the packing given by Andreev's theorem. Since the nerve of this circle packing is a triangulation of $S^2$, the point of tangency corresponds to an edge on two distinct triangles of this nerve. Thus there are two additional circles tangent to the two given circles, as in Figure [7](#fig:circles){reference-type="ref" reference="fig:circles"}.

<figure id="fig:circles">
<div class="center">
<p><embed src="figures/circles1.eps" /> <embed src="figures/circles2.eps" /></p>
</div>
<figcaption>The form of the packing of circles about any vertex. Dashed circles correspond to the shaded faces of the polyhedron at this vertex.</figcaption>
</figure>

Now, apply a Möbius transformation taking the vertex, or the point of tangency of the circle packing, to infinity. This takes the two tangent circles to two parallel lines. It takes the two additional tangent circles to circles tangent to both the parallel lines, as in Figure [8](#fig:rec-circles){reference-type="ref" reference="fig:rec-circles"}. Note this also gives the similarity structure of the rectangle under consideration. If we normalize so that the shaded side (coming from the intersection with a 2--punctured disk) has length $1$, then the circle lying under the dashed line in Figure [8](#fig:rec-circles){reference-type="ref" reference="fig:rec-circles"} has diameter $1$. Since circles in the circle packing do not overlap, this forces a white side (i.e. without dashes in the figure) to have length at least $1$.

<figure id="fig:rec-circles">
<div class="center">
<p><embed src="figures/rec-circ1.eps" /> <embed src="figures/rec-circ2.eps" /></p>
</div>
<figcaption>Result of taking point of tangency to infinity.</figcaption>
</figure>

For an upper bound on the length of a white side, note it is longest when all circles in the circle packing are lined up in a row, tangent to the two parallel lines. In this case, when a shaded side has length $1$, the length of the white side will be the number of circles between the parallel lines, minus $1$. To find the number of circles possible, we use an Euler characteristic argument. Note there will be $2n$ shaded faces in one of the polyhedra, coming from opening up $n$ crossing circles. These each correspond to a single face of the triangulation of $S^2$ used in Andreev's theorem. Because it is a triangulation, the number of edges equals $3/2$ the number of faces, or $3n$. Then by an Euler characteristic argument, there are $n+2$ vertices. Recall each vertex gave a circle in our circle packing. Since two of these circles become our parallel lines, there are $n$ circles packed between these. Thus the maximum length of a white side is $n-1$.

Now, note that the cusp in the projection plane intersects each 2--punctured disk $2n$ times, each time in a meridian. Half of this meridian will come from the intersection of one polyhedron (the "top" half), the other half from the intersection of the other polyhedron. Thus the meridian runs along two shaded sides of rectangles. Still normalizing so each shaded side has length $1$, this implies a meridian has length $2$. The curve giving the height $H$ of the cusp runs along $2n$ white sides of the rectangles (one for each 2--punctured disk of intersection). The normalized height will be given by $H/\sqrt{2H} = \sqrt{H/2}.$ The height $H$ will be minimal when each of the $2n$ white sides it runs along are of minimal length, or length $1$. Thus the minimal normalized height is $\sqrt{n}$.

Similarly, the height $H$ will be maximal when each white side is of maximal length, or length $n-1$. Thus the maximal normalized height is $\sqrt{n(n-1)}$. ◻
:::

### Hyperbolic cone deformation on $S^3-L$ {#subsec:crossings}

If the normalized lengths of the slopes on which Dehn filling was performed were sufficiently large, then Hodgson and Kerckhoff showed that the Dehn filling could be realized by a hyperbolic cone deformation [@hk:univ]. Proposition [\[prop:proj-height\]](#prop:proj-height){reference-type="ref" reference="prop:proj-height"} indicates that to attain these minimal normalized slope lengths, we need only ensure that there are sufficiently many crossings in each twist region. In particular, by [@hk:univ], provided $\sqrt{c_j}
\geq 10.6273$, or provided that there are at least $113$ crossings per twist region of the prime, twist reduced diagram of $K$, then the Dehn filling of $S^3-L$ can be realized by a hyperbolic cone deformation.

Actually, we will see that the number of crossings in each twist region needs to be larger than $113$ to apply Theorem [\[thm:bound-bdry-time\]](#thm:bound-bdry-time){reference-type="ref" reference="thm:bound-bdry-time"}. For now, however, note that we may ensure a hyperbolic cone deformation does exist from $S^3-L$ to $S^3-K$ by putting conditions on the diagram of $K$.
