---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-091-153-resolutions-and-derived-functors
section_title: "Resolutions and Derived Functors"
section_number: 15.3
pages: 338-345
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
Conventions 15.1.17 and 15.2.1. ThusK is a base ﬁeld and⊗=⊗K. In the next
deﬁnitions we collect the algebraically graded versions of some deﬁnitions from
Sections 10 and 11.
Deﬁnition 15.3.1.Let A be a graded ring, and letP∈C(A, gr).
(1) The complexP is called agraded-free complexif all the gradedA-modules
Pi are graded-free, and the diﬀerential is zero.
(2) The complexP is called asemi-graded-free complexif it admits a ﬁltration
{Fj(P )}j≥−1 in Cstr(A, gr), such that F−1(P ) = 0 , P = 
jFj(P ), and
GrF
j (P ) is a graded-free complex for everyj.
(3) The complexP is called aK-graded-projective complexif for every acyclic
complex N∈C(A, gr), the complexHomA(P,N ) is acyclic.
Deﬁnition 15.3.2.Let A be a graded ring, and letI∈C(A, gr).
(1) The complexI is called agraded-cofree complexif all theA-modules Ip are
graded-cofree, and the diﬀerential is zero.
(2) The complexI is called asemi-graded-cofree complexif it admits a coﬁl-
tration{Fq(I)}q≥−1 in Cstr(A, gr), such thatF−1(I) = 0, each GrF
q (I) is
graded-cofree complex, andI = lim←qFq(I).
(3) The complex I is called a K-graded-injective complexif for every acyclic
complex N∈C(A, gr), the complexHomA(N,I ) is acyclic.
Deﬁnition 15.3.3.A complexP ∈C(A, gr) is called aK-graded-ﬂat complexif
for every acyclic complexN∈C(Aop, gr) the complexN⊗AP is acyclic.
Theorem 15.3.4. LetA be a graded ring, and letM∈C(A, gr).
(1) There exists a quasi-isomorphismρ:P→M in Cstr(A, gr), whereP is a
semi-graded-free complex, andsup(P ) = sup(H(M)).
(2) There exists a quasi-isomorphismρ: M→I in Cstr(A, gr), whereI is a
semi-graded-cofree complex, andinf(I) = inf(H(M)).
Proof.
(1) This is a modiﬁcation of Theorem 11.4.17 and Corollary 11.4.27. The proof is
the same, after a few obvious modiﬁcations.
(2) This is a modiﬁcation of Theorem 11.6.24 and Corollary 11.6.31. The proof is
the same, after a few obvious modiﬁcations. The injective objectK∗we use here is
K∗:=K of course. □
The various kinds of complexes mentioned in the deﬁnitions above are related
as follows.
Theorem 15.3.5. LetA be a graded ring.
(1) A complexP∈C(A, gr) is K-graded-projective if and only if it is isomorphic
in K(A, gr) to a semi-graded-free complexQ.
(2) If P∈C(A, gr) is K-graded-projective, then it is K-graded-ﬂat.
(3) If P∈C(A, gr) is K-graded-projective, thenP∗∈C(Aop, gr) is K-graded-
injective.
(4) A complexI∈C(A, gr) is K-graded-injective iﬀ it is isomorphic inK(A, gr)
to a semi-graded-cofree complexJ.
Proof.
(1)ByTheorem11.4.14, thatappliestothiscontexttoo, asemi-graded-freecomplex
Q is K-graded-projective. And by Proposition 10.2.3, a complexP∈C(A, gr) is K-
graded-projective iﬀHomK(A,gr)(P,N ) = 0 for every acyclic complexN∈C(A, gr).
338
Derived Categories | Amnon Yekutieli | 14 Apr 2019
First let’s assume that there is an isomorphismP ∼= Q in K(A, gr) to a semi-
graded-free complexQ. Then for every acyclic complexN∈C(A, gr) we get
HomK(A,gr)(P,N )∼= HomK(A,gr)(Q,N ) = 0.
Therefore P is K-graded-projective.
Conversely, let’s assume thatP is K-graded-projective. By Theorem 15.3.4(1)
there is a quasi-isomorphism ρ: Q→P in Cstr(A, gr) from a semi-graded-free
complex Q. By Corollary 10.2.14,P(ρ) :Q→P is an isomorphism inK(A, gr).
(2) TakeN∈C(Aop, gr). We have the adjunction isomorphism
(N⊗AP )∗= HomK(N⊗AP,K)
∼= HomA(P, HomK(N,K)) = HomA(P,N∗)
in Cstr(K, gr). IfN is acyclic then so areN∗, HomA(P,N∗) and (N⊗AP )∗. Since
the functor (−)∗is faithfully exact, we see thatN⊗AP is acyclic too. Therefore
P is K-graded-ﬂat.
(3) TakeN∈C(Aop, gr). We have the adjunction isomorphism
HomAop(N,P∗) = HomAop(N, HomK(P,K))
∼= HomK(N⊗AP,K) = (N⊗AP )∗
in Cstr(K, gr). By item (2)P is K-graded-ﬂat. IfN is acyclic then so areN⊗AP,
(N⊗AP )∗and HomAop(N,P∗). ThereforeP∗is K-graded-injective.
(4) By Theorem 11.6.21, that applies to this context too, a semi-graded-cofree com-
plex J is K-graded-injective. And by Proposition 10.1.3, a complexI∈C(A, gr) is
K-graded-injective iﬀHomK(A,gr)(N,I ) = 0 for every acyclic complexN∈C(A, gr).
First let’s assume that there is an isomorphismI ∼= J in K(A, gr) to a semi-
graded-cofree complexJ. Then for every acyclic complexN∈C(A, gr) we get
HomK(A,gr)(N,I )∼= HomK(A,gr)(N,J ) = 0.
Therefore I is K-graded-injective.
Conversely, let’sassumethatI isK-graded-injective. ByTheorem15.3.4(2)there
is a quasi-isomorphismρ:I→J in Cstr(A, gr) to a semi-graded-cofree complexJ.
By Corollary 10.1.19,P(ρ) :I→J is an isomorphism inK(A, gr). □
The next proposition tells us that some resolving properties of complexes are
preserved by the restriction functorC(A⊗B, gr)→C(A, gr).
Proposition 15.3.6. LetA and B be graded rings.
(1) If P ∈C(A⊗B, gr) is K-graded-projective, then it is K-graded-projective
in C(A, gr).
(2) If P∈C(A⊗B, gr) is K-graded-ﬂat, then it is K-graded-ﬂat inC(A, gr).
(3) If I∈C(A⊗B, gr) is K-graded-injective, then it is K-graded-injective in
C(A, gr).
Proof.
(1) TakeN∈C(A, gr). We have isomorphisms
HomA(P,N )∼= HomA⊗B(P, HomA(A⊗B,N ))
∼= HomA⊗B(P, HomK(B,N ))
in Cstr(K, gr). As an object ofC(K, gr), B is K-graded-projective. Hence, ifN is
acyclic, then so isHomA(P,N ).
(2, 3) Like item (1), but using the fact thatB is K-graded-ﬂat overK, and using
other adjunction isomorphisms. □
Corollary 15.3.7. LetA and B be graded rings, and letM∈C(A⊗B, gr).
339
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(1) There exists a quasi-isomorphismP→M in Cstr(A⊗B, gr), whereP is a
K-graded-projective complex overA, everyPi is a graded-projective module
over A, and sup(P ) = sup(H(M)).
(2) There exists a quasi-isomorphismP→M in Cstr(A⊗B, gr), whereP is
a K-graded-ﬂat complex overA, everyPi is a graded-ﬂat module overA,
and sup(P ) = sup(H(M)).
(3) There exists a quasi-isomorphismM →I in Cstr(A⊗B, gr), where I is
a K-graded-injective complex overA, everyIp is a graded-injective module
over A, and inf(I) = inf(H(M)).
Proof.
(1) Take the resolutionP →M from Theorem 15.3.4(1). In view of Theorem
15.3.5(1), Proposition 15.3.6(1) and Proposition 15.2.6(2), the complexP has the
required properties.
(2) Use item (1), plus Theorem 15.3.5(2).
(3) Take the resolutionM→I from Theorem 15.3.4(2). This will do, by Theorem
15.3.5(4), Proposition 15.3.6(3), Proposition 15.2.11(3) and Proposition 15.2.13(3).
□
Corollary 15.3.8. LetA, B and C be graded rings.
(1) The triangulated right derived bifunctor
RHomA(−,−) : D(A⊗Bop, gr)op×D(A⊗Cop, gr)→D(B⊗Cop, gr)
exists.
(2) Let M∈D(A⊗Bop, gr) and N∈D(A⊗Cop, gr). Assume that eitherM
is K-graded-projective overA, orN is K-graded-injective overA. Then the
morphism
ηR
M,N : HomA(M,N )→RHomA(M,N )
in D(B⊗Cop, gr) is an isomorphism.
(3) Let B′→B and C′→C be gradedK-ring homomorphisms. Then the
diagram
D(A⊗Bop, gr)op×D(A⊗Cop, gr)
RHomA(−,−) //
Rest×Rest

