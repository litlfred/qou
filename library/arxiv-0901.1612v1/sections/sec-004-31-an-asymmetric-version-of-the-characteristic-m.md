---
doc_id: arxiv-0901.1612v1
doc_title: "TRIPLE LINKING NUMBERS, AMBIGUOUS HOPF INV ARIANTS"
section_id: sec-004-31-an-asymmetric-version-of-the-characteristic-m
section_title: "An asymmetric version of the characteristic map"
section_number: 3.1
pages: 6-18
source_pdf: 0901.1612v1.pdf
source_sha256: b4f3efcadd1e5caf
doc_brief: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links — Three-component links in the 3-dimensional sphere were classi- fied up to link homotopy by John"
duplicate_of: "deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-lin"
---
S3⊂ R4, let ℘x denote stereographic projection of S3−{ x} onto the 3-space R3
x
through the origin in R4 that is orthogonal to the vector x, as shown in Figure 2.
x
−x
y
z
℘xy
℘xz
R3
x
S3
(℘xy−℘xz)/‖℘xy−℘xz‖
Figure 2. Stereographic projection
6
Triple linking numbers, ambiguous Hopf invariants and integral formulas
For any (x,y,z )∈ Conf3S3, consider the points ℘xy and ℘xz in R3
x. Translation in
R3
x moves℘xz to the origin, and then dilation in R3
x makes the translated ℘xy into a
unit vector. Composing with ℘−1
x , we see that x has been kept ﬁxed, y has moved to
the point (℘xy−℘xz)/‖℘xy−℘xz‖ on the equatorial 2-sphere S2
x = S3∩ R3
x, and z
has moved to−x, as indicated in the ﬁgure.
This procedure deﬁnes a deformation retraction
r(x,y,z ) = ( x, (℘xy−℘xz)/‖℘xy−℘xz‖ ,−x)
of Conf 3S3 onto the subspace {(x,w,−x)| x •w = 0}, which is a copy of the unit
tangent bundle US 3 of the 3-sphere via the correspondence ( x,w,−x)↔ (x,w ). Let
π :US 3→S2 denote the projection onto the ﬁber, sending ( x,w ) to wx−1.
Now deﬁne the asymmetric characteristic map ~gL :T 3−→S2 of a link L, as
above, to be the composition π◦r◦eL. Noting that ( ℘xv)x−1 = ℘1(vx−1), we have
explicitly
~gL(s,t,u ) = ℘1(yx−1)−℘1(zx−1)
‖℘1(yx−1)−℘1(zx−1)‖
where x =x(s), y =y(t) and z =z(u) parametrize the components of L. This map is
easily seen to be homotopic to the characteristic map gL deﬁned above.
The restriction of ~gL to∗× S1×S1 is the negative of the Gauss map for the link
℘1((Y∪Z)x−1), and so noting that ℘1 is orientation reversing (with the usual sign
conventions) its degree is the linking number of Y with Z. Since gL is homotopic to
~gL, the same is true forgL. But then it follows from the symmetry of gL that its degree
onS1×∗× S1 is the linking number of X withZ, and its degree on S1×S1×∗ is the
linking number of X with Y . This proves the ﬁrst statement in Theorem A.
This version ~gL of the characteristic map will also facilitate the topological proof of
the rest of Theorem A, to be given next.
7
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
4. Sketch of the topological proof of Theorem A
Starting with a link in the 3-sphere, consider the delta move shown in Figure 3,
which may be thought of as a higher order variant of a crossing change. It takes place
within a 3-ball, outside of which the link is left ﬁxed.
X X′
Y Y′
Z Z′
Figure 3. The delta move L→L′
The delta move was introduced by Murakami and Nakanishi [1989], who proved that
an appropriate sequence of such moves can transform any link into any other link with
the same number of components, provided the two links have the same pairwise linking
numbers.
The key organizational idea for this proof of Theorem A is to show that the delta
move, when applied to the three components X, Y and Z of the link L, as shown
in Figure 3, increases its Milnor µ-invariant by 1, while increasing the Pontryagin
ν-invariant of its characteristic map gL by 2.
The fact that the delta move increases µ by 1 is well known to experts; our proof
relies on the geometric formula for µ due to Mellor and Melvin [2003] in terms of how
each link component pierces the Seifert surfaces of the other two components, plus a
count of the triple point intersections of these surfaces. In particular, one can use a
family of Seifert surfaces that diﬀer only near the delta move, as shown in Figure 4.
Figure 4. Seifert surfaces for L and L′
8
Triple linking numbers, ambiguous Hopf invariants and integral formulas
To see how the delta move aﬀects the ν-invariant, we will viewν as a relative Euler
class, following Gompf [1998] and Cencelj, Repovˇ s and Skopenkov [2007].
To that end letL andL′ be two three-component links inS3 with the same pairwise
linking numbers p, q and r, and let L and L′ be the framed links in the 3-torus † that
are the preimages of a common regular value of their characteristic maps gL and gL′.
Orient L and L′ so that, when combined with the pullback of the orientation on S2 to
a tangent 2-plane transverse to these links, we get the given orientation on T 3. Since
L and L′ have the same pairwise linking numbers, L and L′ are homologous in T 3. It
then follows by a standard argument thatL×0 and L′×1 together bound an embedded
surface F in T 3× [0, 1].
The relative normal Euler class e(F) is the intersection number of F with a
generic perturbation of itself that is directed by the given framings along L× 0 and
L′× 1, but is otherwise arbitrary. Then, according to Gompf and Cencelj–Repovˇ s–
Skopenkov,
ν(gL′,gL) ≡ e(F) mod 2 gcd( p,q,r ).
The key step in seeing how the delta move aﬀects the ν-invariant is to adjustL and
L′ by link homotopies so that up to isotopy
L′ = L∪ L∗
where L∗ is a two-component link bounding an annulusA⊂T 3−L with relative normal
Euler class 2. Then the surface F = ( L× [0, 1])∪ (A× 1), with ∂F = L′× 1− L× 0,
has e(F) = 2, since e(L× [0, 1]) = 0. Thus ν(gL′,gL)≡ e(F) = 2, showing that the
delta move increases the ν-invariant ofL by 2. Explaining how this step is carried out
will complete our sketch of the topological proof of Theorem A.
We begin with the delta move as shown above and change it by an isotopy so that
it now appears as pictured in Figure 5.
B B
C C
X
Y
Z
X′
Y′
Z′
Figure 5. A diﬀerent view of the delta move
From this picture, we see that the delta move can be regarded as a pair of crossing
changes of opposite sign which introduce a pair of small “clasps”
 −→
 .
