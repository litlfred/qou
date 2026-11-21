---
doc_id: arxiv-1808.02836v2
doc_title: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds Introduction"
section_id: sec-021-53-closed-one-sided-incompressible-surfaces
section_title: "Closed one-sided incompressible surfaces"
section_number: 5.3
pages: 29-32
source_pdf: 1808.02836v2.pdf
source_sha256: 0224a296253122a2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 1.0
doc_brief: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds Introduction — Previous work of the authors studies minimal triangulations of closed 3–manifolds using a characterisation of low"
---
[]{#ssec:closedonesided label="ssec:closedonesided"}

In what follows, the *weight* of a normal surface $S$ in a triangulation $\mathcal{T}$ is defined to be the overall number of intersection points of $S$ with the edges of $\mathcal{T}$.

::: lemma
[]{#lem:chiofS label="lem:chiofS"} Let $M$ be a once-punctured hyperbolic torus bundle and let $\mathcal{T}$ be a monodromy ideal triangulation of $M.$ Furthermore, let $S \subset \mathcal{T}$ be a normal surface of $\mathcal{T}$ which is a taut least weight representative of an even torsion class of $H_2 (M, \mathbb{Z}).$ Then $S$ meets each tetrahedron of $\mathcal{T}$ in a single quadrilateral. Moreover, $\chi(S) = - (\# \textrm{ horizontal quads}).$
:::

::: proof
*Proof.* Let $S \subset \mathcal{T}$ be a normal surface of $\mathcal{T}$ which is a taut representative of a fixed even torsion class $c \in H_2 (M, \mathbb{Z}).$ We assume that $S$ is of least weight amongst all taut representatives. The monodromy ideal triangulation $\mathcal{T}$ naturally endows $M$ with a circular Morse type function: The layering defines a cyclic ordering of pairs of faces forming a once-punctured torus fibre. Let $T$ be such a two-triangle fibre.

Consider the intersection $S \cap T.$ This is a family of embedded disjoint normal simple closed curves in the two-triangle structure on $T.$ A well-known elementary fact is that any such curve is either non separating or vertex linking. Next, note that $S \cap T$ cannot contain two parallel curves, since otherwise we can perform an annular compression using an innermost fibre $0$ weight annulus $A$ and find a new homologous normal surface of less weight or less genus or both.

To be more specific, consider $N(A),$ where $N(A)$ is a small regular neighbourhood of $A.$ Then $S \cap N(A)$ contains two annuli and these are replaced by two annuli in $\partial N(A)$ to form a new surface with the same weight and Euler characteristic as $S$ and representing the same class $c.$ If this surface is disconnected, it is easy to see one component is one-sided and the other is two-sided, as $c$ is a torsion class. Hence we can discard the two-sided component (it must bound in $M$) and the resulting surface still represents $c.$ As this new surface is not normal, it can be isotoped to a normal surface of less weight, giving a contradiction.

Hence, from now on, we can assume that each fibre meets $S$ in one or two curves. Note that in the latter case exactly one curve links the ideal vertex in the fibre and the other curve is non separating. Let $\gamma$ denote the non separating curve in $S \cap T.$

The curve $\gamma \subset T$ is determined by how often it intersects the three edges of $T.$ Since $\gamma$ is connected, these three intersection numbers are pairwise coprime. This can be seen by the fact that, given two intersection numbers, the third one must either be the sum or the non-negative difference of the first two.

A key observation is that $S$ propagates across the tetrahedron $\Delta \in \mathcal{T}$ layered on top of $T$ in a very well-behaved way. In what follows, we denote the edge of $\Delta$ opposite $T$ by $e,$ and the new fibre opposite $T$ (i.e., the two triangles of $\Delta$ containing $e$) by $T'.$

Assume that $S \cap T$ contains a vertex linking curve $\alpha.$ $\alpha$ intersects $T$ in six normal arcs (one of each type). Four of them necessarily yield two normal triangles in $\Delta$ and two normal arcs in $T'.$ For the remaining two arcs, three cases need to be considered.

1\) They are in the boundary of a quadrilateral normal disc in $\Delta.$ In this case, the two normal triangles and the normal quadrilateral containing $\alpha$ intersect both triangles of $T'$ in two parallel normal arcs. Moreover, all other normal arcs of $S \cap T'$ must be of the same type (otherwise $S$ self-intersects inside $\Delta$). In particular, $S \cap T'$ has parallel curves, which contradicts our assumption that $S$ is least weight, using the annular compression argument from above. See Figure [1](#fig:toruslevel_2){reference-type="ref" reference="fig:toruslevel_2"} on the left.

2\) One of them yields a normal triangle $t,$ and the other one is in the boundary of a normal quadrilateral in $\Delta$ together with a normal arc of $\gamma.$ In this case, $S \cap T',$ again consists of one type of normal arc per triangle of $T',$ with two exceptional normal arcs coming from $t.$ Let one triangle of $T'$ contain $k$ and the other one contain $\ell$ copies of parallel normal arcs. Hence, one edge of $T'$ intersects $S$ once, the second one $k+1 = \ell$ times and the third $k$ times, hence, $\ell + 1 = k,$ a contradiction. See Figure [1](#fig:toruslevel_2){reference-type="ref" reference="fig:toruslevel_2"} on the right.

3\) All of the six normal arcs of $\alpha$ are in the boundaries of normal triangles in $\Delta.$ Since 1) and 2) are not possible, this must be the case for all tetrahedra of $\mathcal{T}$ and $S$ contains a boundary parallel torus. This contradicts the assumption that $S$ is a least weight taut representative of $c.$

