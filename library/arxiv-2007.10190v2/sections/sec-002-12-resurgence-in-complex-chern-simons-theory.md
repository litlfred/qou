---
doc_id: arxiv-2007.10190v2
doc_title: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS"
section_id: sec-002-12-resurgence-in-complex-chern-simons-theory
section_title: "Resurgence in complex Chern-Simons theory"
section_number: 1.2
pages: 1-7
source_pdf: 2007.10190v2.pdf
source_sha256: 37bcbd3a343bb21a
doc_brief: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS — The asymptotic expansion of quantum knot invariants in complex Chern-Simons theory gives rise to factorially divergent formal power series."
---
2. The equation (1 − x)(1− x−1) = 1 and the 4 1 knot 4
3. The equation x−2(1− x)3 = 1 and the 5 2 knot 5
4. Descendants 7
4.1. The Kashaev invariant and its descendants 7
4.2. The q-series (G0
0, G1
0) and their descendants 8
4.3. The state integral and its descendants 9
5. Computations 11
5.1. Resurgent analysis 11
5.2. The 4 1 knot 13
5.3. The 5 2 knot 16
6. Open questions 20
Acknowledgements 20
Appendix A. q-series associated with the 5 2 knot 21
A.1. The state integral of the 5 2 knot 21
A.2. The symmetry q↔ q−1 23
References 23
1. Introduction
1.1. Asymptotic expansions in perturbative quantum ﬁeld theory. Perturbative ex-
pansions in quantum ﬁeld theories are often mathematically deﬁned but typically lead to
Date: 29 November 2020.
Key words and phrases: Chern-Simons theory, holomorphic blocks, state-integrals, knots, 3-manifolds,
resurgence, perturbative series, Borel resummation, Stokes automorphisms, Stokes constants, q-holonomic
modules, q-diﬀerence equations, BPS states, Kashaev invariant, colored Jones polynomial.
1
arXiv:2007.10190v2  [hep-th]  2 Dec 2020
2 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARI ˜NO
factorially divergent formal power series. Important examples are the perturbative expan-
sions of the partition function of 3-dimensional manifolds (with, or without boundary) in
complex Chern-Simons theory with arbitrary gauge group. For instance, in [GLMn08] it
was shown that the LMO invariant of a 3-manifold (which is the perturbative expansion of
the Witten-Reshetikhin-Turaev invariant at the trivial ﬂat collection and arbitrary gauge
group), is a Gevrey-1 formal power series, that is a formal power series whose nth coeﬃ-
cient is bounded by n!Cn for some positive constant C. Said diﬀerently, these perturbative
expansions have Borel transforms which are germs of holomorphic functions at the origin.
In [Gar08] it was conjectured that the perturbative expansions in complex Chern-Simons
theory are resurgent functions, and more precisely that they have analytic continuation as
multivalued functions in the complex plane minus a discrete and computable set of points,
placed in ﬁnitely many vertical lines in the complex plane. These vertical lines are formed by
an inﬁnite towers of singularities, with a 2 πi periodicity. The position of these singularities
is dictated by the values of the complex Chern-Simons function (a C /2πiZ -valued function)
on the set of ﬂat connections.
1.2. Resurgence in complex Chern-Simons theory. In what follows, we will identify
the partition function of complex Chern-Simons theory with the state integral of Andersen-
Kashaev in [AK14], following the ideas of Hikami, Dimofte et al [Hik07, DGLZ09]. Although
this identiﬁcation has not been derived from ﬁrst principles, it turns out to have a number
of startling consequences. We will focus on manifolds of the form M = S3\K, whereK is a
hyperbolic knot.
Our goal is to give an explicit description of the resurgent structure of the formal power
series of perturbative Chern-Simons theory in terms of a fundamental solution of a pair of
linearq-diﬀerence equation and a matrix of integers. We will describe the general story ﬁrst,
and illustrate it with concrete examples later.
We will denote by P the set of critical points of the complex Chern-Simons action and
by σ a typical critical point. Given our identiﬁcation of Chern-Simons theory with state
integrals, it turns out that the setP coincides with the set of critical points of the integrand
of the state integral, an eﬀectively computable set of algebraic numbers. The critical val-
ues of the complex Chern-Simons function are labeled by σ and an integer µ (often called
“multicovering”):
CS(σ;µ) = V (σ)
2π − 2πiµ, µ ∈ Z . (1)
We conjecture that the corresponding transseries Φσ,µ satisfy the translation invariance prop-
erty
Φσ,µ(τ) = ˜qµ Φσ(τ), ˜q = e−2πi/τ, (2)
where Φσ(τ) is the conventional asymptotic expansion of the state integral around the saddle
point σ. It has the form
Φσ(τ) = exp
(V (σ)
2πτ
)
ϕσ(τ), ϕ σ(τ)∈ C [[τ]]. (3)
As a consequence, all the Stokes automorphisms acting on Φ σ,µ are packaged in two Stokes
automorphism matrices S+(q), S−(q−1), which are matrices of q- and q−1-series respectively,
THE RESURGENT STRUCTURE OF QUANTUM KNOT INV ARIANTS 3
and each of which encodes Stokes automorphism across a half-plane. Their detailed deﬁnition
is given in Section 5.1.
An important feature of state integrals is that they depend on additional parameters and
this leads to a system of a pair of linearq-diﬀerence equations, one in the upper half-plane and
another in the lower half-plane [GK17]. In our examples, these linear q-diﬀerence equations
have explicit sets of fundamental solutions. We conjecture that
Conjecture 1. (a) S±(q) are bilinear functions of two fundamental solutions of the pair of
linear q-diﬀerence equations.
(b) S±(q) satisfy the inversion relation
S+(q)T S−(q) = 1. (4)
(c) S±(q) are uniquely determined by S+(0), S−(0) and a pair of fundamental solutions to
the pair of linear q-diﬀerence equations.
The above matrices S± uniquely determine the collection of transseries Φσ,µ(τ) for all (σ,µ )
via an abstract Riemann-Hilbert correspondence ﬁrst pointed out in [Vor83] and developed
recently in [GMN10, IMnS19, KS20]. Note that this transcendental correspondence converts
the diﬃcult problem of computing coeﬃcients of Φ σ,µ(τ) (typically, one can not compute
more than a couple of hundred coeﬃcients) into the much easier problem of computing
fundamental solutions of linear q-diﬀerence equations, up to a matrix of unknown integers.
Given a hyperbolic knotK there is a distinguished critical pointσ1 (the geometric represen-
tation, corresponding to the complete hyperbolic structure), and in that case we conjecture
a precise relation between the entry S+
σ1,σ1(q) of the matrix S+(q) and the (rotated) 3D-index
of Dimofte-Gaiotto-Gukov [DGG14, DGG13].
Conjecture 2. We have:
S+
σ1σ1(q) = Ind rot
K (q). (5)
We recall that the 3D-indexIK(m,e )(q) associated to a knot K is labeled by two integers
(m,e ). It counts BPS states in a three-dimensional,N = 2 supersymmetric theoryTM which
can be associated to the manifold M = S3\K [DGG14]. The rotated index is then given by
Indrot
K (q) =
∑
e∈Z
IK(0,e )(q). (6)
The relation in (5) between the resurgent structure of complex Chern–Simons theory and
a counting of BPS states in the corresponding supersymmetric theory was anticipated in
[Mn19, GGMn20b].
We emphasize that although the state integrals and their perturbation theory are well-
deﬁned, the above picture is largely conjectural. However, it ﬁts well with the work of
Kontsevich-Soibelman [KS11], as well as with a lecture of Kontsevich on June 30, 2020
[Kon20], and it paves the way for a deeper understanding of the topological/physical meaning
of the integers appearing in S±.
We should point out that the above theory in fact has little to do with knots and 3-
manifolds and complex Chern-Simons theory, and little to do with the Bloch group, but
appears to be part of a larger combinatorial structure. This is apparent in the data needed
4 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARI ˜NO
to deﬁne the formal power series of [DG13, DG18] as well as the data needed to deﬁne q-
hypergeometric Nahm sums (and thus their asymptotic expansion at roots of unity [GZa])
and the data needed to deﬁne state integrals [GK17]. This combinatorial structure is some-
times called a K2-Lagrangian, or an extended symplectic group.
We will illustrate the above conjectures concretely for the invariants of the two simplest
hyperbolic knots, the 41 and the 52 knots. Some aspects of the resurgent structure of complex
Chern–Simons theory for the 4 1 knot were studied in [GMnP, GH18], but they focused on
the “classical” transseries Φσ(τ) (i.e. they didn’t address the resurgent structure of the tower
of singularities). The resurgent problem in the case of compact SU(2) Chern–Simons theory
was addressed in [CG11, GMnP], where complete towers of Stokes constants were explicitly
computed for some Seifert three-manifolds.
This paper is, in a sense, a sequel to [GZc] and [GZb] which the reader can consult for
further information, motivation, historical presentation, as well as for the connection with
the asymptotics of the Kashaev invariant and with the quantum modularity conjecture.
Note that our notation ϕσ(τ) from Equation (3) corresponds to the notation Φ (σ)
0 (2πix)
of [GZc]. In particular, the coeﬃcient of τn in ϕσ(τ) is (up to multiplication by an eighth
root of unity and the square root of an nonzero element of Fσ) in (2πi)nFσ, where Fσ is the
trace ﬁeld of σ.
2. The equation (1−x)(1−x−1) = 1 and the 41 knot
The state integral of the 4 1 knot is given by Equation (39) below with (A,B ) = (1, 2) and
µ =λ = 0. The critical points of the integrand are solutions of the algebraic equation
(1−x)(1−x−1) = 1. (7)
The latter has two solutions ξ1 = e 2πi/6 and ξ2 = e−2πi/6 which lie in the number ﬁeld
Q (√−3), the trace ﬁeld of the 4 1 knot. The corresponding series Φ σj(τ) satisfy the relation
Φσ2(τ) = iΦσ1(−τ) and the ﬁrst few terms of ϕσ1(τ/(2πi))∈ 3−1/4Q (√−3)[[τ]] are given by
ϕσ1
( τ
2πi
)
= 1
4√
3
(
1 + 11τ
72√−3 + 697τ 2
2 (72√−3)2 + 724351τ 3
30 (72√−3)3 +···
)
. (8)
The exponent in (3) involves the hyperbolic volume of the 4 1 knot complement
V (σ1) =V = 2Im Li2(eiπ/3) = 2.029883... . (9)
The two series Φσj(τ) for j = 1, 2 form a vector
Φ(τ) =
(
Φσ1(τ)
Φσ2(τ)
)
(10)
that also appears in the reﬁned quantum modularity conjecture [GZc]. Φ( τ) is the vector of
series whose description in Borel plane we wish to give.
Consider the linear q-diﬀerence equation
ym+1(q)− (2−qm)ym(q) +ym−1(q) = 0 ( m∈ Z ). (11)
THE RESURGENT STRUCTURE OF QUANTUM KNOT INV ARIANTS 5
It has a fundamental solution set given by the columns of the following matrix
Wm(q) =
(
G0
m(q) G1
m(q)
G0
m+1(q) G1
m+1(q)
)
, (12)
where G0
m(q) and G1
m(q) are deﬁned by
G0
m(q) =
∞∑
n=0
(−1)nqn(n+1)/2+mn
(q;q)2
n
(13a)
G1
m(q) =
∞∑
n=0
(−1)nqn(n+1)/2+mn
(q;q)2
n
(
2m +E1(q) + 2
n∑
j=1
1 +qj
1−qj
)
, (13b)
and E1(q) = 1− 4∑∞
n=1qn/(1−qn) is the Eisenstein series.
It is easy to see that G0
m satisﬁes (11). Indeed, G0
m(q) =∑∞
n=0an,−m(q)−1 where an,m(q)
is given in (34) below. Equations (35a)-(35c), applied to an,−m(q)−1 conclude the result. A
similar proof applies for G1
m. Another way to do so is to use the state integral (39) (with
(A,B ) = (1, 2)) and show that the latter satisﬁes the linear q-diﬀerence equation (11) in two
ways, one with respect to the variable λ and another with respect to the variable µ.
The fundamental solution Wm(q) satisﬁes
det(Wm(q)) = 2 (14)
and the symmetry
Wm(q−1) =W−m(q)
(
1 0
0 −1
)
, (15)
and the orthogonality
1
2Wm(q)
(
0 1
−1 0
)
Wm(q)T =
(
0 1
−1 0
)
. (16)
for all integers m, as well as
1
2Wm(q)
(
0 1
−1 0
)
W𝓁(q)T∈ SL(2, Z [q, 1/q]) (17)
for all integers m,𝓁 . The S matrix is given by
S+(q) = 1
2
(
0 1
1 1
)
W−1(q)
(
0 1
1 0
)
W−1(q)T
(
0 −1
1 2
)
, (18a)
S−(q) = 1
2
(
−1 −1
0 1
)
W−1(q)
(
0 1
1 0
)
W−1(q)T
(
1 0
−2 1
)
. (18b)
The above matrix S satisﬁes Equation (4).
3. The equation x−2(1−x)3 = 1 and the 52 knot
The state integral of the 5 2 knot is given by Equation (39) below with (A,B ) = (2, 3) and
µ =λ = 0. The critical points of the integrand are solutions of the algebraic equation
x−2(1−x)3 = 1. (19)
6 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARI ˜NO
The above equation (which deﬁnes a cubic ﬁeld of discriminant −23, the trace ﬁeld of the
52 knot) has three solutions ξ1 = 0.78492 + 1.30714... i, ξ2 = 0.78492− 1.30714... i and
ξ3 = 0.43016... , corresponding to the geometric representation, its conjugate and the real
representation. The corresponding series Φ σj(τ) satisfy Φ σ2(τ) = −iΦσ1(−τ) and the ﬁrst
few terms of φσj(τ/(2πi)) are given by
ϕσj
( τ
2πi
)
=
(−3ξ2
j + 3ξj− 2
23
)1/4(
1 + 33ξ2
j + 242ξj− 245
22· 232 τ + 100250ξ2
j− 12643ξj + 2732
25· 233 τ 2
+−50198891ξ2
j + 35443870ξj− 79016748
27· 3· 5· 235 τ 3
+−3809943572ξ2
j + 1861268771ξj + 1015686665
211· 3· 5· 236 τ 4 +...
)
. (20)
The exponent in (3) involves
V (σ1) = 2.821... + 1.379... i, V(σ2) =−2.821... + 1.379... i, V(σ3) =−2.758... (21)
whereℜV (σ1) is the hyperbolic volume of the 5 2 knot complement, andℑV (σ1) =ℑV (σ2)
the Chern-Simons action. The three series Φ σj(τ) for j = 1, 2, 3 form a vector
Φ(τ) =


