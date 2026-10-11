---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-011-convergence-of-the-magnus-series
section_title: "Convergence of the Magnus series"
section_number: null
pages: 16-18
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
2.7.1. On the existence of Ω(t)
In most cases, one is interested in the case where A belongs to a Lie algebra g under the commutator product. In this
general setting, the Magnus theorem can be formulated as four statements concerning the solution of Y ′ = A(t)Y, each one
more stringent than the preceding [16]. Specifically,
(A) The differential equation Y ′ = A(t)Y has a solution of the form Y(t) = exp Ω(t).
(B) The exponent Ω(t) lies in the Lie algebra g.
(C) The exponent Ω(t) is a continuous differentiable function of A(t) and t, satisfying the nonlinear differential equation
Ω′ = d exp−1
Ω(A(t)).
(D) The operator Ω(t) can be computed by the Magnus series (40).
Let us now analyze in detail the conditions under which statements (A)–(D) hold.
(A) If A(t) and Y(t) are n× n matrices, from well-known general theorems on differential equations it is clear that the initial
value problem defined by (30) and Y(0) = I always has a uniquely determined solution Y(t) which is continuous and has
a continuous first derivative in any interval in which A(t) is continuous [63]. Furthermore, the determinant of Y is always
different from zero, since
det Y(t) = exp
Z t
0
tr A(s)ds

.
On the other hand, it is well known that any matrix Y can be written in the form exp Ωif and only if det Y̸ = 0 [64, p. 239],
so that it is always possible to write Y(t) = exp Ω(t).
In the general context of Lie groups and Lie algebras, it is indeed the regularity of the exponential map from the Lie algebra
g to the Lie group G that determines the global existence of an Ω(t) ∈g [65,66]: the exponential map of a complex Lie algebra
is globally one-to-one if and only if the algebra is nilpotent, i.e. there exists a finite n such that adx1adx2 · · · adxn−1xn = 0,
where xj are arbitrary elements from the Lie algebra. In general, however, the injectivity of the exponential map is only
assured for ξ ∈g such that ∥ξ∥< ρG for a real number ρG > 0 and some norm in g [32,67].
(B) Although in principle ρG constitutes a sharp upper bound for the mere existence of the operator Ω∈g, its practical
value in the case of differential equations is less clear. As we have noticed, any nonsingular matrix has a logarithm, but this
logarithm might be in gl(n, C) even when the matrix is real. The logarithm of Y(t) may be complex even for real A(t) [16].
In such a situation, the solution of (30) cannot be written as the exponential of a matrix belonging to the Lie algebra over the
field of real numbers. One might argue that this is indeed possible over the field of complex numbers, but (i) the element
Ωcannot be computed by the Magnus series (40), since it contains only real rational coefficients, and (ii) examples exist
where the logarithm of a complex matrix does not lie in the corresponding Lie subalgebra [16].
It is therefore interesting to determine for which range of t a real A(t) in (30) leads to a real logarithm. This issue has
been tackled by Moan in [67] in the context of a complete normed (Banach) algebra, proving that if
Z t
0
∥A(s)∥2ds < π
(67)
then the solution of (30) can indeed be written as Y(t) = exp Ω(t), where Ω(t) is in the Banach algebra.
S. Blanes et al. / Physics Reports 470 (2009) 151–238
167
(C) In his original paper [4], Magnus was well aware that if the function Ω(t) is assumed to be differentiable, it may not exist
everywhere. In fact, he related the differentiability issue to the problem of solving d expΩ(Ω′) = A(t) with respect to Ω′
and provided an implicit condition for an arbitrary A. More specifically, he proved the following result for the case of n × n
matrices (Theorem V in [4]).
Theorem 5. The equation A(t) = d expΩ(Ω′) can be solved by Ω′ = d exp−1
ΩA(t) for an arbitrary n × n matrix A if and only if
none of the differences between any two of the eigenvalues of Ωequals 2πim, where m = ±1, ±2, . . . , (m̸ = 0).
This result can be considered, in fact, as a reformulation of Lemma 3, but, unfortunately, does not have very much practical
application unless the eigenvalues of Ωcan easily be determined from those of A(t). One would instead like to have
conditions based directly on A.
2.7.2. Convergence of the Magnus series
For dealing with the validity of statement (D) one has to analyze the convergence of the series P∞
k=1 Ωk. Magnus also
considered the question of when the series terminates at some finite index m, thus giving a globally valid Ω= Ω1+· · ·+Ωm.
This will happen, for instance, if

A(t),
Z t
0
A(s)ds

= 0
identically for all values of t, since then Ωk = 0 for k > 1. A sufficient (but not necessary) condition for the vanishing of all
terms Ωk with k > n is that
[A(s1), [A(s2), [A(s3), . . . , [A(sn), A(sn+1)] . . .]]] = 0
for any choice of s1, . . . , sn+1. In fact, the termination of the series cannot be established solely by consideration of the
commutativity of A(t) with itself, and Magnus considered an example illustrating this point.
In general, however, the Magnus series does not converge unless A is small in a suitable sense. Several bounds to the
actual radius of convergence in terms of A have been obtained in the literature. Most of these results can be stated as
follows. If Ωm(t) denotes the homogeneous element with m −1 commutators in the Magnus series, as given by (51), then
Ω(t) = P∞
m=1 Ωm(t) is absolutely convergent for 0 ≤t < T, with
T = max

t ≥0 :
Z t
0
∥A(s)∥2ds < rc

.
(68)
Thus, both Pechukas and Light [15] and Karasev and Mosolova [68] obtained rc = log 2 = 0.693147 . . . , whereas Chacon
and Fomenko [69] got rc = 0.57745 . . .. In 1998, Blanes et al. [30] and Moan [70] obtained independently the improved
bound
rc =
1
2
Z 2π
0
1
2 + x
2(1 −cot x
2)
dx ≡ξ = 1.08686870 . . .
(69)
by analyzing the recurrence (49)–(50) and (51), respectively. Furthermore, Moan also obtained a bound on the individual
terms Ωm of the Magnus series [67] which is useful, in particular, for estimating errors when the series is truncated.
Specifically, he showed that
∥Ωm(t)∥≤
fm
2

2
Z t
0
∥A(s)∥2ds
m
≤π

1
ξ
Z t
0
∥A(s)∥2 ds
m
,
where fm are the coefficients of
G−1(x) =
X
m≥1
fmxm = x +
1
4
x2 +
5
72
x3 +
11
576
x4 +
479
86 400
x5 + · · · ,
the inverse function of
G(s) =
Z s
0
1
2 + x
2(1 −cot x
2)
dx.
On the other hand, by analyzing some selected examples, Moan [67] concluded that, in order to get convergence for all
real matrices A(t), it is necessary that rc ≤π in (68), and more recently Moan and Niesen [71] have been able to prove that,
indeed, rc = π provided only real matrices are involved.
In any case, it is important to remark that statement (D) is locally valid, but cannot be used to compute Ωin the large.
However, as we have seen, the other statements need not depend on the validity of (D). In particular, if (B) and (C) are
globally valid, one can still investigate many of the properties of Ω, even though one cannot compute it with the aid of (D).
168
S. Blanes et al. / Physics Reports 470 (2009) 151–238
