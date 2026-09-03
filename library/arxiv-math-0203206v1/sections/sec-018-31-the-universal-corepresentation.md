---
doc_id: arxiv-math-0203206v1
doc_title: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories"
section_id: sec-018-31-the-universal-corepresentation
section_title: "The Universal Corepresentation"
section_number: 3.1
pages: 12-14
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
doc_brief: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups"
---
Throughout this section ( A, ∆) stands for an arbitrary aqg and B denotes a ∗-algebra. We recall the universal
corepresentationU of (A, ∆) and discuss its various properties [18].
Definition 3.1 A corepresentation of (A, ∆) onB is an element V ∈M (A ⊗B) such that (∆ ⊗ι)V =V13V23.
Proposition 3.2 SupposeV is a corepresentation of (A, ∆) on B. Then the following are equivalent:
1. V is invertible in M (A ⊗B) with V −1 = (S ⊗ι)V .
2. (ε ⊗ι)V = 1.
3. V (A ⊗B) = A ⊗B = (A ⊗B)V .
A corepresentation V satisfying these equivalent conditions is said to be non-de generate.
Definition 3.3 A unitary corepresentation V of (A, ∆) on B is a corepresentation on B which is a unitary
element of M (A ⊗B).
The following result is fundamental for corepresentations of aqg. We regard elements of A ⊗ ˆA as endomor-
phisms of A.
Theorem 3.4 There exists a unique element U ∈M (A ⊗ ˆA) such that
[U (x ⊗ω)](y) = (ι ⊗ω)(∆(y)(x ⊗ 1))
[(x ⊗ω)U ](y) = (ω ⊗ι)((1 ⊗x)∆( y))
for all x,y ∈A and ω ∈ ˆA. Moreover, we have the following properties for U :
1. U is unitary in M (A ⊗ ˆA).
2. (∆ ⊗ι)U =U13U23.
12
3. (ι ⊗ ˆ∆) U =U12U13.
4. (ω ⊗ι)U =ω for all ω ∈ ˆA.
5. (ι ⊗a)U =a for all a ∈A, where a acts on ˆA by the identiﬁcation A = ˆAˆ.
Note that claims 1 and 2 say that U is a unitary corepresentation of ( A, ∆) on ˆA, whereas claims 1 and 3
say that σ(U ) is a unitary corepresentation of ( ˆA, ˆ∆) on A. Below we will explain why U is called the universal
corepresentation of (A, ∆). It follows that σ(U ) is the universal corepresentation of ( ˆA, ˆ∆).
Let Hom(A,B ) denote the set of ∗-homomorphisms from A to M (B) satisfying θ(A)B =B.
Proposition 3.5 LetV ∈M (A ⊗B) and consider the linear map
πV : ˆA →M (B), ω ↦→(ω ⊗ι)V.
Then the following equivalences hold:
1. V is a corepresentation (of (A, ∆) on B) iﬀ πV is multiplicative.
2. V is a non-degenerate corepresentation iﬀ πV is multiplicative and non-degenerate.
3. V is a unitary corepresentation iﬀ πV ∈ Hom( ˆA,B ).
The universality of U can now be formulated as follows.
Theorem 3.6 For any unitary corepresentation V of (A, ∆) on B and any θ ∈ Hom( ˆA,B ), we have:
1. (ι ⊗πV )U =V .
2. π(ι⊗θ)U =θ.
The result remains valid for the non-degenerate situation without ∗-operation.
Definition 3.7 Let B′ be non-degenerate ∗-algebra. For θ ∈ Hom(A,B ) and θ′ ∈ Hom(A,B ′) we deﬁne
θ ×θ′ ∈ Hom(A,B ⊗B′) by θ ×θ′ = (θ ⊗θ′)∆ . If V and V ′ are unitary corepresentations of (A, ∆) on B and
B′, respectively, we deﬁne a unitary corepresentation V ×V ′ of (A, ∆) on B ⊗B′ by V ×V ′ =V12V ′
13.
Theorem 3.8 The map sending unitary corepresentations V of (A, ∆) onB toπV ∈ Hom( ˆA,B ), is a bijection.
Let V ′ be a unitary corepresentation of (A, ∆) on B′. Then πV ×V ′ = πV ×πV ′ . For the universal corepre-
sentation U of (A, ∆) on ˆA we have πU = ι ∈ Hom( ˆA, ˆA), and ﬁnally for the trivial unitary corepresentation
1 ⊗ 1 ∈A ⊗B(C) of (A, ∆) we have π1⊗1 = ˆε, where ˆε is the counit of ( ˆA, ˆ∆) .
Proof. The only part which is not immediate from the results above, is the iden tityπV ×V ′ =πV ×πV ′ . To show
this, ﬁrst note that
V ×V ′ =V12V ′
13 = [(ι ⊗πV )U ]12[(ι ⊗πV ′)U ]13 = (ι ⊗πV ⊗πV ′)(U12U13)
= (ι ⊗πV ⊗πV ′ )(ι ⊗ ˆ∆) U = (ι ⊗ (πV ⊗πV ′) ˆ∆) U = (ι ⊗πV ×πV ′ )U.
Thus we may conclude that
πV ×V ′(ω) = (ω ⊗ι ⊗ι)(V ×V ′) = (ω ⊗ι ⊗ι)(ι ⊗πV ×πV ′ )U = (πV ×πV ′ )(ω ⊗ι)U = (πV ×πV ′ )(ω),
for all ω ∈ ˆA. ■
13
Remark 3.9 The correspondence established in Theorem 3.8 is in fact a functor if we deﬁne arrows for rep-
resentations and corepresentations on ∗-algebras in the following way. For any objects π ∈ Hom(A,B ) and
π′ ∈ Hom(A,B ′) deﬁne an arrow f :π →π′ to be f ∈ Hom(B,B ′) such that fπ =π′. Similarly, if V and V ′
are unitary corepresentations of ( A, ∆) on B andB′, respectively, we deﬁne an arrow f :V →V ′ between these
objects to be f ∈ Hom(B,B ′) such that V ′ = (ι ⊗f )V . Then the correspondence V ↦→πV in Theorem 3.8 is
an equivalence of tensor categories (they are not ∗-categories). ✷
Remark 3.10 We remark on the tensor categories of actions and coactions of an aqg (A, ∆) on ∗-algebras.
By an action γ of (A, ∆) on a ∗-algebra B, we mean a surjective linear map γ : A ⊗B → B such that
γ(m ⊗ι) = γ(ι ⊗γ). An arrow f :γ →γ′ is an element f ∈ Hom(B,B ′) such that fγ =γ′f . We do not deﬁne
tensor products in the general case.
Givenπ ∈ Hom(A,B ), we deﬁne the action γπ of (A, ∆) on B byγπ(a ⊗b) = π(a)b, for all a ∈A andb ∈B.
Using non-degeneracy of f , we see that for any f ∈ Hom(B,B ′), we have f : π → π′ iﬀ f : γπ → γπ′ . Thus
π ↦→γπ is an equivalence of the tensor category of non-degenerate ∗-representations of (A, ∆) on ∗-algebras to
the tensor category of actions of ( A, ∆) on ∗-algebras contained in the image of the functor and with tensor
product γπ ×γπ′ simply deﬁned to be the action γπ×π′. We have not incorporated the ∗-preserving property of
π in γπ and the axioms for actions.
A coaction δ of (A, ∆) on a ∗-algebra B is a δ ∈ Hom(B,A ⊗B) such that ( ι ⊗δ)δ = (∆ ⊗ι)δ and
(ε ⊗ι)δ = ι. Such coactions form a tensor category, an arrow f : δ → δ′ being an element f ∈ Hom(B,B ′)
such that ( ι ⊗f )δ = δ′f and the tensor product δ ×δ′ being the comodule of ( A, ∆) on B ⊗B′ given by
(δ ×δ′)(b ⊗b′) = δ(b)12δ′(b′)13, for all b ∈B and b′ ∈B′.
Let V be a unitary corepresentation of ( A, ∆) on B. Then the linear map δV : B → M (A ⊗B) given by
δV (b) = V (1 ⊗b)V ∗ for all b ∈ B, is indeed a coaction of ( A, ∆ op) on B. Non-degeneracy of δV follows from
V (A ⊗B) = A ⊗B, and the formula ( ι ⊗δV )δV = (∆ op ⊗ι)δV follows from the calculation
(ι ⊗δV )δV (b) = (ι ⊗δV )V (1 ⊗δV (b))((ι ⊗δV )V )∗ =V23V13V ∗
23(1 ⊗V (1 ⊗b)V ∗)(V23V13V ∗
23)∗
=V23V13(1 ⊗ 1 ⊗b)V ∗
13V ∗
23 = (∆ op ⊗ι)V (1 ⊗ 1 ⊗b)((∆ op ⊗ι)V )∗ = (∆ op ⊗ι)(V (1 ⊗b)V ∗)
= (∆ op ⊗ι)δV (b)
for all b ∈ B. Note that any arrow f : V → V ′ will be an arrow f : δV → δV ′ , but the converse is not
true (consider B′ commutative). So we have a tensor functor V ↦→δV from the tensor category of unitary
corepresentations of (A, ∆) on ∗-algebras to the tensor category of coactions of ( A, ∆ op) on ∗-algebras, which
in general, is not an equivalence. ✷
