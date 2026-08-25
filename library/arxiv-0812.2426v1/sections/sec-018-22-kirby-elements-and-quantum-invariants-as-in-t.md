---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-018-22-kirby-elements-and-quantum-invariants-as-in-t
section_title: "Kirby elements and quantum invariants. As in the previous section, let B"
section_number: 2.2
pages: 6-8
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨ uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
be a ribbon autonomous category with a coend C. In this setting, k = End C(/BD ) is
a commutative monoid.
Let L be a framed link in S3 with n components. There always exists a (non-
unique) ribbon n-string link T such that L is isotopic to the closure of T . For
α ∈ HomC(/BD ,C ), set
τB(L;α) = φT ◦α⊗n ∈ k,
where φT : C⊗n → /BD is deﬁned as above.
Following [Vir06], by a Kirby element of B, we mean a morphismα ∈ HomB(/BD ,C )
such that, for any framed link L, τB(L;α) is well-deﬁned and invariant under iso-
topies and 2-handle slides of L. A Kirby element α of B is said to be normalizable
1A framed link with n components is always the closure of some ribbon n-string link.
CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INV ARIANTS 7
if τB(© +1;α) and τB(© −1;α) are invertible in k, where © ±1 denotes the unknot
with framing ±1.
By universality of the coaction δ of C on objects of C, we see that the twist
θY :Y →Y of B and its inverse lead to morphisms θ±
C : C → /BD such that:
θ±1
Y = (id Y ⊗θ±
C )δY.
a Ifα is a Kirby element of B, we have: τB(© ±1;α) = θ±
Cα, so that α is normalizable
if and only if θ±
Cα are invertible in k.
Recall (see [Lic97]) that every (closed, connected, oriented) 3-m anifold can be
obtained from S3 by surgery along a framed link L ⊂ S3. For any framed link L
in S3, we will denote by ML the 3-manifold obtained from S3 by surgery along
L, by nL the number of components of L, and by b−(L) the number of negative
eigenvalues of the linking matrix of L.
An immediate consequence of the Kirby theorem [Kir78] is that if α is a normal-
izable Kirby element of B, then:
τB(ML;α) = (θ+
Cα)b− (L)−nL (θ−
Cα)−b− (L) τB(L;α)
is an invariant of 3-manifolds. Furthermore these invariants are mu ltiplicative under
the connected sum of 3- manifolds: τB(M #M ′;α) = τB(M ;α)τB(M ′;α).
Note that if α is a normalizable Kirby element and k is an automorphism of /BD ,
then kα is also a normalizable Kirby element. The normalization of the invariant
τB(M ;α) has been chosen so that τB(M ;kα) = τB(M ;α).
The question is now: how to determine the (normalizable) Kirby elemen t of B?
A partial answer was given in [Vir06]. Denoting by mC , ∆ C , and SC respectively
the product, coproduct, and antipode of the Hopf algebra C, we have:
Theorem 2.1 ([Vir06, Theorem 2.5]) . Any morphism α : /BD →C in B such that:
SCα =α and (mC ⊗ idC )(idC ⊗ ∆ C )(α ⊗α) = α ⊗α
is a Kirby element of B.
For instance, the unit uC of C is a normalizable Kirby element (its associated
invariant is the trivial one).
A more interesting example of a a Kirby element is an S-invariant integral Λ of
C, that is, a morphism Λ : /BD →C such that SC (Λ) = Λ and mC (Λ ⊗ idC ) = Λ εC =
mC (idC ⊗ Λ), where εC is the counit of C. For the existence of such integrals,
we refer to [BKLT00]. If Λ is normalizable, then the associated invaria nt is the
Lyubashenko’s one [Lyu95], up to a diﬀerent normalization.
Note that other Kirby elements exist in general (see [Vir06]).
Remark 2.2. Assume B is a modular category in the sense of [Tur94], that is, a
ribbon fusion category with invertible S-matrix. Let {Vi}i∈I be a representative
family of simple objects of B. Then B admits a coend C = ⨁
i∈I
∨Vi ⊗Vi. Let
φX :X → ∨∨X be the sovereign structure of B and set:
Λ =
∑
i∈I
dim(Vi) (id∨ Vi ⊗φ−1
i )coevVi : /BD →C,
Then Λ is a SC-invariant integral of C. Furthermore it is normalizable and its
associated invariant is the Reshetikhin-Turaev one [Tur94], up to a d iﬀerent nor-
malization. More precisely, assuming dim B = ∑
i∈I dim(Vi)2 has a square root D
in k (which is then invertible in this context), setting ∆ − =θ−
C Λ, and denoting by
b1(M ) the ﬁrst Betti number of M , we have:
RTB(M ) = D−1
(D
∆ −
) b1(M)
τB(M ; Λ).