†For the reader’s convenience, all subsets of T 3 in this section are written in blackboard bold to
distinguish them from subsets of S3.
9
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
We may assume that the move takes place inside the large ball B in S3 of radius
π/2 centered at−1. If we think of 1 and −1 as the north and south poles of S3, then
B is just the southern hemisphere. Figure 5 shows that inside B, the portions of X
and X′ lie along the great circle through 1 and i (so in fact X and X′ coincide) while
the portions of Y , Z, Y′ and Z′ lie close to the great circle C through j and k.
Outside B, the links L and L′ coincide and, maintaining this coincidence, we move
them into a more favorable position as follows. First unknot X =X′ by a link homo-
topy, and move it to the rest of the great circle through 1 and i. Then by an isotopy
moveY and Z into a small neighborhood of the great circle C, and position them so
that their orthogonal projections to C are Morse functions with just one critical point
per critical value. As intended, Y′ and Z′ move likewise outside B. Note that each of
the aforementioned clasps contributes two critical values to these projections, and we
may assume that no other critical values fall between these two.
Now we use the asymmetric versions ~gL and ~gL′ of the characteristic mapsT 3→S2,
identifying the target S2 with the unit 2-sphere in the purely imaginary ijk-subspace
of the quaternions. We interpret Figure 5 as showing the image of S3−{ 1} under the
stereographic projection ℘1, and view i as the north pole of S2.
It is straightforward to check that, under the genericity conditions imposed above,
the point i∈S2 is a common regular value for ~gL and ~gL′, and that the framed links
L and L′ inT 3 that are the inverse images of i under these maps are for the most part
the same. In fact we will show that, up to isotopy L′ = L∪ L∗ where L∗ consists of a
pair of oppositely oriented spiral perturbations of S1× pt× pt, coming from the two
clasps shown in Figure 5, and that these two spirals bound an annulus A in T 3− L
whose relative normal Euler class e(A) is 2. The argument will be given as we explain
Figures 6–8.
The discussion is independent of what the links L and L′ look like outside the ball
B shown in Figure 5. The simplest case occurs when L is the three-component unlink,
and L′ =X′∪Y′∪Z′ is the Borromean rings, whose stereographic image is shown in
Figure 6.
−1
i
−i
∞↔ 1
C
X′
Z′ Y′
Figure 6. Borromean Rings
10
Triple linking numbers, ambiguous Hopf invariants and integral formulas
We have, as before, that X′ is the great circle through 1 and i, with image the blue
vertical axis, while Y′ and Z′ lie in a small tubular neigborhood of the great circle
C through j and k, with images shown in red and green. In this circumstance, the
general formula L′ = L∪ L∗ has L empty, and hence L′ = L∗.
Figure 7 shows enlargements of the two clasps between red Y′ and green Z′, with
points on their segments labeled by numbers on Y′ and by letters on Z′, ordered
consistently with their orientations.
Y′
Y′
Z′
Z′1
2
3 4
5
6a
b
cd
e
f
Figure 7. The two clasps
Our job is to ﬁnd the preimage L′ inS1×S1×S1 of the regular value i of the map
gL′, which means we must ﬁnd the points where the vector from the green ℘1(zx−1)
to the red ℘1(yx−1) points straight up.
We pause to see the eﬀect of right multiplication byx−1. Let x travel alongX =X′
from 1 to−i to−1 to i and back to 1, which is the direction in which this component
is oriented. Then right multiplication by x−1 gradually rotates this component in
the opposite direction. In the image 3-space, it looks like the vertical axis is moving
downwards. At the same time, the great circle C throughj andk is gradually rotated
in the direction from j towards−k. A small tubular neighborhood of C follows this
rotation and twists as it goes, dragged by the downward motion of the vertical axis.
Now focusing on the left clasp, and starting with x = 1, we see that the arrow ⃗f2
from green f to red 2 points up. As x moves aroundX′ from 1 towards−i (up on the
blue vertical axis) a loop of upward pointing vectors is traced out, passing successively
through ⃗e1, ⃗d2, ⃗e3, and ﬁnally back to ⃗f2. In Figure 8, the 3-torus is depicted as a
cube, in which this loop is shown near the front left corner of the bottom red-green
square, traced in a counterclockwise direction. When the progression of x(s) values is
taken into account, we get the orange spiral curve shown above this loop. This is one
component of L′, and is oriented according to the convention for framed links.
Focusing on the right clasp and repeating the above procedure, we get the orange
spiral curve shown at the right rear, lying over the loop ⃗a5⃗b6⃗c5⃗b4. This is the other
component of L′, and is also oriented according to convention.†
†In fact, one need not go through the careful analysis to determine the orientations of the spirals.
All that is important is that they are oppositely oriented, which follows from the fact that the pairwise
linking numbers for the Borromean rings are zero.
11
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
T 3
A
f e d c b a
654321
s
t
u
Figure 8. Computing e(A) = 2
Together, the components of L′ bound the orange annulus A shown in the cube.
This annulus is constructed as follows. Each point on the left spiral loop is joined to
the point on the right spiral loop at the same height s by a straight line segment in
the 2-torus s×S1×S1. The t-coordinate moves steadily so that y(t) travels along the
arc of Y′ which lies in the ball B (joining 3 to 4) and the u-coordinate moves steadily
so that z(u) travels along the arc of Z′ which lies in B (joining d to c). It is easy to
see that this annulus A is embedded in the 3-torus and that, even in the general case
where L is not empty, it would still be disjoint from L.
Now since A lies inT 3, its relative normal Euler classe(A) (when viewed as a surface
inT 3× [0, 1]) can be computed as the intersection number of A with the inverse image
of any other regular value of ~gL′. In particular, the point−i is also a regular value, and
its inverse image ˆL′ is calculated from an analysis of the clasps, just as we did for the
inverse image of i. It consists of two spirals, which can be obtained from the spirals
in L′ by moving them half-way along in the vertical (blue) direction. We show ˆL′ in
Figure 8 as a pair of purple spirals, which are oriented the same way as the orange
spirals.
It is seen in this ﬁgure that the purple spirals pierce the orange annulus twice in the
positive direction, conﬁrming that
e(A) = A • ˆL′ = 2 ,
and completing the sketch of the topological proof of Theorem A.
12
Triple linking numbers, ambiguous Hopf invariants and integral formulas
5. Sketch of the algebraic proof of Theorem A
This proof is organized around the following key diagram:
(∗)
[[S1∪S1∪S1,S 3]] H(3)
[S1×S1×S1,S 2]
g
?
 π1Maps(S1×S1,S 2)
