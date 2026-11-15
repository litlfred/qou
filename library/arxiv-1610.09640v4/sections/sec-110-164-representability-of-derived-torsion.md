---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-110-164-representability-of-derived-torsion
section_title: "Representability of Derived Torsion"
section_number: 16.4
pages: 367-371
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
an adaptation of results from [157, Section 7] to the connected graded setting.
In Section 17 we are going to use the representability of derived torsion to give an
alternative proof of M. Van den Bergh’s theorem on existence of balanced dualizing
complexes (see Theorem 17.3.19).
Recall that Conventions 15.1.17 and 15.2.1 are in force. In this subsection we
assume the following strengthening of Setup 16.3.1.
Setup 16.4.1. We are given a left noetherian connected graded K-ring A, with
augmentation ideal m = L
i≥1 Ai ⊆A, such that the torsion functor Γm has ﬁnite
right cohomological dimension. We are also given a graded K-ring B.
As before, the graded ring B plays an auxiliary role, a placeholder for A or K.
Deﬁnition 16.4.2. Under Setup 16.4.1, the dedualizing complex of A is the com-
plex PA := RΓm(A) ∈D(Aen, gr).
The name “dedualizing” is due to L. Positselsky [121] . Regarding the lack of
left-right symmetry in this deﬁnition, see Corollary 16.5.11 and Proposition 16.5.19.
As a special case of Proposition 16.3.16, there is a morphism σR
A : PA = RΓm(A)
→A in D(Aen, gr).
Theorem 16.4.3 (Representability of Derived Torsion, [157]). Under Setup 16.4.1
there is a unique isomorphism
evR,L
m,(−) : PA ⊗L
A (−)
≃
−→RΓm(−)
of triangulated functors from D(A ⊗Bop, gr) to itself, called derived m-torsion
tensor-evaluation, such that for every complex M ∈D(A ⊗Bop, gr) the diagram
(♥)
PA ⊗L
A M
evR,L
m,M
∼
=
/
σR
A ⊗L
A idM

RΓm(M)
σR
M

A ⊗L
A M
lu
∼
=
/ M
is commutative.
The isomorphism marked “lu” in diagram (♥) is the left unitor isomorphism of
the closed monoidal structure, see equation (16.3.3).
The proof of the theorem requires the next lemma.
Lemma 16.4.4. Let F, G : D(A, gr) →D(B, gr) be quasi-compact triangulated
functors, and let η : F →G be a morphism of triangulated functors. Assume that
ηA : F(A) →G(A) is an isomorphism. Then η is an isomorphism.
367
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Proof. We are given that ηA is an isomorphism. Because the algebraic degree twist
M 7→M(i) is an automorphism of D(A, gr), it follows that ηA(i) is an isomorphism
for every integer i. Likewise for the cohomological degree shift (i.e. the translation
M 7→M[i] on complexes), so ηA(i)[j] is an isomorphism for every integer j. Both
functors are quasi-compact, and therefore ηP is an isomorphism for every graded-
free complex of A-modules P ∼= L
x∈X A(ix)[jx].
Suppose we are given a distinguished triangle M ′ →M →M ′′
△
−→in D(A, gr),
such that two of the three morphisms ηM ′, ηM and ηM ′′ are isomorphisms. Because
η is a morphism of triangulated functors, it follows that third morphism is also an
isomorphism.
Next
consider
a
semi-graded-free
DG
module
P.
Take
a
ﬁltration
{Fj(P)}j≥−1 of P as in Deﬁnition 15.3.1(2). For every j we have a distinguished
triangle
Fj−1(P)
θj
−→Fj(P) →GrF
j (P)
△
−→
in D(A, gr), where θj : Fj−1(P) →Fj(P) is the inclusion.
Since GrF
j (P) is a
graded-free complex, by induction on j we conclude that ηFj(P ) is an isomorphism
for every j ≥0. The homotopy colimit construction (see Deﬁnition 14.1.11) gives
a distinguished triangle
M
j∈N
Fj(P)
Θ
−−→
M
j∈N
Fj(P) →P
△
−→
in D(A, gr), where
Θ|Fj−1(P ) := (id, −θj) : Fj−1(P) →Fj−1(P) ⊕Fj(P).
By quasi-compactness we know that ηL
Fj(P ) is an isomorphism. Therefore ηP is
an isomorphism.
Finally, every M ∈D(A, gr) admits an isomorphism M ∼= P with P semi-graded-
free. Therefore ηM is an isomorphism.
□
Proof of Theorem 16.4.3.
Step 1. We begin by constructing the morphism of triangulated functors evR,L
m,(−).
For each complex M ∈C(A ⊗Bop, gr) we choose a K-graded-injective resolution
ρM : M →IM and a K-graded-ﬂat resolution θM : QM →M, both in Cstr(A ⊗
Bop, gr). Note that IM is K-graded-m-ﬂasque over A, and QM is K-graded-ﬂat over
A. We use these choices for presentations of the right derived functor
(RΓm, ηR) : D(A ⊗Bop, gr) →D(A ⊗Bop, gr)
and the left derived bifunctor
(−⊗L
A −, ηL) : D(Aen, gr) × D(A ⊗Bop, gr) →D(A ⊗Bop, gr).
Let us also choose a K-graded-injective resolution ψ : A →J in Cstr(Aen, gr). With
these choices we have the following presentations: PA = Γm(J),
(16.4.5)
RΓm(M) = Γm(IM)
and
(16.4.6)
PA ⊗L
A M = Γm(J) ⊗A QM.
Suppose N ∈C(A ⊗Bop, gr) is some complex. Given homogeneous elements
x ∈Γm(J) and n ∈N, the tensor x ⊗n belongs to Γm(J ⊗A N). In this way we
obtain a homomorphism
(16.4.7)
evm,J,N : Γm(J) ⊗A N →Γm(J ⊗A N)
in Cstr(A ⊗Bop, gr), which is functorial in N.
368
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Consider a complex M ∈C(A ⊗Bop, gr). The choices we made give rise to this
solid diagram
(16.4.8)
A ⊗A QM
lu
/
ψ ⊗A id

