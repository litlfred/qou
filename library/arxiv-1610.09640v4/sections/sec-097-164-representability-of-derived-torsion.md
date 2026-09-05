---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-097-164-representability-of-derived-torsion
section_title: "Representability of Derived Torsion"
section_number: 16.4
pages: 367-371
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
an adaptation of results from [157, Section 7] to the connected graded setting.
In Section 17 we are going to use the representability of derived torsion to give an
alternative proof of M. Van den Bergh’s theorem on existence of balanced dualizing
complexes (see Theorem 17.3.19).
Recall that Conventions 15.1.17 and 15.2.1 are in force. In this subsection we
assume the following strengthening of Setup 16.3.1.
Setup 16.4.1. We are given a left noetherian connected gradedK-ring A, with
augmentation ideal m =⨁
i≥1Ai⊆A, such that the torsion functorΓ m has ﬁnite
right cohomological dimension. We are also given a gradedK-ring B.
As before, the graded ringB plays an auxiliary role, a placeholder forA orK.
Deﬁnition 16.4.2.Under Setup 16.4.1, thededualizing complex ofA is the com-
plex PA := RΓ m(A)∈D(Aen, gr).
The name “dedualizing” is due to L. Positselsky [121] . Regarding the lack of
left-right symmetry in this deﬁnition, see Corollary 16.5.11 and Proposition 16.5.19.
As a special case of Proposition 16.3.16, there is a morphismσR
A :PA = RΓ m(A)
→A in D(Aen, gr).
Theorem 16.4.3(Representability of Derived Torsion, [157]). Under Setup16.4.1
there is a unique isomorphism
evR,L
m,(−) : PA⊗L
A (−)
≃
− →RΓ m(−)
of triangulated functors from D(A⊗Bop, gr) to itself, called derived m-torsion
tensor-evaluation, such that for every complexM∈D(A⊗Bop, gr) the diagram
(♥) PA⊗L
AM
evR,L
m,M
∼=
//
σR
A⊗L
A idM

RΓ m(M)
σR
M

A⊗L
AM lu
∼=
//M
is commutative.
The isomorphism marked “lu” in diagram (♥) is the left unitor isomorphism of
the closed monoidal structure, see equation (16.3.3).
The proof of the theorem requires the next lemma.
Lemma 16.4.4. Let F,G : D(A, gr)→D(B, gr) be quasi-compact triangulated
functors, and letη:F→G be a morphism of triangulated functors. Assume that
ηA :F (A)→G(A) is an isomorphism. Thenηis an isomorphism.
367
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. We are given thatηA is an isomorphism. Because the algebraic degree twist
M↦→M(i) is an automorphism ofD(A, gr), it follows thatηA(i) is an isomorphism
for every integeri. Likewise for the cohomological degree shift (i.e. the translation
M↦→M[i] on complexes), soηA(i)[j] is an isomorphism for every integerj. Both
functors are quasi-compact, and thereforeηP is an isomorphism for every graded-
free complex ofA-modules P∼=⨁
x∈XA(ix)[jx].
Suppose we are given a distinguished triangleM′→M→M′′∆
−→in D(A, gr),
such that two of the three morphismsηM′,ηM andηM′′are isomorphisms. Because
ηis a morphism of triangulated functors, it follows that third morphism is also an
isomorphism.
Next consider a semi-graded-free DG module P. Take a ﬁltration
{Fj(P )}j≥−1 of P as in Deﬁnition 15.3.1(2). For everyj we have a distinguished
triangle
Fj−1(P )
θj
−→Fj(P )→GrF
j (P )
∆
−→
in D(A, gr), where θj : Fj−1(P ) →Fj(P ) is the inclusion. Since GrF
j (P ) is a
graded-free complex, by induction onj we conclude thatηFj(P) is an isomorphism
for everyj≥0. The homotopy colimit construction (see Deﬁnition 14.1.11) gives
a distinguished triangle
⨁
j∈N
Fj(P )
Θ
−−→
⨁
j∈N
Fj(P )→P
∆
−→
in D(A, gr), where
Θ|Fj−1(P) := (id,−θj) :Fj−1(P )→Fj−1(P )⊕Fj(P ).
By quasi-compactness we know thatη⨁
Fj(P) is an isomorphism. ThereforeηP is
an isomorphism.
Finally, everyM∈D(A, gr) admits an isomorphismM∼=P withP semi-graded-
free. ThereforeηM is an isomorphism. □
Proof of Theorem16.4.3.
Step 1. We begin by constructing the morphism of triangulated functorsevR,L
m,(−).
For each complexM∈C(A⊗Bop, gr) we choose a K-graded-injective resolution
ρM : M→IM and a K-graded-ﬂat resolutionθM : QM →M, both in Cstr(A⊗
Bop, gr). Note thatIM is K-graded-m-ﬂasque overA, andQM is K-graded-ﬂat over
A. We use these choices for presentations of the right derived functor
(RΓ m,ηR) : D(A⊗Bop, gr)→D(A⊗Bop, gr)
and the left derived bifunctor
(−⊗L
A−,ηL) : D(Aen, gr)×D(A⊗Bop, gr)→D(A⊗Bop, gr).
Let us also choose a K-graded-injective resolutionψ:A→J in Cstr(Aen, gr). With
these choices we have the following presentations:PA = Γ m(J),
(16.4.5) RΓ m(M) = Γ m(IM)
and
(16.4.6) PA⊗L
AM = Γ m(J)⊗AQM.
Suppose N ∈C(A⊗Bop, gr) is some complex. Given homogeneous elements
x∈Γ m(J) and n∈N, the tensorx⊗n belongs to Γ m(J⊗AN). In this way we
obtain a homomorphism
(16.4.7) evm,J,N : Γ m(J)⊗AN→Γ m(J⊗AN)
in Cstr(A⊗Bop, gr), which is functorial inN.
368
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Consider a complexM∈C(A⊗Bop, gr). The choices we made give rise to this
solid diagram
(16.4.8) A⊗AQM
lu //
ψ⊗A id

