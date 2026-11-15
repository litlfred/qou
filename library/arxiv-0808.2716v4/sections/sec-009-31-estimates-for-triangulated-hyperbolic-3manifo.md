---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF F AREY MANIFOLDS"
section_id: sec-009-31-estimates-for-triangulated-hyperbolic-3manifo
section_title: "Estimates for triangulated hyperbolic 3–manifolds"
section_number: 3.1
pages: 12-17
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
doc_brief: "CUSP AREAS OF F AREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on t he cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2 –bridge link"
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.979
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

## Parameterization by radii of Ford domain faces {#subsec:param}

We now restrict our attention to the case of Farey manifolds. Suppose, for the moment, that $M$ is a punctured torus bundle. Consider one zigzag of $M$; this is a punctured torus $T$. From the canonical triangulation on $M$, $T$ inherits a triangulation. Edges are dual to faces of the Ford domain of $M$. Since $T$ is a punctured torus, there are only three edges in a triangulation of $T$, and two triangles. Thus the zigzag of $T$ meets six hemispheres of the Ford domain, which are identified in pairs. See Figure [1](#fig:torus-lengths){reference-type="ref" reference="fig:torus-lengths"}.

<figure id="fig:torus-lengths">

<figcaption>Euclidean distances in the universal cover of a zigzag. The translation from the left-most to the right-most edge represents one meridian in a punctured torus, or two meridians in a <span class="math inline">4</span>–punctured sphere.</figcaption>
</figure>

Let $F_a$ be a face of the Ford domain whose radius is largest among the faces dual to the pleating locus of $T$. (In other words, $F_a$ is dual to the edge of the pleating that is shortest outside the maximal cusp.) Conjugate ${\mathbb{H}}^3$ such that the distance between the center of $F_a$ and the center of the nearest adjacent face of the Ford domain to the right ($F_b$, say) is $1$. Let $a$ denote the radius of $F_a$, $b$ the radius of $F_b$.

By Lemma [\[lemma:ford-circles\]](#lemma:ford-circles){reference-type="ref" reference="lemma:ford-circles"}, the other circle of the Ford domain which is met by $T$ has radius $ab$. Call this face $F_{ab}$. By following the triangulation of a once punctured torus, we see the Euclidean lengths between centers of horospheres must be as in Figure [1](#fig:torus-lengths){reference-type="ref" reference="fig:torus-lengths"}.

This parameterization for a pleated punctured torus extends easily to $4$--punctured spheres. In an ideal triangulation of a $4$--punctured sphere $S$, there are six edges and four ideal triangles --- double the complexity above. However, recall that we have chosen the cusp neighborhoods and the canonical triangulation equivariantly. As a result, the zigzag of $S$ will look the same when viewed from each cusp. When viewed from any puncture of $S$, the zigzag crosses three faces of the Ford domain, whose radii will be $a$, $b$, and $ab$.

We are interested in the sizes of horospheres at the bottom of each edge in Figure [1](#fig:torus-lengths){reference-type="ref" reference="fig:torus-lengths"}.

::: lemma
Suppose that when we lift to ${\mathbb{H}}^3$, the maximal cusp of $M$ lifts to a horosphere at height $h$, while the zigzag has Euclidean distances and radii as above. Then the distances between horospheres along the edges dual to $F_a$, $F_b$ and $F_{ab}$ are $2\log(h/a)$, $2\log(h/b)$, and $2\log(h/(ab))$, respectively.

Thus if we conjugate again such that the maximal cusp of $M$ lifts to a horosphere of height $1$, then we see horospheres of diameter $a^2/h^2$, $b^2/h^2$, and $a^2b^2/h^2$, respectively. []{#lemma:horo-sizes label="lemma:horo-sizes"}
:::

::: proof
*Proof.* Recall that the face $F_a$ is equidistant from the horosphere of height $h$ about infinity and another horosphere which lies under $F_a$. Thus the distance between the face $F_a$ and the horosphere below it must equal the distance between the face of radius $a$ and the horosphere of height $h$ above it. Thus the distance between the two horospheres is $2\log(h/a)$.

Now, if we conjugate such that the maximal cusp of $M$ lifts to a horosphere of height $1$, we do not change hyperbolic lengths, so the distance between horospheres is still $2\log(h/a)$. But now, if the diameter of the horosphere centered on ${\mathbb{C}}$ is $d$, this implies $\log(1) - \log(d) = 2\log(h/a)$, or $d= a^2/h^2$.

The argument is the same for horospheres under $F_b$ and $F_{ab}$. ◻
:::

By Lemma [\[lemma:horo-sizes\]](#lemma:horo-sizes){reference-type="ref" reference="lemma:horo-sizes"}, the largest horosphere has diameter the maximum of $a^2/h^2$, $b^2/h^2$, and $a^2b^2/h^2$. But we chose $F_a$ so that $a$ was the maximum of $a$, $b$, and $ab$. So the largest horosphere has diameter $a^2/h^2$.

To improve estimates, we may use the fact that faces of the Ford domain meet in a certain pattern in the three dimensional manifold $M$ as well as in the surface $S$. We will need the following lemma about angles between faces of the Ford domain. This lemma was first observed in a slightly different form by Guéritaud [@gueritaud:thesis Page 29].

::: lemma
[]{#lemma:cos-bound label="lemma:cos-bound"} Let $F_A$, $F_B$, $F_C$ and $F_E$ be faces of the Ford domain corresponding to a single zigzag, with $F_A$ adjacent to $F_B$, $F_B$ to $F_C$, and $F_C$ to $F_E$. Suppose also that $F_A$, $F_B$, and $F_C$ are dual to a canonical tetrahedron. Denote by $A$ the Euclidean radius of the hemisphere $F_A$ (which is also the radius of $F_E$), and denote by $C$ the Euclidean radius of $F_C$. Denote the distance between the centers of $F_E$ and $F_C$ by $D$. Let $\alpha$ denote the angle between the line segments from the center of $F_B$ to the center of $F_C$, and from the center of $F_B$ to the center of $F_A$. Then the angle $\alpha$ satisfies $$\cos{\alpha} >
 \frac{ A^4 + C^4 + D^4 - 2A^2 D^2 - 2 C^2 D^2}
            {2 A^2 C^2}.$$
:::

::: proof
*Proof.* Note that $\alpha$ is the dihedral angle of a tetrahedron in the canonical triangulation. That tetrahedron is dual to the point of intersection of faces $F_A$, $F_B$, and $F_C$. The key fact that we will use is that these three faces must overlap.

Consider the circles given by the points where the spheres of $F_A$ and $F_B$ meet the boundary at infinity. We will abuse notation and call these circles $F_A$ and $F_B$. Consider a third circle $C(\beta)$ with radius $C$ such that the line between the center of this circle and the center of $F_B$ makes an angle $\beta$ with the line between the center of $F_B$ and the center of $F_A$. When $\beta=\alpha$, this circle $C(\beta)$ is the circle of $F_C$. See Figure [2](#fig:circle-lemma){reference-type="ref" reference="fig:circle-lemma"}(a).

However, we want to consider varying $\beta$. The angle $\beta$ can lie anywhere in the interval $(0,\pi)$. For large $\beta$, the circle $C(\beta)$ may not meet $F_A$. We can decrease $\beta$ until these two circles overlap. Since $F_A$, $F_B$, and $F_C$ are dual to a tetrahedron of the canonical triangulation, when $\beta= \alpha$, $C(\alpha)$ and $F_A$ must overlap enough that the interiors of the regions bounded by these circles and by $F_B$ intersect nontrivially. Thus $\alpha$ must be strictly less than the value of $\beta$ for which the three circles meet in a single point. We will find this value of $\beta$. See Figure [2](#fig:circle-lemma){reference-type="ref" reference="fig:circle-lemma"}(b).

<figure id="fig:circle-lemma">
<table>
<tbody>
<tr class="odd">
<td style="text-align: center;">(a)</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;">(b)</td>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table>
<figcaption>(a) The circles of <span class="math inline"><em>F</em><sub><em>A</em></sub></span>, <span class="math inline"><em>F</em><sub><em>B</em></sub></span>, <span class="math inline"><em>C</em>(<em>β</em>)</span>. (b) The value of <span class="math inline"><em>β</em></span> for which the faces meet in a single point.</figcaption>
</figure>

Now, given the distance $D$ and the radii $A$ and $C$, we can compute all the other distances and radii of the zigzag, using Lemma [\[lemma:ford-circles\]](#lemma:ford-circles){reference-type="ref" reference="lemma:ford-circles"}. In particular, the radius of $F_B$ is $AC/D$. The distance between centers of $F_A$ and $F_B$ is $A^2/D$, and the distance between the centers of $F_B$ and $F_C$ is $C^2/D$.

Without loss of generality, suppose $F_B$ has center $(0,0)$, and $F_A$ has center $(A^2/D, 0)$. Here we are writing points in ${\mathbb{C}}$ as points in ${\mathbb{R}}^2$. Then the center of $C(\beta)$ is $$((C^2/D)\cos{\beta}, (C^2/D)\sin{\beta}).$$

The value of $\beta$ for which the three circles meet in a single point will be determined as follows. The circles of $F_A$ and of $F_B$ intersect in two points which lie on a line $\ell_{AB}$ between the circles. Similarly, the circles of $F_B$ and of $C(\beta)$ intersect in two points which lie on a line $\ell_{BC}$. Notice that the three circles meet in a single point exactly when the lines $\ell_{AB}$ and $\ell_{BC}$ intersect in a point which lies on the circle of $F_B$. We therefore compute these lines and their intersection.

The line $\ell_{AB}$ is given by the intersection of the circles $(x-A^2/D)^2 + y^2 = A^2$, and $x^2 + y^2 = (AC/D)^2$. This has equation: $$x = \frac{A^2 + C^2 - D^2}{2D}.$$ Similarly, the line $\ell_{BC}$ has equation: $$(\cos\beta)x +(\sin\beta)y = \frac{A^2 + C^2 - D^2}{2D}$$ Their intersection is therefore the point $$\left( \frac{A^2 + C^2 - D^2}{2D}, \frac{A^2 + C^2 - D^2}{2D}
    \left(\frac{1-\cos\beta}{\sin\beta}\right)\right).
\label{eqn:point}$$

We want this point to lie on the circle $x^2 + y^2 = (AC/D)^2$. Plugging the point ([\[eqn:point\]](#eqn:point){reference-type="ref" reference="eqn:point"}) into the equation of the circle, we find $\beta$ satisfies $$\left( \frac{A^2 + C^2 - D^2}{2D} \right)^2 \left(1 +
\left(\frac{1-\cos\beta}{\sin\beta}\right)^2 \right) =
\frac{A^2 C^2}{D^2},$$ which simplifies to $$\frac{2}{1+ \cos \beta}
= \left(\frac{2 AC}{A^2 + C^2 - D^2}\right)^2.$$ Thus $$\cos \beta \: = \:  \frac{(A^2 + C^2 - D^2)^2}{2A^2 C^2} - 1 \: = \: 
\frac{ A^4 + C^4 + D^4 - 2A^2 D^2 - 2 C^2 D^2}{2 A^2 C^2}.$$

Since $\alpha$ is strictly less than this $\beta$, and $0<\alpha<\pi$, $\cos\alpha$ must be strictly greater than $\cos\beta$. This completes the proof. ◻
:::
