---
doc_id: s40879-023-00706-0
doc_title: "Bring's curve: old and new"
section_id: sec-002-21-basic-properties
section_title: "Basic properties"
section_number: 2.1
pages: 3-11
source_pdf: s40879-023-00706-0.pdf
source_sha256: 4c5af312d2e5d6a7
doc_brief: "Bring's curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
---
period matrix and its automorphisms. We begin with two descriptions: one as a model
in P4 and the second as a plane curve. In particular we shall construct the birational
map between these models, which we believe new. Such a map enables us to concretely
translate calculations from one model to another and will be helpful later in Sect. 4
when we look at quotients of the curve.
Deﬁnition 2.1 Bring’s curveB is deﬁned in P
4 by the (homogeneous) equations 1
Hk ..=
5∑
i=1
xk
i = 0, k = 1, 2, 3, (1)
where we have taken the coordinates [x1 : x2 : x3 : x4 : x5]∈ P4.
We will call (1)t h eP4-model of Bring’s curve. Historically, this curve was attributed
to Bring by Klein in his lectures on the icosahedron [ 42]. Bring’s improvement on the
Tschirnhaus transformation enabled the general quintic to be brought to the Bring–
Jerrard form x5 + ex + f = 0[ 1]: if xi , i = 1,..., 5, are the roots of this equation
then the symmetric sums∑
i xk
i = 0f o rk = 1, 2, 3, and so the above curve emerges.
Green [30] exploits this relation to Bring’s curve to (implicitly) solve the quintic using
automorphic forms. At this stage we may observe that S5 ⩽ Aut(B).
Remark 2.2 In the above deﬁnition we have implicitly taken P4 = CP4, and indeed
this will be our deﬁnition throughout. At various junctures we will however highlight
the number ﬁelds within C that are relevant ﬁelds of deﬁnition for morphisms of the
curve, or geometrically important points on the curve.
For many calculations a plane model of a curve in P
2 is useful. One of the main
tools we will utilise in this paper is the Riemann surfaces module of SageMath [ 64]
which requires such a model. As such we introduce the following.
Deﬁnition 2.3 The Hulek–Craig (HC) model of Bring’s curve is the (singular) plane
curve in P2 given by
F(X, Y, Z) ..= X(Y 5+ Z 5) + (XYZ )2 − X 4YZ − 2(YZ )3 = 0, (2)
taking homogeneous coordinates [X : Y : Z]∈ P2. We denote its normalisation by B.
This model was used in [ 15, 39] where they studied the curves modular properties.
Indeed Craig gives a parameterization of the curve in terms of modular functions
following work of Ramanujan. Craig does not identify the curve as Bring’s, whereas
Hulek ﬁnds the equation as a hyperplane section of a surface that parameterises elliptic
normal curves of degree 5, and then refers to previous results to connect it with Bring.
This connection was ﬁrst made in [ 52], where the curve is attributed to Klein. Indeed,
1 Note here we use the notation Hk of [11] for the symmetric sum, whereas [ 24]u s e sSk .
123
3 Page 4 of 46 H.W. Braden, L. Disney-Hogg
because of this interpretation, one can write down Bring’s curve in the form of a
quotient of the upper half plane H as
H//Gamma10(2, 5) where /Gamma10(2, 5) = /Gamma10(2) ∩ /Gamma1(5) =
⎧
⎪⎨
⎪⎩
(
ab
cd
)
∈ SL2(Z)
⏐⏐⏐
⏐
a ≡ d ≡ 1 (mod 5)
b ≡ 0 (mod 5)
c ≡ 0 (mod 10)
⎫
⎪⎬
⎪⎭
.To our knowledge, [39] is the ﬁrst occurrence of this plane model of the curve; Klein
will write it down in [ 42, pp. 165, 242] but the relation to a plane model of Bring’s
curve is not made explicit. We will call ( 2) the HC-model of Bring’s curve. In the
following subsection we shall show the birational equivalence of ( 2) and ( 1).
Another plane model of Bring’s curve is given by (x − 1) y5 − (x + 1) x2 = 0,
introduced in [ 66, Proposition 3.1] by considering the curve as a cyclic cover of P1,
see Sect. 4.
2.1 Basic properties
Towards proving the birational equivalence of the two models given for Bring’s curve
we begin with some basic properties of the curve. We introduce afﬁne coordinates
(x, y) = (X/Z, Y/Z) such that the HC-model is 0 = f (x, y) = F(x, y, 1).
2 Then
Resy( f (x, y), ∂y f (x, y)) = x4(x5 − 1)2(256x10 − 837x5 + 3456). Investigation of
the vanishing of this resultant leads to the following.
Lemma 2.4 ([8]) The only singular points in the HC-model of the curve are V k =
[ζ k : ζ 2k : 1] for k = 0,..., 4, where ζ = exp(2πi/5), and V5 =[ 1: 0 : 0].
We shall return these points in due course; each of these singular points desingu-
larizes to two points. We also have non-singular points a =[ 0 : 0 : 1], b =[ 0 : 1: 0],
about which we can take a local parameter t (that is a parameter 0 at the points)
such that nearby points behave as [2t3 : t : 1] and [2t3 : 1: t] respectively. The point V5
desingularises to two points on B, which we denote
c =[ 1: 0 : 0]2, d =[ 1: 0 : 0]1,
which in the vicinity of these points have local behaviour [1: t : t4] and [1: t4 : t]
respectively. We see from this that
Corollary 2.5
div(x) = 3a + 2b − 4c − d, div(y) = a − b − 3c + 3d,
RF = 2a + b + 3c +
∑
i
ri,
where R F is the ramiﬁcation divisor corresponding to the map x : B → P1 and the
ri are the roots of the polynomial256x10 − 837x5 + 3456 appearing in the resultant.
2 Note the coordinates x, y will also interchangeably be used as coordinates on the normalisation away
from the preimages of singular points.
123
Bring’s curve: old and new Page 5 of 46 3
Lemma 2.6 ([8]) The genus of Bring’s curve is g = 4 and we have the ordered basis
of (unnormalised) differentials on B
v1 = (y3 − x) dx
∂y f (x, y) ,v 2 = (y2x − 1) dx
∂y f (x, y) ,
v3 = (y − x2) dx
∂y f (x, y) ,v 4 = y(x2 − y) dx
∂y f (x, y) .
Remark 2.7 Note that because a singular curve and its normalisation have the same
geometric genus, we still expect to have four independent differentials in the HC-
model.
These differentials, while independent as holomorphic differentials, do satisfy an
algebraic relation, namely
Q: v1v2 + v3v4 = 0. (3)
It is a famous result that Q ∼= P1× P1 [65], and as we will subsequently want an
explicit form of the isomorphism we shall write it down. Namely we have the map
Q → P
1× P1 given by ϕ: P1× P1 → Q ⊂ P3,
ϕ([u : v],[z : w]) =[ uz : vw :vz :− uw] ..=[ v1 : v2 : v3 : v4]. (4)
The inverse map ϕ−1 : Q → P1× P1 is given by
ϕ−1([v1 : v2 : v3 : v4]) =
⎧
⎪⎪
⎪⎨
⎪⎪
⎪
⎩
([v
1 : v3],[v3 : v2]), {v1,v 3} ⁄={ 0} ⁄={ v2,v 3},
([− v4 : v2],[v3 : v2]), {v1,v 3}={ 0} ⁄={ v2,v 3},
([v1 : v3],[v1 :− v4]), {v1,v 3} ⁄={ 0}={ v2,v 3},
([− v4 : v2],[v1 :− v4]), {v1,v 3}={ 0}={ v2,v 3}.
Proposition 2.8 ([8]) The canonical divisor class on Bring’s curve B is [KB]=
[a + 2b + 3c].
Proof This may be shown analytically or (as given in the accompanying note-
book) entirely using computer algebra. To show this analytically we use div (dx ) =
− 2(4c + d) + RF .
We now establish the main result of this subsection.
Proposition 2.9 The HC-model (2) is a model of Bring’s curve(1).
Proof We will prove this by explicitly constructing the birational transform. To do so
we make use of the proof of [ 22, Theorem 3], where the author considers a particular
Clebsch hexagon, 3 constructs a pencil of plane sextics from this, and ﬁnds Bring’s
3 For the purposes of this deﬁnition a hexagon is a set of six points in P2 no three of which are collinear,
called the vertices. A Brianchon point of a hexagon is a non-vertex point through which three edges (the
lines joining two distinct vertices) pass. A Clebsch hexagon is a hexagon with ten Brianchon points [ 21].
123
3 Page 6 of 46 H.W. Braden, L. Disney-Hogg
curve as the canonical model of a distinguished point in this pencil. By assuming that
the HC-model is already the distinguished curve in a pencil, we can construct the
birational map. Note this is a fundamentally different approach to the that originally
taken with the HC-model, which was derived from considerations of the modular
theory of the curve.
Explicitly, Dye introduces j as a solution to j
2 − j − 1 = 0 and then deﬁnes the
pencil of curves4 Sλ = S + λ|C|3 where
S(x, y, z) = (x + jy )6 + (x − jy )6
+(y + jz)6 + (y − jz)6 + (z + jx )6 + (z − jx )6,
C(x, y, z) = x2 + y2 + z2. (5)
Next Dye considers the Clebsch hexagon H with vertices
(1,± j, 0), ( 0, 1,± j), ( ± j, 0, 1),
for which the corresponding ten Brianchon points are at
(± j2, 1, 0), ( 0,± j2, 1), ( 1, 0,± j2), ( 1,±1,±1).
Dye shows that there is a unique member of the pencil, which he calls /Gamma1, that contains
the vertices. Moreover, /Gamma1has the vertices and only the vertices as double points.
To get a canonical model 5 for /Gamma1, which Dye shows has genus 4, we now need
a little theory from [ 56, pp. 122–124], namely that a generic cubic surface in P3 is
birational to the vanishing condition for a system of plane cubics through six base
points in generic positions. We apply this taking these six points to be the vertices of
the hexagon H . We shall see a posteriori that these are indeed in general position.
We shall now proceed as follows.
(i) We will explicitly give the correspondence between a (generic) cubic in P
3 and
the vanishing condition for the system of cubics.
(ii) We construct the cubic which corresponds to the vanishing condition for the
cubics through the six points Vk on the HC-model.
(iii) We verify that the constructed map is birational from P2 to the cubic.
(iv) Motivated by the geometry of Bring’s curve, we ﬁnd a collineation which maps
the found cubic to the standard Clebsch surface (deﬁned below) in P4.
(v) We verify that restricting to the HC-model in P2 corresponds to restricting to
Bring’s curve in the Clebsch surface.
(vi) We give examples of this new birational map from the (normalisation) of the
HC-model to Bring’s on some particular points. We do this now.
4 We are using the coordinates [x : y : z] here, distinct from [X : Y : Z], to highlight that these are not those
of the HC-model.
5 We use the phrase “canonical model of /Gamma1" to mimic the language used by Dye. For a singular curve, the
canonical model is the canonical model as naturally deﬁned for the normalisation of the curve.
123
Bring’s curve: old and new Page 7 of 46 3
(i) Such a generic cubic surface F ⊂ P3 can be written as the vanishing of a determi-
nant
⏐⏐⏐⏐
⏐
⏐
u
1 v1 w1
u2 v2 w2
u3 v3 w3
⏐⏐⏐⏐
⏐
⏐
= 0,
where u
1,...,w 3 are linear homogeneous functions of the P3 coordinates, that is to
say P =[ L1 : L2 : L3 : L4]∈ F ⊂ P3 if and only if there exists P′=[ X : Y : Z]∈ P2
such that
Xu i(P) + Yvi(P) + Zwi(P) = 0.
Thinking of P′as a point in a plane /Pi1we get a birational transformation /Pi1↔ F,
P′↔ P.T h em a p/Psi1: /Pi1→ F will have the La as homogeneous cubics in X, Y, Z .
To see this rewrite the determinant equation as (for i = 1, 2, 3)
4∑
a=1
aia (P′)La = 0
for some aia linear homogeneous in the X, Y, Z . On each afﬁne patch La ⁄= 0 solving
this involves inverting a 3× 3 matrix whose entries are linear homogeneous polynomi-
als in X, Y, Z . Likewise, given the La , we have a 3-parameter family of cubics given
by
aL 1 + bL 2 + cL 3 + dL 4 = 0f o r [a : b : c : d]∈ P3.
A cubic in P2 has ten projective coefﬁcients, and so a 3-parameter family is deﬁned
by six constraints. Generically we can take those constraints to come in the form of
intersection with six generic points Oi ∈ /Pi1.
(ii) For our purposes, the six points we want to intersect with are the vertices of the
Clebsch hexagon, which are the double points of the exceptional curve /Gamma1. Assuming
the the HC-model gives such an exceptional curve, we take the points Vk identiﬁed in
Lemma 2.4. Hence, if we write a generic cubic in X, Y, Z as
a0 X 3 + a1 X 2Y + a2 X 2 Z + a3 XY 2
+ a4 XYZ + a5 XZ 2 + a6Y 3 + a7Y 2 Z + a8YZ 2 + a9 Z 3
the equations on the coefﬁcients we get (coming from intersecting with Vk , k =
0,..., 4, and V5 respectively) are
a0ζ 3k + a1ζ 4k + a2ζ 2k + a3 + a4ζ 3k + a5ζ k + a6ζ k + a7ζ 4k + a8ζ 2k + a9 = 0,
a0 = 0.
123
3 Page 8 of 46 H.W. Braden, L. Disney-Hogg
Setting the coefﬁcients of ζ nk to be zero gives us the 3-parameter family of cubics
0 = aX 2Y + bX 2 Z + cXY 2 + dXZ 2 − dY 3 − aY 2 Z − bY Z2 − cZ 3
..= aL 1 + bL 2 + cL 3 + dL 4.
Precisely because the resulting family of cubics is 3-parameter, we know that the six
points from H must have been sufﬁciently general.
Comparing the coefﬁcients we see that our map intoP3 is (essentially) the canonical
embedding
[v1 : v2 : v3 : v4]=[ − L4 : L3 :− L2 : L1].
One can check, using for example Gröbner bases, that the La satisfy the equation
L2 L2
4 − L2
1 L4 − L1 L2
3 + L2
2 L3 = 0.
This is the cubic we call F.
(iii) One can use the package Cremona [61] in Macaulay2 to check that the map /Psi1
is birational. Note one needs to make sure that the range is chosen such that the map
is explicitly surjective, not just use the implicit knowledge that the map is surjective
onto its image. Doing so and asking for the inverse map gives
[X : Y : Z]=[ L2
2 − L1 L3 : L1 L4 : L2 L4].
For example, we can see
L2
2 − L1 L3
L1 L4
= (X 2 Z − YZ 2)2 − (X 2Y − Y 2 Z)(XY 2 − Z 3)
(X 2Y − Y 2 Z)(XZ 2 − Y 3)
= X 4 Z 2 − X 2YZ 3 − X 3Y 3 + XY 4 Z
X 3YZ 2 − XY 2 Z 3 − X 2Y 4 + Y 5 Z = X
Y ,
and
L1 L4
L2 L4
= L1
L2
= X 2Y − Y 2 Z
X 2 Z − YZ 2 = (X 2 Z − YZ 2)(Y/Z)
X 2 Z − YZ 2 = Y
Z .
(iv) We now have a cubic surface in P3 corresponding to the system of curves inter-
secting the Vi .F r o m[37, pp. 198–201] we know there exists a coordinate system in
which this cubic can be written as the subset of P4
123
Bring’s curve: old and new Page 9 of 46 3
H3 = 0 = H1
(this is called ‘the’ Clebsch surface). To look for such a coordinate system, we write
this surface in P3 as
0 = x2
1 x2 + x1x2
2 + x2
1 x3 + x2
2 x3 + x1x2
3
+ x2x2
3 + x2
1 x4 + x2
2 x4 + x2
3 x4 + x1x2
4 + x2x2
4
+ x3x2
4 + 2x1x2x3 + 2x1x2x4 + 2x1x3x4 + 2x2x3x4.
From here, one can use the fact that the ten Eckardt points6 of the cubic in La form the
ten vertices of a pentahedron [ 37], and that in the coordinate system of the Clebsch
surface in P4 these lie at the permutations of [1:− 1: 0 : 0 : 0] [24]. This gives us a
possible way a spotting the transform if we can calculate the Eckardt points of F.T o
do this, we use the identiﬁcation from [22], that the three lines in F intersecting to give
an Eckardt point come from the three edges of H intersecting at a Brianchon point.
To this end we ﬁnd the images of the Vi Vj for which we give a generating set of the
ideal corresponding to the line, for example
(a) /Psi1(V0V5):⟨ L4 − L3, L2 − L1⟩,
(b) /Psi1(V1V2):⟨ L4 + (ζ 2 + ζ + 1) L2 + (ζ 4 − ζ 2 − ζ) L1, L3 + (ζ 3 + 2ζ 2 + ζ) L2
+ (ζ 3 + ζ 2 + ζ) L1⟩,
(c) /Psi1(V3V4):⟨ L4 + (−ζ 2 − ζ) L2 + (ζ 3 + 2ζ 2 + ζ) L1, L3 + (ζ 3 − ζ − 1) L2
+ (ζ 2 + ζ + 1) L1⟩.
Then
/Psi1(V0V5) ∩ /Psi1(V1V2) ∩ /Psi1(V3V4) =
[
− ζ 3 − ζ 2 − 1 :− ζ 3 − ζ 2 − 1 : 1 : 1
]
= /Psi1(V0V5 ∩ V1V2 ∩ V3V4).
One can do likewise to ﬁnd the other Eckardt points.
Armed now with the knowledge of the Eckardt points, we can ﬁnd appropriate
projective transforms A that biject the sets of Eckardt points by acting
(x1, x2, x3, x4)T = A(L1, L2, L3, L4)T,
for example,
A =
⎛
⎜⎜⎝
ζ 3 −1 −ζ 2 ζ
1 −ζ 3 −ζζ 2
ζ 2 −ζ −1 ζ 3
ζ −ζ 2 −ζ 3 1
⎞
⎟⎟⎠ .
We can then use again Macaulay2 to check that this transform then gives us the correct
cubic in P3.
6 An Eckardt point of a surface is a point where three lines contained within the surface intersect [ 37].
123
3 Page 10 of 46 H.W. Braden, L. Disney-Hogg
(v) Moreover, if we now restrict to the HC-model in the system of curves that intersect
the Vi , that is we impose the condition that F(X, Y, Z) = 0, we get the ﬁnal degree-2
polynomial on the xi (H2 = 0). This quadric is in fact the Schur quadric correspond-
ing to a distinguished double six 7 of lines that necessarily exist on a cubic surface
constructed as above [22]. An equivalent rational map is given in [ 20, p. 557], but the
inverse is not provided.
(vi) To see this working, let us consider c and d, and see that these are desingualrised
on the smooth canonical embedding. Taking [X : Y : Z]=[ 1: t : t4] we get
[L1 : L2 : L3 : L4]=[ 1: t3 : t + t6 :− t2],
and so taking the limit we get [1: 0 : 0]2 ↦→[ 1: 0 : 0 : 0] in L coordinates. Acting with
A, we get the point in P4 given by
[x1 : x2 : x3 : x4 : x5]=[ ζ 3 : 1: ζ 2 : ζ : ζ 4].
Repeating the process taking [X : Y : Z]=[ 1: t4 : t] gives [1: 0 : 0]1 ↦→[ 0 : 1: 0 : 0]
in L coordinates, which is equivalently
[x1 : x2 : x3 : x4 : x5]=[ 1: ζ 3 : ζ : ζ 2 : ζ 4].
This makes sense, as the change Y ↔ Z corresponds to L1 ↔ L2, L3 ↔ L4.
Moreover, to clarify our last point on the imposition of H2 = 0, we consider the
point [X : Y : Z]=[ 0 : 1: 1] which does not lie on the HC-model of the curve. Under
our birational map this corresponds to the point
[L1 : L2 : L3 : L4]=[ 1 : 1 : 1 : 1]⇒[ x1 : x2 : x3 : x4 : x5]=
[
2 −
√
5 :− 2 +
√
5:− 1: 1 : 0
]
.
This point does lie on the Clebsch diagonal surface given by H1 = 0 = H3, but does
not satisfy H2 = 0.
Note that in the above proof of the equivalence of the Riemann surfaces, the bira-
tional map we constructed was deﬁned over Q[ζ]. As such, to equate the two algebraic
curves we need to be working over a ﬁeld containing Q[ζ]. We will later see when
looking at quotients of Bring’s curve that it is insufﬁcient to work over Q. Indeed,
note that over Q there are no solutions to the equations deﬁning Bring’s curve in the
P4-model.
7 A double six is a collection of 12 lines a1,..., a6, b1,..., b6 in P3, arranged as
a1 a2 a3 a4 a5 a6
b1 b2 b3 b4 b5 b6
so that each line is disjoint from those in the same row and column, but intersects the other ﬁve lines.
123
Bring’s curve: old and new Page 11 of 46 3
