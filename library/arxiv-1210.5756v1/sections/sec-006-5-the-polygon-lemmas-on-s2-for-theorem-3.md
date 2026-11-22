---
doc_id: arxiv-1210.5756v1
doc_title: "Contact Graphs of Unit Sphere Packings Revisited ∗"
section_id: sec-006-5-the-polygon-lemmas-on-s2-for-theorem-3
section_title: "The Polygon Lemmas on S2 for Theorem 3"
section_number: 5
pages: 8-13
source_pdf: 1210.5756v1.pdf
source_sha256: c7546a79a85b8dd5
toc_source: outline
doc_brief: "Contact Graphs of Unit Sphere Packings Revisited ∗ — The contact graph of an arbitrary ﬁnite packing of unit balls in Euclidean 3-space is the (simple) graph whose vertices correspond to the packing"
---
The Polygon Lemmas on S2 for Theorem 3
On S2, we take a point set X = {x1, ..., xN} with minimum spherical distance π/3 between any two points in
X. The solution to the Newton-Gregory problem (of determining the maximum number of non-overlapping
unit balls which can touch a ﬁxed unit ball) by Sch¨utte and van der Waerden [14] implies that N ≤12.
Taking the Delaunay triangulation DX of X on S2, we notice that we can classify the triangles based on
how many times a side length of greater than π/3 occurs. (For many of the basic properties of Delaunay
triangulations we refer the interested reader to [5] as well as [9].) In fact, we say that an irregular triangle
in DX is of type R where R is the number of side lengths of the triangle greater than π/3. We will reserve
the term regular triangle for the type 0 triangles which have side lengths all equal to π/3. For the sake of
completeness we note that if two points of X lie at (spherical) distance π
3 from each other, then the geodesic
line segment (i.e., great circular arc of length π
3 ) connecting them is an edge of DX on S2. Based on this
we note also that the method described in this section as well as in the following one is quite general and
applies to any triangulation of X on S2 that possesses the above mentioned edge property.
I
II
III
Figure 5: Three types of irregular triangles, types I, II, and III from left to right. Dashed sides represent
side lengths of greater than π/3 and non-dashed sides represent side lengths of exactly π/3.
8
We now prove three lemmas, the Quadrilateral Lemma, the Pentagon Lemma, and the Hexagon Lemma,
which are needed for our proof of Theorem 3. We note that, in what follows, the angles of a regular triangle
(of side length π
3 ) have radian measure arccos(1/3) (= 70.528 . . .◦).
Let C4 denote a spherical quadrilateral of side lengths π/3 which triangulates into two irregular triangles
of type I. The Quadrilateral Lemma ensures that C4 cannot exist in DX when there are two adjacent vertices
of C4 say, v and w such that all of the Delaunay triangles of DX, not in C4, having v or w as a vertex are
regular.
α
β
a
Figure 6: A triangulated C4 quadrilateral with side lengths of π/3.
Lemma 4. (Quadrilateral Lemma)
Let α and β denote the internal angles of C4 subtended at adjacent vertices of C4 as shown in Figure 6.
If α ∈{2π −k arccos(1/3) | k = 1, 2, 3}, then C4 cannot exist in DX and if α = 2π −4 arccos(1/3), then
β /∈{2π −k arccos(1/3) | k = 1, 2, 3, 4}.
Proof. If α = 2π −arccos(1/3) or α = 2π −2 arccos(1/3), then C4 is non-convex with α > π, a contradiction.
So, either α = 2π −3 arccos(1/3) or α = 2π −4 arccos(1/3). By the (ﬁrst) law of cosines (see for example
[12]),
a = arccos
1 + 3 cos α
4

From the symmetry of C4 about the diagonal and the ﬁrst law of cosines,
β/2 = arccos
1 −cos a
√
3 sin a

