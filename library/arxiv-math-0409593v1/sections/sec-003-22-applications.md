---
doc_id: arxiv-math-0409593v1
doc_title: "CATEGORIFICATION OF THE BRAID GROUPS RAPHAËL ROUQUIER 1. Introduction Actions of braid groups on triangulated categories are quite widesp read. They arise for instance in represent"
section_id: sec-003-22-applications
section_title: "Applications"
section_number: 2.2
pages: 4-6
source_pdf: 0409593v1.pdf
source_sha256: ad965f5c80838824
doc_brief: "CATEGORIFICATION OF THE BRAID GROUPS RAPHAËL ROUQUIER 1. Introduction Actions of braid groups on triangulated categories are quite widesp read. They arise for instance in representation theory, for co"
---
2.2.1. We consider schemes of ﬁnite type type over an algebraic closu re of a ﬁnite ﬁeld Fq
(the case of complex algebraic varieties is similar). Let π : X → Y be a smooth projective
morphism already deﬁned over Fq. Assume the geometric ﬁbers are projective lines.
Let Λ be a ﬁeld of coeﬃcients (=an extension of Qℓ for ℓ ⁄ |q a prime number). Put C = Db(Y )
and D = Db(X) (bounded derived categories of constructible sheaves of Λ-vec tor spaces). Take
F = π∗, G = Rπ∗ and Φ =?(1)[2]. We have a canonical isomorphism (projection formula )
? ⊗ Rπ∗Λ X
∼
→ Rπ∗π∗. Via this isomorphism, η′ becomes id ⊗η′(Λ Y ) and ε becomes id ⊗t,
where t : Rπ∗Λ X → Λ Y (−1)[−2] is the trace map (an isomorphism on H2).
So, the triangle (1) is obtained from the triangle Λ Y
η′(Λ Y )
− − − − →Rπ∗Λ X
t
− →Λ Y (−1)[−2]↝ by
applying ? ⊗. This is indeed a distinguished triangle, for it is so at geometric ﬁbers.
Let L be a relative ample sheaf for π and c ∈ H 2(X, Λ(1)) be its ﬁrst Chern class. The hard
Lefschetz Theorem states that the composition Λ Y
η′(Λ Y )
− − − − →Rπ∗Λ X
c
− →Rπ∗Λ X(1)[2]
t(1)[2]
− − − →Λ Y is
an isomorphism. It follows that the connecting map in the triangle abo ve is zero.
Thus, we are in the setting of §2.1.2 and we get a self-equivalence of Db(X).
This can be also constructed as a kernel transform. Let α, β : X ×Y X → X be the ﬁrst
and second projections. Let i : ∆ X → X ×Y X be the closed immersion of the diagonal and
CATEGORIFICATION OF THE BRAID GROUPS 5
j : Z → X ×Y X be the open immersion of the complement of ∆ X. Denote by ˜ε : 1 Db(X×Y X) →
i∗i∗ and ˜η : Rj!j∗ → 1Db(X×Y X) the adjunction morphisms. One checks easily that there is a
commutative diagram where the rows are distinguished triangles
Υ /d47/d47 π∗Rπ∗
ε′
/d47/d47
∼
/d15/d15
1D
∼
/d15/d15
/d47/d47/d47/d111 /d47/d111/d47/d111/d47/d111 /d47/d111
Rβ∗Rj!j∗α∗
Rβ∗ ˜ηα∗
/d47/d47 Rβ∗α∗
Rβ∗ ˜εα∗
/d47/d47 Rβ∗i∗i∗α∗ /d47/d47/d47/d111/d47/d111/d47/d111
where the middle vertical map is the base change isomorphism.
Denote by p, q : Z → X the ﬁrst and second projections. Then, Υ ≃ Rp!q∗ and Υ ′ ≃ Rp∗q!.
2.2.2. Assume we are in the setting of §2.1.2 with C = Db(k-mod) where k is a ﬁeld and
the categories and functors involved are k-linear. There is an integer n such that Φ =?[ n].
Let E = F (k). Then, F ≃ E⊗k? and G ≃ R Hom(E, ?). The morphism ε comes from
t : Hom(E, E[n]) → k.
The morphism ε is the counit of an adjoint pair ( G, F Φ) if and only if dim k
⨁
i Hom(E, M [i]) <
∞ for all M ∈ D and Hom( E, M ) × Hom(M, E[n]) → k, (f, g) ↦→t(gf ) is a perfect pairing for
all M ∈ D .
The triangle (1) is distinguished if and only if 0 → k · id → ⨁
i Hom(E, E[i])
t
− →k → 0 is an
exact sequence.
In other words, E is an n-spherical object and Υ, Υ ′ are the corresponding twist functors of
Seidel and Thomas [SeiTho, §2b]. So, the framework above corresponds exactly to the twist
functor theory when C ≃ Db(k-mod).
Remark 2.5. The case C = Db(kd-mod) also leads to interesting examples.
Remark 2.6. It would be interesting to see if the construction of §2.1.2 can be used to construct
automorphisms of derived categories of Calabi-Yau varieties corre sponding, via Kontsevich’s
homological mirror symmetry conjecture, to graded symplectic au tomorphisms on the mirror
associated to Lagrangian submanifolds more complicated than sphe res.
2.2.3. Let us consider here two abelian categories A and B and ˜F : A → B , ˜G : B → A and
˜Φ a self-equivalence of A. We assume we have two adjoint pairs ( ˜F , ˜G) and ( ˜G, ˜F ˜Φ). So, we
have four morphisms (units and counits of the two adjunctions)
˜η : 1 B → ˜F ˜Φ ˜G, ˜ε : ˜G ˜F ˜Φ → 1A
˜η′ : 1 A → ˜G ˜F , ˜ε′ : ˜F ˜G → 1B.
Let ˜Υ be the complex 0 → ˜F ˜G
˜ε′
− →1B → 0 and ˜Υ ′ the complex 0 → 1B
˜η
− → ˜F ˜Φ ˜G → 0 (with
˜F ˜G and ˜F ˜Φ ˜G in degree 0). We put C = K(A) and D = K(B) and we denote by F , G, etc...
the extensions of ˜F , ˜G, etc... to C and D.
Assume B is artinian and noetherian (every object is a ﬁnite extension of simple objects).
If we have the equality [ ˜G ˜F ] = [id] + [ ˜Φ −1] as endomorphisms of K0(A) (or more generally, if
[ ˜F ˜Φ ˜G ˜F ˜G] = [ ˜F ˜G ˜F ˜Φ ˜G] = [ ˜F ˜G] + [ ˜F ˜Φ ˜G] in End( K0(B))), then, the conclusion of Proposition
2.1 remains valid.
Let us justify this, following ideas of Rickard [Ri, §3]. There is an adjoint pair (Υ ′, Υ), hence
there is a map u : id → ΥΥ ′ that doesn’t vanish on a non-zero object of B. One shows that
ΥΥ ′ is homotopy equivalent to a complex of functors with only one non-ze ro term, R, in degree
6 RAPHA ¨EL ROUQUIER
0 and R is an exact functor. The assumption on classes shows that [ R] = [id]. So, R sends a
simple object to itself, for a simple object is characterized amongst objects of B by its class in
K0(B). In particular, u : id → R is an isomorphism on simple objects. So, u is an isomorphism.
