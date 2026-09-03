---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-029-72-comparison-of-two-complexes
section_title: "Comparison of two complexes"
section_number: 7.2
pages: 28-28
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
---
categories and functors coming from weak Hopf algebras, the Yet ter complex deﬁned
here is the same as the complex deﬁned in the previous section.
Proposition 7.4. LetA be a weak Hopf algebra, B a weak Hopf subalgebra in A,
C = Rep(A), C′ = Rep(B), and F : C → C ′ be the restriction functor. Then the
complexC•
F (C) coincides with the complex C•(A,B ) deﬁned in Section 6.
Proof. Let us show that End( Tn ◦F ⊗n) = Cn(A,B ). For this, deﬁne a map ξ :
Cn(A,B ) → End(Tn). Recall that for any representations X1,...,X n of A, the
representation X1 ⊗C... ⊗CXn is deﬁned to be the image of the projection ∆ n(1)
acting on X1 ⊗... ⊗Xn [NTV]. Therefore, any element a ∈ Cn(A,B ) deﬁnes an
operator on the usual tensor product X1 ⊗... ⊗Xn which preserves the subspace
X1 ⊗C ... ⊗C Xn (since a = Ad(1)a). Let us denote by ξ(a) its restriction to this
subspace. Since a is invariant under the adjoint action, we ﬁnd that ξ(a) is not
only a linear map but also a morphism of representations. So we have d eﬁned the
map ξ.
Now we need to show that the map ξ is an isomorphism. For this purpose, we
construct the inverse map. Take f ∈ End(Tn ◦F ⊗n). Extend it by zero to the
space Ker∆ n(1) in X1 ⊗... ⊗Xn. Then we get a linear operator ˜f onX1 ⊗... ⊗Xn,
which is functorial in X1,...,X n. Thus, ˜f corresponds to a unique element ˆf of
A⊗n. It is clear that ˆf = Ad(1) ˆf , since both sides deﬁne the same operators in
X1 ⊗... ⊗Xn. It is also clear that ˆf is invariant under adjoint action, as f is a
morphism in the category. Finally, it is clear that ξ( ˆf ) = f , and ˆξ(a) = a. Thus, ξ
is an isomorphism.
Finally, it is easy to see that the map ξ identiﬁes the diﬀerentials of the two
complexes. The proposition is proved. □