G
?
The left half represents the geometric-topological problem we are trying to solve, and
is devoid of algebraic structure. The right half represents the algebraic structures that
we impose on the left half via the two horizontal maps in order to solve the problem.
In the upper left corner of ( ∗) we have the set of link-homotopy classes of three-
component links in the 3-sphere S3, and in the lower left corner the set of homotopy
classes of maps of the 3-torus to the 2-sphere. The vertical map g between them
assigns to the link-homotopy class of L the homotopy class of its characteristic map
gL. Theorem A describes g and asserts that it is one-to-one.
In the upper right corner of ( ∗) we have the group H(3) of link-homotopy classes
of three-component string links. A k-component string link consists of k oriented
intervals embedded disjointly in a cube, with their tails on the bottom face, their tips
on the top face directly above their tails, and their interiors in the interior of the
cube. The terminology was coined by Habegger and Lin [1990]. The product of two
k-component string links with endpoints in a common position is given by stacking
the second one on top of the ﬁrst. When a string link moves by a link homotopy, each
strand is allowed to cross itself, while diﬀerent strands must remain disjoint, just as
for links. Then the above product induces a group structure on the set H(k) of link
homotopy classes of k-component string links.
P Q R
= =
PQP−1Q−1 = B
P
Q
P−1
Q−1
Figure 9. Generators forH(3)
13
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
Following Habegger and Lin, we derive the following presentation for H(3):
H(3) = ⟨P,Q,R,B | [P,Q ] = [Q,R ] = [R,P ] =B,
[P,B ] = [Q,B ] = [R,B ] = 1⟩
The string links P , Q, R and B are those shown in Figure 9.
Using this presentation, elements of H(3) can be written uniquely in the form
PpQqRrBµ , for p,q,r,µ ∈ Z.
Two elements PpQqRrBµ and Pp∗
Qq∗
Rr∗
Bµ∗
are conjugate if and only if p = p∗,
q =q∗, r =r∗ and µ≡µ∗ mod gcd(p,q,r ).
A string link S can be closed up to a link ˆS by joining the tops of the strands to
their bottoms outside the cube, without introducing any more crossings. For example,
the closure of the three-component string link B is the Borromean rings, as shown in
Figure 10.
=
ˆB
Figure 10. The string link B closes up to the Borromean rings ˆB
Thus the Borromean rings, a “primitive example” in the world of links, is the closure
of a string link which is itself a commutator of simpler string links.
The closing-up operation descends to link homotopy classes and provides the upper
horizontal map in (∗). It is easily seen that the closure of the string link PpQqRrBµ
has pairwise linking numbers p, q and r and Milnor invariant µ mod gcd(p,q,r ). It
follows that this closing-up map is onto. Furthermore, its point inverse images are
the conjugacy classes inH(3), a special circumstance for links with three components
which fails for four or more components.
In the lower right corner of ( ∗) we have the union of the fundamental groups of
the components of the space of continuous maps of the 2-torus to the 2-sphere, with
one group π1Mapsp(S1×S1,S 2) for each choice of degree p of these maps. The work
of Fox [1948] on torus homotopy groups (the case p = 0), and its generalization by
Larmore and Thomas [1980], provides explicit presentations for these groups:
π1Mapsp(S1×S1,S 2) = ⟨Up,Vp,Wp| [Up,Vp] =W 2
p , W2p
p = 1,
[Up,Wp] = [Vp,Wp] = 1⟩
14
Triple linking numbers, ambiguous Hopf invariants and integral formulas
Using this presentation, elements of π1Mapsp(S1×S1,S 2) can be written uniquely
in the form
Uq
pVr
p Wν
p , for q,r,ν ∈ Z with 0≤ν <2|p|.
Two elements Uq
pVr
p Wν
p and Uq∗
p Vr∗
p Wν∗
p are conjugate if and only if q = q∗, r = r∗
and ν≡ν∗ mod 2 gcd(p,q,r ).
A direct argument using framed links shows how the generators Up, Vp and Wp of
π1Mapsp(S1×S1,S 2) can be represented by speciﬁc maps S1×S1×S1→ S2, all
agreeing with some ﬁxed map of degree p on∗× S1×S1. In addition to this common
feature, the representatives for Up, Vp, Wp have degrees q = 1, 0, 0 on S1×∗× S1,
degreesr = 0, 1, 0 on S1×S1×∗ , and Pontryagin invariantsν = 0, 0, 1 relative to the
chosen basepoint for π1Mapsp(S1×S1,S 2).
The lower horizontal map in the key diagram takes a homotopy class of based loops
in the space Maps(S1×S1,S 2), ignores basepoints, identiﬁes S1×S1 with∗×S1×S1,
and then regards this class as a homotopy class of maps of S1×S1×S1→S2 in the
usual way. In particular, the element Uq
pVr
p Wν
p ofπ1Mapsp(S1×S1,S 2) is taken to a
map with degrees p,q andr on the 2-dimensional coordinate subtori, and – this is the
key observation – with Pontryagin invariant ν mod 2 gcd(p,q,r ) relative to the image
of the basepoint map. This lower horizontal map is onto, and point inverse images are
conjugacy classes in π1Mapsp(S1×S1,S 2).
The ﬁnal step will be to deﬁne the vertical mapG on the right side of the key diagram
to make the whole diagram commutative, and to be a group homomorphism, insofar as
possible. The hedge “insofar as possible” refers to the fact that we have a groupH(3) in
the upper right corner of the diagram, but only a union of groupsπ1Mapsp(S1×S1,S 2)
in the lower right corner. We deal with this disparity by demoting H(3) to a union of
groups as follows.
LetH0(3) denote the subgroup of H(3) consisting of string links with the second
and third strands unlinked, and with presentation:
H0(3) =⟨Q,R,B | [Q,R ] =B, [Q,B ] = [R,B ] = 1⟩.
Consider the left cosets Hp(3) = PpH0(3) ofH0(3), and convert each of them into a
subgroup isomorphic toH0(3) by using left translation to transfer the group structure
from subgroup to coset. Adopting the notations Qp =PpQ,Rp =PpR andBp =PpB
for the generators of Hp(3) in this borrowed group structure, we get the presentation
Hp(3) =⟨Qp,Rp,Bp| [Qp,Rp] =Bp, [Qp,Bp] = [Rp,Bp] = 1⟩.
We are now ready to deﬁne the vertical mapG on the right side of (∗) so as to make
the whole diagram commutative, and at the same time to be a union of homomorphisms
from the groupsHp(3) to the groups π1Mapsp(S1×S1,S 2).
15
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
To do this, we start with speciﬁc string links to represent the elements of Hp(3).
For purposes of illustration, we choose p = 2, and show in Figure 11 the string links
12 = P 2, Q2 = P 2Q and R2 = P 2R, and under them the three-component links we
get by closing them up.
12 Q2 R2
ˆ12 ˆQ2 ˆR2
Figure 11. Closing up the generators of H2(3)
The corresponding characteristic maps from S1×S1×S1→ S2 all restrict to the
same map of degree 2 on∗× S1×S1, and therefore all three represent elements of the
fundamental group π1Maps2(S1×S1,S 2) based at this map. We denote these three
images by G2(P 2),G2(P 2Q) and G2(P 2R), with the intent of forcing commutativity
in the key diagram. In fact, we can do this for all the string links P 2QqRrBµ, and a
simple geometric argument shows that composition in the group H2(3) carries over in
this way to multiplication in the group π1Maps2(S1×S1,S 2).
Furthermore, a direct argument using framed links shows that the elementsG2(P 2Q)
andG2(P 2R) may serve as the elements U2 and V2 in the above presentation for
π1Maps2(S1×S1,S 2), so thatG2 takesP 2Q toU2 andP 2R toV2. It then follows that
G2 maps P 2B = [P 2Q,P 2R] to [U2,V 2] =W 2
2 .
The value p = 2 used above was just for purposes of illustration, and the cor-
responding results are true for all values of p. Thus we have deﬁned the verti-
cal map G on the right side of our key diagram to be a union of homomorphisms
Gp :Hp(3)→π1Mapsp(S1×S1,S 2) making the whole diagram commutative.
Now letL be any three-component link inS3 with pairwise linking numbersp,q and
r and Milnor invariant µ. Then L is link homotopic to the closure of PpQqRrBµ. By
commutativity of the key diagram, the homotopy class of the characteristic map gL is
the image under the lower horizontal map of the elementGp(PpQqRrBµ) =Uq
pVr
p W 2µ
p
of π1Mapsp(S1×S1,S 2), and therefore has Pontryagin invariant 2µ, as desired.
This completes our sketch of the algebraic proof of Theorem A.
16
Triple linking numbers, ambiguous Hopf invariants and integral formulas
6. Sketch of the proof of Theorem B
Let L be a 3-component link in S3 with pairwise linking numbers p, q and r all
zero. We saw in Theorem A that these numbers are the degrees of the characteristic
map gL :T 3→S2 on the 2-dimensional coordinate subtori. Thus gL is homotopic to
a map which collapses the 2-skeleton of T 3, and so is in eﬀect a map of S3→S2. The
Hopf invariant of this map, which we will regard as the Hopf invariant of gL, is equal
to Pontryagin’sν-invariant comparinggL to the constant map, and we will denote this
byν(gL).
To calculate this Hopf invariant, we adapt J. H. C. Whitehead’s integral formula for
the Hopf invariant of a map from S3→ S2 to the case of a map from T 3→ S2, and
show how to make the calculation explicit.
Whitehead [1947] expressed the Hopf invariant of a mapf :S3→S2 as follows. Let
ω be the area 2-form on S2, normalized so that
∫
S2ω = 1. Then its pullback f∗ω is a
closed 2-form on S3 which is exact because H2(S3; R) = 0. Hence f∗ω =dα for some
1-form α on S3, and Whitehead showed that
Hopf(f) =
∫
S3
α∧f∗ω,
the integral being independent of the choice of α.
We recast Whitehead’s formula in terms of vector ﬁelds by letting Vf be the vector
ﬁeld on S3 corresponding in the usual way to the 2-form f∗ω. Then Vf is divergence-
free, since f∗ω is closed, and is in fact in the image of curl since f∗ω is exact. Thus
Vf =∇× W for some vector ﬁeld W on S3, and the integral formula for the Hopf
invariant becomes
Hopf(f) =
∫
S3
W • Vf d(vol),
independent of the choice of W .
To make Whitehead’s formula more explicit, one needs a way to produce a vector
ﬁeld W whose curl is Vf. On R3 this can be done by viewing Vf as a ﬂow of electric
current and then calculating the corresponding magnetic ﬁeld BS(Vf) using the classical
formula of Biot and Savart [1820]:
BS(Vf) = −∇× Gr(Vf),
where Gr is the Green’s operator that inverts the vector Laplacian. Then by Amp` ere’s
Law,∇× BS(Vf) =Vf.
The explicit formula for the Green’s operator is well known on R3, namely convo-
lution with the fundamental solution ϕ(r) = −1/(4πr) of the scalar Laplacian, and
hence
BS(Vf)(y) =
∫
R3
Vf(x)×∇yϕ (‖y−x‖) dx,
17
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
assuming that V is compactly supported, to guarantee that the integral converges.
The corresponding formula on S3 was given by DeTurck and Gluck [2008] and by
Kuperberg [2008].
We can summarize the calculation of the Hopf invariant in the single formula
Hopf(f) =
∫
S3
BS(Vf) • Vf d(vol)
which was Woltjer’s original expression for the helicity of the vector ﬁeld Vf.
A routine check shows that the above formula, with the integration over T 3 instead
of S3, yields the value of the Hopf invariant of the characteristic map gL : T 3→ S2.
This provides a formula for Pontryagin’s ν-invariant, and portrays it as the helicity of
the associated vector ﬁeld VgL, which for simplicity we denote by VL:
(‡) ν(gL) = Hopf(gL) = Hel(VL) =
∫
T 3
BS(VL) • VL d(vol).
A straightforward calculation shows that
VL = Ft×Fu • F
4π‖F‖3 ∂/∂s + Fu×Fs • F
4π‖F‖3 ∂/∂t + Fs×Ft • F
4π‖F‖3 ∂/∂u,
whereF :T 3→ R3−{ 0} is the map deﬁned in Section 3, and where subscripts denote
partial derivatives.
Therefore, to make the integral formula (‡) explicit, it remains to obtain an explicit
formula for the Biot-Savart operator on the 3-torus. As in the case of R3, this depends
on having an explicit formula for the fundamental solution of the scalar Laplacian.
