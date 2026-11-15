---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-052-scaling-and-squaring-with-padé-approximation
section_title: "Scaling and squaring with Padé approximation"
section_number: null
pages: 61-62
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
Among one of the least dubious ways of computing exp(C) is by scaling and squaring in combination with a diagonal
Padé approximation [139]. The procedure is based on a fundamental property of the exponential function, namely

e& = (eH

for any integer j. The idea, then, is to choose j to be a power of two for which exp(C /j) can be reliably and efficiently computed,
and then to form the matrix (exp(C/j))! by repeated squaring. If the integer j is chosen as the smallest power of two for which
||C||/j < 1, then exp(C/j) can be satisfactorily computed by diagonal Padé approximants of order, say, m. This is roughly the
method used by the built-in function expm in Matlab.

For the integrators based on the Magnus expansion, as C = O(h?) with p > 1, one usually gets good approximations
with relatively small values of j and m.

As is well known, diagonal Padé approximants map the Lie algebra o,(n) to the J-orthogonal Lie group O,(n) and thus
also constitute a valid alternative to the evaluation of the exponential matrix in Magnus-based methods for this particular
Lie group. More specifically, if B € o,(n), then w2m(tB) € O,(n) for sufficiently small t € R, with

Pm(A)
Pm(—A)’

provided the polynomials P,, are generated according to the recurrence

Wam (a) = (276)

PoAY=1, PiAY=2+A
Pr(A) = 2(2m — 1)Pm—1(A) + 4?Pm—2(A).
212 S. Blanes et al. / Physics Reports 470 (2009) 151-238

Moreover, W2m(A) = exp(A) + O(A2"*1) and w corresponds to the Cayley transform (262), whereas for m = 2, 3 we have

War) = (14 324+ 1122?) (1- 32+ 5)
“ee 2°" 12 2°" 12

1 1... 1.3 1 1, 1.3
We(A) (: taht oe + oat ) /( st T5¥ — Tt ) .
Thus, we can combine the optimized approximations to 2 obtained in Section 5.4 for Magnus based methods with diagonal
Padé approximants, up to the corresponding order, to obtain time-symmetric integration schemes preserving the algebraic
structure of the problem without computing the matrix exponential. For instance, the “Magnus-Padé” methods thus
obtained involve, in addition to one matrix inversion, 3 and 8 matrix-matrix products for order 4 and 6, respectively.
Observe that since 2!2"! = @(h) then

Wom (2P") = exp(2") + oH),

where k = min{m, n}. With m = n we have a method of order 2n. However, for some problems, this rational approximation
to the exponential may be not very accurate depending on the eigenvalues of 2!?"!, In this case, one may take m > n, thus
giving a better approximation to the exponential and a more accurate result by slightly increasing the computational cost
of the method. Of course, when the norm of the matrix 2!2"! is not so small, this technique can be combined with scaling
and squaring [142].

Instead of using Padé approximants for the exponential of the scaled matrix B = C/2", Najfeld and Havel [143] propose
a rational approximation for the matrix function

e+]
H(B) = Bcoth(B) = B m7 5 (277)
eh — |
from which the exponential can be obtained as
25 __ H@)+B
H(B) —B

and then iteratively square the result k times to recover the exponential of the original matrix C. From the continued fraction
expansion of H(B), it is possible to compute the first rational approximations as

+ 2B 1+ 3B? + SB
H2(B) = 7. 1p’ H4(B) = 71 1p2 1 1 pa
I+ 7B I+ 5B? + 9145

and so on. Observe that the representation (277) can be regarded as a generalized Cayley transform of B and thus it also
provides approximations in the group O,(n). In [143] the authors report a saving of about 30% in the number of matrix
multiplications with respect to diagonal Padé approximants when an optimal k and a rational approximation for H(B) is
used.
