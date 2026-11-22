---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF FAREY MANIFOLDS"
section_id: sec-014-32-parameterization-by-radii-of-ford-domain-face
section_title: "Parameterization by radii of Ford domain faces"
section_number: 3.2
pages: 14-17
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 0.981
doc_brief: "CUSP AREAS OF FAREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on the cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2–bridge link complements."
---
[]{#subsec:param label="subsec:param"}

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
