---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-002-21-basic-properties
section_title: "Basic Properties"
section_number: 2.1
pages: 2-8
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
doc_brief: "European Journal of Mathematics (2024) 10:3 RESEARCH ARTICLE — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
matrix and its automorphisms. We begin with two descriptions: one as a model inP4 and the
second as a plane curve. In particular we shall construct the birational map between these
models, which we believe new. Such a map enables us to concretely translate calculations
from one model to another and will be helpful later in §4 when we look at quotients of the
curve.
Deﬁnition 2.1. Bring’s Curve B is deﬁned in P4 by the (homogeneous) equations 1
(1) Hk :=
5∑
i=1
xk
i = 0, k = 1, 2, 3,
where we have taken the coordinates [x1 :x2 :x3 :x4 :x5]∈ P4.
We will call (1) the P4-model of Bring’s curve. Historically, this curve was attributed
to Bring by Klein in his lectures on the icosahedron [Kle88]. Bring’s improvement on the
Tschirnhaus transformation enabled the general quintic to be brought to the Bring-Jerrard
form x5 +ex +f = 0 [VSA03]: if xi, i = 1,..., 5, are the roots of this equation then the
symmetric sums ∑
ixk
i = 0 for k = 1, 2, 3, and so the above curve emerges. Green [Gre78]
exploits this relation to Bring’s curve to (implicitly) solve the quintic using automorphic
forms. At this stage we may observe that S5≤ Aut(B).
Remark 2.2. In the above deﬁnition we have implicitly taken P4 = CP4, and indeed this will
be our deﬁnition throughout. At various junctures we will however highlight the number ﬁelds
within C that are relevant ﬁelds of deﬁnition for morphisms of the curve, or geometrically
important points on the curve.
1Note here we use the notation Hk of [Bur83] for the symmetric sum, whereas [Edg78] uses Sk.
BRING’S CUR VE: OLD AND NEW 3
For many calculations a plane model of a curve in P2 is useful. One of the main tools we
will utilise in this paper is the Riemann surfaces module of SageMath [The21] which requires
such a model. As such we introduce the following.
Deﬁnition 2.3. The Hulek-Craig (HC) model of Bring’s curve is the (singular) plane
curve in P2 given by
(2) F (X,Y,Z ) :=X(Y 5 +Z 5) + (XYZ )2−X 4YZ − 2(YZ )3 = 0,
taking homogeneous coordinates [X :Y :Z]∈ P2.
This model was used in [Hul87, Cra02] where they studied the curves modular properties.
Indeed Craig gives a parameterization of the curve in terms of modular functions following
work of Ramanujan. Craig does not identify the curve as Bring’s, whereas Hulek ﬁnds the
equation as a hyperplane section of a surface that parameterises elliptic normal curves of
degree 5, and then refers to previous results to connect it with Bring. This connection
was ﬁrst made in [Nar78], where the curve is attributed to Klein. Indeed, because of this
interpretation, one can write down Bring’s curve as
H/Γ0(2, 5) where Γ 0(2, 5) = Γ0(2)∩Γ(5) =



(a b
c d
)
∈SL2(Z)
⏐⏐
a≡d≡ 1 (mod 5)
b≡ 0 (mod 5)
c≡ 0 (mod 10)


