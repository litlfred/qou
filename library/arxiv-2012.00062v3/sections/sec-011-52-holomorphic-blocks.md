---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-011-52-holomorphic-blocks
section_title: "Holomorphic blocks"
section_number: 5.2
pages: 27-39
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
(and their descendants) which factorize the state-integral (and its descendants), and discuss
their analytic properties, and their linearq-diﬀerence equations. Note that in this section,
as well as in Section 5.3, all the statements are theorems, whose proofs we provide.
Motivated by the state-integralZ41(u;τ) of the41 knot given in (113), and by the descen-
dant state-integralZ41,m,µ(0;τ) given in (67), we introduce the descendant state-integral of
the 41 knot
Z41,m,µ(u;τ) = e−2πiu2
∫
D
Φb(v) Φb(u +v) e−πi(v2+4uv)+2π(mb−µb−1)v dv (125)
for integersm andµ, which agrees with the Andersen-Kashaev invariant of the41 knot when
m = µ = 0. Here the contourD was introduced in (67). It is expressed in terms of two
descendant holomorphic blocks, which we denote byAm andBm instead ofBσ1
m andBσ2
m, in
order to simplify the notation. For|q|⁄ = 1, Am(x;q) and Bm(x;q) are given by
Am(x;q) =θ(−q
1
2x;q)−2x2mJ(qmx2,x ;q), (126a)
Bm(x;q) =θ(−q− 1
2x;q)xmJ(qmx,x−1;q), (126b)
where J(x,y ;qε) :=Jε(x,y ;q) for|q|< 1 and ε =± is theq-Hahn Bessel function
J+(x,y ;q) = (qy;q)∞
∞∑
n=0
(−1)n q
1
2n(n+1)xn
(q;q)n(qy;q)n
, (127a)
J−(x,y ;q) = 1
(y;q)∞
∞∑
n=0
(−1)n q
1
2n(n+1)xny−n
(q;q)n(qy−1;q)n
. (127b)
Thenexttheoremexpressesthedescendantstate-integralsbilinearlyintermsofdescendant
holomorphic blocks.
28 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
Theorem 14.(a) The descendant state-integral can be expressed in terms of the descendant
holomorphic blocks by
Z41,m,µ(ub;τ) =(−1)m+µqm/2˜qµ/2
(
e− 3πi
4 −πi
6 (τ+τ−1)Am(x;q)A−µ(˜x; ˜q−1) (128)
+ e
3πi
4 +πi
3 (τ+τ−1)Bm(x;q)B−µ(˜x; ˜q−1)
)
. (129)
(b) The functionsAm(x;q),Bm(x;q) are holomorphic functions of|q|⁄ = 1 and meromorphic
functions ofx∈ C ∗ with poles inx∈qZ of order at most1.
(c) Let
Wm(x;q) =
(
Am(x;q) Bm(x;q)
Am+1(x;q) Bm+1(x;q)
)
(|q|⁄ = 1). (130)
For all integersm and µ, the state-integralZ41,m,µ(u;τ) and the matrix-valued function
Wm,µ(u;τ) =W−µ(˜x; ˜q−1)∆(τ)Wm(x;q)T, (131)
where
∆(τ) =
(
e− 3πi
4 −πi
6 (τ+τ−1) 0
0 e
3πi
4 +πi
3 (τ+τ−1)
)
, (132)
are holomorphic functions ofτ∈ C ′ and entire functions ofu∈ C .
Proof. Part (a) follows by applying the residue theorem to the state-integral (125), along the
lines of the proof of Theorem 1.1 in [GK17]. A similar result was stated in [Dim15].
Part (b) follows from the fact that when|q|< 1, the ratio test implies thatJ+(x,y ;q) is
an entire function function of(x,y )∈ C 2 andJ−(x,y ;q) is a meromorphic function of(x,y )
with poles iny∈qZ .
For part (c), one uses parts (a) and (b) to deduce thatWm,µ(u;τ) is holomorphic ofτ∈ C′
and meromorphic inu with potential simple poles atibZ + ib−1Z . An expansion at these
points, done by the method of Section 5.3, demonstrates that the function is analytic at the
points ibZ + ib−1Z . □
Note that the summand ofJ+ (a properq-hypergeometric function) equals to that ofJ−
after replacingq by q−1. This implies that J± have a common annihilating idealIJ with
respect tox,y which canbecomputed (rigorously, along with aprovided certiﬁcate) using the
creative telescoping method of Zeilberger [PWZ96] implemented in theHolonomicFunctions
package of Koutschan [Kou09, Kou10]. Below, we will abbreviate this package byHF.
Lemma 15.The annihilating ideal ofIJ of J± is given by
IJ =⟨(−x +y) +xSy−ySx, 1 + (−1−x +qy)Sy +xS2
y⟩ (133)
where Sx and Sy are the shiftsx to qx and y to qy.
The next theorem concerns the properties of the linearq-diﬀerence equations satisﬁed by
the descendant holomorphic blocks.
Theorem 16.(a) The pairAm(x;q) andBm(x;q) areq-holonomic functions in the variables
(m,x ) with a common annihilating ideal
I41 =⟨qmx2 + (−qm +q1+2mx2)Sm +x3Sx, (1−x−1Sm)(1−x−2Sm) +q1+mSm⟩ (134)
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 29
where Sm is the shift ofm to m + 1 and Sx is the shift ofx to qx. I41 has rank 2 and the
two functions form a basis of solutions of the corresponding system of linear equations.
(b) As functions of an integerm,Am(x;q) andBm(x;q) form a basis of solutions of the linear
q-diﬀerence equationˆB41(Sm,x,q m,q )fm(x;q) = 0 for|q|⁄ = 1 where
ˆB41(Sm,x,q m,q ) = (1−x−1Sm)(1−x−2Sm) +q1+mSm. (135)
(c) The WronskianWm(x;q) of (135), deﬁned in (130), satisﬁes
det(Wm(x;q)) =x3m+3 (m∈ Z ). (136)
(d) The Wronskian satisﬁes the orthogonality relation
W−1(x;q)
(
1 0
0 −1
)
W−1(x;q−1)T =
(
x−2 +x−1− 1 1
1 0
)
. (137)
It follows that for all integersm and 𝓁
Wm(x;q)
(
1 0
0 −1
)
W𝓁(x;q−1)T∈ GL(2, Z [q±,x±]) (138)
(e) As functions ofx, Am(x;q) and Bm(x;q) form a basis of a linearq-diﬀerence equation
ˆA41(Sx,x,q m,q )fm(x;q) = 0 where
ˆA41(Sx,x,q m,q ) =
2∑
j=0
Cj(x,qm,q )Sj
x, (139)
Sx is the operator that shiftsx to qx and
C0 =q2+3mx2(−1 +q3+mx2) (140a)
C1 =−qm(−1 +q2+mx2)(1−qx−q1+mx2−q3+mx2−q3+mx3 +q4+2mx4) (140b)
C2 =q2x2(−1 +q1+mx2). (140c)
(f) The Wronskian of (139)
Wm(x;q) =
(
Am(x;q) Bm(x;q)
Am(qx;q) Bm(qx;q)
)
, (|q|⁄ = 1) (141)
satisﬁes
det(Wm(x;q)) =qmx3m(1−qm+1x2) ( m∈ Z ). (142)
Proof. Since Am(x;q) and Bm(x;q) are given in terms ofq-proper hypergeometric multi-
sums, it follows from the fundamental theorem of Zeilberger [Zei90, WZ92, PWZ96] (see
also [GL16]) that they areq-holonomic functions in both variablesm andx. Part (a) follows
from an application of theHF package of Koutschan [Kou09, Kou10].
Part (b) follows from theHF package. The fact that they are a basis follows from (c).
For part (c), Equation (135) implies that the determinant of the Wronskian satisﬁes the
ﬁrst order equationdet(Wm+1(x;q)) = x3 det(Wm(x;q)) (see [GK13, Lem.4.7]). It follows
that det(Wm(x;q)) =x3m det(W0(x;q)) with initial condition a function ofx given by Swart-
touw [Swa92]
det(W0(x;q)) =x3 (|q|⁄ = 1). (143)
30 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
We recall the details of the proof which will be useful in the case of the52 knot. When
|q|< 1, theq-Hahn Bessel functionJ(x,y ;q) satisﬁes the recursion relation
yJ(qx,y ;q)− (1 +y−x)J(x,y ;q) +J(q−1x,y ;q) = 0. (144)
This follows from [Swa92], and can also be proved using theHF package. It then follows that
Jν,1(z;q) :=J(z,q ν;q), Jν,2(z;q) :=z−νJ(q−νz,q−ν;q) (145)
are two independent solutions to
qνJ (qz;q)− (1 +qν−x)J (z;q) +J (q−1z;q) = 0. (146)
The corresponding Wronskian
Wν(z;q) =
(
Jν,1(z;q) Jν,2(z;q)
Jν,1(qz;q) Jν,2(qz;q)
)
(147)
satisﬁes the recursion relation (see [GK13, Lem.4.7])
detWν(z;q) =q−ν detWν(q−1z;q) (148)
which implies that the determinant ofU(z;q) =zνWν(z;q) is an elliptic function
detU(qz;q) = detU(z;q). (149)
It can be computed by the following limit
detU(z;q) = lim
k→∞
detU(qkz;q) = lim
z→0
detU(z;q)
= lim
z→0
(
q−νJ(z,q ν;q)J(q1−νz,q−ν;q)−J(q−νz,q−ν;q)J(qz,q ν;q)
)
=(q−ν− 1)(q1+ν;q)∞(q1−ν;q)∞, (150)
where in the last step we just used theq-expansion deﬁnition of theq-Hahn Bessel function.
We thus have
zν detWν(z;q) =−(qqν;q)∞(q−ν;q)∞. (151)
Using the substitution
z↦→x2, z ν↦→x (152)
in the above equation and cancelling with theθ-prefactors ofAm(x;q)andBm(x;q)we obtain
Equation (143) for|q|< 1. The case of|q|> 1 can be obtained by analytic continuation on
both sides of (143).
For part (d), Equation (135) implies that
Wm+1(x;q) =
(
0 1
−x3 x2 +x−q1+mx3
)
Wm(x;q). (153)
Hence, Equation (138) follows from (137). The latter is a direct consequence of the analytic
continuation formula
J(x,y ;q) =θ(−q1/2y;q)J(y−1x,y−1;q−1) (154)
which one easily sees by comparing (127a) and (127b).
Part (e) follows from theHF package. The fact that they are a basis follows from (f).
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 31
For part (f), sinceAm(x;q) (as well asBm(x;q)) are annihilated by the ﬁrst generator
of (134), it follows that
qmx2Am(x;q)−qm(1−q1+mx2)Am+1(x;q) +x3Am(qx;q) = 0. (155)
After solving for the above forAm(qx;q) (and same forBm(qx;q)) and substituting into the
Wronskian (141), it follows that the two Wronskians are related by
Wm(x;q) =
(
1 0
−qmx−1 qmx−3(1−q1+mx2)
)
Wm(x;q). (156)
After taking determinants, it follows that
det(Wm(x;q)) =qmx−3(1−q1+mx2) det(Wm(x;q)) (157)
This, together with (136) concludes the proof of (142). □
We now come to Conjecture 5 concerning a reﬁnement of theˆA-polynomial. Combining
Theorems 14 and 16 we obtain explicit linearq-diﬀerence equations for the descendant inte-
grals with respect to theu and them variables. To simplify our presentation keeping an eye
on Equation (129), let us deﬁne a normalized version of the descendant state-integral by
z41,m,µ(u;τ) = (−1)m+µq−m/2˜q−µ/2Z41,m,µ(u;τ). (158)
Theorem 17. z41,m,k(ub;τ) is aq-holonomic function of (m,u ) with annihilator idealI41
given in (134). As a function ofu(resp.,m) it is annihilated by the operatorsˆA41(Sx,x,q m,q )
and ˆB41(Sm,x,q m,q ) (given respectively by (139) and (135)), whose classical limit is
ˆA41(Sx,x,q m, 1)
= (−1 +qmx2)(x2S2
x−qm(1−x− 2qmx2−qmx3 +q2mx4)Sx +q3mx2)
(159)
and
ˆB41(Sm,x,q m, 1) = (1−x−1Sm)(1−x−2Sm) +qmSm. (160)
ˆA41(Sx,x, 1, 1) is theA-polynomial of the knot,ˆA41(Sx,x, 1,q ) is the (homogeneous part) of
the ˆA-polynomial of the knot andˆB41(x2y,x, 1, 1) is the deﬁning equation of the curve (116).
Note that although the two equations (135) and (139) look quite diﬀerent, they come
from the common annihilating ideal (134) of rank2. This explains their common order,
assuming that the ideal is generic. The annihilating ideal is easier to describe than theSm-
free element (139) of it. In fact, the ﬁrst generator ofI41 expressesSx as a polynomial inSm,
and eliminatingSm, one obtains equation (139) from (135). The characteristic variety ofI41
is a complex is a 2-dimensional complex surface in(C ∗)4 and its intersection with a complex
3-torus contains two special curves, namely theA-polynomial and theB-polynomial of the
41 knot.
32 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
5.3. Taylor series expansion atu = 0. The descendant state-integral is a meromophic
function ofu which is analytic atu = 0 and factorizes in terms of descendant holomorphic
blocks (129). In this section we compute the Taylor series of the holomorphic blocks and of
the state-integral atu = 0 and show how the factorization of the descendant state-integral
(129) reproduces (69).
We begin with some general comments valid for descendant holomorphic blocks and state-
integrals. Since the descendant holomorphic blocks are products of theta functions times
q-hypergeometric sums, we need to compute the Taylor expansion of each piece. For Taylor
expansion of theq-hypergeometric sums, we
φn(u) := (q1+neu;q)∞
(q1+n;q)∞
= exp
(
−
∞∑
l=1
1
l!E(n)
l (q)ul
)
(161a)
~φn(u) := (˜q; ˜q)∞
(˜qeu; ˜q)∞
(˜q−1; ˜q−1)n
(˜q−1eu; ˜q−1)n
= exp
( ∞∑
l=1
1
l!
~E(n)
l (˜q)ul
)
(161b)
from [GK17, Prop.2.2], where
E(n)
l (q) =
∞∑
s=1
sl−1qs(n+1)
1−qs (162)
and
~E(n)
l (˜q) =



