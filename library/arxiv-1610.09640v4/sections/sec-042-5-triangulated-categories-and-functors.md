---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-042-5-triangulated-categories-and-functors
section_title: "Triangulated Categories and Functors"
section_number: 5
pages: 91-94
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
In this section we introduce triangulated categories and triangulated functors.
We prove that for a DG ring A and an abelian category M, the homotopy category
K(A, M) is triangulated. We also prove that a DG functor F : C(A, M) →C(B, N)
induces a triangulated functor F : K(A, M) →K(B, N).
Recall that by Convention 1.2.4, there is a nonzero commutative base ring K,
which is implicit most of the time.
All rings are central K-rings, and all ring
homomorphisms are over K. All linear categories are K-linear, and all linear (i.e.
additive) functors between them are K-linear.
5.1. Triangulated Categories. In this subsection we deﬁne triangulated cate-
gories, and make some remarks regarding them.
Recall that a functor is called an isomorphism of categories if it is bijective on
sets of objects and on sets of morphisms.
Deﬁnition 5.1.1. Let K be an additive category. A translation functor on K is an
additive automorphism T of K. The pair (K, T) is called a T-additive category.
Remark 5.1.2. Some texts give a more relaxed deﬁnition: the translation functor
T is only required to be an additive auto-equivalence of K. The resulting theory is
more complicated (it is 2-categorical, but most texts try to suppress this fact).
Later in the book (see Deﬁnition 12.1.7) we will write M[k] := Tk(M), the k-th
translation of an object M.
Deﬁnition 5.1.3. Suppose (K, TK) and (L, TL) are T-additive categories. A T-
additive functor between them is a pair (F, τ), consisting of an additive functor
F : K →L, together with an isomorphism
τ : F ◦TK
≃
−→TL ◦F
of functors K →L, called a translation isomorphism.
Deﬁnition 5.1.4. Let (Ki, Ti) be T-additive categories, for i = 0, 1, 2, and let
(Fi, τi) : (Ki−1, Ti−1) →(Ki, Ti)
be T-additive functors. The composition
(F, τ) = (F2, τ2) ◦(F1, τ1)
is the T-additive functor (K0, T0) →(K2, T2) deﬁned as follows: the functor is
F := F2◦F1, and the translation isomorphism τ : F ◦T0
≃
−→T2◦F is τ := τ2◦F2(τ1).
Deﬁnition 5.1.5. Suppose (K, TK) and (L, TL) are T-additive categories, and
(F, τ), (G, ν) : (K, TK) →(L, TL)
are T-additive functors. A morphism of T-additive functors
η : (F, τ) →(G, ν)
is a morphism of functors η : F →G, such that for every object M ∈K this diagram
in L is commutative:
F(TK(M))
τM
/
ηTK(M)

TL(F(M))
TL(ηM)

G(TK(M))
νM
/ TL(G(M)) .
This material will be published by Cambridge University Press as Derived Categories by Amnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works. c⃝Amnon Yekutieli, 2019.
91
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Deﬁnition 5.1.6. Let (K, T) be a T-additive category. A triangle in (K, T) is a
diagram
L
α−→M
β−→N
γ−→T(L)
in K.
Sometimes, when the names of the morphisms in the triangle above are not
important, we may use the more compact notation
(5.1.7)
L −→M −→N
△
−−→.
Deﬁnition 5.1.8. Let (K, T) be a T-additive category. Suppose
L
α−→M
β−→N
γ−→T(L)
and
L′
α′
−→M ′
β′
−→N ′
γ′
−→T(L′)
are triangles in (K, T). A morphism of triangles between them is a commutative
diagram
L
α
/
φ

M
β
/
ψ

N
γ
/
χ

T(L)
T(φ)

L′
α′
/ M ′
β′
/ N ′
γ′
/ T(L′)
in K.
The morphism of triangles (φ, ψ, χ) is called an isomorphism if φ, ψ and χ are
all isomorphisms.
Remark 5.1.9. Why “triangle”? This is because sometimes a triangle
L
α−→M
β−→N
γ−→T(L)
is written as a diagram
N
γ
~
L
α
/ M
β
a
See [62, page 20].
Deﬁnition 5.1.10. A triangulated category is a T-additive category (K, T),
equipped with a set of triangles called distinguished triangles. The following axioms
have to be satisﬁed:
(TR1)
(a) Every triangle that is isomorphic to a distinguished triangle is also a
distinguished triangle.
(b) For every morphism α : L →M in K there is a distinguished triangle
L
α−→M −→N −→T(L).
(c) For every object M the triangle
M
idM
−−→M →0 →T(M)
is distinguished.
(TR2) A triangle
L
α−→M
β−→N
γ−→T(L)
is distinguished iﬀthe triangle
M
β−→N
γ−→T(L)
−T(α)
−−−−→T(M)
is distinguished.
92
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(TR3) Suppose
L
α
/
φ

