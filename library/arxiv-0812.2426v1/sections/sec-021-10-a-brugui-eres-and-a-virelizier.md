---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-021-10-a-brugui-eres-and-a-virelizier
section_title: "A. BRUGUI `ERES AND A. VIRELIZIER"
section_number: 10
pages: 10-11
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨ uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
PSfrag replacements
,,,
,,
,,,,
.
Figure 5. Rules for transforming Hopf diagrams to tangles
D = ↝ hD = ↝ Φ(D) = ∼
Figure 6. From Hopf diagrams to ribbon string links
that is, a ribbon (2 n, 0)-tangle consisting of n arc components, without any closed
component, such that the k-th arc joins the (2k − 1)-to the 2k-th bottom endpoints.
Then, by rotating hD, we get a ribbon n-string link Φ( D):
D Hopf diagram ↝PSfrag replacements hD ↝ Φ(D) =PSfrag replacements
hD .
An example of this procedure is depicted in Figure 6.
This leads to a functor Φ : Diag → RSL deﬁned on objects by n ↦→Φ(n) = n
and on morphisms by D ↦→Φ(D).
Theorem 2.3 ([BV05, Theorem 4.5]) . Φ : Diag → RSL is a well-deﬁned monoidal
functor and there exists (constructive proof ) a monoidal fu nctor Ψ : RSL → Diag
which satisﬁes Φ ◦ Ψ = 1 RSL.
Note that by ‘constructing proof’ we mean there is an explicit algorit hm that
associates to a ribbon string T a Hopf diagram Ψ( T ) such that Φ
(
Ψ(T )
)
= T
(see [BV05]). The key point is that such a functor Ψ exists thanks to the relations
we put on Hopf diagrams.
Let now B be a ribbon autonomous category which admits a coend C. Let us
answer to the second question of Section 2.1: given a ribbon n-string link T , how
to compute the morphism φT : C⊗n → /BD which is deﬁned by universal property?
Recall C is a Hopf algebra in B and denote its coproduct, counit, and antipode
by ∆ C , εC, and SC respectively. The twist (and its inverse) of B is encoded by
morphisms θ±
C → C → /BD (see Section 2.2). Furthermore, we can deﬁned a Hopf
pairing ωC : C ⊗C → /BD via:
ωC (iX ⊗iY ) = (ev X ⊗ evY )(id∨ X ⊗τ∨ Y,X τX, ∨ Y ⊗ id∨ Y ),
where τ is the braiding of B and iY : ∨Y ⊗ Y → C is the universal dinatural
transformation of the coend C. Finally, we set ω+
C =ωC (S−1
C ⊗ idC) and ω−
C =ωC .
CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INV ARIANTS 11
Theorem 2.4 ([BV05, Theorem 5.1]) . Let T be ribbon n-string link. Let D be
any Hopf diagram (with n entries) which encodes T , that is, such that Φ(D) = T
(recall there is an algorithm producing such a Hopf diagram) . Then the morphism
φT : C⊗n → /BD deﬁned by T is given by replacing in D the generators ∆ , ε, ω±, θ±,
S±1, and τ ±1 (see Figure 1) by the morphisms ∆ C , εC, ω±
C , θ±
C , S±1
C , and τ ±1
C,C
respectively.
Remark that the product and unit of the coend C are not needed to represent
Hopf diagrams.
Let us summarize the above universal construction of quantum inv ariants, start-
ing from a ribbon category B which admits a coend C. Pick a normalizable Kirby
elementα of B (for example as in Theorem 2.1). Recall it gives rise to the invariant
τB(M,α ) of 3- manifolds. Let M be a 3- manifold. Present M by surgery along
a framed link L, which can be viewed as the closure of a ribbon n-string link T
where n is the number of components of L. Encode the string link T by a Hopf
diagram D:
M ≃S3
L, L ∼PSfrag replacements
T with T =PSfrag replacements
T
↦→D =PSfrag replacements
T
The morphism φT : C⊗n → /BD associated to T can be computed by replacing the
generators of D by the corresponding structural morphisms of the coend C. Then
evaluateφT with the Kirby element α and normalize to get the invariant:
τB(M ;α) =
PSfrag replacements
ω−
C
ω+
C
SC
τC,C
∆ C
α
θ+
C
θ−
C
b−(L) −n
−b−(L)
PSfrag replacements
ω−
C
ω+
C
SC
τC,C
∆ C
α
θ+
C
θ−
C
b−(L) −n
−b−(L)
PSfrag replacements
ω−
C ω+
C
SC τC,C
∆ C∆ C
αα
θ+
C
θ−
C
b−(L) −n
−b−(L)
In particular, to compute such quantum invariants deﬁned from th e center Z(C)
of a autonomous category C, one needs to give an explicit description of the struc-
tural morphism of the coend of Z(C) in terms of the category C. In the next section,
