---
doc_id: arxiv-1101.3374v1
doc_title: "PONTRYAGIN INVARIANTS AND INTEGRAL FORMULAS FOR MILNOR’S TRIPLE LINKING NUMBER"
section_id: sec-001-4-explicit-formulas-for-the-characteristic-map
section_title: "Explicit formulas for the characteristic map"
section_number: 4
pages: 20-57
source_pdf: 1101.3374v1.pdf
source_sha256: 01d76c1d259c1d51
doc_brief: "PONTRYAGIN INVARIANTS AND INTEGRAL FORMULAS FOR MILNOR’S TRIPLE LINKING NUMBER — To each three-component link in the 3-sphere, we associate a geometrically natural characteristic map from the 3-torus"
---
In this section we give an explicit diﬀeomorphism from the Grassmann manifold G 2R4
of oriented 2-planes through the origin in 4-space to a product of two 2-spheres, and then
use it to give a formula for the characteristic map gL :T 3→S2 of a three-component link
L in the 3-sphere.
We also describe an alternative formhL :T 3→S2 of the characteristic map, homotopic
togL but more convenient for the proof of Theorem A that we will give in Section 6. The
formula for hL will reveal a close connection between the characteristic map and the
classical Gauss map T 2→S2 for two-component links in 3-space.
20
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
Throughout we regard R4 as the algebra of quaternions, with orthonormal basis
1,i,j,k and unit sphere S3 (oriented so that i,j,k is a positive frame for the tangent
space to S3 at the point 1), and R3 as the subspace of pure imaginary quaternions
spanned byi,j andk, with unit sphere S2. Thus S3 is viewed as the multiplicative group
of unit quaternions, and S2 as the subset of pure imaginary unit quaternions.
For any quaternionq =q0 +q1i+q2j +q3k, let ¯q denote its conjugateq0−q1i−q2j−q3k,
which coincides with q−1 when q∈ S3, and let Re (q) = q0 and Im (q) = q1i +q2j +q3k
denote its real and imaginary parts.
The Grassmann manifold G 2R4
It is well known that G 2R4 can be identiﬁed with a product of two 2-spheres. In
particular, we will use the diﬀeomorphism
π : G2R4−→S2×S2
that maps the oriented plane ⟨a,b⟩, spanned by an orthonormal 2-frame ( a,b ) in R4, to
the point (b¯a, ¯ab) in S2×S2. Note that both coordinates
π+⟨a,b⟩ = b¯a and π−⟨a,b⟩ = ¯ab
do in fact lie in S2 since right and left multiplication by ¯a are orthogonal transformations
of R4, carrying the orthonormal frame (a,b ) to the orthonormal frames (1,b ¯a) and (1, ¯ab).
To see that π is well-deﬁned, consider any other orthonormal basis for the plane ⟨a,b⟩.
It must be of the form (ac,bc ) for some c in the circle subgroup C¯ab through ¯ab, since this
group acts on the plane by rotations. Thus it suﬃces to check that bcac = b¯a, which is
immediate, and that acbc = ¯ab, which is true since c commutes with ¯ab.
To see thatπ is in fact a diﬀeomorphism, we can simply write down the inverse. It maps
a pair (x,y ) in S2×S2 to the plane ⟨c,cy⟩ where c is the midpoint of any geodesic arc
fromx toy onS2. This can be veriﬁed by a straightforward calculation using the fact that
conjugation by a pure imaginary quaternion rotates the 2-sphere about that quaternion
byπ radians, so cy¯c =x.
The characteristic map gL
Recall from the introduction that the Grassmann map G : Conf 3S3→ G2R4 sends a
triple (x,y,z ) of distinct points in S3 to the plane they span in R4, translated to pass
through the origin, and oriented so that
G(x,y,z ) = ⟨x−z,y−z⟩.
We have extended notation so that for any two linearly independent vectorsa andb in R4,
the symbol ⟨a,b⟩ denotes the oriented plane they span. Then, given a three-component
link L in S3, its characteristic map gL :T 3→S2 is deﬁned using the Grassmann map G
and the projection π+ : G2R4→S2 by the formula
gL(s,t,u ) = π+G(x,y,z ) = π+⟨x−z,y−z⟩
where x =x(s), y =y(t) and z =z(u) parametrize the components of L.
21
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
To make this explicit, and to show that using π− in place of π+ in the deﬁnition would
not change the homotopy class of gL, we need expressions for π±⟨a,b⟩ when a and b are
arbitrary linearly independent vectors in R4, but not necessarily orthonormal.
For example, if a and b are orthogonal, then b¯a and ¯ab are still pure imaginary, and so
need only be normalized to give π+⟨a,b⟩ and π−⟨a,b⟩.
For a general pair of linearly independent vectorsa andb, the vectorc =b−(b·a/a·a)a,
where· is the dot product in R4, is orthogonal to a and satisﬁes⟨a,c⟩ =⟨a,b⟩. Therefore
π+⟨a,b⟩ =π+⟨a,c⟩, which equals the unit normalization of the vector c¯a =b¯a−b·a. But
b·a = Re (b¯a), and so π+⟨a,b⟩ is the unit normalization of Im ( b¯a). Similarly π−⟨a,b⟩ is
the unit normalization of Im (¯ab). Therefore, for any two linearly independent vectors a
and b, we have
π±⟨a,b⟩ = ( a,b )±/|(a,b )±|
where (, )± are the skew symmetric bilinear forms on R4 deﬁned by
(a,b )+ = Im b¯a and ( a,b )− = Im ¯ab.
It follows that gL(s,t,u ) is the unit normalization of the vector
F (x,y,z ) = ( x−z,y−z)+ = ( x,y )+ + (y,z )+ + (z,x )+
= ( ix·y +iy·z +iz·x , jx·y +jy·z +jz·x , kx·y +ky·z +kz·x)
where the last expression follows from the formula ( a,b )+ = (ia·b,ja·b,ka·b). This
formula is seen as follows. By deﬁnition, ( a,b )+ = Im (b¯a) = (i·b¯a)i + (j·b¯a)j + (k·b¯a)k.
But q·b¯a = qa·b for any q (in particular i, j or k) since right multiplication by the
unit quaternion a/|a| is an isometry, and so ( a,b )+ = (ia·b)i + (ja·b)j + (ka·b)k =
(ia·b,ja·b,ka·b). Summarizing, we have shown:
Proposition 4.1. The characteristic map gL : T 3→ S2 of a three-component
link L in S3 is given by the formula
gL(s,t,u ) = F (x,y,z )/|F (x,y,z )|
wherex =x(s), y =y(t) and z =z(u) parametrize the components of L, and
F : Conf 3S3→ R3 is the function deﬁned above.
This formula for gL will be used in our proof of Theorem B in Sections 8 and 9. For
Theorem A it will be more convenient, for the most part, to use an alternative form of
the characteristic map that we introduce next.
The asymmetric characteristic map hL
Given a three-component linkL in the 3-sphere, we deﬁne below an asymmetric version
hL :T 3−→S2
of the characteristic map in which the last component of L plays a distinguished role, and
show that it is homotopic to the earlier deﬁned symmetric characteristic map gL. As will
be seen, the map hL can be viewed as a parametrized family of Gauss maps for twisted
versions of the ﬁrst two components of L, parametrized by the third component.
For notational economy, we will use ⌈⌊q⌉⌋to denote the unit normalization q/|q| of any
nonzero quaternion q.
22
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
The key observation that motivates the deﬁnition of hL is that the Grassmann map
G : Conf 3S3→ G2R4 factors up to homotopy through the Stiefel manifold V2R4 of
orthonormal 2-frames in 4-space.
More precisely, let pr z denote stereographic projection of S3−{z} onto z⊥, the
3-plane through the origin in R4 orthogonal to z. Then we deﬁne the Stiefel map
H : Conf3S3−→V2R4 , (x,y,z )↦−→(z,⌈⌊przx− przy⌉⌋)
(recall that the square brackets signify unit normalization), and will show that it is a
homotopy equivalence whose composition with the canonical projection
P : V2R4−→G2R4 , (z,v )↦−→⟨z,v⟩
is homotopic to the Grassmann map G.
To see this, ﬁrst observe that there is a deformation retraction of Conf3S3 to its subspace
V = {(v,−z,z )| v⊥z}
deﬁned as follows. Start with ( x,y,z )∈ Conf3S3, and consider the points pr zx and przy
inz⊥. Translation inz⊥ moves przy to the origin, and then dilation inz⊥ makes the trans-
lated przx into a unit vector. Conjugating this motion by pr z movesx to⌈⌊przx− przy⌉⌋,
movesy to−z, and leaves z ﬁxed, as pictured in Figure 14, thus deﬁning a deformation
retraction of Conf 3S3 to its subspace V , sending (x,y,z ) to (⌈⌊przx− przy⌉⌋,−z,z ).
z
−z
x
y
przx
przy
z⊥
S3
⌈⌊przx− przy⌉⌋ = (pr zx− przy)/|przx− przy|
Figure 14. The deformation retraction Conf 3S3→V
Identifying V with V 2R4 via (v,−z,z ) ↔ (z,v ), this shows that H is a homotopy
equivalence with homotopy inverse I given by I(z,v ) = (v,−z,z ). The calculation
GI(z,v ) = ⟨v−z,−2z⟩ = ⟨z,v⟩ = P (z,v ),
shows that GI =P , and so G≃PH as claimed.
Now observe that there are two natural homeomorphisms from the Stiefel manifold
V2R4 to S3×S2 that arise from viewing S3 as the unit quaternions and S2 as the pure
imaginary unit quaternions, namely ( z,v )↦→ (z,v ¯z) and ( z,v )↦→ (z, ¯zv). These yield
projections π± : V2R4→S2 given by
π+(z,v ) = v¯z and π−(z,v ) = ¯zv.
23
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
These are just the lifts to V 2R4 of the previously deﬁned projections π± : G 2R4→ S2
with the same names.
Deﬁne the asymmetric characteristic map hL : T 3→ S2 to be the composition
π+HeL, that is,
hL(s,t,u ) = ⌈⌊przx− przy⌉⌋¯z
where as usual x =x(s),y =y(t) andz =z(u) parametrize the components of L, and the
square brackets indicate unit normalization.
Proposition 4.2. The two versions gL and hL of the characteristic map of a
three-component link L in S3 are homotopic. Furthermore, these maps are
independent, up to homotopy, of the choice of projections π+ or π− used in
their deﬁnitions.
Proof. By deﬁnition gL = π+GeL and hL = π+HeL, shown in the diagram below as the
maps from left to right across the bottom and top, respectively.
V2R4
T 3
eL
- Conf3S3
H -
S2
π+
-
G2R4
P
? π+
-
G
-
Here eL(s,t,u ) = (x(s),y (t),z (u)) records the parametrization of the link, and G and H
are the Grassmann and Stiefel maps with their associated projections π+. It was shown
above that the left triangle in the diagram commutes up to homotopy, and the right
triangle commutes on the nose. Therefore hL and gL are homotopic.
Now the same argument shows that the maps h′
L = π−HeL and g′
L = π−GeL are
homotopic. Hence to complete the proof, it suﬃces to show thathL andh′
L are homotopic.
To do so, view V 2R4 as the unit tangent bundle of S3, with projection p to the base S3
given by p(z,v ) = z. Then the composition pHeL is null-homotopic, since it maps onto
the third component of L, and so the map HeL is homotopic to a map into any S2-ﬁber
of the bundle V 2R4→ S3. We choose the ﬁber over z = 1, where the two projections
π+(z,v ) =v¯z and π−(z,v ) = ¯zv coincide. It follows that hL and h′
L are homotopic. □
A Gaussian view of the asymmetric characteristic map
The formula above forhL involves ﬁrst normalizing a vector inz⊥, and then multiplying
by ¯z to move it to the unit sphere S2 in the pure imaginary quaternion 3-space R3. We
would like to express this directly as the normalization of a vector in R3.
A geometric argument shows that stereographic projection pr a is given by
prab = (Im b¯a)a/(1− Re b¯a)
and it follows that (prab)c = pracbc for any three unit quaternions a, b and c with a⁄=b.
Hence the formula hL(s,t,u ) =⌈⌊przx− przy⌉⌋¯z can be rewritten as
hL(s,t,u ) = ⌈⌊pr1x¯z− pr1y¯z⌉⌋
= ⌈⌊pr−1(−y¯z)− pr−1(−x¯z)⌉⌋
24
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
where, as usual, x =x(s), y =y(t) and z =z(u) parametrize L, and the square brackets
indicate unit normalization in R3. We favor the last expression because stereographic
projection from−1 is orientation-preserving, while from 1 it is orientation-reversing.
Now for any two distinct unit quaternions a and z, introduce the abbreviation
az = pr−1(−a¯z) ∈ R3,
and so in particular a−1 = pr−1a. Then we can write
hL(s,t,u ) = ⌈⌊yz−xz⌉⌋.
For ﬁxedu, this is just the classical Gauss map for the two-component link Xz∪Yz⊂ R3
that is the image of the ﬁrst two components X∪Y of L under the map a↦→ az. Thus
the asymmetric characteristic map hL can be viewed as a one-parameter family of Gauss
maps for images in 3-space of X∪Y . The third component Z provides the parameter and
determines the axes about which these images are gradually twisted.
In the next section, we will explain this perspective more carefully. But we can see
right now that it yields an easy proof of the ﬁrst part of Theorem A, equating the pairwise
linking numbers of the link L with the degrees of the restriction of its characteristic map
gL to the coordinate 2-tori.
Proof of the ﬁrst statement in Theorem A
It can be arranged by an isotopy of L that z(0) =−1. Then the restriction of hL to
the coordinate 2-torus S1×S1× 0 is precisely the Gauss map of the stereographic image
X−1∪Y−1 of X∪Y , whose degree is equal to the linking number Lk( X,Y ) since pr−1 is
orientation-preserving. Since gL is homotopic to hL, the same is true for gL. But then it
follows from the symmetry of gL that Lk(X,Z ) and Lk(Y,Z ) are given by the degrees of
gL on S1× 0×S1 and on 0×S1×S1, respectively.
The proof of the second statement in Theorem A – which relates the triple linking
number of L to the Pontryagin ν-invariant of its characteristic map – is more delicate. It
will occupy us for the next two sections.
5. The Pontryagin ν-invariant of the characteristic map
Fix a link L in S3 with three components X, Y and Z parametrized by x = x(s),
y =y(t) andz =z(u). Recalling that S3 is regarded as the group of unit quaternions, the
asymmetric characteristic map hL :T 3→S2 is given by
hL(s,t,u ) = ( yz−xz)/|yz−xz|
whereaz is an abbreviation for the vector pr−1(−a¯z) in pure imaginary quaternion 3-space
R3. To carry out the proof of Theorem A, we need a way to compute the absolute
Pontryaginν-invariant ofhL. A procedure for doing so is described here.
Throughout this section and the next, R3 is pictured in the usual way, with theij-plane
horizontal and the k-axis pointing straight up as in Figure 15. In particular, we view k as
the north pole of the unit sphere S2.
25
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
i
j
k
Figure 15. Pure imaginary quaternion 3-space
Outline of the procedure for computing ν(hL)
First, we will manipulate L by a link homotopy into a favorable position – referred to
as generic below – so that, in particular, the north pole k of S2 is a regular value of hL.
Then we will determine the associated Pontryagin link
L = h−1
L (k) ⊂ T 3
by giving a simple method for constructing a toral diagram for it, in the sense of Section 3.
Roughly speaking, our approach is as follows.
By deﬁnition of hL, the Pontryagin link L consists of all ( s,t,u )∈ T 3 for which the
vector in R3 fromxz toyz points straight up, where x =x(s),y =y(t) andz =z(u). The
genericity of L will imply that for some points ( s,t ) in the 2-torus T 2 there is a unique
u = u(s,t )∈ S1 that will make this happen, while for all other points ( s,t ), no u will
work. Furthermore, the set D of all points of the ﬁrst kind, called isogonal points for
reasons explained below, is a smooth 1-dimensional submanifold of T 2 whose components
we call icycles.
Thus
L = {(s,t,u )∈T 3| (s,t )∈D and u =u(s,t )},
the graph of the function u(s,t ) over the collection D of icycles in T 2. When suitably
oriented and decorated with framing and vertical winding numbers, D will be the desired
toral diagram ofL.
In particular, the icycles in D correspond to certain oriented cycles of vectors directed
from X to Y , which we call bicycles, that are easily spotted from a picture of L. Each
bicycle has a longitudinal and meridional degree, recording how much it turns and
spins relative to the standard open book structure onS3. The framing and vertical winding
number of the corresponding icycle are determined by these degrees.
Therefore a diagram forL can be constructed once we identify the bicycles in L. With
this diagram in hand, the methods of Section 3 can then be used to compute ν(hL).
We now give the details of this procedure. There are three geometries involved: spherical
geometry in S3, where the link L lives, Euclidean geometry in R3, the setting for the
asymmetric characteristic map, and hyperbolic geometry in the complex upper half plane
26
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
H, which turns out to be for us the natural geometry on the pages of the “standard” open
book decomposition of R3. We begin with an explicit construction of this open book,
which provides a framework for the discussion that follows.
The standard open books in R3 and S3
Consider the great circle K in S3 through 1 and k, and the orthogonal great circle C
through i and j. Orient both circles by left complex multiplication by K (i.e. from 1
towardk on K, and i towardj on C) so that their linking number is +1.
Stereographic projection from −1 carries K onto the k-axis in R3, and ﬁxes C, which
now appears as the unit circle in the ij-plane. The complement V of the k-axis in R3 is
naturally identiﬁed with the product of a circle S1 (viewed as the quotient R/2πZ) with
the complex upper half plane H (which for later purposes will be viewed as the hyperbolic
plane) via the diﬀeomorphism
V −→ S1× H
with coordinates 𝓁 : V−→S1 and m : V−→ H given by
𝓁(q) = arg( q1 +q2i) and m(q) = q3 +|q1 +q2i|i.
for q = q1i +q2j +q3k∈ V = R3−k-axis. In other words, if q = (r,θ,z ) in cylindrical
coordinates, then 𝓁(q) = θ and m(q) = z +ri. We call 𝓁 and m the longitudinal and
meridional projections in R3, and refer to 𝓁(q) as the polar angle of q.
The longitudinal projection deﬁnes the standard open book in R3, with binding the
k-axis, and with pages Pθ = 𝓁−1(θ) for θ∈ S1. The pages are just the oriented vertical
half-planes bounded by the k-axis, each indexed by its polar angle as shown in Figure 16.
The meridional projection serves to identify each page Pθ with the hyperbolic plane H,
with “center” iθ =i cosθ +j sinθ corresponding to i. The union of all the page centers
is the unit circle C.
i iθ
j
k
θ
binding
pages
Pθ
C
Figure 16. The standard open book in R3
27
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
The longitudinal and meridional projections in R3 lift to S3 (in the complement of K)
by composing with stereographic projection from−1. Relying on the context, we continue
to denote them by 𝓁 and m, and to refer to 𝓁(q) as the polar angle of q. Explicitly
𝓁(q) = arg( q1 +q2i) and m(q) = q3 +|q1 +q2i|i
1 +q0
.
for q =q0 +q1i +q2j +q3k∈S3−K. Here we are using the formula
pr−1q = (Im q)/(1 + Req) = (q1i +q2j +q3k)/(1 +q0),
and then plugging this into the formula above for the longitudinal and meridional projec-
tions in R3.
Just as in R3, the longitudinal projection in S3 deﬁnes the standard open book inS3,
with binding K, and with pages Hθ =𝓁−1(θ). The pages are now open great hemispheres
in S3 with centers (i.e. poles) iθ along the great circle C, and with K as equator. By
design, pr−1 maps each hemispherical page Hθ in S3 onto the corresponding half-planar
page Pθ in R3.
We now turn our attention back to links in the 3-sphere.
Generic links
A three-component link L =X∪ Y ∪ Z in S3 is generic if
(1) Z coincides with the oriented binding K of the standard open book, and
(2) X and Y wind “generically” around Z.
More precisely, the second condition requires the restriction toX∪Y of the longitudinal
projection 𝓁 : S3−K−→S1, which sends each point to its polar angle, to be a Morse
function with just one critical point per critical value. Geometrically, this means X and
Y are transverse to the pages of the standard open book in S3, except for ﬁnitely many
pages where exactly one of them turns around at a single point. These will be called the
critical points ofL, while all other points on X∪Y will be called regular points. Each
regular point w has a sign, denoted sign(w), when viewed as an intersection point of L
with the page containing w. Thus sign(w) = +1 or−1 according to whether L is oriented
in the direction of increasing or decreasing polar angle near w.
An example of a generic link is shown in Figure 17. It has four critical points, two on
X and two on Y , indicated by dots in the picture.
Any three-component link in S3 is evidently link homotopic to a generic one: ﬁrst
unknot the last component by a link homotopy and move it to coincide with K, and then
adjust the ﬁrst two components by a small isotopy to satisfy the genericity condition (2).
From this point on we assume that L is generic without further mention.
28
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
X
Y
Z
Figure 17. A generic link
As a consequence, we will show the following:
(a) The north pole k∈S2 is a regular value of the characteristic map hL.
(b) There is a simple method for constructing a toral diagram for the associated
Pontryagin linkL =h−1
L (k) from a picture of L.
This is the content of the “bicycle theorem” below. To state it precisely, we need to
introduce the key notion of a bicycle in L, and its associated icycle in T 2.
Bicycles and icycles
Assume, as always, that the components X,Y andZ ofL are parametrized by smooth
functions x = x(s), y = y(t) and z = z(u) with nowhere vanishing derivatives. In
particular, points ( s,t ) in the 2-torus parametrize pairs of points x∈ X and y ∈ Y .
Suppose that x and y have the same polar angle θ, or equivalently that they lie in a
common pageHθ of the standard open book in S3. Then we call (s,t ) an isogonal point
in T 2, and call (x,y ) a page vector in L with polar angle θ, reﬂecting the fact that the
vector in R3 from pr−1(x) to pr−1(y) lies entirely on the half-planar page Pθ.
A page vector (x,y ) will be called critical ifx ory is a critical point of L, and regular
if both x andy are regular. A regular page vector is positive if the oriented strands of L
through x and y point in the same direction, meaning sign( x) = sign(y), and is negative
if they point in opposite directions. These notions are illustrated in Figure 18, in which
the vectors labeled 1 and 2 are positive regular page vectors, 3 is negative regular, and 4
is critical.
Now consider the spaces
D = {isogonal points in T 2} and P = {page vectors in L}.
By deﬁnition D parametrizesP. The genericity of L implies that P consists of a ﬁnite
number of disjoint cycles of page vectors, and that D consists of a ﬁnite collection of
smooth simple closed curves in T 2. Orient P so that it points to the right (meaning in
the direction of increasing polar angle) at each positive regular page vector in it, and to
the left at each negative regular page vector. This gives a well-deﬁned orientation on P,
inducing one onD as well. We call these the preferred orientations onP andD.
29
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
1
2
3
4
X Y
Z
Figure 18. Page vectors
Deﬁnition. A bicycle (or “bi-cycle”) in L is a component Pi ofP, that is, an oriented
cycle of page vectors. Each bicycle is parametrized by a component Di ofD, which we
call its associated icycle (or “i-cycle”).
Some examples of bicycles and their associated icycles
We ﬁrst draw in Figure 19 four local pictures of a bicycle near a regular page vector,
and below them, their parametrizing icycles. It is understood that these pictures take
place somewhere in front of the upward pointing Z axis. The four cases represent the
possible directions of X and Y relative to the page containing the vector. In each case,
the orientation of the bicycle is indicated by a squiggly arrow.
Y
X
Y
X
Y
X
Y
X
s
t
s
t
s
t
s
t
Figure 19. Local pictures of a bicycle and its corresponding icycle
For an example of a full bicycle, consider the “clasp” between X and Y pictured in
Figure 20(a). This gives rise to the bicycle in Figure 20(b), passing successively through
the vectors labeled 1, 2, 3, 4 and then back to 1. The associated icycle is a counterclockwise
30
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
circle inT 2, shown in Figure 20(c). The route taken by this bicycle is “short” in the sense
that it does not wind around the binding, although it does spin within the pages.
X
Y
Z
1
2
3
4
s
t
1
2
3
4
(a) the clasp (b) the bicycle (c) the icycle
Figure 20. Bicycle arising from a clasp
As another example, the link shown in Figure 17 and reproduced in Figure 21(a) below
has three bicycles. Two of them are short, arising from the clasps as in the previous exam-
ple, while the remaining long one oscillates back and forth in the longitudinal direction,
eventually making one full revolution around the binding. It is an instructive exercise left
to the reader to recover the plot of the associated icycles in Figure 21(b), in which the
trivial circles labeledA andB correspond to the clasps inL with the same labels, C labels
the icycle that parametrizes the long bicycle, and the corners of the square parametrize
the pair (x,y ) indicated by the dots in Figure 21(a).
s
t
X
Y
Z
A B A
B
C
(a) the generic link L (b) the icycles of L
Figure 21. A generic link and its icycles
Before proceeding, we remind the reader that our interest in icycles associated to L
stems from the fact that – when suitably decorated – they give a toral diagram for a
Pontryagin link of the characteristic map hL. This is the content of the bicycle theorem.
The Bicycle Theorem
The longitudinal and meridional projections on S3−K, deﬁned earlier, induce projec-
tions by the same name on the space P of page vectors,
S1 𝓁←−P m−→ H,
31
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
given by 𝓁(x,y ) =𝓁(x) =𝓁(y) and m(x,y ) = arg(m(y)−m(x)). In other words 𝓁(x,y ) is
the polar angle that parametrizes the common hemispherical page in S3 containingx and
y, and m(x,y ) is the argument of the vector from m(x) to m(y) in H.
Using these projections, we deﬁne the longitudinal and meridional degrees of a
bicyclePi in L by
𝓁i = deg( 𝓁|Pi) and mi = deg( m|Pi).
These integer invariants record, respectively, the number of times Pi travels around the
binding Z, and the number of times its vectors spin around in the pages as it goes.
For example, any bicycle arising from a clasp between X and Y has zero longitudinal
degree, while its meridional degree can be ±1. In particular, the one shown in Figure 20
has meridional degree−1, while the ones labeled A andB in Figure 21(a) have degrees 1
and−1, respectively. The long bicycle in Figure 21(a), labeled C, has longitudinal degree
2 and meridional degree 1.
For any icycle Di in T 2, parametrizing a bicycle Pi in L, deﬁne the framing ni and
vertical winding number ri ofDi by
ni = −𝓁i−mi and ri = mi
where 𝓁i and mi are the longitudinal and meridional degrees of Pi.
We can now state the main result of this section.
Bicycle Theorem. LetL be a generic link in S3. Then
(a) The north pole k∈S2 is a regular value of hL :T 3→S2.
(b) The collection D of icycles of L, together with their framings and
vertical winding numbers as deﬁned above, forms a toral diagram for
the associated Pontryagin link L =h−1
L (k).
Before proving this theorem, we illustrate how it can be used to compute the Pontryagin
invariant of the characteristic map of a generic link.
Computing ν(hL) for a generic link L using the bicycle theorem
As a ﬁrst example, again consider the link L pictured in Figure 21(a). As noted above,
it has three bicyles A, B, C, with longitudinal degrees 0, 0, 2, meridional degrees 1,−1, 1,
and so by deﬁnition, framings −1, 1,−3 and vertical winding numbers 1,−1, 1.
By the bicycle theorem, the Pontryagin link for the characteristic map hL has toral
diagram as shown in Figure 21(b) with vertical winding numbers 1, −1 and 1 on the
icyclesA,B andC, and with global framing n =−1 + 1− 3 =−3. Thus the total vertical
winding number is r = 1− 1 + 1 = 1 and from the diagram we compute the horizontal
winding numbers to be p =−1 andq =−2. (These values for the winding numbers of the
diagram are conﬁrmed by the calculations p = Lk(Y,Z ) =−1, q = Lk(X,Z ) =−2 and
r = Lk(X,Y ) = 1.) Thus the invariant ν(hL) is well deﬁned modulo 2 = 2 gcd(−1,−2, 1).
Using a base point in the lower right corner of the diagram, and straight line paths
from the icycles to the base point, the depths of the icycles A,B andC are 1,−1 and−1.
Thus by Proposition 3.1 we conclude that
ν(hL) = n +pq +∑diri = −3 + 2 + 1 = 0 ∈ Z2.
32
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
Although the purpose of this example is to illustrate how the bicycle theorem is used
for computations, we note that Theorem A (yet to be proved) yields the same result here
eﬀortlessly, since it implies that the Pontryagin invariant of the characteristic map of any
three-component link inS3 is even. Therefore, when the pairwise linking numbersp,q and
r are relatively prime, as they are in this case, the computation is modulo 2 gcd(p,q,r ) = 2,
and so the Pontryagin invariant is zero.
Double crossing changes
For our next example we analyze the eﬀect on ν(hL) of changing two crossings of
opposite signs between the ﬁrst two components of a generic link L = X∪Y∪Z. This
will be a key step in our inductive proof of Theorem A.
To this end, choose a positive and a negative crossing between X and Y in a suitable
projection ofL, and let (x+,y +) and (x−,y−) be the corresponding page vectors. Changing
both of the crossings yields a new link ˆL, with the same pairwise linking numbers as L.
This is illustrated in Figure 22 where L is the Borromean rings, shown on the left, and ˆL
is the unlink, shown on the right.
X
Y
Z
(a) the Borromean rings L
ˆX
ˆY
ˆZ
(b) the unlink ˆL
Figure 22. A double crossing change
We then say thatˆL is obtained from L by a double crossing change, and propose to
use the bicycle theorem to compute the resulting change
∆ν = ν(hˆL)−ν(hL)
in Pontryagin invariants.
As it turns out, there is a simple formula for ∆ ν involving the link L0 obtained from L
by “smoothing” both crossings in the usual way:
The smoothed link L0 has three components, P and Q (replacing X and Y ) and Z.
The component P goes from + to− alongY , and then back from− to + along X, where
we retain the + and − labels after smoothing, while Q goes from + to − along X, and
then back from − to + along Y . This is illustrated in Figure 23 for the double crossing
33
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
change shown in Figure 22, where we use X+− to denote the arc on X from + to− , and
so forth.
P
Q
Z
X+−
X−+
Y+−
Y−+
Figure 23. The smoothed link L0 = P∪Q∪Z
Then we have the following consequence of the Bicycle Theorem:
Corollary 5.1. (Double Crossing) If L =X∪Y∪Z is transformed into ˆL by
a double crossing change, and P and Q are the components of the associated
smoothing of X∪Y , as explained above, then the corresponding Pontryagin
invariants change by
∆ν = 2 Lk(P,Z ) = −2 Lk(Q,Z ) ∈ Z2 gcd(p,q,r)
wherep, q and r are the pairwise linking numbers of the components of L.
Proof. First note that
Lk(P∪Q,Z ) = Lk( X∪Y,Z ) = p +q = 0 ∈ Zgcd(p,q,r)
so it suﬃces to establish the ﬁrst equality in the corollary.
We may assume that the two page vectors v+ = (x+,y +) and v− = (x−,y−) associated
with the chosen crossings lie on distinct hemispherical pages H+ and H− of the standard
open book in S3, and that these pages contain no critical points in the link. These two
page vectors may lie in distinct bicycles in L, or they may lie in the same bicycle.
Suppose ﬁrst that v+ and v− lie in distinct bicyclesP+ andP− inL. When we changeL
toˆL, these bicycles will change, but the icyclesD+ andD− in the 2-torus that parametrize
them will stay the same. However, their vertical winding numbersr+ andr− (which record
the meridional degrees of P+ andP−) and their framings n+ and n− (which record the
negative of the sum of the meridional and longitudinal degrees ofP+ andP−) will change.
In particular, we claim that
ˆr+ = r+− 1 and ˆr− = r− + 1,
and consequently ˆn+ =n+ + 1 and ˆn− =n−− 1 since the longitudinal degrees of the
bicycles clearly do not change. The ﬁgure below helps us to see this.
X
Y
L ˆX
ˆY
ˆL
34
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
In this ﬁgure, we start with a positive crossing in L and change it to a negative crossing
in ˆL. Since the strands of X and Y are both pointing to the right, the bicycle P+ is
moving from left to right. During this motion the page vectors in P+ undergo half a
counter-clockwise rotation with respect to the preferred orientation on the pages. In the
corresponding picture for ˆL , we see half a clockwise rotation. Therefore the bicycle in ˆL
has one more full clockwise rotation in the pages than inL, and soˆr+ =r+−1 as claimed.
If, for example, we switched the arrow on the strand of Y , we would have a negative
crossing, but then the corresponding bicycle would be moving from right to left, and we
would see that ˆr− =r− + 1 as claimed. With this guidance, we leave the remaining cases
to the reader.
Now suppose that the page vectors v+ and v− lie in the same bicycle P+ =P−. Then
the above changes in vertical winding number r for the corresponding icycle D+ =D−
will cancel, and so we see that neither the vertical winding number nor the framing of the
icycle will change, that is ˆr± =r± andˆn± =n±.
Note that in either case, whether v+ and v− lie in the same or diﬀerent bicycles, the
total framing n of the diagram (the sum of the framings of the icycles) does not change.
At this point we recall Proposition 3.1, which tells us that
ν(hL) = n +pq +∑diri.
In passing from L to ˆL via the double crossing change, we have just seen that the total
framing n does not change, and the pairwise linking numbers p and q certainly do not
change. We have also seen that the icycles stay the same, so their depths di do not
change. Only the winding numbers r+ and r− of the (possibly equal) icycles D+ andD−
may change. In particular, they also do not change when the page vectors
v+ = ( x(s+),y (t+)) and v− = ( x(s−),y (t−))
lie in the same bicycle, and so ∆ ν = 0 in this case, while they change to ˆr+ =r+− 1 and
ˆr− =r− + 1 when v+ and v− lie in distinct bicycles, in which case we have
∆ν = ν(hˆL)−ν(hL)
= d−(ˆr−−r−) +d+(ˆr+−r+)
= d−−d+.
Thus in either case it remains to prove that d−−d+ = 2 Lk(P,Z ).
To show this, we must compute the depths d+ and d− ofD+ andD−. This requires a
choice of base point, and then a choice of paths γ+ and γ− fromD+ andD− to this base
point. We let ( s+,t−) be the base point, and use the vertical path γ+ from (s+,t +) to
(s+,t−) and the horizontal path γ− from (s−,t−) to (s+,t−).
The depth d− of the componentD− ofD counts the intersections of γ− withD, which
means that it counts the times that ( x(s),y (t−)) is a page vector for s− ≤ s ≤ s+,
assuming parametrizations set up so that s− < s+ . Since y(t−) already lies in the page
H−, this means we are counting the times that x(s) also lies in H− for s−≤s≤s+ . In
other words we are counting the intersection number X−+·H− . Examining Figure 19,
we ﬁnd that the signs of the intersection points of γ− withD agree with the signs of the
35
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
corresponding intersection points of X−+ with H−, and hence
d− = 2 X−+·H− mod 2 gcd(p,q,r ).
In a similar fashion, we ﬁnd that intersections of γ+ withD correspond to intersections
of Y+− with H+, but in this case, the signs of corresponding points of intersection are
opposites, and so the depth of D+ is
d+ = −2Y+−·H+ mod 2 gcd(p,q,r ).
Therefore the assertion that d−−d+ = 2Lk(P,Z ), which will complete the proof of the
corollary, reduces to the identity
X−+·H− +Y+−·H+ = Lk( P,Z ).
But this follows easily from the fact that P =X−+∪Y+−. Figure 24 helps us to see this.
In the ﬁgure, the arcX−+ winds around the verticalZ axisk times and the arcY+− winds
around it 𝓁 times, while the entire loop P =X−+∪Y+− winds around it k +𝓁 + 1 times.
By our half-counting convention, we have
X−+·H− = 1 /2 +k and Y+−·H+ = 1 /2 +𝓁
and the result follows. □
H− H+
X−+
Y+−
Z
k
𝓁
− +
Figure 24. The linking of P =X−+∪Y+− and Z
For the inductive step of the proof of Theorem A in the next section, we will need to
apply this formula for ∆ ν under the double crossing change L→ ˆL shown in Figure 25
(which will be seen to be equivalent to a delta move). It is understood that L and ˆL
should coincide outside the picture, where in fact they can be arbitrary. Indeed, if not
generic outside the ball, they can be adjusted by a link homotopy to become so, and then
the methods described above apply. Since the component Q of the smoothed link L0 is
just a meridian of Z with Lk(Q,Z ) =−1, it follows that ∆ν = 2.
Thus we have proved the following:
36
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
X
Y
Z
+ − − +
(a) the link L (b) the link ˆL
Figure 25. A simple double crossing change
Corollary 5.2. If two links L and ˆL coincide outside a 3-ball, and appear in
the ball as shown in Figure 25, then ν(h ˆL) =ν(hL) + 2.
We now embark on the proof of the bicycle theorem, which will occupy us for the rest
of this section.
Proof of the bicycle theorem
Start with a generic link L in S3 where, as usual, x = x(s), y = y(t) and z = z(u)
parametrize the three components X, Y and Z. Then Z coincides with the binding K of
the standard open book, which is the circle subgroup of S3 containing the quaternion k.
Looking back at the formula for the characteristic map
hL(s,t,u ) = ( yz−xz)/|yz−xz| where az = pr−1(−a¯z),
we see that we must understand theK-action sendingz∈K to the automorphisma↦→a¯z
ofS3, and the inducedK-action on R3 via stereographic projection. Visualizing how these
actions transform the pages of the standard open books will aid us in our subsequent
arguments, and we do this next.
The geometry of the K-action
For anyz = cosα +k sinα in the binding K, right multiplication by ¯z = cosα−k sinα
is an isometry of S3 that rotates K by−α radians, likewise rotates the orthogonal great
circle C of page centers by α radians, and so advances each hemispherical page Hθ to
the page Hθ+α while simultaneously rotating the page by −α radians about its center iθ.
Therefore, as z traversesK, any given page turns once around K, successively occupying
the positions vacated by the other pages. During this time, the page spins once negatively
about its center, so that in total it is following a left-handed screw motion along C.
This turning of the hemispherical pages about K in S3 is transferred by stereographic
projection to a turning of the half-planar pages about the k-axis in R3, while the spherical
rotations of the pages in S3 become hyperbolic rotations of the pages in R3 about their
centers. This is a consequence of the conformality of stereographic projection, which
implies that the page identiﬁcation Hθ↔Pθ is conformal. Once again, the net eﬀect is a
left-handed screw motion along C.
This description of the K-action has the following technical consequence that is critical
for our study of the characteristic map of a generic link.
37
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
Lemma 5.3. (Twist Lemma) Letx and y be distinct points in S3 lying in the
complement of the binding K of the standard open book.
(a) If x and y lie on diﬀerent pages, then for z∈K, the vector yz−xz
never lies on a page of the corresponding open book in R3, and in
particular never points straight up.
(b) If x and y lie on the same page, then as z traverses K, the vectors
yz−xz lie on successive pages in R3, turning once positively around
the binding, and spinning once counterclockwise without backtracking
within the pages as they go. In particular, yz−xz points straight up
for a unique z =τ(x,y )∈K.
Proof. Since the K-action carries pages to pages, x and y will lie on the same page in S3
if and only if xz andyz lie on the same page in R3 for all z∈K. Part (a) of the lemma is
now obvious. Using the meridional projection, and the description of the K-action above,
part (b) of the lemma translates into the following statement. For any pair of distinct
points x and y in the upper half-plane model of the hyperbolic plane H, the function
d(α) = arg(rot αy− rotαx)
is strictly increasing, where rot α : H→ H is hyperbolic rotation about i by α radians.
Since we wish to prove this for all x and y, it suﬃces to show that d′(0) > 0 (because
d′(α) for one choice of x and y is equal to d′(0) for some other choice of x and y).
To prove this, we transfer the problem to the Poincar´ e diskD using the conformal map
f : D −→ H , f (z) = 1−z
1 +z i
that sends 0 to i. Hyperbolic rotation of H about i by any angle is conjugate by f to
euclidean rotation of D by the same angle. Thus we must show that for any pair of distinct
points x and y in D, the function
g(α) = arg( f(eiαy)−f(eiαx))
has positive derivative at α = 0. Noting that f(a)−f(b) = 2i(b−a)/(1 +a)(1 +b) and
using the fact that the argument function converts products into sums and quotients into
diﬀerences, we ﬁnd that g(α) diﬀers by a constant from the function
h(α) = α− arg(1 +eiαx)− arg(1 +eiαy),
and so it remains to show that h′(0) > 0. But a simple geometric argument using the
central angle theorem from elementary plane geometry shows that, for any given z∈ D,
the derivative of the function arg(1 + eiαz) at α = 0 is strictly less than 1 /2. Therefore
h′(0)> 1− 1/2− 1/2 = 0 as desired. □
It follows from the twist lemma that, for any point ( s,t ) in the 2-torus that is isogonal
for our generic link L (meaning that x = x(s) and y = y(t) have the same polar angle,
and hence lie on the same page of the open book), there exists a unique u =u(s,t )∈S1
for which the vectoryz−xz points straight up, namely theu for whichz =z(u) =τ(x,y ).
It follows that the link
L = h−1
L (k) = {(s,t,u )∈T 3| (s,t )∈D and u =u(s,t )},
38
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
is the graph of the functionu(s,t ) over the collectionD of isogonal curves inT 2, as asserted
in the introduction.
We now use the twist lemma to prove part (a) of the bicycle theorem, asserting that
k is a regular value of hL. This will endow the components of L with orientations (and
thus vertical winding numbers) and framings, as deﬁned in Section 3. The proof of the
bicycle theorem will then be completed by showing that these agree with the preferred
orientations, vertical winding numbers and framings of the components of D, as deﬁned
earlier in this section.
Why is k a regular value of hL?
Suppose that hL(s,t,u ) =k. This means that the vector from xz to yz points straight
up, and so lies in some page P of the standard open book in R3. We must show that at
(s,t,u ) the vectors ∂shL, ∂thL and ∂uhL span the tangent space to S2 at k.
We are guided by Figure 26, depicting a neighborhood of the vertical vector
⇀
v fromxz
toyz in R3, lying on the page P . In this ﬁgure, Xz andYz denote the images of X andY
under the z-action, one or both of which must be transverse to P since L is generic. We
arbitrarily depict Xz tangent to P and Yz transverse to it.
yz
xz
⇀
v
Yz
Xz
∂uhL
∂thL
P
TURN
S
P
I
N
Figure 26. k is regular
The hollow arrows in the ﬁgure indicate the left-handed screw motion of the K-action.
In particular, as the u parameter increases along K, this action (the stereographic image
of right multiplication by −¯z) turns the pages in the indicated direction while spinning
them in a left-handed fashion about their centers.
As the t parameter along Y increases, the tip of
⇀
v moves to the right along Yz, so that
∂thL also points to the right, transverse to P . For clarity, we draw this partial derivative
vector at the tip of
⇀
v, even though it is really tangent to S2 at its north pole k.
As the u parameter along Z increases, two things happen which aﬀect
⇀
v. The page
containing it turns around the binding, but such an action keeps
⇀
v vertical, so has no
inﬁnitesimal eﬀect. In addition, the page spins around its center, shifting the binding in
39
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
a downward direction. Thus by the twist lemma, the vector ∂uhL is nonzero and tangent
to the page, pointing toward the binding when placed with its initial point at yz.
It follows that ∂thL and ∂uhL are linearly independent, conﬁrming that ( s,t,u ) is a
regular point of the map hL. Since (s,t,u ) was chosen arbitrarily in h−1
L (k), we see that
k is a regular value of hL, proving part (a) of the Bicycle Theorem.
Finishing the proof of the Bicycle Theorem
Starting with a three-component link L in generic position in S3, we have shown above
that the Pontryagin linkL of its characteristic map hL is given by
L = h−1
L (k) = {(s,t,u )∈T 3| (s,t )∈D and u =u(s,t )}.
It remains to prove that the preferred orientation, vertical winding numberri and framing
ni of each isogonal curveDi, as speciﬁed in Figure 19 and just before the statement of the
bicycle theorem, agree with the orientation, vertical winding number and framing of the
componentLi of the Pontryagin link that lies over Di.
To see that the orientations agree, choose a regular page vector ( x,y ) parametrized
by an isogonal point ( s,t ) in Di, and consider the orientation of Y relative to the page
containingx and y, as recorded by the sign of y.
Figure 27 shows the associated vertical vector ( xz,yz) in 3-space for the case when
sign(y) = +1, causing the displaced link component Yz to point to the right. Arguing as
above (see Figure 26) we see that ∂thL also points to the right, while ∂uhL points toward
the binding as always. Thus ∂thL and ∂uhL form a positive basis for the tangent plane
to S2 at k. Since ∂s, ∂t and ∂u form a positive basis for the tangent space to T 3 at each
of its points, it follows that the link component Li must be oriented in the direction of
increasing s near the associated point ( s,t,u ) in the 3-torus, and this agrees with the
orientation assigned toDi in Figure 19.
yz
xz
Yz
Xz
∂uhL
∂thL
Figure 27. Orientation of the Pontryagin link
Similarly, if sign(y) =−1 thenLi points in the direction of decreasings near (s,t,u ).
Referring again to Figure 19, it is evident that this agrees with the preferred orientation
onDi.
40
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
Next consider the vertical winding number ri ofDi. By deﬁnition ri is equal to the
meridional degree mi of the associated bicycle Pi, that is, the number of times that the
page vectors spin in the pages of the open book as the bicycle is traversed. By the twist
lemma, this is equal to the number of times that z spins around K, or equivalently that
u = u(s,t ) spins around the circle as ( s,t ) traverses Di, which is the vertical winding
number ofLi.
Finally consider the framing ni ofDi. By deﬁnition ni =−𝓁i−mi, where 𝓁i andmi are
the longitudinal and meridional degrees of the associated bicyclePi. This integer speciﬁes
a normal vector ﬁeld
⇀
n toLi by addingni full twists (positive or negative according to the
sign of ni) to the lift
⇀
z of a normal vector ﬁeld to Di in T 2, the “zero” or “blackboard”
framing.
We must show that the vector ﬁeld
⇀
n coincides with the Pontryagin framing of Li. In
other words, the diﬀerential of hL carries it onto a homotopically trivial loop of nonzero
tangent vectors to S2 at k. To see this, ﬁrst note that
⇀
z is homotopic to the vertical
vector ﬁeld ∂u, remaining nonzero and transverse to Li during the homotopy. Now since
∂uhL is always tangent to the page containing xz and yz, as shown above, it is clear that
each longitudinal circuit of the bicyclePi causesdhL(
⇀
z) to spin once in the same direction
about the binding. By the twist lemma, each meridional spin of the bicycle also causes
dhL(
⇀
z) to spin once about the binding. Thus dhL(
⇀
z) spins 𝓁i +mi times as the bicycle is
traversed. Adding ni =−𝓁i−mi full twists to the framing negates this spinning, and so
dhL(
⇀
n) does not spin at all, up to isotopy, as asserted.
This completes the proof of the bicycle theorem.
6. Proof of Theorem A
LetL be a three-component link in the 3-sphere with characteristic map gL :T 3→S2.
Theorem A asserts that the degrees of gL on the coordinate 2-tori of T 3 are equal to the
pairwise linking numbersp,q andr of the components ofL, and that Pontryagin’s absolute
ν-invariant ofgL is equal to twice Milnor’s triple linking number µ(L) mod 2 gcd(p,q,r ).
The ﬁrst statement was proved easily at the end of Section 4. We now prove the second
statement by an inductive argument, relying heavily on the techniques and results of the
last section. Throughout, we will use the asymmetric characteristic map hL :T 3→S2 in
place of gL, since these two maps are homotopic.
Proof of the base case of Theorem A
In Example 2.1 we introduced the “base links” Lpqr with pairwise linking numbers p,q
andr andµ(Lpqr) = 0. See Figure 3. We will show that Theorem A holds for these links.
To accomplish this, we must show that for eachp,q andr, the associated characteristic
map hLpqr is homotopic to the base map fpqr :T 3→S2 used in Section 3 to convert the
relative Pontryaginν-invariant to an absolute ν-invariant. In other words, we must show
that ν(hLpqr) = 0.
First moveLpqr by a link homotopy into generic position, and let L =X∪Y∪Z be the
resulting link. Then Z coincides with the binding K of the standard open book, while X
and Y wind around Z in a generic fashion, q and p times respectively, linking each other
41
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
r times along the way. In fact this winding can be made monotonic, to appear as shown
in Figure 28 for the case ( p,q,r ) = (5, 3,−2).
q
p
r
X
Y
Z
Figure 28. A generic link L representingLpqr
Observe that one need not actually construct a link homotopy carrying Lpqr to L, but
need only check that the pairwise and triple linking numbers of Lpqr and L coincide,
and then appeal to Milnor’s classiﬁcation. The veriﬁcation that µ(L) = 0 is completely
analogous to the calculation for µ(Lpqr), using the obvious stacked disks, joined by half
twisted bands, as Seifert surfaces forX andY , and a hemispherical page in the open book
on S3 as a Seifert surface for Z.
Now the bicycles in L are easily identiﬁed. There are d = gcd(p,q ) of them, all of
longitudinal degree 𝓁 = lcm(p,q ), and all but one of meridional degree 0, the remaining
one being of degree r. The parametrizing icycles are all parallel to a ( p/d,q/d ) torus knot
in the 2-torus, with vertical winding numbers all equal to zero, except one equal to r. By
the bicycle theorem, these icyles form a diagram for the Pontryagin link ofhL, with global
framing−(pq +r). This is exactly the situation described in Example 3.2, and so
ν(hLpqr) = ν(hL) = 0 ∈ Z2 gcd(p,q,r)
as asserted.
Proof of the inductive step of Theorem A
First recall from Example 2.2 that any three-component link L with pairwise linking
numbersp, q and r is link homotopic to a link obtained from Lpqr by a sequence of delta
moves of the type shown in Figure 4 (or its inverse), by a result of Murakami and Nakanishi
[1989]. It was shown in that example that each such move increases µ(L) by 1.
Now observe that such a delta move ∆ : L→ ˆL can be viewed as a double crossing
change D, of the kind shown in Figure 25, composed with an isotopy, as indicated in
Figure 29. By Corollary 5.2, this double crossing change increases ν(L) by 2, and so ∆
does the same.
42
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
isotopy
D
∆
L
X
Y
ˆL
ˆL
Figure 29. Another view of the delta move
Since this argument applies to an arbitrary delta move, it follows that ν(L) = 2µ(L)
for all three component links L. This completes the proof of Theorem A.
7. Sketch of an algebraic proof of Theorem A
In this section we sketch an entirely diﬀerent proof of the theorem using string links
and maps of the 2-torus to the 2-sphere. The reader is referred to our paper [2008] for
more details.
The proof is organized around the following key diagram, in which the left half, devoid
of algebraic structure, represents the topological problem we are trying to solve, while the
right half represents the algebraic structures that we impose on the left half via the two
horizontal maps in order to solve the problem.
Three-component
links in S3
up to link homotopy
 closing up Three-component
