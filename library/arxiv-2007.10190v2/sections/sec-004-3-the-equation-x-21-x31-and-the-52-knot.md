---
doc_id: arxiv-2007.10190v2
doc_title: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS"
section_id: sec-004-3-the-equation-x-21-x31-and-the-52-knot
section_title: "The equation x-2(1-x)3=1 and the 52 knot"
section_number: 3
pages: 5-7
source_pdf: 2007.10190v2.pdf
source_sha256: 37bcbd3a343bb21a
toc_source: outline
doc_brief: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS — The asymptotic expansion of quantum knot invariants in complex Chern-Simons theory gives rise to factorially divergent formal power series."
---
The state integral of the 52 knot is given by Equation (39) below with (A, B) = (2, 3) and
µ = λ = 0. The critical points of the integrand are solutions of the algebraic equation
x−2(1 −x)3 = 1 .
(19)
6
STAVROS GAROUFALIDIS, JIE GU, AND MARCOS MARI˜NO
The above equation (which deﬁnes a cubic ﬁeld of discriminant −23, the trace ﬁeld of the
52 knot) has three solutions ξ1 = 0.78492 + 1.30714 . . . i, ξ2 = 0.78492 −1.30714 . . . i and
ξ3 = 0.43016 . . . , corresponding to the geometric representation, its conjugate and the real
representation. The corresponding series Φσj(τ) satisfy Φσ2(τ) = −iΦσ1(−τ) and the ﬁrst
few terms of φσj(τ/(2πi)) are given by
ϕσj
 τ
2πi

=
−3ξ2
j + 3ξj −2
23
1/4 
1 + 33ξ2
j + 242ξj −245
22 · 232
τ + 100250ξ2
j −12643ξj + 2732
25 · 233
τ 2
+ −50198891ξ2
j + 35443870ξj −79016748
27 · 3 · 5 · 235
τ 3
+−3809943572ξ2
j + 1861268771ξj + 1015686665
211 · 3 · 5 · 236
τ 4 + . . .

.
(20)
The exponent in (3) involves
V (σ1) = 2.821 . . . + 1.379 . . . i, V (σ2) = −2.821 . . . + 1.379 . . . i, V (σ3) = −2.758 . . .
(21)
where ℜV (σ1) is the hyperbolic volume of the 52 knot complement, and ℑV (σ1) = ℑV (σ2)
the Chern-Simons action. The three series Φσj(τ) for j = 1, 2, 3 form a vector
Φ(τ) =


Φσ1(τ)
Φσ2(τ)
Φσ3(τ)

.
(22)
Consider the linear q-diﬀerence equation
ym(q) −3ym+1(q) + (3 −q2+m)ym+2(q) −ym+3(q) = 0.
(23)
The above equation has a fundamental solution set given by the columns of the following
matrix
Wm(q) =









W +
m(q),
|q| < 1,



0
0
1
0
1
0
1
0
0


W −
−m−2(q−1)



1
0
0
0
−1
0
0
0
1


,
|q| > 1.
(24)
where the matrices W ε
m(q) with ε = ± are respectively
W ε
m(q) =


Hε
0,m(q)
Hε
1,m(q)
Hε
2,m(q)
Hε
0,m+1(q)
Hε
1,m+1(q)
Hε
2,m+1(q)
Hε
0,m+2(q)
Hε
1,m+2(q)
Hε
2,m+2(q)


(25)
and Hε
j,m(q) are given in Appendix A for j = 0, 1, 2 and m ∈Z.
The fundamental solutions satisfy
det(Wm(q)) = 2,
(26)
for all integers m as well as
1
2Wm(q)


0
0
1
0
2
0
1
0
0

Wℓ(q−1)T ∈SL(3, Z[q, 1/q])
(27)
THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS
7
for all integers m, ℓ. In particular, we have:
1
2Wm−1(q)


0
0
1
0
2
0
1
0
0

W−m−1(q−1)T =


1
0
0
0
0
1
0
1
3 −qm

.
(28)
The S matrix is given by
S+(q) = 1
2


0
1
0
0
1
1
−1
0
0

W−1(q−1)


0
0
1
0
−2
0
1
0
0

W−1(q)T


0
0
−1
1
1
0
0
1
0

,
(29a)
S−(q) = 1
2


0
3
−1
0
−1
0
1
0
0

W−1(q)


0
0
1
0
−2
0
1
0
0

W−1(q−1)T


0
0
1
3
−1
0
−1
0
0

.
(29b)
The above matrix S satisﬁes Equation (4). A proof is given in Appendix A.2.
