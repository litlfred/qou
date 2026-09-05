---
doc_id: arxiv-math-0505056v2
doc_title: "Matrix factorizations and link homology II"
section_id: sec-000-matrix-factorizations-with-a-parameter
section_title: "Matrix factorizations with a parameter"
section_number: null
pages: 1-12
source_pdf: 0505056v2.pdf
source_sha256: 1b6580406c3d35b5
doc_brief: "Matrix factorizations and link homology II — To a presentation of an oriented link as the closure of a braid we assign a complex of bigraded vector spaces."
---
In the paper [KR] we constructed, for each n > 0, a bigraded cohomology
theory of links in R3 whose Euler characteristic is a certain one-variable
specialization (qn,q ) of the HOMFLYPT polynomial [HOMFLY], [PT]. The
n = 0 specialization is the Alexander polynomial, equal to the Euler char-
acteristic of the knot homology theory discovered by Ozsv´ ath, R asmussen
and Szab´ o [OS], [R1]. The approach in [KR] fails for n = 0, assigning trivial
groups to any link.
In this sequel to [KR] we assume that the reader is familiar with that
paper. Recall that our construction of link cohomology was based o n matrix
factorizations with potentials being sums and diﬀerences of xn+1, for various
x. When n = 0, the category of matrix factorizations (up to chain homo-
topies) with the potential ∑ ±xi is trivial. Looking for a remedy, let us add
a formal variable a and change the potential from x to ax.
Take an oriented arc c as in ﬁgure 1, label its ends x1 and x2, and assign
the potential ax1 −ax2 to the arc. Let R = Q[a,x 1,x 2] and deﬁne Cc as the
factorization
R
a
− →R
x1−x2
− − − →R.
We haved2 =ax1 −ax2 and view Cc as an object of the homotopy category
of matrix factorizations with the potential a(x1 −x2).
1
x 1x 2
c
Figure 1: An arc
x1 x2
x3 x4
Figure 2: Wide edge t
MakeR bigraded by setting
deg(a) = (2, 0), deg(xi) = (0, 2). (1)
This implies deg(d2) = (2, 2) and we select the bigrading of the middle R in
the factorization so that deg( d) = (1, 1):
R
a
− →R{−1, 1}
x1−x2
− →R, (2)
where the bidegree shift by ( n1,n 2) is denoted {n1,n 2}.
Next, given a wide edge t as in ﬁgure 2, assign variables x1,x 2,x 3,x 4 to
the edges next to it. We can write
ax1 +ax2 −ax3 −ax4 =a(x1 +x2 −x3 −x4) + 0(x1x2 −x3x4).
Deﬁne Ct as the tensor product (over R) of factorizations
R
a
− →R{−1, 1}
x1+x2−x3−x4
− − − − − − − − →R (3)
and
R
0
− →R{−1, 3}
x1x2−x3x4
− − − − − − →R (4)
where R = Q[a,x 1,x 2,x 3,x 4].
Throughout the paper we work with matrix factorizations with pote ntials
w =a ∑
iǫixi wherei ranges over some ﬁnite setI of integers andǫi ∈ {1, −1}
are ”orientations” of xi. The category mfw has objects ( M,d ) where M =
2
x i
x ix i
x i x i
x i
M
  0
  0   0
M
  0
  2   2
M
  0
  0   2
M
 1
 1  1
M
  0
  2   4
M
 1
 1  3
M
  0
−2   0
M
 1
−1   1
M
  0
  0   2
