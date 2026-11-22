---
doc_id: arxiv-1307.6697v2
doc_title: "REPRESENTATIONS OF FUNDAMENTAL GROUPS OF 3-MANIFOLDS"
section_id: sec-006-7-an-example-the-figure-eight-knot
section_title: "An example: the figure-eight knot"
section_number: 7
pages: 16-20
source_pdf: 1307.6697v2.pdf
source_sha256: a3afaefdaebe0292
toc_source: outline
doc_brief: "REPRESENTATIONS OF FUNDAMENTAL GROUPS OF 3-MANIFOLDS — In this paper we are interested in computing representations of the funda- mental group of a 3-manifold into PGL(3, C) (in particular in PGL(2"
---
The ﬁgure eight knot is given as a gluing of two tetrahedra as in Figure 2. We refer to it
to set the equations of compatibility.
Let zij and wij be the coordinates associated to the edge ij of each of the tetrahedra.
We obtain the edge and face equations:
(Le)







z23w24z13w31z14w21
=
1
z32w42z31w13z41w12
=
1
z24w23z21w43z34w41
=
1
z42w32z12w34z43w14
=
1.
(Lf)







z21z31z41w21w31w41
=
1
z12z32z42w13w23w43
=
1
z13z23z43w12w32w42
=
1
z14z24z34w14w24w34
=
1.
7.1. Boundary holonomy representation. The meridian and the longitude are com-
puted from the Snappea triangulation. We follow the algorithm to compute the holonomy
along the meridian and the longitude along appropriate paths:
(421)1 →(423)1 →(324)0 →(314)0
(421)1 →(431)1 →(214)0 →(234)0 →(243)1 →(241)1 →(134)0 →(132)0 →
(312)1 →(342)1 →(432)0 →(412)0 →(134)1 →(132)1 →(312)0 →(314)0
17
1
3
4
2
1
3
4
2
Figure 2. Triangulation of m004
Figure 3. The holonomy of the ﬁgure eight cusp. The red line corresponds
to L and the green line to M
The corresponding matrices are:
gM =


z12z21
z34w24
−z12z13 + z34z24
z34z24z13
−z32w42
z13
0
1
z32w42
0
0
w42
z34


gL =


z13z31w14w23
w31z42w42z24
∗
∗
0
1
∗
0
0
z31w13z13w24
z42w32z24w41


