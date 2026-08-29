---
doc_id: arxiv-math-0111205v1
doc_title: "From Subfactors to Categories and Topology II"
section_id: sec-043-81-an-adjoint-for-the-forgetful-functor-z1c-c
section_title: "An adjoint for the forgetful functor Z1(C) → C"
section_number: 8.1
pages: 49-50
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
doc_brief: "From Subfactors to Categories and Topology II — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
In Section 4 we proved that the functor F : Z1(C) → B is fully faithful and essentially
surjective. By [35, Theorem IV.4.1] this implies that F has a two-sided adjoint G : B →
Z1(C). Together with Lemma 5.2 this implies
HomC(X, Y ) ∼= HomB(F (X, eX ), J (Y ⊠ 1)J) ∼= HomZ1(C)((X, eX ), G(J (Y ⊠ 1)J)),
where ( X, eX ) ∈ Z 1(C), Y ∈ C . With the forgetful functor H : Z1(C) → C , (X, eX ) ↦→X
this becomes
HomC(H(X, eX ), Y ) ∼= HomZ1(C)((X, eX ), G(J (Y ⊠ 1)J)). (8.1)
We thus have
49
Proposition 8.1 The forgetful functor H : Z1(C) → C , (X, eX ) ↦→X has a two-sided
adjoint K : C → Z 1(C), X ↦→G(J (X ⊠ 1)J). On the objects one has
K(Y ) ∼=
⨁
(X,eX )
dim HomC(X, Y ) (X, eX ), (8.2)
where the summation is over the isomorphism classes of simpl e objects in Z1(C).
Proof. Eq. (8.1) just says that K is a right adjoint of H. That K is also a left adjoint of H
is proven in the same way. One must also show that the isomorph isms in (8.1) are natural
w.r.t. ( X, eX ) and Y . We leave this to the reader. For Y = Xi and ( X, eX ) simple, (8.1)
implies that K(Xi) contains ( X, eX ) with multiplicity dim Hom C(X, Xi). For general Y
we have
K(Y ) ∼=
⨁
i∈Γ
dim Hom(Xi, Y )
⨁
(X,eX )
dim HomC(X, Xi) (X, eX ),
and (8.2) follows by semisimplicity of C. ■
Remark 8.2 By the general theory [38] there is a dual Frobenius algebra ˆQ = ( ˆQ, . . .)
in B, where ˆQ = J J. Under the equivalence Z1(C)
⊗
≃ B , ˆQ corresponds to
G(J J) = K(1) ∼=
⨁
(X,eX )
dim HomC(X, 1) (X, eX ). (8.3)
Thus this object is part of the Frobenius algebra in Z1(C) which establishes the weak
monoidal Morita equivalence Z1(C) ≈ C ⊠ Cop. K(1) clearly contains the unit ( 1, id) of
Z1(C) with multiplicity one. The reader might ﬁnd it amusing to id entify explicitly the
morphisms w, w′ in Z1(C) which come with the canonical Frobenius algebra. ✷