D(B⊗Cop, gr)
Rest

D(A⊗B′op, gr)op×D(A⊗C′op, gr)
RHomA(−,−) // D(B′⊗C′op, gr)
is commutative up to isomorphism.
Proof. The same arguments used in the proof of Proposition 14.3.15 work here,
because there exist enough acyclic resolutions – see Corollary 15.3.7. □
Corollary 15.3.9.The categoryD(A, gr) has inﬁnite direct sums. On objects, the
direct sum is degreewise, for theZ2 grading.
Proof. The proof of Theorem 10.1.26 works here. □
Corollary 15.3.10. LetA, B and C be graded rings.
(1) The triangulated left derived bifunctor
(−⊗L
A−) : D(B⊗Aop, gr)×D(A⊗Cop, gr)→D(B⊗Cop, gr)
exists.
340
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(2) LetM∈D(B⊗Aop, gr) andN∈D(A⊗Cop, gr). Assume that eitherM is
K-graded-ﬂat overAop, orN is K-graded-ﬂat overA. Then the morphism
ηL
M,N :M⊗L
AN→M⊗AN
in D(B⊗Cop, gr) is an isomorphism.
(3) Let B′→B and C′→C be gradedK-ring homomorphisms. Then the
diagram
D(B⊗Aop, gr)×D(A⊗Cop, gr)
(−⊗L
A−) //
Rest×Rest

