---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-080-134-van-den-bergh-rigidity
section_title: "Van den Bergh Rigidity"
section_number: 13.4
pages: 273-280
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
plexR over a noetherian commutative ringA is not unique. This lack of uniqueness
(not to mention any sort of functoriality!) was the source of major diﬃculties in
[62], ﬁrst for gluing dualizing complexes on schemes, and then for producing the
trace morphisms associated to maps of schemes.
In 1997, M. Van den Bergh [153] discovered the idea ofrigidity for dualizing
complexes. This was done in the context of noncommutative ring theory: A is
a noncommutative noetherian ring, central over a base ﬁeldK. The theory of
noncommutative rigid dualizing complexes was developed further in several papers
of J.J. Zhang and A. Yekutieli, among them [183] and [187]. We shall talk about
this noncommutative theory in Section 18 of the book.
Herewewilldealwiththecommutativesideonly, whichturnsouttobeextremely
powerful. Before explaining it, let us ﬁrst observe that this is one of the rare cases
in which an idea originating from noncommutative algebra had signiﬁcant impact
in commutative algebra and algebraic geometry.
In this subsection we study Van den Bergh rigidity in the following context:
Setup 13.4.1.A is a commutative ring, andB is a ﬂat commutativeA-ring.
We introduce the notion ofrigid complex over B relative to A, and describe
some of its properties. In Subsection 13.5 we will discussrigid dualizing and residue
complexes. This material is adapted from the papers [188], [189] and [175].
The theory of rigid complexes does not really require the assumption thatB is
ﬂat overA, but ﬂatness makes the theory much easier. See Remark 13.4.24.
Consider the enveloping ringB⊗AB. It comes equipped with a few ring homo-
morphisms:
(13.4.2) B
ηi
−→B⊗AB
ϵ
− →B,
whereη0(b) :=b⊗1,η1(b) := 1⊗b, andϵ(b0⊗b1) :=b0·b1. We viewB as a module
overB⊗AB via ϵ. Of courseϵ◦ηi = idB.
Supposewearegiven B-modulesM0 andM1. Thenthetensorproduct M0⊗AM1
is a (B⊗AB)-module. In this way we get an additive bifunctor
(−⊗A−) : M(B)×M(B)→M(B⊗AB).
Passing to complexes, and then to homotopy categories, we obtain a triangulated
bifunctor
(13.4.3) (−⊗A−) : K(B)×K(B)→K(B⊗AB).
273
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Lemma 13.4.4. The bifunctor (13.4.3) has a left derived bifunctor
(−⊗L
A−) : D(B)×D(B)→D(B⊗AB).
If either M0 or M1 is a complex of B-modules that is K-ﬂat overA, then the
morphism ηL
M0,M1 :M0⊗L
AM1→M0⊗AM1 in D(B⊗AB) is an isomorphism.
Proof. This is a variant of Theorem 12.3.1. We know by Corollary 11.4.26 and
Proposition 10.3.4 that every complexM∈C(B) admits a K-ﬂat resolutionP→
M. Because B is ﬂat overA, the complexP is also K-ﬂat overA. By Theorem
9.3.16 the left derived bifunctor (−⊗L
A−) exists, and the condition on ηL
M0,M1
holds. □
Remark 13.4.5. The innocuous looking Lemma 13.4.4 is actually of tremendous
importance. Without the ﬂatness ofA→B we could do very little homological
algebra of bimodules. Getting around the lack of ﬂatness requires the use of ﬂat
DG ring resolutions, as explained in Remark 13.4.24.
Every moduleL∈M(B) has an action byB⊗AB coming from the homomor-
phismϵin (13.4.2). Consider now a moduleN∈M(B⊗AB). TheK-moduleN has
two possibleB-module structures, coming from the homomorphismsηi. Thus the
K-module HomB⊗AB(L,N ) has three possibleB-module structures: there is one
action from theB-module structure onL, and there are two from theB-module
structures onN.
Lemma 13.4.6. The threeB-module structures onHomB⊗AB(L,N ) coincide.
Exercise 13.4.7. Prove the lemma.
We are mostly interested in theB-module L = B. As the moduleN changes,
we get an additive functor
HomB⊗AB(B,−) : M(B⊗AB)→M(B).
Passing to complexes, and then to homotopy categories, we get a triangulated
functor
HomB⊗AB(B,−) : K(B⊗AB)→K(B).
This has a right derived functor
(13.4.8) RHomB⊗AB(B,−) : D(B⊗AB)→D(B),
that is calculated by K-injective resolutions. Namely ifI ∈C(B⊗A B) is a K-
injective complex, then the morphism
ηR
B,I : HomB⊗AB(B,I )→RHomB⊗AB(B,I )
in D(B) is an isomorphism.
By composing the bifunctor (−⊗L
A−) from Lemma 13.4.4 and the functor
RHomB⊗AB(B,−) from (13.4.8) we obtain a triangulated bifunctor
(13.4.9) RHomB⊗AB(B,−⊗L
A−) : D(B)×D(B)→D(B).
Deﬁnition 13.4.10.Under Setup 13.4.1, thesquaring operation is the functor
SqB/A : D(B)→D(B)
deﬁned as follows:
(1) For a complexM∈D(B), its square is the complex
SqB/A(M) := RHomB⊗AB(B,M ⊗L
AM)∈D(B).
(2) For a morphismφ:M→N in D(B), its square is the morphism
SqB/A(φ) := RHomB⊗AB(B,φ⊗L
Aφ) : SqB/A(M)→SqB/A(N)
in D(B).
274
Derived Categories | Amnon Yekutieli | 14 Apr 2019
It will be good to have an explicit formulation of the squaring operation. Let us
ﬁrst choose a K-projective resolutionσ:P→M in C(B). Note thatP is unique up
tohomotopyequivalence, and σisuniqueuptohomotopy. Since B isﬂatoverA, the
complex P is K-ﬂat overA. We get an isomorphismpresP :P⊗AP
≃
− →M⊗L
AM
in D(B⊗A B), that we call apresentation. It is uniquely characterized by the
commutativity of the diagram
M⊗L
AM
ηL
M,M //M⊗AM
P⊗L
AP
ηL
P,P
∼= //
Q(σ)⊗L
AQ(σ) ∼=
OO
P⊗AP
presP
∼=
gg
Q(σ⊗Aσ)
OO
in D(B⊗AB).
Next we choose a K-injective resolutionρ: P⊗AP →I in C(B⊗AB). The
complex I is unique up to homotopy equivalence, and the homomorphism ρis
unique up to homotopy. The resolutionρgives rise to an isomorphism
presI : HomB⊗AB(B,I )
≃
− →RHomB⊗AB(B,P ⊗AP )
in D(B) such that the diagram
HomB⊗AB(B,P ⊗AP )
ηR
B,P⊗AP
//
Q(Hom(id,ρ))

