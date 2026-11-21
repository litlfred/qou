---
doc_id: arxiv-math-0108011v1
doc_title: "The Homfly polynomial of the decorated Hopf link"
section_id: sec-007-21-formal-schur-functions
section_title: "Formal Schur functions"
section_number: 2.1
pages: 8-8
source_pdf: 0108011v1.pdf
source_sha256: e4af4b5d3c5ff6cd
toc_source: inferred
doc_brief: "The Homfly polynomial of the decorated Hopf link — The main goal is to ﬁnd the Homﬂy polynomial of a link formed by decorating each component of the Hopf link with the closure of a directly oriented"
---
Formal Schur functions
We follow Macdonald in deﬁning the Schur functions of a formal power se-
ries E(t) = 1 + P∞
i=1 eiti with coeﬃcients ei in a commutative ring. When
E(t) is a polynomial with a formal factorisation as E(t) = QN
j=1(1 + xjt)
then any partition λ of n determines the classical Schur symmetric function
sλ(x1, . . . , xN) in terms of determinants whose entries are powers of {xj},
given explicitly by equation (14). This can be written as a polynomial in the
elementary symmetric functions {ei} of x1, . . . , xN, which are the coeﬃcients
of E(t), by means of the Jacobi-Trudy formula. So long as N ≥n this poly-
nomial in {ei} is independent of N. Macdonald deﬁnes the Schur function
sλ(E(t)) for a formal power series to be this polynomial in the coeﬃcients
{ei}, described explicitly in section 4.2.
The coeﬃcient ei itself is the Schur function sλ(E(t)) for the partition
λ = 1i = (1, . . . , 1), represented by the Young diagram consisting of a sin-
gle column with i cells. Equally, when λ is a single row with j cells then
sλ(E(t)) = hj, where hj is the complete symmetric function of degree j in
x1, . . . , xN in the case of the polynomial E(t) above. In any case, the power
series H(t) = 1 +
P hjtj satisﬁes the power series equation E(−t)H(t) = 1.
Since sλ(E(t)) is a polynomial in {ei} depending only on λ it is clear that
if R and S are any commutative rings and we apply a ring homomorphism
ρ : R →S to the coeﬃcients {ei} ∈R to get the power series ρ(E(t)) with
coeﬃcients {ρ(ei)} ∈S then
sλ(ρ(E(t))) = ρ(sλ(E(t))),
for every λ.
We make use later of the homogeneity of the Schur function sλ in the
form
sλ(E(αt)) = α|λ|sλ(E(t)),
(2)
where λ has |λ| cells.
