---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF FAREY MANIFOLDS"
section_id: sec-013-31-estimates-for-triangulated-hyperbolic-3manifo
section_title: "Estimates for triangulated hyperbolic 3–manifolds"
section_number: 3.1
pages: 12-14
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.938
doc_brief: "CUSP AREAS OF FAREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on the cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2–bridge link complements."
---
Recall from Section [\[sec:ford-rev\]](#sec:ford-rev){reference-type="ref" reference="sec:ford-rev"} that the Ford domain of a cusped hyperbolic manifold $M$ is a union of finite--sided polyhedra, with one ideal vertex for each cusp of $M$. Consider those faces of the Ford domain which do not meet an ideal vertex. These consist of points that are equidistant from two or more lifts of a cusp into ${\mathbb{H}}^3$. Each such face is the portion of a geodesic plane in ${\mathbb{H}}^3$ which can be "seen" from infinity. That is, the geodesic planes are Euclidean hemispheres centered on points of ${\mathbb{C}}$ (here we are considering the boundary at infinity of ${\mathbb{H}}^3$ to be ${\mathbb{C}}\cup \{\infty\}$), of some Euclidean radius. These overlap to cover all of ${\mathbb{C}}$. Looking down from infinity, one sees portions of these Euclidean spheres. These are the faces. The intersections of two adjacent faces give edges. The intersections of edges are vertices.

These faces of the Ford domain glue together in pairs. Each pair of faces consists of two hemispheres with identical Euclidean radii, which glue together by some isometry of ${\mathbb{H}}^3$. In fact this isometry can be taken to be a reflection in the face of the Ford domain, followed by a Euclidean reflection (i.e. reflection in the vertical plane that is the perpendicular bisector of the geodesic connecting centers of the two hemispheres), followed by a rotation. See, for example, Maskit's book [@maskit Chapter IV, Section G].

We will be interested in the sizes of the radii, as well as distances between centers of the Euclidean hemispheres that give the faces of the Ford domain. For our applications, the cell decomposition dual to the Ford domain is always an actual triangulation, hence we shall talk about triangles and tetrahedra.

Now, suppose $S_1$ and $S_2$ are two adjacent faces, which are Euclidean hemispheres of radius $R_1$ and $R_2$, respectively, and whose centers are Euclidean distance $D$ apart.

::: lemma
[]{#lemma:triangle-ineq label="lemma:triangle-ineq"} $R_1$, $R_2$, and $D$ as above satisfy the triangle inequality: $$R_1 + R_2 > D, \quad R_2 + D > R_1, \quad D+R_1 > R_2.$$
:::

::: proof
*Proof.* If $D \geq R_1+R_2$, the two faces $S_1$ and $S_2$ do not meet, contradicting the fact that they are adjacent.

If $R_2+ D < R_1$, then the hemisphere $S_2$ lies completely inside the region bounded by the complex plane and the hemisphere $S_1$. Thus $S_2$ cannot be a face of the Ford domain. This is a contradiction. By a symmetric argument, $D+R_1 > R_2$. ◻
:::

Now consider the geometric dual of the Ford domain, which we will assume is an actual triangulation. In the universal cover, this dual is given by taking an ideal vertex at the center of each Euclidean hemisphere face of the Ford domain, and one at infinity. There is one edge for each hemisphere face of the Ford domain: a geodesic running from infinity down to the center of the hemisphere. For each intersection of two faces of the Ford domain, there is a 2--cell. By assumption, when we project to the manifold these 2--cells become ideal triangles. Similarly, the intersection of three adjacent faces is dual to a 3--cell which projects to an ideal tetrahedron. Finally, note the geometric dual may not be realized as a combinatorial dual since, for example, the top of a face $S$ of the Ford domain may be covered by another face of the Ford domain, and thus the geodesic dual to $S$ will run through this other face in the universal cover before meeting $S$. However, this will not affect our arguments below.

As above, let $S_1$ and $S_2$ denote adjacent faces of the Ford domain, which are Euclidean hemispheres of radius $R_1$ and $R_2$, respectively, and whose centers are Euclidean distance $D$ apart. Let $S_1'$ and $S_2'$ denote the faces that glue to $S_1$ and $S_2$, respectively. So $S_1'$ and $S_2'$ are Euclidean hemispheres of radius $R_1$ and $R_2$ in the universal cover.

Because $S_1$ is adjacent to $S_2$, we may consider the 2--cell which is the geometric dual of their intersection. By assumption, this is an ideal triangle in the manifold $M$. One edge of this triangle is dual to $S_1$ and its paired face $S_1'$. We take a lift to ${\mathbb{H}}^3$ such that this edge runs from infinity straight down the vertical geodesic with endpoints infinity and the center of $S_1$. When it meets $S_1$, it is identified with the corresponding point (at the center) of $S_1'$, and then runs up the vertical geodesic from the center of $S_1'$ to infinity. Another edge is dual to $S_2$ and $S_2'$, and can be seen in ${\mathbb{H}}^3$ similarly.

This triangle will have a third edge, by assumption, dual to a pair of faces $S_3$ and $S_3'$. Here $S_3$ will be a sphere adjacent to $S_1'$, and $S_3'$ will be a sphere adjacent to $S_2'$.

::: lemma
1.  The radius of the spheres $S_3$ and $S_3'$ is $R_1R_2/D$.

2.  The distance between the center of $S_3$ and the center of $S_1'$ is $R_1^2/D$.

3.  The distance between the center of $S_3'$ and the center of $S_2'$ is $R_2^2/D$.

[]{#lemma:ford-circles label="lemma:ford-circles"}
:::

::: proof
*Proof.* Consider the universal cover. The isometry gluing $S_1$ to $S_1'$ takes the point on ${\mathbb{C}}$ at the center of $S_1$ to infinity. It therefore takes the third edge of the triangle, which lifts to a geodesic in ${\mathbb{H}}^3$ running from the center of $S_1$ to the center of $S_2$, to a geodesic running from infinity down to the center of $S_3$.

We may assume without loss of generality that the center of $S_1$ is $0$ and the center of $S_2$ is $D$. The isometry taking $S_1$ to $S_1'$ is an inversion in $S_1$, followed by a Euclidean reflection and rotation [@maskit]. Since Euclidean reflection and rotation do not affect radii of hemispheres or distance on ${\mathbb{C}}$, the lengths are given by determining the corresponding lengths under the inversion in $S_1$.

Note under this inversion, $D$ maps to $R_1^2/D$, proving part (b). A symmetric argument, reversing the roles of $S_1$ and $S_2$, gives part (c).

Finally, to show that the size of the radius is as claimed, consider the point of intersection of $S_1$ and $S_2$ which lies over the real line. It has coordinates $(x, 0, z)$, say. Since this is a point on $S_1$, it will be taken to itself under the inversion. However, this point is on the edge of the Ford domain where the three faces $S_1$, $S_2$ and $S_3$ meet. Thus it will also lie on $S_3$ after the inversion. So to find the radius of $S_3$, we only need to determine the Euclidean distance between this point of intersection $(x, 0, z)$ and the center $(R_1^2/D, 0, 0)$ of $S_3$.

The square of this distance is $x^2 -2xR_1^2/D + z^2$. Using the fact that $x^2 + z^2 = R_1^2$ (since $(x,0,z)$ lies on $S_1$) we simplify this formula to $R_1^2/D^2(D^2-2Dx+R_1^2)$. Now using the fact that $(x,0,z)$ lies on $S_2$, we know $x^2 -2Dx + D^2 + z^2 = R_2^2$, or $R_1^2 -2Dx + D^2 = R_2^2$. Hence the square of the radius is $R_1^2R_2^2/D^2$. ◻
:::

Finally, we prove a general estimate about the lengths of edges that are not dual to the Ford domain.

::: lemma
[]{#lemma:length-non-canonical label="lemma:length-non-canonical"} Let $e$ be a geodesic from cusp to cusp in a hyperbolic manifold $M$. Fix a choice of horoball neighborhoods. If $e$ is not an edge of the canonical polyhedral decomposition (with respect to this horoball neighborhood), then the length of $e$ is at least $\ln(2)$.
:::

::: proof
*Proof.* Suppose not. Suppose there exists a geodesic from cusp to cusp which is not a canonical edge yet has length less than $\ln(2)$. Lift to ${\mathbb{H}}^3$. The geodesic lifts to a geodesic $\gamma$. Conjugate such that one endpoint of $\gamma$ is infinity, and such that the horosphere of height $1$ about infinity projects to the cusp. Then the other endpoint of $\gamma$ runs through a horosphere $H$ of diameter greater than $1/2$.

The set of all points equidistant from $H$ and from the horosphere about infinity is a hemisphere $S$ of radius at least $1/\sqrt{2}$. This is not a face of the Ford domain, hence there must be some face of the Ford domain $F_r$ of radius $r$, say, which overlaps the highest point of $S$. Thus $1/\sqrt{2} < r \leq 1$, and the distance $d$ between the center of $F_r$ and the center of $S$ is at most $\sqrt{r^2-1/2}$.

On the other hand, there must be a horosphere under the hemisphere $F_r$ of diameter $r^2$. The distance $d$ between the center of the horosphere of diameter $r^2$ and that of diameter $1/2$ is at least $r/\sqrt{2}$, with equality when the two horospheres are tangent.

Then we have $$\frac{r}{\sqrt{2}} \leq d \leq \sqrt{r^2 - \frac{1}{2}}.$$

This is possible only when $r = 1$ and $d=1/\sqrt{2}$. However, in that case the highest point of $S$ will not be overlapped by $F_r$. ◻
:::