RHomB⊗AB(B,P ⊗AP )
RHom(id,Q(ρ))∼=

HomB⊗AB(B,I )
ηR
B,I
∼= //
presI
∼=
44
RHomB⊗AB(B,I )
is commutative.
The combination of the presentationspresP and presI gives an isomorphism
presP,I : HomB⊗AB(B,I )
≃
− →SqB/A(M)
in D(B), that we also call a presentation.
Let φ: M →N be a morphism in D(B). The morphism SqB/A(φ) can also
be made explicit using presentations. For that we need to choose a K-projective
resolution σN :Q→N in C(B), and a K-injective resolutionρN :Q⊗AQ→J in
C(B⊗AB). These provide us with a presentation
presQ,J : HomB⊗AB(M,J )
≃
− →SqB/A(N).
There are homomorphisms ˜φ:P→Q in Cstr(B), andχ:I→J in Cstr(B⊗AB),
both unique up to homotopy, such that the diagrams
P
Q(σ)
∼=
//
Q(˜φ)

M
φ

Q
Q(σN)
∼=
//N
M⊗L
AM
φ⊗L
Aφ

P⊗AP
presP
∼=
oo Q(ρ)
∼=
//
Q(˜φ⊗A ˜φ)

I
Q(χ)

N⊗L
AN Q ⊗AQ
presQ
∼=
oo Q(ρN)
∼=
//J
275
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in D(B) and D(B⊗AB) respectively are commutative. See Subsections 10.1 and
10.2. Then the diagram
(13.4.11) HomB⊗AB(B,I )
presP,I
∼=
//
Q(Hom(id,χ))

