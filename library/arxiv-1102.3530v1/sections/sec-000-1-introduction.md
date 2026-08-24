---
doc_id: arxiv-1102.3530v1
doc_title: "The colored Jones polynomial, the Chern-Simons invariant, and the Reidemeister torsion"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 1102.3530v1.pdf
source_sha256: ad3edab19f3dc404
doc_brief: "The colored Jones polynomial, the Chern-Simons invariant, and the Reidemeister torsion — W e show that from the asymptotic behavior of an evaluation of the colored Jones polynomial of the ﬁgure-eight"
---
Let JN (K;q) be the colored Jones polynomial of a knot K in the three-sphere
S3 associated with the N -dimensional irreducible representation of sl(2; C). We
normalize it so that JN (unknot;q) = 1. Note that J2(K;q) is the celebrated Jones
polynomial [11] after a suitable change of variable.
In 1995 Kashaev introduced a complex valued knot invariant for eac h natural
number N by using quantum dilogarithm [12] and observed that its asymptotic
behavior for large N determines the hyperbolic volume for several hyperbolic knots
[13]. He also conjectured that it is also true for any hyperbolic knot. Here a knot
is called hyperbolic if its complement has a unique complete hyperbolic st ructure
with ﬁnite volume. It is proved in 2001 by J. Murakami and the author that his in-
variant coincides with JN
(
K; exp(2π√−1/N)
)
[21]. We also generalized Kashaev’s
conjecture to the following volume conjecture.
Conjecture 1.1 (Volume Conjecture [13, 21]) . LetK be a knot in S3 and Vol(K)
denote the simplicial volume of S3 \K. Then the following equality would hold:
(1.1) lim
N →∞
log
⏐
⏐JN
(
K; exp(2π√
−1/N)
) ⏐
⏐
N = Vol(K)
2π .
See for example [20] about recent developments of the conjectu re and its gener-
alizations.
As one of the generalizations Yokota and the author [22] proved t hat for the
ﬁgure-eight knot the colored Jones polynomial knows much more. A ctually we
showed that if we perturb the parameter 2 π√−1 a little the corresponding limit
determines the SL(2; C) Chern–Simons invariant associated with an irreducible rep-
resentation of π1(S3 \K) to SL(2; C) in the sense of Kirk and Klassen [14]. In fact
we showed the following theorem.
Date: November 3, 2018.
2000 Mathematics Subject Classiﬁcation. Primary 57M27 57M25 57M50.
Key words and phrases. colored Jones polynomial, volume conjecture, Chern–Simon s invariant,
Reidemeister torsion.
The authors are supported by Grant-in-Aid for Challenging E xploratory Research (21654053).
1
2 HITOSHI MURAKAMI
Theorem 1.2 ([22]). Let E be the ﬁgure-eight knot. There exists a neighborhood
U ⊂ C of 0 such that if u ∈ (U \π√−1Q) ∪ {0} then the following limit exists:
lim
N →∞
logJN
(
K; exp((u + 2π√−1/N))
)
N .
Moreover the limit determines the SL(2; C) Chern–Simons invariant associated with
an irreducible representation of π1(S3 \E) to SL(2; C) which is determined by the
parameteru.
On the other hand, Andersen and Hansen [1, Theorem 1] reﬁned t he volume
conjecture for the ﬁgure-eight knot as follows.
Theorem 1.3 ([1]). The following asymptotic equivalence holds:
JN
(
E; exp(2π
√
−1/N)
)
∼
N →∞
1
31/ 4N 3/ 2 exp
( N Vol(E)
2π
)
= 2 π3/ 2
( 2√−3
) 1/ 2( N
2π√−1
) 3/ 2
exp
( N
2π√−1 ×
√
−1 Vol(E)
)
.
Note that the twisted Reidemeister torsion and the Chern–Si mons invariant as-
sociated with the unique complete hyperbolic structure of S3 \E are 2/√−3 and√−1 Vol(E) respectively.
Note that we write f (N ) ∼
N →∞
g(N ) if and only if lim N →∞f (N )/g(N ) = 1 and
that (1.1) follows from the equivalence relation above when K is the ﬁgure-eight
knot.
In this paper we reﬁne Theorem 1.2 as Theorem 1.3 for the case wher eu is real.
Theorem 1.4. Letu be a real number with 0<u< log((3 +
√
5)/2) = 0.9624...
and put ξ := 2π√−1 +u. Then we have the following asymptotic equivalence of the
colored Jones polynomial of the ﬁgure-eight knot E:
(1.2) JN (E; exp(ξ/N )) ∼
N →∞
√−π
2 sinh(u/2)T (u)1/ 2
( N
ξ
) 1/ 2
exp
( N
ξ S(u)
)
,
where
S(u) := Li 2(eu−ϕ (u)) − Li2(eu+ϕ (u)) −uϕ(u)
and
T (u) := 2√
(eu +e−u + 1)(eu +e−u − 3)
.
Hereϕ(u) := arccosh(cosh(u) − 1/2) and
Li2(z) := −
∫ z
0
log(1 −x)
x dx
is the dilogarithm function.
Note that S(u) deﬁnes the SL(2; C) Chern–Simons invariant and T (u) is the
cohomological twisted Reidemeister torsion, both of which are asso ciated with an
irreducible representation of π1(S3 \E) into SL(2; C) sending the meridian to an
element with eigenvalues exp(u/2) and exp( −u/2). See Section 4 for details.
Remark 1.5. Since the ﬁgure-eight knot is amphicheiral, we have JN (E;q−1) =
JN (E;q). Thus if u< 0 we have
JN
(
E; exp((u + 2π
√
−1)/N)
)
=JN
(
E; exp((−u − 2π
√
−1)/N)
)
=JN
(
E; exp((−u + 2π
√
−1)/N)
)
,
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 3
wherez denotes the complex conjugate of z. So if we prove Theorem 1.4 for u> 0,
we have a similar asymptotic equivalence for u< 0. Details are left to the readers.
Theorem 1.4 conﬁrms the following conjecture in the case of the ﬁgu re-eight knot
for real u with 0 <u< log((3 +
√
5)/2).
Conjecture 1.6 ([8, 2]) . Let K be a hyperbolic knot. Then there exists a neigh-
borhoodU ∈ C of 0 such that if u ∈U \π√−1Q, we have the following asymptotic
equivalence:
JN (K; exp(ξ/N )) ∼
N →∞
√−π
2 sinh(u/2)T (K;u)1/ 2
( N
ξ
) 1/ 2
exp
( N
ξ S(K;u)
)
,
where ξ := 2π√−1 +u, T (K;u) is the cohomological twisted Reidemeister torsion
and S(K;u) is the SL(2; C) Chern–Simons invariant, both of which are associated
with an irreducible representation of π1(S3 \K) intoSL(2; C) sending the meridian
to an element with eigenvalues exp(u/2) and exp(−u/2).
For physical interpretations of this conjecture, see for example [7, 2].
For torus knots we know the following result. Let T (a,b ) be the torus knot of
type (a,b ) for positive coprime integers a and b. It is known that the SL(2; C)
character variety of π1(S3 \T (a,b )) has (a − 1)(b − 1)/2 components [15] (see also
[18]). Such components are indexed by a positive integer k that is not a multiple
of a or b. See [9, § 2] for details. Let ρk be an irreducible representation in the
component indexed by k,Sk(u) be the Chern–Simons invariant associated with ρk
with exp( ±u/2) the eigenvalues of the image of the meridian by ρk, and Tk be the
cohomological twisted Reidemeister torsion associated with ρk. Then we have the
following formulas [9]:
Sk(u) := −
(
2kπ√−1 −ab(2π√−1 +u)
) 2
4ab
and
Tk := 16 sin2(kπ/a) sin2(kπ/b)
ab .
Dubois and Kashaev [5], and Hikami and the author [9] obtain the follo wing as-
ymptotic equivalences.
Theorem 1.7 ([5]). Foru = 0 we have
JN
(
T (a,b ); exp(2π
√
−1/N)
)
∼
N →∞
π3/ 2
2ab
( N
2π√−1
) 3/ 2 ab−1∑
k=1
(−1)k+1k2T 1/ 2
k exp
( N
ξ Sk(0)
)
.
Note that since Tk vanishes if a or b divides k, the summation is for all the irre-
ducible components of the character variety.
Theorem 1.8 ([9]). Letu be a complex number with 0< |u|< 2π/(ab). Then we
have
JN
(
T (a,b ); exp(ξ/N )
)
∼
N →∞
1
∆( T (a,b );eu)
when Reu> 0 and
JN
(
T (a,b ); exp(ξ/N )
)
∼
N →∞
1
∆( T (a,b );eu) +
√−π
2 sinh(u/2)
ab−1∑
k=1
(−1)kT 1/ 2
k
( N
ξ
) 1/ 2
exp
( N
ξ Sk(u)
)
4 HITOSHI MURAKAMI
when Reu< 0, whereξ :=u+2π√−1 and ∆( T (a,b );t) is the Alexander polynomial.
See [9] for more details.
The paper is organized as follows. In Section 2 we give an integral for mula for
the colored Jones polynomial using the quantum dilogarithm. We stud y its asymp-
totic behavior by using the saddle point method to give a proof of The orem 1.4
in Section 3. In Section 4 we give topological interpretations of S(u) and T (u).
Sections 5 to 8 are devoted to miscellaneous calculations.
