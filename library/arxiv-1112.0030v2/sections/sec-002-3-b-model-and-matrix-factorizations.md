---
doc_id: arxiv-1112.0030v2
doc_title: "Homological algebra of knots and BPS states"
section_id: sec-002-3-b-model-and-matrix-factorizations
section_title: "B-model and matrix factorizations"
section_number: 3
pages: 10-25
source_pdf: 1112.0030v2.pdf
source_sha256: 745f143c2df4734b
doc_brief: "Homological algebra of knots and BPS states — It is known that knot homologies admit a physical descriptio n as spaces of open BPS states. W e study operators and algebras acting on these spaces."
---
Let us denote byHg,R a homology theory of knots and links colored by a repre-
sentation R of the Lie algebra g. Many such homology theories can be constructed
using categories of matrix factorizations [ 33, 34, 35, 36, 37, 38, 39, 40 ]. In this
approach, one of the main ingredients is a polynomial function Wg,R called the po-
tential, associated to every segment of a link (or, more generally, of a tan gle) away
from crossings. For example, for the fundamental representat ion of g = sl(N ) the
potential is a function of a single variable,
(3.1) Wsl(N ),
(x) = xN +1 .
In physics, matrix factorizations are known [ 41, 42, 43, 44, 45, 46 ] to describe
D-branes and topological defects in Landau-Ginzburg models which , in the present
context, are realized on the two-dimensional part of the ﬁve-bra ne world-volume
in (1.4) or (1.6). More precisely, it was advocated in [ 6] that reduction of the
M-theory conﬁguration (1.4) on one of the directions in D and a T-duality along
the time direction gives a conﬁguration of intersecting D3-branes in type IIB string
theory, such that the eﬀective two-dimensional theory on their c ommon world-
volume provides a physical realization of the Landau-Ginzburg mode l that appears
in the mathematical constructions.
In particular, this interpretation was used to deduce potentials Wg,R associated
to many Lie algebras and representations. Indeed, since away fro m crossings every
segment of the knot K is supposed to be described by a Landau-Ginzburg theory
with potential Wg,R , we can approximate this local problem by taking W = R3 and
K = R in (1.4). Then, we also have LK = R3 and the reduction (plus T-duality) of
(1.4) gives type IIB theory in ﬂat space-time with two sets of D3-br anes supported
on 4-dimensional hyperplanes in R10: one set supported on R× W , and another
supported on R× LK. The space of open strings between these two groups of
D3-branes contains information about the potential Wg,R .
For example, in the case of the fundamental representation of sl(N ), the ﬁrst
stack consists of N D3-branes and the second only contains a single D3-brane. The
open strings between these two stacks of D3-branes transform in the bifundamental
representation (N, +1) under the gauge symmetry U (N )× U (1) on the D3-branes.
The Higgs branch of this two-dimensional theory is the K¨ ahler quotient of the vector
space CN parametrized by the bifundamental chiral multiplets, modulo U (1) gauge
symmetry of a single D3-brane supported on R× LK:
(3.2) CN / /U(1) ∼
= CPN−1 .
The chiral ring of this theory on the intersection of D3-branes is pr ecisely the Jacobi
ring of the potential (3.1).
Following similar arguments one can ﬁnd potentials associated to many other
Lie algebras and representations [ 6], such that
(3.3) Hg,R (
) = J (Wg,R ) .
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES 11
Figure 2. The physics of open strings between two stacks of La-
grangian branes is described by the Landau-Ginzburg model with
potential Wg,R .
For example, the arguments that lead to (3.1) can be easily generaliz ed to R = Λ r,
the r-th anti-symmetric representation of sl(N ). The only diﬀerence is that, in
this case, the corresponding brane systems (1.4) and (1.6) conta in r coincident
M5-branes supported on R× LK× D. Following the same arguments as in the
case of the fundamental representation ( r = 1) and zooming in closely on the local
geometry of the brane intersection, after all the dualities we end u p with a system
of intersecting D3-branes in ﬂat ten-dimensional space-time,
N D3-branes : R× W(3.4)
r D3′-branes : R× LK
where, as in the previous discussion, for the purpose of deriving Wg,R we can
approximate W ≃ R3 and LK ≃ R3, so that W∩ LK = R. Now, the open
strings between two sets of D3-branes in (3.4) transform in the bif undamental
representation ( N, r) under the gauge symmetry U (N )× U (r) on the D3-branes.
Here, if we want to “integrate out” open strings ending on the D3 ′-branes, only
the second gauge factor should be considered dynamical, while U (N ) should be
treated as a global symmetry of the two-dimensional U (r) gauge theory on the
brane intersection. In the infrared this theory ﬂows to a sigma-mo del based on the
Grassmannian manifold:
(3.5) Gr( r, N) = U (N )
U (r)× U (N− r) .
The potential of the corresponding Landau-Ginzburg model [ 47] is a homogeneous
polynomial of degree N + 1,
(3.6) Wsl(N ), Λ r (z1, . . . , zr) = xN +1
1 + . . . + xN +1
r ,
where the right-hand side should be viewed as a function of the varia bles zi of
degree deg( zi) = i, i = 1 , . . . , r, which are the elementary symmetric polynomials
in the xj ,
zi =
∑
j1<j2<···<ji
xj1 xj2··· xji .
12 SERGEI GUKOV AND MARKO STO ˇSI ´C
We shall return to the discussion of the potential Wsl(N ), Λ r later in this section. In
the case of more general representations, one needs to conside r various sectors of the
U (r) gauge theory on R× LK labeled by non-trivial ﬂat connections (Wilson lines)
around the codimension-2 locus where D3 ′-branes meet D3-branes, cf. [15, 48 ].
In this paper we are mostly interested in knots colored by symmetric and anti-
symmetric representations of g = sl(N ), even though much of the present discussion
can be easily generalized to other Lie algebras and representations . Thus, for a
symmetric representation R = Sr of g = sl(N ) one ﬁnds that the corresponding
potential Wsl(N ),S r (z1, . . . , zr) is a homogeneous polynomial of degree N + r in
variables zi of degree i = 1 , . . . , r, much like (3.6). Moreover, the explicit form of
such potentials can be conveniently expressed through a generat ing function [ 6]:
(3.7)
∑
N
(−1)N tN +rWsl(N ),S r (z1, . . . , zr) = (1 +
r∑
i=1
tizi) log(1 +
r∑
i=1
tizi) ,
which in the basic case N = r = 2 gives
(3.8) Wsl(2), = z4
1− 6z2
1z2 + 6z2
2 .
Instead of going through the derivation of this formula we can use a simple trick
based on the well known isomorphism sl(2)∼
= so(3) under which a vector repre-
sentation of so(3) is identiﬁed with the adjoint representation of sl(2). Indeed, it
implies that (3.8) should be identical to the well known potential
(3.9) Wso(3),V = x2 + xy2
in the so(3) homology theory, cf. [6, 37 ]. It is easy to verify that the potentials
(3.8) and (3.9) are indeed related by a simple change of variables. 5
Moreover, the fact that the adjoint representation of sl(2) is identical to the
vector representation of so(3) implies that
(3.10)
Hsl(2), (K) ∼
= Hso(3),V (K)should hold for every knot K. In particular, it should hold for the unknot. And,
sinceHso(3),V ( ) is 3-dimensional, it follows
(3.11) dim Hsl(2), ( ) = dim Hso(3),V ( ) = 3 .
This is indeed what one ﬁnds in physical realizations of knot homologies reviewed in
section 1. In the framework of [ 4] the colored homology Hsl(2), of the unknot was
computed in [ 9] using localization with respect to the toric symmetry of the Calabi-
Yau space X. Similarly, in the gauge theory framework [ 12] the moduli space of
solutions on R2 with a single defect operator in the adjoint representation of the
gauge group G = SU (2) is the weighted projective space WCP2
(1, 1, 2) (= the space
of Hecke modiﬁcations [ 49], see also [ 50]). In this approach, the colored homology
Hsl(2),
( ) is given by the L2 cohomology of the moduli space WCP2
(1, 1, 2) which
is 3-dimensional, in agreement with (3.11).
5Explicitly, the change of variables that relates (3.8) and ( 3.9) is given by:
x = − 1
2 (
√
2 +
√
6) z2
1 +
√
6 z2
y = 2 1/ 4 z1
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES 13
3.1. Colored diﬀerentials. One of the reasons why we carefully reviewed
the properties of the potentials Wg,R is that they hold a key to understanding the
colored diﬀerentials. Namely, in doubly-graded knot homologies cons tructed from
matrix factorizations diﬀerentials that relate diﬀerent theories ar e in one-to-one
correspondence with deformations of the potentials [ 51, 52, 53, 54, 55, 6 ]:
(3.12) diﬀerentials on Hg,R ⇐⇒ deformations of Wg,R
For example, deformations of the potential (3.1) of the form ∆ W = βxM+1 with
M < N , correspond to diﬀerentials dM that relate sl(N ) and sl(M ) knot homologies
(with R = ).
More generally, one can consider deformations ∆ W of the potential Wg,R such
that deg ∆ W < deg Wg,R and
(3.13) Wg,R + ∆ W ≃ Wg′,R ′
for some Lie algebra g′ and its representation R′. Here, the symbol “ ≃” means
that the critical point(s) of the deformed potential is locally descr ibed by the new
potential Wg′,R ′ . A deformation of this form leads to a spectral sequence that
relates knot homologies Hg,R andHg′,R ′
. With the additional assumption that the
spectral sequence converges after the ﬁrst page one arrives a t (3.12). Moreover, the
diﬀerence
(3.14) deg Wg,R − deg ∆ W
gives the q-grading of the corresponding diﬀerential. Notice, the condition de g ∆ W <
deg Wg,R implies that this q-grading is positive.
For example, among deformations of the degree-4 potential (3.8) one ﬁnds
∆ W = z3
1, which leads to a diﬀerential of q-degree 1 that relates Hsl(2),
and
Hsl(2), . This deformation has an obvious analog for higher rank S2-colored ho-
mology; it deforms the homogeneous polynomial Wsl(N ), (z1, z2) of degree N + 2
in such a way that the deformed potential has a critical point descr ibed by the
potential Wg′,R ′ = Wsl(N ), (z1) of degree N + 1. Therefore, it leads to a colored
diﬀerential of q-degree 1, such that
(3.15)
(
Hsl(N ), , d colored
) ∼
= Hsl(N ),
.
In section 4 we present further evidence for the existence of a diﬀ erential with such
properties not only in the doubly-graded sl(N ) theory but also in the triply-graded
knot homology that categoriﬁes the colored HOMFLY polynomial.
Similar colored diﬀerentials exist in other knot homologies associated w ith more
general Lie algebras and representations. Basically, a knot homolo gy associated
to a representation R of the Lie algebra g comes equipped with a set of colored
diﬀerentials that, when acting on Hg,R , lead to homological invariants associated
with smaller representations (and, possibly, Lie algebras),
(3.16) dim R′ < dim R .
While it would be interesting to perform a systematic classiﬁcation of s uch colored
diﬀerentials using the general principle (3.12), in this paper we limit our selves only
to symmetric and anti-symmetric representations of g = sl(N ).
14 SERGEI GUKOV AND MARKO STO ˇSI ´C
As we already discussed earlier, when R = Λ r is the r-th anti-symmetric repre-
sentation of sl(N ) the corresponding Landau-Ginzburg potential (3.6) is a homo-
geneous polynomial of degree N + 1. Equivalently, the potentials with a ﬁxed value
of r can be organized into a generating function, analogous to (3.7):
(3.17)
∑
N
(−1)N tN +1Wsl(N ), Λ r (z1, . . . , zr) = log(1 +
r∑
i=1
tizi) .
For example, in the ﬁrst non-trivial case of r = 2 there are only two variables,
z1 = x1 + x2 and z2 = x1x2. For N = 2 one ﬁnds a “trivial” potential Wsl(2),
of degree 3, which corresponds to the fact that the anti-symmet ric representation
R = Λ 2 (also denoted R = ) is trivial in sl(2). For N = 3, the existence of
the anti-symmetric tensor ǫijk identiﬁes the second anti-symmetric representation
R = with the fundamental representation of sl(3). The next case in this sequence,
N = 4, is the ﬁrst example where the second anti-symmetric represen tation is not
related to any other representation of sl(4). According to (3.6) and (3.17), the
corresponding potential is a homogeneous polynomial of degree 5,
(3.18) Wsl(4),
= z5
1
5 − z3
1z2 + z1z2
2 .
Before studying deformations of this potential, we note that by a s imple change of
variables it is related to the potential
(3.19) Wso(6),V = x5 + xy2
associated to a vector representation of so(6). This is a manifestation of the well
known isomorphism sl(4)∼
= so(6) under which the six-dimensional anti-symmetric
representation R =
of sl(4) is identiﬁed with the vector representation of so(6).
This isomorphism can help us understand deformations of the poten tial Wsl(4), =
Wso(6),V . Indeed, the deformations of Wso(N ),V were already studied in [ 6]; they
include several deformations which lead to canceling diﬀerentials and a deformation
by ∆ W = y2 that leads to a universal diﬀerentialHso(N ),V ↝ Hsl(N−2), .
In view of the relation Wsl(4), (z1, z2) = Wso(6),V (x, y), these deformations
(and the corresponding diﬀerentials) should be present in the sl(4) theory as well.
In particular, there are deformations of Wsl(4), that lead to canceling diﬀerentials
and, more importantly, there is a deformation by ∆ W = y2 that leads to the
universal diﬀerential which relates Hso(6),V ∼
=Hsl(4),
andHsl(4), . Note, from the
viewpoint of the sl(4) knot homology, this is exactly the colored diﬀerential dcolored
that does not change the rank of the Lie algebra, but changes the representation.
Making use of (3.17) it is easy to verify that, for all values of N , the potential
Wsl(N ), admits a deformation by terms of degree N that leads to Wsl(N ), and,
therefore, to the analog of (3.15):
(3.20)
(
Hsl(N ),
, d colored
) ∼
= Hsl(N ),
.
Much like in the case of the symmetric representations, this colored diﬀerential as
well as canceling diﬀerentials come from the triply-graded theory th at categoriﬁes
the -colored HOMFLY polynomial (see section 5 for details).
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES 15
4. Colored HOMFL Y homology
In this section we propose structural properties of the triply-gr aded theory cate-
gorifying the colored version of the reduced HOMFLY polynomial. The central role
in this intricate network of structural properties belongs to the c olored diﬀerentials,
whose existence we already motivated in the previous sections.
4.1. Structural properties. Let N and r be positive integers, and letHsl(N ),S r
(K)
denote a reduced doubly-graded homology theory categorifying P Sr
N (K), the poly-
nomial invariant of a knot K labeled with the r-th symmetric representation of
sl(N ). P Sr
N denotes the Poincar´ e polynomial of Hsl(N ),S r
(K). Motivated by
physics, we expect that such theories with a given value of r have a lot in common.
Conjecture 4.1. For a knot K and a positive integer r, there exists a ﬁnite
polynomialP Sr
(K)∈ Z+[a±1, q±1, t±1] such that
(4.1) P Sr
N (K)(q, t) =P Sr
(K)(a = qN , q, t),
for all suﬃciently large N .
Since the left-hand side of (4.1) is a Poincar´ e polynomial of a homolog y the-
ory, all coeﬃcients of P Sr
(K)(a, q, t) must be nonnegative. This suggests that
there exists a triply-graded homology theory whose Poincar´ e poly nomial is equal
toP Sr
(K)(a, q, t), and whose Euler characteristic is equal to the normalized Sr-
colored two-variable HOMFLY polynomial.
As in the case of ordinary HOMFLY homology [ 3] (that, in fact, corresponds to
r = 1) and in the case of Kauﬀman homology [ 6], this triply-graded theory comes
with the additional structure of diﬀerentials, that will imply Conject ure 4.1. In
particular, for each positive integer r we have a triply-graded homology theory of
a knot K. Moreover, these theories come with additional structure of diﬀe rentials
that, as in (3.16), allow us to pass from the homology theory with R = Sr to the-
ories with R′ = Sm and m < r .
Thus, we arrive to our main conjecture that describes the struct ure of the
triply-graded homology categorifying the Sr-colored HOMFLY polynomials:
Conjecture 4.2. For every positive integer r there exists a triply-graded ho-
mology theory HSr
∗ = HSr
i,j,k (K) that categoriﬁes the reduced two-variable Sr-
colored HOMFLY polynomial of K. It comes with a family of diﬀerentials {dSr
N},
with N∈ Z, and also with an additional collection of universal colored diﬀerentials
dr→m, for every 1 ≤ m < r , satisfying the following properties:
• Categoriﬁcation: HSr
∗ categoriﬁes P Sr
:
χ(HSr
∗ (K)) = P Sr
(K).
• Anticommutativity: The diﬀerentials {dSr
N} anticommute6:
dSr
N dSr
M =−dSr
M dSr
N .
• Finite support:
dim(HSr
∗ ) < +∞.
6cf. comments following (2.11)
16 SERGEI GUKOV AND MARKO STO ˇSI ´C
• Specializations: For N > 1, the homology of HSr
∗ (K) with respect to dSr
N is
isomorphic toHsl(N ),S r
(K):
(
HSr
∗ (K), dSr
N
)
∼
=Hsl(N ),S r
(K).
• Canceling diﬀerentials: The diﬀerentials dSr
1 and dSr
−r are canceling: the ho-
mology ofHSr
∗ (K) with respect to the diﬀerentials dSr
1 and dSr
−r is one-dimensional,
with the gradings of the remaining generators being simple invariants of the knot K.
• V ertical Colored diﬀerentials: The diﬀerentials dSr
1−k, for 1 ≤ k≤ r− 1,
have a-degree−1, and the homology of HSr
∗ (K) with respect to the diﬀerential
dSr
1−k is isomorphic, after simple regrading that preserves a- and t-gradings, to the
k-colored homologyHSk
∗ (K).
• Universal Colored diﬀerentials: For any positive integer m, with m < r , the
diﬀerentials dr→m have a-degree zero, and the homology of HSr
∗ (K) with respect
to the colored diﬀerential dr→m is isomorphic (after regrading) to the m-colored
homologyHSm
∗ (K): (
HSr
∗ (K), dr→m
)
∼
=HSm
∗ (K).
A combinatorial deﬁnition of a triply-graded theory with the struct ure given
in Conjecture 4.2, as well as of the homologies Hsl(N ),S r
(K) for r > 1 and N > 2,
still does not exist in the literature.
Even though there is no such combinatorial deﬁnition, one can use a ny combina-
tion of the above axioms as a deﬁnition, and the remaining properties as consistency
checks. In particular, one can obtain various consequence of the Conjecture 4.2 and
properties of the triply-graded homology HSr
, along with the predictions for the
triply-graded homology of simple knots.
In the rest of this section we give a summary of these properties, in cluding
some non-trivial checks.
4.2. A word on grading conventions. So far we summarized the general
structural properties of the colored knot homology. Now we are a bout to make
it concrete and derive explicit predictions for colored homology grou ps of simple
knots. This requires committing to speciﬁc grading conventions, as well as other
choices that may aﬀect the form of the answer. It is important to r ealize, however,
that none of these aﬀect the very existence of the structural p roperties, which are
present with any choices and merely may look diﬀerent. While some of t hese choices
will be discussed in section 6.2, here we focus on
• choices that associate various formulae to a Young tableaux λ versus its
transpose λt;
• choices of grading, e.g. grading conventions used in this paper (that we
sometimes refer to as “old”) and grading conventions used in most o f the
existent literature [ 3, 58, 59 ] (that we sometimes call “new” in view of
the forthcoming work [ 60] based on this choice).
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES 17
The ﬁrst choice here breaks the symmetry (“mirror symmetry”) b etween repre-
sentations Sr and Λ r. Indeed, since in view of the Conjecture 1.1 the triply-graded
homologies associated with these representations are essentially id entical and can
be packaged in a single theory Hr, one has a choice whether Sr homologies arise
for N > 0 or N < 0.
The second choice listed here starts with diﬀerent grading assignme nts, but
turns out to be exactly the same as the ﬁrst choice. In other word s, the “old”
gradings and “new” gradings are related by “mirror symmetry.” Ano ther way to
describe this is to note, that in grading conventions of this paper th e Sr-colored
superpolynomials are related (by a simple change of variables) to the Λ r-colored
invariants that one would ﬁnd by following the same steps in grading co nventions
of e.g. [3, 58, 59 ]:
(4.2) P Sr
here = P Λ r
elsewhere
Note, that the Sr-colored invariant is related to the Λ r-colored invariant, and vice
versa. The explicit change of variables in this transformation is sens itive to even
more elementary redeﬁnitions, such as a→ a2 and q→ q2 which is ubiquitous in
knot theory literature. For example, with one of the most popular c hoices of a-
and q-grading, the transformation of variables / gradings looks like:
A ↦→ at3 ,
q ↦→ 1
qt2 ,(4.3)
t ↦→ 1
q .
The moral of the story is that, besides the grading conventions us ed in the
earlier literature, the present paper oﬀers yet another choice of grading conventions
consistent with all the structural properties. And the relation be tween the two
grading conventions can be viewed as a manifestation of mirror symm etry (1.10).
Keeping these words of caution in mind, now let us take a closer look at the structure
of the colored knot homology.
4.3. Consequences of Conjecture 4.2. First of all, our main Conjecture
4.2 implies the Conjecture 4.1. Indeed, in order to be consistent with the special-
ization a = qN from (4.1), the q-degree of the diﬀerential dSr
N must be proportional
to N . Since HSr
∗ has ﬁnite support, this leads to the Conjecture 4.1, with P Sr
(K)
being the Poincar´ e polynomial ofHSr
∗ (K).
More precisely, the diﬀerentials dSr
N , N≥ 1, are expected to have the following
degrees:
deg(dSr
N ) = (−1, N,−1), N > 0,
which is consistent with the specialization a = qN and the formula (3.14) that de-
termines the q-grading of the corresponding diﬀerential in the doubly-graded th eory.
In fact, the diﬀerential dSr
N acts on the the following bi-graded chain complex:
Csl(N ),S r
p,k =
⨁
iN +j=p
HSr
i,j,k ,
18 SERGEI GUKOV AND MARKO STO ˇSI ´C
and has q-degree 0, and t-degree−1. The homology of Csl(N ),S r
with respect to
dSr
N is isomorphic to Hsl(N ),S r
.
In general, the degrees of the diﬀerentials dSr
N , for N∈ Z are given by:
deg(dSr
N ) = ( −1, N,−1), N ≥ 1− r,
deg(dSr
N ) = ( −1, N,−3), N ≤− r.
We note that for every r≥ 1, and every N∈ Z, the degree of the diﬀerential dSr
N
has the form deg( dSr
N ) = (−1, N,∗).
4.3.1. Canceling diﬀerentials. Canceling diﬀerentials appear in all conjectural
triply-graded theories, including the ordinary HOMFLY homology and the Kauﬀ-
man homology. The deﬁning property of a canceling diﬀerential is tha t the ho-
mology of the triply-graded theory with respect to this diﬀerential is “trivial”, i.e.
isomorphic to the homology of the unknot. In reduced theory, this means that the
resulting homology is one-dimensional. Furthermore, the degree of the remaining
generator depends in a particularly simple way on the knot.
In the case of the colored HOMFLY homology HSr
, the canceling diﬀerentials
are dSr
1 and dSr
−r. Their degrees are:
deg(dSr
1 ) = ( −1, 1,−1),
deg(dSr
−r) = ( −1,−r,−3).
Note that for r = 1 this agrees with the gradings of the canceling diﬀerentials
in the ordinary triply-graded HOMFLY homology. (Keep in mind, thoug h, the
conventions we are using in this paper, see Remark A.1.) For either of the two
canceling diﬀerentials, the degree of the surviving generator depe nds only on the
S-invariant7 of a knot K, introduced in [ 3]. In particular, the surviving generators
have the following ( a, q, t)-degrees:
deg
(
HSr
∗ (K), dSr
1
)
= ( rS,−rS, 0),(4.4)
deg
(
HSr
∗ (K), dSr
−r
)
= ( rS, r2S, 2rS) .
Note, that the remaining generator with respect to dSr
1 has t-degree equal to zero.
4.3.2. Vertical Colored diﬀerentials. Arguably, the most interesting feature of
the colored triply-graded theory is the existence of colored diﬀere ntials. They allow
to pass from the homology theory for a representation R = Sr to the homology
theory for another representation R′ = Sm, with m < r .
The ﬁrst group of colored diﬀerentials are “vertical” colored diﬀere ntials dSr
1−k,
for 1≤ k≤ r− 1. As said before, the degrees of these diﬀerentials are
(4.5) deg( dSr
1−k) = (−1, 1− k,−1), 1≤ k≤ r− 1.
The homology ofHSr
with respect to the diﬀerential dSr
1−k, for any k = 1, . . . , r−
1, is (up to a simple regrading) isomorphic to HSk
.
7Again, the value that we are using here is half of the value deﬁ ned in [ 3].
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES 19
In particular, up to an overall shift of the a-grading, the a- and t-gradings of
the homologies match. More precisely, the Poincare polynomial of th e homology
(HSr
, dSr
1−k) satisﬁes:
(4.6) ( HSr
, dSr
1−k)(a, q = 1, t) = a(r−k)SP Sk
(a, q = 1, t),
where the S-invariant is deﬁned by (4.4). The q-grading is controlled in the follow-
ing way: the canceling diﬀerentials dSk
1 and dSk
−k ofHSk
correspond to two canceling
diﬀerentials of (HSr
, dSr
1−k) of degrees (−1, 1 + r− k,−1) and (−1,−r,−3), respec-
tively.
In the particular case of the diﬀerential dSr
0 that allows passage from Sr-colored
homology to the uncolored S1-homology, the explicit regrading is particularly sim-
ple:
(4.7) ( HSr
, dSr
0 )(a, q, t) = a(r−1)SP
(a, qr, t).
4.3.3. Universal Colored diﬀerentials. The universal colored diﬀerentials in the
triply-graded theory are “universal” analogs of the colored diﬀere ntials in the
doubly-graded theory (3.15):
Hsl(N ),S r
↝ Hsl(N ),S r−1
.
As explained in section 3, these colored diﬀerentials come from the de formations of
the Landau-Ginzburg potentials.
Since colored diﬀerentials are universal in the triply-graded theory — i.e. they
relate colored triply-graded homologies without even specializing to d oubly-graded
sl(N ) theories — they should have zero a-degree. This property distinguishes them
clearly from the vertical colored diﬀerentials.
Furthermore, as explained in section 3, the basic colored diﬀerentia l dr→(r−1)
should have q-degree equal to 1. Then, it is easy to see that consistency of the theory
also requires this diﬀerential to have zero t-grading. Combining all of these facts,
we conclude that the ( a, q, t)-degree of the diﬀerentials dr→(r−1) is equal to (0 , 1, 0).
More generally, we expect that the degree of the diﬀerential dr→m depends only
on the diﬀerence r− m and the homology of HSr
∗ (K) with respect to the colored
diﬀerential dr→m is isomorphic (up to regrading) to HSm
∗ (K). The explicit form of
the regrading for the colored diﬀerential d2→1 is as follows: the Poincar´ e polynomial
of the homology (H , d2→1) is equal to P (a2, q2, t2q). Put diﬀerently,
(4.8)
(
H (K), d2→1
)
2i,k +2j, 2k
∼
= H
i,j,k (K) .
In general, the explicit regrading is very subtle (unlike the case of th e vertical
colored diﬀerentials).
We point out that, for m < m 1 < r , the homology (( HSr
, dr→m1), dm1→m)
does not need to coincide with the homology ( HSr
, dr→m).
4.4. Second symmetric representation. In this subsection we focus on the
case r = 2, i.e. on the homology H (K). Specialization of the above mentioned
properties to r = 2 gives:
20 SERGEI GUKOV AND MARKO STO ˇSI ´C
• Two canceling diﬀerentials d1 and d−2 that have degrees:
deg(d1 ) = ( −1, 1,−1),
deg(d−2) = ( −1,−2,−3).
• The generator that survives the diﬀerential d1 has degree (2 S,−2S, 0).
• The generator that survives the diﬀerential d−2 has degree (2 S, 4S, 4S).
• The vertical colored diﬀerential d0 has degree (−1, 0,−1).
• The Poincar´ e polynomial of the homology (H (K), d0 ) is equal to aSP (K)(a, q2, t).
• The colored diﬀerential d2→1 has degree (0 , 1, 0).
• The Poincar´ e polynomial of the homology ( H (K), d2→1) is equal to
P (K)(a2, q2, t2q).
In addition, the homology ofH (K) with respect to the diﬀerential d2 should
be isomorphic (after specialization a = q2) toHsl(2), (K). To ﬁnd the latter ho-
mology one can use the isomorphism (3.10) with Hso(3),V (K) which, in turn, can
be obtained from the triply-graded Kauﬀman homology HKauﬀ (K) studied in [ 6].
Indeed, the doubly-graded homology Hso(3),V (K) is isomorphic to the homology
ofHKauﬀ (K) with respect to the corresponding diﬀerential d3 from [ 6], after the
specialization λ = q2. Usually, that diﬀerential d3 acts trivially; in particular, this
is the case for all knots that we analyze below.
The structure of the homology H (K) with the above diﬀerentials allows us
to compute it for various small knots, as we shall illustrate next.
4.4.1.HS2
andP S2
for small knots. The homology H (K) and the super-
polynomialP (K)(a, q, t) (= the Poincar´ e polynomial of H (K)) must satisfy
the following properties:
• specialization to t =−1 gives the reduced -colored HOMFLY polyno-
mial P (K).8
• specialization to a = q2 gives the Poincar´ e polynomialP2 (K) of the
homologyHsl(2), (K). This homology is isomorphic to Hso(3),V (K). To
ﬁnd the latter one, we use the results from Table 3 of [ 6], if available. 9
• H (K) comes equipped with the diﬀerentials described in section 4.4.
8In order to ﬁnd the colored HOMFLY polynomial P (K) one can use e.g. equation (3.25)
in [ 26] and the values for the BPS invariants ˆN ,g,Q tabulated in section 6 of that paper. The
result gives the unreduced two-variable colored HOMFLY pol ynomial. In order to ﬁnd the reduced
polynomial, one should divide the unreduced polynomial by:
(a − a− 1)(aq − a− 1q− 1)
(q − q− 1)(q2 − q− 2) .
The results from [ 26] enable us to compute the reduced -colored HOMFLY polynomial for the
knots 3 1, 4 1, 5 1 and 6 1. Another useful source of the colored HOMFLY polynomials an d their
specializations to a = q2 and a = q3 is the KnotAtlas [ 56], which the reader may want to consult
for many other knots.
9In all examples we have computed, the values i + j for all nontrivial Kauﬀman homology
groups HKauﬀ
i,j,k (K) have the same parity. Thus the diﬀerential d3 on the Kauﬀman homology,
which is of degree ( − 1, 2, − 1), is trivial. Consequently, the Poincar´ e polynomial P so(3),V (K)(q, t )
is equal to the λ = q2 specialization of the Poincar´ e superpolynomial of the Kau ﬀman homology
P Kauﬀ (K)(λ = q2, q, t ) in all our examples.
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES 21
These requirements are more than suﬃcient to determine the color ed su-
perpolynomial for many small knots. As the ﬁrst example, we consid er the
trefoil knot:
Example. The trefoil knot 31
The reduced -colored HOMFLY polynomial of the trefoil knot is
equal to (see e.g. [26, 57 ]):
P (31) = a2q−2 + a2q + a2q2 + a2q4− a3− a3q− a3q3− a3q4 + a4q3 .
The homologyHso(3),V (31) is computed in [ 6] (see eq. (6.14) and Table 3).
Hence we have:
P2 (31) = q2 + q5t2 + q6t2 + q6t3 + q7t3 + q8t4 + q9t5 + q10t5 + q11t6
From these two expressions we immediately deduce the colored supe rpoly-
nomial of the trefoil 10:
(4.9) P (31) = a2(q−2 + qt2 + q2t2 + q4t4) + a3(t3 + qt3 + q3t5 + q4t5) + a4q3t6.
Note that its specializations to t = −1 and a = q2 give P (31) and
P2 (31), respectively. Moreover, the corresponding homology H (31) also
enjoys the action of two canceling diﬀerentials and one colored diﬀer ential.
In order to visualize this homology, we represent each generator b y a dot
in the ( a, q)-plane, with a label denoting its t-grading. In Figure 3, the
canceling diﬀerential d1 is represented by a blue arrow, the canceling
diﬀerential d−2 is represented by a red arrow, the colored diﬀerential d2→1
is represented by a magenta arrow, while the vertical colored diﬀer ential
d0 is represented by dashed light blue arrow.
The generator that survives d1 has degree (2 ,−2, 0), while the one
that survives d−2 has degree (2 , 4, 4). Both are consistent with the S-
invariant of the trefoil S(31) = 1 and the general discussion in section 4.4.
The Poincar´ e polynomial of the homology with respect to the colore d dif-
ferential d2→1 is equal to:
a2q−2 + a2q4t4 + a4q3t6 ,
while the Poincar´ e polynomial of the homology with respect to the ve rtical
colored diﬀerential d0 is equal to:
a2q−2 + a2q2t4 + a3t3 .
A careful reader will notice that the last two expressions are equa l to
P (31)(a2, q2, t2q) and aP (31)(a, q2, t), respectively, whereP (31)(a, q, t)
is the ordinary superpolynomial, whose explicit form is written in (A.1).
10As discussed in section 4.2, there are two diﬀerent possibil ities for grading conventions.
Besides the grading conventions discussed in most of this pa per, there are also “new” grading
conventions where the a and q degrees are both twice the value of the corresponding degree s in
the conventions that we are using in this paper, while the t-degree change is more subtle. The
value of the colored superpolynomial of the trefoil in the “n ew” gradings is given by
Pnew grad. (31) = a4(q− 4 + q2t4 + q4t6 + q8t8) + a6(t5 + q2t7 + q6t9 + q8t11) + a8q6t12.
W e note that in these gradings, the answer coincides with [ 58, 59 ].
22 SERGEI GUKOV AND MARKO STO ˇSI ´C
32−1 0 1−2−3
2
3
4
4
a
q
6
5
4220
3 3 5
Figure 3. The reduced S2-colored homology of the trefoil knot.
This computation can be easily extended to many other small knots. We list
the results for all prime knots with up to 6 crossings in Tables 1 and 2. The fact
that the structure described in this section works beautifully for a ll knots with up
to 6 crossings is already an impressive test of our main Conjecture 4 .2. However,
to convince even hard-boiled skeptics, in appendix B we carry out a m uch more
challenging computation of the colored HOMFLY homology for “thick” knots 8 19
and 9 42.
We notice that all computations of colored homologies in this paper ar e done
by hand, only by using the existence and properties of the diﬀerent ials described in
this section. Moreover, in majority of the cases only a few of the diﬀ erentials are
used to obtain the result, which than matched perfectly all the rem aining properties.
4.5. Diﬀerentials for higher symmetric representations. Now let us
consider the triply graded homology HSr
of knots and links colored by the rep-
resentation R = Sr with more general r≥ 1. Much as in the case r = 2 considered
in the previous subsection, we expect that HSr
comes equipped with the following
diﬀerentials:
• canceling diﬀerential dSr
1 of degree (−1, 1,−1), whose homology is one-
dimensional and consists of a degree ( rS,−rS, 0) generator;
• canceling diﬀerential dSr
−r of degree (−1,−r,−3), which leaves behind a
one-dimensional homology with a generator of degree ( rS, r2S, 2rS);
• for every 1 ≤ k < r , there exists a vertical colored diﬀerential dSr
1−k of
degree (−1, 1− k,−1), such that the homology of HSr
with respect to
dSr
1−k is isomorphic to HSk
;
• for every 1 ≤ m < r , there exists a universal colored diﬀerential dr→m
which, when acting on HSr
, leaves behind the homology HSm
. In partic-
ular, the colored diﬀerential dr→(r−1) has degree (0 , 1, 0).
4.5.1. Colored superpolynomialP S3
for the trefoil. It can be computed by re-
quiring that its specialization to t =−1 equals the reduced S3-colored HOMFLY
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES 23
Knot P
31 a2(q2t2 + q−2 + qt2 + q4t4) + a3(q4t5 + q3t5 + t3 + qt3) + a4q3t6
41 a−2q−2t−4 + (a−1q−3 + a−1q−2)t−3 + (q−3 + a−1q−1 + a−1)t−2+
+(q−2 + q−1 + a−1 + a−1q)t−1 + (q−1 + 3 + q) + (q2 + q + a + aq−1)t+
+(q3 + aq + a)t2 + (aq3 + aq2)t3 + a2q2t4
51 a4q−4 + (a4q−1 + a4)t2 + (a5q−2 + a5q−1)t3+
+(a4q2 + a4q3 + a4q4)t4 + (a5q + 2a5q2 + a5q3)t5+
+(a4q5 + a4q6 + a6q)t6 + (a5q4 + 2a5q5 + a5q6)t7+
+(a4q8 + a6q4 + a6q5)t8 + (a5q7 + a5q8)t9 + a6q7t10.
52 a2q−2 + (a2q−1 + a2)t + (2a2q + a2q2 + a3q−2 + a3q−1)t2+
+(a2q2 + a2q3 + 2a3 + 2a3q)t3 + (a2q4 + 2a3q + 3a3q2 + a3q3 + a4)t4+
+(2a3q3 + 2a3q4 + a4 + 2a4q + a4q2)t5+
+(a3q4 + a3q5 + a4q2 + 3a4q3 + a4q4)t6+
+(a4q3 + 2a4q4 + a4q5 + a5q2 + a5q3)t7+
+(a4q6 + a5q3 + a5q4)t8 + (a5q5 + a5q6)t9 + a6q5t10.
Table 1. Colored superpolynomial for prime knots with up to 5 crossings.
polynomial and that it enjoys the action of the canceling and the ﬁrs t colored dif-
ferentials of appropriate degrees. In particular, according to th e general rules (4.4),
we require that the remaining generator with respect to the d1 action has degree
(3,−3, 0), while the remaining generator with respect to the action of d−3 has
degree (3 , 9, 6). For the colored diﬀerential d3→2 we require that the remaining ho-
mology should have rank 9, just like H (31). From these, we obtain the following
result:
P S3
(31) = a3q−3 + (a3q + a3q2 + a3q3)t2 + (a4 + a4q + a4q2)t3 +
+(a3q5 + a3q6 + a3q7)t4 + (a4q4 + 2a4q5 + 2a4q6 + a4q7)t5 +
+(a5q4 + a5q5 + a5q6 + a3q9)t6 + (a4q8 + a4q9 + a4q10)t7 +
+(a5q8 + a5q9 + a5q10)t8 + a6q9t9.
Note, there exists a diﬀerential d3→1 onHS3
(31) of degree (0 , 4, 2), such that the
homology with respect to this diﬀerential is of rank 3, as H (31).
Also, there exists a diﬀerential d0 of degree (−1, 0,−1) such that the Poincare
polynomial of (H (31), d0 ) is equal to a2P (31)(a, q3, t).
24 SERGEI GUKOV AND MARKO STO ˇSI ´C
Knot P
61 a−2q−2t−4 + (a−1q−3 + a−1q−2)t−3 + (a−1q−2 + 2a−1q−1 + q−3 + a−1)t−2+
+(q−3 + a−1 + 3q−2 + 2q−1 + a−1q)t−1 + (aq−3 + 2q−2 + aq−2 + 5 + q)+
+(aq−2 + 1 + 3q + 3aq−1 + 2q2 + 2a)t+
+(aq−1 + 4a + 4aq + q3 + a2q−1 + aq2)t2+
+(a2q−1 + aq + 2a2 + 3aq2 + 2aq3 + a2q)t3+
+(a2 + 2a2q + aq3 + 3a2q2 + aq4 + a2q3)t4+
+(a2q2 + 2a2q3 + a3q + a3q2 + a2q4)t5+
+(a3q2 + a3q3 + a2q5)t6 + (a3q4 + a3q5)t7 + a4q4t8.
62 a4q6t8 + (a3q6 + a3q7)t7 + (a4q3 + a2q7)t6 + (2a3q3 + 2a3q4)t5+
+(a4 + a2q3 + 3a2q4 + a2q5)t4 + (2a3 + 2a3q + aq4 + aq5)t3 + (3a2q + a2q2)t2+
+(a3q−3 + a3q−2 + aq + aq2)t + (a2q−3 + 3a2q−2 + a2q−1 + q2)+
+(aq−2 + aq−1)t−1 + a2q−5t−2 + (aq−5 + aq−4)t−3 + q−4t−4+
+(1 + q)(1 + a−1qt−1)(1 + a−1q−2t−3)× [a4q4t7 + (a4q3 + a3q4)t6+
+(a4q + a3q3)t5 + (a3q2 + a3q)t4 + a3t3 + (a3q−2 + a2)t2].
63 a2q5t6 + (aq5 + aq6)t5 + (a2q2 + q6)t4 + (2aq2 + 2aq3)t3+
+(a2q−1 + q + 3q2 + q3)t2 + (2aq−1 + 2a + a−1q3 + a−1q4)t
+(q−1 + 5 + q) + (aq−4 + aq−3 + 2a−1 + 2a−1q)t−1 + (q−3 + 3q−2 + q−1 + a−2q)t−2+
+(2a−1q−3 + 2a−1q−2)t−3 + (q−6 + a−2q−2)t−4 + (a−1q−6 + a−1q−5)t−5 + a−2q−5t−6+
+(1 + q)(1 + a−1qt−1)(1 + a−1q−2t−3)× [a2q3t5 + (a2q + aq3)t4+
+(a2 + aq2 + aq)t3 + 3at2 + (aq−1 + aq−2 + 1)t + (aq−3 + q−1) + q−3t−1].
Table 2. Colored superpolynomial for prime knots with 6 crossings.
Finally, there exists a diﬀerential d−1 of degree (−1,−1,−1) such that the
homology(H (31), d−1 ) is isomorphic to H (31).
In Appendix C we compute also the S3-colored homology of the ﬁgure-eight
knot 4 1.
4.5.2. Size of the homology. Computations show that for a knot K, the rank
of the homology HSr
grows exponentially with r. In particular, this makes the
computation of the homologies HSr
(K) diﬃcult for large r. (In fact, even for r > 2
the size of the homology is too big to make computations practical.) To be more
precise, for all thin and torus knots studied here we ﬁnd:
(4.10) rank HSr
(K) =
(
rankHS(K)
) r
.
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES 25
