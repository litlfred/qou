---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-043-chebyshev-approximation
section_title: "Chebyshev approximation"
section_number: null
pages: 62-63
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
Another valid alternative is to use polynomial approximations to the exponential of C as a whole. Suppose, in particular,
that C is a matrix of the form C = −iτH, with H Hermitian and τ > 0, as is the case in Quantum Mechanics. In the
Chebyshev approach, the evolution operator exp(−iτH) is expanded in a truncated series of Chebyshev polynomials, in
analogy with the approximation of a scalar function [144]. As is well known, given a function F(x) in the interval [−1, 1], the
Chebyshev polynomial approximations are optimal, in the sense that the maximum error in the approximation is minimal
compared to almost all possible polynomial approximations [145]. To apply this procedure, one has to previously bound the
extreme eigenvalues Emin and Emax of H. Then a truncated Chebyshev expansion of exp(−ix) on the interval [τEmin, τEmax]
is considered:
exp(−ix) ≈
m
X
n=0
cnPn(x),
where
Pn(x) = Tn

2x −τEmax −τEmin
τEmax −τEmin

with appropriately chosen coefficients cn. Here Tn(x) are the Chebyshev polynomials on the interval [−1, 1] [45], which can
be determined via the recurrence relation
Tn+1(x) = 2xTn(x) −Tn−1(x);
T1(x) = x;
T0(x) = 1.
Finally, one uses the approximation
exp(−iτH) ≈
m
X
n=0
cnPn(τH).
(278)
S. Blanes et al. / Physics Reports 470 (2009) 151–238
213
This technique is frequently used in numerical quantum dynamics to compute exp(−iτH)ψ0 over very long times. This can
be done with m matrix-vector products if the approximation (278) is considered with a sufficiently large truncation index m.
In fact, the degree m necessary for achieving a specific accuracy depends linearly on the step size τ and the spectral radius of
H [146], and thus an increase of the step size reduces the computational work per unit step. In a practical implementation,
m can be chosen such that the accuracy is dominated by the round-off error [147]. This approach has two main drawbacks:
(i) it is not unitary, and therefore the norm is not conserved (although the deviation from unitarity is really small due to its
extreme accuracy), and (ii) intermediate results are not obtained, since, typically, τ is very large.
