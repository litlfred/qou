---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-039-4-ζ-dkζ-dk
section_title: "(ζ +dk,ζ +dk)"
section_number: 4
pages: 44-45
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
= 1
2 (dk,ζ ) + 1
2
∑
bik<0
bikλki.
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 45
One can calculate m′
k in a similar way. □
Deﬁnition 6.2.3. We say that a quantum monoidal seed S = ( {Mi}i∈J,L, ~B,D )
admits a mutation in direction k ∈Jex if there exists a simple object M ′
k ∈ Cµk(D)k such
that
(i) there exist exact sequences in C
0 →q ⨀
bik>0
M ⊙bik
i →qmkMk ⊗M ′
k → ⨀
bik<0
M ⊙(−bik)
i → 0,(6.4)
0 →q ⨀
bik<0
M ⊙(−bik)
i →qm′
kM ′
k ⊗Mk → ⨀
bik>0
M ⊙bik
i → 0,(6.5)
wheremk and m′
k are as in (
6.3).
(ii) µk(S ) :=
(
{Mi}i⁄=k ⊔ {M ′
k},µk(L),µk( ~B),µk(D)
)
is a quantum monoidal seed in
C.
We call µk(S ) the mutation of S in direction k.
By Lemma 6.2.2, the following lemma is obvious.
Lemma 6.2.4. Let S = ({Mi}i∈J,L, ~B,D ) be a quantum monoidal seed which admits
a mutation in direction k ∈Jex. Then we have
[µk(S )] = µk([S ]).
Deﬁnition 6.2.5. Assume that a k-linear abelian monoidal category C satisﬁes (6.1)
and (6.2). The category C is called a monoidal categoriﬁcation of a quantum cluster
algebra A over Z[q±1/2] if
(i) the Grothendieck ring Z[q±1/2] ⊗Z[q±1]K(C) is isomorphic to A,
(ii) there exists a quantum monoidal seed S = ( {Mi}i∈J,L, ~B,D ) in C such that
[S ] := ({q−(di,di)/4[Mi]}i∈J,L, ~B) is a quantum seed of A,
(iii) S admits successive mutations in all the directions.
Note that if C is a monoidal categoriﬁcation of a quantum cluster algebra A, then
any quantum seed in A obtained by a sequence of mutations from the initial quan-
tum seed is of the form ( {q−(di,di)/4[Mi]}i∈J,L, ~B) for some quantum monoidal seed
({Mi}i∈J,L, ~B,D ). In particular, all the quantum cluster monomials in A are the
classes of real simple objects in C up to a power of q1/2.