M
β
/
ψ

N
γ
/ T(L)
L′
α′
/ M ′
β′
/ N ′
γ′
/ T(L′)
is a commutative diagram in K in which the rows are distinguished triangles.
Then there exists a morphism χ : N →N ′ such that the diagram
L
α
/
φ

M
β
/
ψ

N
γ
/
χ

T(L)
T(φ)

L′
α′
/ M ′
β′
/ N ′
γ′
/ T(L′) .
is a morphism of triangles.
(TR4) Suppose we are given these three distinguished triangles:
L
α−→M
γ−→P −→T(L),
M
β−→N
ϵ−→R −→T(M),
L
β◦α
−−→N
δ−→Q −→T(L).
Then there is a distinguished triangle
P
φ−→Q
ψ−→R
ρ−→T(P)
making diagram (5.1.11) commutative.
(5.1.11)
L
α
/
id

M
γ
/
β

P
/
φ

T(L)
id

L
β◦α
/
α

N
δ
/
id

Q
/
ψ

T(L)
T(α)

M
β
/
γ

N
ϵ
/
δ

R
/
id

T(M)
T(γ)

P
φ
/ Q
ψ
/ R
ρ
/ T(P)
Here are a few remarks on triangulated categories. See Remark 5.4.16 regarding
triangulated categories arising from algebraic topology.
Remark 5.1.12. The numbering of the axioms we use is taken from [62], and it
agrees with the numbering in [158]. The numbering in [75] and [76] is diﬀerent.
In the situation that we care about, namely K = K(A, M), the distinguished
triangles will be those triangles that are isomorphic, in K(A, M), to the standard
triangles in C(A, M) from Deﬁnition 4.2.5. See Deﬁnition 5.4.2 below for the precise
statement.
The object N in item (b) of axiom (TR1) is referred to as a cone of the morphism
α. We should think of the cone as something combining “the cokernel” and “the
kernel” of α. Axiom (TR3) guarantees a sort of weak functoriality of the cone. See
Subsection 5.3, and in particular Remark 5.3.9, for more properties of the cone.
93
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Axiom (TR2) says that if we “turn” a distinguished triangle (cf. Remark 5.1.9)
we remain with a distinguished triangle.
Remark 5.1.13. The axiom (TR4) is called the octahedral axiom. It is supposed
to replace the isomorphism
(N/L)/(M/L) ∼= N/M
for objects L ⊆M ⊆N in an abelian category M. The octahedral axiom is needed
for the theory of t-structures: it is used, in [16], to show that the heart of a t-
structure is an abelian category (see Remark 5.3.26). This axiom is also needed to
form Verdier quotients of triangulated categories (see Remark 7.1.14). The book
[113] has detailed discussions of the octahedral axiom.
A T-additive category (K, T) that only satisﬁes axioms (TR1)-(TR3) is called
a pretriangulated category. (The reader should not confuse “pretriangulated cate-
gory”, as used here, with the “pretriangulated DG category” from [25]; see Remark
5.5.4.) It is not known whether the octahedral axiom is a consequence of the other
axioms; there was a recent paper by A. Maccioca (arxiv:1506.00887) claiming that,
but it had a fatal error in it.
In our book the octahedral axiom does not play any role. For this reason we
had excluded it from an earlier version of the book, in which we had discussed
pretriangulated categories only. Our decision to include this axiom in the current
version of the book, and thus to talk about triangulated categories (rather than
about pretriangulated ones) is just to be more in line with the mainstream usage.
With the exception of a longer proof of Theorem 5.4.3 – stating that K(A, M) is a
triangulated category – there is virtually no change in the content of the book, and
almost all deﬁnitions and results are valid for pretriangulated categories.
Remark 5.1.14. The structure of triangulated categories is poorly understood,
and there is no classiﬁcation of triangulated functors between them. This is true
even for the derived category D(A) of a ring A.
For instance, a famous open
question of J. Rickard is whether every triangulated auto-equivalence F of D(A) is
isomorphic to P ⊗L
A (−) for some tilting complex P. More on this issue in Section
14.
In this book the role of the triangulated structure on derived categories is sec-
ondary. It is mostly used for induction on the amplitude of the cohomology of
complexes; cf. Section 12.
Furthermore, one of the most important functors studied here – the squaring
operation SqB/A from Subsections 13.4 and 18.2 – is a functor from D(B) to itself,
which is not triangulated, nor even linear: it is a quadratic functor.