x i
x i
x i
d
d
d
d
d
d
d
d
dd
a a
a a
a
a
Figure 3: Lattice of factorization M
M 0 ⊕M 1 andM 0,M 1 are free bigraded R-modules (possibly of inﬁnite rank),
while d is a generalized diﬀerential
M 0 d
− →M 1 d
− →M 0
of bidegree (1, 1) and subject to d2 =w. HereR is the ring of polynomials in
a andxi’s with rational coeﬃcients. The bidegrees are given by formula (1).
Morphisms in mfw are bidegree-preserving maps of R-modules M 0 → N 0,
M 1 →N 1 that commute with d.
We found it useful to visualize a matrix factorization as above by dec om-
posing
M 0 = ⊕
k,l
M 0
k,l, M 1 = ⊕
k,l
M 1
k,l,
as direct sums of vector spaces, one for each bidegree ( k,l ), and placing them
in the nodes of a coordinate lattice, see ﬁgure 3. Diagonal arrows d enote the
diﬀerential, horizontal arrows show multiplication by a and vertical arrows–
multiplications by xi.
The category hmfw of matrix factorizations up to chain homotopies has
the same objects as mfw and the Q-vector space of morphisms from M toN is
the quotient of the space of morphisms in mfw by null-homotopic morphisms
(the homotopy maps must have bidegree ( −1, −1)).
If the index set I is empty, then R = Q[a] and mfw is equivalent to the
category of complexes of free graded Q[a]-modules.
3
t  2
x1
x2
x4
x3
x5
x6
x7
x8
x9
t  1
Figure 4: Graph Γ , an example
In general, given a planar marked graph Γ (as described in [KR, Intro duc-
tion]), possibly with boundary points, we assign to it a matrix factoriz ation
C(Γ) which is the tensor product of Cc, over all arcs c in Γ, and Ct, over all
wide edges t in Γ. For instance, for the graph in ﬁgure 4,
C(Γ) = Ct1 ⊗Ct2 ⊗Cc1 ⊗Cc2
wherec1,c 2 are the arcs of Γ with endpoints labelled x3,x 5 andx7,x 6, respec-
tively. The tensor product is taken over suitable polynomial rings Q[a,xi] so
that C(Γ) is a ﬁnite rank free Q[a,x 1,...,x 9]-module. The potential
w =a(x1 +x2 −x7 −x4 −x8 −x9)
and we view C(Γ) as an object of mfw (or hmfw) with the ground ring R
the polynomial ring Q[a,x 1,x 2,x 4,x 7,x 8,x 9] in a and external (or boundary)
variables. The other variables x3,x 5,x 6 are ”internal”. Notice that C(Γ) has
inﬁnite rank as an R-module.
When Γ has no boundary points, w = 0 and C(Γ) becomes a 2-periodic
complex
C 0(Γ)
d
− →C 1(Γ)
d
− →C 0(Γ)
of bigraded Q[a]-modules. Its cohomology, denoted H(Γ), is a bigraded Q[a]-
module.
If Γ is a single circle with one mark (glue together the endpoints of the
arc in the ﬁgure 1 and place a mark there), the complex is
Q[a,x 1]
a
− →Q[a,x 1]{−1, 1}
0
− →Q[a,x 1]
4
x2
x4
Γ 0
x3
x1
x4 x3
x2x1
Γ 1
0χ
χ 1
Figure 5: Graphs Γ 0 and Γ 1
(since now x2 =x1), and H(Γ) ∼= Q[x1]{−1, 1}.
Consider the diagrams Γ 0, Γ 1 in ﬁgure 5. Factorization C(Γ 0) is the tensor
product of
R
a
− →R{−1, 1}
x1−x4
− − − →R
and
R
a
− →R{−1, 1}
x2−x3
− − − →R,
where R = Q[a,x 1,x 2,x 3,x 4]. In the product basis, C(Γ 0) has the form
R
⊕
R{−2, 2}
P0
− →
R{−1, 1}
⊕
R{−1, 1}
P1
− →
R
⊕
R{−2, 2}
with
P0 =
( a x 3 −x2
a x 1 −x4
)
, P 1 =
( x1 −x4 x2 −x3
−a a
)
.
Likewise,C(Γ 1) has the presentation
R
⊕
R{−2, 4}
Q0
− →
R{−1, 1}
⊕
R{−1, 3}
Q1
− →
R
⊕
R{−2, 4}
with
Q0 =
( a x 3x4 −x1x2
0 x1 +x2 −x3 −x4
)
, Q 1 =
( x1 +x2 −x3 −x4 x1x2 −x3x4
0 a
)
.
A map between C(Γ 0) and C(Γ 1) can be described by a pair of 2 ×2 matrices
with coeﬃcients in R that specify the images of the basis vectors of Ci(Γ 0)
in Ci(Γ 1) for i = 0, 1.
5
χ 0
=
0
{0,2}
−1
0 0
χ  1
= 0
0
{0,−2}
1
{0,−2} 0
Figure 6: Complex assigned to a crossing
Let χ0 :C(Γ 0) − →C(Γ 1) be given by the pair of matrices
U 0
0 =
( x4 −x2 0
0 1
)
, U 1
0 =
( x4 −x2
−1 1
)
. (5)
Our bases in C(Γ 0) andC(Γ 1) are homogeneous with respect to the bigrading
of R. It’s easy to see that χ0 is a homogeneous map of bidegree (0 , 2).
Next, deﬁne χ1 :C(Γ 1) − →C(Γ 0) by the pair of matrices
U 0
1 =
(
1 0
0 x4 −x2
)
, U 1
1 =
(
1 x2
1 x4
)
. (6)
The map χ1 is bidegree-preserving.
Given a plane diagram D of a tangle, place at least one mark on each
internal edge of the diagram (an edge disjoint from the boundary o fD), and
label the marks and boundary points by x1,...,x m. To each crossing p of
the diagram assign the complex Cp of matrix factorizations as follows. Up to
shifts, the complex is the cone of the map χ0 or χ1, depending on whether
the crossing is positive or negative. The shifts are explained in ﬁgure 6.
Thus, if the crossing is positive,
Cp = 0 − →C(Γ 0){0, 2}
χ 0
− →C(Γ 1) − →0,
withC(Γ 1) positioned in cohomological degree 0 . The shift {0, 2} makes the
diﬀerential preserve the bidegree. If the crossing is negative,
Cp = 0 − →C(Γ 0){0, −2}
χ 0
− →C(Γ 1){0, −2} − →0,
withC(Γ 0) in cohomological degree 0 . The overall bigrading shift by {0, −2}
is here for the normalization of the Reidemeister move IIa (see later ).
6
Deﬁne C(D) as the tensor product of Cp, over all crossings p of D, and
Cc, over all arcs c. It’s a complex built out of matrix factorizations C(Γ),
over all resolutions Γ of D. The diﬀerential ∂ preserves the bigrading of each
term Cj(D). We view C(D) as an object of the category K(hmfw). The
latter is the category whose objects are complexes of objects in hmfw and
whose morphisms are homomorphism of complexes modulo null-homoto pic
morphisms.
Now we specialize to the case when D is a link diagram (has empty
boundary). Then each term Cj(D) in the complex C(D) is an object of the
homotopy category of bigraded free Q[a]-modules. We’ll see that Cj(D), for
any diagram D, decomposes as a direct sum of contractible pieces
0 − →Q[a]
1
− →Q[a] − →0
and the cohomology H(Cj(D)), which we denote CHj(D). Moreover,a acts
trivially on CHj(D), so we can ignore the Q[a]-module structure and think
of it as a bigraded Q-vector space,
CHj(D) = ⊕
k,l
CHj
k,l (D).
The bigrading descends from the bigrading on matrix factorizations C(Γ).
Thus, to D we assign the complex CH (D) of bigraded Q-vector spaces
· · ·
∂
− →CHj(D)
∂
− →CHj+1(D)
∂
− →...
As a Q-vector space, CH (D) is the direct sum of cohomology groups H(Γ)
of complexes C(Γ), over all resolutions of D.
The cohomology H(D) = H(CH (D),∂ ) of the above complex is triply-
graded,
H(D) = ⊕
j,k,l
Hj
k,l (D).
Of course, for the whole construction to be interesting, H(D) should not
depend on the choice of D, givenL.
Proposition 1 LetD be a marked tangle diagram. Then C(D), as an object
ofK(hmfw), does not depend on the number of markings on each edge of D.
Proposition 1 is proved in the next section.
Next we run into an obstacle: things seem to work well only if we restr ict
to diagrams D that come from braids. Let’s say that D is a braid diagram if
7
Figure 7: A braid diagram
Type I Type IIa
Type IIbType III
Figure 8: Reidemeister moves
D depicts the link L as the closure of a clockwise oriented braid, see ﬁgure 7.
We denote the braid by D as well.
To justify the introduction of braid diagrams, partition the Reideme ister
moves of links into types I, II, III in the usual way and then separa te II
into two subtypes, IIa and IIb, depending on orientations, see ﬁg ure 8. We
only consider the type III move with the orientations pointing in the s ame
direction.
Proposition 2 If diagrams D1,D 2 are related by a Reidemeister move of
type I, IIa or III, the complexes C(D1) and C(D2) are isomorphic as objects
of the category K(hmfw), up to an overall shift in the triple grading.
For a proof see Section 2.
8
It seems likely to us that C(D1) and C(D2) are not isomorphic (up to a
shift) if D1,D 2 are the two tangles in the IIb move in ﬁgure 8, although we
did not prove this. To avoid the IIb move, we restrict our considera tion to
braid diagrams. Closures of braid diagrams D1,D 2 are isotopic as oriented
links iﬀ D1,D 2 are related by a chain of Markov moves. A Markov move is
one of the following:
(a) conjugation DD′ ↔D′D,
(b) transformations in the braid group:
Dσjσi ↔ Dσiσj if |i −j|> 1,
D ↔ Dσiσ−1
i ,
D ↔ Dσ−1
i σi,
Dσiσi+1σi ↔ Dσi+1σiσi+1.
(c) transformations D ↔Dσ±1
n , for a braid D with n strands.
Notice that we never see the Reidemeister move IIb when dealing with
braid diagrams. The propositions stated earlier imply:
Theorem 1 Given two braid diagrams D1,D 2 of an oriented link L, the
cohomology groupsH(D1) and H(D2) are isomorphic as triply-graded vector
spaces, up to an overall shift in the grading.
To describe the Euler characteristic of H(D), we consider the function
F from braid diagrams to the ring of rational functions in q and t that is
uniquely determined by the following properties:
• F (D1) = F (D2) ifD1,D 2 are conjugate braid presentations (see Markov
move (a) above),
• F (D1) = F (D2) if D1,D 2 are related by a braid presentation move
(Markov moves (b) above),
• F (Dσn) = F (D), for a braid D with n strands,
• F (Dσ−1
n ) = −t−1q−1F (D), for a braid D with n strands,
• For any braid diagram D there is a skein relation
q−1F (Dσi) −qF (Dσ−1
i ) = (q −q−1)F (D),
• If D is the one-strand diagram of the unknot, F (D) = t−1
q−1−q.
9
σ i
positive
σ i
 −1
