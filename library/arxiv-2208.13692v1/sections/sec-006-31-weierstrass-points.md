---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-006-31-weierstrass-points
section_title: "Weierstrass Points"
section_number: 3.1
pages: 13-17
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
doc_brief: "European Journal of Mathematics (2024) 10:3 RESEARCH ARTICLE — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
Deﬁnition 3.2 ([McM14], Proposition 12.6, Theorem 12.7) . A Weierstrass Point on a
curve X of genus g with canonical embedding Xc⊆ Pg−1 is a point P satisfying one of the
following equivalent conditions:
(1) there exists a hyperplane H⊂ Pg−1such that H∩Xc has multiplicity at least g at
P ,
(2) there exists a holomorphic diﬀerential on X vanishing at P with order≥g,
(3) there exists a meromorphic function on X with poles just at P of order≤g, and
(4) the Wronskian determinant given by Wr(P ) = det
(
diωj
dzi
)
i,j=0,...,g−1
, where{ωj} is
a basis of holomorphic diﬀerentials and z is a local coordinate around P , vanishes.
10Being a geometric point on a curve is a priori not an interesting statement unless we know the corre-
sponding map is regular, as we have in this case.
14 H. W. BRADEN AND LINDEN DISNEY-HOGG
(a) Dodecadodecahedron.
 (b) Small Stellated Dodecahedron.
Figure 1. Geometric realisations.
(a) {5, 4} tessellation.
 (b) {5, 5} tessellation.