QM
θM
/ M
ρM

J ⊗A QM
χM
/ IM
in Cstr(A ⊗Bop, gr). The homomorphisms ψ ⊗A id, θM ◦lu and ρM are quasi-
isomorphisms. Because IM is K-injective in C(A ⊗Bop, gr), there is a quasi-iso-
morphism χM : J ⊗A QM →IM that makes this diagram commutative up to
homotopy.
We now form diagram (16.4.9) in Cstr(A ⊗Bop, gr). Here evm,J,QM is the ho-
(16.4.9)
Γm(J) ⊗A QM
evm,J,QM
/
σJ ⊗A id

Γm(J ⊗A QM)
Γm(χM)
/
σ(J⊗AQM )

Γm(IM)
σIM

J ⊗A QM
id
/ J ⊗A QM
χM
/ IM
A ⊗A QM
ψ ⊗A id
O
id
/ A ⊗A QM
ψ ⊗A id
O
θM◦lu
/ M
ρM
O
momorphism from (16.4.7). The diagram (16.4.9) is commutative up to homotopy.
(Actually all small squares, except the bottom right one, are commutative in the
strict sense.) The vertical arrows ψ ⊗A id and ρM are quasi-isomorphisms. Pass-
ing to D(A ⊗Bop, gr) we get a commutative diagram, with vertical isomorphisms
between the second and third rows. The diagram with the four extreme objects
only is the one we are looking for. By construction it is a commutative diagram in
D(A ⊗Bop, gr), and it is functorial in M. The morphism
evR,L
m,M : PA ⊗L
A M →RΓm(M)
that we want is represented by
Γm(χM) ◦evm,J,QM : Γm(J) ⊗A QM →Γm(IM).
See (16.4.5) and (16.4.6).
Step 2. In this step we prove that evR,L
m,M is an isomorphism for every complex
M ∈D(A ⊗Bop, gr). Because the functor Rest is conservative, it suﬃces to prove
that the morphism
Rest(evR,L
m,M) : Rest(PA ⊗L
A M) →Rest(RΓm(M))
in D(A, gr) is an isomorphism. Going over all the details of the construction above,
and noting that ρM : M →IM and θM : QM →M are K-ﬂat and K-injective
resolutions, respectively, also in the category Cstr(A, gr), we might as well forget
about the ring B.
So now we are in the case B = K, A ⊗Bop = A, and we want to prove that
evR,L
m,M is an isomorphism for every M ∈D(A, gr). By Theorem 16.3.21 the functor
RΓm on D(A, gr) is quasi-compact. The functor P ⊗L
A (−) is also quasi-compact.
This means that we can use Lemma 16.4.4, and it tells us that it suﬃces to prove
that evR,L
m,M is an isomorphism for M = A.
369
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Let us examine the morphism evR,L
m,A, i.e. evR,L
m,M for M = A. We can choose the
K-ﬂat resolution θA : QA →A in Cstr(A, gr) to be the identity of A. Also, we can
choose the K-injective resolution ρA : A →IA in Cstr(A, gr) to be the restriction of
ψ : A →J. Then the homomorphism χA : J ⊗A QA →IA in diagram (16.4.8) can
be chosen to be χA = id ⊗A id. We get a commutative diagram
Γm(J) ⊗A QA
evm,J,QA
/
id ⊗AθA

