---
doc_id: arxiv-1507.06276v2
doc_title: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS"
section_id: sec-015-42-twisted-cylinder-twists
section_title: "Twisted cylinder twists"
section_number: 4.2
pages: 18-19
source_pdf: 1507.06276v2.pdf
source_sha256: f552aa5de7125b23
toc_source: outline
doc_brief: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS — Let g be a symmetrizable Kac-Moody algebra and let Uq(g) de- note the corresponding quantized enveloping algebra."
---
considered in the present paper in full generality, we introduce a slig ht generaliza-
tion of tom Dieck’s notion of a cylinder twist for ( B, A). This generalization involves
a second twist which suggests the slightly repetitive terminology.
Let tw : A → A be braided tensor equivalence given by M ↦→Mtw and
f ↦→ftw ∈ Hom(Mtw,N tw) for all M,N ∈ Ob(A) and f ∈ Hom(M,N ). This
means that tw is a braided tensor functor as deﬁned in [Kas95, Deﬁnition XIII.3.6]
and an equivalence of categories. A family t = (tM )M∈Ob(A) of morphisms tM ∈
HomB(M,M tw) is called a B-tw-endomorphism of A if
tN ◦f =ftw ◦tM(4.4)
for all f ∈ HomA(M,N ). In other words, a B-tw-endomorphism of A is a natural
transformation t : ForB
A → ForB
A ◦tw.
UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS 19
Deﬁnition 4.6. Let (B, A) be a tensor pair and tw : A → A a braided tensor
equivalence. A tw-cylinder twist for (B, A) consists of a B-tw-automorphism t =
(tM )M∈Ob(A) of A such that
tM⊗N = (tM ∗ 1N tw )cN tw,M (tN ∗ 1M )cM,N(4.5)
for all M,N ∈Ob(A) = Ob(B).
Let ( B, A) be a tensor pair with a tw-cylinder twist. The relation ctw
N,M =
cN tw,M tw and (4.4) imply that
tM⊗N ◦cN,M =cN tw,M tw ◦tN ⊗M.
As in the proof of Proposition 4.5 one now obtains
(tM ∗ 1N tw )cN tw,M (tN ∗ 1M )cM,N =cN tw,M tw (tN ∗ 1M tw )cM tw,N (tM ∗ 1N ).(4.6)
Example 4.7. Consider the setting of Example 4.1. Let ϕ : Uq(g) → Uq(g) be
a Hopf algebra automorphism. For any M ∈ Ob(Oint) let Mϕ be the integrable
representation with left action •ϕ given by u •ϕ m = ϕ(u)m for all u ∈ Uq(g),
m ∈ M . By [Twi92, Theorem 2.1] one has ϕ(U +) = U + and ϕ(U 0) = U 0 and
hence Mϕ ∈ Ob(Oint). Moreover, as ϕ(U 0) = U 0 the map ϕ induces a group
isomorphism ϕP :P →P . We assume additionally that ϕP is an isometry, that is
(ϕP (λ),ϕP (µ)) = (λ,µ ) for all λ,µ ∈P . Then one obtains an auto-equivalence of
braided tensor categories
tw : Oint → Oint
given by tw(M ) = Mϕ andtw(f ) = f . In this case relations (4.5) and (4.6) become
tM⊗N = (tM ⊗ 1) ˆRN ϕ ,M (tN ⊗ 1) ˆRM,N,(4.7)
(tM ⊗ 1) ˆRN ϕ,M (tN ⊗ 1) ˆRM,N = ˆRN ϕ,M ϕ (tN ⊗ 1) ˆRM ϕ,N (tM ⊗ 1),(4.8)
respectively, for any M,N ∈Ob(Oint).