D(B⊗Cop, gr)
Rest

D(B′⊗Aop, gr)×D(A⊗C′op, gr)
(−⊗L
A−) // D(B′⊗C′op, gr)
is commutative up to isomorphism.
Proof. The same arguments used in the proof of Proposition 14.3.13 work here,
because there exist enough acyclic resolutions – see Corollary 15.3.7. □
Corollary 15.3.11. LetA, B and C be graded rings.
(1) Given M∈M(A⊗Bop, gr) and N∈M(A⊗Cop, gr), for everyp∈N there
is a canonical isomorphism
Extp
A(M,N )∼= Hp(
RHomA(M,N )
{
in M(B⊗Cop, gr). Here Extp
A(−,−) is the classical p-th right derived
bifunctor of HomA(−,−).
(2) Given M∈M(B⊗Aop, gr) and N∈M(A⊗Cop, gr), for everyp∈N there
is a canonical isomorphism
TorA
p (M,N )∼= H−p(
M⊗L
AN
{
in M(B⊗Cop, gr). Here TorA
p (−,−) is the classicalp-th left derived bi-
functor of (−⊗A−).
Proof. This is clear from Corollary 15.3.8(2) and Corollary 15.3.10(2) respectively.
□
Corollary 15.3.12. LetA, B, C and D be graded rings.
(1) Let L∈D(A⊗Bop, gr), M ∈D(B⊗Cop, gr) and N ∈D(C⊗Dop, gr).
There is an isomorphism
L⊗L
B (M⊗L
CN)∼= (L⊗L
BM)⊗L
CN
in D(A⊗Dop, gr). This isomorphism is functorial inL,M,N .
(2) Let L∈D(B⊗Aop, gr), M ∈D(C⊗Bop, gr) and N ∈D(C⊗Dop, gr).
There is an isomorphism
RHomB
(
L, RHomC(M,N )
{∼= RHomC(M⊗L
BL,N )
in D(A⊗Dop, gr). This isomorphism is functorial inL,M,N .
Proof. Both assertions are immediate consequences of the associativity of the tensor
product for modules, and the Hom-tensor adjunction for modules. □
The triangulated category D(Aen, gr) has a biclosed monoidal structure on it,
with monoidal operation(−⊗L
A−) and monoidal unitA. See Remark 14.3.23 for
the nongraded variant. In the next deﬁnition we present the pertinent operations
related to this structure; these will be needed for several constructions. We do
not need to know anything about the concept of monoidal structure beyond this
terminology. The interested reader can look it up in [102]; the previous corollaries
(almost) guarantee that the monoidal axioms hold in this context.
341
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 15.3.13(Monoidal Operations). LetA andB be graded rings, and let
M∈D(A⊗Bop, gr) and N∈D(B⊗Aop, gr) be complexes.
(1) The left unitor isomorphism forM is the obvious isomorphismlu : A⊗L
A
M
≃
− →M in D(A⊗Bop, gr).
(2) The right unitorisomorphism forN is the obvious isomorphismru :N⊗L
A
A
≃
− →N in D(B⊗Aop, gr).
(3) The left co-unitor isomorphism for M is the obvious isomorphism lcu :
RHomA(A,M )
≃
− →M in D(A⊗Bop, gr).
Here is a notion that is dual to a minimal complex of injectives (see Deﬁnition
13.2.5). Recallthatforacomplex P, themoduleofdegree icoboundariesis Bi(P ) =
Im
(
di−1
P :Pi−1− →Pi{
⊆Pi.
Deﬁnition 15.3.14.Let A be a connected graded ring, with augmentation ideal
m. A minimal complex of graded-freeA-modules is a bounded above complexP,
such that for everyi the graded modulePi is graded-free, and there is an inclusion
Bi(P )⊆m·Pi.
Proposition 15.3.15. Let A be a connected graded ring, and letP be a bounded
above complex of graded-freeA-modules. The following conditions are equivalent:
(i) P is a minimal complex of graded-freeA-modules.
(ii) The complexK⊗AP has zero diﬀerential.
Exercise 15.3.16. Prove this proposition.
Deﬁnition 15.3.17.Let A be a connected graded ring, and letM ∈M(A, gr).
A minimal graded-free resolutionof M is a quasi-isomorphism ρ: P →M in
Cstr(A, gr) from a minimal complex of graded-freeA-modules P.
Proposition 15.3.18. LetA be a connected graded ring, and letM∈M(A, gr) be
a bounded below graded module. Then:
(1) M has a minimal graded-free resolutionη:P→M.
(2) For everyi there is an isomorphismPi∼=A⊗TorA
−i(K,M ) in M(A, gr).
(3) The minimal graded-free resolutionη:P→M in item(1) above is unique,
up to a non-unique isomorphism inCstr(A, gr).
Proof.
(1) Let V0 := K⊗A M and P 0 := A⊗V0. By Proposition 15.2.30 there is a
surjection η: P 0 →M. Let M−1 := Ker(η)⊆P 0. By construction we have
M−1⊆m⊗V0 = m·P 0. And of courseM−1 is a bounded below gradedA-module.
Next letV1 := K⊗AM−1 and P−1 := A⊗V1. By Proposition 15.2.30 there
is a surjection d−1 : P−1→M−1. The graded moduleM−2 := Ker(d−1)⊆P−1
satisﬁesM−2⊆m⊗V1 = m·P−1. And so on.
(2) Due to minimality, the diﬀerential of the complexK⊗AP is zero; see Proposition
15.3.15. Therefore
TorA
−i(K,M )∼= Hi(K⊗L
AM)∼= Hi(K⊗AP )∼=K⊗APi∼=V−i.
(3) Supposeη′:P′→M is some other minimal graded-free resolution. BecauseP
and P′are K-projective in C(A, gr), there is a homotopy equivalenceφ: P→P′
in Cstr(A, gr). Therefore
(15.3.19) id⊗φ:K⊗AP→K⊗AP′
is a quasi-isomorphism. But by Proposition 15.3.15, these complexes have zero
diﬀerentials, so (15.3.19) is an isomorphism inCstr(K, gr). The graded Nakayama
Lemma (Proposition 15.2.30(3)) implies thatφ: P →P′is an isomorphism in
Cstr(A, gr). □
342
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Exercise 15.3.20. Try to generalize Proposition 15.3.18 to a complex M ∈
C(A, gr). The trick is to ﬁnd the correct boundedness conditions onM.
Corollary 15.3.21. AssumeA is a left noetherian connected graded ring, andM
is a ﬁnite gradedA-module. Then in the minimal graded-free resolutionη:P→M,
the graded-freeA-modulesPi are all ﬁnite.
Proof. In the proof of Proposition 15.3.18(1), the graded K-modules Vi are all
ﬁnite. □
Here is a graded version of Deﬁnitions 11.4.29 and 12.9.1.
Deﬁnition 15.3.22.Let A be a graded ring.
(1) A complex P ∈C(A, gr) is called pseudo-ﬁnite semi-graded-freeif it is a
bounded above complex of ﬁnite graded-freeA-modules.
(2) A complexL∈D(A, gr) is calledderived graded-pseudo-ﬁniteif it belongs
to the saturated full triangulated subcategory ofD(A, gr) generated by the
pseudo-ﬁnite semi-graded-free complexes.
Example 15.3.23. If the graded ringA is connected and left noetherian, then
the derived graded-pseudo-ﬁnite complexes overA are precisely the objects of
D−
f (A, gr). See Theorems 11.3.18 or 11.4.40.
Proposition 15.3.24. AssumeA is a left noetherian connected graded ring. Con-
sider A as a gradedAen-module. Then in the minimal graded-free resolutionρ:
P→A of A over Aen, the graded-freeAen-modulesPi are all ﬁnite.
The subtle point is that the graded ringAen might not be left noetherian – see
Remark 15.1.30.
Proof. Let us writePi∼=Aen⊗V−i, whereV−i∈M(K, gr). We shall prove that all
the V−i are ﬁnite gradedK-modules.
When we restrict the quasi-isomorphismρ:P→A to the categoryCstr(Aop, gr),
it becomes a homotopy equivalence. Henceτ:= ρ⊗id : P⊗AK→A⊗AK is
a quasi-isomorphism in Cstr(A, gr). Writing Q := P⊗AK∈C(A, gr), we get a
graded-free resolutionτ:Q→K overA. Note thatQi∼=A⊗V−i in Cstr(A, gr).
Now
(15.3.25) K⊗AQ∼=K⊗AP⊗AK∼=K⊗AenP
in Cstr(K, gr). Because P is a minimal complex of graded-freeAen-modules, the
complex K⊗Aen P has zero diﬀerential; see Proposition 15.3.15. But then the
complexK⊗AQ has zero diﬀerential. We conclude thatQ is a minimal complex of
graded-free A-modules, and henceτ: Q→K is a minimal graded-free resolution
overA. Corollary 15.3.21 says that the gradedA-modules Qi are ﬁnite; and hence
the gradedK-modules V−i are ﬁnite. □
Corollary 15.3.26. If A is a left noetherian connected graded ring, thenA is a
derived graded-pseudo-ﬁnite complex overAen.
Proof. This is an immediate consequence of Proposition 15.3.24, which says that
the complexP is pseudo-ﬁnite graded-semi-free overAen. □
Theorem 15.3.27. Let A, B, C and D be graded rings. For complexes L ∈
D(A⊗Cop, gr), M∈D(A⊗Bop, gr) and N∈D(B⊗Dop, gr) there is a morphism
evR,L
L,M,N : RHomA(L,M )⊗L
BN→RHomA(L,M⊗L
BN)
in D(C⊗Dop, gr), calledderived graded tensor-evaluation. The morphismevR,L
L,M,N
is functorial in the objectsL,M,N . Moreover, if all three conditions below hold,
then evR,L
L,M,N is an isomorphism.
343
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(i) The complexL is derived graded-pseudo-ﬁnite overA.
(ii) The complexM has bounded below cohomology.
(iii) The complexN has ﬁnite graded-ﬂat dimension overB.
Just to clarify, condition (ii) says thatHi(M) = 0 for i≪0. We do not care
about the boundedness (in algebraic degree) of the graded modulesHi(M).
Proof. The proof of just like that of Theorem 12.9.10, but working in the graded
derived categories. For condition (iii), notice that ifN has ﬁnite graded-ﬂat di-
mension overB, then there is an isomorphismP ∼= N in D(B, gr), whereP is a
bounded complex of graded-ﬂatB-modules. □
Deﬁnition 15.3.28.Let A be a graded ring.
(1) The full subcategory of D(A, gr) on the complexesM whose cohomology
modules Hp(M) belong to Mdwf(A, gr) is denoted byDdwf(A, gr).
(2) The full subcategory ofD(A, gr) on the complexes whose cohomology mod-
ules belong toMf(A, gr) is denoted byDf(A, gr).
(3) The full subcategory ofD(A, gr) on the complexes whose cohomology mod-
ules belong toMcof(A, gr) is denoted byDcof(A, gr).
Because Mdwf(A, gr) is a a thick abelian subcategory ofM(A, gr), it follows that
Ddwf(A, gr) is a full triangulated subcategory ofD(A, gr). Likewise for Df(A, gr)
whenA is left noetherian, and forDcof(A, gr) whenA is right noetherian connected.
Because (−)∗is exact, it induces a triangulated functor
(15.3.29) (−)∗: D(A, gr)op→D(Aop, gr).
Proposition 15.3.30. LetA be a graded ring.
(1) If M∈Ddwf(A, gr) then M∗∈Ddwf(Aop, gr).
(2) The functor
(−)∗: Ddwf(A, gr)op→Ddwf(Aop, gr)
is an equivalence ofK-linear triangulated categories.
(3) If A is left noetherian connected, then the functor
(−)∗: Df(A, gr)op→Dcof(Aop, gr)
is an equivalence ofK-linear triangulated categories.
Exercise 15.3.31. Prove this proposition. (Hint: use Proposition 15.2.28 and
Theorem 15.2.34.)
The next result is from [153].
Theorem 15.3.32. LetA, B and C be gradedK-rings.
(1) ForM∈D(A⊗Bop, gr) and N∈D(A⊗Cop, gr) there is a morphism
θM,N : RHomA(M,N )→RHomAop(N∗,M∗)
in D(B⊗Cop, gr), that is functorial inM and N.
(2) If M ∈Ddwf(A⊗Bop, gr) and N ∈Ddwf(A⊗Cop, gr) then θM,N is an
isomorphism.
Proof.
(1) Choose a K-graded-projective resolution ρ: P →M in Cstr(A⊗Bop, gr).
By Proposition 15.3.6 the complexP is K-graded-projective overA; so there is a
canonical isomorphism
φρ: RHomA(M,N )
≃
− →HomA(P,N )
in D(B⊗Cop, gr). K-linear duality gives a homomorphism
˜θP,N : HomA(P,N )→HomAop(N∗,P∗)
344
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in Cstr(B⊗Cop, gr).
Now ρ∗:M∗→P∗is a quasi-isomorphism inCstr(B⊗Aop, gr), and according
to Proposition 15.3.6(1) and Theorem 15.3.5(3) the the complexP∗is K-graded-
injective overAop. Therefore there is a canonical isomorphism
ψρ∗: HomAop(N∗,P∗)
≃
− →RHomAop(N∗,M∗)
in D(B⊗Cop, gr). The resulting morphism
θM,N :=ψρ∗◦Q(˜θP,N )◦φρ: RHomA(M,N )→RHomAop(M∗,N∗)
in D(B⊗Cop, gr) is functorial inM and N.
(2) Because the restriction functors between the derived categories are conservative
(see Proposition 14.3.10), we can forget the ringsB andC, and just considerθM,N
as a morphismD(K, gr).
For every integeri there is a canonical isomorphism
(15.3.33) Hi(
RHomA(M,N )
{∼= HomDdwf(A,gr)
(
M,N [i]
{
.
Using the isomorphismN∗[−i]∼=N[i]∗in D(Aop, gr) we also have
(15.3.34)
Hi(
RHomAop(N∗,M∗)
{∼= HomDdwf(Aop,gr)
(
N∗,M∗[i]
{
∼= HomDdwf(Aop,gr)
(
N[i]∗,M∗{
.
The construction ofθM,N in the proof of item (1) above shows that theK-linear
homomorphism
Hi(θM,N ) : Hi(
RHomA(M,N )
{
→Hi(
RHomAop(N∗,M∗)
{
becomes, after using the isomorphisms (15.3.33) and (15.3.34), the duality mor-
phism
HomDdwf(A,gr)
(
M,N [i]
{
→HomDdwf(Aop,gr)
(
N[i]∗,M∗{
.
According to Proposition 15.3.30(2) this is an isomorphism. □
Remark 15.3.35. In this section, and the two sections following it, we work over
a base ﬁeldK. This simpliﬁes a lot of the constructions. It is however possible to
relax this condition, and to work over a noetherian commutative base ringK that is
not a ﬁeld. But then there are (at least) two complications. The ﬁrst complication
is that we will have to ﬁx an injective cogeneratorK∗of M(K); cf. Subsection 11.6.
Matlis Duality will take the formM∗:= Hom K(M,K∗), and HomK(−,−) might
also involve continuity in a delicate way.
The second complication is that for the homological algebra to be eﬀective,
the gradedK-rings would have to beﬂat. The absence of ﬂatness poses serious
diﬃculties. This can be tackled usingK-ﬂat DG ring resolutions; and these DG
rings would have to be bigraded (with upper and lower indices, as explained in the
Subsection 15.1). This sort of resolution has not been studied yet, as far as we
know; but cf. [180] for some preliminary ideas.
