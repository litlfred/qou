---
doc_id: download
doc_title: "Concentration of empirical distribution functions with applications to non-i.i.d. models"
section_id: sec-007-high-dimensional-random-matrices
section_title: "High-dimensional random matrices"
section_number: null
pages: 23-26
source_pdf: Download.pdf
source_sha256: ca9639465b08d34c
toc_source: outline
doc_brief: "Concentration of empirical distribution functions with applications to non-i.i.d. models — 12 sections: Front matter; Introduction; Empirical Poincaré inequalities"
---
We shall now apply the bounds obtained in Theorems 1.1 and 7.1, to the case of the spectral
empirical distributions. Let {ξjk}1≤j≤k≤n be a family of independent random variables on some
probability space with mean Eξjk = 0 and variance Var(ξjk) = 1. Put ξjk = ξkj for 1 ≤k < j ≤n
and introduce a symmetric n × n random matrix,
 = 1
√n
⎛
⎜⎜⎝
ξ11
ξ12
···
ξ1n
ξ21
ξ22
···
ξ2n
...
...
...
...
ξn1
ξn2
···
ξnn
⎞
⎟⎟⎠.
Arrange its (real random) eigenvalues in increasing order: X1 ≤··· ≤Xn. As before, we asso-
ciate with particular values X1 = x1,...,Xn = xn an empirical (spectral) measure Fn with mean
(expected) measure F = EFn.
An important point in this scheme is that the joint distribution μ of the spectral values, as a
probability measure on Rn, represents the image of the joint distribution of ξjk’s under a Lip-
schitz map T with Lipschitz seminorm ∥T ∥Lip =
√
2
√n. More precisely, by the Hoffman–Wielandt
theorem with respect to the Hilbert–Schmidt norm, we have
n

i=1
|Xi −X′
i|2 ≤∥ −′∥2
HS = 1
n
n

j,k=1
|ξjk −ξ′
jk|2 ≤2
n

1≤j≤k≤n
|ξjk −ξ′
jk|2
for any collections {ξjk}j≤k and {ξjk}′
j≤k with eigenvalues (X1,...,Xn), (X′
1,...,X′
n), respec-
tively. This is a well-known fact ([2], page 165) which may be used in concentration problems;
see, for example, [15,30].
In particular (see Proposition A1 in the Appendix), if the distributions of ξjk’s satisfy a one-
dimensional Poincaré-type inequality with common constant σ 2, then μ satisﬁes a Poincaré-type
inequality with an asymptotically much better constant σ 2
n = 2σ 2
n . According to Theorem 1.1,
E
 +∞
−∞
|Fn(x) −F(x)|dx ≤Cσn
An + logn
n
1/3
,
where C is an absolute constant and An = 1
σn maxi,j |EXi −EXj|. Since maxi |EXi| is of order
at most σ, An is at most √n and we arrive at the bound (1.7) in Theorem 1.3:
E
 +∞
−∞
|Fn(x) −F(x)|dx ≤Cσ
n2/3 .
Now, let us explain the second statement of Theorem 1.3 for the case where the ξjk’s satisfy
a logarithmic Sobolev inequality with a common constant σ 2, in addition to the normalizing
conditions Eξjk = 0, Var(ξjk) = 1 (which implies that σ ≥1). Let G denote the standard semi-
circle law with variance 1, that is, with density g(x) = 1
2π
√
4 −x2, −2 < x < 2. In this case, the
Lipschitz seminorm is M = ∥G∥Lip = 1
π. Also,
βn = (Mσn)2/3
n1/3
= C′
σ
n
2/3
for some absolute C′. Therefore, applying Theorem 7.1 and using σ ≥1, we arrive at the
bound (1.8):
E sup
x∈Rn |Fn(x) −G(x)| ≤Cσ 2/3 log1/3 n
n2/3
+ sup
x∈R
|F(x) −G(x)|.
(8.1)
Thus, Theorem 1.3 is proved. For individual points that are close to the end-points x = ±2
of the supporting interval of the semicircle law, we may get improved bounds in comparison
with (8.1). Namely, by Proposition 6.1 (and repeating the argument from the proof of the in-
equality of Corollary 6.2), for all t > 0,
Eet|Fn(x)−G(x)| ≤Eet(Fn(x)−G(x)) + Ee−t(Fn(x)−G(x))
≤et(F(x+h)−G(x)) + et(G(x)−F(x−h))
≤2et(G(x+h)−G(x−h))+t∥F−G∥,
where h =