Figure 2. Hyperbolic tilings.
In [SW97] the Weierstrass points are shown (implicitly) to correspond to the edge-centres
of the universal map. This shows that the order 2 rotation that permutes the vertices and
face-centres adjacent to an edge-centre will preserve the corresponding Weierstrass point.
They can also be interpreted geometrically as pairwise-symmetric distributed along the
edges of the small stellated dodecahedron. As Weber identiﬁes the order-3 symmetry as
the rotation about the axis through opposite vertices of the unstellated dodecahedron, one
might wonder from this picture whether Weierstrass points are ﬁxed points of the order-3
BRING’S CUR VE: OLD AND NEW 15
permutations in the group. This turns out not be the case and a counting argument helps
elucidate: the small stellated dodecahedron has 12 faces, which in turn means we want to
have 60
12 = 5 Weierstrass points per face. Hence where three faces overlap there must be
three Weierstrass points ‘stacked’ there, which are invisibly permuted by the action.
Having now identiﬁed the Weierstrass points as some of the geometric points, we give a
concrete result about what the Weierstrass points are.
Proposition 3.3 ([Edg78]). Bring’s curve has 60 Weierstrass points, on which Aut(B) acts
transitively. Letting{α,β,γ} be the roots of the cubic x3 + 2x2 + 3x + 4, these are given in
the P4-model by Wijk where, for example,
W345 = [1 : 1 :α :β :γ].
Proof. Edge, working in the P4-model, identiﬁes the Weierstrass points with the 60 intersec-
tions of the curve with the 10 planes Π ij ={xi =xj}. To do this, Edge quotes [Wim95] to
show that these intersection points are stalls 11, i.e. inﬂection points of certain linear series,
and for the canonical embedding these are exactly the Weierstrass points [ACGH85, p. 37].
Simple algebra then gives the exact expression we write down. This viewpoint makes it clear
that the Weierstrass points at the intersection with Πij are preserved by the transposition12
(ij) only, so have orbits of size 120
2 = 60, and as the automorphism restricts to a permutation
of the Weierstrass points, the action is then transitive. □
With our naming convention, note Wijk is deﬁned by xi = α, xj = β, xk = γ. If we
choose a diﬀerent labelling of the roots of the cubic, this would give a diﬀerent labelling
of the Weierstrass points. The Weierstrass points split as 60 = 6 × 10, with 6 Weierstrass
points being ﬁxed by each of the 10 involutions in S5.
The property that the automorphism group acts transitively on the Weierstrass points is
very rare, as characterised by the following result.
Theorem 3.4 ([LS12], Theorem 15). If X is a Riemann surface of genus g >2 with g3−g
Weierstrass points on which AutX acts transitively then either
• g = 4 and X is Bring’s curve,
• g = 3 and X is Klein’s curve, or
• g = 3 and AutX∼=S4.
Remark 3.5. As we have an explicit birational map from our plane model to our canonical
embedding of the curve, we can get the explicit forms of the Weierstrass points in the HC-
model using Edge’s identiﬁcation of the Weierstrass points in the P4-model. If one does not
have this information, it is still possible to calculate the Weierstrass points using Sage and
some educated guesswork. Using computer algebra, and the characterisation of Weierstrass
points as zeros of the Wronskian determinant, one can check that in the HC-model the
11A stall of a plane curve is a point where the osculating (hyper)plane has a 4-point intersection [Edg71].
12In Theorem 4 of [Dye95], these transpositions are associated with the Brianchon points of the Clebsch
hexagon H from the proof of Proposition 2.11.
16 H. W. BRADEN AND LINDEN DISNEY-HOGG
Weierstrass points have base coordinates at the 60 roots of the polynomial equations
0 =x12− 32x11− 114x10− 200x9 + 100x8 + 48x7− 936x6 + 1728x5− 2000x4 + 3200x3
− 2624x2 + 768x− 64,
0 =x24− 24x23 + 1306x22− 2864x21 + 10096x20− 32704x19− 5704x18− 41824x17
+ 43056x16 + 831616x15 + 837856x14 + 992256x13 + 2603136x12 + 1238016x11
+ 1560576x10 + 5584896x9 + 3357696x8 + 3838976x7 + 5856256x6 + 2543616x5
+ 2200576x4 + 1355776x3 + 454656x2 + 65536x + 4096,
0 =x24 + 56x23 + 1176x22− 1784x21− 3904x20 + 36096x19 + 12776x18− 211904x17
+ 304736x16 + 431616x15 + 339456x14− 1985664x13− 625344x12 + 1034496x11
+ 3512576x10− 584704x9− 3572224x8− 2018304x7 + 3303936x6 + 3055616x5
+ 1099776x4 + 45056x3 + 229376x2− 16384x + 4096.
One can check that the Galois group of each polynomial is C4×S3. We have seen that in
the HC-model the automorphisms have coeﬃcients in Z[ζ], and so we know the splitting ﬁeld
must be an extension of Q[ζ], which accounts for the C4 factor in the Galois group. S3 has a
subgroup of order 2, corresponding to an extension of degree-2, and a brute force calculation
shows that we also wish to adjoin i
√
2. This has already nearly reduced the problem, and
then one needs a small moment of inspiration to ﬁnd the last thing to adjoin. Looking at
[RR92] then may inspire one to adjoin the real root of the polynomial x3 + 7x2 + 8x + 4, say
ξ, and this gives the full splitting ﬁeld. We can solve the cubic explicitly using Cardano’s
formula to ﬁnd
ξ =−1
3
{
7 +
[
3
√
145 + 30
√
6 +
3
√
145− 30
√
6
]}
,
and as such we could also take our splitting ﬁeld to be
Q
[
ζ,i
√
2,
3
√
145 + 30
√
6
]
.
We observe by Cardano’s formula that α,β,γ ∈ Q[i
√
2,
3
√
30 + 15
√
6], and this latter ﬁeld is
isomorphic to Q[i
√
2,
3
√
145 + 30
√
6]. With these expression for the Weierstrass points, and
the explicit knowledge of the automorphism group as an action on aﬃne coordinates, we can
ﬁnd explicitly the transposition that preserves a given Weierstrass point.
Note that an alternative method for computing Weierstrass points algorithmically has been
implemented in Magma [Hes02b].
We now have seen how our Weierstrass points satisfy characterisations 1 and 4 of Deﬁni-
tion 3.2, and we complete the picture with the following result which we believe new.
Proposition 3.6. Deﬁne the points P345,P′
345 corresponding to the Weierstrass pointW345
(and similarly for the other Weierstrass points) by
P345 = [δ′ :δ : (−43α2− 113α− 92)β/112
− (13α2− 27α− 20)/28 : (43α2 + 25α− 4)β/112 + (13α2 + 3α− 24)/28 : 1]
P′
345 = [δ :δ′ : (−43α2− 113α− 92)β/112
− (13α2− 27α− 20)/28 : (43α2 + 25α− 4)β/112 + (13α2 + 3α− 24)/28 : 1].
BRING’S CUR VE: OLD AND NEW 17
Hereα, β were deﬁned in Proposition 3.3 and δ, δ′ are the roots of
x2−
[(11α + 12)β + 4(3α + 2)
14
]
x +
[23(155α + 388)β + 92(97α + 172)
6272
]
.
Then there is a holomorphic diﬀerential ν345 on Bring’s curve with divisor
4W345 +P345 +P′
345,
and a meromorphic function on Bring’s curve with divisor
P145 +P′
145 +P245 +P′
245− 4W345.
Proof. Note that algorithmically it is possible to construct these through the work in
[Hes02a], the tools for which are partially implemented in Sage but not with enough gener-
ality for us to use out-the-box. As such we need a diﬀerent approach.
We know that for any Weierstrass point W there is a hyperplane H⊂ P3 intersecting
the canonical embedding with multiplicity g = 4 at W (that is H∩B = 4W +P +P′
for some P,P′∈B ). Such a hyperplane gives a holomorphic diﬀerential νijk with (νijk) =
4Wijk +Pijk +P′
ijk. From [Edg78] we know that for Bring’s curve the osculating plane 13 at
W intersects 4 times, and so this is the plane we are looking for. As Edge gives a formula
for the osculating plane (attributed to Hesse), we can explicitly calculate the remaining 2
intersections with the curve in terms of a polynomial roots. This gives us the ﬁrst result for
the divisor of the meromorphic diﬀerential.
Furthermore, from [Edg81] we have a tritangent plane which has intersection with Bring’s
curve
2(W145 +W245 +W345).
We will discuss this plane (and others like it) more in§5.2, but for now all we need is that this
means there is a holomorphic diﬀerential ω(1)
45α onB with (ω(1)
45α) = 2(W145 +W245 +W345).
As such we get the divisor of the meromorphic function
ν145ν245
(
ω(1)
45α
)2

 =P145 +P′
145 +P245 +P′
245− 4W345.
As we can calculate the formula for all these planes explicitly if we wish, we could (in
principle) construct the corresponding function and diﬀerential. □
Remark 3.7. We are able to verify the results in Proposition 3.6 using the Abel-Jacobi map
implemented in the Sage [DH21]; see the notebooks.
