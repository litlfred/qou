---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-011-12-the-categories-reph-a-and-rep-a
section_title: "The categories Reph(A) and Rep+(A)"
section_number: 12
pages: 91-96
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
---
12. The categories Reph(A) and Rep+(A)
Let A be a complex ∗-algebra. In this section we associate with A the linear ∗-category
Reph(A) with objects representations on non-degenerate Hermitian spaces.
If A has further the structure of an Ω-involutive weak quasi-Hopf algebra, then we
introduce in Reph(A) the structure of a rigid tensor ∗-category.

92 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Most importantly, the subclass of unitary weak quasi-Hopf algebras leads to rigid tensor
C
∗
-categories Rep+(A).
The basic notion is that of Hermitian space, that is a finite dimensional vector space V
equipped with a non degenerate Hermitian form (ξ, η). If W is another such space, any
linear map T : V → W admits an adjoint T
∗
: W → V defined as in the more familiar case
of Hilbert spaces: (T ξ, η) = (ξ, T ∗η). The category Herm with objects finite dimensional
Hermitian spaces and morphisms linear maps between them is the simplest example of a
∗
-category.
Definition 12.1. Let A be a unital complex ∗-algebra (a discrete complex ∗-algebra resp.)
with involution ∗: A → A.
a) A ∗–representation is a unital (nondegenerate resp.) representation ρ of A on a
nondegenerate Hermitian space Vρ satisfying ρ(a
∗
) = ρ(a)
∗
for a ∈ A.
b) A C
∗
-representation of A is a ∗-representation on a Hilbert space.
The study of ∗-representations on Hermitian spaces is motivated by Uq(g), for |q| = 1
[185]. In this case, Wenzl showed that for generic values of q, or for certain roots of unity
of sufficiently high order there is a finite set of irreducible C
∗
-representations [185]. In the
latter case representation theory is not semisimple. A brief review and connections with
the theory of representations of weak quasi-Hopf algebras will be studied in later sections.
Proposition 12.2. Let A be a complex ∗-algebra either unital or a discrete. Let Reph(A) be
the category with objects nondegenerate ∗–representations of A on nondegenerate Hermitian
spaces. If T ∈ (ρ, σ) is a morphism of Reph(A), the adjoint map T
∗
: Vσ → Vρ is still a
morphism of Reph(A). In this way Reph(A) becomes a linear ∗-category.
An isometric morphism S ∈ (ρ, σ) between two ∗-representations is a morphism satisfying S
∗S = 1. Similarly, a unitary is an invertible isometry, that is a morphism U ∈ (ρ, σ)
satisfying U
∗U = 1, UU∗ = 1. Therefore there is a natural notion of unitary equivalence
between ∗–representations ρ and σ. Unitary equivalence implies equivalence, but, unlike
the case of Hilbert space ∗–representations, the converse does not hold. In other words, a
representation can be made into a ∗-representation in more than one way, up to unitary
equivalence. This can be seen with the following simple construction.
Given a ∗-representation ρ, let ρ− denote the ∗-representation with the same space and
action as ρ but with with the opposite Hermitian form: (ξ, η)Vρ−= −(ξ, η)Vρ. We shall refer
to ρ− as the opposite ∗-representation. Note that ρ and ρ− are equivalent as representations
but they are not unitarily equivalent in the following two cases, either ρ is irreducible, or
it may reduce but it is a C
∗
-representation. Indeed, given another ∗-representation σ and
a linear map T : Vρ → Vσ with adjoint T
∗ with respect to the original forms, the adjoint of
T as a map Vρ− → Vσ or Vρ → Vσ− is −T
∗
. Thus the unitarity condition for an intertwiner
T : Vρ → Vρ− becomes T
∗T = −I, with T∗
the adjoint of T as a map Vρ → Vρ, and this is
incompatible with either irreducibility (T acts as a scalar) or the C
∗
-assumption on ρ.
A ∗-representation σ is called an orthogonal direct sum of ρ and τ if there are isometries
S ∈ (ρ, σ), T ∈ (τ, σ) such that SS∗ + T T∗ = 1. This implies that SVρ and T Vτ are

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 93
spanning, orthogonal subspaces of Vσ: (SVρ, T Vτ ) = 0, and hence are complementary
by nondegeneracy of the form. We write σ = ρ ⊕ τ and refer to ρ and τ as orthogonal
summands of σ. If ρ and τ are ∗–representations, the direct sum Hermitian form on Vρ⊕Vτ
makes this space into a ∗-representation σ in the natural way and we have σ = ρ ⊕ τ via
the inclusions S : Vρ → Vσ, T : Vτ → Vσ. Any other realisation of σ as a direct sum of ρ
and σ will be unitarily equivalent to this.
If A is not semisimple as an algebra, representations may admit invariant submodules
which are not summands. The following proposition shows that the ∗–structure is useful
to distinguish between summands and submodules.
Proposition 12.3. Let A be a complex ∗-algebra either unital or a discrete. If S ∈ (ρ, σ)
is an isometry in Reph(A), then E = SS∗is a selfadjoint idempotent with range SVρ,
defining an orthogonal summand of σ. Conversely, every submodule W of Vσ (i.e. a
subspace of Vσ invariant under all the σ(a), a ∈ A) for which the restricted Hermitian
form is nondegenerate, is a ∗–representation and an orthogonal summand.
Proof. In general, if the restriction of the Hermitian form of Vσ is nondegenerate on a
submodule W then the adjoint of the restriction of an element σ(a) with respect to the
restricted form equals the restriction of σ(a
∗
) by ∗-invariance of σ and nondegeneracy.
Hence W defines a ∗-representation and the inclusion map S : W → Vσ is an isometry.
Given an isometry S ∈ (ρ, σ) in Reph(A), E = SS∗ obviously defines an algebraic
summand of σ. The ranges of E and 1 − E are orthogonal subspaces of Vσ. This implies
that the Hermitian form of Vσ is nondegenerate on either subspace and therefore these are
∗–representations ρ and τ such that σ = ρ ⊕ τ .
□
We next give a criterion for nondegeneracy of Hermitian forms.
Proposition 12.4. Let A be a complex ∗-algebra either unital or a discrete. A nonzero
Hermitian form on the vector space of an irreducible representation ρ of A making it
∗
-invariant is nondegenerate. Any other ∗-representation structure on ρ is unitarily equivalent to ρ or ρ−.
Proof. The subspace V
⊥
ρ = {v ∈ Vρ,(v, Vρ) = 0} is a submodule by ∗
-invariance of ρ, and
it must be proper, hence V
⊥
ρ = 0 by irreducibility, and this shows nondegeneracy. Every
other nondegenerate Hermitian form on Vρ is defined by an invertible map B : Vρ → Vρ
via (ξ, η)B = (ξ, Bη), with B selfadjoint with respect to the given Hermitian form. The
adjoint of a map T : Vρ → Vρ with respect to the new form as compared to the old
changes to B−1T
∗B. The ∗
-invariance condition for ρ with respect to the new form reads
as B−1ρ(a
∗
)B = ρ(a
∗
) for a ∈ A by ∗-invariance of ρ. Thus B is a nonzero real scalar.
□
A tensor product of Hermitian spaces becomes an Hermitian space in the natural way:
(ξ ⊗ ξ
′
, η ⊗ η
′
)p := (ξ, η)(ξ
′
, η′). In this way Herm becomes a tensor ∗-category, and it is
the unique ∗-structure on Herm compatible with the tensor structure.

