---
doc_id: arxiv-2111.04763v2
doc_title: "Resurgence of Chern-Simons theory at the trivial flat connection"
section_id: sec-010-3-the-x-variable
section_title: "The x-variable"
section_number: 3
pages: 23-27
source_pdf: 2111.04763v2.pdf
source_sha256: 760a7f9794e8baaa
toc_source: outline
doc_brief: "Resurgence of Chern-Simons theory at the trivial flat connection — Some years ago, it was conjectured by the first author that the Chern–Simons perturbation theory of a 3-manifold at the trivial flat"
---
In this section we discuss an extension of the results of Section 2 adding an x-variable. In
the context of the nth colored Jones polynomial, x = qn corresponds to an eigenvalue of the
meridian in the asymptotic expansion of the Chern–Simons path integral around an abelian
representation of a knot complement.
In the context of the state-integral of Andersen-
Kashaev [AK14], the x-variable is the monodromy of a peripheral curve. The corresponding
state-integral factorises bilinearly into holomorphic blocks, which are functions of (x, q) and
(˜x, ˜q) [BDP14].
In the context of quantum modular forms, x plays the role of a Jacobi
variable.
The corresponding perturbative series are now x-deformed (see [GGMn, Sec.5.1]), but
there are some tricky aspects of this deformation that we now discuss. The critical points of
the action, after exponentiation, lie in a plane curve S in (C∗)2 (the so-called spectral curve)
defined over the rational numbers, where (C∗)2 is equipped with coordinate functions x and
y. The field Q(S) of rational functions of S (assuming S is irreducible, or working with
one component of S at a time) can be identified with Q(x)[y]/(p(x, y)) where p(x, y) = 0
is the defining polynomial of S. The coefficients of the perturbative series are elements of
(Q(S)∗)−1/2Q(S) and the perturbative series are labeled by the branches of the projection
S →C∗corresponding to (x, y) 7→y (with discriminant δ, a rational function on S). Each
such branch σ defines locally an algebraic function y = yσ = yσ(x) ∈Q(x) satisfying the
equation p(x, yσ(x)) = 0, which gives rise to an embedding of the field of Q(S) to the field
Q(x) of algebraic functions obtained by replacing y by yσ(x). For each such branch σ, the
perturbative series has the form
Φ(σ)(x, τ) = e
V σ(x)
2πiτ φ(σ)(x, τ)
(85)
where φ(σ)(x, τ) ∈
1
√
iδσ(x)Q(x)[[2πiτ]].
The volume V σ(x) is also a function of x given
explicitly as a sum of dilogarithms and products of logarithms.
In the above discussion it is important to keep in mind that the asymptotic series (85)
are labeled by branches of the finite ramified covering S →C∗. Going around a loop in x-
space that avoids the finitely many ramified points will change the labeling of the y = y(x)
branches, and correspondingly of the asymptotic series. In the present paper (as well as
in [GGMn]), we define the asymptotic series in a neighborhood of x ∼1 of the geometric
representation, and we do not discuss the x-monodromy question.
In the case of the 41 knot, the asymptotic series associated to the geometric, and the
conjugate flat connections are given by
φ(σ1)(x;
τ
2πi) =
1
p
δ(x)

1 −i(x−3 −x−2 −2x−1 + 15 −2x −x2 + x3)
24δ(x)3
τ + . . .

φ(σ2)(x;
τ
2πi) =
i
p
δ(x)

1 + i(x−3 −x−2 −2x−1 + 15 −2x −x2 + x3)
24δ(x)3
τ + . . .

