---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-043-52-triangulated-and-cohomological-functors
section_title: "Triangulated and Cohomological Functors"
section_number: 5.2
pages: 94-96
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
additive categories, with translation functors TK and TL respectively. A T-additive
functor F : K →L was deﬁned in Deﬁnition 5.1.3.
A morphism of T-additive
functors η : F →G was introduced in Deﬁnition 5.1.5.
Deﬁnition 5.2.1. Let K and L be triangulated categories.
(1) A triangulated functor from K to L is a T-additive functor (F, τ) : K →L
that satisﬁes this condition: for every distinguished triangle
L
α−→M
β−→N
γ−→TK(L)
in K, the triangle
F(L)
F (α)
−−−→F(M)
F (β)
−−−→F(N)
τL◦F (γ)
−−−−−−−→TL(F(L))
is a distinguished triangle in L.
94
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(2) Suppose (G, ν) : K →L is another triangulated functor.
A morphism
of triangulated functors η : (F, τ) →(G, ν) is a morphism of T-additive
functors, as in Deﬁnition 5.1.5.
Sometimes we keep the translation isomorphism τ implicit, and refer to F as a
triangulated functor.
Deﬁnition 5.2.2. Let K be a triangulated category. A full triangulated subcategory
of K is a subcategory L ⊆K satisfying these conditions:
(a) L is a full additive subcategory (see Deﬁnition 2.2.6).
(b) L is closed under translations, i.e. L ∈L iﬀT(L) ∈L.
(c) L is closed under distinguished triangles, i.e. if L′ →L →L′′
△
−−→is a
distinguished triangle in K s.t. L′, L ∈L, then also L′′ ∈L.
Observe that L itself is triangulated, and the inclusion L →K is a triangulated
functor.
Proposition 5.2.3. For i = 0, 1, 2 let (Ki, Ti) be triangulated categories, and let
(Fi, τi) : (Ki−1, Ti−1) →(Ki, Ti) be triangulated functors. Deﬁne the T-additive
functor (F, τ) := (F2, τ2) ◦(F1, τ1) as in Deﬁnition 5.1.4. Then (F, τ) : (K0, T0) →
(K2, T2) is a triangulated functor.
Exercise 5.2.4. Prove Proposition 5.2.3.
Deﬁnition 5.2.5. Let K be a triangulated category, and let M be an abelian
category.
(1) A cohomological functor F : K →M is an additive functor, such that for
every distinguished triangle
L
α−→M
β−→N
γ−→T(L)
in K, the sequence
F(L)
F (α)
−−−→F(M)
F (β)
−−−→F(N)
is exact in M.
(2) A contravariant cohomological functor F : K →M is a contravariant addi-
tive functor, such that for every distinguished triangle
L
α−→M
β−→N
γ−→T(L)
in K, the sequence
F(N)
F (β)
−−−→F(M)
F (α)
−−−→F(L)
is exact in M.
Proposition 5.2.6. Let F : K →M be a cohomological functor, and let
L
α−→M
β−→N
γ−→T(L)
be a distinguished triangle in K. Then the sequence
· · · →F(Ti(L))
F (Ti(α))
−−−−−−→F(Ti(M))
F (Ti(β))
−−−−−−→F(Ti(N))
F (Ti(γ))
−−−−−−→F(Ti+1(L))
F (Ti+1(α))
−−−−−−−→F(Ti+1(M)) →· · ·
in M is exact.
95
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Proof. By axiom (TR2) we have these distinguished triangles:
Ti(L)
(−1)i · Ti(α)
−−−−−−−−→Ti(M)
(−1)i · Ti(β)
−−−−−−−−→Ti(N)
(−1)i · Ti(γ)
−−−−−−−−→Ti+1(L),
Ti(M)
(−1)i · Ti(β)
−−−−−−−−→Ti(N)
(−1)i · Ti(γ)
−−−−−−−−→Ti+1(L)
(−1)i+1 · Ti+1(α)
−−−−−−−−−−−→Ti+1(M),
Ti(N)
(−1)i · Ti(γ)
−−−−−−−−→Ti+1(L)
(−1)i+1 · Ti+1(α)
−−−−−−−−−−−→Ti+1(M)
(−1)i+1 · Ti+1(β)
−−−−−−−−−−−→Ti+1(N).
Now use the deﬁnition of a cohomological functor, noting that multiplying mor-
phisms in an exact sequence by −1 preserves exactness.
□
Proposition 5.2.7. Let K be a triangulated category. For every P ∈K the functor
HomK(P, −) : K →Mod K
is a cohomological functor, and the functor
HomK(−, P) : K →Mod K
is a contravariant cohomological functor.
Proof. We will prove the covariant statement.
The contravariant statement is
proved similarly, and we leave this to the reader.
Consider a distinguished triangle L
α−→M
β−→N
γ−→T(L) in K. We have to prove
that the sequence
HomK(P, L)
Hom(idP ,α)
−−−−−−−−→HomK(P, M)
Hom(idP ,β)
−−−−−−−→HomK(P, N)
in Mod K is exact. In view of Proposition 5.3.1, all we need to show is that for
every ψ : P →M s.t. β ◦ψ = 0, there is some φ : P →L s.t. ψ = α ◦φ. In a
picture, we must show that the diagram below (solid arrows)
P
id
/
φ

P
/
ψ

0
/

T(P)
T(φ)

L
α
/ M
β
/ N
γ
/ T(L) .
can be completed (dashed arrow). This is true by (TR2) (= turning) and (TR3)
(= extending).
□
Exercise 5.2.8. Prove the contravariant statement in the proposition above.
Question 5.2.9. Let K and L be triangulated categories, and let F : K →L be
an additive functor. Is it true that there is at most one isomorphism of functors
τ : F ◦TK
≃
−→TL ◦F such that the pair (F, τ) is a triangulated functor?
