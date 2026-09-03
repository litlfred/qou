---
doc_id: arxiv-math-0203206v1
doc_title: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories"
section_id: sec-020-32-representations-vs-corepresentations-as-tenso
section_title: "Representations vs. Corepresentations as Tensor ∗-Categories"
section_number: 3.2
pages: 14-17
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
doc_brief: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups"
---
We now proceed to establish the correspondence between repres entations of an aqg (A, ∆) and corepresentations
of ( ˆA, ˆ∆), restricting ourselves to ﬁnite dimensional Hilbert spaces. For h omomorphisms π :A → EndK there
are two diﬀerent notions of non-degeneracy which, fortunately, are equivalent for K ﬁnite dimensional.
Lemma 3.11 LetA be an algebra and K a ﬁnite dimensional vector space. For a homomorphism π :A → EndK
the conditions π(A)EndK = EndK and π(A)K =K are equivalent.
Proof. ForK ﬁnite dimensional we clearly have (End K)K =K. Assuming π(A)EndK = EndK we compute
π(A)K =π(A)((EndK)K) = (π(A)EndK)K = (EndK)K =K.
Conversely, assume π(A)K = K. With the isomorphism α : K ⊗K ∗ → EndK determined by α(x ⊗φ)(z) =
xφ(z) for x,z ∈K,φ ∈K ∗ we have (sα(x ⊗φ))(z) = sxφ(z) = α(sx ⊗φ)(z) and therefore
π(A)EndK =π(A)α(K ⊗K ∗) = α((π(A)K) ⊗K ∗) = α(K ⊗K ∗) = End K,
as desired. ■
14
Definition 3.12 Let (A, ∆) be an aqg. Let Repf (A, ∆) denote the class of (algebraically) non-degenerate
∗-representations of A on ﬁnite dimensional Hilbert spaces including the zero repr esentation 0. Let π1,π 2 ∈
Repf (A, ∆) . Then πi ∈ Hom(A,B (Ki)), so we deﬁne π1 ×π2 ∈ Hom(A,B (K1) ⊗B(K2)) = Hom(A,B (K1 ⊗
K2)) ⊂ Repf (A, ∆) according to Deﬁnition 3.7.
We regard Rep f (A, ∆) as a tensor ∗-category with representations as objects and intertwiners as a rrows.
(Recall that a zero representation 0 is not regarded as an irreduc ible object.) The tensor product is the one
given in the deﬁnition above. Clearly, Rep f (A, ∆) is a tensor ∗-category with the counit ε as the irreducible
unit. Of course, the ∗-operation in the category is the usual Hilbert space adjoint of ope rators.
Definition 3.13 We say V is a ﬁnite dimensional unitary corepresentation of an aqg (A, ∆) on a Hilbert space
K if K is ﬁnite dimensional and V is a unitary corepresentation of (A, ∆) on the unital ∗-algebra B(K) of
linear operators on K. Let Corepf (A, ∆) denote the class of all such unitary corepresentations incl uding the
zero corepresentation 0. Let V,V ′ ∈ Corepf (A, ∆) . Then we deﬁne the unitary corepresentation V ×V ′ of
(A, ∆) on B(K) ⊗B(K ′) = B(K ⊗K ′) according to Deﬁnition 3.7. Clearly, we have V ×V ′ ∈ Corepf (A, ∆) .
We regard Corepf (A, ∆) as a tensor ∗-category with corepresentations as objects and intertwiners a s arrows.
Recall that T ∈B(K,K ′) is an intertwiner between two corepresentations V,V ′ ∈ Corepf (A, ∆) iﬀ T (ω ⊗ι)V =
(ω ⊗ι)V ′T , for all ω ∈ ˆA. The tensor product is the one given in the deﬁnition above. Clearly, Corepf (A, ∆)
is a tensor ∗-category with the unit 1 ⊗ 1 as the irreducible unit. Again, the ∗-operation in the category is the
usual Hilbert space adjoint of operators.
The two tensor categories are related in the following way.
Theorem 3.14 Let notation be as above. The correspondence
P : Corep f (A, ∆) → Repf ( ˆA, ˆ∆) , V ↦→πV
provided by Proposition 3.5 together with the identity map o n morphisms gives rise to an isomorphism of tensor
∗-categories.
Proof. The proof is immediate from Theorem 3.8. ■
Remark 3.15 A similar result can be obtained for the inﬁnite dimensional case. One n eeds then to talk about
∗-representations which are non-degenerate in the C∗-algebra sense, so π ∈ Rep(A, ∆) iﬀ the exists a (possibly
inﬁnite dimensional) Hilbert space K and a ∗-homomorphismπ :A →B(K) such that the vector space π(A)K
is dense in K. The tensor ∗-category Corep(Ar, ∆ r) of unitary corepresentations on Hilbert spaces consists of
Hilbert spaces K and unitariesV ∈M (Ar ⊗B0(K)) such that (∆ r ⊗ι)V =V13V23. For the exact correspondence
thus established, see [5].
We will look at another way of obtaining a tensor ∗-category Rep f (Ao
s, ˆ∆) from a compact aqg ( A, ∆)
which is equivalent to Corep f (A, ∆). This can sometimes come in very handy, especially when dealing with
representations of quantized universal enveloping Lie algebras Uq(g).
First recall that (A, ∆) is a Hopf ∗-algebra with counit ε, coinverseS and unit I, so the vector space A′ of all
linear functionals on A is a unital ∗-algebra with unit ε, product ωη = (ω ⊗η)∆ ∈A′ and ∗-operation ω∗ ∈A′
given by ω∗(a) =
ω(S(a)∗), for all a ∈A. Deﬁne a linear map ˆ∆ : A′ → (A ⊗A)′ by ˆ∆( ω)(a ⊗b) = ω(ab), for
all ω ∈A′ and a,b ∈A. Consider the subspace Ao of A′ given by
Ao = {ω ∈A′ | ˆ∆( ω) ∈A′ ⊗A′},
where we understand the embedding A′ ⊗A′ ⊂ (A⊗A)′. Then (Ao, ˆ∆) is called the maximal dual Hopf ∗-algebra
of (A, ∆). Note that for ˆf ∈ M ( ˆA) as in Theorem 2.12, we have ˆf ∈ Ao and ˆ∆( ˆf ) = ˆf ⊗ ˆf . Regard Ao as
a locally convex topological vector space with pointwise convergenc e, so ωλ → ω in Ao if ωλ(a) → ω(a), for
all a ∈A. The continuous unital ∗-representations of (Ao, ˆ∆) on ﬁnite dimensional Hilbert spaces clearly form
a tensor ∗-category with conjugates given by the same formulas as for Rep f ( ˆA, ˆ∆). Note that in general, the
maximal dual Hopf ∗-algebra can be very small!
15
Theorem 3.16 Let (A, ∆) be a compact aqg and let (Ao
s, ˆ∆) be a sub Hopf ∗-algebra of the maximal dual Hopf
∗-algebra of (A, ∆) which separates the elements of A. (Thus Ao
s is a unital ∗-subalgebra of Ao and ˆ∆ is given
by restriction). Consider the tensor ∗-category Repf (Ao
s, ˆ∆) of continuous unital ∗-representations of (Ao
s, ˆ∆)
on ﬁnite dimensional Hilbert spaces with arrows, ∗-operation and tensor product deﬁned in the obvious way.
Then the assignment
N : Corep f (A, ∆) → Repf (Ao
s, ˆ∆) , V ↦→πV with πV (ω) = (ω ⊗ι)V, ∀ω ∈Ao
s,
together with the identity map on arrows, is an equivalence o f tensor ∗-categories.
Proof. The only part which requires a proof is that any π ∈ Repf (Ao
s, ˆ∆) is of the form πVπ for some Vπ ∈
Corepf (A, ∆). Thus let π :Ao
s →B(K) be a continuous unital ∗-representation of Ao
s on a ﬁnite dimensional
Hilbert space K. We will provide a Vπ ∈A ⊗B(K) such that πVπ = π. Using the fact that Ao
s separates the
elements of A, it is then clear that Vπ will be unitary, that (∆ ⊗ι)Vπ = (Vπ)13(Vπ)23 and that the ∗-preserving
tensor functor N is an equivalence.
Now pick an orthonormal basis ( ei) for K and consider the system mij of matrix units for B(K) deﬁned as
mij(ek) = δjkei, for all i,j,k . Consider, for ﬁxed i andj, the linear functional on Ao
s given by ω ↦→(π(ω)ej,ei)
for all ω ∈ Ao
s. Since π is continuous w.r.t pointwise topology on Ao
s, it follows from [27, Proposition 2.4.4],
that there exists a unique aij ∈A such that ω(aij) = (π(ω)ej,ei), for all ω ∈Ao
s. Deﬁne now Vπ ∈A ⊗B(K)
byVπ =∑
ijaij ⊗mij. By construction πVπ =π and we are done. ■
Remark 3.17 It is known that for the usual quantized compact aqg ( Aq, ∆), the associated quantized universal
enveloping Lie algebras Uq(g) are Hopf ∗-algebras with Ao
s =Uq(g) which separate the elements of Aq [17, Sect.
7.1.5]. Thus the tensor ∗-category of continuous unital ∗-representations of ( Uq(g), ˆ∆) on ﬁnite dimensional
Hilbert spaces is equivalent to Corep f (Aq, ∆). Also ˆf ∈ Uq(g), so the intrinsic dimension can be read oﬀ
conveniently for such representations [30]. We return to this issue in the next subsection. ✷
We now recast our results in the language of modules and comodules.
Proposition 3.18 Any non-degenerate ∗-representation π of a discrete aqg (A, ∆) on a ﬁnite dimensional
Hilbert spaceK gives rise to an A-moduleK. Namely, deﬁne a linear map απ :A⊗K →K byαπ(a⊗ξ) = π(a)ξ,
for all a ∈A and ξ ∈K. Then the following properties hold:
1. απ(m ⊗ι) = απ(ι ⊗απ).
2. απ(A ⊗K) = K.
3. (απ(a∗ ⊗ξ),η ) = (ξ,απ(a ⊗η)) ∀a ∈A ∀ξ,η ∈K.
Denote by Modf (A, ∆) the tensor ∗-category of linear maps α :A ⊗K →K satisfying properties 1-3 above, with
arrows t :α →α′ being linear maps t :K →K ′ satisfying α′ =tα and tensor product α ×α′ :A ⊗K ⊗K ′ →
K ⊗K ′ uniquely determined by
(α ×α′)(ι ⊗α ⊗α)(a ⊗b ⊗ξ ⊗c ⊗ξ′) =
∑
k
α(ak ⊗ξ) ⊗α′(bk ⊗ξ′),
for all a,b ∈ A, ξ ∈ K and ξ′ ∈ K ′ and where ∑
kak ⊗bk = ∆( a)(b ⊗c). Then the assignment π ↦→απ is a
monoidal ∗-preserving equivalence of Repf (A, ∆) and Modf (A, ∆) .
Proof. Straightforward, once one shows that α ×α′ is well-deﬁned. This is most easily done by considering the
corresponding well-deﬁned tensor product π ×π′ of the associated non-degenerate ∗-representations, i.e, of π
and π′ such that α =απ and α′ =απ′ , and then noting that α ×α′ =απ×π′ . ■
16
Proposition 3.19 Any unitary corepresentation V of a compact aqg (A, ∆) on a ﬁnite dimensional Hilbert
spaceK gives rise to an A-comoduleK. Namely, deﬁne a linear map βV :K →A ⊗K byβV (ξ) =∑
kak ⊗xkξ,
for all ξ ∈K and where V =∑
kak ⊗xk ∈A ⊗B(K). Then the following properties hold:
1. (∆ op ⊗ι)βV = (ι ⊗βV )βV .
