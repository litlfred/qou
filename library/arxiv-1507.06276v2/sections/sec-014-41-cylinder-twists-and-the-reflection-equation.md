---
doc_id: arxiv-1507.06276v2
doc_title: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS"
section_id: sec-014-41-cylinder-twists-and-the-reflection-equation
section_title: "Cylinder twists and the reflection equation"
section_number: 4.1
pages: 17-18
source_pdf: 1507.06276v2.pdf
source_sha256: f552aa5de7125b23
toc_source: outline
doc_brief: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS — Let g be a symmetrizable Kac-Moody algebra and let Uq(g) de- note the corresponding quantized enveloping algebra."
---
(A, ⊗,I,a,l,r ) be a tensor category as deﬁned in [Kas95, Deﬁnition XI.2.1]. Let B
be another category and assume that there exists a functor ∗ : B × A → B which
we write as
(M,N ) ↦→M ∗N, (f,g ) ↦→f ∗g
on objects M ∈ Ob(B),N ∈ Ob(A) and morphisms f,g in B and A, respectively.
The functor ∗ is called a right action of A on B if there exist natural isomorphisms
α and ρ with
αM,N,N ′ : (M ∗N ) ∗N ′ →M ∗ (N ⊗N ′) for M ∈Ob(B),N,N ′ ∈Ob(A)
ρM :M ∗I →M for M ∈Ob(B)
which satisfy the pentagon and the triangle axiom given in [tD98, (2.1) , (2.2)].
A category B together with a right action of A on B is called a right A-module
category.
Example 4.1. As seen in Section 3.3, the category A = Oint is a braided tensor
category. Let B ⊆Uq(g) be a right coideal subalgebra, that is a subalgebra satisfyi ng
∆(B) ⊆B ⊗Uq(g).
Let B be the category with Ob(B) = Ob(Oint) and HomB(M,N ) = HomB(M,N ) for
all M,N ∈Ob(B). Then B is a right A-module category with ∗ given by M ∗N =
M ⊗N .
From now on, following [tD98], we will consider the following data:
(1) ( A, ⊗,I,a,l,r,c ) is a braided tensor category with braiding cM,N :M ⊗N →
N ⊗M for all M,N ∈Ob(A).
(2) ( B, ∗,α,ρ ) is a right A-module category.
(3) A is a subcategory of B withOb(A) = Ob(B). In other words Hom A(M,N )
is a subset of Hom B(M,N ) for all M,N ∈Ob(A) = Ob(B).
(4) ∗, α, ρ restrict to ⊗,a, r on A × A.
We call ( B, A) a tensor pair if the above conditions (1)-(4) are satisﬁed. By con di-
tion (3) there exists a forgetful functor
ForA
B : A → B.
Deﬁnition 4.2. Let (B, A) be a tensor pair. A natural transformation
t = (tM )M∈Ob(A) : ForA
B → ForA
B
is called a B-endomorphism of A. If tM : ForA
B (M ) → ForA
B (M ) is an automor-
phisms for all M ∈Ob(A) then t is called a B-automorphisms of A.
18 MARTINA BALAGOVI ´C AND STEF AN KOLB
In other words, a B-endomorphism of A is a family t = (tM )M∈Ob(A) of mor-
phisms tM ∈ HomB(M,M ) such that
tN ◦f =f ◦tM(4.1)
for all f ∈ HomA(M,N ).
Example 4.3. The pair (B, A) from Example 4.1 is a tensor pair. In this setting
a B-endomorphism of Oint is an element t ∈ U which commutes with all elements
of the coideal subalgebra B ⊂ U . In other words, the maps tM : M → M are
B-module homomorphisms for all M ∈Ob(Oint).
The following deﬁnition provides the main structure investigated by t om Dieck
and H¨ aring-Oldenburg in [tD98], [tDHO98], [HO01].
Deﬁnition 4.4 ([tD98]). Let (B, A) be a tensor pair. A cylinder twist for (B, A)
consists of a B-automorphism t = (tM )M∈Ob(A) of A such that
tM⊗N = (tM ∗ 1N )cN,M (tN ∗ 1M )cM,N(4.2)
for all M,N ∈Ob(A) = Ob(B).
The deﬁnition of a cylinder twist in [tD98] involves a second equation. T his
equation, however, is a consequence of (4.2). This was already obs erved in [tD98,
Proposition 2.10].
Proposition 4.5. Let (B, A) be a tensor pair with a cylinder twist (tM )M∈Ob(A).
Then the relation
(tM ∗ 1N )cN,M (tN ∗ 1M )cM,N =cN,M (tN ∗ 1M )cM,N (tM ∗ 1N )(4.3)
holds for all M,N ∈Ob(A).
Proof. AscN,M is a morphism in A, relation (4.1) implies that
tM⊗N ◦cN,M =cN,M ◦tN ⊗M.
If one inserts relation (4.2) into both sides of the above equation on e obtains Equa-
tion (4.3). □
In [tDHO98] Equation (4.3) is called the four-braid relation . Here we follow
the mathematical physics literature [KS92] and call (4.3) the reﬂection equation .
Equation (4.2) is know as the fusion procedure, see [KS92, 6.1], as it allows us to fuse
the two solutions tM and tN of the reﬂection equation for M and N , respectively,
to a new solution tM⊗N for the tensor product M ⊗N .
