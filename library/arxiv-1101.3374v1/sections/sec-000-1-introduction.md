---
doc_id: arxiv-1101.3374v1
doc_title: "PONTRYAGIN INVARIANTS AND INTEGRAL FORMULAS FOR MILNOR’S TRIPLE LINKING NUMBER"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-20
source_pdf: 1101.3374v1.pdf
source_sha256: 01d76c1d259c1d51
doc_brief: "PONTRYAGIN INVARIANTS AND INTEGRAL FORMULAS FOR MILNOR’S TRIPLE LINKING NUMBER — To each three-component link in the 3-sphere, we associate a geometrically natural characteristic map from the 3-torus"
---
Borromean Rings
Three-component links in the 3-sphere S3 were classiﬁed up to
link homotopy – a deformation during which each component
may cross itself but distinct components must remain disjoint – by
John Milnor in his senior thesis, published in 1954. A complete
set of invariants is given by the pairwise linking numbers p, q and
r of the components, and by the residue class µ of one further
integer modulo the greatest common divisor of p, q and r, the
triple linking number of the title. For example, the Borromean
rings shown here have p =q =r = 0 and µ =±1, where the sign
depends on the ordering and orientation of the components.
To each such linkL we will associate a geometrically natural characteristic mapgL from
the 3-torus T 3 =S1×S1×S1 to the 2-sphere S2 in such a way that link homotopies of
L become homotopies of gL. The deﬁnition of gL will be given below. The assignment
L↦→gL then deﬁnes a function
g :L3−→[T 3,S 2]
from the setL3 of link homotopy classes of three-component links in S3 to the set [T 3,S 2]
of homotopy classes of maps T 3→S2, and it will be seen below that g is injective.
Maps from T 3 to S2 were classiﬁed up to homotopy by Lev Pontryagin in 1941. A
complete set of invariants is given by the degrees p, q and r of the restrictions to the
2-dimensional coordinate subtori, and by the residue class ν of one further integer modulo
twice the greatest common divisor of p, q andr, the Pontryagin invariant of the map.
1
arXiv:1101.3374v1  [math.GT]  18 Jan 2011
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
This invariant is an analogue of the Hopf invariant for maps from S3 to S2, and is an
absolute version of the relative invariant originally deﬁned by Pontryagin forpairs of maps
from a 3-complex to S2 that agree on the 2-skeleton of the domain.
Our ﬁrst main result, Theorem A below, equates Milnor’s and Pontryagin’s invariants
p, q and r for L and gL, and asserts that
2µ(L) = ν(gL).
As a consequence, the function g :L3 −→ [T 3,S 2] above is one-to-one, with image the
set of maps of even ν-invariant.
In the special case when p =q =r = 0, we derive an explicit and geometrically natural
integral formula for the triple linking number, reminiscent of Gauss’ classical integral
formula for the pairwise linking number. This formula and variations of it are presented
in Theorem B below.
In the rest of this introduction, we provide the deﬁnition of the characteristic map, give
careful statements of Theorems A and B, and then discuss some motivation for our work
coming from the homotopy theory of conﬁguration spaces and from ﬂuid dynamics and
plasma physics.
The characteristic map of a three-component link in the 3-sphere
Let x, y and z be three distinct points on the unit 3-sphere S3 in R4. They cannot
lie on a straight line in R4, so must span a 2-plane there. Translate this plane to pass
through the origin, and then orient it so that the vectors x−z and y−z form a positive
basis. The result is an element G(x,y,z ) of the Grassmann manifold G 2R4 of all oriented
2-planes through the origin in 4-space. This procedure deﬁnes the Grassmann map
G : Conf3S3 −→ G2R4
pictured in Figure 1, where
Conf3S3 ⊂ S3×S3×S3
is the conﬁguration space of ordered triples of distinct points in S3. The map G is
equivariant with respect to the diagonal SO(4) action on S3×S3×S3 and the usual
SO(4) action on G 2R4.
G(x,y,z )
x
y z
S3R4
Figure 1. The Grassmann map (x,y,z )↦→G(x,y,z )
2
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
The Grassmann manifold G2R4 is diﬀeomorphic to the productS2×S2 of two 2-spheres,
as explained in Section 4 below. Let π+ and π− : G2R4→ S2 denote the projections to
the two factors. One of these will be used in the deﬁnition of the characteristic map, but
the choice of which one will be seen to be immaterial.
Now let L be a link in S3 with three parametrized components
X = {x(s)| s∈S1} , Y = {y(t)| t∈S1} and Z = {z(u)| u∈S1}
as indicated schematically in Figure 2. Here and throughout, we view the parametrizing
circle S1 as the quotient R/2πZ, and assume implicitly that the parametrizing functions
x =x(s), y =y(t) and z =z(u) are smooth with nowhere vanishing derivatives.
X
Y
Z
S3
Figure 2. The link L in S3
We deﬁne the characteristic map gL : T 3→ S2 in terms of the Grassmann map
G : Conf3S3→ G2R4 and the projection π+ : G2R4→S2 by the formula
gL(s,t,u ) = π+(G(x(s),y (t),z (u)).
In other wordsgL is the composition π+GeL whereeL :T 3→ G2R4 is the embedding that
parametrizes the link, given by eL(s,t,u ) = ( x(s),y (t),z (u)). We regard gL as a natural
generalization of the Gauss map T 2→S2 associated with a two-component link in R3.
It is clear that the homotopy class of gL is unchanged under reparametrization of L, or
more generally under any link homotopy of L. Furthermore, gL is “symmetric” in that
it transforms under any permutation of the components of L by precomposing with the
corresponding permutation automorphism ofT 3 multiplied by the sign of the permutation.
Statement of results
The ﬁrst of our two main results gives an explicit correspondence between the Milnor
link homotopy invariants of a three-component ordered, oriented link in the 3-sphere and
the Pontryagin homotopy invariants of its characteristic map.
Theorem A. Let L be a 3-component link in S3. Then the pairwise linking
numbers p, q and r of L are equal to the degrees of its characteristic map
gL : T 3→ S2 on the two-dimensional coordinate subtori of T 3, while twice
Milnor’sµ-invariant for L is equal to Pontryagin’s ν-invariant for gL modulo
2 gcd(p,q,r ).
3
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
Conventions. (1) In this paper, links inS3 are always ordered(the components are taken
in a speciﬁc order) and oriented (each component is oriented).
(2) The two-dimensional coordinate subtori ofT 3 are oriented to have positive intersection
with the remaining circle factors.
The key idea of the proof centers on the “delta move”, a higher order variant of a
crossing change. Applied to a three-component link L in the 3-sphere, we show easily that
this move increases Milnor’s µ-invariant by 1, and then the bulk of the proof is devoted
to showing that it increases Pontryagin’s ν-invariant by 2.
The background material for the proof is contained in Sections 2 and 3 of the paper.
In particular, in Section 2 we discuss how to compute Milnor’s µ-invariant, describe the
delta move, and prove that it increases the µ-invariant by 1. In Section 3, we discuss
Pontryagin’s homotopy classiﬁcation of maps from a 3-manifold to the 2-sphere in terms
of framed bordism of framed links, deﬁne the “Pontryagin link” of such a map to be the
inverse image of any regular value, and then show how to convert the relative ν-invariant
to an absolute one when the manifold is the 3-torus. This section concludes with a simple
procedure for computing the absoluteν-invariant of any map of the 3-torus to the 2-sphere
from a diagram of its Pontryagin link.
The proof of Theorem A will occupy us in Sections 4–6, and is organized as follows.
In Section 4, we derive an explicit formula for the characteristic map gL needed for
the proof of Theorem B, but not for that of Theorem A. We then describe an alternative
asymmetric form hL of the characteristic map that is more convenient for the proof of
Theorem A, and that, just as for gL, depends a priori on the choice of a projection to the
2-sphere. We show that the two characteristic maps are homotopic to one another, and
that, up to homotopy, neither in fact depends on the choice of projection. We note a close
relation between hL and the classical Gauss maps of two-component links in 3-space, and
use this, together with the symmetry of gL, to prove the ﬁrst statement in Theorem A.
In Section 5, we set up for the proof of the rest of Theorem A by describing the standard
open-book structure on S3 with disk pages, use a link homotopy to move a given link L
into “generic position” with respect to it, and then show how to explicitly visualize the
Pontryagin link of the corresponding asymmetric characteristic map hL. Finally, we use
the results of Section 3 to develop a method for computing ν(hL) =ν(gL).
In Section 6, we complete the proof of Theorem A by induction, using the methods
developed in Sections 2 and 3 to ﬁrst conﬁrm the “base case”, and then using the meth-
ods of Section 5 to carry out the inductive step, showing that the delta move increases
Pontryagin’sν-invariant by 2.
Section 7 contains a sketch of a more algebraic proof of this theorem using the group
of link homotopy classes of three-component string links and the fundamental groups of
spaces of maps of the 2-torus to the 2-sphere. More details for this alternative proof can
be found in our announcement [2008], which is otherwise an abridged version of some of
the material in the current paper.
In Sections 8 and 9, we investigate the special case when the pairwise linking numbers
p,q andr ofL are all zero, and so theµ andν-invariants are ordinary integers. In this case
we will use J. H. C. Whitehead’s integral formula for the Hopf invariant, adapted to maps
4
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
of the 3-torus to the 2-sphere, together with a formula for the fundamental solution of the
scalar Laplacian on the 3-torus as a Fourier series in three variables, to provide an explicit
integral formula for ν(gL), and hence for µ(L) in light of Theorem A. See Theorem B,
stated below.
This formula will be presented in three versions: ﬁrst as an integral involving diﬀerential
forms on the 3-torus, second as the same integral expressed in terms of vector ﬁelds, and
ﬁnally as an inﬁnite sum involving Fourier coeﬃcients.
To state these formulas, we need some deﬁnitions. Let ω denote the Euclidean area
2-form onS2, normalized to have total area 1. Then ω pulls back under the characteristic
map gL to a closed 2-form ωL on T 3, which can be converted to a divergence-free vector
ﬁeld
⇀
vL on T 3 via the usual formula
ωL(
⇀
a,
⇀
b) = (
⇀
a×
⇀
b)·
⇀
vL.
We call ωL the characteristic 2-form of L, and
⇀
vL its characteristic vector ﬁeld .
When p, q and r are all zero, ωL is exact and
⇀
vL is in the image of curl. In Section 8 we
give explicit formulas for ωL and
⇀
vL, and in Section 9 for the fundamental solution ϕ of
the scalar Laplacian on T 3, which appear in the integral formulas for µ(L).
For the third version of our formula for the Milnor invariant, we need to express the
characteristic 2-form and vector ﬁeld in terms of Fourier series on the 3-torus. To that
end, view T 3 as the quotient ( R/2πZ)3 and write x = (s,t,u )∈ R3 for a general point
there. Using the complex form of Fourier series, express
ωL =
∑
n∈Z3
(
cs
ndt∧du +ct
ndu∧ds +cu
nds∧dt
)
ein·x.
Using vector notation cn = (cs
n,ct
n,cu
n) , dx = ( ds,dt,du ) , ∂x = (∂/∂s,∂/∂t,∂/∂u )
and ⋆dx = ( dt∧du,du∧ds,ds∧dt) , the formulas for ωL and
⇀
vL become
ωL =
∑
n∈ Z3
cnein·x
· ⋆dx and
⇀
vL =
∑
n∈ Z3
cnein·x
·∂x.
As a consequence of the assumption that the pairwise linking numbers of L vanish, the
coeﬃcient c0 is the zero vector, which will imply that ωL is exact, or equivalently that
⇀
vL
is in the image of curl.
Theorem B. If the pairwise linking numbers of a three-component link L inS3
are all zero, then Milnor’s µ-invariant of L is given by each of the following
equivalent formulas
µ(L) = 1 /2
∫
T 3
δ(ϕ∗ωL)∧ωL (1)
= 1 /2
∫
T 3×T 3
⇀
v L(x)×
⇀
v L(y)·∇yϕ(x− y) dxdy (2)
= 8 π3∑
n⁄=0
an× bn· n/|n|2 . (3)
where ϕ is the fundamental solution of the scalar Laplacian on the 3-torus,
ωL and
⇀
v L are the characteristic form and vector ﬁeld of L, and an and bn
are the real and imaginary parts of the Fourier coeﬃcients cn of ωL and
⇀
v L.
5
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
Explanation of the notation. In (1), δ is the exterior co-derivative and ϕ∗ωL is the
convolution of ϕ with ωL, discussed in detail in Sections 8 and 9.
In (2), the diﬀerence x−y is taken in the abelian group structure on T 3, the expression
∇yϕ(x− y) indicates the gradient with respect to y while x is held ﬁxed, and dx anddy
are volume elements onT 3. This formula is just the vector ﬁeld version of (1) in which the
integral hidden in the convolution is expressed openly; we will see below that it represents
the “helicity” of the vector ﬁeld
⇀
vL on T 3.
Observe that the integrands in (1) and (2) are invariant under the group SO(4) of
orientation-preserving rigid motions of S3, attesting to the naturality of the formulas.
Background and Motivation
Conﬁguration spaces. To study the linking of simple closed curves in a 3-manifold
M from the perspective of homotopy theory, it is convenient to ignore the knotting of
individual components and focus on the relation of link homotopy. For some background
on this notion, see Milnor [1954, 1957] and, for example, Massey [1969], Casson [1975],
Turaev [1976], Porter [1980], Fenn [1983], Orr [1989], Cochran [1990], and Habegger and
Lin [1990].
Conﬁguration spaces come into the picture as follows. Let L be an ordered, oriented
link in M withn componentsX,Y,... parametrized by x =x(s),y =y(t),... fors,t,...
in S1. Then consider the evaluation map
eL :Tn −→ ConfnM , (s,t,... )↦−→(x,y,... )
from the n-torus Tn = S1×···× S1 to the conﬁguration space Conf nM of ordered
n-tuples of distinct points in M. Since link homotopies of L become homotopies of eL,
the assignment L↦→ eL induces a map from the set Ln(M) of link homotopy classes of
n-component links in M to the set [Tn, ConfnM] of homotopy classes of maps from Tn to
ConfnM,
e :Ln(M) −→ [Tn, ConfnM].
We can think of the map e as deﬁning a representation from the world of link homotopy
to the world of homotopy, and the basic question is whether or not this representation is
faithful, that is, one-to-one.
For two-component links in R3, the representation e is faithful. The set L2(R3) is in
one-to-one correspondence with the integers via the classical linking number, while the
set [T 2, Conf2R3] is also in one-to-one correspondence with the integers via the Brouwer
degree, since Conf 2R3 deformation retracts to S2. The correspondence e is bijective since
the linking number of a two-component link equals the degree of its “Gauss map”
T 2 −→ S2 , (s,t )↦−→ y−x
|y−x|.
6
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
The proﬁt is the famous integral formula of Gauss [1833],
Lk(X,Y ) = 1
4π
∫
T 2
dx
ds× dy
dt·
x−y
|x−y|3 dsdt
=
∫
T 2
dx
ds× dy
dt·∇yϕ(y−x) dsdt,
where ϕ(x) = 1 /4π|x| is the fundamental solution of the scalar Laplacian in R3. The
integrand is natural, in the sense that it is invariant under the group of orientation-
preserving rigid motions of R3, acting on the link.
By contrast, for two-component links in S3 the representation e is not faithful. The
conﬁguration space Conf 2S3 has the homotopy type of S3, and hence all maps of T 2 to
Conf2S3 are homotopically trivial. In particular, the analogue of Gauss’s linking integral
in S3, with an integrand which is geometrically natural in the above sense, cannot be
obtained by this route. Nevertheless, such an integral formula was found by DeTurck
and Gluck [2008a] using an alternative route via electrodynamics on the 3-sphere, and
independently by Kuperberg [2008] via the calculus of double forms.
For higher-dimensional two-component links, the same dichotomy holds. In Rn, Scott
[1968] and Massey and Rolfsen [1985] showed that link homotopy classes of links whose
components are copies of Sk and Sn−k−1 are in bijective correspondence with homotopy
classes of maps from Sk×Sn−k−1 to the conﬁguration space Conf 2Rn≃Sn−1, and conse-
quently with πn−1(Sn−1)∼= Z. Finding a geometric linking integral is straightforward, as
the Gauss linking integral and its proof easily generalize to this setting. Shifting the scene
to Sn does not change the link homotopy story, but all maps from Sk×Sn−k−1 to the
conﬁguration space Conf 2Sn≃Sn are homotopically trivial. Geometrically natural link-
ing integrals still exist in this situation, as demonstrated by DeTurck and Gluck [2008b]
and Shonkwiler and Vela-Vick [2011], but ﬁnding them requires new techniques.
Forn-component homotopy Brunnian links in R3 – meaning links that become trivial
up to link homotopy when any single component is removed – and analogous links in
higher dimensions, Koschorke [1997] showed that the representation e is again faithful.
This provided the ﬁrst proof (up to sign) of our Theorem A for the case when the pairwise
linking numbers are zero.
The content of the present paper is that, for arbitrary three-component links L in S3,
the representation e is faithful, and that we are led thereby to a natural integral for
Milnor’s triple linking number when the pairwise linking numbers vanish. The relevant
conﬁguration space Conf 3S3 is easily seen to deformation retract to S3×S2, where the
S3 coordinate records one of the three points in each triple (see Section 4). It follows that
the evaluation map eL :T 3→ Conf3S3 is homotopic to a map of T 3 into an S2 ﬁber, and
this turns out to be, up to homotopy, our characteristic map gL.
Theorem A asserts, among other things, that L and L′ are link homotopic if and only
if gL and gL′ are homotopic, and hence that
e :L3(S3)−→[T 3, Conf3S3]
is faithful. Furthermore, it was observed above that ifh∈ SO(4) is an orientation preserv-
ing isometry ofS3, theneh(L) =h·eL where· is the diagonal action, and so the integrands
7
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
in the formulas for Milnor’s triple linking number µ(L) in Theorem B are invariant under
the action of SO(4).
We emphasize that our Theorems A and B are set speciﬁcally in S3, and that so
far we have been unable to ﬁnd corresponding results in Euclidean space R3 which are
equivariant (for Theorem A) and invariant (for Theorem B) under the noncompact group
of orientation-preserving rigid motions of R3.
Fluid mechanics and plasma physics. The helicity of a vector ﬁeld V deﬁned on
a bounded domain Ω in R3 is given by the formula
Hel(V ) = 1
4π
∫
Ω×Ω
V (x)×V (y)·
x−y
|x−y|3 dxdy
=
∫
Ω×Ω
V (x)×V (y)·∇yϕ(x−y) dxdy.
where, as above, ϕ is the fundamental solution of the scalar Laplacian in R3, and dx and
dy are volume elements.
Woltjer [1958] introduced this notion during his study of the magnetic ﬁeld in the Crab
Nebula, and showed that the helicity of a magnetic ﬁeld remains constant as the ﬁeld
evolves according to the equations of ideal magnetohydrodynamics, and that it provides
a lower bound for the ﬁeld energy during such evolution. The term “helicity” was coined
by Moﬀatt [1969], who also derived the above formula from Woltjer’s original expression.
There is no mistaking the analogy with Gauss’s linking integral, and no surprise that
helicity is a measure of the extent to which the orbits of V wrap and coil around one
another. Since its introduction, helicity has played an important role in astrophysics and
solar physics, and in plasma physics here on earth.
Looking back at Theorem B, we see that the integral in our formula for Milnor’s
µ-invariant of a three-component link L in the 3-sphere expresses the helicity of the asso-
ciated vector ﬁeld
⇀
vL on the 3-torus.
Our study was motivated by a problem proposed by Arnol′d and Khesin [1998] regarding
the search for “higher helicities” for divergence-free vector ﬁelds. In their own words:
The dream is to deﬁne such a hierarchy of invariants for generic vector
ﬁelds such that, whereas all the invariants of order ≤ k have zero value
for a given ﬁeld and there exists a nonzero invariant of order k + 1, this
nonzero invariant provides a lower bound for the ﬁeld energy.
Since the helicity integral above is analogous to the Gauss linking integral, the general
hope is that higher helicities will be analogous to higher order linking invariants. But the
anti-symmetry of Milnor’s triple linking number appears to be an impediment to naively
generalizing it to a second order helicity for vector ﬁelds, and suggests that attention be
directed to yet higher order link homotopy and concordance invariants.
The formulation in Theorems A and B has led to partial results that address the case
of vector ﬁelds on invariant domains such as ﬂux tubes modeled on the Borromean rings;
see Komendarczyk [2009, 2010].
8
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
Other integral formulas. Previous integral formulas for Milnor’s triple linking num-
ber and attempts to deﬁne a higher order helicity can be found in the work of Massey [1958,
1969], Monastyrsky and Retakh [1986], Berger [1990, 1991], Guadagnini, Martellini and
Mintchev [1990], Evans and Berger [1992], Akhmetiev and Ruzmaiken [1994, 1995], Arnol′d
and Khesin [1998], Laurence and Stredulinsky [2000], Leal [2002], Hornig and Mayer [2002],
Rivi` ere [2002], Khesin [2003], Bodecker and Hornig [2004], Auckly and Kapitanski [2005],
Akhmetiev [2005], and Leal and Pineda [2008].
The principal sources for these formulas are Massey triple products in cohomology,
quantum ﬁeld theory in general, and Chern–Simons theory in particular. A common
feature of these integral formulas is that choices must be made to ﬁx the domain of
integration and the value of the integrand.
Acknowledgements. We are grateful to Fred Cohen and Jim Stasheﬀ for their substan-
tial input and help during the preparation of this paper, and to Toshitake Kohno, whose
2002 paper provided one of the inspirations for this work. Komendarczyk and Shonkwiler
also acknowledge support from DARPA grant #FA9550-08-1-0386, and Vela-Vick from an
NSF postdoctoral fellowship.
The Borromean rings shown on the ﬁrst page are from a panel in the carved walnut
doors of the Church of San Sigismondo in Cremona, Italy. The photograph is courtesy of
Peter Cromwell.
2. The Milnor µ-invariant
Let L be a three-component link in either R3 or S3, with oriented components X, Y
and Z, and pairwise linking numbers p, q and r. Milnor’s original deﬁnition of the triple
linking number µ(L), typically denoted ¯µ123(L), was algebraic. The formulation in his
PhD thesis [1957] is expressed in terms of the lower central series of the link group G, the
fundamental group of the complement of L, as follows.
Choose based meridians for the link components X,Y andZ, and letx,y andz denote
the corresponding elements of G. In general, these three elements do not generate G, but
they do generate the quotient of G by the third term [[G,G ],G ] in its lower central series.
In this quotient group, the longitude of Z can be written as a word w in x, y and z and
their inverses. Assign an integer mxy(w) to this word that counts with signs the number
of times that x appears before y in w, allowing intervening letters. More precisely, each
appearance of x··· y or x−1··· y−1 contributes +1 to mxy(w), while x··· y−1 or x−1··· y
contributes−1. Then µ(L) is the element of Zgcd(p,q,r) deﬁned by
µ(L) = mxy(w) mod gcd(p,q,r ).
There is a geometric reformulation of this deﬁnition, found by Mellor and Melvin [2003],
that is more convenient for our purposes: choose Seifert surfaces FX, FY and FZ for the
components of L, and move these into general position. Starting at any point on X,
record its intersection with the Seifert surfaces for Y andZ by a wordwX iny andz. For
example a y or y−1 in wX indicates a positive or negative intersection point of X with
FY . Set mX =myz(wX), where the right hand side is computed as in the last paragraph,
and similarly set mY =mzx(wY ) and mZ =mxy(wZ). Finally, let t be the signed count
of the number of triple points of intersection of the three Seifert surfaces. Then
µ(L) = mX +mY +mZ−t mod gcd(p,q,r ).
9
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
It follows from this formula that µ(L) is invariant under even permutations of the com-
ponents of L, but changes sign under odd permutations. This is a well known property of
Milnor’s triple linking number.
We give two sample calculations of the triple linking number, using this geometric
formulation, that will feature in our inductive proof of Theorem A in Section 6.
Example 2.1. LetLpqr be the link shown in Figure 3, with components X,Y andZ and
with pairwise linking numbers p, q and r. Choose the Seifert surfaces FX, FY and FZ to
be the obvious disks, essentially lying in the page, bounded by X, Y and Z.
X
Y Z
rq
p
Figure 3. The base link Lpqr for p = 5, q = 3, r =−2
Starting at appropriate points on the link components, we can read oﬀ the words
wX =yrzq , wY =zpxr and wZ =xqyp.
Thus mX =qr, mY =rp and mZ =pq. Furthermore, it is clear that there are no triple
points of intersection of the three disks. Therefore
µ(Lpqr) = qr +rp +pq− 0 = 0 ∈ Zgcd(p,q,r).
The links Lpqr will serve as the base links for our proof of Theorem A.
Example 2.2. Consider the delta move shown in Figure 4, transforming the link L on
the left to the link ˆL on the right.
X ˆX
Y ˆY
Z ˆZ
Figure 4. The delta move L→ˆL
10
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
This move takes place within a 3-ball, outside of which the link is left ﬁxed. It does not
alter the pairwise linking numbers of L, and may be thought of as a higher order variant
of a crossing change.
The delta move was introduced by Matveev [1987]. It was shown by Murakami and
Nakanishi [1989] that a suitable sequence of such moves can transform any link into any
other link with the same number of components and the same pairwise linking numbers.
In particular, the base linkLpqr above can be transformed into any other three-component
link with pairwise linking numbers p,q andr by a sequence of delta moves. The inductive
step of our proof of Theorem A will be based on this observation, and so we determine
right now the eﬀect of the delta move on the µ-invariant.
If the three arcs involved in the delta move do not come from three distinct components
of the link L, then the change can be achieved by a link homotopy, and hence neither
Milnor’s µ-invariant nor Pontryagin’sν-invariant forgL will change.
But if the arcs do come from three distinct components of L as shown in the ﬁgure,
then µ increases by 1, that is µ(ˆL) = µ(L) + 1. This can be seen as follows, using the
geometric formula for the µ-invariant.
In Figure 5, we display on the left fragments of the Seifert surfaces FX, FY and FZ
before the delta move, while on the right, after the delta move, each old surface is enlarged
a bit to provide new surfaces F ˆX, F ˆY and F ˆZ.
FX FY
FZ
F ˆX F ˆY
F ˆZ
Figure 5. A negative triple point appears
On the left, the three surface fragments are disjoint, while on the right, after their
enlargement, they are not. Where these surfaces now come together, we have an additional
isolated triple point, and since the normals to the surfaces at this point form a left-handed
frame, this triple point gets a minus sign. Thus t drops by 1. We also see that after
the delta move, the curve ˆZ has two extra intersections with F ˆY , the ﬁrst positive and
the second negative, and no extra intersections with F ˆX. Since these new intersection
points are adjacent along the curve, and of opposite signs, it follows that the new count
m ˆZ =mxy(w ˆZ) is equal to the old one mZ. Similarly m ˆX =mX and m ˆY =mY . Hence
µ =mX +mY +mZ−t increases by 1, as claimed.
The heart of the proof of Theorem A will be to show that application of the delta move
increases Pontryagin’sν-invariant by 2.
11
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
3. The Pontryagin ν-invariant
Heinz Hopf proved in 1931 that homotopy classes of maps from the 3-sphere to the
2-sphere are in one-to-one correspondence with the integers via his now famous Hopf
invariant. Pontryagin [1941] generalized this to give the homotopy classiﬁcation for maps
from an arbitrary ﬁnite 3-complex to the 2-sphere. It is convenient for our purposes to
restrict to smooth maps from 3-manifolds to the 2-sphere, and to use Poincar´ e duality
to take Pontryagin’s result, originally presented via cohomology, and reformulate it in
homological terms.
Deﬁnition and properties
Fix a closed oriented smooth 3-manifold M. The homotopy classiﬁcation of maps
f :M→S2 can be expressed using two diﬀerential topological invariants.
The primary invariant
λ(f) ∈ H1(M) (with integral coeﬃcients understood)
records the homology class of the preimage link L = f−1(∗) of any regular value ∗ of f
(oriented as explained below), or equivalently the Poincar´ e dual of the pull-backf∗(ω) of
the orientation classω∈H2(S2). It is easily shown that two maps have the same primary
invariant if and only if they induce the same map on homology.
The secondary invariant
ν(f0,f 1) ∈ Z2d(λ)
compares two maps f0 and f1 with the same primary invariant λ. Here d(λ) is the
divisibility of λ as an element of the free abelian group H1(M)/torsion. Thus d(λ) = 0 if
λ is of ﬁnite order, and otherwise d(λ) is the largest positive integer d for which λ = dκ
for some κ∈H1(M).
For example, if M is the 3-torus T 3, then λ(f) = (p,q,r )∈ H1(T 3)∼= Z3 where p, q
andr are the degrees of f restricted to the coordinate 2-tori, and the divisibility d(p,q,r )
is the greatest common divisor of p, q and r.
In the next few paragraphs, we discuss these invariants λ and ν in more detail, and
provide a natural way, in the special case that M is the 3-torus, to transform ν from a
relative invariant into an absolute one, meaning a function of a single map.
First recall that a framing of a smooth link in M is a homotopy class of trivializations
of the normal bundle of the link. It can be represented by an orthonormal triple ( u, v, t)
of vector ﬁelds along the link with respect to some Riemannian metric on M, where t is
tangent to the link. We can use this to orient the link by t by insisting that the triple give
the orientation on M. Conversely, if the link is already oriented by t, then the framing
can be speciﬁed by a single unit normal vector ﬁeld u, as v is then determined by the
condition that (u, v, t) be an orthonormal frame giving the orientation on M. In pictures,
therefore, we often indicate a framing on an oriented link by simply drawing a thin parallel
push-oﬀ of the link, recording the tips of the vectors in u.
Now given a map f :M→S2 with regular value∗, the linkL =f−1(∗)⊂M inherits
a framing by pulling back an oriented basis for the tangent space to S2 at∗, and acquires
12
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
an orientation from this framing, as above. Equipped with this framing and orientation,
L will be called the Pontryagin link of f at∗.
Note that any framed oriented link L in M arises as the Pontryagin link of some map
from M to S2. In particular, the Pontryagin–Thom construction produces such a
map, given by wrapping each normal disk ﬁber of a tubular neighborhood ofL around the
2-sphere by the exponential map, using the framing to identify the ﬁber with the disk of
radiusπ in the tangent space toS2 at∗, and sending everything outside the neighborhood
to the antipode of ∗. This construction provides a one-to-one correspondence
[M,S 2] ←→ Ωfr
1 (M)
where [M,S 2] is the set of homotopy classes of maps M→ S2, and Ω fr
1 (M) is the set of
framed bordism classes of framed oriented links inM (see e.g. Chapter 7 in Milnor [1965]).
Now we return to our discussion of the invariants associated with maps f :M→S2.
An easy argument shows that the primary invariant λ(f), the homology class of the
oriented link f−1(∗), is independent of the choice of regular value ∗, and that λ(f) is
invariant under homotopies of f. Indeed, the preimages L0 andL1 of any regular values
for any pair of maps homotopic to f are bordant in M× [0, 1] (see Milnor [1965] for a
proof). It follows thatL0 andL1 are homologous inM. Conversely, homologous links inM
are bordant in M× [0, 1] by a standard argument going back to Thom [1954]. This shows
that the partition of [ M,S 2] into subsets [M,S 2]λ according to their primary invariants
λ∈H1(M) corresponds to the partition of Ω fr
1M into unframed bordism classes.
The secondary invariant associated with a pair of bordant framed links measures the
obstruction to extending the framings on the links across any bordism between them. More
precisely, given f0 and f1 in [M,S 2]λ with Pontryagin links L0 andL1, and an oriented
surfaceF⊂ M× [0, 1] with ∂F =L1× 1−L 0× 0, the framings onL0 andL1 combine to
give a normal framing ofF along its boundary. The obstruction to extending this framing
acrossF is measured by its relative Euler class e(F) in H2(F,∂F;π1SO(2)) = Z, which
in homological terms is the intersection number of F with a generic perturbation of itself
that is directed by the given framings along ∂F. This class depends on the choice of the
regular values of f0 and f1 used to deﬁne the Pontryagin links, and on the choice of the
bordismF between the links. But the residue class of e(F) mod 2d(λ) does not depend
on these choices; see Gompf [1998] and Cencelj, Repovˇ s and Skopenkov [2007] for details,
and also see Auckly and Kapitanksi [2005]. This residue class
ν(f0,f 1) = e(F) mod 2d(λ) ∈ Z2d(λ)
will be referred to as the relative Pontryagin ν-invariant of f0 and f1.
Converting the relative Pontryagin ν-invariant into an absolute invariant
The task of converting ν into an absolute invariant, that is, changing it from a function
of two variables to a function of one variable, requires the choice of a base map fλ in
each subset [M,S 2]λ of homotopy classes of maps with primary invariantλ. One can then
deﬁne the absolute Pontryagin ν-invariant by
ν(f) = ν(f,fλ)
for any f∈ [M,S 2]λ. Whether such choices can be made in a topologically meaningful
way depends on the manifold M.
13
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
For example, Pontryagin [1941, page 356] explicitly cautioned against trying to make
this choice when M =S1×S2. In this case there are, up to homotopy, exactly two maps
toS2 with primary invariant 1∈H1(S1×S2) = Z, meaning degree 1 on the cross-sectional
2-spheres in S1×S2. One of these is the projection f0(θ,x ) =x to the S2 factor, and the
other is the twist map f1(θ,x ) = rotθ(x) that rotates the S2 factor once while traversing
the S1 factor; here rotθ indicates rotation of S2 through an angle θ about its polar axis.
Note that the double twist f2(θ,x ) = rot2θ(x) is homotopic to f0.
What Pontryagin observed is thatf0 andf1 diﬀer by an automorphism ofS1×S2, and so
there is no natural way to choose which one should serve as the base map for the homology
class [S1×S2,S 2]1. More precisely, the automorphism h given by h(θ,x ) = (θ, rotθ(x))
satisﬁes f0h = f1, while f1h = f2, which is homotopic to f0. Thus the maps f0 and f1
have equal topological status, and so neither is more basic than the other.
A key feature of this example is the existence of a homotopically nontrivial automor-
phism of S1×S2 that induces the identity on homology. In general, if a 3-manifold M
supports such an automorphism h, then λ(fh) = λ(f) for any map f : M→ S2. Hence
the existence of h provides a potential obstruction to the natural choice of base maps in
[M,S 2]λ for allλ. The 3-torus has no such automorphisms, due to the fact that its higher
homotopy groups vanish.
For each triple of integers p, q and r, we now show how to pick out a speciﬁc map
fpqr : T 3 → S2 having these preassigned cross-sectional degrees, which can serve in a
topologically meaningful way as the base map for the set [ T 3,S 2](p,q,r) of all such maps.
We will describe fpqr by specifying its Pontryagin link Lpqr, as follows. Choose three
pairwise disjoint circlesCs,Ct andCu that are cosets of the coordinate circle subgroups
S1
s =S1× 0× 0 , S1
t = 0×S1× 0 and S1
u = 0× 0×S1
of the 3-torus (where as usual S1 = R/2πZ) with disjoint tubular neighborhoods Ns,
Nt andNu. Equip these circles with their coordinate framings induced from the Lie
framing (∂s,∂t,∂u) of the tangent bundle of T 3, that is, (∂t,∂u) forCs, (∂u,∂s) forCt and
(∂s,∂t) forCu. Then construct Lpqr fromp parallel copies ofCs inNs (meaningp distinct
cosets of S1
s lying in Ns), q copies of Ct inNt and r copies of Cu inNu, all with their
coordinate framings, as indicated in Figure 6. Thus fpqr wraps the disk ﬁbers of the tubes
Ns,Nt andNu around S2 by maps of degree p, q and r, and is constant elsewhere.
s
u
tp
q
r
Figure 6. Pontryagin linkLpqr for the base map fpqr
14
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
Here and below, the 3-torus is pictured as the cube [0 , 2π]3 in stu-space with opposite
faces identiﬁed. The axes correspond to the coordinate circles S1
s, S1
t and S1
u, and the
coordinate framings are the “blackboard” framings, i.e. those given by parallel push-oﬀs
in the projection shown. The linkL5 3−2 is shown in the ﬁgure. Note that by construction
L000 is empty, so f000 is constant.
Computing the absolute Pontryagin ν-invariant
Our goal is to give a simple procedure for computing the Pontryagin ν-invariant of a
map f :T 3→S2 from a “toral diagram” of its Pontryagin link L.
By deﬁnition, a toral diagram ofL consists of
(1) a classical oriented link diagram D in the 2-torus T 2 with crossingsC,
(2) a ﬁnite set of signed points in T 2, the marked points, partitioned into the
isolated onesM⊂ T 2−D , and the internal onesN⊂D−C , and
(3) integer framings for each component ofD and each point inM.
For example, the link Lpqr above is duplicated in Figure 7(a) with its toral diagram
beneath it, and another example is given in Figure 7(b).
3
2
(a) The linkLpqr and its diagram (b) Another example
Figure 7. Toral diagrams of framed links in T 3
It is understood thatL should project toD∪M under the projection T 3→T 2 sending
(s,t,u ) to (s,t ), and so points in M correspond to vertical components ∗×∗× S1 inL,
oriented up or down according to the signs. The points in N correspond to transverse
intersections ofL with the horizontal 2-torus T 2× 0 – shaded in the ﬁgures – where
the sign +1 or −1 indicates whether the curve points up or down near the intersection.
To explain the crossings C, view T 3 as the cube [0 , 2π]3 in stu-space with opposite
faces identiﬁed, as before, and T 2 as the square [0, 2π]2 in thest-plane with opposite sides
identiﬁed. AboveD−N , the linkL resides inT 2×(0, 2π). At a crossing, the over-crossing
strand is the one with the larger vertical u-coordinate in the cube.
15
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
Finally, the framings specify a push-oﬀ ofL by comparison with the blackboard framing
ofD∪M inT 2. These “blackboard” framings are obtained by pushing D∪M oﬀ itself in
the direction of a normal vector ﬁeld in T 2, and then lifting these push-oﬀs to a collection
of framing curves for the components ofL that we call their 0-framings. For vertical circles,
these are just the coordinate framings. Now the n-framing on any given component of
L is the one obtained from the 0-framing by adding n full twists, right or left handed
according as n is positive or negative.
In these ﬁgures we typically indicate the framing on the link in T 3 by a thin push-oﬀ,
and use the convention that the unlabeled components of the diagram have framing zero,
that is, the blackboard framing. We also denote the positive marked points in the diagram
with solid dots, and the negative ones with hollow dots.
We have allowed isolated marked points in the deﬁnition above so that projections of
links such as Lpqr will qualify as toral diagrams, and to facilitate our later work. Note,
however, that a generic isotopy of L will eliminate the set M of isolated marked points,
converting an n-framed isolated marked point – corresponding to a vertical circle in L –
into a small ( n± 1)-framed circle with one internal marked point – corresponding to a
spiral perturbation of the vertical circle. More precisely, using the notation above of solid
dots for positive marked points and hollow dots for negative ones, we have
= =n n− 1 n + 1
and = =n n + 1 n− 1
as is readily veriﬁed by a suitable picture in the 3-torus.
Now suppose we are given a toral diagram of a Pontryagin linkL for a mapf :T 3→S2.
We say that the diagram representsf, and seek to compute ν(f) from it.
First observe that the primary invariant
λ(f) = ( p,q,r )
is easily read from the diagram. Indeed p and q (which are the degrees of the projections
ofL to the horizontal circle factors S1
s and S1
t ) are just the intersection numbers of D
with S1
t and−S1
s, and r (the degree of the projection of L to the vertical circle S1
u , or
equivalently the intersection number of L with the horizontal 2-torus) is the sum of the
signs of all the marked points. We call p and q the horizontal winding numbers of
the diagram, and r its vertical winding number . For what follows, we will also need
to consider the vertical winding of the individual components of L. Each such component
Li projects either to some subset Di ofD, or to a point Mi inM (ifLi is vertical). In
either case, we call this projected image the “ith component” of the diagram, and write ri
for the sum of all the marked points that lie on it. Clearly ri is just the vertical winding
number ofLi, and∑ri =r, the total vertical winding number of the diagram.
To computeν(f), we will transformL by a sequence of framed bordisms intoLpqr with
some extra twists in the framing. The number of twists is by deﬁnitionν(f); counting these
twists ultimately yields the simple formula for ν(f) that will be given in Proposition 3.1.
To cleanly state this formula, we assume from the outset that our diagram has no
crossings. There is no loss of generality in doing so since the crossings can be eliminated
by saddle bordisms ofL, as illustrated in Figure 8 (viewingL from the top, looking down
on a crossing in the horizontal torus) which of course do not change ν(f). Furthermore,
16
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
we will see that the Pontryagin link of a “generic link” (to be deﬁned in Section 5), has a
toral diagram without crossings.
∼
bordism
=
Figure 8. Using saddles to eliminate crossings
Each such saddle bordism is achieved by adding a 1-handle, as indicated on the left side
of Figure 9, and drawn in full, suppressing one dimension in T 3, on the right side.
Figure 9. The saddle bordism
The eﬀect of the saddle bordism on the diagram is easy to describe. If it is used to
eliminate a self-crossing of an ni-framed componentDi (meaningDi is the projection of
a component Li ofL) thenDi splits into two components whose framings must add up
to ni± 1, depending on the sign of the crossing. Beyond this condition, the framings on
the new components can be chosen arbitrarily since twists in the original framing can be
shifted along Li at will. If the saddle bordism is used to eliminate a crossing between
distinct componentsDi andDj ofD with framings ni and nj, then the result is a single
component with framing ni +nj± 1.
Once we have a toral diagram without crossings representingf, the extra data needed
to compute ν(f) is the list of vertical winding numbers ri of its components together
with one additional integer n =∑ni, the sum of all the component framings ni, which
we call the total framing and place as a label next to the diagram.
To state the formula eﬃciently, we will use one more list of numbers that is easily read
from the diagram. First pick a basepoint ∗ in T 2 away fromD∪M , and then for each i,
choose an arc γi that runs from the ith component ofD∪M to∗. Now deﬁne the depth
of the ith component to be
di = 2 γi·D mod 2 gcd(p,q,r ),
that is, twice the intersection number in T 2 of the arc γi with the union D of the closed
curves in the diagram. This intersection number must be properly interpreted for compo-
nents ofD. In this case the initial point of γi lies onD, contributing± 1
2 to the intersection
number, and thus ±1 to di. It follows that di is always an odd integer for components
ofD, and an even integer for components of M, meaning isolated marked points. An
example is shown in Figure 10.
17
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
∗
Di
γi
Mj
γjdi = 2· 2 1
2 = 5
dj = 2·− 1 =−2
Figure 10. Depths of components in the diagram
Of course the depthdi depends on the choice of arc γi, but only modulo 2 gcd(p,q ), and
so it is certainly well deﬁned modulo 2 gcd( p,q,r ). Furthermore, in the formula for ν(f)
below, the depths appear only as coeﬃcients in the sum ∑diri. It is readily seen that
this sum changes by a multiple of ∑ 2ri = 2r when moving the basepoint ∗, and so it is
well deﬁned modulo 2 gcd(p,q,r ), independent of the choices of ∗ and of the arcs γi.
We can now state the main result of this section.
Proposition 3.1. Let f : T 3 → S2 be a smooth map whose Pontryagin link
L is represented by a toral diagram in T 2 without crossings, with horizontal
winding numbers p and q, vertical winding number r, and total framing n.
Then the primary and secondary Pontryagin invariants of f are given by
λ(f) = ( p,q,r ) and
ν(f) = n +pq +∑diri mod 2 gcd(p,q,r )
whereri and di are the vertical winding numbers and depths (with respect to
any chosen basepoint) of the components of the diagram.
Proof. The formula for λ(f) was derived on page 16, and the formula for ν(f) is, as
explained above, at least well deﬁned modulo 2 gcd( p,q,r ), independent of the choice of
basepoint. So it remains to verify that this is the correct formula for ν(f).
First observe that, in the absence of crossings, the integers ri are all that are needed to
recover the link L up to isotopy. In particular, each nonvertical component of L can be
taken to wind monotonically around the last circle factor of T 3. Furthermore, equipped
with the total framing n, we can recover the framed link L up to framed bordism . To see
this, note that a pair of saddle bordisms can be used as shown in Figure 11 to transfer a
twist in the framing from any component of L to any other, and so we can distribute the
framings in any desired way among the components.
We now propose to transformL by a sequence of framed bordisms into Lpqr with some
extra twists in the framing. These correspond to homotopies off and so do not change the
Pontryagin invariantν(f). We will carry this out on a diagrammatic level, transforming
our given toral diagram, with total framingn, to the diagram forLpqr shown in Figure 7(a)
with some total framing, which by deﬁnition will equalν(f). So we must simply keep track
of the change in the total framing as we proceed.
18
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
∼ = ∼
Figure 11. Using saddles to transfer twists
We ﬁrst use saddle bordisms to replace the vertical winding of each non-vertical com-
ponentLi by|ri| zero-framed vertical components, at the cost of adding ri to the total
framing. The new vertical circles are “adjacent” to Di – meaning displaced slightly to the
right of it in the projection – and oriented up or down according to the sign of ri.
This is illustrated in Figure 12. The net eﬀect on the diagram is to reduce all the
vertical winding numbers to zero on the components of D (i.e. to eliminate the internal
marked points N ), to add ∑|rj| isolated marked points, and to add ∑rj to the total
framing of the diagram, where the sums are only over the non-vertical components of L.
∼
n n + 1
Figure 12. Using saddles to replace vertical winding by vertical circles
Since our target is the base link Lpqr (with extra twists), the vertical circles must be
gathered together. This is the purpose of our base point ∗, which will serve as a gathering
spot, and the arcs γi, which will serve as the paths in T 2 along which to move the vertical
circles which at the moment are adjacent to the Li. At each intersection of γi with a
component of D, these vertical circles must cross the corresponding strand of L. This
crossing can be accomplished by a pair of saddle bordisms as indicated in Figure 13,
adding±2 to the diagram framing. On the diagrammatic level, this can viewed as a two
step process, running the bordism shown in Figure 12 backwards and then forwards, in
order to move an isolated marked point across a component ofD, as shown at the bottom
of the ﬁgure.
Now it is easy to check that the act of removing the vertical winding of the nonvertical
components ofL, and then gathering all the resulting vertical circles (including the original
ones corresponding to M) will add ∑diri to the total framing of the diagram. Visually,
19
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
∼ ∼
n− 1 n n + 1
Figure 13. Using saddles to gather the vertical circles
this process can be thought of as a “migration” to the base point of all the marked points
in the diagram.
Next use disk bordisms to remove the null homotopic components of D (arranging for
them to be 0-framed by storing their twists elsewhere, as explained above) and similarly
use annular bordisms to remove any pair of curves that are parallel but oppositely oriented.
The diagram now consists of a ( p,q ) torus link in T 2 (meaning c parallel copies of the
(p′,q′) torus knot, where p =cp′ andq =cq′ withp′ andq′ relatively prime) together with
r isolated marked points near ∗. The total framing, which was originally equal to n, has
changed to n +∑diri.
Finally we transform the (p,q ) torus link by using saddle bordisms (reversing the process
described above for removing crossings) into p copies of S1
s andq copies of S1
t , grouped as
inLpqr, at the cost of addingpq to the total framing. Thus we have arrived atLpqr, having
changed the total framing from n to n +pq +∑diri. This veriﬁes the stated formula for
ν(f), and completes the proof of Proposition 3.1. □
The following application will arise in the proof of Theorem A in Section 6.
Example 3.2. If f is represented by the ±(pq +r)-framed (p,q ) torus link in T 2, with
one component K of vertical winding number r, and the rest of vertical winding number
zero, then λ(f) = (p,q,r ), and choosing a base point adjacent to K,
ν(f) = ( pq +r) +pq + (1·r + 0 + 0) = 2( pq +r) = 0 ∈ Z2 gcd(p,q,r).