QM
θM //M
ρM

J⊗AQM
χM //IM
in Cstr(A⊗Bop, gr). The homomorphisms ψ⊗A id, θM◦lu and ρM are quasi-
isomorphisms. Because IM is K-injective in C(A⊗Bop, gr), there is a quasi-iso-
morphism χM : J⊗A QM →IM that makes this diagram commutative up to
homotopy.
We now form diagram (16.4.9) inCstr(A⊗Bop, gr). Here evm,J,QM is the ho-
(16.4.9) Γ m(J)⊗AQM
evm,J,QM //
σJ⊗A id

Γ m(J⊗AQM)
Γm(χM) //
σ(J⊗AQM )

Γ m(IM)
σIM

J⊗AQM
id //J⊗AQM
χM //IM
A⊗AQM
ψ⊗A id
OO
id //A⊗AQM
ψ⊗A id
OO
θM◦lu //M
ρM
OO
momorphism from (16.4.7). The diagram (16.4.9) is commutative up to homotopy.
(Actually all small squares, except the bottom right one, are commutative in the
strict sense.) The vertical arrowsψ⊗A id and ρM are quasi-isomorphisms. Pass-
ing to D(A⊗Bop, gr) we get a commutative diagram, with vertical isomorphisms
between the second and third rows. The diagram with the four extreme objects
only is the one we are looking for. By construction it is a commutative diagram in
D(A⊗Bop, gr), and it is functorial inM. The morphism
evR,L
m,M :PA⊗L
AM→RΓ m(M)
that we want is represented by
Γ m(χM)◦evm,J,QM : Γ m(J)⊗AQM→Γ m(IM).
See (16.4.5) and (16.4.6).
Step 2. In this step we prove that evR,L
m,M is an isomorphism for every complex
M∈D(A⊗Bop, gr). Because the functorRest is conservative, it suﬃces to prove
that the morphism
Rest(evR,L
m,M) : Rest(PA⊗L
AM)→Rest(RΓ m(M))
in D(A, gr) is an isomorphism. Going over all the details of the construction above,
and noting thatρM : M →IM and θM : QM →M are K-ﬂat and K-injective
resolutions, respectively, also in the categoryCstr(A, gr), we might as well forget
about the ringB.
So now we are in the caseB = K, A⊗Bop = A, and we want to prove that
evR,L
m,M is an isomorphism for everyM∈D(A, gr). By Theorem 16.3.21 the functor
RΓ m on D(A, gr) is quasi-compact. The functorP⊗L
A (−) is also quasi-compact.
This means that we can use Lemma 16.4.4, and it tells us that it suﬃces to prove
that evR,L
m,M is an isomorphism forM =A.
369
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Let us examine the morphismevR,L
m,A, i.e. evR,L
m,M for M =A. We can choose the
K-ﬂat resolutionθA :QA→A in Cstr(A, gr) to be the identity ofA. Also, we can
choose the K-injective resolutionρA :A→IA in Cstr(A, gr) to be the restriction of
ψ:A→J. Then the homomorphismχA :J⊗AQA→IA in diagram (16.4.8) can
be chosen to beχA = id⊗A id. We get a commutative diagram
Γ m(J)⊗AQA
evm,J,QA //
id⊗AθA