Φσ1(τ)
Φσ2(τ)
Φσ3(τ)

. (22)
Consider the linear q-diﬀerence equation
ym(q)− 3ym+1(q) + (3−q2+m)ym+2(q)−ym+3(q) = 0. (23)
The above equation has a fundamental solution set given by the columns of the following
matrix
Wm(q) =



W +
m(q), |q|< 1,

0 0 1
0 1 0
1 0 0

W−
−m−2(q−1)


1 0 0
0 −1 0
0 0 1

, |q|> 1. (24)
where the matrices Wε
m(q) with ε =± are respectively
Wε
m(q) =


Hε
0,m(q) Hε
1,m(q) Hε
2,m(q)
Hε
0,m+1(q) Hε
1,m+1(q) Hε
2,m+1(q)
Hε
0,m+2(q) Hε
1,m+2(q) Hε
2,m+2(q)

 (25)
and Hε
j,m(q) are given in Appendix A for j = 0, 1, 2 and m∈ Z .
The fundamental solutions satisfy
det(Wm(q)) = 2, (26)
for all integers m as well as
1
2Wm(q)


0 0 1
0 2 0
1 0 0

W𝓁(q−1)T∈ SL(3, Z [q, 1/q]) (27)
THE RESURGENT STRUCTURE OF QUANTUM KNOT INV ARIANTS 7
for all integers m,𝓁 . In particular, we have:
1
2Wm−1(q)


0 0 1
0 2 0
1 0 0

W−m−1(q−1)T =


1 0 0
0 0 1
0 1 3 −qm

 . (28)
The S matrix is given by
S+(q) = 1
2


0 1 0
0 1 1
−1 0 0

W−1(q−1)


0 0 1
0 −2 0
1 0 0

W−1(q)T


0 0 −1
1 1 0
0 1 0

, (29a)
S−(q) = 1
2


0 3 −1
0 −1 0
1 0 0

W−1(q)


0 0 1
0 −2 0
1 0 0

W−1(q−1)T


0 0 1
3 −1 0
−1 0 0

 . (29b)
The above matrix S satisﬁes Equation (4). A proof is given in Appendix A.2.
