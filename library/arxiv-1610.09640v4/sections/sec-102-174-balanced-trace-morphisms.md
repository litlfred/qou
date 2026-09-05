---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-102-174-balanced-trace-morphisms
section_title: "Balanced Trace Morphisms"
section_number: 17.4
pages: 402-411
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
15.1.17 and 15.2.1.
Deﬁnition 17.4.1.A graded ring homomorphismf : A→B is calledﬁniteif it
makesB into a ﬁnite gradedA-module on both sides.
Throughout this subsection we assume the next setup:
Setup 17.4.2. We are given noetherian connected gradedK-rings A and B, with
augmentationideals mand nrespectively, andaﬁnitegradedK-ringhomomorphism
f :A→B. We are also given a homomorphism of gradedK-rings g :C→D.
The ringsC andD will play auxiliary roles, to allow us to handle bimodules. In
practice C will be eitherA or K, andD will be eitherB or K. The graded ring
homomorphism f⊗gop :A⊗Cop→B⊗Dop induces a restriction functor
Rest = Restf⊗gop : D(B⊗Dop, gr)→D(A⊗Cop, gr).
This restriction functor will often remain implicit.
Theorem 17.4.3. Assume Setup17.4.2.
(1) There is a canonical morphism
Rest◦RΓ n→RΓ m◦Rest
of triangulated functorsD(B⊗Dop, gr)→D(A⊗Cop, gr).
(2) Let N ∈D(B⊗Dop, gr), and assume either thatN ∈D+(B⊗Dop, gr)
or that the functorΓ m has ﬁnite right cohomological dimension. Then the
canonical morphism RΓ n(N)→RΓ m(N) in D(A⊗Cop, gr) is an isomor-
phism.
For the proof we need a few lemmas.
Lemma 17.4.4. For everyN∈M(B⊗Dop, gr) there is equalityΓ m(N) = Γ n(N)
of (B⊗Dop)-submodules ofN.
Proof. Take any integerq≥1, and letmq := m···m, theq-fold power of the ideal
m. BecauseB is a ﬁniteA-module, it follows thatB/(mq·B)∼= (A/mq)⊗AB is a
ﬁnite module overA/mq, and hence it is a ﬁniteK-module. This implies that the
graded moduleB/(mq·B) is concentrated in a ﬁnite algebraic degree interval, say
[0,i 1]. Soforevery i>i 1 thereisequality (mq·B)i =Bi. Takingq′:= max(q,i 1+1)
we get nq′
⊆mq·B.
The argument above shows that for everyq≥1 there exists someq′≥q for
which nq′
⊆mq·B. Trivially there is an inclusion mq·B⊆nq. These inclusions
yield
HomB(B/nq′
,N )⊆HomA(A/mq,N )⊆HomB(B/nq,N )⊆N.
Combined with formula (16.3.5) the assertion is proved. □
Recall the ML condition from Deﬁnition 11.1.5. An inverse system{Nq}q∈N in
M(K, gr) is said to have thetrivial ML property, or is calledprozero, if for every
q there is someq′≥q such that the homomorphismNq′→Nq is zero. See [158,
Deﬁnition 3.5.6].
Lemma 17.4.5. Let{Nq}q∈N be an inverse system inM(K, gr) that has the ML
property. The following are equivalent:
(i) The inverse system has the trivial ML property.
(ii) lim←qNq = 0.
Lemma 17.4.6.Let{Nq}q∈N be an inverse system inM(A, gr) that has the trivial
ML property, and letM∈M(A, gr). Then limq→HomA(Nq,M ) = 0.
402
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Exercise 17.4.7. Prove Lemmas 17.4.5 and 17.4.6.
For a ﬁnite gradedA-module M, and for numbersp,q∈N, we deﬁne
(17.4.8) Fp,q(M) := TorA
p (A/mq+1,M ) = H−p(
(A/mq+1)⊗L
AM
{
∈M(A, gr).
Then, ﬁxingp, we deﬁne
(17.4.9) Fp(M) := lim←qFp,q(M)∈M(A, gr).
In this way we obtain functors
(17.4.10) Fp,q,Fp : Mf(A, gr)→M(A, gr).
Lemmas 17.4.11 and 17.4.15 below are essentially [159, Lemma 6.4 and Propo-
sition 6.5].
Lemma 17.4.11. Let M be a ﬁnite gradedA-module and letp≥1. Then the
inverse system{Fp,q(M)}q∈N has the trivial ML property.
Proof.
Step 1. Here we show that for ﬁxedp, the inverse system{Fp,q(M)}q∈N satisﬁes
the ML condition.
Because A is left noetherian andM is a ﬁnite gradedA-module, we can ﬁnd a
resolution···→L−1→L0→M→0 in M(A, gr), such that eachL−p is a ﬁnite
graded-free A-module. Then
Fp,q(M) = H−p(
(A/mq+1)⊗L
AM
{∼= H−p(
(A/mq+1)⊗AL
{
isaﬁnite (A/mq+1)-module. Soasagraded A-moduleitisartinian. Forﬁxed q, and
for allq′≥q, the descending chain condition on the submodulesIm
(
Fp,q′(M)→
Fp,q(M)
{
⊆Fp,q(M)tellsusthatthiseventuallystabilizes. ThisistheMLproperty.
Step 2. Let0→M′→M→M′′→0 be a short exact sequence inMf(A, gr). For
eachq we have a long exact Tor sequence
(17.4.12)
···→F1,q(M′)→F1,q(M)→F1,q(M′′)
→F0,q(M′)→F0,q(M)→F0,q(M′′)→0
Asq varies, these long exact sequences form an inverse system. By step 1 we know
that in every position the ML property is satisﬁed. Therefore by Theorem 11.1.7,
applied in each degree separately, i.e. to the inverse systems inM(K), the inverse
limit
(17.4.13)
···→F1(M′)→F1(M)→F1(M′′)
→F0(M′)→F0(M)→F0(M′′)→0
is an exact sequence.
Step 3. For a ﬁxed degreek, we have(mq+1·M)k = 0 whenq≫0. This is because
M is a ﬁnite gradedA-module, and thus it is bounded below in algebraic degree.
It follows that the canonical homomorphismMk→(M/mq+1·M)k is bijective for
q≫0. Going to the limit inq we see that the canonical homomorphism
M→F0(M) = lim←qF0,q(M) = lim←q(M/mq+1·M)
is bijective. Therefore there is an isomorphism of functorsF0∼= Id. We deduce
that F0 is an exact functor onMf(A, gr).
Step 4. We now prove, by induction onp, that the functorFp is zero for every
p≥1.
403
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Given a moduleM ∈Mf(A, gr), we choose a surjectionL↠ M from a ﬁnite
graded-free moduleL. We get a short exact sequence0→N→L→M→0 in
Mf(A, gr). Hence, by step 2, there is a long exact sequence
(17.4.14)
···→F2(N)→F2(L)→F2(M)
δ1
−→F1(N)→F1(L)→F1(M)
δ0
−→F0(N)→F0(L)→F0(M)→0
in M(A, gr); cf. the exact sequence (17.4.13). NowFp,q(L) = 0 for allq≥0 and all
p> 0, becauseL is ﬂat; so in the limit we getFp(L) = 0 for allp> 0.
Since the functorF0 is exact (by step 3), we see thatδ0 = 0. Also we have
F1(L) = 0. ThereforeF1(M) = 0.
But M was an arbitrary object ofMf(A, gr), so in fact the functorF1 is zero.
This implies that in the exact sequence (17.4.14) we haveF1(N) = 0. We also have
F2(L) = 0. This implies thatF2(M) = 0. And so on. This ﬁnishes the proof that
Fp = 0 for allp≥1.
Step 5. Take someM ∈Mf(A, gr). We know thatFp(M) = 0 for everyp≥1.
By step 1 we also know that for everyp inverse system{Fp,q(M)}q∈N has the ML
property. Lemma 17.4.5 says that for everyp≥1 the inverse system{Fp,q(M)}q∈N
has the trivial ML property. □
Lemma 17.4.15. If J is a graded-injectiveB-module, then as anA-module,J is
graded-m-ﬂasque.
Proof. Take somep> 0. We have to show thatRpΓ m(J) = 0. Now
RpΓ m(J)∼= lim
q→
Extp
A
(
A/mq+1,J ).
But
Extp
A
(
A/mq+1,J ) = Hp(
RHomA(A/mq+1,J )
{
.
By derived Hom-tensor adjunction we have a canonical isomorphism
RHomA(A/mq+1,J )∼= RHomB
(
B⊗L
A (A/mq+1),J
{
.
in D(A, gr). BecauseJ is graded-injective, we have
RHomB
(
B⊗L
A (A/mq+1),J
{∼= HomB
(
B⊗L
A (A/mq+1),J
{
,
and also
Hp(
HomB
(
B⊗L
A (A/mq+1),J
{∼= HomB
(
H−p(
B⊗L
A (A/mq+1)
{
,J
{
∼= HomB
(
TorA
p (B,A/ mq+1),J
{
.
Putting it all together we get
RpΓ m(J)∼= lim
q→
HomB
(
Fp,q(B),J
{
,
where Fp,q(B) := Tor A
p (B,A/ mq+1), like in formula (17.4.8). Now B is a ﬁnite
Aop-module. According to Lemma 17.4.11, applied to the ringAop instead ofA,
the inverse system{Fp,q(M)}q∈N has the trivial ML property. By Lemma 17.4.6
we see thatlimq→HomB
(
Fp,q(B),J
{
= 0. □
Proof of Theorem17.4.3.
(1) For a complexN∈D(B⊗Dop, gr) we choose a K-injective resolutionρ:N→J
in Cstr(B⊗Dop, gr). Then we choose a K-injective resolutionσ:J→I in Cstr(A⊗
Cop, gr). (We are hiding the restriction functorRest here.) So σ◦ρ: N→I is a
K-injective resolution inCstr(A⊗Cop, gr). We get presentationsRΓ n(N) = Γ n(J)
and RΓ m(N) = Γ m(I). By Lemma 17.4.4 there is equalityΓ m(J) = Γ n(J). The
404
Derived Categories | Amnon Yekutieli | 14 Apr 2019
morphism RΓ n(N)→RΓ m(N) in D(A⊗Cop), gr) we are looking for is the one
represented by the homomorphismΓ m(σ) : Γ n(J) = Γ m(J)→Γ m(I) in Cstr(A⊗
Cop, gr). It does not depend on the choices made.
(2) Now we choose the K-injective resolutionρ:N→J in Cstr(B⊗Dop, gr) more
carefully: we take the semi-graded-cofree resolution from Theorem 15.3.4(2). Then
thecomplex J isK-injectivein C(B⊗Dop, gr), eachJp isinjectivein M(B⊗Dop, gr),
and inf(J) = inf(H(N)). According to Lemma 17.4.15,J is a complex of graded-m-
ﬂasque modules. By Lemma 16.1.5, under either of the two conditions, the complex
J is graded-m-ﬂasque. Therefore the homomorphismΓ m(σ) : Γ m(J)→Γ m(I) in
Cstr(A⊗Cop, gr) is a quasi-isomorphism. □
Corollary 17.4.16. If the functor Γ m has ﬁnite right cohomological dimension,
then the functorΓ n has ﬁnite right cohomological dimension.
Proof. Part 2 of Theorem 17.4.3 implies that the right cohomological dimension of
Γ n is at most the right cohomological dimension ofΓ m. □
Corollary 17.4.17. If the ringA satisﬁes the leftχcondition, then so does the
ring B.
Proof. A graded B-module N is ﬁnite iﬀ it is ﬁnite as a gradedA-module, and
the same for coﬁniteness. LetN∈Mf(B, gr). By Proposition 16.5.17 the graded
A-modules Hp
m(N) are all coﬁnite. But by part 2 of Theorem 17.4.3 we know
that Hp
n(N)∼= Hp
m(N) as graded A-modules. So the graded B-modules Hp
n(N)
are all coﬁnite. Again using Proposition 16.5.17 we see thatB satisﬁes the leftχ
condition. □
Corollary 17.4.18.If the ringA has a balanced dualizing complex(RA,βA), then
the ringB has a balanced dualizing complex(RB,βB).
Proof. According to Corollary 17.3.24,A satisﬁes theχcondition, and it has ﬁnite
local cohomological dimension. Corollaries 17.4.16 and 17.4.17, applied to the ﬁnite
graded ring homomorphismsA→B and Aop→Bop, tell us thatB satisﬁes theχ
condition, and it has ﬁnite local cohomological dimension. Again using Corollary
17.3.24, now in the reverse direction, we conclude thatB has a balanced dualizing
complex. □
The graded ring homomorphismf : A→B induces, by applying the functor
(−)∗= HomK(−,K), a homomorphismf∗:B∗→A∗in M(Aen, gr).
Deﬁnition 17.4.19.Under Setup 17.4.2, assumeA andB have balanced dualizing
complexes (RA,βA) and (RB,βB) respectively. A balanced trace morphism is a
morphism
trf = trB/A :RB→RA
in D(Aen, gr), such that the diagram
RΓ m(RB)
RΓm(trf) //
βB ∼=

RΓ m(RA)
βA∼=

B∗ f∗
//A∗
in D(Aen, gr) is commutative. Here we use the canonical isomorphismRΓ n(RB)
∼= RΓ m(RB) from Theorem 17.4.3(2).
In Subsection 12.6 we studied backward morphisms for objects in derived cat-
egories. This makes sense also for complexes of graded bimodules. Namely, given
complexes M ∈D(A⊗Cop, gr) and N ∈D(B⊗Dop, gr), we can talk about a
405
Derived Categories | Amnon Yekutieli | 14 Apr 2019
backward morphismθ:N→M in D(A⊗Cop, gr). The backward morphismθin-
duces two morphisms by adjunction. First there is the morphismbadjR
A(θ) : N→
RHomA(B,M ) in D(B⊗Cop, gr); this is thederived backward adjunction morphism
on theA side. The second isbadjR
Cop(θ) :N→RHomCop(D,M ) in D(A⊗Dop, gr);
this is thederived backward adjunction morphism on theCop side. The construc-
tions are just like those in Theorem 12.6.12(2), but now using the graded bimodule
resolutions from Subsection 15.3.
Deﬁnition 17.4.20. Consider a backward morphism θ : N →M in
D(A⊗Cop, gr).
(1) θis called anondegenerate backward morphism on theA side if the mor-
phism badjR
A(θ) is an isomorphism.
(2) θis called anondegenerate backward morphism on theCop side if the mor-
phism badjR
Cop(θ) is an isomorphism.
(3) θis said to be anondegenerate backward morphism on both sidesif it is
nondegenerate both on theA side and on theCop side.
Example 17.4.21. The backward morphism f∗: B∗→A∗in D(Aen, gr) is a
nondegenerate backward morphism on both sides.
Theorem 17.4.22. The following hold in the situation of Deﬁnition17.4.19.
(1) There exists a unique balanced trace morphismtrf :RB→RA.
(2) The balanced trace morphismtrf is a nondegenerate backward morphism
on both sides.
We shall need several lemmas for the proof. In analogy to Deﬁnition 16.4.2, the
dedualizing complex ofB is PB := RΓ n(B)∼= RΓ nop(B) in D(Ben, gr).
Lemma 17.4.23. There are canonical isomorphismsPB∼= B⊗L
APA and PB∼=
PA⊗L
AB in D(B⊗Aop, gr) and D(A⊗Bop, gr) respectively.
Proof. According to Theorems 17.4.3(2) and 16.4.3 there are isomorphismsPB =
RΓ n(B)∼= RΓ m(B)∼=PA⊗L
AB in D(A⊗Bop, gr). The same theorems, but applied
totheoppositerings, giveusisomorphisms PB∼= RΓ nop(B)∼= RΓ mop(B)∼=B⊗L
APA
in D(B⊗Aop, gr). □
Like Deﬁnition 16.6.30, the abstract derivedn-adic completion functor is
ADCn := RHomB(PB,−) : D(B⊗Dop, gr)→D(B⊗Dop, gr).
Lemma 17.4.24. For N ∈D(B⊗D, gr) there is an isomorphism ADCn(N)∼=
ADCm(N) in D(A⊗Dop, gr). It is functorial inN.
Proof. We have isomorphisms
ADCn(N) = RHomB(PB,N )∼=1 RHomB(B⊗L
APA,N )
∼=2 RHomA(PA,N ) = ADCm(N)
in D(A⊗Dop, gr). The isomorphism ∼=1 comes from Lemma 17.4.23, and the
isomorphism∼=2 is by adjunction. □
In the next lemma we takeC =D :=K.
Lemma 17.4.25. Let N∈D+
f (B, gr), letM∈D+
f (A, gr), and letθ:N→M be
a backward morphism inD(A, gr). The following conditions are equivalent:
(i) θis a nondegenerate backward morphism on theA side.
(ii) The morphism RΓ m(θ) : RΓ m(N)→RΓ m(M) in D(A, gr) is a nondegen-
erate backward morphism on theA side.
406
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. Let us choose bounded below injective resolutionsN→J and M→I in
Cstr(B, gr) and Cstr(A, gr) respectively. Then the backward morphismθis repre-
sented by a homomorphism˜θ:J→I in Cstr(A, gr).
The morphismbadjR
A(θ) :N→RHomA(B,M ) in D(B, gr) is represented by the
homomorphism badjA(˜θ) : J→HomA(B,I ) in Cstr(B, gr). The formula for it it
this: badjA(˜θ)(j)(b) = ˜θ(b·j) forj∈J andb∈B. Now HomA(B,I ) is a K-graded-
injective complex overB, by adjunction. By Lemma 17.4.15 the complexesJ and
HomA(B,I ) are graded-m-ﬂasque. So the morphism
RΓ m
(
badjR
A(θ)
{
: RΓ m(N)→RΓ m
(
RHomA(B,M )
{
is represented by
(17.4.26) Γ m(badjA(˜θ)) : Γ m(J)→Γ m
(
HomA(B,I )
{
.
The morphism RΓ m(θ) is represented by the homomorphismΓ m(˜θ) : Γ m(J)→
Γ m(I). Since the complex Γ m(I) is K-graded-injective over A (by stability, see
Theorem 16.3.25), it follows thatbadjR
A
(
RΓ m(θ)
{
is represented by
(17.4.27) badjA(Γ m(˜θ)) : Γ m(J)→HomA(B, Γ m(I)).
A calculation, using the fact thatB is a ﬁniteA-module, shows that
(17.4.28) Γ m
(
HomA(B,I )
{
= HomA
(
B, Γ m(I)
{
as subcomplexes ofHomA(B,I ). Let us consider the diagram
(17.4.29) Γ m(J)
badjA(Γm(˜θ))//
Γm(badjA(˜θ))
((
HomA
(
B, Γ m(I)
{
=

⊆
))
Γ m
(
HomA(B,I )
{ ⊆ // HomA(B,I )
in Cstr(A, gr). It is commutative: the triangle on the right is just the equality
(17.4.28). And an element j ∈Γ m(J) goes by all paths to the homomorphism
b↦→˜θ(b·j) in HomA(B,I ).
Passing to the derived category, (17.4.29) gives the commutative diagram
(17.4.30) RΓ m(N)
badjR
A(RΓm(θ)) //
RΓm(badjR
A(θ))
**
RHomA
(
B, RΓ m(M)
{
∼=

RΓ m
(
RHomA(B,M )
{
in D(A, gr).
Since bothN and RHomA(B,M ) belong to D+
f (A, gr), by Lemma 17.3.31 they
belongto D+(A, gr)com. ByTheorem 16.6.32 (theMGM Equivalence) we know that
the morphism badjR
A(θ) is an isomorphism if and only if the morphism
RΓ m(badjR
A(θ)) is an isomorphism. Diagram (17.4.30) says that this happens if
and only if badjR
A
(
RΓ m(θ)
{
is an isomorphism. Going back to the deﬁnition, we
conclude thatθis nondegenerate if and only ifRΓ m(θ) is nondegenerate. □
Proof of Theorem17.4.22.
(1) According to Theorems 17.3.19 and 17.2.4 there is an isomorphism RA ∼=
(PA)∗∼= ADCm(A∗) in D(Aen, gr). The same theorems, together with Lemma
17.4.24 (taking C := A and D := B), say that RB ∼= (PB)∗∼= ADCn(B∗) ∼=
ADCm(B∗) in D(Aen, gr).
407
Derived Categories | Amnon Yekutieli | 14 Apr 2019
The equivalence in Corollary 17.3.36 says that there are isomorphisms
(17.4.31) RΓ m(RB)∼= (RΓ m◦ADCm)(B∗)∼=B∗
and
(17.4.32) RΓ m(RA)∼= (RΓ m◦ADCm)(A∗)∼=A∗
in D(Aen, gr). And that there is a unique morphismθ: RB→RA in D(Aen, gr)
such that the diagram
(17.4.33) RΓ m(RB)
RΓm(θ) //
∼=

RΓ m(RA)
∼=

B∗ f∗
//A∗
in D(Aen, gr), in which the vertical isomorphisms are (17.4.31) and (17.4.32), is
commutative.
But to get a balanced trace morphismtrf we need a commutative diagram like
(17.4.33) in which the vertical isomorphisms areβB and βA respectively. Because
the automorphisms ofA∗and B∗in D(Aen, gr) are multiplication by nonzero ele-
ments ofK, there is a uniquec∈K×such thattrf :=c·θ:RB→RA is a balanced
trace morphism.
(2) To see thattrf is a nondegenerate backward morphism on theA side we can
forget theAop-structure. So we can viewtrf as a backward morphismtrf :RB→
RA in D(A, gr). Now RΓ m(trf) = β−1
A ◦f∗◦βB. In Example 17.4.21 we saw that
f∗:B∗→A∗is a nondegenerate backward morphism inD(A, gr). The morphisms
βA and βB are isomorphisms. Therefore
RΓ m(trf) : RΓ m(RB)→RΓ m(RA)
is a nondegenerate backward morphism inD(A, gr). According to Lemma 17.4.25
the morphism trf is a nondegenerate backward morphism inD(A, gr).
As for theAop side: the symmetry from Corollary 17.3.35 gives isomorphisms
RA∼= ADCmop(A∗) and RB ∼= ADCmop(B∗) in D(Aen, gr). Going over the con-
structions in the proof of item (1) above, we see that there is equalityRΓ mop(trf) =
d·β−1
A ◦f∗◦βB for somed∈K×. Therefore RΓ mop(trf) is a nondegenerate back-
ward morphismD(Aop, gr). Now Lemma 17.4.25, transcribed to the ringAop, says
that trf is a nondegenerate backward morphism inD(Aop, gr). □
Corollary 17.4.34. Let A
f
− →B
g
− →C be ﬁnite homomorphisms inRnggr/cK,
and assume these rings have balanced dualizing complexes(RA,βA), (RB,βB) and
(RC,βC) respectively. Thentrg◦f = trf◦trg as morphismsRC→RA in D(Aen, gr).
Proof. The follows from the uniqueness in Theorem 17.4.22 and the fact that(g◦
f)∗=f∗◦g∗as homomorphismsC∗→A∗in M(A, gr). □
We end this subsection with a partial converse to Corollaries 17.4.16 and 17.4.17.
Recall that a central elementa∈A is calledregular if it is not a zero divisor, i.e.
the only elementb∈A such thata·b = 0 is b = 0.
Theorem 17.4.35.LetA be a noetherian connected graded ring, and leta∈A be a
regular homogeneous central element of positive degree. Deﬁne the connected graded
ring B :=A/(a). IfB satisﬁes theχcondition and it has ﬁnite local cohomological
dimension, thenA also satisﬁes theχcondition and it has ﬁnite local cohomological
dimension.
This is [10, Theorem 8.8]. The original proof does not use derived categories,
and is quite diﬀerent from the proof below.
408
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. By op-symmetry it suﬃces to prove thatA satisﬁes the leftχcondition and
that the functorRΓ m has ﬁnite cohomological dimension.
Letd∈N be the local cohomological dimension ofB, and leti≥1 be the degree
of the elementa. In view of Propositions 16.5.17 and 16.3.19, all we need to prove
is that the following two conditions hold for everyM∈Mf(A, gr) :
(i) Hp
m(M) is a coﬁniteA-module for everyp.
(ii) Hp
m(M) = 0 for everyp>d + 1.
Let us denote the augmentation ideal ofB by n. The short exact sequence
0→A
a·(−)
− −−− →A(i)→B(i)→0 in M(Aen, gr) is viewed as a distinguished triangle
A
a·(−)
− −−− →A(i)→B(i)
∆
−−→in D(Aen, gr). Applying the functor(−)⊗L
AM to it, we
obtain a distinguished triangle
(17.4.36) M
a·(−)
− −−− →M(i)→N
∆
−−→
in D(A, gr), where by deﬁnitionN :=B(i)⊗L
AM∈D(B, gr). Note that Hp(N)∈
Mf(B, gr) for allp, and Hp(N) = 0 unless−1≤p≤0.
Next we apply the functorRΓ m to (17.4.36), and use Theorem 17.4.3, to obtain
this distinguished triangle
(17.4.37) RΓ m(M)
a·(−)
− −−− →RΓ m(M(i))→RΓ n(N)
∆
−−→
in D(A, gr). Taking cohomologies in (17.4.37) we obtain this exact sequence
(17.4.38) Hp−1
n (N)→Hp
m(M)
a·(−)
− −−− →Hp
m(M(i))→Hp
n(N)
in M(A, gr). Let use write
Kp := Ker
(
Hp
m(M)
a·(−)
− −−− →Hp
m(M(i))
{
⊆Hp
m(M).
Since a∈m, there is an inclusion
(17.4.39) Soc
(
Hp
m(M)
{
= HomA
(
K, Hp
m(M)
{
⊆Kp.
For p > d+ 1 we have Hp−1
n (N) = 0 and Hp
n(N) = 0 . The exact sequence
(17.4.38) says that the homomorphisma·(−) : Hp
m(M)→Hp
m(M(i)) is bijective.
So Kp = 0, and by (17.4.39) we see thatSoc
(
Hp
m(M)
{
= 0. But Hp
m(M) is an
m-torsion module, so according to Proposition 16.3.12 we getHp
m(M) = 0. This
establishes condition (ii).
Finally take anyp. By theχcondition forB and by Proposition 16.5.17 we know
that Hp−1
n (N) is a coﬁnite gradedB-module; and thus it is a coﬁnite gradedA-
module. According to the NC Graded Matlis Duality (Theorem 15.2.34) the coﬁnite
graded A-modules are the artinian objects in the abelian categoryM(A, gr). From
the exact sequence (17.4.38) we obtain a surjectionHp−1
n (N)→Kp. ThereforeKp
is a coﬁnite gradedA-module. The inclusion (17.4.39) says that Soc
(
Hp
m(M)
{
is
a coﬁnite gradedA-module; and thus it is a ﬁnite gradedK-module. Hence, by
Corollary 16.3.13, Hp
m(M) is a coﬁnite gradedA-module. This is condition (i).□
409
Derived Categories | Amnon Yekutieli | 14 Apr 2019
