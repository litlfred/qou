---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-033-b1-recovering-a-recent-result-of-vassilieva
section_title: "B.1. Recovering a recent result of Vassilieva"
section_number: null
pages: 63-65
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
on the degree in α of cµ,ν;π, can be used to give a short proof of a recent result of
Vassilieva. In the paper [Vas13], she considered the follow ing quantity: for µ a
partition of n, let r = |µ| − ℓ(µ) and
(57) ar
µ (α ) :=
∑
λ⊢n
1
j(α)
λ
θµ(λ)
(
θ(2,1n−2)(λ)
) r .
Using structure constants, we can write: for any partition λ of n,
(
θ(2,1r−2)(λ)
) r =
∑
µ1,µ2,...,µr ⊢n
µ1=(2,1r−2)
(r−1∏
i=1
cµi,(2,1r−2);µi+1
)
θµr (λ).
Plugging this into Equation (57) and using the orthogonalit y relation presented in
Lemma 7.3 (1): ∑
λ⊢n
1
j(α)
λ
θµ(λ)θν (λ) = δµ,ν
zµαℓ(µ)
(see [Vas13, Section 3.3]), we get
(58) ar
µ (α ) = 1
zµαℓ(µ)
∑
µ1,µ2,...,µr ⊢n
µ1=(2,1r−2), µ r =µ
r−1∏
i=1
cµi,(2,1r−2);µi+1.
From Corollary 4.2, the coefﬁcient cµi,(2,1r−2);µi+1 vanishes unless
(59) |µi+1| − ℓ(µi+1) ≤ |µi| − ℓ(µi) + 1.
As |µ1| −ℓ(µ1) = 1 and |µr| −ℓ(µr) = |µ| −ℓ(µ) = r, for any non-zero summand
in (58), one has equality in (59) for all integers i. But, again from Corollary 4.2,
equality in (59) implies that the coefﬁcient cµi,(2,1r−2);µi+1 is independent of α.
Hence, the quantity αℓ(µ)zµar
µ (α ) is independent on α.
64 M. DOŁ ˛ EGA AND V . FÉRAY
In the caseα = 1, it can be interpreted as some number ofminimal factorizations
in the symmetric group (see [Vas13, Lemma 1] or [GJ96a, Proposition 3.1]), which
has been computed by Dénes in [Dén59]:
zµar
µ (1) =
( r
µ1 − 1, · · · , µℓ(µ)−1
) ℓ(µ)−1∏
i=1
µµi−2
i .
Dénes in fact considered only the case µ = (n), that is minimal factorizations of a
cycle, but it can be easily proved that minimal factorizations of a product of disjoint
cycles are obtained by shufﬂing factors of minimal factorizations of its cycles.
From the case α = 1 and the independence on α, we conclude immediately that
ar
µ (α ) = 1
αℓ(µ)zµ
( r
µ1 − 1, · · · , µℓ(µ)−1
) ℓ(µ)−1∏
i=1
µµi−2
i ,
which is the main result in [Vas13].
B.2. Goulden’s and Jackson’sb-conjecture. In this Section, we explain that our
quantities cµ,ν;π (for a general value of the parameter α) are the same as quantities
cπ
µ,ν (b) considered by Goulden and Jackson in [GJ96a]. As a consequen ce, we
give a partial answer to a question raised by these authors. W e use the convention
that the boldface quantities refer to the notations of Goulden and Jackson [GJ96a].
To establish this connection we will need to use the α-scalar product on the
symmetric functions, for which Jack polynomials and power-sum symmetric func-
tions are orthogonal basis [Mac95, (VI,10)]. The following formula is a natural
extension of Frobenius counting formula, see e.g. [LZ04, Appendix, Theorem 2].
Proposition B.1. Let µ, ν and π be three partitions of the same integer n. Then
cµ,ν;π = zπαℓ(π)∑
λ⊢n
θπ(λ) θµ(λ) θν(λ)
⟨Jλ, Jλ⟩ .
Proof. Let partitions µ ⊢ n and ν ⊢ n be ﬁxed. We consider the following sym-
metric function:
F :=
∑
λ⊢n
θµ(λ) θν(λ)
⟨Jλ, Jλ⟩ Jλ.
By deﬁnition of cµ,ν;π, one has:
(60) F =
∑
λ⊢n
∑
π⊢n
cµ,ν;π
( θπ(λ)
⟨Jλ, Jλ⟩Jλ
)
.
But θπ(λ) is deﬁned by
Jλ =
∑
π⊢n
θπ(λ) pπ.
As pπ is an orthogonal basis, this implies
θπ(λ) = ⟨Jλ, pπ⟩
⟨pπ, pπ⟩.
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 65
But Jλ is also an orthogonal basis, hence:
(61) pπ =
∑
λ
⟨Jλ, pπ⟩
⟨Jλ, Jλ⟩Jλ = ⟨pπ, pπ⟩
∑
λ
θπ(λ)
⟨Jλ, Jλ⟩Jλ.
Plugging this into (60), one has:
F =
∑
π⊢n
cµ,ν;π
pπ
⟨pπ, pπ⟩
and thus,
cµ,ν;π = ⟨F, pπ⟩ =
∑
λ⊢n
θµ(λ) θν(λ)
⟨Jλ, Jλ⟩ ⟨Jλ, pπ⟩
=
∑
λ⊢n
θµ(λ) θν(λ)
⟨Jλ, Jλ⟩ ⟨pπ, pπ⟩θπ(λ).
As ⟨pπ, pπ⟩ = zπ · αℓ(π), we obtain the claimed formula. □
Comparing the proposition with the deﬁnition of the connect ion series cπ
µ,ν (b)
[GJ96a, equations (1) and (5)], we get that
(62) cµ,ν;π = cπ
µ,ν (b).
Goulden and Jackson had conjectured that they were polynomials with non-negative
integer coefﬁcients in b = α − 1 (which have conjecturally a combinatorial mean-
ing in terms of matchings ; see [GJ96a, Section 4]). Corollar y 4.2 implies the
following weaker statement, which was not known yet.
Proposition B.2. The connection series cπ
µ,ν (b) introduced in [GJ96a] is a poly-
nomial in b with rational coefﬁcients of degree at most d(µ, ν; π).
