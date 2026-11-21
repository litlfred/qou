---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-025-standard-phase
section_title: "Standard phase"
section_number: null
pages: 136-139
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
As in the one-dimensional case, we begin with the simplest phase function
and a monomial amplitude. We ﬁrst state a formula for the one-dimensional
integral with amplitude A(x) = x2n and standard phase in terms of the explicit
5.2 Standard phase
119
constants
β2n = √π (2n)!
n! 4n .
Proposition 5.6. For all n ∈N,
Z ∞
−∞
x2ne−x2 dx = β2n.
Proof
For n = 0 this is just the standard Gaussian integral
Z ∞
−∞
e−x2dx = √π ,
and the general result follows by induction. Indeed, rewriting
Z ∞
−∞
x2ne−x2 dx =
Z ∞
−∞
−x2n−1
2

−2x e−x2 dx

and applying integration by parts gives
Z ∞
−∞
x2ne−x2 dx = 2n −1
2
Z ∞
−∞
x2n−2 e−x2 dx
= 2n −1
2
· √π ·
(2n −2)!
(n −1)! 4n−1
= √π (2n)!
n! 4n
by induction, as claimed.
□
Corollary 5.7 (monomial integral). Let S (z) = Pd
j=1 z2
j and r ∈Nd. Then
Z
Rd zre−λS (z) dz = βrλ−(d+|r|)/2
for any λ > 0, where βr = Qd
j=1 βrj if all the components r j are even and
βr = 0 otherwise.
Proof
If n ∈N then making the change of variables x = yλ−1/2 and applying
Proposition 5.6 proves
Z ∞
−∞
x2n e−λx2 dx = λ−1/2−n
Z ∞
−∞
y2ne−y2dy = λ−1/2−nβ2n ,
while
R ∞
−∞x2n+1 e−λx2 = 0 as its integrand is odd. The integral under considera-
tion factors as
Z
Rd zre−λS (z) dz =
d
Y
j=1
"Z ∞
−∞
z
rj
j e−λz2
j dz j
#
,
120
Multivariate Fourier–Laplace integrals
and the result follows from simplifying each factor.
□
Before establishing Theorem 5.1 we also need to bound the error terms that
appear.
Lemma 5.8 (Big-O Lemma). Let A be a measurable function satisfying A(z) =
O(|z|r) at the origin. Then the integral of A(z)e−λS (z) over any compact set K
may be bounded from above by
Z
K
A(z)e−λS (z) dz = O

λ−(d+r)/2
.
The implied constant on the right goes to zero as the implied constant in the
hypothesis A(z) = O(|z|r) goes to zero.
Proof
Because K is compact and A(z) = O(|z|r) at the origin, there exists a
constant C > 0 such that |A(z)| ≤C|z|r on all of K. Let
K0 =
n
z ∈K : |z| ≤λ−1/2o
denote the intersection of K with the ball of radius λ−1/2, and for n ≥1 let
Kn =
n
z ∈K : 2n−1λ−1/2 ≤|z| ≤2nλ−1/2o
denote the intersection of K with a shell. On K0 we have |A(z)| ≤Cλ−r/2 and
|e−λS (z)| ≤1, so
Z
K0
A(z)e−λS (z) dz ≤Vol(K0)Cλ−r/2 = (π/λ)d/2
Γ
 d
2 + 1
 C λ−r/2.
For n ≥1, when z ∈Kn we have the upper bounds
|A(z)| ≤2rnCλ−r/2
by upper bound on |z|
e−λS (z) ≤e−22n−2
by lower bound on |z|
Vol(Kn) ≤2dnπd/2
Γ
 d
2 + 1
 λ−d/2
by upper bound on |z|.
Thus, if C′ = 1 + P
n≥0 2(d+r)ne−22n−2 < ∞then

Z
K
A(z)e−λS (z) dz

 ≤
∞
X
n=0

Z
Kn
A(z)e−λS (z) dz

 ≤
πm/2
Γ
 d
2 + 1
 C C′ λ−(d+r)/2
with the right-hand side going to zero with the implied constant C, as claimed.
□
We are now ready to prove Theorem 5.1.