SqB/A(M)
SqB/A(φ)

HomB⊗AB(B,J )
presQ,J
∼=
// SqB/A(N)
in D(B) is commutative.
The squaring operation is not an additive functor. In fact, it is a quadratic
functor:
Theorem 13.4.12. Letφ:M→N be a morphism inD(B) and letb∈B. Then
SqB/A(b·φ) =b2·SqB/A(φ),
as morphisms SqB/A(M)→SqB/A(N) in D(B).
Proof. We shall use presentations. Let˜φ:P→Q be a homomorphism inCstr(B)
that representsφ, as above. Then the homomorphismb·˜φ:P→Q Cstr(B) repre-
sentsb·φ. Tensoring we get a homomorphism
(b·˜φ)⊗A (b·˜φ) :P⊗AP→Q⊗AQ
Cstr(B⊗AB). But
(b·˜φ)⊗A (b·˜φ) = (b⊗b)·(˜φ⊗A ˜φ).
Hence on the K-injectives we get the homomorphism(b⊗b)·χ:I→J Cstr(B⊗AB).
We conclude that
HomB⊗AB
(
idB, (b⊗b)·χ
{
: HomB⊗AB(B,I )→HomB⊗AB(B,J )
represents SqB/A(b·φ). Finally, by Lemma 13.4.6 we know that
HomB⊗AB
(
idB, (b⊗b)·χ
{
= HomB⊗AB(b2·idB,χ)
=b2·HomB⊗AB(idB,χ).
□
Deﬁnition 13.4.13.Let M ∈D(B). A rigidifying isomorphism for M over B
relative toA is an isomorphismρ:M
≃
− →SqB/A(M) in D(B).
Deﬁnition 13.4.14.A rigid complexoverB relative toA is a pair(M,ρ), consist-
ing of a complexM∈D(B) and a rigidifying isomorphismρ:M
≃
− →SqB/A(M) in
D(B).
Deﬁnition 13.4.15.Suppose (M,ρ)and (N,σ)are rigid complexes overB relative
toA. Amorphism of rigid complexesφ: (M,ρ)→(N,σ)is a morphismφ:M→N
in D(B), such that the diagram
M
ρ
∼=
//
φ

SqB/A(M)
SqB/A(φ)

N σ
∼=
// SqB/A(N)
in D(B) is commutative.
The category of rigid complexes overB relative toA is denoted byD(B)rig/A.
276
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Recall (Deﬁnition 13.1.5) that a complexM ∈D(B) has the derived Morita
property if the derived homothety morphismhmR
M :B→RHomB(M,M ) in D(B)
is an isomorphism.
Theorem 13.4.16. Let (M,ρ) be a rigid complex overB relative toA. If M has
the derived Morita property, then the only automorphism of(M,ρ) in D(B)rig/A is
the identity.
Proof. Let φ: (M,ρ)
≃
− →(M,ρ) be an automorphism in D(B)rig/A. By Proposi-
tion 13.1.6, there is a unique invertible elementb∈B such thatφ= b·idM, as
morphisms M→M in D(B).
Next, according to Theorem 13.4.12, we have
SqB/A(φ) = SqB/A(b·idM) =b2·SqB/A(idM).
Plugging this into the diagram in Deﬁnition 13.4.15 we get a commutative diagram
M
ρ
∼=
//
b·idM

SqB/A(M)
b2·idM

M
ρ
∼=
// SqB/A(M)
in D(B). Once more using Proposition 13.1.6 we see thatb2 =b. Because b is an
invertible element, it follows thatb = 1. Thusφ= idM. □
Example 13.4.17. Assume B = A, and take M := B. Then B⊗A B ∼= B,
M⊗L
AM∼=M, and there are canonical isomorphisms
SqB/A(M) = RHomB⊗AB(B,M ⊗L
AM)∼= HomB(B,M )∼=M.
Thus the pair (M, idM) belongs to D(B)rig/A. Furthermore, the complexM has
the derived Morita property, so Theorem 13.4.16 applies.
Remark 13.4.18. To the reader who might object to Example 13.4.17 for being
silly, we have two things to say. First, the existence theorem for rigid dualizing
complexes 13.5.7, whose proof is beyond the scope of this book, starts with the
tautological rigid structureof K∈D(K), whereK is the regular base ring. The
rigid structure is then propagated to all ﬂat essentially ﬁnite type (FEFT)K-rings
using induction and coinduction of rigid structures. See the exercise and examples
below for an indication of these procedures.
The second fact we want to point out is that whenA is an FEFTK-ring, thenA
has exactly one rigid complex(M,ρ)∈D(A)rig/K (up to a unique isomorphism) that
is nonzero on each connected component ofSpec(A); and it is the rigid dualizing
complex ofA (that will be deﬁned in the next subsection). This is proved in [188],
[13] and [139].
Exercise 13.4.19. Assume A⁄= 0, and takeB := A[t1,...,tn], the polynomial
ring inn variables.
(1) Let C :=B⊗AB, and letI be the kernel of the multiplication homomor-
phismϵ:C→B. Showthat I isgeneratedbythesequence c = (c1,...,cn),
where cj :=tj⊗1−1⊗tj.
(2) Show that the Koszul complexK(C;c) is a free resolution ofB over C.
(Hint: for 1≤m≤n deﬁneBm := A[t1,...,tm] and Cm := Bm⊗ABm.
By direct calculation show thatK(C1;c1)→B1 is a quasi-isomorphism.
Next, there is a ring isomorphismBm⊗A B1
≃
− →Bm+1, 1⊗t1↦→tm+1.
277
Derived Categories | Amnon Yekutieli | 14 Apr 2019
This induces a ring isomorphismCm⊗AC1∼= Cm+1 and an isomorphism
of complexes
K(Cm;cm)⊗A K(C1;c1)∼= K(Cm+1;cm+1).
Use this last formula and induction onm to prove thatK(Cm;cm)→Bm
is a quasi-isomorphism.)
(3) Prove that
Exti
C(B,C )∼=
{
B if i =n
0 if i⁄=n.
(Hint: use the Koszul resolution from above.)
(4) Conclude from item (3) that the complexB[n]∈D(B) is rigid relative to
A; namely that there is a rigidifying isomorphismρ:B[n]
≃
− →SqB/A
(
B[n]
{
in D(B).
Example 13.4.20. Let A be a nonzero noetherian ring, and let B :=
A[t1,...,tn] as in the exercise above. Let∆ B/A := Ωn
B/A, the module of degreen
diﬀerential forms ofB relative toA. It is then-th exterior power ofΩ 1
B/A, so it is
a freeB module of rank1, with basisd(t1)∧···∧d(tn). By the previous example,
there exists some rigidifying isomorphismρfor the complex∆ B/A[n].
However, it can be shown (see [188] or [175]) that the complex∆ B/A[n] has a
canonical rigidifying isomorphism relative toA. I.e. there is a rigidifying isomor-
phism ρ: ∆ B/A[n]
≃
− →SqB/A
(
∆ B/A[n]
{
in D(B) which is invariant underA-ring
automorphisms ofB.
This rigidifying isomorphismρis an incarnation of Grothendieck’s Fundamen-
tal Local Isomorphism [62, Proposition II.7.2] and the Residue Isomorphism [62,
Theorem II.8.2].
It is well-known that a ﬁnitely generated moduleM over a noetherian ringA is
ﬂat iﬀ it is projective. See [105, Corollary to Theorem 7.12].
Example 13.4.21. Let A be a noetherian ring, and letA→B be a ﬁnite ﬂat
ring homomorphism. So B is a ﬁnitely generated projectiveA-module. Deﬁne
∆ B/A := HomA(B,A )∈M(B). It can be shown (see [175]) that the complex
∆ B/A hasacanonicalrigidifyingisomorphismrelativeto A. I.e.thereisarigidifying
isomorphism ρ: ∆ B/A
≃
− →SqB/A(∆ B/A) in D(B) which is invariant underA-ring
automorphisms ofB.
Remark 13.4.22. The squaring operationSqB/A is functorial also in the ringB,
in two directions. For this remark we assume that the ringA is noetherian, and
the rings B and C are ﬂat essentially ﬁnite typeA-rings. (See Remark 13.4.24
regarding the ﬂatness.)
Suppose u : B →C is a ﬁniteA-ring homomorphism, and θ: N →M is a
backward (or trace) morphism inD(B) overu, in the sense of Deﬁnition 12.6.11.
Then there is a backward morphism
Squ/A(θ) : SqC/A(N)→SqB/A(M)
in D(B)overu. The morphismSqu/A(θ)is functorial inuandθin an obvious sense.
Furthermore, under suitable ﬁniteness conditions, ifθis a nondegenerate backward
morphism (see Deﬁnition 12.6.13), then so isSqu/A(θ). We call this property the
trace functorialityof the squaring operation.
The trace functoriality of the squaring operation allows us to talk aboutrigid
trace morphisms. Withu :B→C as above, suppose that(M,ρ)∈D(B)rig/A and
278
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(N,σ)∈D(C)rig/A. A rigid trace morphismθ: (N,σ)→(M,ρ) overu relative to
A is a trace morphismθ:N→M overu such that the diagram
N σ
∼=
//
θ

SqC/A(N)
Squ/A(θ)

M
ρ
∼=
// SqB/A(M)
in D(B) is commutative.
Next, suppose v : B→C is an essentially étale homomorphism (i.e. formally
étale, plustheEFTconditionthatwasalreadyassumed)of A-rings, andλ:M→N
is a forward morphism overv, in the sense of Deﬁnition 12.6.3. Then there is a
forward morphism
qv/A(λ) : SqB/A(M)→SqC/A(N)
in D(B) over u. The morphism Sqv/A(λ) is functorial inv and λin an obvious
sense. Furthermore, under suitable ﬁniteness conditions, ifλis a nondegenerate
forward morphism (see Deﬁnition 12.6.7), then so isSqv/A(λ). We call this property
the étale functorialityof the squaring operation.
The étale functoriality of the squaring operation allows us to talk aboutrigid lo-
calization morphisms. Withv :B→C as above, suppose that(M,ρ)∈D(B)rig/A,
and (N,σ)∈D(C)rig/A. A rigid localization morphismλ: (M,ρ)→(N,σ) overv
relative toA is a forward morphismλ:N→M overv such that the diagram
M
ρ
∼=
//
λ

SqB/A(M)
Sqv/A(λ)

N σ
∼=
// SqC/A(N)
in D(B) is commutative.
These functorialities of the squaring operation are hard to prove. An imprecise
study of them was made in the papers [188] and [189]. A correct treatment of the
trace functoriality can be found in the paper [173]; and a correct treatment of the
étale functoriality will appear in [175].
Remark 13.4.23. The squaring operation is related toHochschild cohomology.
Assume for simplicity thatA is a ﬁeld andM is aB-module. Then for eachi the
cohomology
Hi(SqB/A(M)) = Exti
B⊗AB(B,M ⊗AM)
is thei-th Hochschild cohomology with values in theB-bimodule M⊗AM. For
more on this material see [14], [137] and [138].
Remark 13.4.24.It is possible to avoid the assumption thatB is ﬂat overA. This
is done by choosing a commutative DG ring˜B that is K-ﬂat as a DGA-module,
with a DG ring quasi-isomorphism ˜B→B overA. Such resolutions always exist
(see [188] or [173]). Then we take
(13.4.25) SqB/A(M) := RHom ˜B⊗A ˜B(B,M ⊗L
AM).
This was the construction used by Zhang and Yekutieli in the paper [188].
Unfortunately there was a serious error in [188]: we did not prove that for-
mula (13.4.25) is independent of the resolution˜B. This error was discovered, and
corrected, by L. Avramov, S. Iyengar, J. Lipman and S. Nayak in their paper [14].
There were ensuing errors in [188] regarding the functoriality of the squaring
operation in the ring B (as described in Remark 13.4.22). The paper [14] did
279
Derived Categories | Amnon Yekutieli | 14 Apr 2019
not treat such functoriality at all, and the constructions and proofs of the trace
functoriality were corrected only in our recent paper [173]. It is worthwhile to
mention that the correct proofs (both in [14] and [173]) rely onnoncommutative
DG ringsand DG bimodulesover them; and the squaring operation is replaced by
the rectangle operation.
Because the non-ﬂat case is so much more complicated, we have decided not to
reproduce it in the book. The interested reader can look up the research papers
[173], [175], [176] and [177], the survey article [168], or the lecture notes [174].
A general treatment of derived categories of bimodules, based on K-ﬂat DG ring
resolutions, will be in the paper [178].