![Left: The normal arcs of $\alpha$ are in two normal triangles and one normal quadrilateral. Right: The normal arcs of $\alpha$ are in three normal triangles and one normal quadrilateral. []{#fig:toruslevel_2 label="fig:toruslevel_2"}](toruslevel_3){#fig:toruslevel_2 width=".85\\textwidth"}

Hence, for the rest of the proof we can assume that $S \cap T$ is connected for each fibre $T.$ Consequently, it follows that $S \cap T$ has only one or two normal arc types in each triangle of $T,$ since otherwise $S \cap T$ contains a vertex linking component.

We claim that $\Delta$ can only contain vertical normal discs of $S,$ unless $\Delta \cap S$ consists of a single horizontal quad and $S$ intersects two edges of $T$ exactly once, and is disjoint from $e.$

More precisely, there are two cases we have to consider:

1.  The intersection of $S$ with $T$ is disjoint from one of the edges of $T.$ In this case the other two edges must intersect $S$ exactly once. If we layer on the edge disjoint from $S$ then there is a single horizontal quadrilateral in the tetrahedron, if we layer on one of the other edges, there is a single vertical quadrilateral. See Figure [2](#fig:toruslevel){reference-type="ref" reference="fig:toruslevel"} on the right.

2.  The surface $S$ intersects $T$ in two normal arc types per triangle. In this case all normal discs of $S$ in $\Delta$ must necessarily be vertical. To see this note that a horizontal normal quadrilateral can only have two normal arcs of $S \cap T$ in its boundary. Since by the assumption, at least one other normal disc must exist in $\Delta,$ this must be a vertical normal triangle. Arguing as in case 1) and 2) above we can then follow that all three normal arc types must be present per triangle, a contradiction. See Figure [2](#fig:toruslevel){reference-type="ref" reference="fig:toruslevel"} on the left.

It is now easy to verify that the Euler characteristic of $S$ is the negative of the number of horizontal quadrilateral discs, using the circular Morse type function induced by the layering. For each horizontal quadrilateral disc induces a simple saddle type singularity of Morse index one, whereas there are no critical points on vertical triangles or quadrilaterals.

![Left: $S\cap T$ has two normal arc types per triangle of $T.$ Right: $S\cap T$ is disjoint from one edge of $T.$[]{#fig:toruslevel label="fig:toruslevel"}](toruslevel_2){#fig:toruslevel width=".85\\textwidth"}

Since $S$ is taut, no component can be a torus or Klein bottle. Hence there must be at least one horizontal quadrilateral. We can cut $M$ open along a corresponding fibre $T$ to form a product of the form $T \times I$ where $T$ is a once punctured torus. This product admits an induced ideal triangulation which is minimal layered.

There are two steps to complete the proof. The first is to follow the argument in [@Rubinstein-one-sided-1978 Theorem 12] which shows that there is a unique isotopy class of incompressible surfaces in a lens space with even fundamental group. We want to apply a similar argument to an incompressible surface $S^*$ in a product of a once punctured torus and an interval.

Consider a product $X= T \times I$ where $T$ is a once punctured torus and there are two essential boundary curves $C, C'$ in $T \times \{0\}, T \times \{1\}$ respectively and the intersection number of $C,C'$ is even when projected to a copy of $T.$ We claim there is a unique incompressible surface $S^*$ up to isotopy with $\partial S^* = C \cup C'.$

Pick an annulus $A$ in the product structure of $X$ with boundary curve on $T \times \{1\}$ parallel to $C'.$ We can assume without loss of generality that $A$ is transverse to $S^*$ and the intersection $A \cap S^*$ contains only arcs which are essential on $S^*$ and have both ends on $T \times \{0\}.$ An innermost such an arc on $A$ cuts off a bigon which can be used to perform a boundary compression of $S^*$ across $T \times \{0\}.$ Exactly as in [@Rubinstein-one-sided-1978], this boundary compression must change the boundary curve $C$ of $\partial S^*$ to a new curve which has smaller intersection number with $C'.$ It is now easy to show as in [@Rubinstein-one-sided-1978] that this process produces a unique family of bands attached to a collar about $C$ forming $S^*$ which is therefore unique up to isotopy.

The second step is to observe that the canonical quadrilateral surface in the induced ideal layered triangulation of the product is incompressible. The proof again follows [@Rubinstein-one-sided-1978]. The key idea is to use induction and the recursion formula for the genus of the incompressible surface. By removing the tetrahedra up to the first containing a horizontal quadrilateral, we obtain a new product with an induced minimal layered triangulation. The recursion formula for the change in boundary slope and the genus matches the formula in [@Rubinstein-one-sided-1978] and this shows that the canonical quadrilateral surface must be incompressible as it is a minimal genus cobordism surface connecting $C$ and $C'.$ This completes the proof. ◻
:::

::: corollary
[]{#cor:rank2minimalbundle label="cor:rank2minimalbundle"} Let $M$ be a once-punctured hyperbolic torus bundle and let $\mathcal{T}$ be a monodromy ideal triangulation of $M.$ Suppose that $H_2 (M, \mathbb{Z})$ contains a Klein $4$-group $H.$ Then $$|\mathcal{T}| = \sum \limits_{0 \neq c \in H} || \ c\ ||,$$ and in particular $\mathcal{T}$ is a minimal triangulation.
:::

::: proof
*Proof.* For each of the three non-trivial classes in $H$ we have least weight taut normal representatives. We know from the first part of Lemma [\[lem:chiofS\]](#lem:chiofS){reference-type="ref" reference="lem:chiofS"} that each of them meets each tetrahedron of $\mathcal{T}$ in exactly one normal quadrilateral. Moreover, since $H$ is a Klein $4$-group, the sum of all three representatives must have edge weight zero mod two. It follows that every tetrahedron contains all three quadrilateral types exactly once. In particular, in each tetrahedron exactly one of the three representatives has a single horizontal normal quadrilateral.

Hence, by the second part of Lemma [\[lem:chiofS\]](#lem:chiofS){reference-type="ref" reference="lem:chiofS"} the negative of the sum of Euler characteristics of these three representatives must equal the number of tetrahedra of $\mathcal{T}.$ It now follows from Theorem [\[thm:sumofnorms\]](#thm:sumofnorms){reference-type="ref" reference="thm:sumofnorms"} that $\mathcal{T}$ is minimal. ◻
:::

Combining Corollary [\[cor:rank2minimalbundle\]](#cor:rank2minimalbundle){reference-type="ref" reference="cor:rank2minimalbundle"} with the covering argument provided in §[\[subsec:Reduction using coverings\]](#subsec:Reduction using coverings){reference-type="ref" reference="subsec:Reduction using coverings"} proves Theorem [\[thm:torusbundles\]](#thm:torusbundles){reference-type="ref" reference="thm:torusbundles"}.