negative
Figure 9: Positive and negative crossings and braid generators
To see that F is simply a version of the HOMFLYPT polynomial, let α =
−t−1q−1 and consider
~F (D) = √α
|D|+−|D|−−s(D)+1
F (D)
where |D|+, respectively |D|−, is the number of positive, respectively neg-
ative, crossings of D, while s(D) is the number of strands of D. Our con-
ventions are explained in ﬁgure 9. Then ~F (D) is invariant under all Markov
moves of braids and satisﬁes the HOMFLYPT skein relation
q√α ~F (Dσ−1
i ) − (q√α)−1 ~F (Dσi) = (q −q−1) ~F (D). (7)
Thus, ~F (D) equals the HOMFLYPT polynomial of the link L, normalized
so that
~F (unknot) = α
1 −q−2.
Theorem 2 For any braid diagram D the Euler characteristic ⟨D⟩ ofH(D)
equalsF (D).
The Euler characteristic
⟨D⟩
def
=
∑
j,k,l
(−1)jtkql dimQHj
k,l (D)
is a power series in q with coeﬃcients in Z[t,t −1]. The theorem claims that
each vector spaceHj
k,l (D) is ﬁnite dimensional and the sum above is a rational
function of t and q equal to F (D). See the end of Section 2 for a proof.
Specializing to q√α = 1 in the equation (7) nets us the Alexander polyno-
mial. In terms of t andq, we are imposing the relation t = −q. Homologically,
t, q and the minus sign correspond to the three grading directions. Hen ce,
suitably collapsing the tri-grading to a bigrading we get a categoriﬁca tion of
the Alexander polynomial.
10
Sergei Gukov, Albert Schwarz and Cumrun Vafa recently conject ured
[GSV] that there exist integer-valued link invariants DQ,s,r depending on
three integer parameters Q,s,r, that can be used to determine ranks of sl(n)
link homology groups as well as the coeﬃcients of the HOMFLYPT polyn o-
mial of a link. These invariants should come from the physical theory of the
BPS states and should be related to ranks of cohomology groups of suitable
moduli spaces. It would be interesting to try relating DQ,s,r to the dimensions
of cohomology groups Hj
k,l. Our normalization of the HOMFLYPT polyno-
mial is similar to the one in [GSV], both having q −q−1 as the denominator
of the unknot invariant.
On the other hand, it’s been independently suggested by several p eople,
including Oleg Viro [V], that there should exist a triply-graded link homolo gy
theory with the HOMFLYPT polynomial as the Euler characteristic. T he
current paper resulted from our search for such a theory and fo r a combina-
torial categoriﬁcation of the Alexander polynomial.
Triply-graded cohomology theories had previously appeared in the w ork of
Asaeda, Przytycki and Sikora [APS] on categoriﬁcation of invarian ts of links
in I-bundles over surfaces, and in Audoux and Fiedler [AF], who introd uced
a reﬁned Jones polynomial and its categoriﬁcation, which are only inv ariant
under braid-like isotopies. Restriction to braid-like isotopies appear s in our
construction as well, but we don’t know how our invariant relates to t hose of
[APS] and [AF].
To conclude this section, we mention several modiﬁcations, potent ial gen-
eralizations and illnesses of the homology theory H.
• It’s not natural that we have to restrict to braid diagrams to get a
link invariant. In another sign of disfunctionality, the theory does n ot
extend to all cobordisms. For instance, the cohomology groups of the
unknot do not have a Frobenius algebra structure over the cohom ol-
ogy ring of the empty link (it’s convenient to deﬁne the latter ring to
be Q[a]), preventing us from extending the theory even to unknotted
cobordisms between unlinks.
• Any ﬁeld k can be used instead of Q. More generally, we can work
over Z, so that the invariant of a closed planar graph Γ is a complex
of graded free abelian groups, up to chain homotopy equivalence, a nd
the invariant of a link is a complex of complexes as above, up to chain
homotopy equivalence. Taking the homology H(Γ, Z) of each resolution
ofD and forming a complex out of them produces a complex CH (D, Z)
from a diagram D. We then specialize to braid diagrams and take the
cohomology of CH (D, Z). The resulting groups H(D, Z) are triply-
11
graded and, up to isomorphism, do not depend on the choice of braid
diagram D, givenL.
• In Section 2 we rewrite the factorizations C(Γ 0),C (Γ 1) and the maps
χ0, χ1 in the form that depends only on a and the diﬀerences xi −
xj of the variables xi. This allows us to pass from the ring R =
Q[a,x 1,...,x m] to the smaller ring R = Q[a,x 2 −x1,...,x m −x1].
The deﬁnition of cohomology and the proof of its invariance work ove r
R as well, leading to reduced cohomology groups H(D), with the prop-
erty H(D) = H(D) ⊗Q Q[x]. In the reduced theory the unknot has
one-dimensional cohomology groups.
• sl(n) link homology theory (see [KR]) utilized the potential xn+1. Soon
afterwards Gornik [G] studied a deformation of that theory with th e
potentialxn+1−(n+1)βnx. In then = 2 case the deformation was found
earlier by Lee [L] and used by Rasmussen in his combinatorial proof of
the Milnor conjecture [R2]. The deﬁnitions in [KR] can be generalized
to the potential xn+1 +anxn + · · · +a1x where a1,...,a n are formal
variables. We hope that this generalization will be invariant under the
Reidemeister moves and will turn out to be the ” sl(n)-equivariant”
version of sl(n) link homology. The invariant of the empty link should
be the ring of polynomials in a1,...,a n, and naturally isomorphic to the
U(n)-equivariant cohomology ring of the point. The invariant of the
unknot should be the quotient of the polynomial ring Q[x,a 1,...,a n]
by the relation xn+1 +anxn + · · · +a1x = 0, isomorphic to the U(n)-
equivariant cohomology ring of CPn. A certain version of Bar-Natan
link homology [BN], [K] should correspond to the potential x3 +ax.
• For a common generalization of the U(n)-equivariant link homology
and the theory described here one could try the potential an+1xn+1 +
anxn + · · · +a1x with all a’s being formal variables. Factorizations
C(Γ 0),C (Γ 1), the maps χ0,χ 1 and the complex C(D) can be deﬁned
for this potential as well, but we don’t know whether this theory will
be invariant under the Reidemeister-Markov moves of braid diagram s.