−n +E(n)
l (˜q) l = 1
E(n)
l (˜q) l> 1 odd
2E(0)
l (˜q)−E(n)
l (˜q) l> 1 even.
(163)
For the Taylor series of the theta functions, we use the well-known identity that expresses
them in terms of quasi-modular forms (see, eg. [CMZ18, Sec.8, Eqn(76)], or alternatively
observe that the theta functions that appear in the bilinear expressions of the holomorphic
blocks are exponentials of quadratic and linear forms inu; see for instance (111a)–(111b).
Yet alternatively (and this is the method that we will use below), whenr ands are nonzero
integers withr odd and positive, we can use the identity
θ(−q
r
2xs;q) = (−1)
r+1
2 q
r2−1
8 x−s(r+1)
2 (1−xs)φ0(su)φ0(−su) (164)
whereas whenr is odd and negative, we can use theq-diﬀerence equation (109) to bring it
to the cass ofr odd and positive.
One last comment is that the descendant holomorphic blocks are in general meromorphic
functions ofu. However, their bilinear combination that appears in the descendant state-
integrals is regular atu = 0.
WenowgivethedetailsoftheTaylorseriesexpansionof Z41,m,µ(u;τ)andofthedescendant
holomorphic blocks for the41 knot. Using the deﬁnition ofJ(x,y ;q) and (161a)–(161b), we
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 33
ﬁnd
Am(eu;q) = (1− e−u)−2(q;q)−3
∞φ0(u)−2φ0(−u)−2
∞∑
n=0
qnm
(q;q)n(q−1;q−1)n
φn(u)e(2n+2m)u
=u−2(q;q)−3
∞
(
α(m)
0 (q) +uα(m)
1 (q) +O(u2)
)
(165)
where
α(m)
0 (q) =G0
m(q), (166a)
α(m)
1 (q) =
∞∑
n=0
qnm
(q;q)n(q−1;q−1)n
(1 + 2n + 2m−E(n)
1 (q)), (166b)
and
Bm(eu;q) = (1− eu)(q;q)3
∞φ0(u)φ0(−u)
∞∑
n=0
qnm
(q;q)n(q−1;q−1)n
φn(−u)e(n+m)u
=−u(q;q)3
∞
(
β(m)
0 (q) +uβ(m)
1 (q) +O(u2)
)
(167)
where
β(m)
0 (q) =G0
m(q), (168a)
β(m)
1 (q) =
∞∑
n=0
qnm
(q;q)n(q−1;q−1)n
(1
2 +n +m +E(n)
1 (q)
)
. (168b)
We notice that
β(m)
1 (q)−α(m)
1 (q) =−1
2G1
m(q). (169)
Similarly, using the deﬁnition ofJ(x,y ;q−1), we ﬁnd
Am(eu;q−1) = (1− eu)(q;q)3
∞φ0(u)2φ0(−u)2
∞∑
n=0
q−nm
(q;q)n(q−1;q−1)n
~φn(u)e(2n+2m)u
=−u(q;q)3
∞
(
~α(m)
0 (q) +u~α(m)
1 (q) +O(u2)
)
(170)
where
~α(m)
0 (q) =G0
−m(q), (171a)
~α(m)
1 (q) =
∞∑
n=0
q−nm
(q;q)n(q−1;q−1)n
(1
2 +n + 2m +E(n)
1 (q)
)
, (171b)
and
Bm(eu;q−1) = φ0(u)−1φ0(−u)−1
(1− e−u)2(q;q)3
∞
∞∑
n=0
q−nm
(q;q)n(q−1;q−1)n
~φn(−u)e(n+m)u
=u−2(q;q)−3
∞
(
~β(m)
0 (q) +u~β(m)
1 (q) +O(u2)
)
(172)
34 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
where
~β(m)
0 (q) =G0
−m(q), (173a)
~β(m)
1 (q) =
∞∑
n=0
q−nm
(q;q)n(q−1;q−1)n
(1 + 2n +m−E(n)
1 (q)). (173b)
We also notice
~β(m)
1 (q)−~α(m)
1 (q) = 1
2G1
−m(q). (174)
Applying these results to the right hand side of (129), we ﬁnd theO(1/u) contributions
from (170) and (172) cancel, and theO(u0) contributions reproduce exactly (69). Notice
that the√τ terms that appear in (69) come from expanding in terms of2πbu and 2πb−1u
in (129).
As an application of the above computations, we obtain proof of a simpliﬁed formula for
the q-series G1(q) from (43b) which was found experimentally in [GZa].
Proposition 18. For|q|< 1, we have:
G1(q) =
∞∑
n=0
(−1)nqn(n+1)/2
(q;q)2
n
(6n + 1). (175)
Proof. We ﬁrst show that the deﬁnition (43b) can equally be written as
G1(q) =
∞∑
n=0
(−1)nqn(n+1)/2
(q;q)2
n
(
1 + 2n− 4E(n)
1 (q)
)
. (176)
By deﬁnition
E(n)
1 (q) =
∞∑
s=1
qs(n+1)
1−qs, (177)
they satisfy the recursion relation
E(n)
1 (q)−E(n−1)
1 (q) =− qn
1−qn, (178)
and therefore
E(n)
1 (q) =E(0)
1 (q)−
n∑
j=1
qj
1−qj. (179)
Using the identiﬁcationE1(q) = 1 − 4E(0)
1 (q), one can then easily show that (176) is the
same as (43b).
(175) follows from (176) thanks to the non-trivial identity
∞∑
n=0
n +E(n)
1 (q)
(q;q)n(q−1;q−1)n
= 0, |q|< 1, (180)
which now we prove. The crucial fact we use is that when|q| < 1, J(x,y ;q) is symmetric
betweenx and y (see a proof in [BDP14]). Let us consider the following expansion in small
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 35
u
J(e−u, eu;q) =
∞∑
n=0
(q1+neu;q)∞
e−nu
(q−1;q−1)n
= (q;q)∞
∞∑
n=0
φn(u)e−nu
(q;q)n(q−1;q−1)n
=(q;q)∞
∞∑
n=0
1− (n +E(n)
1 (q))u
(q;q)n(q−1;q−1)n
+O(u2). (181)
SinceJ(e−u, eu;q) =J(eu, e−u;q), the coeﬃcient ofu (and in fact, of any odd power ofu) in
the expansion above vanishes, which leads to (180). □
As a second application, we demonstrate that Theorem 9, especially the identities (52),
(55), as well as the recursion relation (49), can be proved by taking theu = 0 limit of the
analogue identities in Theorem 16.
Using the expansion formulas of holomorphic blocks (165), (167), (170), (172), the Wron-
skians can be expanded as
Wm(eu;q) =
(
G0
m(q) +uα(m)
1 (q) G0
m(q) +uβ(m)
1 (q)
G0
m+1(q) +uα(m+1)
1 (q) G0
m+1(q) +uβ(m+1)
1 (q)
)(
u−2(q;q)−3
∞ 0
0 −u(q;q)3
∞
)
,
(182)
Wm(eu;q−1) =
(
G0
−m(q) +u~α(m)
1 (q) G0
−m(q) +u~β(m)
1 (q)
G0
−m−1(q) +u~α(m+1)
1 (q) G0
−m−1(q) +u~β(m+1)
1 (q)
)(
−u(q;q)3
∞ 0
0 u−2(q;q)−3
∞
)
(183)
Taking the determinant of (182), we ﬁnd
detWm(eu;q) = 1
2 detWm(q) +O(u) (184)
which together with theu-expansion of the right hand side of (136) leads to the determinant
identity (52). Furthermore, by substituting (182), (183) into the Wronskian relation (137),
the latter also reduces in the leading order to the determinant identity (52). On the other
hand, the Wronskian relation (54) is equivalent to
Wm(q) = 2
(
0 −1
1 0
)(
Wm(q)−1)T
(
0 1
−1 0
)
(185)
which can be proved directly by expressing the inverse matrix on the right hand side by
minors and determinant, using the explicit value of the determinant given by the identity
(52).
Finally, from the expression (166a),(168a) of the leading order coeﬃcientsα(m)
0 (q),β(m)
0 (q)
of Am(eu;q), Bm(eu;q) in the expansion ofu, one concludes that the recursion relation (49)
should be theu = 0 limit of the recursion relation (135) inm, and one can easily check it is
indeed the case.
36 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
ϕσ1(τ )
ϕσ2(τ )
Figure 6. The singularities in the Borel plane for the seriesϕσj(x;τ) with
j = 1, 2 of knot41 wherex is close to 1. The shortest vertical spacing between
singularities is 2πi, and the horizontal spacing between neighboring singulari-
ties in each cluster islogx.
5.4. Stokes matrices nearu = 0. In this section we conjecture a formula for the Stokes
matrices of the asymptotic seriesϕ(x;τ). When we turn on the non-vanising deformation
parameter u, the resurgent structure discussed in Section 3.1 undergoes signiﬁcant changes.
Compared to Figure 2 there are many more singular points in the Borel plane whose positions
depend onu in addition toτ, and the Stokes matrices also becomeu-dependent. However, if
we focus on the case whenu is not far away from zero, equivalent tox not far away from 1,
the resurgent data is holomorphic inu and reduces to those in Section 3.1 in theu = 0 limit.
For instance, each singular point in Figure 2 splits to a cluster of neighoring singular points
separated with distancelogx as shown in Figure 6. In particular, each singular pointιi,j on
the real axis splits to a cluster of three, in accord with the oﬀ-diagonal entries±3 in (60),
and if we choose realx, the split singularities still lie on the real axis. As in Section 3.1, we
label the four regions separating singularities on real axis and all the others byI,II,III,IV
(see Figure 7). In each of the four regions, we have the following the results.
Conjecture 19.The asymptotic series and the holomorphic blocks are related by (15) with
the diagonal matrix ∆(τ) as in (132), where matricesMR(x;q) are given in terms of the
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 37
III
III IV
Figure 7. Four diﬀerent sectors in theτ-plane for Φ(u;τ) of knot 41 with u
close to zero.
matrices W−1(x;q) as follows
MI(x;q) =
(
1 0
0 −1
)
W−1(x;q)T
(
0 1
−x−1 1
)
, |q|< 1, (186a)
MII (x;q) =W−1(x−1;q)T
(
−x−1 0
−x−1 1
)
, |q|< 1, (186b)
MIII (x;q) =W−1(x−1;q)T
(
−x−1 0
1 +x 1
)
, |q|> 1, (186c)
MIV (x;q) =
(
1 0
0 −1
)
W−1(x;q)T
(
0 1
−x−1 −x−1−x−2
)
, |q|> 1. (186d)
The above conjecture completely determines the resurgent structure ofΦ(τ). Indeed, it
implies that the Stokes matrices, deﬁned in Equations (34) and (33), are explicitly given by:
S+(x;q) =
(
0 −1
x−1 −1−x
)
·W−1(x−1;q−1)·W−1(x;q)T·
(
0 x
−1 −1−x−1
)
, |q|< 1,
(187a)
S−(x;q) =
(
x x
0 −1
)
·W−1(x;q)·W−1(x−1;q−1)T·
(
x−1 0
x−1 −1
)
, |q|< 1. (187b)
We remark that sinces(Φσ)(x;τ) for σ = 1, 2 transform under the reﬂectionπ : x↦→ x−1
uniformly by (210) (see the comment below), the Stokes matrices should be invariant under
π, and we have checked that (187a),(187b) indeed satisfy this consistency condition.
38 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
In theq↦→ 0 limit,
S+(x; 0) =
(
1 x−1 + 1 +x
0 1
)
, S−(x; 0) =
(
1 0
−x−1− 1−x 1
)
(188)
A curious corollary of our computation is that the matrices of integers (60) from [GH18, GZb]
which relates the asymptotics of the coeﬃcients ofϕ(τ)to the coeﬃcients themselves, spreads
out to the matrices (188) with entries inZ[x±1].
Using the unique factorization Lemma 8 and the Stokes matrixS from above, we can
compute the Stokes constants and the corresponding matrixS of Equation (36) to arbitrary
order inq, and we ﬁnd that
S+
σ1,σ1(x;q) =S+(x;q)1,1− 1
=(−2−x−2− 2x−1− 2x−x2)q + (−3−x−2− 2x−1− 2x−x2)q2 +O(q3),
(189)
S+
σ1,σ2(x;q) =S+(x;q)1,2/S+(x;q)1,1− (S(1,0)
σ1,σ2x +S(0,0)
σ1,σ2 +S(−1,0)
σ1,σ2 x−1)
=(3 +x−2 + 2x−1 + 2x +x2)q
+ (17 +x−4 + 4x−3 + 9x−2 + 15x−1 + 15x + 9x2 + 4x3 +x4)q2 +O(q3),
(190)
S+
σ2,σ1(x;q) =S+(x;q)2,1/S+(x;q)1,1
=(−3−x−2− 2x−1− 2x−x2)q
+ (−17−x−4− 4x−3− 9x−2− 15x−1− 15x− 9x2− 4x3−x4)q2 +O(q3),
(191)
S+
σ2,σ2(x;q) =S+(x;q)2,2− 1− S+(x;q)1,2S+(x;q)2,1/S+(x;q)1,1
=(2 +x−2 + 2x−1 + 2x +x2)q
+ (17 +x−4 + 4x−3 + 9x−2 + 14x−1 + 14x + 9x2 + 4x3 +x4)q2 +O(q3).
(192)
They enjoy the symmetry
S+
σ1,σ2(x;q) =−S+
σ2,σ1(x;q), (193)
and experimentally, it appears that the entries of the matrixS+(x;q) = (S+
σi,σj(x;q)) (except
the upper-left one) are (up to a sign) inN [x±1][[q]]. Similarly we can extract the Stokes
constantsS(𝓁,−k)
σi,σj associated to the singularities in the lower half plane, and assemble into
q−1-seriesS−
σi,σj(x;q−1). We ﬁnd they are related toS+
σi,σj(x;q) by
S−
σi,σj(x;q) =−S+
σj,σi(x;q), i⁄=j
S−
σ1,σ1(x;q) =S+
σ2,σ2(x;q), S−
σ2,σ2(x;q) =S+
σ1,σ1(x;q). (194)
Let us now verify Conjecture 4. From (187a) we ﬁnd that indeed
S+(x;q)
·
=W−1(x−1;q−1)·W−1(x;q)T. (195)
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 39
Using the recursion relation (153) and the relation between two Wronskians (156), we further
ﬁnd
S+(x;q)
··
=W0(x−1;q−1)·W 0(x;q)T. (196)
If we use the uniform notation for all holomorphic blocks
(Bα
K(x;q))α=1,2 = (A0(x;q),B 0(x;q)), (197)
the right hand side of (196) reads
W0(x−1;q−1)·W 0(x;q)T =
(∑
α
Bα
41(qjx;q)Bα
41(q−ix−1;q−1)
)
i,j=0,1
. (198)
which is precisely the right hand side of (20) in Conjecture 4 following (19).1 In addition, the
forms of the accompanying matrices on the left and on the right are such that the(1, 1) entry
of S+(x;q) equates exactly the DGG index with no magnetic ﬂux. By explicit calculation,
S+(x;q)1,1 =J(x,x−1;q)J(x,x−1;q−1) +J(x−2,x−1;q)J(x2,x ;q−1)
= 1− (2x−2 +x−1 + 2 +x + 2x2)q− (x−2 + 2x−1 + 3 + 2x +x2)q2 +O(q3),
(200)
which is the Indrot
41 (0,x ;q) given in [BDP14].
