---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-021-57-numerical-verification
section_title: "Numerical verification"
section_number: 5.7
pages: 43-45
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
toc_source: outline
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
jecture 19. This involves, on the one hand, a numerical computation of the asymptotics of
the holomorphic blocks and on the other hand, a numerical computation of the Borel re-
summation by the Laplace integral of a Padé approximation. Taking the two computations
into account, we found out numerically, integers appearing at two exponentially small scales,
namely ˜q and ˜x, and guessing these integers eventually led to Conjecture 19.
We found ample numerical evidence for the resurgent data (186a)–(186d). First of all,
due to the symmetry Φ1(x; −τ) = −iΦ2(x; τ), Φ2(x; −τ) = iΦ1(x; τ), the resurgent behavior
of s(Φ)(x; τ) for τ in the lower half-plane can be deduced from that for τ in the upper
half-plane. We only have to numerically test the resurgent data for τ in regions I, II in the
upper-half plane.
The ﬁrst piece of evidence comes from analysing the radial asymptotics of the left hand
side of (15). Note that the matrix ∆(τ) = diag(∆σ(τ)) is always diagonal, and each row of
(15) is
∆σ(τ)Bσ(x; q) =
X
σ′
MR(˜x, ˜q)σ,σ′sR(Φσ′)(x; τ).
(226)
If we take τ = eiα/k with the argument α depending on a ray in the region R and k a
very large integer, the diﬀerence between exp

V (σ′)
2πiτ

associated to diﬀerent critical points is
greatly magniﬁed, and the right hand side of (226) is dominated by a single series. Further-
more, when τ is in the upper (lower) half plane, ˜q (1/˜q) is exponentially suppressed and the
44
STAVROS GAROUFALIDIS, JIE GU, AND MARCOS MARIÑO
|sI(Φ)(x;τ)
PI(x;τ) −1|
|sI(Φ)(x;τ)
s′
I(Φ)(x;τ) −1|
|˜q(τ)|
|˜x(x, τ)|
σ1
3.2 × 10−66
9.7 × 10−66
8.3 × 10−33
0.05
σ2
1.9 × 10−94
5.2 × 10−94
(a) Region I: τ =
1
20e
πi
5
|sII(Φ)(x;τ)
PII(x;τ) −1|
|sII(Φ)(x;τ)
s′
II(Φ)(x;τ) −1|
|˜q(τ)|
|˜x(x, τ)−1|
σ1
1.9 × 10−94
5.2 × 10−94
8.3 × 10−33
0.05
σ2
3.2 × 10−66
9.7 × 10−66
(b) Region II: τ =
1
20e
4πi
5
|sIV (Φ)(x;τ)
PIV (x;τ) −1|
|sIV (Φ)(x;τ)
s′
IV (Φ)(x;τ) −1|
|˜q(τ)−1|
|˜x(x, τ)|
σ1
1.9 × 10−94
5.2 × 10−94
8.3 × 10−33
0.05
σ2
3.2 × 10−66
9.7 × 10−66
(c) Region III: τ =
1
20e−4πi
5
|sIII(Φ)(x;τ)
PIII(x;τ) −1|
|sIII(Φ)(x;τ)
s′
III(Φ)(x;τ) −1|
|˜q(τ)−1|
|˜x(x, τ)−1|
σ1
3.2 × 10−66
9.7 × 10−66
8.3 × 10−33
0.05
σ2
1.9 × 10−94
5.2 × 10−94
(d) Region IV : τ =
1
20e−πi
5
Table 1. Numerical tests of holomorphic lifts of Borel sums of asymptotic
series for knot 41. We perform the Borel-Padé resummation on Φ(x; τ) with
280 terms at x = 6/5 and τ in four diﬀerent regions, and compute the relative
diﬀerence between them and the right hand side of (201a)–(201d), which we
denote by PR(x; τ). They are within the error margins of Borel-Padé resum-
mation, which are estimated by redo the resummation with 276 terms, denoted
by s′
R(•) in the tables. The relative errors are much smaller than |˜q±1|, |˜x±1|,
possible sources of additional corrections.
correction MR(˜x, ˜q)σ,σ′ as a series in ˜q (1/˜q) is dominated by the leading term. (226) thus
becomes
∆σ(τ)Bσ(x; q) ∼exp
 
V (ˆσ) + ωˆσ
2πieiα
k −log(iδ(x, yˆσ)) +
∞
X
n=1
Sn(x, yˆσ)eniαk−n
!
,
k ≫1,
(227)
where ωˆσ is possible contribution from the leading term of MR(˜x, ˜q)σ,ˆs, and the series in k−1
is log ϕ(x, yˆσ; τ). As pointed out in [GZa], this equation can be tested numerically with the
help of Richardson transformations (see for instance [BO99]).
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY
45
Next, we can test (226) directly. One way of doing this is to compute Borel-Padé re-
summation sR(Φσ′)(x; τ) for various values of x ∈R and τ in the same region R, and by
comparing with the left hand side extract terms of MR(˜x, ˜q)σ,σ′ order by order. To facilitate
this operation, instead of MR(˜x; ˜q) we consider
f
MR(˜x; ˜q) =

θ(−˜q−1/2˜x; ˜q)2
0
0
θ(−˜q1/2˜x; ˜q)−1

MR(˜x; ˜q)
(228)
whose entries are ˜q-series with coeﬃcients in Z[˜x±1] instead of in Z(˜x). Using 280 terms of
Φσ(x; τ), we ﬁnd the results for τ in the upper half plane
f
MI(x; q) =

−x + (x2 + x3)q + (x2 + x3)q2
1 −(x + x2 + x3)q −(x + x2)q2
−1 + (x−1 + x)q + (x−1 + x)q2
1 −(x−1 + 1 + x)q −(x−1 + x)q2

+ O(q3)
(229a)
f
MII(x; q) =

−x + (1 + x−1 + x−2)q + (1 + x−1)q2
1 −(x−1 + x−2)q −(x−1 + x−2)q2
−1 + (x + 1 + x−1)q + (x + x−1)q2
1 −(x + x−1)q −(x + x−1)q2

+ O(q3)
(229b)
and they agree with (186a), (186b). Another more decisive way is to compute both sides of
(226) numerically assuming (186a), (186b) and compare them. Alternatively, we can compare
two sides of the equations of holomoprhic lift (201a), (201b). We ﬁnd that the diﬀerence
between the two sides is always within the error margin of Borel-Paé resummation, and much
smaller than ˜q±1, ˜x±1, i.e. possible additional corrections. We illustrate this comparison by
one example with x = 6/5 and τ =
1
20e± πi
5 , 1
20e± 4πi
5 in four regions in Table 1.
A ﬁnal way to test these results is to see that in the x 7→1 limit, the resurgent data as well
as the Stokes matrices (187a)–(187b) are compatible with the results in section 3.1 where
x = 1. This is a non-trivial test since the matrix W−1(x−1; q−1) (|q| < 1) in (187a)–(187b) is
divergent in the limit x 7→1.