(86)
24
STAVROS GAROUFALIDIS, JIE GU, MARCOS MARIÑO, AND CAMPBELL WHEELER
where
δ(x) =
√
−x−2 + 2x−1 + 1 + 2x −x2.
(87)
The corresponding perturbative series are defined by
Φ(σ1)(x; τ) =e
A(x)
2πiτ φ(σ1)(x; τ),
Φ(σ2)(x; τ) =e−A(x)
2πiτ φ(σ2)(x; τ),
(88)
where
A(x) = 1
2 log(t)2 + 2 log(t) log(x) + log(x)2 + Li2(−tx) + Li2(−t) + π2
6 + πi log(x),
(89)
with t(x) = −1−x−1+x−iδ(x)
2
being a solution to the equation (t+x−1)+(t+x−1)−1 = x+x−1−1.
Note that when x = 1, δ(1) =
√
3, t(1) = −1+i
√
3
2
and Φ(σj)(1; τ) = Φ(σj)(τ), the latter defined
in Section 2.3.
3.1. The Φ(σ0)(x, τ) series. We begin by discussing the perturbative series φ(σ0)(x, τ) which
is a formal power series in 2πiτ whose coefficients are rational functions of x with rational
coefficients.
The series is defined by the right hand side of Equation (25) after setting
h = 2πiτ. One way to compute the ℓ-th coefficient of that series is by computing the colored
Jones polynomial, expanding in n and h as in (23) and then resumming as in (26), taking
into account the fact that the latter sum is a rational function. An alternative way is by
using Habiro’s expansion of the colored Jones polynomials [Hab02b] (see also [Hab08])
JK(x, q) =
∞
X
k=0
ck(x, q)HK
k (q),
ck(x, q) = x−k(qx; q)k(q−1x; q−1)k
(90)
where HK
k (q) ∈Z[q±] are the Habiro polynomials of the knot K and JK(qn, q) is the nth
colored Jones polynomial. The latter can be efficiently computed using a recursion (which
always exists [GL05]) together with initial conditions. This is analogous to applying the
WKB method to a corresponding linear q-difference equation [DGLZ09, Gar08b]. We com-
ment that the colored Jones polynomials of a knot K have a descendant version defined
by [GK]
DJK,(m)(x, q) =
∞
X
k=0
ck(x, q)HK
k (q) qkm,
(m ∈Z) .
(91)
Correspondingly, the Kashaev invariant has a descendant version DJK,(m)(1, q) (an element
of the Habiro ring) and the asymptotic series Φ(σ0)(x, h) have a descendant version Φ(σ0)
m (x, h)
defined for all integers m in [GK], which we will not use in the present paper.
Going back to the case of the 41 knot, we have
φ(σ0)(x;
τ
2πi) = −
1
x−1 −3 + x −
x−1 −1 + x
(x−1 −3 + x)4τ 2
(92)
−x−4 + 14x−3 + 64x−2 −156x−1 + 201 −156x + 64x2 + 14x3 + x4
12(x−1 −3 + x)7
τ 4 + . . .
(93)
RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION
25
and the corresponding perturbative series is given by Φ(σ0)(x; τ) = φ(σ0)(x; τ).
3.2. A 3×3 matrix of (x, q)-series. We now extend the results of Section 2.2 by including
the Jacobi variable x which, on the representation side, determines the monodromy of the
meridian of an SL2(C) representation σ.
Our first task is to define the 3 × 3 matrix Jm(x, q). For |q|̸ = 1, we define
Cm(x, q) =
∞
X
k=0
(−1)k
qk(k+1)/2+km
(x−1; q)k+1(x; q)k+1
Am(x, q) =
∞
X
k=0
(−1)k qk(k+1)/2+kmxk+m
(q; q)k(x2q; q)k
Bm(x, q) = Am(x−1, q).
(94)
Our series Cm(x, q) contain as a special case the series F41(x, q) in [GM21, Par20, Par]
F41(x, q) = (x1/2 −x−1/2)C0(x, q).
(95)
We assemble these (x, q)-series into a matrix
Jm(x, q) =


1
Cm(x, q)
Cm+1(x, q)
0
Am(x, q)
Am+1(x, q)
0
Bm(x, q)
Bm+1(x, q)


(96)
whose bottom-right 2 × 2 matrix is Jred
m (x, q). The properties of Jm(x, q) are summarised in
the next theorem.
Theorem 11. The matrix Jm(x, q) is a fundamental solution to the linear q-difference equa-
tion
Jm+1(x, q) = Jm(x, q)A(x, qm, q),
A(x, qm, q) =


