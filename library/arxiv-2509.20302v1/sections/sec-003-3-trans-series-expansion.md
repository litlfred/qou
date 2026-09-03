---
doc_id: arxiv-2509.20302v1
doc_title: "Universality in the resurgence of generalized Tracy-Widom distributions"
section_id: sec-003-3-trans-series-expansion
section_title: "Trans-series expansion"
section_number: 3
pages: 2-3
source_pdf: 2509.20302v1.pdf
source_sha256: 59837f5b511c9e07
doc_brief: "Universality in the resurgence of generalized Tracy-Widom distributions — We analyze determinants associated with Bessel kernels and generic symbol functions, which govern a class of ob- servables"
---
Based on the previous results [30, 31], concrete ex-
amples and many consistency checks we conjecture that
the strong coupling expansion (valid for g > 0) has the
trans-series structure
D(g) = Ae4πg∑i(xi−yi)g
β2+2ℓβ
2
×
(7)
∑
{δi=0,1}
e−8πg∑i δixiS{δi}D{δi}(g)
where D{δi}(g) are asymptotic series in g−1, e−8πgxi
are non-perturbative scales and S{δi} are their corre-
sponding Stokes constants. A is a convenient normaliza-
tion, which can be calculated from χ [21]. The generic
framework to calculate the trans-series for the logarithm
of the determinant already provides a similar structure.
The simplification is that the sum involves only at most
once each non-perturbative scale, so no higher power
appears (similarly to the expectation value of the Wilson
loop). In particular, if we have only a finite number of
zeros, then the trans-series contains only a finite number
of non-perturbative corrections.
The logarithm of the perturbative part lnD{0,0,...}(g)
was already calculated in [12, 13]. After exponential-
ization we parametrize it as
D{}(g) ≡D{0,0,...}(g) =
∞
∑
k=0
D{}
k g−k
(8)
by introducing the convention that in the upper index we
list the nonzero δs only. The coefficients can be calcu-
lated from a system of integro-differential equation with
the first few coefficients being [12, 13]:
D{}
0 = 1
;
D{}
1 =
1−4ℓ2
β
16
I1
(9)
D{}
2 =
16ℓ4
β −40ℓ2
β +9
512
I2
1
;
ℓβ = ℓ+β
D{}
3 = −

16ℓ4
β −40ℓ2
β +9

(4ℓ2
β −17)I3
1 +8I2

24576
2
in terms of the moments:
In = (−1)n−1 ∑
k≥1

1
(2πxk)2n−1 −
1
(2πyk)2n−1

(10)
We choose S{} = 1, which fixes A uniquely. Assign-
ing the degree n to In we can show that only terms with
degree up to the given order appear. Higher order ex-
pressions, D{}
k>3, can be obtained from [12, 13] by ex-
ponentiation.
The leading non-perturbative correction is related to
the nearest zero x1, has magnitude e−8πgx1, and can be
parametrized as
D{1}(g) ≡D{1,0,...}(g) =
∞
∑
k=0
D{1}
k
g−k
(11)
Using the methods developed in [30, 31] the coefficients
can be determined to be
D{1}
0
= 1
;
D{1}
1
=

1−4ℓ2
β

(πx1I1 −1)
16πx1
,
(12)
D{1}
2
=

16ℓ4
β −40ℓ2
β +9

(πx1I1 −1)2
512π2x2
1
D{1}
3
= −

16ℓ4
β −40ℓ2
β +9

24576π3x3
1

4ℓ2
β(πx1I1 −1)3+
8π3x3
1I2 −17πx1I1(πx1I1(πx1I1 −3)+3)+19

and the corresponding Stokes constant is [21, 30, 31]
S{1} = eiπℓβ
4πx1
Φ(2iπx1)
Φ′(−2iπx1)
(13)
= −ieiπℓβ ∏
j>1
(x1 +xj)
(x1 −xj) ∏
j
(x1 −yj)
(x1 +yj)
We have calculated many more terms, D{1}
k
, for k =
4,... and observed that the perturbative part can be
mapped to the leading non-perturbative correction by
the replacements In →In +
2(−1)n
(2πx1)2n−1 .
This is a very interesting result and has far-reaching
consequences.
First, it implies that the two asymp-
totic series D{} and D{1} have the same perturba-
tive expansion in terms of their own moments I{}
n
≡
In and I{1}
n
= I{}
n +
2(−1)n
(2πx1)2n−1 .
From the defini-
tion of the moments it is clear, that if I{}
n
corre-
sponds to {x1,x2,...|y1,y2,...} then I{1}
n
corresponds to
{−x1,x2,...|y1,y2,...} ≡{x2,...|x1,y1,y2,...}. This
10
20
30
40
50
60
70
-1.5917
-1.5916
-1.5915
-1.5914
-1.5913
Figure 1: Asymptotic behaviour of D{}
k
for x1 = 1,x2 = 3/2. We
present the asymptotic series (blue) and its first 3 (yellow, green, red)
Richardson transforms against the asymptotical value −5/π, which
includes the Stokes constant S{1}. We zoomed to the first 70 coeffi-
cients for visibility, but we performed the test with 200 terms and also
at higher orders.
nicely matches with the magnitude of the correction
e−8πgx1, which alltogether with the e4πgx1 prefactor flips
also the sign of x1 in the exponent. Formally we are
turning x1 to a new y. We can then think of D{1} as
the perturbative part corresponding to the symbol Φ{1}
labeled by {x2,...|x1,y1,y2,...}.
In the case of the Wilson loop, when we have only
one x1, the transformation x1 →−x1 changes the sign
of every moment, which leads to the observed wn →
(−1)nwn relation.
