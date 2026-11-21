---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-047-b2-gouldens-and-jacksons-b-conjecture
section_title: "B.2. Goulden's and Jackson's b-conjecture"
section_number: null
pages: 64-65
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
quantities cµ,ν;π (for a general value of the parameter α) are the same as quantities
cπ
µ,ν(b) considered by Goulden and Jackson in [GJ96a]. As a consequence, we
give a partial answer to a question raised by these authors. We use the convention
that the boldface quantities refer to the notations of Goulden and Jackson [GJ96a].
To establish this connection we will need to use the α-scalar product on the
symmetric functions, for which Jack polynomials and power-sum symmetric func-
tions are orthogonal basis [Mac95, (VI,10)]. The following formula is a natural
extension of Frobenius counting formula, see e.g. [LZ04, Appendix, Theorem 2].
Proposition B.1. Let µ, ν and π be three partitions of the same integer n. Then
cµ,ν;π = zπαℓ(π) X
λ⊢n
θπ(λ) θµ(λ) θν(λ)
⟨Jλ, Jλ⟩
.
Proof. Let partitions µ ⊢n and ν ⊢n be ﬁxed. We consider the following sym-
metric function:
F :=
X
λ⊢n
θµ(λ) θν(λ)
⟨Jλ, Jλ⟩
Jλ.
By deﬁnition of cµ,ν;π, one has:
(60)
F =
X
λ⊢n
X
π⊢n
cµ,ν;π
 θπ(λ)
⟨Jλ, Jλ⟩Jλ

.
But θπ(λ) is deﬁned by
Jλ =
X
π⊢n
θπ(λ) pπ.
As pπ is an orthogonal basis, this implies
θπ(λ) = ⟨Jλ, pπ⟩
⟨pπ, pπ⟩.
LARGE DIAGRAMS AND STRUCTURE CONSTANTS
65
But Jλ is also an orthogonal basis, hence:
(61)
pπ =
X
λ
⟨Jλ, pπ⟩
⟨Jλ, Jλ⟩Jλ = ⟨pπ, pπ⟩
X
λ
θπ(λ)
⟨Jλ, Jλ⟩Jλ.
Plugging this into (60), one has:
F =
X
π⊢n
cµ,ν;π
pπ
⟨pπ, pπ⟩
and thus,
cµ,ν;π = ⟨F, pπ⟩=
X
λ⊢n
θµ(λ) θν(λ)
⟨Jλ, Jλ⟩
⟨Jλ, pπ⟩
=
X
λ⊢n
θµ(λ) θν(λ)
⟨Jλ, Jλ⟩
⟨pπ, pπ⟩θπ(λ).
As ⟨pπ, pπ⟩= zπ · αℓ(π), we obtain the claimed formula.
□
Comparing the proposition with the deﬁnition of the connection series cπ
µ,ν(b)
[GJ96a, equations (1) and (5)], we get that
(62)
cµ,ν;π = cπ
µ,ν(b).
Goulden and Jackson had conjectured that they were polynomials with non-negative
integer coefﬁcients in b = α −1 (which have conjecturally a combinatorial mean-
ing in terms of matchings ; see [GJ96a, Section 4]). Corollary 4.2 implies the
following weaker statement, which was not known yet.
Proposition B.2. The connection series cπ
µ,ν(b) introduced in [GJ96a] is a poly-
nomial in b with rational coefﬁcients of degree at most d(µ, ν; π).
