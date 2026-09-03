---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-016-fourierlaplace-integrals-in-one-variable
section_title: "Fourier–Laplace integrals in one variable"
section_number: null
pages: 107-109
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
doc_brief: "Analytic Combinatorics in Several Variables — 85 sections: Preface to the second edition; List of Symbols; Introduction"
---
In this chapter we perform a systematic asymptotic study of Fourier–Laplace
integrals having the form
∫
γ
A(z) exp(−λφ(z)) dz,
as the parameter λ→∞ . The functions A andφ are called the amplitude and
phase functions, respectively (note that whenφ(z) =−iρ(z) is purely imaginary
some authors use the term phase to denote ρ rather than iρ). The univariate
setting covered in this chapter gives a basis for the multivariate case handled
in Chapter 5, which in turn underlies the asymptotic results of analytic combi-
natorics in several variables. Our main result is the following theorem, which
is proved in Section 4.2.
Theorem 4.1 (univariate Fourier–Laplace asymptotics). Let A and φ be ana-
lytic functions in a neighborhoodN⊆ C of the origin. Let
A(z) =
∞∑
j=0
b jz j
φ(z) =
∞∑
j=0
c jz j
be the power series for A and φ at the origin, and let 𝓁≥ 0 and k≥ 2 be the
indices of the least nonvanishing terms in these series, so that b 𝓁, ck , 0 and
b j = ci = 0 for any j < 𝓁and i < k. Letγ : [−ε,ε ]→C be any smooth curve
withγ(0) = 0 , γ′(0) and assume that Re{φ(γ(t))}≥ 0 with equality only at
89
90 Fourier–Laplace integrals in one variable
t = 0. Denote
I+(λ) :=
∫
γ|[0,ε]
A(z) exp(−λφ(z)) dz
I(λ) :=
∫
γ
A(z) exp(−λφ(z)) dz
C(k,𝓁 ) := Γ((1 +𝓁)/k)
k ,
where Γ is the Euler gamma function. Then there are asymptotic expansions
I+(λ)≈
∞∑
j=𝓁
a jC(k, j)(ckλ)−(1+ j)/k (4.1)
I(λ)≈
∞∑
j=𝓁
α jC(k, j)(ckλ)−(1+ j)/k (4.2)
with the following explicit description.
(i) a j is a polynomial expression, explicitly constructed in our proof, in the
values b𝓁,..., b j, c−1
k , ck+1,..., ck+ j−𝓁 whose ﬁrst two values are a 𝓁 = b𝓁
and a𝓁+1 = b𝓁+1− b𝓁
2 +𝓁
k
ck+1
ck
,
(ii) the choice of kth root in the expression (ckλ)−(1+ j)/k is made by taking the
principal root in x−1(ckλxk)1/k where x =γ′(0),
(iii) the numbers α j are related to the numbers aj by
α j =

2a j if k is even and j is even
0 if k is even and j is odd(
1−ζ j+1
)
a j if k is odd,
where
ζ =− exp
(iπ
k sgn Im{φ(γ′(0))})
.
Remarks. (i) If φ(0) =ν, 0 but Re{φ(x)} is still minimized at x = 0, then
one may apply this result by replacingφ(x) withφ(x)−ν and multiplying
the asymptotic behavior by exp(λν).
(ii) The hypothesis that the minimum of Re {φ} occurs only at 0 will be re-
moved when we reach the multivariate setting. In one variable, due to an-
alyticity, either the minimum occurs only at zero in some neighborhood
of the origin or the real part ofφ is identically zero in that neighborhood.
The analysis of a purely imaginary phase function takes place more nat-
urally with C∞ methods, which are discussed in Section 4.3 below.
