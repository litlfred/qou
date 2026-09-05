---
doc_id: arxiv-math-0409593v1
doc_title: "CATEGORIFICATION OF THE BRAID GROUPS RAPHAËL ROUQUIER 1. Introduction Actions of braid groups on triangulated categories are quite widesp read. They arise for instance in represent"
section_id: sec-002-21-a-general-construction
section_title: "A general construction"
section_number: 2.1
pages: 2-4
source_pdf: 0409593v1.pdf
source_sha256: ad965f5c80838824
doc_brief: "CATEGORIFICATION OF THE BRAID GROUPS RAPHAËL ROUQUIER 1. Introduction Actions of braid groups on triangulated categories are quite widesp read. They arise for instance in representation theory, for co"
---
2.1.1. This section can probably be skipped in a ﬁrst reading.
We will be working here with algebraic triangulated categories (following Keller), a simple
setting that provides functorial cones.
Let E be a Frobenius category (an exact category with enough project ive and injective objects
and where injective and projective objects coincide). Let Comp acyc(E-proj) be the category of
acyclic complexes of projective objects of E. Let Frob be the 2-category of Frobenius categories,
with 1-arrows the exact functors that send projectives to proj ectives and 2-arrows the natural
transformations of functors.
The construction E ↦→Compacyc(E-proj) is an endo-2-functor of Frob. The 2-functor from E
to the 2-category of triangulated categories that sends E to its stable category ¯E factors through
the previous functor.
The important point is that the category Comp acyc(E-proj) has functorial cones. Given F, G :
Compacyc(E-proj) → Compacyc(E ′-proj) and φ : F → G, then we have a well deﬁned cone C(φ)
of φ and we have morphisms G → C(φ) and C(φ) → F [1] such that F → G → C(φ) → F [1]
gives a distinguished triangle of functors from ¯E to ¯E ′.
Note that if φ0 : F0 → G0 is a morphism of functors (exact, preserving projectives) betwe en
E and E ′, then we get via Comp acyc(−) a morphism of functors φ : F → G, with F, G :
Compacyc(E-proj) → Compacyc(E ′-proj).
CATEGORIFICATION OF THE BRAID GROUPS 3
The category of functors (exact, preserving projectives) Com pacyc(E-proj) → Compacyc(E ′-proj)
is a Frobenius category. We deﬁne the category AlgTr( E, E ′) to be its stable category. Its ob-
jects are the exact functors Comp acyc(E-proj) → Compacyc(E ′-proj) and Hom AlgTr(E,E ′)(F, G) is
the image of Hom( F, G) in Hom Fun(¯E, ¯E ′)( ¯F , ¯G).
This deﬁnes the 2-category of algebraic triangulated categories A lgTr, with objects the Frobe-
nius categories E. We have a 2-functor from AlgTr to the 2-category of triangulate d categories
obtained by sending E to ¯E. It is 2-fully faithful.
2.1.2. Let C and D be two algebraic triangulated categories, F : C → D , G : D → C be two
functors and Φ be a self-equivalence of C. Let there be given also two adjoint pairs ( F, G) and
(G, F Φ). We have four morphisms (units and counits of the adjunctions)
η : 1 D → F Φ G, ε : GF Φ → 1C
η′ : 1 C → GF, ε ′ : F G → 1D.
Let Υ be the cocone of ε′ and Υ ′ be the cone of η : there are distinguished triangles of functors
Υ → F G
ε′
− →1D↝ and 1 D
η
− →F Φ G → Υ ′↝ .
Assume
(1) 1 C
η′
− →GF
εΦ −1
− − − →Φ −1 0
↝
is a distinguished triangle.
Proposition 2.1. The functors Υ and Υ ′ are inverse self-equivalences of D.
Proof. Let γ be the map F Φ G → Υ ′ in the triangle above, i.e., we have the distinguished
triangle 1 D
η
− →F Φ G
γ
− →Υ ′↝ . We have a commutative diagram with horizontal and vertical
distinguished triangles
F G
/d79/d79/d79/d15/d79/d15/d79/d15
F G
F Gη /d47/d47
id
/d54/d54/d108/d108/d108/d108/d108/d108/d108/d108/d108/d108/d108/d108/d108/d108/d108
F GFΦ G
F Gγ /d47/d47
F εG
/d79/d79
F GΥ ′ /d47/d47/d47/d111/d47/d111/d47/d111
F Φ G
F η′Φ G
/d79/d79
The octahedral axiom shows that ( F Gγ) ◦ (F η′Φ G) : F Φ G
∼
→ F GΥ ′ is an isomorphism.
We have a commutative diagram
F Φ G
F η′Φ G /d47/d47
id /d41/d41/d82/d82/d82/d82/d82/d82/d82/d82/d82/d82/d82/d82/d82/d82 F GFΦ G
F Gγ /d47/d47
ε′F Φ G
/d15/d15
F GΥ ′
ε′Υ ′
/d15/d15
F Φ G γ
/d47/d47 Υ ′
The distinguished triangle ΥΥ ′ → F GΥ ′ ε′Υ ′
− − →Υ ′ ↝ gives a distinguished triangle ΥΥ ′ →
F Φ G
γ
− →Υ ′↝ , hence ΥΥ ′ ≃ 1D.
The case of Υ ′Υ is similar — note that the triangle (1) shows that GF ≃ idD ⊕Φ −1, hence
Φ commutes with GF . □
4 RAPHA ¨EL ROUQUIER
Remark 2.2. One sees easily that ηF + F Φ η′ : F ⊕ F Φ
∼
→ F Φ GF and Gη + η′Φ G : G ⊕ Φ G
∼
→
GF Φ G are isomorphisms. One can show that the requirement that ηF G + F Φ η′G : F G ⊕
F Φ G → F Φ GF G and F Gη + F η′Φ G : F G ⊕ F Φ G → F GFΦ G are isomorphisms, instead of
the stronger requirement that (1) is a distinguished triangle, is eno ugh to get Proposition 2.1.
2.1.3. Let us recall a version of Barr-Beck’s Theorem ([Mac, §VI.7, exercice 7], [De2, §4.1]).
Let C be a category. A comonad is the data of a functor H : C → C , of c : H → H 2 and
ε : H → id such that ( cH) ◦ c = ( Hc) ◦ c and ( εH) ◦ c = ( Hε) ◦ c. Note that ε is determined
by c.
A coaction of ( H, c, ε) on an object M of C is the data of ρ : M → H(M) such that
ε(M) ◦ ρ = id M and c ◦ ρ = F (ρ) ◦ ρ. The category ( H, c, ε)-comod has objects the pairs ( M, ρ)
and a morphism ( M, ρ) → (M ′, ρ′) is a morphism f : M → M ′ such that ρ′f = H(f )ρ.
Let A and B be two abelian (resp. algebraic triangulated categories), T : A → B an exact
functor (resp. a triangulated functor). Assume T has a right adjoint U. Put H = T U, denote by
ε : H → idB and η : id A → U T the counit and unit of adjunctions and let c = T ηU : H → H 2.
We have a functor ˜T : A → (H, c, ε)-comod given by M ↦→(T M, T η(M)).
The following Theorem is an easy application of Barr-Beck’s general r esult to abelian and
triangulated categories.
Theorem 2.3. If T is faithful, then ˜T : A
∼
→ (H, c, ε)-comod is an equivalence.
We deduce from this Theorem that the category C, together with the functors F , G and
the adjunctions, is determined by D, Θ = F G and c = F η′G : Θ → Θ 2. We view this as a
categorical version of the “ﬁxed points” construction.
Remark 2.4. Let V = K0(D), U = K0(C), f = [ F ] : U → V and g = [ G] : V → U. Assume
[Φ] = id U . Then, gf = 2 id U and θ = [Θ] : x ↦→x − f g(x) : V → V is an involution. One
recovers U (up to unique isomorphism) from θ acting on V as V θ.