Γm(J ⊗A QA)
Γm(χA)
/
Γm(id ⊗AθA)

Γm(IA)
id

Γm(J) ⊗A A
evm,J,A
/ Γm(J ⊗A A)
Γm(ru)
/ Γm(J)
in Cstr(A, gr). Here ru : J ⊗A A
≃
−→J is the canonical isomorphism (the right
unitor).
The horizontal arrows in the second row, and the vertical arrows, are
all bijective. We conclude that Γm(χA) ◦evm,J,QA is bijective. Hence evR,L
m,A is an
isomorphism in D(A, gr).
Step 3. It remains to prove the uniqueness of evR,L
m,(−). By applying the functor RΓm
to the diagram (♥), and then making use of the morphism of functors σR : RΓm →
Id, we obtain the commutative diagram (16.4.10) in D(A ⊗Bop, gr). The vertical
(16.4.10)
PA ⊗L
A M
evR,L
m,M
∼
=
/ RΓm(M)
RΓm(PA ⊗L
A M)
σR
(PA⊗L
AM)
O
RΓm(evR,L
m,M)
∼
=
/
RΓm(σR
A ⊗L
A idM)

RΓm(RΓm(M))
σR
RΓm(M)
O
RΓm(σR
M)

RΓm(A ⊗L
A M)
RΓm(lu)
∼
=
/ RΓm(M)
morphisms σR
RΓm(M) and RΓm(σR
M) are isomorphisms because of the idempotence
(Corollary 16.3.36).
Therefore the other two vertical arrows are isomorphisms.
We see that the isomorphism evR,L
m,M can be expressed as the composition of other
isomorphisms; so it is unique.
□
The next result is due to Van den Bergh [153]. We give another proof, based on
Theorem 16.4.3. Recall the K-linear duality functor
(−)∗: D(A ⊗Bop, gr)op →D(B ⊗Aop, gr).
Its formula is
(−)∗:= HomK(−, K) ∼= HomA(−, A∗).
Corollary 16.4.11 (Van den Bergh’s Local Duality, [153]). Under Setup 16.4.1,
for every complex M ∈D(A ⊗Bop, gr) there is an isomorphism
RΓm(M)∗∼= RHomA
 M, (PA)∗
in D(B ⊗Aop, gr). This isomorphism is functorial in M.
370
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Proof. We have the following functorial isomorphisms
RΓm(M)∗∼=† (PA ⊗L
A M)∗= HomK(PA ⊗L
A M, K)
∼= RHomA(PA ⊗L
A M, A∗)
∼=♥RHomA
 M, RHomA(PA, A∗)

∼= RHomA
 M, (PA)∗
in D(B ⊗Aop, gr).
The isomorphism ∼=† is according to Theorem 16.4.3.
The
isomorphism ∼=♥comes from derived Hom-tensor adjunction.
□