94 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
We next describe how to obtain a tensor ∗-category from an Ω-involutive weak quasibialgebra. Note that the ∗
-structure obtained restricting that of Herm to Reph(A) is
not the correct one, as it does not make a tensor product of two ∗–representations into
a
∗
-representation. This is due to the fact that the coproduct and ∗-involution do not
commute. On the other hand, because of the twisted commutation relation they satisfy,
one can consider a twist of the product form by the action of Ω,
(ζ, ζ′)Ω := (ζ, Ωζ
′
)p, ζ, ζ′ ∈ Vρ⊗ρ
′
,
which is indeed a non degenerate and Hermitian form.
Theorem 12.5. Let A be an Ω-involutive weak quasi bialgebra. For every pair of ∗–
representations ρ, ρ
′
, the form (·, ·)Ω on Vρ⊗V
′
ρ makes ρ⊗ρ
′
into a ∗–representation. In
this way Reph(A) becomes a tensor ∗–category with unitary associativity morphisms. This
category is strict if A is a bialgebra.
Proof. Let V be a Hermitian space, and consider a new Hermitian form of V defined by a
given selfadjoint invertible A ∈ L(V ). Denote by VA the associated Hermitian space. Let
W, B, be another such pair. Given T ∈ L(V, W), we denote by T
∗ and T†
the adjoint of
T with respect to the new forms (that is as a map T : VA → WB) and the original form
respectively. They are related by T
∗ = A−1T†B. Therefore given T ∈ L(Vρ⊗Vρ
′, Vσ⊗Vσ′),
we have T
∗ = Ω−1T†Ω with adjoints referred to the twisted form and the restricted product
form respectively. Thus T
∗ = T†
if T
†
commutes with the action of Ω. For example, this
always holds for T = S⊗S
′
, with S ∈ (ρ, σ), S
′ ∈ (ρ′
, σ′). Indeed, T
† = S∗⊗S′∗, and S∗
and S
′∗ are intertwiners. We at once find (S⊗S
′
)
∗ = S∗⊗S′∗. Notice that the product
form is related to the involution of the tensor product ∗–algebra A ⊗ A:
ρ ⊗ ρ
′
(b
∗
) = ρ ⊗ ρ
′
(b)
†
, b ∈ A ⊗ A.
Therefore for a ∈ A,
ρ⊗ρ
′
(a)
∗ = ρ ⊗ ρ′
(∆(a))∗ =
ρ⊗ρ
′
(Ω−1)ρ ⊗ ρ
′
(∆(a))†ρ⊗ρ
′
(Ω) = ρ ⊗ ρ
′
(Ω−1∆(a)
∗Ω) =
ρ ⊗ ρ
′
(∆(a
∗
)) = ρ⊗ρ
′
(a
∗
).
Given ∗-representations ρ, σ, τ , the ∗–representations (ρ⊗σ)⊗τ and ρ⊗(σ⊗τ ) act via the
morphisms ∆⊗1◦∆ and 1⊗∆◦∆, respectively, on the subspaces of Vρ⊗ Vσ⊗Vτ determined
by the image of I under those morphisms. With respect to the triple product form, the
associated Hermitian forms are induced by Ω⊗I∆⊗1(Ω) and I ⊗Ω1⊗∆(Ω), respectively.
To show that the associativity morphisms αρ,σ,τ are unitary arrows of Reph(A), we compute
their adjoints taking into account the remark at the beginning of the proof,
α
∗
ρ,σ,τ = (Ω ⊗ I∆ ⊗ 1(Ω))−1α
†
ρ,σ,τ I ⊗ Ω1 ⊗ ∆(Ω) =
ρ ⊗ σ ⊗ τ (∆ ⊗ 1(Ω−1)Ω−1 ⊗ IΦ
∗
I ⊗ Ω1 ⊗ ∆(Ω)) = ρ ⊗ σ ⊗ τ (Φ−1) =
α
−1
ρ,σ,τ .
If in addition A is a bialgebra then Φ is the trivial associator, hence Ω is a 2-cocycle by
Prop. 11.4. This means that (ρ⊗σ)⊗τ and ρ⊗(σ⊗τ ) also coincide as ∗–representations.
Since the associativity morphisms are trivial, Reph(A) is strict.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 95
□
Corollary 12.6. Suppose that A is a unitary weak quasi bialgebra A. Then the full subcategory Rep+
(A) of Reph(A) with objects C
∗
-representations is a tensor C
∗
-category.
Proof. The Ω-twisted inner product of a tensor product of two C
∗
-representations is still
a positive inner product by positivity of Ω.
□
Proposition 12.7. Let A be an Ω-involutive weak quasi bialgebra. The forgetful functor
F : Reph(A) → Herm (or F : Rep+(A) → Hilb in the C
∗
-case) is a ∗-functor. The natural
transformations satisfy
F
∗
ρ,σ = ρ ⊗ σ(Ω) ◦ Gρ,σ, G∗ρ,σ = Fρ,σ ◦ ρ ⊗ σ(Ω−1
). (12.1)
Proof. ∗-invariance of F is clear. Relations (12.1) follow from computations as in the proof
of Theorem 12.5. □
We observe that thanks to Gρ,σ ◦Fρ,σ = ρ⊗σ(∆(I)), relations (12.1) can also be written
in the form
F
∗
ρ,σ
◦ Fρ,σ = ρ ⊗ σ(Ω), Gρ,σ ◦ G
∗
ρ,σ = ρ ⊗ σ(Ω−1
). (12.2)
Proposition 12.8. Let A be an Ω-involutive weak quasi-bialgebra with involution (
∗
, Ω)
and F ∈ A ⊗ A a twist. Consider the twisted algebra AF with involution (
∗
, ΩF ) as in
Prop. 11.8. Then the tensor equivalence E defined in Prop. 7.2 restricts to a unitary
tensor equivalence between Reph(A) → Reph(AF ) (Rep+(A) → Rep+(AF ) in the unitary
case).
Proof. The two algebras have the same ∗-involution, hence the equivalence is a ∗-functor.
We show unitarity of the associated natural transformation, which is given by the action
of Eρ,σ = ρ ⊗ σ(F
−1
) from E(ρ) ⊗ E(σ) to E(ρ ⊗ σ). We have E
∗
ρ,σ = Ω−1
F
ρ ⊗ σ(F
−1∗
)Ω =
ρ ⊗ σ(FΩ
−1F∗F−1∗Ω) = ρ ⊗ σ(F) = E
−1
ρ,σ.
□
We next note that while at the algebraic level, the element Ω defining a unitary involution
of a weak quasi-Hopf C
∗
-algebra may be non-unique, passing to another such operator gives
rise to a unitarily equivalent tensor C
∗
-category.
Proposition 12.9. Let A be a weak quasi-bialgebra endowed with the structure of a C
∗
-
algebra (or a discrete weak quasi-bialgebra with positive involution). Let Ω and Ω
′ define
two unitary Ω-involutive structures. Let us upgrade the category of C
∗
-representations
of A to corresponding tensor C
∗
-categories Rep+
Ω
(A) and Rep+
Ω′(A). Then the functor
F : Rep+
Ω
(A) → Rep+
Ω′(A) acting as identity on objects and morphisms admits the structure
of a unitary tensor equivalence.
Proof. It is easy to check that the functor F becomes a tensor ∗-equivalence with the
natural transformations F(ρ)⊗F(σ) → F(ρ⊗σ) acting as identity. The unitary part of the
polar decomposition equips F with the structure of a unitary tensor equivalence by Prop.
4.22 b). □