.
To our knowledge, [Hul87] is the ﬁrst occurrence of this plane model of the curve; Klein
will write it down in [Kle88, p. 165, p. 242] but the relation to a plane model of Bring’s
curve is not made explicit. We will call (2) the HC-model of Bring’s curve. In the following
subsection we shall show the birational equivalence of (2) and (1).
Another plane model of Bring’s curve is given by y5− (x + 1)x2(x− 1)−1 = 0, introduced
in [Web05, Proposition 3.1] by considering the curve as a cyclic cover of P1, see §4.
2.1. Basic Properties. Towards proving the birational equivalence of the two models given
for Bring’s curve we begin with some basic properties of the curve. We introduce aﬃne
coordinates (x,y ) = (X/Z,Y/Z ) such that the HC-model is 0 = f(x,y ) = F (x,y, 1). Then
Resy(f(x,y ),∂yf(x,y )) =x4(x5−1)2(256x10−837x5 +3456). Investigation of the vanishing
of this resultant leads to the following.
Lemma 2.4 ([BN12]). The only singular (double) points in the HC-model of the curve are
Vk = [ζk :ζ 2k : 1] for k = 0,..., 4, where ζ = exp(2πi/5), and V5 = [1 : 0 : 0].
We shall return these points in due course; each of these singular points desingularizes to
two points. We also ﬁnd
Lemma 2.5. In the HC-model we have local expansions about the following points on the
curve
a := [0 : 0 : 1]≃ [2t3 :t : 1], b := [0 : 1 : 0]≃ [2t2 : 1/t : 1],
c := [1 : 0 : 0]2≃ [1 :t :t4], d := [1 : 0 : 0]1≃ [1 :t4 :t].
We see from this that
Corollary 2.6.
div(x) = 3a + 2b− 4c−d, div(y) =a−b− 3c + 3d, R F = 2a +b + 3c +
∑
i
ri,
whereRF is the ramiﬁcation divisor corresponding to the map x :B→ P1 and the ri are the
roots of the polynomial 256x10− 837x5 + 3456 appearing in the resultant.
4 H. W. BRADEN AND LINDEN DISNEY-HOGG
Lemma 2.7 ([BN12]). The genus of Bring’s curve is g = 4 and we have the ordered basis
of (unnormalised) diﬀerentials
v1 = (y3−x)dx
∂yf(x,y ) , v 2 = (y2x− 1)dx
∂yf(x,y ) , v 3 = (y−x2)dx
∂yf(x,y ) , v 4 = y(x2−y)dx
∂yf(x,y ) .
These diﬀerentials, while independent as holomorphic diﬀerentials, do satisfy an algebraic
relation.
Lemma 2.8. The canonical embedding of Bring’s curve in P3 ={[v1 :v2 :v3 :v4]} lies on
the quadric
(3) Q :v1v2 +v3v4 = 0.
While all full-rank quadrics in P3 are isomorphic to P1× P1 [Vak10], the standard proof
of which goes via showing every such quadric can be written in some coordinate system as
Q, we will subsequently want an explicit form of the isomorphism.
Proposition 2.9. Q≃ P1× P1.
Proof. Consider the mapQ→ P1× P1, a modiﬁcation of the Segre embedding, given by
ϕ : P1× P1→ P3, ϕ ([u :v], [z :w]) = [uz :vw :vz :−uw] := [v1 :v2 :v3 :v4].
Then ϕ([u :v], [z :w])∈Q .
The map ϕ is injective for suppose ϕ([u :v], [z :w]) =ϕ([u′ :v′], [z′ :w′]). Consider ﬁrst
that v4⁄= 0. Then
−v1
v4
= z
w = z′
w′, −v2
v4
= v
u = v′
u′,
and so correspond to the same point in P1× P1. Next suppose that 0 = −v4 =uw =u′w′
and without loss of generality that u = 0. If u′ = 0 we have injectivity, so suppose that
u′⁄= 0. Then w′ = 0 and [0 : vw : vz : 0] = [ u′z′ : 0 : v′z′ : 0] requiring z′ = 0 and a
contradiction. Thus we have that ϕ is injective.
To show the surjectivity ofϕ we may assume without loss of generality thatv4⁄= 0. Then
set
−v1
v4
= z
w, −v2
v4
= v
u.
Indeed we can spot the inverse map ϕ−1 :Q→ P1× P1 to be given by
ϕ−1([v1 :v2 :v3 :v4]) =



