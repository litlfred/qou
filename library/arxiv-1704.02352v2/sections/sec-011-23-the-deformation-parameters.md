---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-011-23-the-deformation-parameters
section_title: "The deformation parameters"
section_number: 2.3
pages: 17-18
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Y oung diagrams which can be regarded as a natural one-parameter deformation of so me classi- cal Y"
---
root of the variable α which is ubiquitous in the subject of Jack deforma-
tion, we introduce an indeterminate A := √α. The algebra of Laurent
polynomials in the indeterminate A will be denoted by Q
[
A, A−1]
.
A special role will be played by the quantity
(2.2) γ := −A + 1
A ∈ Q
[
A, A−1]
which already appeared in the numerator on the left-hand sid e of (1.9).
2.4. The linear space of α-polynomial functions. In a paper [ ´Sni18] the
second-named author has deﬁned a certain ﬁltered linear spa ce of α-polyno-
mial functions. This linear space consists of certain functions in the set Y of
Y oung diagrams with values in the ringQ
[
A, A−1]
of Laurent polynomials
and, among many equivalent deﬁnitions, one can deﬁne it usin g normalized
Jack characters.
Deﬁnition 2.2 ([ ´Sni18, Proposition 5.2]). The linear space of α-polynomial
functions is the linear span (with rational coefﬁcients) of the functions
(2.3) γk Chπ : Y → Q
[
A, A−1]
over the integers k ≥ 0 and over partitions π ∈ P .
The ﬁltration on this vector space is speciﬁed as follows: fo r an integer
n ≥ 0 the subspace of vectors of degree at most n is the linear span of the
elements (2.3) over integers k ≥ 0 and over partitions π ∈ P such that
k + |π| + ℓ(π) ≤ n.
2.5. Algebras P and P• of α-polynomial functions. The vector space
of α-polynomial functions can be equipped with a product in two d istinct
natural ways (which will be reviewed in the following). With each of these
two products it becomes a commutative, unital ﬁltered algeb ra.
Firstly, as a product we may take the pointwise product of functions on Y.
The resulting algebra will be denoted by P (the fact that the P is closed
under such product was proved by Doł˛ ega and Féray [DF16, Theorem 1.4]).
Secondly, as a product we may take the disjoint product •, see [ ´Sni18,
Section 2.3], which is deﬁned on the linear base of Jack chara cters by con-
catenation (see Section 1.9) of the corresponding partitions
(γp Chπ) • (γq Chσ) := γp+q Chπσ .
The resulting algebra will be denoted by P•.
18 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
2.6. Two probabilistic structures on α-polynomial functions. Assume
that χ : Pn → R is a reducible Jack character and let Pχ be the corre-
sponding probability measure (1.7) on the set Yn of Y oung diagrams withn
boxes. With this setup, functions on Yn can be viewed as random variables;
we denote by Eχ the corresponding expectation.
Let us ﬁx a partition π ∈ P n; we denote by χ(α)
# (π) the random variable
Yn ∋ λ ↦→χ(α)
λ (π) given by irreducible Jack character (1.5). From the way
the probability measure Pχ was deﬁned in (1.7) it follows immediately that
(2.4) Eχ
[
χ(α)
# (π)
]
= χ(π).
Any α-polynomial function F can be restricted to the set Yn of Y oung
diagrams with n boxes; thus it makes sense to speak about its expected
value EχF . In the case when F = Ch π is a Jack character, this expected
value can be explicitly calculated thanks to (2.4):
(2.5) Eχ Chπ =
{
n|π|
χ(π) if n < |π|,
0 otherwise.
By considering the multiplicative structure on α-polynomial functions
given by the pointwise product, we get in this way a condition al expectation
Eχ : P → R; the corresponding cumulants will be denoted by κχ
ℓ .
On the other hand, by considering the disjoint product, we ge t a con-
ditional expectation Eχ : P• → R; the corresponding cumulants will be
denoted by κχ
•ℓ.