string links
up to link homotopy
Maps of T 3 to S2
up to homotopy
characteristic
maps g
?

natural map
Fundamental groups
of spaces of maps
of T 2 to S2
makes diagram
commutative
?
In the upper left corner of the diagram we have the set of link homotopy classes of
three-component links in the 3-sphere S3, and in the lower left corner the set of homotopy
43
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
classes of maps of the 3-torus T 3 to the 2-sphere S2. The vertical map g between them
assigns to the link homotopy class of L the homotopy class of its characteristic map gL.
Theorem A describes g and asserts that it is one-to-one.
A k-component string link consists of k disjoint, oriented, properly embedded arcs in
a cube, with their tails on the bottom face and their tips on the top face directly above
their tails. The product of two such string links with endpoints in a common position
is given by stacking the second one on top of the ﬁrst. When a string link moves by a
link homotopy, each strand is allowed to cross itself, while diﬀerent strands must remain
disjoint, just as for links. Then the above product induces a group structure on the set of
link homotopy classes of k-component string links.
In the upper right corner of the diagram we have the group of link homotopy classes
of three-component string links. Following Habegger and Lin [1990], an explicit presen-
tation for this group can be given in which the pairwise linking numbers and the Milnor
µ-invariant ﬁgure prominently.
The upper horizontal map denotes the operation of closing up a string link to a link. It
is easily shown that this map is onto, and that point inverse images are conjugacy classes
of string links, a special circumstance for links with three components which fails for four
or more components.
We see in the ﬁgure below that the string link on the right closes up to the Borromean
rings on the left.
closes up
Figure 30. Borromean rings as the closure of a string link
Thus the Borromean rings, a “primitive example” in the world of links, is the closure of a
string link which is itself a commutator of simpler string links.
In the lower right corner of the diagram we have the union of the fundamental groups
of the components of the space of continuous maps of the 2-torus T 2 to the 2-sphere S2,
one for each possible degree. The work of Fox [1948] on torus homotopy groups (the case
p = 0) and its generalization by Larmore and Thomas [1980] provide explicit presentations
for these groups in which the degrees on subtori and the Pontryagin ν-invariant ﬁgure
prominently.
The lower horizontal map takes the homotopy class of a based loop in the space of maps
ofT 2 toS2, ignores base points, and interprets this as a homotopy class of maps of T 3 to
S2 in the usual way. The resulting map is onto, and point inverse images are conjugacy
classes in the various fundamental groups.
44
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
Finally, the vertical map on the right side is deﬁned to make the diagram commute. We
have a group in the upper right corner, but demote it to a union of groups to match what
is below it, so that the vertical map can be regarded as a union of group homomorphisms.
Using the explicit presentations of domain and range, one can determine the eﬀects of
this map on generators, and then use the commutativity of the diagram to show that the
vertical map g on the left is precisely as described in Theorem A.
8. Proof of Theorem B, formulas (1) and (2)
Theorem B provides three formulas for Milnor’s µ-invariant of a three-component link
L in S3 whose pairwise linking numbers vanish:
(1) (diﬀerential forms) µ(L) = 1
2
∫
T 3
δ(ϕ∗ωL)∧ωL
(2) (vector ﬁelds) µ(L) = 1
2
∫
T 3×T 3
⇀
vL(x)×
⇀
vL(y)·∇yϕ (x− y) dxdy
(3) (Fourier series) µ(L) = 8 π3∑
n⁄=0
an× bn· n/|n|2
The notation is explained in the introduction.
In the subsections that follow, we obtain explicit expressions for the characteristic 2-form
ωL and vector ﬁeld
⇀
vL, and for the fundamental solution ϕ to the scalar Laplacian on T 3,
and then establish formula (1) by making use of J. H. C. Whitehead’s integral formula for
the Hopf invariant. Then, we show how to obtain formula (2) from formula (1). Finally,
in Section 9 we review the calculus of diﬀerential forms and Fourier analysis on T 3, in
order to make explicit the role and form of ϕ and obtain formula (3).
Explicit formula for the 2-form ωL and the vector ﬁeld
⇀
v L on T 3
Recall the formula for the characteristic map gL : T 3 → S2 of the link L given in
Proposition 4.1,
gL(s,t,u ) = F (x,y,z )
|F (x,y,z )|,
where x = x(s), y = y(t) and z = z(u) parametrize the components of L, and where F
was given in Section 4 as
F (x,y,z ) = ( ix·y +iy·z +iz·x , jx·y +jy·z +jz·x , kx·y +ky·z +kz·x).
Here we view x, y and z as quaternions for the multiplication and as vectors in R4 when
performing the dot product. For simplicity, we write gL =F/|F|, suppressing the appear-
ance of the evaluation map eL(s,t,u ) = (x(s),y (t),z (u)).
Again let ω be the Euclidean area 2-form on the unit 2-sphere S2⊂ R3, normalized
so that the total area is 1 instead of 4 π. If p is a point of S2, and a and b are tangent
vectors to S2 at p, then
ωp(a, b) = 1
4π (a× b)· p.
45
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
This 2-form ω on S2 extends to a closed 2-form ω in R3− 0 given by
ωp(a, b) = (a× b)·p
4π|p|3 ,
which is the pullback of ω from S2 to R3− 0 via the map p↦→ p/|p|.
Hence the pullback g∗
Lω ofω fromS2 toT 3 viagL =F/|F| is the same as the pullback
F∗ω of ω from R3− 0 to T 3 via F .
Write
g∗
Lω = F∗ω = a(s,t,u )dt∧du +b(s,t,u )du∧ds +c(s,t,u )ds∧dt.
Then we have
a(s,t,u ) = F∗ω(∂t,∂u) = ω(F∗∂t,F∗∂u)
= ω(Ft,Fu) = (Ft×Fu)·F
4π|F|3 ,
and likewise forb(s,t,u ) andc(s,t,u ), where the subscripts onF denote partial derivatives.
Therefore, the characteristic 2-form of the link L is
ωL = g∗
Lω = Ft×Fu·F
4π|F|3 dt∧du + Fu×Fs·F
4π|F|3 du∧ds + Fs×Ft·F
4π|F|3 ds∧dt,
and its corresponding characteristic vector ﬁeld is
⇀
vL = Ft×Fu·F
4π|F|3 ∂s + Fu×Fs·F
4π|F|3 ∂t + Fs×Ft·F
4π|F|3 ∂u.
Proof of Theorem B, formula (1)
Let L be a three-component link in the 3-sphere S3 with pairwise linking numbers p,
q and r all zero. By the ﬁrst part of Theorem A these numbers are the degrees of the
characteristic map gL : T 3 → S2 on the 2-dimensional coordinate subtori. Since these
degrees are all zero, gL is homotopic to a map g : T 3→S2 which collapses the 2-skeleton
of T 3 to a point:
gL ≃ g : T 3 σ−→S3 f
−→S2,
where σ is the collapsing map. By the second part of Theorem A, Milnor’s µ-invariant of
L is equal to half of Pontryagin’s ν-invariantν(gL) (comparing gL to the constant map
f000 as explained in Section 3), which in turn is just the Hopf invariant of f : S3→S2,
µ(L) = 1
2ν(gL) = 1
2 Hopf(f).
We can thus use J. H. C. Whitehead’s integral formula for the Hopf invariant as the
ﬁrst ingredient in our formula for the µ invariant. Starting from Hopf’s deﬁnition of his
invariant of a map f : S3→S2 as the linking number between the inverse images of two
regular values, Whitehead [1947] found an integral formula for Hopf( f) as follows.
Let ω be the area 2-form on S2, normalized so that
∫
S2ω = 1. Its pullback f∗ω is a
closed 2-form on S3, which is exact because H2(S3; R) = 0. Hence f∗ω = dα for some
1-formα onS3, and Whitehead showed that the Hopf invariant off is given by the formula
Hopf(f) =
∫
S3
α∧f∗ω =
∫
S3
α∧dα,
46
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
the value of the integral being independent of the choice of α.
To make Whitehead’s formula explicit requires a way to produce a 1-form α whose
diﬀerential dα is a given 2-form f∗ω on S3 which is known to be exact. We give an
explicit formula for this in the Appendix, since it is not needed in the body of the paper.
Instead, we are going to pull the whole situation back to T 3 and perform our calculations
there.
In particular, the formula
Hopf(f) =
∫
S3
α0∧f∗ω,
where α0 is any 1-form on S3 such that dα0 =f∗ω, pulls back to the formula
ν(gL) =
∫
T 3
α0∧g∗ω,
where α0 is any 1-form on T 3 such that dα0 = g∗ω. One such choice of α0 would be
α0 = σ∗α0, with α0 obtained as in the Appendix. However, since we don’t have an
explicit analytic formula forσ, and since the formula for α0 is complicated, we will pursue
a slightly diﬀerent approach.
Taking advantage of the fact that gL is homotopic to g, we also have
ν(gL) =
∫
T 3
α∧g∗
Lω =
∫
T 3
α∧ωL
for any 1-form α onT 3 such that dα =ωL. Therefore, what we really need is a canonical
way to produce a 1-form α on T 3 whose exterior derivative is the exact 2-form ωL. We
will prove in Proposition 9.2 that the 1-form
αL = δ(ϕ∗ωL)
has the desired property that dαL = ωL. Moreover, if ~α is any other 1-form such that
d~α =ωL, then|αL|≤| ~α| in L2(T 3), with equality if and only if ~α =αL.
We thus obtain the explicit integral formula for Milnor’s µ-invariant of the three com-
ponent link L:
µ(L) = 1
2ν(gL) = 1
2
∫
T 3
δ(ϕ∗ωL)∧ωL,
which is formula (1) of Theorem B.
Proof of Theorem B, formula (2)
The 1-form δ(ϕ∗ωL) onT 3 which appears in formula (1) of Theorem B converts to the
vector ﬁeld∇× (ϕ∗
⇀
vL), which can be regarded as the magnetic ﬁeld on T 3 due to the
current ﬂow
⇀
vL. The customary minus sign here is now hidden in the deﬁnitions of the
Laplacian and its inverse (Green’s operator).
The integral formula for Milnor’s µ-invariant given in formula (1),
µ(L) = 1
2
∫
T 3
δ(ϕ∗ωL)∧ωL,
47
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
then converts to the formula
µ(L) = 1
2
∫
T 3
(
∇× (ϕ∗
⇀
vL)
)
·
⇀
vLd vol
in the language of vector ﬁelds. To obtain formula (2) of Theorem B, we ﬁrst expand out
the convolution integral
(ϕ∗
⇀
vL)(x) =
∫
T 3
⇀
vL(y)ϕ(x− y)dy.
Then we compute its curl:
(
∇x× (ϕ∗
⇀
vL)
)
(x) =
∫
T 3
∇x×
(⇀
vL(y)ϕ(x− y)
)
dy
= −
∫
T 3
⇀
vL(y)×∇ xϕ(x− y)dy,
using the product formula ∇× (f
⇀
a) = f(∇×
⇀
a)−
⇀
a×∇f. Note that ∇x×
⇀
vL(y) = 0
since, from the point of view of the variable x, the vector ﬁeld
⇀
vL(y) is constant.
Inserting the expression for the curl of ϕ∗
⇀
vL into the formula for µ(L), we get
µ(L) = −1
2
∫
T 3×T 3
(⇀
vL(y)×∇ xϕ(x− y)
)
·
⇀
vL(x)dxdy
= −1
2
∫
T 3×T 3
⇀
vL(x)×
⇀
vL(y)·∇xϕ(x− y)dxdy
= 1
2
∫
T 3×T 3
⇀
vL(x)×
⇀
vL(y)·∇yϕ(x− y)dxdy,
where at the last step we hid the minus sign by taking the gradient of ϕ with respect to
y instead of x, and obtained formula (2) of Theorem B.
9. Fourier series and the Proof of Theorem B, formula (3)
Fourier series and the fundamental solution of the Laplacian
In the proofs of formulas (1) and (2) of Theorem B, we needed to ﬁnd a 1-form α on
T 3 whose exterior derivative is the exact 2-form ωL associated with the three-component
link L in S3. We asserted that we can choose α =δ(ϕ∗ωL), where ϕ is the fundamental
solution of the scalar Laplacian on T 3. Furthermore, we asserted that this choice of α is
canonical in the sense that it has the smallest L2 norm among all possible choices. We
justify these assertions in this section and lay the groundwork for the proof of formula (3)
of Theorem B by studying the calculus of diﬀerential forms on T 3 = (R/2πZ)3 in terms
of their Fourier series.
We will prove the following two results:
Proposition 9.1. The fundamental solution of the scalar Laplacian on the
3-torus T 3 = (R/2πZ)3 is given by the formula
ϕ(x) = 1
8π3
∑
n⁄=0
ein·x/|n|2.
The function ϕ is C∞ at all points x∈T 3 except 0, where it becomes inﬁnite.
48
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
Proposition 9.2. Ifω is any exact diﬀerential form on T 3 withC∞ coeﬃcients,
then
α = δ(ϕ∗ω)
is a C∞ diﬀerential form satisfying dα =ω. Furthermore, if d~α =ω as well,
then|α|L2≤| ~α|L2, with equality if and only if ~α =α.
Before diving into calculations, we pause for some words of explanation: We write
Ωk(T 3) for the space of C∞ k-forms onT 3. With d as the exterior diﬀerentiation operator
taking Ωk(T 3) to Ωk+1(T 3), and δ the co-diﬀerentiation map adjoint to d in the L2 sense,
the Laplacian of a k-form α is
∆α = ( dδ +δd)α.
This deﬁnition gives us the “geometer’s sign convention” for the Laplacian on functions
(0-forms):
∆f = −
(∂2f
∂x2
1
+ ∂2f
∂x2
2
+ ∂2f
∂x2
3
)
.
Proof of Proposition 9.1
The fundamental solution of the scalar Laplacian is a functionϕ, convolution with which
“inverts” the Laplacian to the extent that this is possible. On T 3, only functions that
integrate to zero are in the range of the Laplacian, and so “the” fundamental solution of
∆ on T 3 is the function ϕ which satisﬁes
∫
T 3
ϕd vol = 0 and ∆( ϕ∗f) = f
for all f∈C∞(T 3) such that
∫
T 3
fd vol = 0.
Even though we have expressed ϕ in terms of complex exponentials, the value of ϕ is
real for real values of x because of the symmetry of the coeﬃcients.
Figure 31 shows the graph of the corresponding fundamental solution
ϕ(x) = 1
4π2
∑
n⁄=0
ein·x/|n|2
of the scalar Laplacian on the 2-torus S1×S1, summed for |n|≤ 10, and displayed over
the range [−3π, 3π]× [−3π, 3π].
With respect to the L2 inner product
⟨f,g⟩ =
∫
T 3
f(x)g(x)dx,
the set of complex exponentials {ein·x| n∈ Z3} is an orthogonal set, and for all n, we
have⟨ein·x,ein·x⟩ = 8π3.
Any function f in L2(T 3) can be expanded into a Fourier series
f ∼
∑
n∈Z3
cnein·x
49
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
 
 
 