We now consider our possible cases for varying α,
Table 1. Cases for the Quadrilateral Lemma
Cases
α
a
β
(1)
1.359
1.151
2.373
(2)
2.590
1.970
1.029
In Case (2) we have that β = 1.029 < π/3 and so, the corresponding two vertices of C4 lie closer to each other
than π
3 , a contradiction. In Case (1), which is realizable, we have β /∈{2π−k arccos(1/3) | k = 1, 2, 3, 4}.
Let C5 denote a spherical pentagon of side lengths π/3 which triangulates into two irregular triangles of
type I and one irregular triangle of type II, as shown in Figure 7. The Pentagon Lemma ensures that C5
cannot exist in DX when all of the Delaunay triangles of DX, not in C5, sharing a vertex in common with
C5 are regular.
9
β`
β`
α
ω
α`
α`
a
β
b
Figure 7: A triangulated C5 pentagon with side lengths of π/3.
Lemma 5. (Pentagon Lemma)
Let α and β denote the non-adjacent internal angles of C5 subtended at the vertices of the type I triangles
of C5, and let ω denote the interior angle of the type II triangle of C5 opposite to the only side of the
type II triangle with length π/3, as shown in Figure 7. If α, β ∈{2π −k arccos(1/3) | k = 3, 4}, then
α′ + β′ + ω /∈{2π −k arccos(1/3) | k = 1, 2, 3, 4}, where α′ and β′ are the internal angles of the two type I
irregular triangles not equal to α and β, respectively.
Proof. Letting α, β ∈{2π −k arccos(1/3) | k = 3, 4}, we can consider three cases: (1) α = β = 2π −
4 arccos(1/3), (2) α = β = 2π −3 arccos(1/3), and (3) α̸ = β. Letting a and b denote the side lengths
opposite to α and β in the corresponding type I triangles, we can compute the side lengths a and b and the
internal angles α′, β′, ω by the ﬁrst law of cosines,
a = arccos
1 + 3 cos α
4

b = arccos
1 + 3 cos β
4

α′ = arccos
1 −cos a
√
3 sin a

β′ = arccos
1 −cos b
√
3 sin b

ω = arccos
cos(π/3) −cos a cos b
sin a sin b

We now consider our possible cases for varying α and β,
Table 2. Cases for the Pentagon Lemma
Cases
α
β
a
b
α′
β′
ω
α′ + β′ + ω
(1)
1.359
1.359
1.151
1.151
1.1867
1.1867
1.158
3.532
(2)
2.590
2.590
1.970
1.970
0.5148
0.5148
1.147
2.176
(3)
1.359
2.590
1.151
1.970
1.1867
0.5148
0.671
2.373
Therefore, we have that in each case, α′ + β′ + ω /∈{2π −k arccos(1/3) | k = 1, 2, 3, 4}.
Let C6 denote a spherical hexagon of side lengths π/3 which triangulates into three irregular triangles
of type I and one irregular triangle of type III, as shown in Figure 8. Let C′
6 denote a spherical hexagon
of side lengths π/3 which triangulates into two irregular triangles of type I and two irregular triangles of
type II, as shown in Figure 9. Let C′′
6 denote a spherical hexagon of side lengths π/3 which triangulates into
two irregular triangles of type I and two irregular triangles of type II, as shown in Figure 10. The Hexagon
Lemma ensures that neither C6, C′
6 nor C′′
6 can exist in DX when all of the Delaunay triangles of DX, not
in C6, C′
6 or C′′
6 , sharing a vertex in common with either C6, C′
6, or C′′
6 are regular. The cases of C6, C′
6,
and C′′
6 hexagons are the only possible Delaunay triangulations of a hexagon (into irregular ones), so they
are the only cases we need to consider for a spherical hexagon occurring as the union of triangles in DX.
10
Lemma 6. (Hexagon Lemma)
Let α, β, α′, β′, γ, and ω denote the internal angles of C6 as shown in Figure 8.
If α, β, γ ∈{2π −
k arccos(1/3) | k = 3, 4}, then α′ + β′ + ω /∈{2π −k arccos(1/3) | k = 1, 2, 3, 4}.
Let α, β, θ, β′, γ′, and ω denote the internal angles of C′
6 as shown in Figure 9.
If α, β ∈{2π −
k arccos(1/3) | k = 3, 4} and θ ∈{2π −k arccos(1/3) | k = 1, 2, 3, 4}, then β′ + γ′ + ω /∈{2π −
k arccos(1/3) | k = 1, 2, 3, 4}.
Let α, β, θ, γ′, and ω denote the internal angles of C′′
6 as shown in Figure 10. If α, β ∈{2π−k arccos(1/3) | k =
3, 4} and θ ∈{2π −k arccos(1/3) | k = 1, 2, 3, 4}, then ω + γ′ /∈{2π −k arccos(1/3) | k = 1, 2, 3, 4}.
Proof. For the case of C6, let α, β, γ ∈{2π −k arccos(1/3) | k = 3, 4} and let a, b, and c denote the side
lengths opposite to α, β, and γ in the corresponding type I triangles. Then we can compute the side lengths
a, b, and c and the internal angles α′, β′, ω by the ﬁrst law of cosines as,
a = arccos
1 + 3 cos α
4

