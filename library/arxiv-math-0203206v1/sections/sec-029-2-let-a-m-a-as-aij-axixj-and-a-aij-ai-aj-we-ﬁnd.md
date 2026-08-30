---
doc_id: arxiv-math-0203206v1
doc_title: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories"
section_id: sec-029-2-let-a-m-a-as-aij-axixj-and-a-aij-ai-aj-we-ﬁnd
section_title: "Let a ∈M (A). As ∆( a)ij =aXi⊗Xj and (a ⊗a)ij =ai ⊗aj we ﬁnd"
section_number: 2
pages: 30-32
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
doc_brief: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups"
---
∆( a) = a ⊗a ⇔ aXi⊗Xj =aXi ⊗aXj ∀i,j ∈I.
Thus the grouplike elements of M (A) are in one-to-one correspondence with those natural transfo rmations of
the embedding functor which respect the tensor structure. ✷
30
Lemma 5.18 The restriction ∆ = ∆ ↾ A is a non-degenerate ∗-homomorphism from A to M (A ⊗A), i.e.
∆( A)(A ⊗A) = (A ⊗A)∆( A) = (A ⊗A).
Proof. To simplify the notation we write Hi = B(E(Xi)) and use the isomorphisms ψ1,ψ 2 to identify M (A)
with Nat E and M (A ⊗A) with Nat E⊗. We will only prove ∆( A)(A ⊗A) = (A ⊗A), the proof of the other
identity being completely analogous. As A = ⊕iB(Hi), it suﬃces to show that for every i,j ∈ IC there is a
c ∈ A with ∆( c)(Ii ⊗Ij) = Ii ⊗Ij , since this implies ai ⊗bj = ∆( c)(Ii ⊗Ij)(ai ⊗bj) ∈ ∆( A)(A ⊗A) for
all ai ∈ B(Hi),bj ∈ B(Hj ). Recall from the Propositions 5.14 and 5.4 that M (A) is isomorphic to the ∗-
algebra of natural transformations of E, and these are uniquely determined by their actions on the irreducib les:
M (A) ∋b ↔ (bi), where bi ≡bXi. Similarly, M (A ⊗A) ∋b ↔ (bij) with bij ≡bXi,Xj . By the deﬁnition of ˜∆
we have ˜∆( b)ij =bXi⊗Xj . As usual, let ( vkα
ij ,α = 1,... ,N k
ij) be an orthonormal basis in Mor( Xk,Xi ⊗Xj) for
all i,j,k ∈IC. Since b ∈M (A) ≡ EndE is a natural transformation we have
˜∆( b)ij =bXi⊗Xj =bXi⊗Xj ◦ idE(Xi⊗Xj ) =bXi⊗Xj ◦ E
( ∑
kα
vkα
ij ◦ vkα∗
ij
)
=
∑
kα
E(vkα
ij ) ◦ bk ◦ E(vkα∗
ij ).
Now ﬁx i0,j 0 ∈ IC and let bk = id E(Xk) if Xk is contained in Xi0 ⊗ Xj0 and bk = 0 otherwise. Since
Xk ≺Xi0 ⊗Xj0 only for ﬁnitely many k we have b = (bk) ∈A and
˜∆( b)i0j0 =
∑
kα
E(vkα
i0j0 ) ◦ idE(Xk) ◦ E(vkα∗
i0j0 ) =
∑
kα
E(vkα
i0j0 ◦ vkα∗
i0j0 ) = E(idXi0 ⊗Xj0 ) = idE(Xi0 ⊗Xj0 ).
Having identiﬁed Nat E⊗ ≡ M (A ⊗A) this precisely means that the ( i0,j 0)-component of ∆( b) ∈M (A ⊗A) =∏
ijB(Hi) ⊗B(Hj) is the identity Ii0 ⊗Ij0 and therefore ∆( b)(Ii0 ⊗Ij0 ) = (Ii0 ⊗Ij0 ) as desired. ■
Corollary 5.19 Deﬁning ∗-homomorphisms ε :A → C and ∆ : A →M (A ⊗A) by ε =ε ↾A and ∆ = ∆ ↾A,
ε and ∆ are the unique extensions of ε and ∆ , respectively, to M (A).
Proof. It is clear that ε is not identically zero, thus non-degenerate. Non-degeneracy of ∆ has been proven in
Lemma 5.18. Now the claim follows from the fact [35] that a non-degen erate ∗-homomorphism φ :A →M (B)
has a unique extension to a unital ∗-homomorphism φ :M (A) →M (B). ■
Proposition 5.20 Let C be a semisimple tensor ∗-category and E : C → H an embedding functor. Then the
∗-algebra A = ⊕i∈ICB(E(Xi)) is a discrete quantum semigroup, i.e. has a non-degenerate c oproduct ∆ : A →
M (A ⊗A) in the sense of [35] and a counit ε :A → C.
Proof. By Lemma 5.18, ∆ is non-degenerate, thus also ∆ ⊗ι : A ⊗A → M (A ⊗A) ⊗A ⊂ M (A ⊗A ⊗A) is
non-degenerate and extends uniquely to ∆ ⊗ι :M (A ⊗A) →M (A ⊗A ⊗A). Another unital ∗-homomorphism
M (A ⊗A) →M (A ⊗A ⊗A) is given by ψ3 ◦ (~∆ ⊗ι) ◦ψ−1
2 . The latter clearly restricts to ∆ ⊗ι onA ⊗A, thus it
coincides with ∆ ⊗ι on all of M (A ⊗A). In the same way we make sense of ι ⊗ ∆ : M (A ⊗A) →M (A ⊗A ⊗A)
and see that it coincides with ψ3 ◦ (~ι ⊗ ∆) ◦ψ−1
2 . Now, the coassociativity property proved in Proposition 5.11
implies
∆ ⊗ι ◦ ∆ = ι ⊗ ∆ ◦ ∆ : M (A) →M (A ⊗A ⊗A),
which is the proper formulation of coassociativity for ( A, ∆).
As observed earlier, the ∗-homomorphism ε : A → C is non-degenerate, thus ε ⊗ι, ι⊗ε : A ⊗A → A
are non-degenerate too and have unique extensions ε ⊗ι, ι ⊗ε to M (A ⊗A). Again, it is clear that ε ⊗ι =
ψ1 ◦ (~ε ⊗ι) ◦ ψ−1
2 and similarly for ι ⊗ε. Thus with Proposition 5.12 we conclude
ε ⊗ι ◦ ∆ = ι ⊗ε ◦ ∆ = id : M (A) →M (A).
We conclude that ( A, ∆) is a discrete quantum semigroup. ■
31
Theorem 5.21 Let C be a semisimple tensor ∗-category and E : C → H an embedding functor. Let (A, ∆) be
the corresponding discrete quantum semigroup. Then the fun ctor F : C → Repf (A, ∆) deﬁned by
F (X) = (E(X),πX ), π X (a) = aX ∀a ∈A, F (s) = E(s)
provides an equivalence of tensor ∗-categories such that K ◦ F =E.
Proof. WithA andF : C → RepfA as deﬁned in Theorem 5.8 we have an equivalence of categories. It re mains to
show thatF : C → Repf (A, ∆) is monoidal for the monoidal structure of Rep f (A, ∆) in Deﬁnition 3.12. Thus we
must exhibit isomorphisms dF
X,Y :F (X) ⊗F (Y ) →F (X ⊗Y ) satisfying the conditions of Deﬁnition 2.1. In view
ofF (X) = (E(X),πX ), an obvious candidate is the isomorphism dE
X,Y :E(X)⊗E(Y ) →E(X⊗Y ) which we have
by virtue of the assumed monoidality of E. If we set dF
X,Y =dE
X,Y for all X,Y ∈ C , the equations in Deﬁnition
2.1 are clearly satisﬁed. It only remains to prove that dF
X,Y is in Mor Repf (A,∆) (F (X) ⊗F (Y ),F (X ⊗Y )), i.e.
dF
X,Y ◦ (πX ×πY )(a) = πX⊗Y (a) ◦ dF
X,Y ∀a ∈A.
Keeping in mind the various identiﬁcations we have made so far, we get
dF
X,Y ◦ (πX ×πY )(a) = dF
X,Y ◦ (πX ⊗πY )∆( a) = dF
X,Y ◦ (πX ⊗πY )∆( a)
=dF
X,Y ◦ (πX ⊗πY )ψ2 ˜∆( a) = πX,Y ˜∆( a) ◦ dF
X,Y =aX⊗Y ◦ dF
X,Y =πX⊗Y (a) ◦ dF
X,Y
for all a ∈A. (The reader is invited to check the required identity explicitly for X =Xi,Y =Xj, as suﬃces by
naturality of the isomorphisms dF .) ■
