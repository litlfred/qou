---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-009-5-bessel-functions
section_title: "Bessel functions"
section_number: 5
pages: 9-10
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
Bessel functions were used in [CE03] to obtain a new proof of the second best asymptotic
upper bound on the density of sphere packings inR n due to Levenshtein [Lev79]. We will
also use these functions to obtain our asymptotic bounds. We list some of their properties
here for later reference.
One of the many equivalent definitions [Wat95, p.40] of theBessel function of the first
kind of orderαis
Jα(z) :=
z
2
α ∞X
n=0
(−1)n
n! Γ(n+α+ 1)
z
2
2n
whenαis not a negative integer, where Γ is the classical gamma function. For non-integer
ordersJ α is a multi-valued function, but by abuse of notation the quotient
Jα(z)
zα = 1
2α
∞X
n=0
(−1)n
n! Γ(n+α+ 1)
z
2
2n
defines an even entire function that takes the value 2 −α/Γ(α+ 1) at the origin. Following
[GIT20], this leads us to define thenormalized Bessel function
ηα(z) := Γ(α+ 1)
∞X
n=0
(−1)n
n! Γ(n+α+ 1)
z
2
2n
= 2αΓ(α+ 1)Jα(z)
zα
satisfyingη α(0) = 1. Forα >−1/2, Poisson’s integral formula for Bessel functions
[OLBC10, p.224, eq. (10.9.4)] can be written as
ηα(x) = 2
B( 1
2,α+ 1
2)
Z 1
0
(1−t 2)α−1/2 cos(xt)dt
where
B(a,b) =
Z 1
0
ta−1(1−t) b−1 = Γ(a)Γ(b)
Γ(a+b)
is the Beta function (note that there is a factor of 2 missing in [GIT20, eq. (2.8)]). This
means thatη α is the Fourier transform of
χα(t) =
√
2π
B( 1
2,α+ 1
2) rect(t/2)(1−t 2)α−1/2
where rect is the characteristic function of the interval

− 1
2, 1
2

. By Fourier inversion, we
have
bηα(t) =χ α(t)
10 MAXIME FORTIER BOURQUE AND BRAM PETRI
wheneverα >1/2, which is whenη α is integrable. In particular,η α is positive-definite
forα >1/2 and its Fourier transform is supported in [−1,1]. By the easy direction of
the Paley–Wiener theorem, this implies thatη α has exponential type 1. In fact, along the
imaginary axis we have the following exact asymptotic for everyα≥−1/2 [Wat95, p.203]:
(5.1)J α(ix)∼ ex
√
2πx asx→∞inR.
The above integrability condition onψ α follows from the asymptotic formula
(5.2)J α(z) =
r
2
πz

cos

z− απ
2 − π
4

+O(e|Imz|/|z|)

as|z|→∞with|argz|< π[AS64, p.364]. Also note thatJ α(x) vanishes to orderαat
the origin, so that forα≥−1/2 the functionx7→ √xJα(x) is bounded near the origin and
hence on (0,∞) by continuity and the above asymptotic.
We will frequently make use of the even entire functions
φα(z) = Jα(z/2)2
z2α =
 ηα(z/2)
4αΓ(α+ 1)
2
and
ψα(z) = Jα(z)2
z2α(1−(z/j α)2)
wherej α is the first positive root ofJ α. These are such thatφ α(x)≥0 for everyx∈R
andψ α(x)≤0 for|x|≥j α. Up to positive constants,φ α(2x) is equal to \χα∗χα(x) so its
Fourier transform is a positive constant multiple ofχ α∗χα≥0 as long asφ α andχ α are
integrable, which holds wheneverα >0. In other words,φ α is positive-definite ifα >0,
with Fourier transform supported in [−1,1]. It was also shown in [GIT20, Remark 1.1]
thatψ α is positive-definite ifα≥−1/2. Observe thatcφ α is admissible ifα>1/2 and cψα
is admissible ifα>−1/2 by the asymptotic formula (5.2).
