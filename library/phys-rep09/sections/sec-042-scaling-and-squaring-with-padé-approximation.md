---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-042-scaling-and-squaring-with-padé-approximation
section_title: "Scaling and squaring with Padé approximation"
section_number: null
pages: 61-62
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
Among one of the least dubious ways of computing exp(C) is by scaling and squaring in combination with a diagonal
Padé approximation [139]. The procedure is based on a fundamental property of the exponential function, namely
eC = (eC/j)j
for any integer j. The idea, then, is to choose j to be a power of two for which exp(C/j) can be reliably and efficiently computed,
and then to form the matrix (exp(C/j))j by repeated squaring. If the integer j is chosen as the smallest power of two for which
∥C∥/j < 1, then exp(C/j) can be satisfactorily computed by diagonal Padé approximants of order, say, m. This is roughly the
method used by the built-in function expm in Matlab.
For the integrators based on the Magnus expansion, as C = O(hp) with p ≥1, one usually gets good approximations
with relatively small values of j and m.
As is well known, diagonal Padé approximants map the Lie algebra oJ(n) to the J-orthogonal Lie group OJ(n) and thus
also constitute a valid alternative to the evaluation of the exponential matrix in Magnus-based methods for this particular
Lie group. More specifically, if B ∈oJ(n), then ψ2m(tB) ∈OJ(n) for sufficiently small t ∈R, with
ψ2m(λ) =
Pm(λ)
Pm(−λ),
(276)
provided the polynomials Pm are generated according to the recurrence
P0(λ) = 1,
P1(λ) = 2 + λ
Pm(λ) = 2(2m −1)Pm−1(λ) + λ2Pm−2(λ).
212
S. Blanes et al. / Physics Reports 470 (2009) 151–238
Moreover, ψ2m(λ) = exp(λ) + O(λ2m+1) and ψ2 corresponds to the Cayley transform (262), whereas for m = 2, 3 we have
ψ4(λ) =

1 +
1
2λ +
1
12λ2
 

1 −
1
2λ +
1
12λ2

ψ6(λ) =

1 +
1
2λ +
1
10λ2 +
1
120λ3
 

1 −
1
2λ +
1
10λ2 −
1
120λ3

.
Thus, we can combine the optimized approximations to Ωobtained in Section 5.4 for Magnus based methods with diagonal
Padé approximants, up to the corresponding order, to obtain time-symmetric integration schemes preserving the algebraic
structure of the problem without computing the matrix exponential. For instance, the ‘‘Magnus–Padé’’ methods thus
obtained involve, in addition to one matrix inversion, 3 and 8 matrix–matrix products for order 4 and 6, respectively.
Observe that since Ω[2n] = O(h) then
ψ2m(Ω[2n]) = exp(Ω[2n]) + O(h2k+1),
where k = min{m, n}. With m = n we have a method of order 2n. However, for some problems, this rational approximation
to the exponential may be not very accurate depending on the eigenvalues of Ω[2n]. In this case, one may take m > n, thus
giving a better approximation to the exponential and a more accurate result by slightly increasing the computational cost
of the method. Of course, when the norm of the matrix Ω[2n] is not so small, this technique can be combined with scaling
and squaring [142].
Instead of using Padé approximants for the exponential of the scaled matrix B ≡C/2k, Najfeld and Havel [143] propose
a rational approximation for the matrix function
H(B) = B coth(B) = B
e2B + I
e2B −I ,
(277)
from which the exponential can be obtained as
e2B =
H(B) + B
H(B) −B
and then iteratively square the result k times to recover the exponential of the original matrix C. From the continued fraction
expansion of H(B), it is possible to compute the first rational approximations as
H2(B) =
I + 2
5B2
I +
1
15B2 ,
H4(B) =
I + 4
9B2 +
1
63B4
I + 1
9B2 +
1
945B4
and so on. Observe that the representation (277) can be regarded as a generalized Cayley transform of B and thus it also
provides approximations in the group OJ(n). In [143] the authors report a saving of about 30% in the number of matrix
multiplications with respect to diagonal Padé approximants when an optimal k and a rational approximation for H(B) is
used.
