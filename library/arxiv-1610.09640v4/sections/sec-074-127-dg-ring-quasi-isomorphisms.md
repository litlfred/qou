---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-074-127-dg-ring-quasi-isomorphisms
section_title: "DG Ring Quasi-Isomorphisms"
section_number: 12.7
pages: 238-240
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
homomorphism of DGK-rings u : A→B induces a homomorphism of graded
K-rings H(u) : H(A)→H(B); cf. Example 3.3.20.
Deﬁnition 12.7.1.A DG ring homomorphism u : A →B is called a quasi-
isomorphism of DG ringsif H(u) is an isomorphism.
Here is a fundamental result, due to B. Keller in 1994 [79], and independently to
V. Hinich in 1997 [66]. It is the justiﬁcation behind the use of DG ring resolutions
(see Remarks 13.4.24, 14.3.24 and 18.1.30).
Theorem 12.7.2. Letu :A→B be a quasi-isomorphism of DGK-rings. Then:
(1) The restriction functorRestu : D(B)→D(A) is an equivalence ofK-linear
triangulated categories, with quasi-inverseLIndu.
(2) For everyM∈D(Bop) andN∈D(B) there is an isomorphismM⊗L
AN
≃
− →
M⊗L
BN in D(K). This isomorphism is functorial inM and N.
(3) For every M,N ∈D(B) there is an isomorphism RHomA(M,N )
≃
− →
RHomB(M,N ) in D(K). This isomorphism is functorial inM and N.
Notice that the restriction functorRestu is suppressed in parts (2) and (3) of
the theorem. The proof hinges on the next lemma.
Lemma 12.7.3. Let u : A→B be a quasi-isomorphism of DGK-rings, letN∈
D(B), and letρ:P→N be a K-projective resolution inCstr(A).
(1) The homomorphism qu,P : P →B⊗A P in Cstr(A) from equation
(12.6.4), and the homomorphismψ: B⊗A P →N, ψ(b⊗p) := b·ρ(p),
in Cstr(B), are both quasi-isomorphisms.
(2) B⊗AP is a K-projective DGB-module.
238
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof.
(1) Look at the commutative diagram
B⊗AP
ψ //N
P
∼= //
qu,P
99
A⊗AP
u⊗idP
OO
idA⊗ρ//A⊗AN
∼=
OO
in Cstr(A), in which the arrows marked∼= are the canonical isomorphisms. The
homomorphism u⊗idP is a quasi-isomorphism, becauseu is a quasi-isomorphism
andP is K-ﬂat overA. The homomorphismidA⊗ρis a quasi-isomorphism, because
ρis a quasi-isomorphism andA is K-ﬂat over itself. Thereforequ,P andψare quasi-
isomorphisms.
(2) Take an acyclic DGB-module N. There is an isomorphism
HomB(B⊗AP,N )∼= HomA(P,N )
in Cstr(K), coming from adjunction for the DG ring homomorphismu. By assump-
tion the DG moduleHomA(P,N ) is acyclic. This shows thatB⊗AP is K-projective
overB. □
Proof of Theorem12.7.2.
(1) Take anyN∈D(B). Choose a K-projective resolutionρ:P→N in Cstr(A),
so that (LIndu◦Restu)(N)∼= B⊗AP in D(B). By the lemma we have a quasi-
isomorphismψ:B⊗AP→N in Cstr(B). This means that we have an isomorphism
Q(ψ) : (LIndu◦Restu)(N)
≃
− →N
in D(B), and it is functorial inN.
On the other hand, starting from a DG moduleM∈D(A), and choosing a K-
projective resolutionρ:P→M in Cstr(A), we have an isomorphismLIndu(M)∼=
B ⊗A P in D(B). So there is an isomorphism (Restu◦LIndu)(M) ∼=
B⊗A P in D(A). According to the lemma there is a quasi-isomorphism qu,P :
P→B⊗AP in Cstr(A). We obtain an isomorphism
Q(ρ)◦Q(qu,P )−1 : (Restu◦LIndu)(M)
≃
− →M
in D(A), and it is functorial inM.
(2) Choose a K-projective resolutionρ: P →M in C(Aop). This produces an
isomorphismφ1 :P⊗AN
≃
− →M⊗L
AN in D(K). The DG moduleP⊗AB∈C(Bop)
is K-projective, and there is a quasi-isomorphismψ: P⊗AB→M in Cstr(Bop),
by the lemma (withBop instead ofB). We get an isomorphism
φ2 := Q(ψ)⊗L
B idN : (P⊗AB)⊗BN
≃
− →M⊗L
BN
in D(K). There is also the canonical isomorphism
φ3 : (P⊗AB)⊗BN
≃
− →P⊗AN
in D(K). The functorial isomorphism we want is
φ2◦φ−1
3 ◦φ−1
1 :M⊗L
AN
≃
− →M⊗L
BN
in D(K).
(3) Let us choose a K-projective resolutionρ:P→M in C(A). This produces an
isomorphism
φ1 : RHomA(M,N )
≃
− →HomA(P,N )
239
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in D(K). The DG moduleB⊗AP∈C(B) is K-projective, and the homomorphism
ψ: B⊗AP→M in Cstr(B) is a quasi-isomorphism (again using the lemma). In
this way we have an isomorphism
φ2 : HomB(B⊗AP,N )
≃
− →RHomB(M,N )
in D(K). And there is the canonical isomorphism of adjunction
φ3 : HomB(B⊗AP,N )
≃
− →HomA(P,N )
in D(K). The functorial isomorphism we want is
φ2◦φ−1
3 ◦φ1 : RHomA(M,N )
≃
− →RHomB(M,N ). □
