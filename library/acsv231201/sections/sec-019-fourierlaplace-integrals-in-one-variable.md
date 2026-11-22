---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-019-fourierlaplace-integrals-in-one-variable
section_title: "Fourier–Laplace integrals in one variable"
section_number: null
pages: 107-109
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Fourier–Laplace integrals in one variable
In this chapter we perform a systematic asymptotic study of Fourier–Laplace
integrals having the form
Z
γ
A(z) exp(−λφ(z)) dz ,
as the parameter λ →∞. The functions A and φ are called the amplitude and
phase functions, respectively (note that when φ(z) = −iρ(z) is purely imaginary
some authors use the term phase to denote ρ rather than iρ). The univariate
setting covered in this chapter gives a basis for the multivariate case handled
in Chapter 5, which in turn underlies the asymptotic results of analytic combi-
natorics in several variables. Our main result is the following theorem, which
is proved in Section 4.2.
Theorem 4.1 (univariate Fourier–Laplace asymptotics). Let A and φ be ana-
lytic functions in a neighborhood N ⊆C of the origin. Let
A(z) =
∞
X
j=0
b jzj
φ(z) =
∞
X
j=0
c jzj
be the power series for A and φ at the origin, and let ℓ≥0 and k ≥2 be the
indices of the least nonvanishing terms in these series, so that bℓ, ck , 0 and
b j = ci = 0 for any j < ℓand i < k. Let γ : [−ε, ε] →C be any smooth curve
with γ(0) = 0 , γ′(0) and assume that Re{φ(γ(t))} ≥0 with equality only at
89
90 Fourier-Laplace integrals in one variable
t = 0. Denote

T,(A):= f A(z) exp(—A@(z)) dz
Yo

La): [40 exp(—Ag(z)) dz
Y

Ck := EON)

where T is the Euler gamma function. Then there are asymptotic expansions

0

T,(a) =D ajCk, leeay"" (4.1)
jal

T(a) =D ajClk, Mlegay (4.2)
j=l

with the following explicit description.

(i) aj; is a polynomial expression, explicitly constructed in our proof, in the
values be,..., bj, an Chetty «+5 Ck+j-e Whose first two values are ag = be
24+ € Chart
koe
(ii) the choice of kth root in the expression (c,a)"** is made by taking the
principal root in x"!(c,Ax*)'* where x = y'(0),
(iii) the numbers «; are related to the numbers a; by

and apy, = bes — be

if k is even and j is even
aj=40 if k is even and j is odd
(1-¢")aj;_ ifkis odd,
where
in ,
¢ = ~exp(= senim{a(y/(0))}) .

Remarks. (i) If ¢(0) = v # 0 but Re{¢(x)} is still minimized at x = 0, then
one may apply this result by replacing ¢(x) with (x) — v and multiplying
the asymptotic behavior by exp(Av).

(ii) The hypothesis that the minimum of Re{@} occurs only at 0 will be re-
moved when we reach the multivariate setting. In one variable, due to an-
alyticity, either the minimum occurs only at zero in some neighborhood
of the origin or the real part of ¢ is identically zero in that neighborhood.
The analysis of a purely imaginary phase function takes place more nat-
urally with C® methods, which are discussed in Section 4.3 below.