([v1 :v3], [v3 :v2]) {v1,v 3}⁄ ={0}⁄ ={v2,v 3},
([−v4 :v2], [v3 :v2]) {v1,v 3} ={0}⁄ ={v2,v 3},
([v1 :v3], [v1 :−v4]) {v1,v 3}⁄ ={0} ={v2,v 3},
([−v4 :v2], [v1 :−v4]) {v1,v 3} ={0} ={v2,v 3}.
□
Proposition 2.10 ([BN12]). The canonical divisor class on Bring’s curve is [KB] = [a +
2b + 3c].
Proof. This may be shown analytically or (as given in the accompanying notebook) entirely
using computer algebra. To show this analytically we use div( dx) =−2(4c +d) +RF . □
We now establish the main result of this subsection.
Proposition 2.11. The HC-model (2) is a model of Bring’s curve (1).
BRING’S CUR VE: OLD AND NEW 5
Proof. We will prove this by explicitly constructing the birational transform. To do so we
make use of the proof of Theorem 3 in [Dye95], where the author considers a particular
Clebsch hexagon2, constructs a pencil of plane sextics from this, and ﬁnds Bring’s curve as
the canonical model of a distinguished point in this pencil. By assuming that the HC-model
is already the distinguished curve in a pencil, we can construct the birational map. Note
this is a fundamentally diﬀerent approach to the that originally taken with the HC-model,
which was derived from considerations of the modular theory of the curve.
Explicitly, Dye introducesj as a solution to j2−j− 1 = 0 and then deﬁnes the pencil of
curves3 Sλ =S +λ|C|3 where
S(x,y,z ) = (x +jy)6 + (x−jy)6 + (y +jz)6 + (y−jz)6 + (z +jx)6 + (z−jx)6,
C(x,y,z ) =x2 +y2 +z2.
(4)
Next Dye considers the Clebsch hexagon H with vertices
(1,±j, 0), (0, 1,±j), (±j, 0, 1),
for which the corresponding 10 Brianchon points are at
(±j2, 1, 0), (0,±j2, 1), (1, 0,±j2), (1,±1,±1).
Dye shows that there is a unique member of the pencil, which he calls Γ, that contains the
vertices. Moreover, Γ has the vertices and only the vertices as double points.
To get a canonical model for Γ, which Dye show’s has genus 4, we now need a little
theory from [SR49, pp. 122-124], namely that a generic cubic surface in P3 is birational to
a system of plane cubics through 6 base points. We apply this taking these six points to be
the vertices of the hexagon H. Such a generic cubic surface F⊂ P3 can be written as the
vanishing of a determinant ⏐⏐⏐⏐⏐⏐
u1 v1 w1
u2 v2 w2
u3 v3 w3
⏐⏐⏐⏐⏐⏐
= 0,
where u1,...,w 3 are linear homogeneous functions of the P3 coordinates, that is to say
P = [L1 :L2 :L3 :L4]∈F⊂ P3 if and only if there exists P′ = [X :Y :Z]∈ P2 such that
Xui(P ) +Yvi(P ) +Zwi(P ) = 0.
Thinking of P′ as a point in a plane Π we get a birational transformation Π ↔F , P′↔P .
The map Ψ : Π→F will have theLa as homogeneous cubics in X,Y,Z . To see this rewrite
the determinant equation as (for i = 1, 2, 3)
4∑
a=1
aia(P′)La = 0
for some aia linear homogeneous in the X,Y,Z . On each aﬃne patch La⁄= 0 solving this
involves inverting a 3×3 matrix whose entries are linear homogeneous polynomials inX,Y,Z .
Likewise, given the La, we have a 3-parameter family of cubics given by
aL1 +bL2 +cL3 +dL4 = 0 for [ a :b :c :d]∈ P3.
2For the purposes of this deﬁnition a hexagon is a set of 6 points in P2, no three of which are collinear,
called the vertices. A Brianchon point of a hexagon is a non-vertex point through which 3 edges (the lines
joining two distinct vertices) pass. A Clebsch hexagon is a hexagon with 10 Brianchon points [Dye91].
3We are using the coordinates [x,y,z ] here, distinct from [X,Y,Z ], to highlight that these are not those
of the HC-model.
6 H. W. BRADEN AND LINDEN DISNEY-HOGG
A cubic in P2 has 10 projective coeﬃcients, and so a 3-parameter family is deﬁned by 6
constraints. Generically we can take those constraints to come in the form of intersection
with 6 generic points Oi∈ Π.
For our purposes, the six points we want to intersect with are the vertices of the Clebsch
hexagon, which are the double points of the exceptional curve Γ. Assuming the the HC-
model gives such an exceptional curve, we take the pointsVk identiﬁed in Lemma 2.4. Hence,
if we write a generic cubic in X,Y,Z as
a0X 3 +a1X 2Y +a2X 2Z +a3XY 2 +a4XYZ +a5XZ 2 +a6Y 3 +a7Y 2Z +a8YZ 2 +a9Z 3
the equations on the coeﬃcients we get (coming from intersecting with Vk (k = 0,..., 4)
and V5 respectively) are
a0ζ 3k +a1ζ 4k +a2ζ 2k +a3 +a4ζ 3k +a5ζk +a6ζk +a7ζ 4k +a8ζ 2k +a9 = 0,
a0 = 0.
Setting the coeﬃcients of ζnk to be zero gives us the 3-parameter family of cubics
0 =aX 2Y +bX 2Z +cXY 2 +dXZ 2−dY 3−aY 2Z−bYZ 2−cZ 3,
:=aL1 +bL2 +cL3 +dL4.
Comparing the coeﬃcients we see that our map into P3 is (essentially) the canonical
embedding. as
[v1 :v2 :v3 :v4] = [−L4 :L3 :−L2 :L1].
One can check, using for example Gr¨ obner bases, that theLa satisfy the equation
L2L2
4−L2
1L4−L1L2
3 +L2
2L3 = 0.
This is the cubic we callF . One can use the package Cremona [Sta18] in Macaulay2 to check
that the map Ψ is birational. Note one needs to make sure that the range is chosen such
that the map is explicitly surjective, not just use the implicit knowledge that the map is
surjective onto its image. Doing so and asking for the inverse map gives
[X :Y :Z] = [L2
2−L1L3 :L1L4 :L2L4].
For example, we can see
L2
2−L1L3
L1L4
=
(
X 2Z−YZ 2)2
−
(
X 2Y−Y 2Z
)(
XY 2−Z 3)
(X 2Y−Y 2Z) (XZ 2−Y 3) ,
= X 4Z 2−X 2YZ 3−X 3Y 3 +XY 4Z
X 3YZ 2−XY 2Z 3−X 2Y 4 +Y 5Z = X
Y ,
and
L1L4
L2L4
= L1
L2
= X 2Y−Y 2Z
X 2Z−YZ 2 = (X 2Z−YZ 2)(Y/Z)
X 2Z−YZ 2 = Y
Z.
We now have a cubic surface in P3 corresponding to the system of curves intersecting the
Vi. From [Hir86, pp. 198-201] we know there exists a coordinate system in which this cubic
can be written as the subset of P4
H3 = 0 =H1
(this is called ‘the’ Clebsch surface). To look for such a coordinate system, we write this
surface in P3 as
0 =x2
1x2 +x1x2
2 +x2
1x3 +x2
2x3 +x1x2
3 +x2x2
3 +x2
1x4 +x2
2x4 +x2
3x4 +x1x2
4 +x2x2
4 +x3x2
4
+ 2x1x2x3 + 2x1x2x4 + 2x1x3x4 + 2x2x3x4.
BRING’S CUR VE: OLD AND NEW 7
From here, one can use the fact that the 10 Eckardt points 4 of the cubic in La form the 10
vertices of a pentahedron [Hir86], and that in the coordinate system of the Clebsch surface
in P4 these lie at the permutations of [1 : −1 : 0 : 0 : 0] [Edg78]. This gives us a possible
way a spotting the transform if we can calculate the Eckardt points of F . To do this, we
use the identiﬁcation from [Dye95], that the 3 lines in F intersecting to give an Eckardt
point come from the 3 edges of H intersecting at a Brianchon point. To this end we ﬁnd
the images of the ViVj for which we give a generating set of the ideal corresponding to the
line, for example
(1) Ψ(V0V5) :⟨L4−L3,L 2−L1⟩,
(2) Ψ(V1V2) :
⟨
L4 + (ζ 2 +ζ + 1)L2 + (ζ 4−ζ 2−ζ)L1,L 3 + (ζ 3 + 2ζ 2 +ζ)L2 + (ζ 3 +ζ 2 +ζ)L1
⟩
,
(3) Ψ(V3V4) :
⟨
L4 + (−ζ 2−ζ)L2 + (ζ 3 + 2ζ 2 +ζ)L1,L 3 + (ζ 3−ζ− 1)L2 + (ζ 2 +ζ + 1)L1
⟩
.
Then
Ψ(V0V5)∩Ψ(V1V2)∩Ψ(V3V4) = [−ζ 3−ζ 2−1 :−ζ 3−ζ 2−1 : 1 : 1] = Ψ(V0V5∩V1V2∩V3V4).
One can do likewise to ﬁnd the other Eckardt points.
Armed now with the knowledge of the Eckardt points, we can ﬁnd appropriate pro-
jective transforms A that biject the sets of Eckardt points by acting ( x1,x 2,x 3,x 4)T =
A(L1,L 2,L 3,L 4)T , for example
A =