96 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
We next discuss classification of ∗-representations for the important class of discrete
Ω-involutive weak quasi-bialgebras in the sense of Def. 11.5. So we may write, up to
∗
-isomorphism, A =
L
r Mnr
(C). The projections ρr : A → Mnr
(C) are irreducible C
∗
-
representations.
Proposition 12.10. The ∗-representations ρr together with their opposites ρ−r, exhaust
the irreducible ∗–representations of A up to unitary equivalence. Furthermore any ∗-
representation of A decomposes as an orthogonal direct sum of copies of them. Finally, Ω
is positive if and only of for all s, t, ρs⊗ρt is an orthogonal direct sum of ρr only.
Proof. When we forget about the ∗-structure, an irreducible representation ρ of A is equivalent to some ρr. Therefore to classify irreducible ∗–representations, we need to classify up
to unitary equivalence the Hermitian forms on C
nr making ρr into a ∗
-representation. By
Prop. 12.4 these are ρr and ρ−r. We have already noticed that ρr and ρ−r are not unitarily
equivalent, hence altogether they form a complete list of irreducible ∗–representations, up
to unitary equivalence. Let now σ be a reducible ∗-representation of A and let us decompose it, as a representation, as a direct sum of certain σr, where σr is a multiple of ρr. Each
σr acts on Vσr = σ(er)Vσ, with er a minimal central projection of A. Hence these subspaces
are pairwise orthogonal by ∗-invariance of σ. In particular, the form of Vσ is nondegenerate
on all the Vσr
. In turn, the pairwise equivalent irreducible summands τi of a fixed σr act
on the linear span Vi of {σr(e11)vi, σr(e21)vi, . . . , σr(enr1)vi} respectively, where viform a
linear basis of σr(e11)Vσr and we claim that it is possible to choose vi pairwise orthogonal.
The claim shows that these copies of ρr act on pairwise orthogonal subspaces. To show
the claim, notice that the map v ∈ σr(e11)Vσr → σr(ei1)v ∈ σr(eii)Vσris unitary between
pairwise orthogonal subspaces of Vσr, hence the form of Vσr must be nondegenerate on
each of them, and the claim follows. To show the last assertion, we use an orthogonal
decomposition into irreducibles in the general case, given by isometries S
±
r,j ∈ (ρ±r, ρs⊗ρt).
These determine the components ρs ⊗ ρt(Ω) in the full matrix C
∗
-subalgebras of A ⊗ A
by the formula (ξ, ρs ⊗ ρt(Ω)η)p =
P(S
±
r,j
∗
ξ, S±
r,j
∗
η), where ξ, η vary in the vector space of
ρs⊗ρt and the inner products at the right hand side refer to ρ±r. The claim easily follows
from this equation.
□
Remark 12.11. Examples have been found by Fr¨ohlich and Kerler [63] and Rowell [157,
158, 159] of braided fusion categories which are not unitarizable.