Γ m(J⊗AQA)
Γm(χA) //
Γm(id⊗AθA)

Γ m(IA)
id

Γ m(J)⊗AA
evm,J,A // Γ m(J⊗AA)
Γm(ru) // Γ m(J)
in Cstr(A, gr). Here ru : J⊗A A
≃
− →J is the canonical isomorphism (the right
unitor). The horizontal arrows in the second row, and the vertical arrows, are
all bijective. We conclude thatΓ m(χA)◦evm,J,QA is bijective. Hence evR,L
m,A is an
isomorphism in D(A, gr).
Step 3. It remains to prove the uniqueness ofevR,L
m,(−). By applying the functorRΓ m
to the diagram (♥), and then making use of the morphism of functorsσR : RΓ m→
Id, we obtain the commutative diagram (16.4.10) inD(A⊗Bop, gr). The vertical
(16.4.10) PA⊗L
AM
evR,L
m,M
∼=
// RΓ m(M)
RΓ m(PA⊗L
AM)
σR
(PA⊗L
AM)
OO
RΓm(evR,L
m,M)
∼=
//
RΓm(σR
A⊗L
A idM)

RΓ m(RΓ m(M))
σR
RΓm(M)
OO
RΓm(σR
M)

RΓ m(A⊗L
AM)
RΓm(lu)
∼=
// RΓ m(M)
morphisms σR
RΓm(M) and RΓ m(σR
M) are isomorphisms because of the idempotence
(Corollary 16.3.36). Therefore the other two vertical arrows are isomorphisms.
We see that the isomorphismevR,L
m,M can be expressed as the composition of other
isomorphisms; so it is unique. □
The next result is due to Van den Bergh [153]. We give another proof, based on
Theorem 16.4.3. Recall theK-linear duality functor
(−)∗: D(A⊗Bop, gr)op→D(B⊗Aop, gr).
Its formula is
(−)∗:= HomK(−,K)∼= HomA(−,A∗).
Corollary 16.4.11 (Van den Bergh’s Local Duality, [153]). Under Setup 16.4.1,
for every complexM∈D(A⊗Bop, gr) there is an isomorphism
RΓ m(M)∗∼= RHomA
(
M, (PA)∗{
in D(B⊗Aop, gr). This isomorphism is functorial inM.
370
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. We have the following functorial isomorphisms
RΓ m(M)∗∼=†(PA⊗L
AM)∗= HomK(PA⊗L
AM,K)
∼= RHomA(PA⊗L
AM,A∗)
∼=♥RHomA
(
M, RHomA(PA,A∗)
{
∼= RHomA
(
M, (PA)∗{
in D(B⊗Aop, gr). The isomorphism ∼=†is according to Theorem 16.4.3. The
isomorphism∼=♥comes from derived Hom-tensor adjunction. □
16.5. SymmetryofDerivedTorsion. Theresultsofthissubsectionareanadap-
tation of results from [157, Section 8] to the connected graded setting. Among other
things, we prove that theχcondition of Artin-Zhang implies symmetry of derived
torsion.
