---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-086-127-dg-ring-quasi-isomorphisms
section_title: "DG Ring Quasi-Isomorphisms"
section_number: 12.7
pages: 238-240
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
homomorphism of DG K-rings u : A →B induces a homomorphism of graded
K-rings H(u) : H(A) →H(B); cf. Example 3.3.20.
Deﬁnition 12.7.1. A DG ring homomorphism u : A →B is called a quasi-
isomorphism of DG rings if H(u) is an isomorphism.
Here is a fundamental result, due to B. Keller in 1994 [79], and independently to
V. Hinich in 1997 [66]. It is the justiﬁcation behind the use of DG ring resolutions
(see Remarks 13.4.24, 14.3.24 and 18.1.30).
Theorem 12.7.2. Let u : A →B be a quasi-isomorphism of DG K-rings. Then:
(1) The restriction functor Restu : D(B) →D(A) is an equivalence of K-linear
triangulated categories, with quasi-inverse LIndu.
(2) For every M ∈D(Bop) and N ∈D(B) there is an isomorphism M ⊗L
AN
≃
−→
M ⊗L
B N in D(K). This isomorphism is functorial in M and N.
(3) For every M, N ∈D(B) there is an isomorphism RHomA(M, N)
≃
−→
RHomB(M, N) in D(K). This isomorphism is functorial in M and N.
Notice that the restriction functor Restu is suppressed in parts (2) and (3) of
the theorem. The proof hinges on the next lemma.
Lemma 12.7.3. Let u : A →B be a quasi-isomorphism of DG K-rings, let N ∈
D(B), and let ρ : P →N be a K-projective resolution in Cstr(A).
(1) The homomorphism qu,P
: P
→B ⊗A P in Cstr(A) from equation
(12.6.4), and the homomorphism ψ : B ⊗A P →N, ψ(b ⊗p) := b·ρ(p),
in Cstr(B), are both quasi-isomorphisms.
(2) B ⊗A P is a K-projective DG B-module.
238
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Proof.
(1) Look at the commutative diagram
B ⊗A P
ψ
/ N
P
∼
=
/
qu,P
9
A ⊗A P
u ⊗idP
O
idA ⊗ρ / A ⊗A N
∼
=
O
in Cstr(A), in which the arrows marked ∼= are the canonical isomorphisms. The
homomorphism u ⊗idP is a quasi-isomorphism, because u is a quasi-isomorphism
and P is K-ﬂat over A. The homomorphism idA ⊗ρ is a quasi-isomorphism, because
ρ is a quasi-isomorphism and A is K-ﬂat over itself. Therefore qu,P and ψ are quasi-
isomorphisms.
(2) Take an acyclic DG B-module N. There is an isomorphism
HomB(B ⊗A P, N) ∼= HomA(P, N)
in Cstr(K), coming from adjunction for the DG ring homomorphism u. By assump-
tion the DG module HomA(P, N) is acyclic. This shows that B⊗AP is K-projective
over B.
□
Proof of Theorem 12.7.2.
(1) Take any N ∈D(B). Choose a K-projective resolution ρ : P →N in Cstr(A),
so that (LIndu ◦Restu)(N) ∼= B ⊗A P in D(B). By the lemma we have a quasi-
isomorphism ψ : B⊗AP →N in Cstr(B). This means that we have an isomorphism
Q(ψ) : (LIndu ◦Restu)(N)
≃
−→N
in D(B), and it is functorial in N.
On the other hand, starting from a DG module M ∈D(A), and choosing a K-
projective resolution ρ : P →M in Cstr(A), we have an isomorphism LIndu(M) ∼=
B ⊗A P
in
D(B).
So
there
is
an
isomorphism (Restu ◦LIndu)(M)
∼=
B ⊗A P in D(A). According to the lemma there is a quasi-isomorphism qu,P :
P →B ⊗A P in Cstr(A). We obtain an isomorphism
Q(ρ) ◦Q(qu,P )−1 : (Restu ◦LIndu)(M)
≃
−→M
in D(A), and it is functorial in M.
(2) Choose a K-projective resolution ρ : P →M in C(Aop). This produces an
isomorphism φ1 : P ⊗A N
≃
−→M ⊗L
A N in D(K). The DG module P ⊗A B ∈C(Bop)
is K-projective, and there is a quasi-isomorphism ψ : P ⊗A B →M in Cstr(Bop),
by the lemma (with Bop instead of B). We get an isomorphism
φ2 := Q(ψ) ⊗L
B idN : (P ⊗A B) ⊗B N
≃
−→M ⊗L
B N
in D(K). There is also the canonical isomorphism
φ3 : (P ⊗A B) ⊗B N
≃
−→P ⊗A N
in D(K). The functorial isomorphism we want is
φ2 ◦φ−1
3
◦φ−1
1
: M ⊗L
A N
≃
−→M ⊗L
B N
in D(K).
(3) Let us choose a K-projective resolution ρ : P →M in C(A). This produces an
isomorphism
φ1 : RHomA(M, N)
≃
−→HomA(P, N)
239
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
in D(K). The DG module B ⊗A P ∈C(B) is K-projective, and the homomorphism
ψ : B ⊗A P →M in Cstr(B) is a quasi-isomorphism (again using the lemma). In
this way we have an isomorphism
φ2 : HomB(B ⊗A P, N)
≃
−→RHomB(M, N)
in D(K). And there is the canonical isomorphism of adjunction
φ3 : HomB(B ⊗A P, N)
≃
−→HomA(P, N)
in D(K). The functorial isomorphism we want is
φ2 ◦φ−1
3
◦φ1 : RHomA(M, N)
≃
−→RHomB(M, N).
□
