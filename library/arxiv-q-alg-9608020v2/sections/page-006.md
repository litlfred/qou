---
doc_id: arxiv-q-alg-9608020v2
doc_title: "Shifted Jack polynomials, binomial formula, and applications"
section_id: page-006
section_title: "Page 6"
section_number: null
pages: 6-6
source_pdf: 9608020v2.pdf
source_sha256: 727268098db7f23d
toc_source: undetermined
doc_brief: "Shifted Jack polynomials, binomial formula, and applications — In this note we prove an explicit binomial formula for Jack polynomials and discuss some applications of it. 1."
---
6
A. OKOUNKOV AND G. OLSHANSKI
where the second equality is based on the binomial formula and the last equality
follows from (2.3)
□.
We call F(l, x; θ) the Bessel functions. They are in the same relation to Jack
polynomials as ordinary Bessel functions to Jacobi polynomials. They are eigen-
functions of the corresponding degeneration of Sekiguchi operators. The formula
(4.2) makes obvious the following known symmetry
F(l, x; θ) = F(x, l; θ) .
Let H(n, R) denote the space of real symmetric matrices of order n, let X, Y ∈
H(n, R), and let x = (x1, . . ., xn) and y = (y1, . . . , yn) be the spectra of X and Y .
The compact orthogonal group O(n) acts on the space H(n, R) by conjugations.
One can prove that
(4.3)
F(y, x; 1/2) =
Z
O(n)
exp(tr(Y uXu−1))du,
where du is the normalized Haar measure on O(n). (Idea of proof: the normalized
polynomials
Pλ(z1, . . ., zn; 1/2)/Pλ(1, . . ., 1; 1/2)
are the spherical functions on the compact symmetric space U(n)/O(n) while the
integrals (4.3) are essentially the spherical functions on the associated Euclidean
type symmetric space O(n)⋉H(n, R). It is well–known (see [DR]) that the spherical
functions of Euclidean type can be obtained from the spherical functions of compact
type by the limit transition (4.1).)
A similar interpretation of the functions F(y, x; θ) also exists for θ = 1 and
θ = 2.
Then one has to consider orbits in the spaces H(n, C) and H(n, H) of
complex and quaternionic Hermitian matrices, respectively. An application of the
expansion (4.2) for θ = 1 is given in [OV]; similar results also hold for θ = 1/2 and
θ = 2.
5. Formula for θ-dimension of a skew diagram λ/µ. Deﬁne the θ-dimension
θ-dim λ/µ of a skew diagram λ/µ as the following coeﬃcient
(5.1)
(
X
xi)kPµ(x; θ) =
X
|λ|=|µ|+k
θ-dim λ/µ Pλ(x; θ) ,
k = 1, 2, . . . .
If θ = 1 then θ-dim λ/µ equals the number of the standard tableaux on λ/µ; for
general θ each tableau T is counted with a certain weight ψ′
T (θ) given in [M], section
VI.6. In particular, if µ = ∅then (see (5.6) below for a proof using shifted Jack
polynomials)
θ-dim λ = |λ|!/H(λ) .
We have
Proposition.
(5.2)
θ-dim λ/µ
θ-dim λ
=
P ∗
µ(λ; θ)
|λ|(|λ| −1) · · ·(|λ| −|µ| + 1) .
This proposition can be deduced from (3.8) and [La,K] (see the remark above),
but it easier to give a direct proof, which uses the very same argument as in [OO],
section 9.
First one proves that