, b = arccos
1 + 3 cos β
4

, c = arccos
1 + 3 cos γ
4

α′ = arccos
1 −cos a
√
3 sin a

β′ = arccos
1 −cos b
√
3 sin b

ω = arccos
cos c −cos a cos b
sin a sin b

We now consider our possible cases for varying α, β, and γ. By symmetry we need to look at only the
following cases,
Table 3. Cases for C6 of the Hexagon Lemma
α
β
γ
a
b
c
α′
β′
ω
α′ + β′ + ω
1.359
1.359
1.359
1.151
1.151
1.151
1.186
1.186
1.277
3.650
1.359
1.359
2.590
1.151
1.151
1.970
1.186
1.186
2.298
4.672
1.359
2.590
2.590
1.151
1.970
1.970
1.186
0.514
1.848
3.549
2.590
2.590
2.590
1.970
1.970
1.970
0.514
0.514
2.260
3.290
Therefore, we have that in each case, α′ + β′ + ω /∈{2π −k arccos(1/3) | k = 1, 2, 3, 4}.
α
β
α`
α`
β`
β`
γ`
γ`
γ
ω
a
b
c
Figure 8: A triangulated C6 hexagon with side lengths of π/3.
For the case of C′
6, let α, β ∈{2π−k arccos(1/3) | k = 3, 4} and let θ ∈{2π−k arccos(1/3) | k = 1, 2, 3, 4}.
We use the formulas for a, b, c, α′, and β′ mentioned in the case of C6. Then, γ = θ −α′ and we compute,
γ′ = arccos
cos a −cos(π/3) cos c
sin(π/3) sin c

ω = arccos
cos(π/3) −cos b cos c
sin b sin c

