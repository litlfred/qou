---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-021-64-moving-paths-in-the-1skeleton-of-the-associah
section_title: "Moving paths in the 1–skeleton of the associahedron using 2–3 and 0–2 moves"
section_number: 6.4
pages: 41-43
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.964
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
[]{#sub.moving.paths label="sub.moving.paths"}

In order to carry out step ([\[retriangulate step 2\]](#retriangulate step 2){reference-type="ref" reference="retriangulate step 2"}) of our plan in Remark [\[retriangulate strategy\]](#retriangulate strategy){reference-type="ref" reference="retriangulate strategy"}, we need to modify the layered triangulations in the polygonal pillows. We will do this using the 2--3, 3--2, 0--2 and 2--0 moves allowed in Theorems [\[thm.00\]](#thm.00){reference-type="ref" reference="thm.00"} and [\[thm.20move.index\]](#thm.20move.index){reference-type="ref" reference="thm.20move.index"}.\
Having completed step ([\[retriangulate step 1\]](#retriangulate step 1){reference-type="ref" reference="retriangulate step 1"}), we have two triangulations, $\mathcal{T}_1$ and $\mathcal{T}_2$, which agree on the polyhedra but may differ in the polygonal pillows. Let $Q$ be a polygonal pillow. Since $\mathcal{T}_1$ and $\mathcal{T}_2$ agree on the polyhedra glued to either side of $Q$, they agree on the triangulations of the polygonal faces $Q_+$ and $Q_-$. Call these triangulations $t_+$ and $t_-$.\
The next well-known theorem concerns the identification of the set of triangulations of an $n$-gon with the vertices of the *associahedron* $K_{n-2}$, and the set of geometric bistellar flips with the edges of $K_{n-2}$. The associahedron $K_{n-2}$ was introduced by Stasheff [@Stasheff:1963]. An identification of $K_{n-2}$ with a convex polytope in Euclidean space was given in the appendix to [@Stasheff:Luminy]. The cellular decomposition of the polytope $K_{n-2}$ (and in particular, its 2-skeleton) is discussed at length in the above references and also in [@Loday]. The fact that the 2-dimensional faces of the associahedron are squares and pentagons also follows from MacLane's coherence theorem [@MacLane]. A vast generalization of regular triangulations of point configurations was studied by Gelfand-Kapranov-Zelevinsky, and in [@GKZ Sec.7.3] it is explained how to identify the secondary polytope of 2-dimensional configurations with the associahedron.

::: thm
[]{#associahedron properties label="associahedron properties"} The set of triangulations of an $n$--gon and the set of diagonal flips connecting them correspond to the vertices and edges of a convex polytope called the *associahedron*. The set of 2--cells of the associahedron consists of squares and pentagons. Each square corresponds to two commuting diagonal flips (as in Definition [\[diagonal flip\]](#diagonal flip){reference-type="ref" reference="diagonal flip"}) on two 4-gons whose interiors are disjoint. Each pentagon corresponds to a *pentagon relation* between the five triangulations of a pentagon. See Figure [1](#associahedron 2-cells){reference-type="ref" reference="associahedron 2-cells"}.
:::

<figure id="associahedron 2-cells">

<figcaption>The 2–cells of the associahedron.</figcaption>
</figure>

Our two layered triangulations of the polygonal pillow $Q$ can be represented as two paths $p_1$ and $p_2$ in the 1--skeleton of the associahedron that both start at the vertex corresponding to $t_-$ and end at the vertex corresponding to $t_+$. Since the fundamental group of the 2--skeleton $X^{(2)}$ of a CW complex $X$ satisfies $\pi_1(X^{(2)})=\pi_1(X)$, it follows that the 2--skeleton of a convex polytope is simply connected, and every loop along the 1-skeleton can be trivialized by moving pieces of it across the 2-cells. It follows that the 2--skeleton of the associahedron is simply connected, and so we can homotope $p_1$ to $p_2$, fixing endpoints, by moving the path across some finite sequence of the 2--cells. To be precise, we can homotope $p_1$ to $p_2$ with a combination of the following moves and their inverses.

1.  Remove a *backtracking*, that is, replace a segment of a path of the form $\ldots,t_1, t_2, t_1,\ldots$ with $\ldots, t_1, \ldots$, where $t_1$ and $t_2$ are related by a diagonal flip. []{#associahedron isotope 2-0 label="associahedron isotope 2-0"}

2.  Move a path that follows two consecutive sides of a square 2--cell to follow the other two sides. []{#associahedron isotope 2-2 label="associahedron isotope 2-2"}

3.  Move a path that follows three consecutive sides of a square 2--cell to follow the other side. []{#associahedron isotope 3-1 label="associahedron isotope 3-1"}

4.  Delete a part of a path that goes around all four sides of a square 2--cell. []{#associahedron isotope 4-0 label="associahedron isotope 4-0"}

5.  Move a path that follows three consecutive sides of a pentagon 2--cell to follow the other two sides. []{#associahedron isotope 3-2 label="associahedron isotope 3-2"}

6.  Move a path that follows four consecutive sides of a pentagon 2--cell to follow the other side. []{#associahedron isotope 4-1 label="associahedron isotope 4-1"}

7.  Delete a part of a path that goes around all five sides of a pentagonal 2--cell. []{#associahedron isotope 5-0 label="associahedron isotope 5-0"}

These moves can be achieved as follows.

-   Move ([\[associahedron isotope 2-0\]](#associahedron isotope 2-0){reference-type="ref" reference="associahedron isotope 2-0"}) corresponds to performing a 2--0 move on the triangulation. Since the two triangulations are both in $\mathcal X_M^{\mathrm{EP}}$, they are both 1--efficient by Remark [\[Xbar\^EP 1-efficient\]](#Xbar^EP 1-efficient){reference-type="ref" reference="Xbar^EP 1-efficient"}. Therefore the two triangulations have the same index by Theorem [\[thm.20move.index\]](#thm.20move.index){reference-type="ref" reference="thm.20move.index"}.

-   Move ([\[associahedron isotope 2-2\]](#associahedron isotope 2-2){reference-type="ref" reference="associahedron isotope 2-2"}) does not change the layered triangulation at all, it only swaps the order in which we add two non-overlapping flat tetrahedra to the layering.

-   Move ([\[associahedron isotope 3-1\]](#associahedron isotope 3-1){reference-type="ref" reference="associahedron isotope 3-1"}) can be made by applying move ([\[associahedron isotope 2-2\]](#associahedron isotope 2-2){reference-type="ref" reference="associahedron isotope 2-2"}) followed by move ([\[associahedron isotope 2-0\]](#associahedron isotope 2-0){reference-type="ref" reference="associahedron isotope 2-0"}).

-   Move ([\[associahedron isotope 4-0\]](#associahedron isotope 4-0){reference-type="ref" reference="associahedron isotope 4-0"}) can be made by applying move ([\[associahedron isotope 2-2\]](#associahedron isotope 2-2){reference-type="ref" reference="associahedron isotope 2-2"}) followed by move ([\[associahedron isotope 2-0\]](#associahedron isotope 2-0){reference-type="ref" reference="associahedron isotope 2-0"}) twice.

-   Move ([\[associahedron isotope 3-2\]](#associahedron isotope 3-2){reference-type="ref" reference="associahedron isotope 3-2"}) corresponds to performing a 3--2 move on the triangulation. As before, since the two triangulations are both in $\mathcal X_M^{\mathrm{EP}}$, they are both 1--efficient by Remark [\[Xbar\^EP 1-efficient\]](#Xbar^EP 1-efficient){reference-type="ref" reference="Xbar^EP 1-efficient"}. Therefore the two triangulations have the same index by Theorem [\[thm.00\]](#thm.00){reference-type="ref" reference="thm.00"}(b).

-   Move ([\[associahedron isotope 4-1\]](#associahedron isotope 4-1){reference-type="ref" reference="associahedron isotope 4-1"}) can be made by applying move ([\[associahedron isotope 3-2\]](#associahedron isotope 3-2){reference-type="ref" reference="associahedron isotope 3-2"}) followed by move ([\[associahedron isotope 2-0\]](#associahedron isotope 2-0){reference-type="ref" reference="associahedron isotope 2-0"}).

-   Move ([\[associahedron isotope 5-0\]](#associahedron isotope 5-0){reference-type="ref" reference="associahedron isotope 5-0"}) can be made by applying move ([\[associahedron isotope 3-2\]](#associahedron isotope 3-2){reference-type="ref" reference="associahedron isotope 3-2"}) followed by move ([\[associahedron isotope 2-0\]](#associahedron isotope 2-0){reference-type="ref" reference="associahedron isotope 2-0"}) twice.

::: proof
*Proof of Theorem [\[thm.2\]](#thm.2){reference-type="ref" reference="thm.2"}.* We have shown in this section that given any two triangulations in $\mathcal X_M^{\mathrm{EP}}$, the steps in Remark [\[retriangulate strategy\]](#retriangulate strategy){reference-type="ref" reference="retriangulate strategy"} can be made using 2--3, 3--2, 0--2 and 2--0 moves which preserve the index. Thus the entire class of triangulations has the same index. Since $\mathcal X_M^{\mathrm{EP}}$ depends only on the topology of $M$, we can take the index of any of these triangulations for the value of the index for the manifold, and this depends only on the topology of $M$. ◻
:::

::: proof
*Proof of Theorem [\[thm.3\]](#thm.3){reference-type="ref" reference="thm.3"}.* Fix a cusped hyperbolic manifold $M$ and $\mathcal{T}\in \mathcal X_M^{\mathrm{EP}}$. $\mathcal{T}$ consists of two types of tetrahedra: the ones that subdivide the ideal hyperbolic cells of the Epstein-Penner cell decomposition of $M$, and the ones that are parts of the pillows. The former have geometric shapes (i.e., shapes that are in the upper half plane), and the latter have real non-degenerate shapes. By construction, the shapes $Z_{\mathcal{T}}$ satisfy the gluing equations of $\mathcal{T}$, proving part (a). Their arguments also satisfy the gluing equations, proving part (c).

Also by construction, the shapes $Z_{\mathcal{T}}$ and $Z_{\mathcal{T}'}$ are related by 2--3, 3--2, 0--2 and 2--0 moves if the corresponding triangulations $\mathcal{T}$ and $\mathcal{T}'$ are related by the same moves. ◻
:::