2σ 2n t
n
= 2σ√t
n
. Taking the logarithm and applying Jensen’s inequality, we arrive at
E|Fn(x) −G(x)| ≤∥F −G∥+

G(x + h) −G(x −h)

+ log2
t
.
(8.2)
Using the Lipschitz property of G only (that is, G(x + h) −G(x −h) ≤h
π) would yield the
previous bound, such as the one in the estimate (6.7) of Proposition 6.4,
E|Fn(x) −G(x)| ≤∥F −G∥+ C
σ
n
2/3
.
(8.3)
However, the real size of increments G(x + h) −G(x −h) with respect to the parameter h
essentially depends on the point x. To be more careful in the analysis of the right-hand side
of (8.2), we may use the following elementary calculus bound, whose proof we omit.
Lemma 8.1. G(x + h) −G(x −h) ≤2g(x)h + 4
3πh3/2 for all x ∈R and h > 0.
Since G is concentrated on the interval [−2,2], for |x| ≥2, we have a simple bound G(x +
h) −G(x −h) ≤4
3πh3/2. As a result, one may derive from (8.2) an improved variant of (8.3). In
particular, if |x| ≥2, then
E|Fn(x) −G(x)| ≤∥F −G∥+ C
σ
n
6/7
.
The more general statement for all x ∈R is given by the following result.
Theorem 8.2. Let ξjk (1 ≤j ≤k ≤n) be independent and satisfy a logarithmic Sobolev in-
equality with constant σ 2, with Eξjk = 0 and Var(ξjk) = 1. For all x ∈R,
E|Fn(x) −G(x)| ≤∥F −G∥+ C
σ
n
6/7
+ g(x)2/3
σ
n
2/3
,
(8.4)
where C is an absolute constant.
A similar uniform bound may also be shown to hold for Esupy≤x |Fn(y) −G(y)| (x ≤0) and
Esupy≥x |Fn(y) −G(y)| (x ≥0). Note that in comparison with (8.3), there is an improvement
for the points x at distance not more than ( σ
n )4/7 from ±2.
Proof of Theorem 8.2. According to the bound (8.2) and Lemma 8.1, for any h > 0, we may
write E|Fn(x) −G(x)| ≤∥F −G∥+ 3ϕ(h), where ϕ(h) = g(x)h + h3/2 + ε
h2 , ε = ( σ
n )2.
We shall now estimate the minimum of this function. Write h = (
ε
1+α )2/7 with parameter
α > 0 to be speciﬁed later on. If g(x) ≤α
√
h, then
ϕ(h) ≤(1 + α)h3/2 + ε
h2 = 2(1 + α)4/7ε3/7.
(8.5)
Note that the requirement on g(x) is equivalent to g(x)7
ε
≤
α7
1+α . Thus, we set A = g(x)7
ε
and
take α = 1 + 2A1/6. Since α ≥1, we get
α7
1+α ≥α6
2 ≥A. Hence, we may apply (8.5). Using
(1 + α)4/7 ≤(2α)4/7 and α4/7 ≤1 + ((2A)1/6)4/7 = 1 + (2A)2/21, we ﬁnally get that
ϕ(h) ≤2 · 24/7
1 + (2A)2/21

ε3/7 ≤4(ε3/7 + A2/21ε3/7).
This is the desired expression in square brackets in (8.4) and Theorem 8.2 follows.
□
Finally, let us comment on the meaning of the general Corollary 6.5 in the matrix model above.
To every interval I on the real line, we associate the number
NI = card{i ≤n:Xi ∈I}
of eigenvalues Xi inside it. Again, Corollary 6.5 may be applied to the standard semicircle law G
with density g(x), in which case β = C( σ
n )2/3. This gives that, under LSI(σ 2), imposed on the
entries ξjk, for any δ > 0 and any interval I of length |I| ≥4∥F −G∥/δ, we have that

NI
n −

I
g(x)dx
 ≤δ|I|
(8.6)
with probability at least 1 −4exp{−cn2δ3
σ 2 |I|3}. As we have already mentioned, under PI(σ 2),
one can show that ∥F −G∥≤Cn−2/3 ([8], Theorem 1.1). Therefore, (8.6) holds true with high
probability, provided that
|I| ≥Cn−2/3/δ
(8.7)
with large C (of order, say, logε n).
Such properties have been intensively studied in recent years in connection with the universal-
ity problem. In particular, it is shown in [18] and [41] that the restriction (8.7) may be weakened
to |I| ≥Cε(logα n)/n under the assumption that the intervals I are contained in [−2 −ε,2 + ε],
ε > 0, that is, ‘in the bulk’.
