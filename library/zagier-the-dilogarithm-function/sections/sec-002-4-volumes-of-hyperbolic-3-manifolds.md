---
doc_id: zagier-the-dilogarithm-function
doc_title: "The Dilogarithm Function"
section_id: sec-002-4-volumes-of-hyperbolic-3-manifolds
section_title: "Volumes of hyperbolic 3-manifolds"
section_number: 4
pages: 11-14
source_pdf: zagier-the-dilogarithm-function.pdf
source_sha256: 05079cf525c6ba0f
toc_source: inferred
---
The dilogarithm occurs in connection with measurement of volumes in euclid-
ean, spherical, and hyperbolic geometry. We will be concerned with the last of
these. Let H3 be the Lobachevsky space (space of non-euclidean solid geome-
try). We will use the half-space model, in which H3 is represented by C × R+
with the standard hyperbolic metric in which the geodesics are either verti-
cal lines or semicircles in vertical planes with endpoints in C × {0} and the
geodesic planes are either vertical planes or else hemispheres with boundary
in C × {0}. An ideal tetrahedron is a tetrahedron whose vertices are all in
∂H3 = C ∪{∞} = P1(C). Let ∆be such a tetrahedron. Although the vertices
are at inﬁnity, the (hyperbolic) volume is ﬁnite. It is given by
Vol(∆) = D(z0, z1, z2, z3),
(7)
where z0, . . . , z3 ∈C are the vertices of ∆and D is the function deﬁned in (5).
In the special case that three of the vertices of ∆are ∞, 0, and 1, equation
(7) reduces to the formula (due essentially to Lobachevsky)
Vol(∆) = D(z).
(8)
14
Don Zagier
In fact, equations (7) and (8) are equivalent, since any 4-tuple of points
z0, . . . , z3 can be brought into the form {∞, 0, 1, z} by the action of some
element of SL2(C) on P1(C), and the group SL2(C) acts on H3 by isometries.
The (anti-)symmetry properties of D under permutations of the zi are
obvious from the geometric interpretation (7), since renumbering the vertices
leaves ∆unchanged but may reverse its orientation. Formula (6) is also an
immediate consequence of (7), since the ﬁve tetrahedra spanned by four at a
time of z0, . . . , z4 ∈P1(C), counted positively or negatively as in (6), add up
algebraically to the zero 3-cycle.
The reason that we are interested in hyperbolic tetrahedra is that these
are the building blocks of hyperbolic 3-manifolds, which in turn (according to
Thurston) are the key objects for understanding three-dimensional geometry
and topology. A hyperbolic 3-manifold is a 3-dimensional riemannian mani-
fold M which is locally modelled on (i.e., isometric to portions of) hyperbolic
3-space H3; equivalently, it has constant negative curvature −1. We are in-
terested in complete oriented hyperbolic 3-manifolds that have ﬁnite volume
(they are then either compact or have ﬁnitely many “cusps” diﬀeomorphic
to S1 × S1 × R+). Such a manifold can obviously be triangulated into small
geodesic simplices which will be hyperbolic tetrahedra. Less obvious is that
(possibly after removing from M a ﬁnite number of closed geodesics) there is
always a triangulation into ideal tetrahedra (the part of such a tetrahedron
going out towards a vertex at inﬁnity will then either tend to a cusp of M
or else spiral in around one of the deleted curves). Let these tetrahedra be
numbered ∆1, . . . , ∆n and assume (after an isometry of H3 if necessary) that
the vertices of ∆ν are at ∞, 0, 1 and zν. Then
Vol(M) =
n

ν=1
Vol(∆ν) =
n

ν=1
D(zν) .
(9)
Of course, the numbers zν are not uniquely determined by ∆ν since they
depend on the order in which the vertices were sent to {∞, 0, 1, zν}, but the
The Dilogarithm Function
15
non-uniqueness consists (since everything is oriented) only in replacing zν by
1 −1/zν or 1/(1 −zν) and hence does not aﬀect the value of D(zν).
One of the objects of interest in the study of hyperbolic 3-manifolds is the
“volume spectrum”
Vol = {Vol(M) | M a hyperbolic 3-manifold} ⊂R+ .
From the work of Jørgensen and Thurston one knows that Vol is a countable
and well-ordered subset of R+ (i.e., every subset has a smallest element), and
its exact nature is of considerable interest both in topology and number theory.
Equation (9) as it stands says nothing about this set since any real number
can be written as a ﬁnite sum of values D(z), z ∈C. However, the parameters
zν of the tetrahedra triangulating a complete hyperbolic 3-manifold satisfy an
extra relation, namely
n

ν=1
zν ∧(1 −zν) = 0,
(10)
where the sum is taken in the abelian group Λ2C× (the set of all formal
linear combinations x ∧y, x, y ∈C×, subject to the relations x ∧x = 0
and (x1x2) ∧y = x1 ∧y + x2 ∧y). (This follows from assertions in [3] or from
Corollary 2.4 of [5] applied to suitable x and y.) Now (9) does give information
about Vol because the set of numbers 
n
ν=1 D(zν) with zν satisfying (10)
is countable. This fact was proved by Bloch [1]. To make a more precise
statement, we introduce the Bloch group. Consider the abelian group of formal
sums [z1] + · · · + [zn] with z1, . . . , zn ∈C× ∖{1} satisfying (10). As one easily
checks, it contains the elements
[x] +

 1
x

,
[x] + [1 −x],
[x] + [y] +

 1 −x
1 −xy

+ [1 −xy] +

 1 −y
1 −xy

(11)
for all x and y in C× −{1} with xy̸ = 1, corresponding to the symmetry
properties and ﬁve-term relation satisﬁed by D( · ). The Bloch group is deﬁned
as
BC = {[z1]+ · · · +[zn] satisfying (10)}/(subgroup generated by
the elements (11))
(12)
(this is slightly diﬀerent from the usual deﬁnition). The deﬁnition of the Bloch
group in terms of the relations satisﬁed by D( · ) makes it obvious that D
extends to a linear map D : BC →R by [z1] + · · · + [zn] →D(z1) + · · · +
D(zn), and Bloch’s result (related to Mostow rigidity) says that the set D(BC)
coincides with D(BQ), where BQ is deﬁned by (12) but with the zν lying in
Q
× ∖{1}. Thus D(BC) is countable, and (9) and (10) imply that Vol is
contained in this countable set. The structure of BQ , which is very subtle,
will be discussed below.
16
Don Zagier
We give an example of a non-trivial element of the Bloch group. For con-
venience, set α = 1 −√−7
2
, β = −1 −√−7
2
. Then
2 ·
1 + √−7
2

∧
1 −√−7
2

+
−1 + √−7
4

∧
5 −√−7
4

= 2 · (−β) ∧α +
 1
β

∧
α2
β

= β2 ∧α −β ∧α2 = 2 · β ∧α −2 · β ∧α = 0 ,
so
2

1 + √−7
2

+

−1 + √−7
4

∈BC .
(13)
This example should make it clear why non-trivial elements of BC can only
arise from algebraic numbers: the key relations 1+β = α and 1−β−1 = α2/β
in the calculation above forced α and β to be algebraic.
