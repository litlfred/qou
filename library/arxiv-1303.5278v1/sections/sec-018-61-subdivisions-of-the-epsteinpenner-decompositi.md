---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-018-61-subdivisions-of-the-epsteinpenner-decompositi
section_title: "Subdivisions of the Epstein–Penner decomposition"
section_number: 6.1
pages: 32-34
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.958
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
For a once-cusped hyperbolic 3--manifold $M$, the Epstein--Penner decomposition (see [@EP]) divides $M$ into a finite number of ideal hyperbolic polyhedra. This subdivision is canonical, depending only on the topology of the manifold, if $M$ has a single cusp. If $M$ has $r \geq 1$ cusps, then the Epstein-Penner cell decomposition is canonical up to the choice of a scale vector $(t_1,\dots,t_r)$ with $t_1, t_2, \dots, t_r >0$ giving the relative size of the cusps. The scale vector is well-defined up to multiplication by a positive real number. For the purposes of defining our canonical set, we can choose all $t_i$ to be the same.

Very often, the cells of the decomposition are all ideal tetrahedra, but other polyhedra can occur. For many applications, including the use in this paper, we need a subdivision of $M$ into ideal tetrahedra only. It is well known that every cusped 3--manifold has a decomposition into ideal tetrahedra, but one often needs more than a purely topological structure on the tetrahedra. The Epstein--Penner decomposition, coming as it does with a geometric structure, provides all of the nice geometric properties one could want. So, in the cases when the cells of the decomposition are not themselves tetrahedra, we would like to further subdivide the polyhedra into tetrahedra. However, there is no canonical way to subdivide, and it is not even clear if one can subdivide the various polyhedra in a consistent way, so that the triangulations induced on the faces of the polyhedra match when the polyhedra are glued to each other. In particular, it is still unknown whether every cusped hyperbolic 3--manifold admits a *geometric triangulation* (that is, a subdivision into positive volume ideal hyperbolic tetrahedra), either constructed by further subdividing the Epstein--Penner decomposition or otherwise.

However, one can use the Epstein--Penner decomposition to produce an ideal triangulation by subdividing the ideal polyhedra, if we also allow flat tetrahedra inserted between faces of the polyhedra to bridge between incompatible triangulations of those faces. Such an ideal triangulation has a *natural semi-angle structure* (see Remark [\[rem:natural semi-angle structure\]](#rem:natural semi-angle structure){reference-type="ref" reference="rem:natural semi-angle structure"}), and so by Theorem [\[semi-angle =\> 1-efficient\]](#semi-angle => 1-efficient){reference-type="ref" reference="semi-angle => 1-efficient"} all of these triangulations are 1--efficient.

To describe our triangulations more precisely, we use the same notation as in [@HRS].

::: defn
In this paper, the term *polyhedron* will mean a combinatorial object obtained by removing all of the vertices from a 3-cell with a given combinatorial cell decomposition of its boundary. We further require that this can be realised as a positive volume convex ideal polyhedron in hyperbolic 3-space $\mathbb{H}^3$.
:::

::: defn
An (ideal) *polygonal pillow* or *$n$-gonal pillow* is a combinatorial object obtained by removing all of the vertices from a 3-cell with a combinatorial cell decomposition of its boundary that has precisely two faces. The two faces are copies of an $n$-gon identified along corresponding edges.
:::

::: defn
Suppose that $\mathcal{P}$ is a cellulation of a 3-manifold consisting of polyhedra and polygonal pillows with the property that polyhedra are glued to either polyhedra or polygonal pillows, but polygonal pillows are only glued to polyhedra. Then we call $\mathcal{P}$ a *polyhedron and polygonal pillow cellulation*, or for short, a *PPP-cellulation*.
:::

::: defn
[]{#diagonal flip label="diagonal flip"} Let $t$ be a triangulation of a polygon. A *diagonal flip* move changes $t$ as follows. First we remove an internal edge of $t$, producing a four sided polygon, one of whose diagonals is the removed edge. Second, we add in the other diagonal, cutting the polygon into two triangles and giving a new triangulation of the polygon.
:::

::: defn
[]{#layered_triang_of_polygonal_pillow label="layered_triang_of_polygonal_pillow"} Let $Q$ be a polygonal pillow, with triangulations $t_-$ and $t_+$ given on its two polygonal faces $Q_-$ and $Q_+$. By a *layered triangulation of $Q$, bridging between $t_-$ and $t_+$*, we mean a triangulation produced as follows. We are given a sequence of diagonal flips which convert $t_-$ into $t_+$. This gives a sequence of triangulations $t_-=L_1, L_2, \ldots, L_k=t_+$, where consecutive triangulations are related by a diagonal flip. Starting from $Q_-$ with the triangulation $t_-=L_1$, we glue a tetrahedron onto the triangulation $L_1$ so that two of its faces cover the faces of $L_1$ involved in the first diagonal flip. The other two faces together with the rest of $L_1$ produce the triangulation $L_2$. We continue in this fashion, adding one tetrahedron for each diagonal flip until we reach $L_k=t_+$, which we identify with $Q_+$.
:::

Our class of triangulations $\mathcal X_M^{\mathrm{EP}}$ of $M$ consists of triangulations that are subdivisions of PPP-cellulations. Our PPP-cellulation will have polyhedra being the polyhedra of the Epstein-Penner decomposition. It also has a polygonal pillow inserted between all pairs of identified faces that have at least 4 sides. We will form our triangulations by first subdividing the ideal hyperbolic polyhedra into positive volume ideal hyperbolic tetrahedra. Secondly, for each polygonal pillow, we insert any layered triangulation that bridges between the induced triangulations of the two boundary polygons of the polyhedra to each side.

::: rmk
[]{#rem:natural semi-angle structure label="rem:natural semi-angle structure"} Any triangulation produced in the way described above has a *natural semi--angle structure*. This comes from the shapes of the tetrahedra as ideal hyperbolic tetrahedra. The dihedral angles of the positive volume ideal hyperbolic tetrahedra, together with 0 and $\pi$ angles for the flat tetrahedra in the layered triangulations in the polygonal pillows satisfy all of the rules for a generalised angle structure, and all angles are in $[0,\pi]$.
:::

The natural semi--angle structure together with Theorem [\[semi-angle =\> 1-efficient\]](#semi-angle => 1-efficient){reference-type="ref" reference="semi-angle => 1-efficient"} show that each triangulation in our class is 1-efficient. However, we also need to show that our class is connected under 2--3, 3--2, 0--2 and 2--0 moves, and for this we will need some extra machinery. The main tool we will use is the theory of regular triangulations of point configurations, following [@DeLoera:book].
