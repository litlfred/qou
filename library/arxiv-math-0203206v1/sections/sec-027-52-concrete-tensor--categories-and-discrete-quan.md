---
doc_id: arxiv-math-0203206v1
doc_title: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories"
section_id: sec-027-52-concrete-tensor--categories-and-discrete-quan
section_title: "Concrete Tensor ∗-Categories and Discrete Quantum Semigroups"
section_number: 5.2
pages: 28-30
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
doc_brief: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups"
---
From now on, C will be a semisimple strict tensor ∗-category. (As discussed in the Introduction, the strictness
assumption does not entail a loss of generality.) We will introduce oth er requirements as we proceed. By
Theorem 5.8 we have associated a ∗-algebraA to a ∗-preserving functor E : C → H . The aim of this subsection
is to endow A with the structure of a discrete aqg under suitable conditions on C and E. To bring out the
special rˆ ole of the target category H, we work in a more general setting as far as seems justiﬁable.
Let E : C → D be a ∗-preserving tensor functor into some tensor ∗-category D. Recall that by Proposition
5.1, NatE is a unital ∗-algebra for every ∗-preserving functor E : C → D .
Proposition 5.10 Let C, D be tensor ∗-categories, C being strict, and let E : C → D be a ∗-preserving tensor
functor. Then
˜∆ : Nat E → NatE⊗, b = (bX ) ↦→ ˜∆( b) = ( ˜∆( b)Y,Z ), ˜∆( b)Y,Z =bY ⊗Z
deﬁnes a unital ∗-homomorphism.
Proof. The morphisms in C × C are of the form s × t where s : Y → Y ′, t : Z → Z ′. Then s ⊗ t ∈
Mor(Y ⊗Z,Y ′ ⊗Z ′). We compute
(E⊗)(s ×t) ◦ ˜∆( b)Y,Z =E(s ⊗t) ◦ bY ⊗Z =bY ′⊗Z′ ◦ E(s ⊗t) = ˜∆( b)Y ′,Z′ ◦ (E⊗)(s ×t),
28
where we usedb = (bX ) ∈ NatE. We conclude that ˜∆( b) ∈ NatE⊗. That b ↦→˜∆( b) is a unital ∗-homomorphism
follows immediately from Proposition 5.1. ■
We now consider the analogues of (∆ ⊗ι), C being strict, and ( ι ⊗ ∆) in the present general setting. ⊗2 will
denote the functor ⊗ ◦ (⊗ ×Id) = ⊗ ◦ (Id × ⊗) : C × C × C → C , where we have used the strictness of C.
Proposition 5.11 Let C, D be tensor ∗-categories and let E : C → D be a ∗-preserving tensor functor. There
are unital ∗-homomorphisms ~∆ ⊗ι, ~ι ⊗ ∆ : Nat E⊗ → NatE⊗2 deﬁned by
~∆ ⊗ι : Nat E⊗ → NatE⊗2, b = (bX,Y ) ↦→ (~∆ ⊗ι)(b) = (( ~∆ ⊗ι)(b)U,V,W ), (~∆ ⊗ι)(b)U,V,W =bU⊗V,W,
~ι ⊗ ∆ : Nat E⊗ → NatE⊗2, b = (bX,Y ) ↦→ (~ι ⊗ ∆)( b) = (( ~ι ⊗ ∆)( b)U,V,W ), (~ι ⊗ ∆)( b)U,V,W =bU,V ⊗W.
These morphisms satisfy (~∆ ⊗ι) ˜∆ = ( ~ι ⊗ ∆) ˜∆ .
Proof. That ( ~∆ ⊗ι)(b) ∈ NatE⊗2 for b ∈ NatE⊗ follows from the following computation:
(E⊗2)(s ×t ×u) ◦ (~∆ ⊗ι)(b)Y,Z,W =E(s ⊗t ⊗u) ◦ bY ⊗Z,W
=bY ′⊗Z′,W ′ ◦ E(s ⊗t ⊗u) = ( ~∆ ⊗ι)(b)Y ′,Z′,W ′ ◦ (E⊗2)(s ×t ×u),
whenever s :U →U ′,t :V →V ′,u :W →W ′. The argument for ( ~ι ⊗ ∆)( b) is completely analogous. Clearly,
both maps ( ~∆ ⊗ι), (~ι ⊗ ∆) are unital ∗-homomorphisms. The coassociativity property follows from
(~∆ ⊗ι) ˜∆( b)U,V,W = ˜∆( b)U⊗V,W =b(U⊗V )⊗W =bU⊗(V ⊗W ) = ˜∆( b)U,V ⊗W = ( ~∆ ⊗ι) ˜∆( b)U,V,W
with b ∈ EndE, where we have used the strictness of C. ■
Proposition 5.12 There are unital ∗-homomorphisms ˜ε : Nat E → End(E(1)) and ~ε ⊗ι, ~ι ⊗ε : Nat E⊗ →
NatE deﬁned by
˜ε : Nat E → End(E(1)), b = (bX ) ↦→b1,
~ε ⊗ι : Nat E⊗ → NatE, b = (bX,Y ) ↦→ (~ε ⊗ι)(b) = (( ~ε ⊗ι)(b)X ), (~ε ⊗ι)(b)X =b1,X,
~ι ⊗ε : Nat E⊗ → NatE, b = (bX,Y ) ↦→ (~ι ⊗ε)(b) = (( ~ι ⊗ε)(b)X ), (~ι ⊗ε)(b)X =bX,1.
They satisfy (~ε ⊗ι) ˜∆ = ( ~ι ⊗ε) ˜∆ = ι.
Proof. Clearly, the map ˜ε : b = (bX ) ↦→ b1 ∈ EndE(1) is a unital ∗-homomorphism. The proofs that
(~ε ⊗ι)(b), (~ι ⊗ε)(b) are in fact in Nat E and that the maps b ↦→(~ε ⊗ι)(b), b↦→(~ι ⊗ε)(b) are ∗-homomorphisms
proceed along the same lines as for coproducts and are therefore omitted. For b ∈ NatE the computation
(~ε ⊗ι) ˜∆( b) = ˜∆( b)1,X =b1⊗X =bX =bX⊗1 = ˜∆( b)X,1 = ( ~ι ⊗ε) ˜∆( b),
where we used the strictness of the unit 1, concludes the proof. ■
We have thus seen that we can deﬁne a ‘coproduct’ ˜∆ : Nat E → NatE⊗ and a ‘counit’ ˜ε : NatE → EndE(1)
satisfying analogues of the usual properties. A priori, however, N atE⊗ has nothing to do with Nat E ⊗ NatE,
regardless of how we interpret the tensor product. The following r esult indicates how to proceed. We now
assume that C is semisimple. As before, by IC we denote the set of isomorphism classes of irreducible objects
of C. For every i ∈IC we pick a representative Xi.
Definition 5.13 Given a tensor ∗-category C, an embedding functor (for C) is a faithful ∗-preserving tensor
functor E : C → H . A concrete tensor ∗-category is a tensor ∗-category together with an embedding functor.
29
Proposition 5.14 Let C be a semisimple tensor ∗-category and E : C → H an embedding functor. With the
∗-algebraA =⨁
i∈ICB(E(Xi)) we have the following canonical ∗-isomorphisms:
NatE
ψ1
− → M (A) = ∏
i∈ICB(E(Xi)),
NatE⊗
ψ2
− → M (A ⊗A) = ∏
i,j∈ICB(E(Xi)) ⊗B(E(Xj )),
NatE⊗2 ψ3
− → M (A ⊗A ⊗A) = ∏
i,j,k∈ICB(E(Xi)) ⊗B(E(Xj )) ⊗B(E(Xk)).
Proof. The isomorphism ψ1 was established in Propositions 5.4 and 2.10 and suppressed subsequ ently. As to
ψ2, we have
NatE⊗ = ∏
i,j∈IC EndE(Xi ⊗Xj) ∼= ∏
i,j∈IC End (E(Xi) ⊗E(Xj))
= ∏
i,j∈ICB(E(Xi) ⊗E(Xj)) = ∏
i,j∈ICB(E(Xi)) ⊗B(E(Xj)) = M (A ⊗A).
Here we used the identiﬁcation B(H ⊗K) ≡ B(H) ⊗B(K) for ﬁnite dimensional Hilbert spaces and the
identiﬁcations made after Propositions 2.10 and 5.4. The isomorphism between EndE(Xi⊗Xj) and EndE(Xi)⊗
E(Xj ) is induced in the canonical way from the isomorphism dE
Xi,Xj : E(Xi) ⊗E(Xj) → E(Xi ⊗Xj) which
makesE monoidal. Unitarity of the dE
Xi,Xj implies that ψ2 is ∗-preserving. The argument for ψ3 is completely
analogous. ■
Remark 5.15 In the above proof it was crucial that the canonical ∗-homomorphisms ⊗ : End X ⊗C EndY →
End(X ⊗Y ) are ∗-isomorphisms for all X,Y ∈ H . A semisimple tensor ∗-category has this property iﬀ every
object is a ﬁnite direct sum of copies of the tensor unit 1. [ Proof. The ‘if’ clause is easy. As to the ‘only
if’ part, let Z be irreducible and consider X ∼= Y ∼= 1 ⊕Z, thus X ⊗Y ∼= 1 ⊕Z ⊕Z ⊕Z 2. If Z ⁄∼= 1 then
EndX ⊗C EndY ∼= C2 ⊗ C2 is commutative whereas End(X ⊗Y ) is non-commutative since X ⊗Y contains the
irreducible Z with multiplicity at least two. This contradicts End X ⊗C EndY ∼= End(X ⊗Y ).] This property
is known to characterize the (semisimple) tensor ∗-category H uniquely up to equivalence. We thus see that
withE =Id : C → C , we cannot conclude that Nat E⊗ ∼= M (A ⊗A). This is consistent with the computation
of Nat ⊗ in Example 5.6. ✷
From now on we restrict ourselves to the case we are ultimately inter ested in.
Definition 5.16 Let C be a semisimple tensor ∗-category and let E : C → H be an embedding functor. Using
the preceding results we deﬁne unital ∗-homomorphisms as follows.
ε : M (A) → C, a ↦→˜ε ◦ ψ−1