ζ 3 −1 −ζ 2 ζ
1 −ζ 3 −ζ ζ 2
ζ 2 −ζ −1 ζ 3
ζ −ζ 2 −ζ 3 1

.
We can then use again Macaulay2 to check that this transform then gives us the correct cubic
in P3. Moreover, if we now restrict to the HC-model in the system of curves that intersect
the Vi, that is we impose the condition that F (X,Y,Z ) = 0, we get the ﬁnal degree-2
polynomial on the xi (H2 = 0). This quadric is in fact the Schur quadric corresponding to
a distinguished double-six 5 of lines that necessarily exist on a cubic surface constructed as
above [Dye95]. An equivalent rational map is given in [Dol12, p. 557], but the inverse is not
provided.
To see this working, let’s consider c and d, and see that these are desingualrised on the
smooth canonical embedding. Taking [X :Y :Z] = [1 :t :t4] we get
[L1 :L2 :L3 :L4] = [1 :t3 :t +t6 :−t2],
and so taking the limit we get [1 : 0 : 0] 2↦→ [1 : 0 : 0 : 0] in L coordinates. Acting with A,
we get the point in P4 given by
[x1 :x2 :x3 :x4 :x5] = [ζ 3 : 1 :ζ 2 :ζ :ζ 4].
Repeating the process taking [ X :Y :Z] = [1 : t4 :t] gives [1 : 0 : 0] 1↦→ [0 : 1 : 0 : 0] in L
coordinates, which is equivalently
[x1 :x2 :x3 :x4 :x5] = [1 :ζ 3 :ζ :ζ 2 :ζ 4].
This makes sense, as the change Y ↔Z corresponds to L1↔L2, L3↔L4.
4An Eckardt point of a surface is a point where three lines contained within the surface intersect [Hir86].
5A double six is a collection of 12 lines a1,...,a 6,b 1,...,b 6 in P3, arranged as
a1 a2 a3 a4 a5 a6
b1 b2 b3 b4 b5 b6
so that each line is disjoint from those in the same row and column, but intersects the other 5 lines.
8 H. W. BRADEN AND LINDEN DISNEY-HOGG
Moreover, to clarify our last point on the imposition of H2 = 0, we consider the point
[X : Y : Z] = [0 : 1 : 1] which does not lie on the HC-model of the curve. Under our
birational map this corresponds to the point
[L1 :L2 :L3 :L4] = [1 : 1 : 1 : 1]⇒ [x1 :x2 :x3 :x4 :x5] = [2 −
√
5 :−2 +
√
5 :−1 : 1 : 0].
This point does lie on the Clebsch diagonal surface given by H1 = 0 = H3, but does not
satisfy H2 = 0. □
Note that in the above proof of the equivalence of the Riemann surfaces, the birational
map we constructed was deﬁned over Q[ζ]. As such, to equate the two algebraic curves we
need to be working over a ﬁeld containing Q[ζ]. We will later see when looking at quotients
of Bring’s curve that it is insuﬃcient to work over Q. Indeed, note that over Q there are no
solutions to the equations deﬁning Bring’s curve in the P4-model.
