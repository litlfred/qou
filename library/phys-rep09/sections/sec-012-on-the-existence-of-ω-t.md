---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-012-on-the-existence-of-ω-t
section_title: "On the existence of Ω (t)"
section_number: null
pages: 16-17
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
In most cases, one is interested in the case where A belongs to a Lie algebra g under the commutator product. In this
general setting, the Magnus theorem can be formulated as four statements concerning the solution of Y’ = A(t)Y, each one
more stringent than the preceding [16]. Specifically,

(A) The differential equation Y’ = A(t)Y has a solution of the form Y(t) = exp 2(t).

(B) The exponent {2(t) lies in the Lie algebra g.

(C) The exponent £2(t) is a continuous differentiable function of A(t) and t, satisfying the nonlinear differential equation
Q! = dexpy' (A(t).

(D) The operator §2(t) can be computed by the Magnus series (40).

Let us now analyze in detail the conditions under which statements (A)-(D) hold.

(A) If A(t) and Y(t) aren x n matrices, from well-known general theorems on differential equations it is clear that the initial
value problem defined by (30) and Y(0) = J always has a uniquely determined solution Y(t) which is continuous and has
a continuous first derivative in any interval in which A(t) is continuous [63]. Furthermore, the determinant of Y is always
different from zero, since

det Y(t) = exp (/ tra(sas) :
0

On the other hand, it is well known that any matrix Y can be written in the form exp if and only if det Y 4 0 [64, p. 239],
so that it is always possible to write Y(t) = exp Q(t).

In the general context of Lie groups and Lie algebras, it is indeed the regularity of the exponential map from the Lie algebra
gto the Lie group g that determines the global existence of an 82(t) € g [65,66]: the exponential map of a complex Lie algebra
is globally one-to-one if and only if the algebra is nilpotent, i.e. there exists a finite n such that ad,, ad, ---ady,_ Xn = 0,
where x; are arbitrary elements from the Lie algebra. In general, however, the injectivity of the exponential map is only
assured for € € g such that ||&|| < 9 for areal number pg > 0 and some norm in g [32,67].

(B) Although in principle pg constitutes a sharp upper bound for the mere existence of the operator 2 € 4, its practical
value in the case of differential equations is less clear. As we have noticed, any nonsingular matrix has a logarithm, but this
logarithm might be in gl(n, C) even when the matrix is real. The logarithm of Y(t) may be complex even for real A(t) [16].
In such a situation, the solution of (30) cannot be written as the exponential of a matrix belonging to the Lie algebra over the
field of real numbers. One might argue that this is indeed possible over the field of complex numbers, but (i) the element
2 cannot be computed by the Magnus series (40), since it contains only real rational coefficients, and (ii) examples exist
where the logarithm of a complex matrix does not lie in the corresponding Lie subalgebra [16].

It is therefore interesting to determine for which range of t a real A(t) in (30) leads to a real logarithm. This issue has
been tackled by Moan in [67] in the context of a complete normed (Banach) algebra, proving that if

| IA(s) lads < x (67)
0

then the solution of (30) can indeed be written as Y(t) = exp 2(t), where £2 (t) is in the Banach algebra.
S. Blanes et al. / Physics Reports 470 (2009) 151-238 167

(C) In his original paper [4], Magnus was well aware that if the function 2(t) is assumed to be differentiable, it may not exist
everywhere. In fact, he related the differentiability issue to the problem of solving d exp, (S2’) = A(t) with respect to 2’
and provided an implicit condition for an arbitrary A. More specifically, he proved the following result for the case of n x n
matrices (Theorem V in [4]).

Theorem 5. The equation A(t) = d expg (2) can be solved by 2' = d expy' A(t) for an arbitrary n x n matrix A if and only if
none of the differences between any two of the eigenvalues of 92 equals 2xim, where m = +1, +2,..., (m# 0).

This result can be considered, in fact, as a reformulation of Lemma 3, but, unfortunately, does not have very much practical
application unless the eigenvalues of 2 can easily be determined from those of A(t). One would instead like to have
conditions based directly on A.