We therefore deduce the unipotent holonomy equations: A = A∗= B = B∗= 1 where
A = z12z21
z34w24
, A∗= w42
z34
, B = z13z31w14w23
w31z42w42z24
, B∗= z31w13z13w24
z42w32z24w41
.
7.2. Solutions. Here the pre-processing provides a reduced system of 7 polynomial equa-
tions in the variables {z14, z43}. All of the 22 other variables belong to Q(z14, z43). This
reduced system is 0-dimensional and one can easily compute Rational Univariate Represen-
tations of its zeroes.
One obtain four sets given by their minimal polynomials.
◮f1 = Y 2 −Y + 1.
The complete hyperbolic structure on the complement of the ﬁgure-eight knot is
obtained from two conjugate solutions. In fact, in that case, if ω± = 1±i
√
3
2
is one
root of f1, then
z12 = z21 = z34 = z43 = w12 = w21 = w34 = w43 = ω±
is a solution of the equations as obtained in [22]. Its volume is 2.029883212 · · ·.
◮f2 = Y 2 −Y + 1.
z12 = z34 = w34 = w43 = z21 = z43 = w12 = w21 = ω±.
18
E. FALBEL, P.-V. KOSELEFF AND F. ROUILLIER
This solution corresponds to a discrete representation of the fundamental group of
the complement of knot in PU(2, 1) with faithful boundary holonomy. Moreover, its
action on complex hyperbolic space has limit set the full boundary sphere ([10]).
◮f3 = Y 2 + Y + 2. Let γ± = −1
2 ± i 1
2
√
7 be a root of f3. The coordinates are
z21 = w21 = z43 = w12 = 5−i
√
7
4
, z12 = w2,1 = 3−i
√
7
8
, w34 = w43 = −1+i
√
7
2
.
◮f4 = 2Y 2 + Y + 1. 1/γ± = −1
4 ± i 1
4
√
7 is a root of f4. We obtain
z12 = z34 = 3−i
√
7
2
, w43 = w34 = 5+i
√
7
8
, z21 = w21 = z43 = w12 = −1+i
√
7
4
.
All solutions corresponding to f2, f3, f4 were obtained in [10] and f3, f4 correspond to spher-
ical CR structures with unipotent boundary holonomy of rank one ([8]).
7.3. Holonomy representation. In order to obtain the representation of the fundamental
group of the complement of the ﬁgure eight knot we identify the face (324)0 of the tetrahe-
dron 0 to the face (423)1 of the tetrahedron 1. The generators are explicitly written from
the remaining three face identiﬁcations following paths which pass through the chosen face
(324)0 = (423)1 inside the tetrahedra and transport the projective basis deﬁned by each
oriented face.
Here are the paths generating the identiﬁcations on the polyhedron:
(1) (134)0 →(341)0 →(342)0 →(423)0 →(234)0 = (243)1 →(241)1
(2) (214)0 →(142)0 →(421)0 →(423)0 →(234)0 = (243)1 →(432)1 →(431)1
(3) (123)0 →(231)0 →(234)0 = (243)1 →(432)1 →(324)1 →(321)1
In order to obtain paths generating the fundamental group with a base point at face
(234)0, the paths have to be conjugated, respectively, by
(1) (234)0 →(342)0 →(341)0 →(413)0 →(134)0
(2) (234)0 →(342)0 →(423)0 →(421)0 →(214)0
(3) (234)0 →(231)0 →(312)0 →(123)0
The coordinate transformations corresponding to each path are obtained by multiplying the
coordinate change matrices. The generators of the group representation are obtained as
inverse matrices of the coordinate change matrices.
Applying the computations above to the solution f2 we obtain the generators
g1 =


1
0
0
−w±
1
0
−w∓
−2w∓
1

, g2 =


3w∓
6w∓
1
3w±
−1
0
1
0
0

, g3 =


1
2w∓
−w∓
0
1
w∓
0
0
1

.
The group ⟨g1, g2, g3⟩preserves the hermitian form


0
0
−w±
0
1
0
−w∓
0
0

.
For the solution f3 we obtain
19
g1 =


1
0
0
−2
γ±
1
0
−γ±
2
2
γ± −1
1

, g2 =


8
γ± + 3
3
γ± + 2
−
4
3γ± + 2
−3
γ±
1
0
2
γ± + 2
0
0


, g3 =


1
2
γ± + 2
−1
γ±
0
1
γ±
0
0
1

.
The group ⟨g1, g2, g3⟩preserves the hermitian form


0
0
γ∓
0
1
0
γ±
0
0

.
Finally, for the solution f4 we obtain
g1 =


1
0
0
2
γ± −2
1
0
−2
γ±
1
2γ± −1
1


, g2 =


−2
−1
2γ± −3
−1
8
γ± + 6
1
0
−1
0
0

, g3 =


1
4
γ± + 3
−γ±
0
1
−
2
γ± −2
0
0
1


.
The group ⟨g1, g2, g3⟩preserves the hermitian form


0
0
−1
2
0
1
0
−1
2
0
0

.
Observe that the three generators satisfy the relations
g3g−1
2 g−1
1 g2 = 1
and
g−1
3 g2g−1
1 g3g1 = 1
which give a presentation of the fundamental group of the ﬁgure eight knot.
7.4. Boundary holonomy. For all solutions in PU(2, 1) we always obtain gL = g−1
1 . The
meridian is respectively
gM =


1
0
0
0
1
0
±
√
3
0
1

