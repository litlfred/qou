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
---
the Ford domain of a cusped hyperbolic manifold M is a union of ﬁnite–sided polyhedra,
with one ideal vertex for each cusp of M . Consider those faces of the Ford domain which
do not meet an ideal vertex. These consist of points that are e quidistant from two or more
lifts of a cusp into H3. Each such face is the portion of a geodesic plane in H3 which can
be “seen” from inﬁnity. That is, the geodesic planes are Eucl idean hemispheres centered
on points of C (here we are considering the boundary at inﬁnity of H3 to be C ∪ {∞}), of
some Euclidean radius. These overlap to cover all of C. Looking down from inﬁnity, one sees
portions of these Euclidean spheres. These are the faces. Th e intersections of two adjacent
faces give edges. The intersections of edges are vertices.
These faces of the Ford domain glue together in pairs. Each pa ir of faces consists of two
hemispheres with identical Euclidean radii, which glue tog ether by some isometry of H3. In
fact this isometry can be taken to be a reﬂection in the face of the Ford domain, followed by
a Euclidean reﬂection (i.e. reﬂection in the vertical plane that is the perpendicular bisector
of the geodesic connecting centers of the two hemispheres), followed by a rotation. See, for
example, Maskit’s book [41, Chapter IV, Section G].
We will be interested in the sizes of the radii, as well as dist ances between centers of the
Euclidean hemispheres that give the faces of the Ford domain . For our applications, the cell
decomposition dual to the Ford domain is always an actual tri angulation, hence we shall talk
about triangles and tetrahedra.
Now, suppose S1 andS2 are two adjacent faces, which are Euclidean hemispheres of r adius
R1 and R2, respectively, and whose centers are Euclidean distance D apart.
Lemma 3.1. R1, R2, and D as above satisfy the triangle inequality:
R1 +R2 >D, R 2 +D>R 1, D +R1 >R 2.
Proof. If D ≥ R1 +R2, the two faces S1 and S2 do not meet, contradicting the fact that
they are adjacent.
IfR2 +D<R 1, then the hemisphere S2 lies completely inside the region bounded by the
complex plane and the hemisphere S1. Thus S2 cannot be a face of the Ford domain. This
is a contradiction. By a symmetric argument, D +R1 >R 2. □
CUSP AREAS OF F AREY MANIFOLDS 13
Now consider the geometric dual of the Ford domain, which we w ill assume is an actual
triangulation. In the universal cover, this dual is given by taking an ideal vertex at the center
of each Euclidean hemisphere face of the Ford domain, and one at inﬁnity. There is one edge
for each hemisphere face of the Ford domain: a geodesic runni ng from inﬁnity down to the
center of the hemisphere. For each intersection of two faces of the Ford domain, there is a
2–cell. By assumption, when we project to the manifold these 2–cells become ideal triangles.
Similarly, the intersection of three adjacent faces is dual to a 3–cell which projects to an
ideal tetrahedron. Finally, note the geometric dual may not be realized as a combinatorial
dual since, for example, the top of a face S of the Ford domain may be covered by another
face of the Ford domain, and thus the geodesic dual to S will run through this other face in
the universal cover before meeting S. However, this will not aﬀect our arguments below.
As above, let S1 and S2 denote adjacent faces of the Ford domain, which are Euclidea n
hemispheres of radius R1 and R2, respectively, and whose centers are Euclidean distance D
apart. Let S′
1 andS′
2 denote the faces that glue to S1 andS2, respectively. So S′
1 andS′
2 are
Euclidean hemispheres of radius R1 and R2 in the universal cover.
Because S1 is adjacent to S2, we may consider the 2–cell which is the geometric dual of
their intersection. By assumption, this is an ideal triangl e in the manifold M . One edge of
this triangle is dual to S1 and its paired face S′
1. We take a lift to H3 such that this edge
runs from inﬁnity straight down the vertical geodesic with e ndpoints inﬁnity and the center
of S1. When it meets S1, it is identiﬁed with the corresponding point (at the center ) of S′
1,
and then runs up the vertical geodesic from the center of S′
1 to inﬁnity. Another edge is dual
to S2 and S′
2, and can be seen in H3 similarly.
This triangle will have a third edge, by assumption, dual to a pair of faces S3 and S′
3.
Here S3 will be a sphere adjacent to S′
1, and S′
3 will be a sphere adjacent to S′
2.
Lemma 3.2. (a) The radius of the spheres S3 and S′
3 is R1R2/D.
(b) The distance between the center of S3 and the center of S′
1 is R2
1/D.
(c) The distance between the center of S′
3 and the center of S′
2 is R2
2/D.
Proof. Consider the universal cover. The isometry gluing S1 to S′
1 takes the point on C at
the center of S1 to inﬁnity. It therefore takes the third edge of the triangle , which lifts to a
geodesic in H3 running from the center of S1 to the center of S2, to a geodesic running from
inﬁnity down to the center of S3.
We may assume without loss of generality that the center of S1 is 0 and the center of S2
is D. The isometry taking S1 to S′
1 is an inversion in S1, followed by a Euclidean reﬂection
and rotation [41]. Since Euclidean reﬂection and rotation d o not aﬀect radii of hemispheres
or distance on C, the lengths are given by determining the corresponding len gths under the
inversion in S1.
Note under this inversion, D maps to R2
1/D, proving part (b). A symmetric argument,
reversing the roles of S1 and S2, gives part (c).
Finally, to show that the size of the radius is as claimed, con sider the point of intersection
of S1 and S2 which lies over the real line. It has coordinates ( x, 0,z ), say. Since this is a
point on S1, it will be taken to itself under the inversion. However, thi s point is on the edge
of the Ford domain where the three faces S1, S2 and S3 meet. Thus it will also lie on S3
after the inversion. So to ﬁnd the radius of S3, we only need to determine the Euclidean
distance between this point of intersection ( x, 0,z ) and the center ( R2
1/D, 0, 0) of S3.
The square of this distance is x2 − 2xR2
1/D +z2. Using the fact that x2 +z2 =R2
1 (since
(x, 0,z ) lies on S1) we simplify this formula to R2
1/D2(D2 − 2Dx +R2
1). Now using the fact
14 D. FUTER, E. KALF AGIANNI, AND J. PURCELL
Fa Fb Fab F ′
a F ′
b F ′
ab
a2b21 1 b2 a2
Figure 5. Euclidean distances in the universal cover of a zigzag. The t rans-
lation from the left-most to the right-most edge represents one meridian in a
punctured torus, or two meridians in a 4–punctured sphere.
that (x, 0,z ) lies on S2, we know x2 − 2Dx +D2 +z2 =R2
2, or R2
1 − 2Dx +D2 =R2
2. Hence
the square of the radius is R2
1R2
2/D2. □
Finally, we prove a general estimate about the lengths of edg es that are not dual to the
Ford domain.
Lemma 3.3. Lete be a geodesic from cusp to cusp in a hyperbolic manifold M . Fix a choice
of horoball neighborhoods. If e is not an edge of the canonical polyhedral decomposition (wi th
respect to this horoball neighborhood), then the length of e is at least ln(2).
Proof. Suppose not. Suppose there exists a geodesic from cusp to cus p which is not a
canonical edge yet has length less than ln(2). Lift to H3. The geodesic lifts to a geodesic γ.
Conjugate such that one endpoint of γ is inﬁnity, and such that the horosphere of height 1
about inﬁnity projects to the cusp. Then the other endpoint o fγ runs through a horosphere
H of diameter greater than 1 /2.
The set of all points equidistant from H and from the horosphere about inﬁnity is a
hemisphere S of radius at least 1 /
√
2. This is not a face of the Ford domain, hence there
must be some face of the Ford domain Fr of radius r, say, which overlaps the highest point
of S. Thus 1 /
√
2< r≤ 1, and the distance d between the center of Fr and the center of S
is at most
√
r2 − 1/2.
On the other hand, there must be a horosphere under the hemisp here Fr of diameter r2.
The distance d between the center of the horosphere of diameter r2 and that of diameter 1 /2
is at least r/
√
2, with equality when the two horospheres are tangent.
Then we have
r√
2 ≤d ≤
√
r2 − 1
2.
This is possible only when r = 1 and d = 1/
√
2. However, in that case the highest point of
S will not be overlapped by Fr. □
3.2. Parameterization by radii of F ord domain faces. We now restrict our attention to
the case of Farey manifolds. Suppose, for the moment, that M is a punctured torus bundle.
Consider one zigzag of M ; this is a punctured torus T . From the canonical triangulation on
M ,T inherits a triangulation. Edges are dual to faces of the Ford domain of M . Since T is a
punctured torus, there are only three edges in a triangulati on of T , and two triangles. Thus
the zigzag of T meets six hemispheres of the Ford domain, which are identiﬁe d in pairs. See
Figure 5.
CUSP AREAS OF F AREY MANIFOLDS 15
Let Fa be a face of the Ford domain whose radius is largest among the f aces dual to the
pleating locus of T . (In other words, Fa is dual to the edge of the pleating that is shortest
outside the maximal cusp.) Conjugate H3 such that the distance between the center of Fa
and the center of the nearest adjacent face of the Ford domain to the right ( Fb, say) is 1.
Let a denote the radius of Fa, b the radius of Fb.
By Lemma 3.2, the other circle of the Ford domain which is met b yT has radius ab. Call
this face Fab. By following the triangulation of a once punctured torus, w e see the Euclidean
lengths between centers of horospheres must be as in Figure 5 .
This parameterization for a pleated punctured torus extend s easily to 4–punctured spheres.
In an ideal triangulation of a 4–punctured sphere S, there are six edges and four ideal triangles
— double the complexity above. However, recall that we have c hosen the cusp neighborhoods
and the canonical triangulation equivariantly. As a result , the zigzag of S will look the same
when viewed from each cusp. When viewed from any puncture of S, the zigzag crosses three
faces of the Ford domain, whose radii will be a, b, and ab.
We are interested in the sizes of horospheres at the bottom of each edge in Figure 5.
Lemma 3.4. Suppose that when we lift to H3, the maximal cusp of M lifts to a horosphere
at height h, while the zigzag has Euclidean distances and radii as above . Then the distances
between horospheres along the edges dual to Fa, Fb and Fab are 2 log(h/a), 2 log(h/b), and
2 log(h/(ab)), respectively.
Thus if we conjugate again such that the maximal cusp of M lifts to a horosphere of height
1, then we see horospheres of diameter a2/h2, b2/h2, and a2b2/h2, respectively.
Proof. Recall that the face Fa is equidistant from the horosphere of height h about inﬁnity
and another horosphere which lies under Fa. Thus the distance between the face Fa and the
horosphere below it must equal the distance between the face of radius a and the horosphere
of height h above it. Thus the distance between the two horospheres is 2 l og(h/a).
Now, if we conjugate such that the maximal cusp of M lifts to a horosphere of height 1,
we do not change hyperbolic lengths, so the distance between horospheres is still 2 log( h/a).
But now, if the diameter of the horosphere centered on C isd, this implies log(1) − log(d) =
2 log(h/a), or d =a2/h2.
The argument is the same for horospheres under Fb and Fab. □
By Lemma 3.4, the largest horosphere has diameter the maximu m of a2/h2, b2/h2, and
a2b2/h2. But we chose Fa so that a was the maximum of a, b, and ab. So the largest
horosphere has diameter a2/h2.
To improve estimates, we may use the fact that faces of the For d domain meet in a certain
pattern in the three dimensional manifold M as well as in the surface S. We will need
the following lemma about angles between faces of the Ford do main. This lemma was ﬁrst
observed in a slightly diﬀerent form by Gu´ eritaud [30, Page 2 9].
Lemma 3.5. LetFA, FB, FC and FE be faces of the Ford domain corresponding to a single
zigzag, with FA adjacent to FB, FB to FC , and FC to FE. Suppose also that FA, FB, and
FC are dual to a canonical tetrahedron. Denote by A the Euclidean radius of the hemisphere
FA (which is also the radius of FE), and denote by C the Euclidean radius of FC . Denote
the distance between the centers of FE andFC byD. Let α denote the angle between the line
segments from the center of FB to the center of FC , and from the center of FB to the center
of FA. Then the angle α satisﬁes
cosα> A4 +C 4 +D4 − 2A2D2 − 2C 2D2
2A2C 2 .
16 D. FUTER, E. KALF AGIANNI, AND J. PURCELL
(a)
β
FB FA
C(β)
(b)
C(β)
FB FA
β
Figure 6. (a) The circles of FA,FB,C(β). (b) The value of β for which the
faces meet in a single point.
Proof. Note that α is the dihedral angle of a tetrahedron in the canonical trian gulation.
That tetrahedron is dual to the point of intersection of face s FA, FB, and FC. The key fact
that we will use is that these three faces must overlap.
Consider the circles given by the points where the spheres of FA andFB meet the boundary
at inﬁnity. We will abuse notation and call these circles FA and FB. Consider a third circle
C(β) with radius C such that the line between the center of this circle and the ce nter of FB
makes an angle β with the line between the center of FB and the center of FA. When β =α,
this circle C(β) is the circle of FC. See Figure 6(a).
However, we want to consider varying β. The angle β can lie anywhere in the interval
(0,π ). For large β, the circle C(β) may not meet FA. We can decrease β until these two
circles overlap. Since FA,FB, andFC are dual to a tetrahedron of the canonical triangulation,
whenβ =α,C(α) and FA must overlap enough that the interiors of the regions bounde d by
these circles and by FB intersect nontrivially. Thus α must be strictly less than the value of
β for which the three circles meet in a single point. We will ﬁnd this value of β. See Figure
6(b).
Now, given the distance D and the radii A andC, we can compute all the other distances
and radii of the zigzag, using Lemma 3.2. In particular, the r adius of FB is AC/D. The
distance between centers of FA andFB isA2/D, and the distance between the centers of FB
and FC is C 2/D.
Without loss of generality, suppose FB has center (0 , 0), and FA has center ( A2/D, 0).
Here we are writing points in C as points in R2. Then the center of C(β) is
((C 2/D) cosβ, (C 2/D) sinβ).
The value of β for which the three circles meet in a single point will be dete rmined as
follows. The circles of FA and of FB intersect in two points which lie on a line ℓAB between
the circles. Similarly, the circles of FB and of C(β) intersect in two points which lie on a
lineℓBC . Notice that the three circles meet in a single point exactly when the lines ℓAB and
ℓBC intersect in a point which lies on the circle of FB. We therefore compute these lines and
their intersection.
The line ℓAB is given by the intersection of the circles ( x −A2/D)2 +y2 = A2, and
x2 +y2 = (AC/D)2. This has equation:
x = A2 +C 2 −D2
2D .
Similarly, the line ℓBC has equation:
(cosβ)x + (sinβ)y = A2 +C 2 −D2
2D
CUSP AREAS OF F AREY MANIFOLDS 17
Their intersection is therefore the point
(2)
(A2 +C 2 −D2
2D ,A2 +C 2 −D2
2D
(1 − cosβ
sinβ
))
.
We want this point to lie on the circle x2 +y2 = (AC/D)2. Plugging the point (2) into
the equation of the circle, we ﬁnd β satisﬁes
(A2 +C 2 −D2
2D
)2(
1 +
(1 − cosβ
sinβ
)2)
= A2C 2
D2 ,
which simpliﬁes to
2
1 + cosβ =
( 2AC
A2 +C 2 −D2
)2
.
Thus
cosβ = (A2 +C 2 −D2)2
2A2C 2 − 1 = A4 +C 4 +D4 − 2A2D2 − 2C 2D2
2A2C 2 .
Since α is strictly less than this β, and 0 < α < π, cos α must be strictly greater than
cosβ. This completes the proof. □