1
0
1
0
0
−1
0
1
x−1 + x −qm+1

,
(97)
has det(Jm(x, q)) = x−1 −x and satisfies the analytic extension
Jm(x, q−1) =


1
0
0
0
0
1
0
1
0

J−m−1(x, q)


1
0
0
0
0
1
0
1
0

.
(98)
Proof. The proof is analogous to the proof of Theorem 3. Equation (97) follows quickly using
the q-hypergeometric expressions and noting that Cm(x, q) has a boundary term so satisfies
an inhomogenous version. The block form again reduces the calculation of the determinant
of Jm(x, q) to a calculation of the determinant of Jred
m (x, q) given in [GGMn]. Equation (98)
follows from the symmetry of the q-hypergeometric functions
Cm(x, q−1) = C−m(x, q)
Am(x, q−1) = B−m(x, q)
Bm(x, q−1) = A−m(x, q).
(99)
□
26
STAVROS GAROUFALIDIS, JIE GU, MARCOS MARIÑO, AND CAMPBELL WHEELER
The Appell-Lerch like sums again appear in the inverse of Jm(x, q). The proof is again
completely analogous to the proof of Theorem 4.
Theorem 12. We have
Jm(x, q)−1 =
1
x−1 −x


x−1 −x
−LBm(x, q)
LAm(x, q)
0
Bm+1(x, q)
−Am+1(x, q)
0
−Bm(x, q)
Am(x, q)


(100)
for the q-series LAm(x, q), LBm(x, q) defined by
LAm(x, q) = Am+1(x, q)Cm(x, q) −Am(x, q)Cm+1(x, q)
LBm(x, q) = Bm+1(x, q)Cm(x, q) −Bm(x, q)Cm+1(x, q)
(101)
The q-series LAm(x, q), LBm(x, q) are expressed in terms of Appell-Lerch type sums:
LAm(x, q) =
∞
X
k=0
(−1)k qk(k+1)/2+km+kxk+m+1
(q; q)k(x2q; q)k(1 −xqk)
LBm(x, q) = LAm(x−1, q) .
(102)
Proof. Given the block form of Jm(x, q) and the determinant calculated previously in Theo-
rem 11, Equation (101) follows from taking the matrix inverse. Observe that again A(x; qm, q)
has first column (1, 0, 0)t and first row (1, 0, 1). It follows that its inverse matrix has first
column (1, 0, 0)t and first row (1, 1, 0). This, together with (97), implies that
Jm+1(x, q)−1 = A(x, qm, q)−1Jm(x, q)−1
=


1
1
0
0
x + x−1 −qm+1
1
0
−1
0

Jm(x, q)−1
(103)
which implies that LAm(x, q), LBm(x, q) satisfy the first order inhomogeneous linear q-
difference equation
LAm−1(x, q) −LAm(x, q) = Am(x, q),
LBm−1(x, q) −LBm(x, q) = Bm(x, q) .
(104)
Let LAm(x, q) denote the right-hand side of the first Equation (102). Then we have
LAm−1(x, q) −LAm(x, q) =
∞
X
k=0
(−1)k qk(k+1)/2+kmxk+m(1 −xqk)
(q; q)k(x2q; q)k(1 −xqk)
= Am(x, q).
Therefore LAm(x, q) −LAm(x, q) is independent of m.
Moreover, limm→∞LAm(x, q) −
LA(0)
m (x, q) = 0 for |q|, |x| < 1 or limm→−∞LAm(x, q) −LA(0)
m (x, q) = 0 for |q|, |x| > 1.
Equations (102) follows from analytic continuation.
□
Now if we take the inverse of Jm(x, q)−1 we can get similar identities for Cm(x, q).
RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION
27
Corollary 13.
Cm(x, q) =
1
x−1 −x (Am(x, q)LBm(x, q) −Bm(x, q)LAm(x, q))
(105)
Cm+1(x, q) =
1
x−1 −x (Am+1(x, q)LBm(x, q) −Bm+1(x, q)LAm(x, q)) .
(106)