11
We now consider 16 cases by varying α, β, and θ.
For simplicity, we have mentioned every case by
disregarding any symmetries present in C′
6. Furthermore, observe that in the column of value for c, 0.149 <
π/3 and 0.725 < π/3, so these cases are not realizable.
Table 4. Cases for C′
6 of the Hexagon Lemma
α
β
θ
γ
a
b
c
α′
β′
γ′
ω
β′ + γ′ + ω
1.359
1.359
1.359
0.172
1.151
1.151
0.149
-
-
-
-
-
1.359
1.359
2.590
1.403
1.151
1.151
1.186
1.186
1.186
1.293
1.148
3.625
1.359
1.359
3.821
2.634
1.151
1.151
1.988
1.186
1.186
0.690
0.648
2.525
1.359
1.359
5.052
3.865
1.151
1.151
1.888
1.186
1.186
0.816
0.763
2.766
1.359
2.590
1.359
0.172
1.151
1.970
0.149
-
-
-
-
-
1.359
2.590
2.590
1.403
1.151
1.970
1.186
1.186
0.514
1.293
0.713
2.521
1.359
2.590
3.821
2.634
1.151
1.970
1.988
1.186
0.514
0.690
1.152
2.357
1.359
2.590
5.052
3.865
1.151
1.970
1.888
1.186
0.514
0.816
1.123
2.454
2.590
1.359
1.359
0.844
1.970
1.151
0.725
-
-
-
-
-
2.590
1.359
2.590
2.075
1.970
1.151
1.683
0.514
1.186
1.967
0.925
4.079
2.590
1.359
3.821
3.306
1.970
1.151
2.082
0.514
1.186
1.762
0.497
3.447
2.590
1.359
5.052
4.537
1.970
1.151
1.451
0.514
1.186
2.119
1.049
4.356
2.590
2.590
1.359
0.844
1.970
1.970
0.725
-
-
-
-
-
2.590
2.590
2.590
2.075
1.970
1.970
1.683
0.514
0.514
1.967
1.049
3.531
2.590
2.590
3.821
3.306
1.970
1.970
2.082
0.514
0.514
1.762
1.175
3.452
2.590
2.590
5.052
4.537
1.970
1.970
1.451
0.514
0.514
2.119
0.930
3.565
Therefore, we have that in each case, β′ + γ′ + ω /∈{2π −k arccos(1/3) | k = 1, 2, 3, 4}.
β
β`
β`
c
a
b
α
α`
α`
γ
γ`
θ
ω
Figure 9: A triangulated C′
6 hexagon with side lengths of π/3.
For the case of C′′
6 , let α, β ∈{2π−k arccos(1/3) | k = 3, 4} and let θ ∈{2π−k arccos(1/3) | k = 1, 2, 3, 4}.
We use the formulas for a, b, c, α′, and γ′ in the case of C6. Then, γ = θ −α′ and we compute,
ω = arccos
cos b −cos(π/3) cos c
sin(π/3) sin c

We now consider 16 cases by varying α, β, and θ.
For simplicity, we have mentioned every case by
disregarding any symmetries present in C′′
6 . Furthermore, observe that in the column of value for c, 0.149 <
π/3 and 0.725 < π/3, so these cases are not realizable.
12
Table 5. Cases for C′′
6 of the Hexagon Lemma
α
β
θ
α′
γ
a
b
c
γ′
ω
γ′ + ω
1.359
1.359
1.359
1.186
0.172
1.151
1.151
0.149
-
-
-
1.359
1.359
2.590
1.186
1.403
1.151
1.151
1.186
1.170
1.293
2.464
1.359
1.359
3.821
1.186
2.634
1.151
1.151
1.988
0.478
0.690
1.168
1.359
1.359
5.052
1.186
3.865
1.151
1.151
1.888
0.648
0.816
1.464
1.359
2.590
1.359
1.186
0.172
1.151
1.970
0.149
-
-
-
1.359
2.590
2.590
1.186
1.403
1.151
1.970
1.186
1.170
2.371
3.542
1.359
2.590
3.821
1.186
2.634
1.151
1.970
1.988
0.478
1.808
2.286
1.359
2.590
5.052
1.186
3.865
1.151
1.970
1.888
0.648
1.857
2.505
2.590
1.359
1.359
0.514
0.844
1.970
1.151
0.725
-
-
-
2.590
1.359
2.590
0.514
2.075
1.970
1.151
1.683
0.867
1.001
1.869
2.590
1.359
3.821
0.514
3.306
1.970
1.151
2.082
0.163
0.527
0.691
2.590
1.359
5.052
0.514
4.537
1.970
1.151
1.451
1.033
1.154
2.187
2.590
2.590
1.359
0.514
0.844
1.970
1.970
0.725
-
-
-
2.590
2.590
2.590
0.514
2.075
1.970
1.970
1.683
0.867
1.967
2.835
2.590
2.590
3.821
0.514
3.306
1.970
1.970
2.082
0.163
1.762
1.926
2.590
2.590
5.052
0.514
4.537
1.970
1.970
1.451
1.033
2.119
3.152
Therefore, we have that in each case, γ′ + ω /∈{2π −k arccos(1/3) | k = 1, 2, 3, 4}.
β
c
a
b
α
α`
γ
γ`
θ
ω
Figure 10: A triangulated C′′
6 hexagon with side lengths of π/3.