Figure 31. Fundamental solution of the scalar Laplacian on S1×S1
where
cn = 1
8π3⟨f,ein·x⟩ = 1
8π3
∫
T 3
f(x)e−in·xdx.
Moreover, by Plancharel’s theorem, the L2(T 3)-norm of f is equal to the 𝓁2-norm of the
sequence of coeﬃcients:
|f|L2 =
∫
T 3
|f(x)|2dx =
∑
n∈Z3
8π3|cn|2.
This shows that the function ϕ of Proposition 9.1 is in L2(T 3), since |cn|2 is of order
1/|n|4, while the number of lattice points at distance |n| from 0 is of order|n|2.
Because the range of the scalar Laplacian is the (closed) subspace of functions f for
which ∫
T 3
f(x)dx = 0 ,
we will denote this subspace of L2(T 3) byL2
0(T 3), and similarly for other function spaces,
where a zero subscript will indicate that all functions in the space have average value
zero. In terms of Fourier coeﬃcients, f ∈ L2
0(T 3) if and only if the Fourier coeﬃcient
c0 =c(0,0,0) = 0.
For functionsf and g in C∞(T 3), their convolutionf∗g is deﬁned by
(
f∗g
)
(x) =
∫
T 3
f(y)g(x− y)dy,
50
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
and also lies in C∞(T 3). One checks easily that eim·x∗ein·x = 0 if m⁄= n, and
ein·x∗ein·x = 8 π3ein·x.
Therefore, if f and g have Fourier series∑cnein·x and∑dnein·x respectively, then the
Fourier series of f∗g is
8π3 ∑
n∈Z3
cndnein·x.
From this it follows that the operation of convolution satisﬁesf∗g =g∗f and (f∗g)∗h =
f∗ (g∗h) whenever all the convolutions are deﬁned. Furthermore,
∂
∂xk
(f∗g) = ∂f
∂xk
∗g = f∗ ∂g
∂xk
.
Foru∈C∞(T 3), with
u(x) =
∑
n∈Z3
bnein·x,
we have
∆u(x) =
∑
n⁄=0
|n|2bnein·x.
Because the (0, 0, 0)-coeﬃcient of ∆u is zero, this shows why in order to solve ∆u =f we
must restrict f to be in C∞
0 (T 3). And for f∈C∞
0 (T 3), with
f(x) =
∑
n⁄=0
cnein·x,
the unique solution u∈C∞
0 (T 3) of ∆u =f has bn =cn/|n|2, and so, since
ϕ(x) = 1
8π3
∑
n⁄=0
ein·x/|n|2,
we conclude that u = ϕ∗f. This completes the proof of Proposition 9.1 except for the
assertion about the smoothness of ϕ away from its singularity, which follows from well-
known local regularity theorems for elliptic partial diﬀerential equations (see, for example,
Folland [1995], Theorem 6.33).
Fourier series and the calculus of diﬀerential forms on the 3-torus
To prove Proposition 9.2, we express the calculus of diﬀerential forms on T 3 in terms
of Fourier series. Except for the fundamental solution ϕ of the (scalar) Laplacian on T 3,
we will assume all functions and forms are C∞.
We continue to express functions (0-forms) as Fourier series: for x = (s,t,u ) and
n = (n1,n 2,n 3), we write
f(x) =
∑
n∈Z3
cnein·x ∈ Ω0(T 3).
Likewise, we employ the notation described in the introduction and express 1-forms using
cn = (cs
n,ct
n,cu
n) and dx = (ds,dt,du ). We write
α(x) =
∑
n∈Z3
cnein·x
·dx ∈ Ω1(T 3).
51
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
With ⋆dx = (dt∧du,du∧ds,ds∧dt) as before, we can express a 2-form as
β(x) =
∑
n∈Z3
cnein·x
·⋆d x ∈ Ω2(T 3).
Finally, withdV =ds∧dt∧du, a 3-form can be written as
γ(x) =
∑
n∈Z3
cnein·xdV ∈ Ω3(T 3).
It is straightforward to express both the exterior derivative d and the codiﬀerential δ in
terms of Fourier coeﬃcients. With f, α, β and γ as above, we have
df =
∑
icnnein·x
·dx and δf = 0 ,
dα =
∑
in× cnein·x
·⋆d x and δα = −
∑
in·cnein·x,
dβ =
∑
in·cnein·xdV and δβ =
∑
in× cnein·x
·dx,
dγ = 0 and δγ = −
∑
icnnein·x
·⋆d x.
Thus, exterior diﬀerentiation and co-diﬀerentiation are expressed in terms of vector al-
gebraic operations on the Fourier coeﬃcients. From these expressions, we conclude the
following about the kernel and image of d and δ:
• For 0-forms,
kerd = {f| cn = 0 for n⁄= 0, while c0 is arbitrary}
imd = {0}
kerδ = {all f}
imδ = {f| c0 = 0}
• For 1-forms,
kerd = {α| cn =λnn for n⁄= 0, while c0 is arbitrary}
imd = {α| cn =λnn for n⁄= 0, c0 = 0}
kerδ = {α| cn·n = 0 for n⁄= 0, while c0 is arbitrary}
imδ = {α| cn·n = 0 for n⁄= 0, c0 = 0}
• For 2-forms,
kerd = {β| cn·n = 0 for n⁄= 0, while c0 is arbitrary}
imd = {β| cn·n = 0 for n⁄= 0, c0 = 0}
kerδ = {β| cn =λnn for n⁄= 0, while c0 is arbitrary}
imδ = {β| cn =λnn for n⁄= 0, c0 = 0}
52
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
• For 3-forms,
kerd = {all γ}
imd = {γ| c0 = 0}
kerδ = {γ| cn = 0 for n⁄= 0, while c0 is arbitrary}
imδ = {0}
Therefore imd⊂ kerd and imδ⊂ kerδ, and the following orthogonal (with respect to
the L2 inner product) decompositions hold:
Ωk(T 3) = ker δ⊕ imd = im δ⊕ kerd
for k = 0,..., 3. The k-forms in ker d∩ kerδ are the forms whose Fourier series contain
only constant terms. These are called harmonic k-forms because they are in the kernel of
the Laplacian ∆ = dδ +δd, so we write Hark(T 3) = kerd∩ kerδ. We then have the Hodge
decomposition
Ωk(T 3) = im δ⊕ Hark(T 3)⊕ imd.
The Laplacian ∆: Ω k(T 3)→ Ωk(T 3) preserves this Hodge decomposition, taking im δ
bijectively to itself, killing Hark(T 3), and taking im d bijectively to itself.
Proof of Proposition 9.2
We must show that ifω is anyC∞ exact diﬀerentialk-form onT 3, then the (k−1)-form
α =δ(ϕ∗ω) is C∞ and satisﬁes dα =ω, and that if d~α =ω as well, then|α|L2≤|~α|L2,
with equality if and only if ~α =α.
Because it is the case we use in Theorem B, we will carry this out speciﬁcally for 2-forms.
The proofs for 1-forms and 3-forms are essentially the same.
For a 2-form
β =
∑
n∈Z3
cnein·x
·⋆d x,
its Laplacian is given by
∆β =
∑
n⁄=0
|n|2cnein·x
·⋆d x.
We can use convolution with the fundamental solutionϕ of the scalar Laplacian to express
the Green’s operator,
Gr(β) = ϕ∗β =
∑
n⁄=0
cn
|n|2ein·x
·⋆d x.
Clearly the Laplacian ∆ and the Green’s operator are inverses of one another when applied
to 2-forms β with c0 = 0, equivalently, to 2-forms β orthogonal to Har 2(T 3).
To prove Proposition 9.2, assume that β is exact, that is, β∈ imd. Then Gr(β) is also
exact, hence certainly closed, and therefore
β = ∆ Gr(β) = ( dδ +δd) Gr(β) = dδ Gr(β) = dδ(ϕ∗β).
Thusα =δ(ϕ∗β) satisﬁes dα =β.
53
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
If~α is any other 2-form satisfying d~α =β, then ~α diﬀers fromα by some closed 2-form,
which must beL2-orthogonal toα sinceα∈ imδ. Thus,|α|L2≤|~α|L2 by the Pythagorean
theorem.
Since the Fourier coeﬃcients of a C∞ 2-form decrease faster than any negative power
of|n|, we have that Gr( β) and δ Gr(β) will be C∞ if β is. This completes the proof of
Proposition 9.2.
Proof of Theorem B, formula (3)
This formula expresses Milnor’s invariant µ(L) in terms of the Fourier coeﬃcients of
ωL:
µ(L) = 8 π3∑
n⁄=0
an× bn· n
|n|2
where
ωL =
∑
n⁄=0
cnein·x· ⋆d x
with cn = an +ibn and with an and bn real.
The formula for ωL is summed over n⁄= 0 because the hypothesis of pairwise linking
numbers zero is equivalent to the vanishing of the harmonic component of ωL, which in
turn is equivalent to the vanishing of its Fourier coeﬃcient c0.
We begin with formula (1) of Theorem B for µ(L):
µ(L) = 1
2
∫
T 3
δ(ϕ∗ωL)∧ωL.
We have
ϕ∗ωL =
∑
n⁄=0
cnein·x
|n|2 · ⋆d x,
and hence, from our table of derivatives and co-derivatives in terms of Fourier series,
δ(ϕ∗ωL) =
∑
n⁄=0
(n× cn)iein·x
|n|2 ·dx.
To compute δ(ϕ∗ωL)∧ωL, we use the fact that if v·dx is a 1-form and w·⋆dx is a
2-form, then
(v·dx)∧ (w·⋆dx) = ( v· w)dV.
Thus
δ(ϕ∗ωL)∧ωL =
∑
m⁄=0
∑
n⁄=0
(n× cn)· cmiei(m+n)·x
|n|2 dV.
When we insert this double sum into the integral µ(L) = 1
2
∫
T 3δ(ϕ∗ωL)∧ωL, most of the
terms in the summation will integrate to zero, leaving only the terms where m + n = 0.
In those cases, ei(m+n)·x =e0 = 1 integrates to 8π3, the volume of T 3.
54
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
Thus
µ(L) = 4 π3∑
n⁄=0
i(n× cn)· c−n
|n|2
= 4 π3∑
n⁄=0
i(cn× c−n)· n
|n|2
and it remains to simplify this last series.
Since cn = an +ibn and since ωL is real-valued, we have c−n = cn = an−ibn. Hence
cn× c−n = ( an +ibn)× (an−ibn) = −2i an× bn,
and therefore
µ(L) = 4 π3∑
n⁄=0
i(cn× c−n)· n
|n|2
= 8 π3∑
n⁄=0
(an× bn)· n
|n|2 ,
completing the proof of formula (3) and, with it, that of Theorem B.
Numerical computation
We used Maple and Matlab to calculate an approximation to Milnor’s µ-invariant for
the three-component link L in S3 given by
x(s) = [ 4
5 sins, coss, 3
5 sins, 0],
y(t) = [ 4
5 sint, 0, cost, 3
5 sint],
z(u) = [ 4
5 sinu, 3
5 sinu, 0, cosu],
fors∈ [0, 2π],t∈ [0, 2π] and u∈ [0, 2π], which is a concrete realization of the Borromean
rings with µ =−1.
Figure 32. Borromean rings
Maple gave the (long, ugly) formula for ωL obtained from Proposition 4.1, and we used
Matlab to calculate approximations to its Fourier coeﬃcients cn for divisions of the s, t
and u intervals into 60 subintervals and for n∈ [−15, 15]3. The approximation of µ we
obtained in this way was−0.97.
55
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
Appendix. Whitehead’s integral formula for the Hopf invariant
We take this opportunity to make J. H. C. Whitehead’s integral formula for the Hopf
invariant of a map f : S3→S2 explicit, and have relegated it to an appendix because we
do not use the result in this paper.
Recall from Section 8 Whitehead’s formula,
Hopf(f) =
∫
S3
α∧ωf,
where ωf =f∗ω is the pullback to S3 of the normalized area form ω on S2, and α is any
1-form on S3 such thatdα =ωf. To make this formula explicit requires a way to produce
such an α.
To do this, we ﬁrst write Whitehead’s formula in the language of vector ﬁelds,
Hopf(f) =
∫
S3
⇀
a·
⇀
vf d vol,
where the 2-form ωf on S3 has been converted to the vector ﬁeld
⇀
vf in the usual way,
and where
⇀
a is any vector ﬁeld on S3 such that∇×
⇀
a =
⇀
vf.
An explicit recipe for
⇀
a was given by DeTurck and Gluck [2008a]:
⇀
a(y) = BS(
⇀
vf)(y) =
∫
S3
Pyx
⇀
vf(x)×∇ yϕ(x, y)dx.
Here BS is the Biot–Savart operator for vector ﬁelds on the 3-sphere. In the last integral,
Pyx indicates parallel transport in S3 along the geodesic segment from x to y, and the
function ϕ is given by
ϕ(α) = − 1
4π2 (π−α) cscα,
and ϕ(x, y) is an abbreviation for ϕ(α(x, y)), with α(x, y) the geodesic distance on S3
between x and y.
The signiﬁcance of the above function ϕ is that it is the fundamental solution of a
shifted Laplacian on S3:
−∆ϕ−ϕ =δ,
where δ is the Dirac delta function.
The above formula for BS(
⇀
vf) is the analogue onS3 of the classical Biot–Savart formula
from electrodynamics in R3, expressing the magnetic ﬁeld BS(
⇀
vf) in terms of the current
ﬂow
⇀
vf. The equation ∇× BS(
⇀
vf) =
⇀
vf is just one of Maxwell’s equations, transplanted
to S3.
Inserting this formula for BS(
⇀
v) into the previous formula for the Hopf invariant and
performing simple manipulations, we get
Hopf(f) = −
∫
S3×S3
Pyx
⇀
vf(x)×
⇀
vf(y)·∇yϕ(x, y)dxdy,
the explicit version of Whitehead’s integral formula on the 3-sphere S3.
56
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
