---
doc_id: arxiv-1203.6551v1
doc_title: "On the number of hyperbolic 3-manifolds of a given volume"
section_id: sec-005-6-hyperbolic-graphs-with-parabolic-meridians
section_title: "Hyperbolic graphs with parabolic meridians"
section_number: 6
pages: 15-18
source_pdf: 1203.6551v1.pdf
source_sha256: a8e84f8ed63dbcca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.971
doc_brief: "On the number of hyperbolic 3-manifolds of a given volume — The work of Jørgensen and Thurston shows that there is a ﬁnite number N(v) of orientable hyperbolic 3-manifolds with any given volume v."
---
[]{#sec.Vol label="sec.Vol"} In this section, we recall some results on hyperbolic graphs in $S^3$ with parabolic meridians; for details see [@HHMP] and [@Mas]. In this paper, spatial graphs may contain link components, and we regard every link as a spatial graph without vertices. We use the word *link* to emphasize that the graph does not have any vertices. Let $G$ be a spatial trivalent graph in $S^3$ and let $N$ be a manifold obtained from $S^3\setminus G$ by removing an open regular neighbourhood of each vertex. Then $N$ is a manifold with boundary consisting of thrice punctured spheres, one corresponding to each vertex of $G$. We say that $G$ is *hyperbolic* if $N$ admits a hyperbolic metric of finite volume with geodesic boundary; then the meridians of the graph correspond to parabolic isometries. We can construct a hyperbolic link from a hyperbolic graph by using the following.

::: lem
[]{#Vol label="Vol"} For hyperbolic graphs, the moves shown in Figure [1](#fig.move1){reference-type="ref" reference="fig.move1"} are volume preserving, where regular neighbourhoods of the two trivalent vertices have been removed in middle diagram.
:::

![Volume preserving moves on hyperbolic graphs](move1.eps){#fig.move1}

::: proof
*Proof.* Note that each vertex in a hyperbolic graph corresponds to a totally geodesic thrice punctured sphere and each edge corresponds to an annulus cusp. Moreover, the hyperbolic structure on a thrice punctured sphere is unique by [@Ada]; hence any orientation preserving homeomorphism between hyperbolic thrice punctured spheres is isotopic to an isometry. Since any homeomorphism between thrice punctured spheres is uniquely determined by its action on the cusps, we may denote homeomorphisms as elements of $S_3$, the symmetry group of degree 3.

Fix labels for the cusps of the thrice punctured spheres as in Figure [1](#fig.move1){reference-type="ref" reference="fig.move1"}. If we glue the boundaries via the homeomorphism corresponding to the identity permutation, then we get the tangle on the left of Figure [1](#fig.move1){reference-type="ref" reference="fig.move1"}. If we glue the boundaries via the homeomorphism corresponding to the permutation interchanging 2 and 3, we get the tangle on the right of Figure [1](#fig.move1){reference-type="ref" reference="fig.move1"}.

![Gluing by a homeomorphism](seq.eps){#fig.seq}

This is illustrated in Figure [2](#fig.seq){reference-type="ref" reference="fig.seq"}. Here we regard $S^3$ as $B^3\cup B^3$ where one ball $B^3$ is a regular neighbourhood of a vertex of the graph shown in the middle of Figure [1](#fig.move1){reference-type="ref" reference="fig.move1"}. We then reverse the inside and the outside with respect to the boundary sphere $S^2 = {\partial}B^3$. After gluing, we get a link or graph in $S^2\times S^1$. The component coming from the cusp labelled by $1$ is a loop which corresponds to a generator of the fundamental group of $S^2\times S^1$, and its complement is homeomorphic to a solid torus. Thus we get a tangle as shown on the left or right of Figure [1](#fig.move1){reference-type="ref" reference="fig.move1"}.

The inverse move (left or right to middle) is valid since any essential thrice punctured sphere (or, $2$-punctured disk) in a hyperbolic 3-manifold is totally geodesic ([@Ada]). Since we are dealing with hyperbolic graphs, the $2$-punctured disk on the left or right of Figure [1](#fig.move1){reference-type="ref" reference="fig.move1"} is essential (see [@Pur] Lemma 2.1). ◻
:::

::: defi
*A *fully augmented link* is a link obtained by applying the gluing moves of Lemma [\[Vol\]](#Vol){reference-type="ref" reference="Vol"} to a planar diagram of a hyperbolic graph (embedded in the plane) so that the resulting graph is actually a link. A *crossing circle* is a component of a fully augmented link which appears as a circle in Figure [1](#fig.move1){reference-type="ref" reference="fig.move1"}. A *knot component* of a fully augmented link is a component which is not a crossing circle.*
:::

::: rmk
*These definitions of a fully augmented link, a crossing circle, and a knot component are equivalent to the original definitions in [@FP] or [@Pur].*
:::

## Polyhedral decomposition for the complement of a hyperbolic graph with a planar diagram {#polyhedral_decomp}

Given a hyperbolic graph $P$ with a planar diagram $D$, let $V$ be the set of vertices of $P$ and $N_P = S^3\setminus P \setminus (\cup_{v\in V} \mathcal{N}(v) )$ where $\mathcal{N}(v)$ is a regular neighbourhood of $v$. Let $\Pi$ be the plane containing $D$. Then $N_P$ admits hyperbolic metric of finite volume with geodesic boundary. We can decompose $N_P$ into two isometric convex ideal hyperbolic polyhedra by the following procedure, depicted in Figure [3](#fig.ATdecomp){reference-type="ref" reference="fig.ATdecomp"}.

Step 1

:   Cut $N_P$ along $\Pi$.

Step 2

:   Collapse each edge of $P$ to a point.

Let $L$ be a fully augmented link which is obtained from $D$ by the gluing moves of Lemma [\[Vol\]](#Vol){reference-type="ref" reference="Vol"}. Then this decomposition is exactly equal to the decomposition of $S^3\setminus L$ found by Agol-Thurston in [@Lac] (see also [@FP], [@Pur]).

![Polyhedral decomposition of a graph complement](ATdecomp.eps){#fig.ATdecomp}

We shade the faces coming from the thrice punctured sphere boundaries of $N_P$ and leave the faces on $\Pi$ white as in [@FP], [@Pur]. Note that every shaded face is an ideal triangle, and since reflection $\phi$ about $\Pi$ leaves each thrice punctured sphere boundary invariant, the shaded faces are all orthogonal to the adjacent white faces. Hence the dihedral angle of each edge is $\pi /2$. Since $\phi$ preserves white faces, each face of these polyhedra is totally geodesic. Hence each white face extends to the boundary at infinity $S^2_{\infty}$ of hyperbolic space to give a Euclidean circle and such circles corresponding to adjacent faces are tangent to each other. Therefore the white faces of each polyhedron determine a circle packing of $S^2_{\infty}$ whose nerve is isomorphic to the dual of the original graph diagram $D$.