, gM = gL
−3, gM = gL
3.
7.5. Some non-unipotent conﬁgurations of the ﬁgure-eight knot. In this section we
give examples of non-unipotent representations in order to show how our method can be
applied without modiﬁcation to a general holonomy condition. We will only deal with a
few examples for the ﬁgure eight knot and reserve a complete study of that knot for a later
paper.
We keep the notations of section 7:
A = z12z21
z34w24
, A∗= w42
z34
, B = z13z31w14w23
w31z42w42z24
, B∗= z31w13z13w24
z42w32z24w41
.
We will ﬁrst impose that A and A∗are primitive cubic roots of unity, and we ﬁnd a ﬁnite
set of solutions. In the second case we will impose that A and A∗are primitive sixth roots
of unity. We ﬁnd here a ﬁnite number of isolated solutions as well a one 1-dimensional
component.
We start with the case when A and A∗are primitive cubic roots of unity. Here the pre-
processing provides a reduced system of 5 polynomial equations in the variables {z14, z24, z43, w14}.
All of the 20 other variables belong to Q(z14, z24, z43, w14).
This reduced system is 1-
dimensional. After saturation the system becomes 0-dimensional. It has 6 components.
Let ζ be a primitive twelfth root of unity.
20
E. FALBEL, P.-V. KOSELEFF AND F. ROUILLIER
The ﬁrst component corresponds to representations in PGL(2, Q(ζ2)) and we get A =
1/A∗= ζ4, B = B∗= 1. The volume is 0, we have g3
M = gL = 1.
The second and the third component give 8 solutions in PGL(3, Q(ζ)).
We get A =
1/A∗= ζ4, B = B∗= 1. Their volumes are equal to 0 and we have g3
M = gL = 1.
The fourth and the ﬁfth components give 8 solutions in PGL(3, Q(α)) where α = ±
√
5 ±
i
√
3. We get A = A∗= ζ4, B = B∗= 1. In this case we have g3
M = gL or g3
M = g−1
L .
The last component gives 4 solutions in PGL(3, C) and 4 solutions in PU(2, 1). We get
A = A∗= ζ4 and B = B∗is a root of X4−175 X3−327 X2−175 X+1. This last polynomial
has 2 conjugated roots with moduli 1 and two real roots. Therefore, the boundary holonomy
group has rank 2. These solutions belong to PU(2, 1) when |B| = 1 and the four others give
a volume .973235 · · ·, when B is real.
We now look at solutions with A and A∗primitive sixth roots of unity. We ﬁnd here seven
0-dimensional components and one 1-dimensional component.
There are 4 hyperbolic solutions corresponding to A = 1/A∗= ζ2 and B = 1/B∗=
7 ± 4
√
3. Their volume is 1.2212874588 · · ·. The meridian satisﬁes g6
M = 1.
There are two components in PGL(3, Q(ζ)), satisfying A = 1/A∗= ζ2, B = B∗= −1.
They all satisfy g3
M = gL, g2
L = 1. None of these belong to PU(2, 1).
There are three components in PGL(3, Q(β)) where β is a root of X4 + X3 −X2 −X + 1.
We have A = 1/A∗= ζ2, B = B∗= −1. They all satisfy g3
M = gL, g2
L = 1. None of these
belong to PU(2, 1).
There is a component giving 4 solutions in PGL(3, C) and 4 solutions in PU(2, 1). We get
A = A∗= ζ4 and B = B∗is a root of X4 −27X3 + 25X2 −27X + 1. This last polynomial
has 2 conjugated roots with moduli 1 and two real roots. Therefore, the boundary holonomy
group has rank 2. These solutions belong to PU(2, 1) when |B| = 1 and the four others give
a volume 1.730258 · · ·, when B is real.
The 1-dimensional component corresponds to reducible representations. We have: A =
1/A∗= ζ2 and B = 1/B∗= −1. The volume of these conﬁgurations is 0. For all these
conﬁgurations, the face variables are all equal to −1. We obtain zijzji = ζ±2, wijwji = ζ∓2
for all i < j. We always obtain g3
M = gL and g2
L = 1.
