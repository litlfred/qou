---
doc_id: arxiv-0903.2472v1
doc_title: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group"
section_id: sec-028-31-ideal-triangulations-of-hyperbolic-3-manifold
section_title: "Ideal triangulations of hyperbolic 3-manifolds"
section_number: 3.1
pages: 27-31
source_pdf: 0903.2472v1.pdf
source_sha256: 637cfd1d4d833c02
doc_brief: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group — We develop several methods that allow us to compute all-loop partition functions in perturbative Chern-Simons theory with"
---
The construction of a state integral model described in the r est of this section applies to
orientable hyperbolic 3-manifolds of ﬁnite volume (possib ly with boundary) and uses ideal
9One choice, brieﬂy mentioned in [26, 27], is to integrate ove r the real axis (resp. real subspace) of the
complex parameter space. While this choice is in some sense n atural, a closer look shows that it cannot be
the right one.
– 26 –
triangulations in a crucial way. Therefore, we begin this se ction by reviewing some relevant
facts from hyperbolic geometry (more details can be found in [46, 47, 49]).
Recall that hyperbolic 3-space H3 can be represented as the upper half-space{(x1,x 2,x 3)|
x3 > 0} with metric (2.7) of constant curvature −1. The boundary ∂H3, topologically an
S2, consists of the plane x3 = 0 together with the point at inﬁnity. The group of isometrie s
of H3 is PSL (2, C), which acts on the boundary via the usual M¨ obius transform ations. In
this picture, geodesic surfaces are spheres of any radius wh ich intersect ∂H3 orthogonally.
An ideal tetrahedron ∆ in H3 has by deﬁnition all its faces along geodesic surfaces, and
all its vertices in ∂H3 — such vertices are called ideal points. After M¨ obius transformations,
one can ﬁx three of the vertices at (0 , 0, 0), (1, 0, 0), and inﬁnity. The coordinate of the
fourth vertex ( x1,x 2, 0), with x2≥ 0, deﬁnes a complex number z = x1 +ix2 called the
shape parameter (sometimes also called edge parameter). At various edges, the faces of the
tetrahedron ∆ form dihedral angles arg zj (j = 1, 2, 3) as indicated in Figure 2, with
z1 =z, z 2 = 1− 1
z , z 3 = 1
1−z. (3.2)
The ideal tetrahedron is noncompact, but has ﬁnite volume gi ven by
Vol (∆ z) = D(z), (3.3)
whereD(z) is the Bloch-Wigner dilogarithm function, related to the u sual dilogarithm Li 2
(see Section 3.3) by
D(z) = Im
(
Li2(z)
)
+ arg(1−z) log|z|. (3.4)
Note that any of the zj can be taken to be the shape parameter of ∆, and that D(zj) =
Vol (∆ z) for each j. We will allow shape parameters to be any complex numbers in C−
{0, 1}, noting that for z∈ R an ideal tetrahedron is degenerate and that for Im z <0 it
technically has negative volume due to its orientation.
/X78/X31
/X78 /X32
/X78 /X33
/X7A
/X31/X30
/X7A /X31
/X7A /X33
/X7A /X32
/X7A /X33
/X31/X30
/X7A /X31 /X7A /X32 /X78 /X31
/X78 /X32
/X28/X70/X72/X6F/X6A/X65/X63/X74/X69/X6F/X6E/X20/X74/X6F/X20/X62/X6F/X75/X6E/X64/X61/X72/X79/X20/X70/X6C/X61/X6E/X65/X29 
/X7A /X31
/X7A /X31
/X7A /X32
/X7A /X33
/X7A /X32
/X7A /X33
Figure 2: An ideal tetrahedron in H3.
A hyperbolic structure on a 3-manifold is a metric that is loc ally isometric to H3. A 3-
manifold is called hyperbolic if it admits a hyperbolic stru cture that is geodesically complete
and has ﬁnite volume. Most 3-manifolds are hyperbolic, incl uding the vast majority of knot
and link complements in S3. Speciﬁcally, a knot complement is hyperbolic as long as the
knot is not a torus or satellite knot [48]. Every closed 3-man ifold can be obtained via Dehn
– 27 –
surgery on a knot in S3, and for hyperbolic knots all but ﬁnitely many such surgerie s yield
hyperbolic manifolds [46].
By the Mostow rigidity theorem [37, 44], the complete hyperb olic structure on a hy-
perbolic manifold is unique. Therefore, geometric invaria nts like the hyperbolic volume
are actually topological invariants. For the large class of hyperbolic knot complements in
S3, the unique complete hyperbolic structure has a parabolic h olonomy with unit eigenval-
ues around the knot. In SL(2, C) Chern-Simons theory, this structure corresponds to the
“geometric” ﬂat connection A(geom) with u = 0. As discussed in Section 2.1, hyperbolic
manifolds with complete hyperbolic structures can also be d escribed as quotients H3/Γ.
Given a hyperbolic knot complement, one can deform the hyper bolic metric in such a
way that the holonomy u is not zero. Such deformed metrics are unique in a neighborho od
of u = 0, but they are not geodesically complete. For a discrete se t of values of u, one can
add in the “missing” geodesic, and the deformed metrics coin cide with the unique complete
hyperbolic structures on closed 3-manifolds obtained via a ppropriate Dehn surgeries on the
knot in S3. For other values of u, the knot complement can be completed by adding either
a circle S1 or a single point, but the resulting hyperbolic metric will b e singular. For
example, if u∈ iR one adds a circle and the resulting metric has a conical singu larity.
These descriptions can easily be extended to link complemen ts ( i.e. multiple cusps), using
multiple parameters uk, one for each link component.
Any orientable hyperbolic manifold M is homeomorphic to the interior of a compact
3-manifold ¯M with boundary consisting of ﬁnitely many tori. (The manifol d M itself can
also be thought of as the union of ¯M with neighborhoods of the cusps, each of the latter
being homeomorphic to T 2× [0,∞).) All hyperbolic manifolds therefore arise as knot or
link complements in closed 3-manifolds. Moreover, every hy perbolic manifold has an ideal
triangulation, i.e a ﬁnite decomposition into (possibly degenerate 10) ideal tetrahedra; see
e.g. [46, 43].
To reconstruct a hyperbolic 3-manifold M from its ideal triangulation {∆ i}N
i=1, faces
of tetrahedra are glued together in pairs. One must remember , however, that vertices of
tetrahedra are not part of M , and that the combined boundaries of their neighborhoods
in M are not spheres, but tori. (Thus, some intuition from simpli cial triangulations no
longer holds.) There always exists a triangulation of M whose edges can all be oriented in
such a way that the boundary of every face (shared between two tetrahedra) has two edges
oriented in the same direction (clockwise or counterclockw ise) and one opposite. Then the
vertices of each tetrahedron can be canonically labeled 0, 1 , 2, 3 according to the number
of edges entering the vertex, so that the tetrahedron can be i dentiﬁed in a unique way with
one of the two numbered tetrahedra shown in Figure 4 of the nex t subsection. This at
the same time orients the tetrahedron. The orientation of a g iven tetrahedron ∆ i may not
agree with that of M ; one deﬁnes ǫi = 1 if the orientations agree and ǫi =−1 otherwise.
The edges of each tetrahedron can then be given shape paramet ers (z(i)
1 ,z (i)
2 ,z (i)
3 ), running
counterclockwise around each vertex (viewed from outside t he tetrahedron) if ǫi = 1 and
clockwise if ǫi =−1.
10It is conjectured and widely believed that nondegenerate te trahedra alone are always suﬃcient.
– 28 –
For a givenM with cusps or conical singularities speciﬁed by holonomy pa rametersuk,
the shape parameters z(i)
j of the tetrahedra ∆ i in its triangulation are ﬁxed by two sets of
conditions. First, the product of the shape parameters z(i)
j at every edge in the triangulation
must be equal to 1, in order for the hyperbolic structures of a djacent tetrahedra to match.
More precisely, the sum of some chosen branches of log z(i)
j (equal to the standard branch
if one is near the complete structure) should equal 2 πi, so that the total dihedral angle
at each edge is 2 π. Second, one can compute holonomy eigenvalues around each t orus
boundary in M as a product of z(i)
j ’s by mapping out the neighborhood of each vertex in
the triangulation in a so-called developing map, and follow ing a procedure illustrated in,
e.g., [42]. There is one distinct vertex “inside” each boundary t orus. One then requires
that the eigenvalues of the holonomy around the kth boundary are equal to e±uk . These
two conditions will be referred to, respectively, as consistency and cusp relations.
Every hyperbolic 3-manifold has a well-deﬁned class in the B loch group [41]. This is a
subgroup11 of the quotient of the free Z-module Z[C−{ 0, 1}] by the relations
[x]− [y] + [y
x ]− [ 1−x−1
1−y−1 ] + [ 1−x
1−y ] = 0. (3.5)
This ﬁve-term or pentagon relation accounts for the fact tha t a polyhedron with ﬁve ideal
vertices can be decomposed into ideal tetrahedra in multipl e ways. The ﬁve ideal tetrahedra
in this polyhedron (each obtained by deleting an ideal verte x) can be given the ﬁve shape
parameters x, y, y/x,...appearing above. The signs of the diﬀerent terms correspond t o
orientations. Geometrically, an instance of the ﬁve-term r elation can be visualized as the
2-3 Pachner move, illustrated in Figure 3.
/X32 /X33
Figure 3: The 2-3 Pachner move.
The class [ M ] of a hyperbolic 3-manifold M in the Bloch group can be computed
by summing (with orientation) the shape parameters [ z] of any ideal triangulation, but
it is independent of the triangulation. Thus, hyperbolic invariants of 3-man ifolds may be
obtained by functions on the Bloch group — i.e. functions compatible with (3.5). For
example, the Bloch-Wigner function (3.4) satisﬁes
D(x)−D(y) +D
(y
x
)
−D
(1−x−1
1−y−1
)
+D
(1−x
1−y
)
= 0, (3.6)
11Namely, the kernel of the map [ z] ↦→2z ∧ (1 − z) ∈ C∗ ∧Z C∗ acting on this quotient module.
– 29 –
and the hyperbolic volume of a manifold M triangulated by ideal tetrahedra {∆ i}N
i=1 can
be calculated as
Vol (M ) =
N∑
i=1
ǫiD(z(i)). (3.7)
The symbols ǫi here could be removed if shape parameters were assigned to te trahedra in a
manner independent of orientation, noting that reversing t he orientation of a tetrahedron
corresponds to sending z↦→1/z and that D(1/z) =−D(z). This is sometimes seen in the
literature.
The complexiﬁed volume i(Vol (M ) +iCS(M )) is trickier to evaluate. For a hyperbolic
manifold with a spin structure, corresponding to full SL(2, C) holonomies, this invariant
is deﬁned modulo 4 π2. Here, we will outline a computation of the complexiﬁed volu me
moduloπ2, following [40]; for the complete invariant modulo 4 π2, see [60]. To proceed, one
must ﬁrst make sure that the three shape parameters z(i) =z(i)
1 ,z(i)
2 , andz(i)
3 are speciﬁcally
assigned to edges [ v(i)
1 ,v (i)
2 ], [v(i)
1 ,v (i)
3 ], and [v(i)
1 ,v (i)
2 ] (respectively) in each tetrahedron ∆ i
of an oriented triangulation of M , where [v(i)
a ,v (i)
b ] denotes the edge going from numbered
vertex v(i)
a to numbered vertex v(i)
b . One also chooses logarithms ( w(i)
1 ,w (i)
2 ,w (i)
3 ) of the
shape parameters such that
ew(i)
1 =±z(i)
1 , e w(i)
2 =±z(i)
2 , e w(i)
3 =±z(i)
3 , (3.8a)
w(i)
1 +w(i)
2 +w(i)
3 = 0 ∀i, (3.8b)
and deﬁnes integers ( q(i),r (i)) by
w(i)
1 = Log(z(i)) +πiq(i), w (i)
2 =−Log(1−z(i)) +πir(i), (3.9)
where Log denotes the principal branch of the logarithm, wit h a cut from 0 to −∞. For a
consistent labeling of the triangulation, called a “combin atorial ﬂattening,” the sum of log-
parameters w(i)
j around every edge must vanish, and the (signed 12) sum of log-parameters
along the two paths generating π1(T 2) = Z2 for any boundary (cusp) T 2 must equal twice
the logarithm of the SL(2, C) holonomies around these paths. 13 The complexiﬁed volume
is then given, modulo π2, as
i(Vol (M ) +iCS(M )) =
N∑
i=1
ǫiL(z(i);q(i),r (i))−
∑
cusps k
(vk
uk +iπuk), (3.10)
with
L(z;q,r ) = Li 2(z) + 1
