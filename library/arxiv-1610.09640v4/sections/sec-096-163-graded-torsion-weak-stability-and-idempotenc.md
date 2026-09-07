---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-096-163-graded-torsion-weak-stability-and-idempotenc
section_title: "Graded Torsion: Weak Stability and Idempotence"
section_number: 16.3
pages: 358-367
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
we begin the study of derived torsion over a connected graded ring. We adhere
to Conventions 15.1.17 and 15.2.1. ThusK is a ﬁeld, and all gradedK-rings are
algebraically graded centralK-rings. The symbol ⊗means⊗K. The enveloping
ring of a gradedK-ringA is the gradedK-ringAen =A⊗Aop. The category of left
algebraically gradedA-modules is M(A, gr), and it is aK-linear abelian category.
Its derived category isD(A, gr).
Recall the notion of left noetherian connected gradedK-ring from Deﬁnitions
15.1.29 and 15.2.18. In this subsection we will assume the following setup:
358
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Setup 16.3.1. We are given a left noetherian connected gradedK-ring A, with
augmentation idealm =⨁
i≥1Ai⊆A. We are also given gradedK-ringsB andC.
The graded ringsB andC are auxiliary – they are just placeholders, allowing us
to write more general formulas. For instance,M(A⊗Bop, gr) is M(Aen, gr) when
we takeB :=A, but it isM(A, gr) when B :=K.
Since A is left noetherian, the augmentation idealm is a ﬁnite graded leftA-
module.
We shall often make implicit use of the canonical isomorphisms
(16.3.2) A⊗AM
≃
− →M and HomA(A,M )
≃
− →M
in M(A⊗Bop, gr). There are similar canonical isomorphisms
(16.3.3) A⊗L
AM
≃
− →M and RHomA(A,M )
≃
− →M
in D(A⊗Bop, gr). Also we viewK∼= A/m as a gradedAen-module via the aug-
mentation ring homomorphismA→K.
We are interested in graded m-torsion. This makes sense for bimodules, and
hence the slightly complicated deﬁnition below.
Deﬁnition 16.3.4.Under Setup 16.3.1:
(1) LetM∈M(A⊗Bop, gr). An elementm∈M is called anm-torsion element
if mj·m = 0 for j≫0.
(2) The set ofm-torsion elements ofM is denoted byΓ m(M), and it is called
the m-torsion submoduleof M.
(3) We callM an m-torsion moduleif Γ m(M) =M.
(4) We denote byMtor(A⊗Bop, gr) the full subcategory ofM(A⊗Bop, gr) on
the m-torsion modules.
The fact that Γ m(M) is a graded (A⊗Bop)-submodule of M is easy to see.
Indeed, we can express the torsion submodule as follows:
(16.3.5) Γ m(M) = lim
j→
HomA(A/mj,M )⊆HomA(A,M ),
using the identiﬁcation (16.3.2), wherej≥1, mj is thej-fold product m···m⊆A,
A→A/mj+1→A/mj are the canonical graded ring surjections, and the operation
limj→is in the categoryM(A⊗Bop, gr).
It is clear that
Γ m : M(A⊗Bop, gr)→Mtor(A⊗Bop, gr)
is a linear functor, and the inclusionsΓ m(M)⊆M assemble into a monomorphism
σ: Γ m↣ Id of functors fromM(A⊗Bop, gr) to itself.
The ringB plays an auxiliary role in Deﬁnition 16.3.4. Because there is no men-
tion of torsion forBop-modules, the notationMtor(A⊗Bop, gr) is not ambiguous.
However, in Subsection 16.5, where torsion forBop modules does become an option,
we will switch to the richer notationM(tor,..)(A⊗Bop, gr). See Deﬁnition 16.5.5.
Lemma 16.3.6. Under Setup16.3.1 the following hold.
(1) The functorΓ m commutes with graded ring homomorphismsC→B, in the
sense that the diagram
M(A⊗Bop, gr)
Γm //
Rest

Mtor(A⊗Bop, gr)
Rest

M(A⊗Cop, gr)
Γm // Mtor(A⊗Cop, gr)
is commutative.
359
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(2) The functor Γ m is idempotent, in the sense that for every M ∈
M(A⊗Bop, gr) the homomorphisms
σΓm(M), Γ m(σM) : Γ m(Γ m(M))→Γ m(M)
are bijective and are equal to each other.
(3) Letφ:M→N be a homomorphism inM(A⊗Bop, gr), such thatM is m-
torsion. Then there is a unique homomorphismφ′:M→Γ m(N) satisfying
φ=σN◦φ′.
(4) The functor Γ m is left exact.
(5) The functor Γ m commutes with direct limits.
(6) The category Mtor(A ⊗Bop, gr) is a thick abelian subcategory of
M(A⊗Bop, gr), closed under taking subobjects and quotients.
Exercise 16.3.7. Prove Lemma 16.3.6. (Hint: for item (6) you will need the fact
that A is left noetherian.)
Recall that for a moduleM ∈M(A, gr), its socle is Soc(M) = Hom A(K,M ).
The socle is a functor, and there is a monomorphismSoc↣ Γ m of functors from
M(A, gr) to itself.
Lemma 16.3.8. LetM∈M(A, gr), and letW := Soc(M). If M is an m-torsion
module, thenW is a graded-essential submodule ofM.
Proof. Take any nonzero gradedA-submodule M′⊆M. Let m∈M′be some
nonzero homogeneous element. BecauseM is a torsion module, yetm⁄= 0, there
is a uniquej∈N such that mj+1·m = 0 but mj·m⁄= 0. So there is a homoge-
neous element a∈mj such that a·m⁄= 0. The element a·m is then a nonzero
homogeneous element inM′∩W. □
TheK-linear dual (see Deﬁnition 15.2.25) of the ringA is the graded bimodule
A∗= Hom K(A,K)∈M(Aen, gr). The augmentation ring homomorphismA→K
induces, by dualizing, a canonical monomorphism
(16.3.9) K↣A∗
in M(Aen, gr). For everyW∈M(K, gr) there is an induced monomorphism
(16.3.10) W∼=W⊗K↣W⊗A∗
in M(Aen, gr).
Lemma 16.3.11. Under Setup 16.3.1, let W ∈M(K, gr), and deﬁneI := A∗⊗
W∈M(A, gr). Consider the canonical monomorphismW↣ I in M(A, gr) from
(16.3.10). Then:
(1) I is a graded-injectiveA-module.
(2) I is an m-torsion A-module.
(3) W = Soc(I).
(4) W is a graded-essential submodule ofI.
Proof.
(1) SayW =⨁
x∈XK(−ix). Then I∼=⨁
x∈XA∗(−ix) in M(A, gr). According to
Proposition 15.2.5(2) and Theorem 15.2.17(1), the gradedA-module I is graded-
injective.
(2) TheA-module A∗is m-torsion, and a direct sum of torsion modules is torsion
(see Lemma 16.3.6(5)).
(3) This is becauseK = Soc(A∗), via the canonical monomorphism (16.3.9).
(4) Combine items (2) and (3) with Lemma 16.3.8. □
360
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proposition 16.3.12. Under Setup 16.3.1, let M ∈M(A, gr), and let W :=
Soc(M). The three conditions below are equivalent.
(i) M is an m-torsion gradedA-module.
(ii) W is a graded-essentialA-submodule ofM.
(iii) There is a graded-essential monomorphismϵ:M↣A∗⊗W in M(A, gr),
that restricts to the identity onW.
Proof.
(i)⇒(ii): This is Lemma 16.3.8.
(ii)⇒(iii): By Lemma 16.3.11 the gradedA-module A∗⊗W is graded-injective.
Hence there is a homomorphismϵ: M →A∗⊗W in M(A, gr) that makes the
diagram
W // //


M
ϵ
zz
A∗⊗W
in M(A, gr) commutative. Let M′:= Ker(ϵ). If M′were nonzero, then, because
W⊆M is a graded-essential submodule, we would haveW∩M′⁄= 0. But W→
A∗⊗W is a monomorphism. We conclude thatϵis a monomorphism too.
Finally, by Lemma 16.3.11(4) we know thatW is a graded-essential submodule
of A∗⊗W. It follows that the monomorphismϵis graded-essential.
(iii)⇒(i): The graded A-module A∗is torsion. We know that the subcategory
Mtor(A, gr) of M(A, gr) is closed under taking arbitrary direct sums and subobjects.
Hence M is m-torsion. □
Coﬁnite graded modules were deﬁned in Deﬁnition 15.2.33.
Corollary 16.3.13. Assume A is a noetherian connected graded ring. LetM ∈
Mtor(A, gr). The two conditions below are equivalent.
(i) M is a coﬁnite gradedA-module.
(ii) W := Soc(M) is a ﬁnite gradedK-module.
Proof. Graded Matlis Duality (Theorem 15.2.34) tells us that the coﬁnite graded
A-modules are the artinian objects in the abelian categoryM(A, gr).
(i)⇒(ii): We are given thatM is a coﬁnite gradedA-module. Hence so is its
submodule W. Since W is an A-module via K, it must be an artinian graded
K-module. SoW is ﬁnite overK.
(ii)⇒(i): Since A∗is a coﬁnite gradedA-module, andA∗⊗W is a ﬁnite direct
sum of degree twists ofA∗, we see thatA∗⊗W is a coﬁnite gradedA-module.
By Proposition 16.3.12 we know thatM is isomorphic to a graded submodule of
A∗⊗W; soM is also a coﬁnite gradedA-module. □
Remark 16.3.14. We do not know if the corollary remains true ifA is just left
noetherian.
Now we pass to derived categories and functors.
Deﬁnition 16.3.15.Under Setup 16.3.1, we denote byDtor(A⊗Bop, gr) the full
subcategory of D(A⊗Bop, gr) on the complexesM whose cohomology modules
Hp(M) belong to Mtor(A⊗Bop, gr) for allp.
Proposition 16.3.16. Under Setup16.3.1 the following hold.
361
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(1) The functor Γ m has a triangulated right derived functor
RΓ m : D(A⊗Bop, gr)→D(A⊗Bop, gr).
If I ∈D(A⊗Bop, gr) is K-graded-injective overA, then the morphism
ηR
I : Γ m(I)→RΓ m(I) is an isomorphism.
(2) There is a unique morphismσR : RΓ m→Id of triangulated functors from
D(A⊗Bop, gr) to itself, such that for everyM∈D(A⊗Bop, gr) there is
equalityσR
M◦ηR
M = Q(σM) of morphisms Γ m(M)→M in D(A⊗Bop, gr).
(3) The category Dtor(A⊗Bop, gr) is a full triangulated subcategory of
D(A⊗Bop, gr), and it contains the image of the functorRΓ m.
(4) The functor RΓ m commutes with gradedK-ring homomorphismsC→B,
in the sense that the diagram
D(A⊗Bop, gr)
RΓm //
Rest

Dtor(A⊗Bop, gr)
Rest

D(A⊗Cop, gr)
RΓm // Dtor(A⊗Cop, gr)
is commutative up to isomorphism. Likewise for the morphism of triangu-
lated functorsσR.
(5) For everyM∈D(A⊗Bop, gr) and p∈Z there is an isomorphism
Hp(RΓ m(M))∼= lim
j→
Extp
A(A/mj,M )
in M(A⊗Bop, gr). This isomorphism is functorial inM.
Proof. (1) By Corollary 15.3.8(3) everyM∈C(A⊗Bop, gr) has a resolutionρ:
M→I in Cstr(A⊗Bop, gr) by a complexI that is K-graded-injective overA. If
ψ:I→I′is a quasi-isomorphism inCstr(A⊗Bop, gr) between such complexes, then
itisahomotopyequivalencein Cstr(A, gr), andhence Γ m(ψ)isaquasi-isomorphism.
We see that the full subcategoryJ⊆K(A⊗Bop, gr) on these complexesI satisﬁes
the conditions of Theorem 8.4.9. Therefore the right derived functorRΓ m exists,
and ηR
I is an isomorphism for allI∈J.
(2) This is a special case of Lemma 16.2.5.
(3) Clear from Lemma 16.3.6(6).
(4) This is immediate from items (1) and (2).
(5) Use formula (16.3.5), and the fact that cohomology commutes with direct limits.
□
Deﬁnition 16.3.17.Under Setup 16.3.1, thei-th local cohomology functoris the
functor
Hi
m := RiΓ m : M(A⊗Bop, gr)→M(A⊗Bop, gr),
the i-th right derived functor ofΓ m.
Corollary 16.3.18. For everyi∈N there is an isomorphismHi
m∼= Hi◦RΓ m of
functors from M(A⊗Bop, gr) to itself.
Proof. This is immediate from Proposition 16.3.16(1). □
Proposition 16.3.19. For everyi∈N the functor
Hi
m : M(A⊗Bop, gr)→M(A⊗Bop, gr)
commutes with direct limits.
362
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. In view of Proposition 16.3.16(4), withC :=K, we can assume thatB =K,
so A⊗Bop = A. Since direct limits commute with each other, by Proposition
16.3.16(5) it suﬃces to prove that for everyi,j the functor Exti
A(A/mj,−) com-
mutes with direct limits. Now A is left noetherian, so we can ﬁnd a resolution
P →A/mj by a nonpositive complex, where eachPi is a ﬁnite graded-freeA-
module. And the functor
Exti
A(A/mj,−)∼= Hi◦HomA(P,−) : M(A, gr)→M(A, gr)
commutes with inﬁnite direct limits. □
Deﬁnition 16.1.2, when used in our context, says that the right cohomological
dimension of the functorΓ m is
(16.3.20) d := sup{p∈N|Hp
m⁄= 0}∈N∪{±∞}.
The cohomological dimension of a triangulated functor was introduced in Def-
inition 12.4.1. A triangulated functor is calledquasi-compact if it commutes with
inﬁnite direct sums (Deﬁnition 16.1.7).
Theorem 16.3.21. Under Setup 16.3.1, assume the torsion functor Γ m :
M(A, gr)→M(A, gr) has ﬁnite right cohomological dimension. Then the derived
torsion functor
RΓ m : D(A⊗Bop, gr)→D(A⊗Bop, gr)
is quasi-compact and has ﬁnite cohomological dimension.
Proof. According to Proposition 16.3.16(4), the functor
Γ m : M(A⊗Bop, gr)→M(A⊗Bop, gr)
also has ﬁnite right cohomological dimension. The right derived functors
RqΓ m = Hq
m : M(A⊗Bop, gr)→M(A⊗Bop, gr)
are quasi-compact by Proposition 16.3.19. So Theorem 16.1.10 applies. □
Lemma 16.3.22. Let I ∈M(A, gr), and let W := Soc(I). The following three
conditions are equivalent.
(i) I is graded-injective andm-torsion.
(ii) I is graded-injective andW is an essential submodule ofI.
(iii) There is an isomorphismI∼=A∗⊗W in C(A, gr) which is the identity on
W.
In condition (iii) we viewW as a submodule ofA∗⊗W using the canonical
embedding (16.3.10).
Proof.
(i)⇒(ii): This is Lemma 16.3.8.
(ii)⇒(iii): By Proposition 16.3.12 there is an essential monomorphismϵ: I→
A∗⊗W in M(A, gr) that extends the identity ofW. BecauseI is graded-injective,
the monomorphismϵis split, by some epimorphismσ:A∗⊗W→I. But W is a
graded-essential submodule ofA∗⊗W, and thereforeσis also a monomorphism.
We conclude that bothσand ϵare isomorphisms.
(iii)⇒(i): According to Lemma 16.3.11, the gradedA-module A∗⊗W is graded-
injective and m-torsion. □
Lemma 16.3.23. Let M ∈M(A, gr) be an m-torsion module, and let I be an
injective hull ofM in M(A, gr). ThenI∼=A∗⊗W, whereW is the socle ofM. In
particular,I is an m-torsion module.
363
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. By Proposition 16.3.12 there is a graded-essential monomorphismϵ:M↣
A∗⊗W in M(A, gr). From Lemma 16.3.11(1) we know thatA∗⊗W is a graded-
injective module overA. So by the uniqueness (up to isomorphism) of graded-
injective hulls, we get an isomorphismI∼=A∗⊗W. Finally, by Lemma 16.3.11(2),
A∗⊗W is m-torsion. □
Lemma 16.3.24. LetI be a graded-injectiveA-module. Then there is an isomor-
phism Γ m(I)∼=A∗⊗W in M(A, gr), whereW is the socle ofI.
Proof. Consider the essential monomorphism ϵ: W ↣ A∗⊗W from Lemma
16.3.11(4), and the monomorphism τ: W ↣ I. Because I is graded-injective,
there is a homomorphismψ:A∗⊗W→I in M(A, gr) such thatψ◦ϵ=τ. Since
ϵis a graded-essential monomorphism, the usual calculation (see the proof of the
implication (ii)⇒(iii) in Proposition 16.3.12) shows thatψis a monomorphism.
LetJ⊆I be the image ofψ, soψ:A∗⊗W
≃
− →J. We know (from Lemma 16.3.11)
thatJ is graded-injective andm-torsion. Hence there is a direct sum decomposition
I =J⊕J′in M(A, gr), and Γ m(J) =J.
By Proposition 16.3.12 we know thatW∩J′= Soc(J′) is a graded-essential
submodule of Γ m(J′); butW⊆J, soW∩J′= 0, and thereforeΓ m(J′) = 0. The
conclusion is thatΓ m(I) =J. □
Theorem 16.3.25. Under Setup16.3.1, the torsion functor
Γ m : M(A, gr)→M(A, gr)
is stable, namely for every graded-injectiveA-module I the m-torsion submodule
Γ m(I) is graded-injective.
Proof. This is immediate from Lemma 16.3.24 and Lemma 16.3.11(1). □
Here is the graded NC version of Deﬁnition 13.2.5.
Deﬁnition 16.3.26.
(1) A minimal complex of graded-injectiveA-modules is a bounded below com-
plex I of graded-injectiveA-modules, such that for everyp the submodule
Zp(I)⊆Ip is graded-essential.
(2) LetM∈D+(A, gr). Aminimal graded-injective resolutionofM is a quasi-
isomorphism ρ: M →I in Cstr(A, gr), where I is a minimal complex of
graded-injectiveA-modules.
Lemma 16.3.27. Let M ∈D+(A, gr). Then M has a minimal graded-injective
resolution.
Proof. The proof of Proposition 13.2.6 works here too. □
There is uniqueness for minimal graded-injective resolutions, but we won’t need
it.
For the next proposition, and for later results, it will be convenient to use this
notation:
Notation 16.3.28.If the torsion functorΓ m has ﬁnite right cohomological dimen-
sion, then we let⋆:=⟨empty⟩, the empty boundedness indicator; otherwise we let
⋆:= +. Thus D⋆is either D or D+.
Proposition 16.3.29. With Notation 16.3.28, let M ∈D⋆(A⊗Bop, gr). The
following conditions are equivalent:
(i) M∈D⋆
tor(A⊗Bop, gr).
(ii) The morphismσR
M : RΓ m(M)→M in D(A⊗Bop, gr) is an isomorphism.
364
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. The implication (ii)⇒(i) is due to Proposition 16.3.16(3).
For the other implication, we can forget the ringB; it is not relevant. First let
us assume thatM∈D+
tor(A, gr). By Lemma 16.3.23 the injective hull inM(A, gr)
of a torsion module is torsion. Then, according to Theorem 11.5.8, there is a quasi-
isomorphismM→I in C+
str(A, gr), whereI is a complex of torsion graded-injective
A-modules. It follows that homomorphism σI : Γ m(I)→I in C+
str(A, gr), that
representsσR
M, is an isomorphism.
When H(M) is not bounded below, butΓ m has ﬁnite right cohomological dimen-
sion, we can use smart truncation, as in the proof of Theorem 12.5.2(2). □
Proposition 16.3.30. With Notation 16.3.28, Let M ∈D⋆
tor(A⊗Bop, gr) and
N∈D+(A⊗Cop, gr). Then there is an isomorphism
RHomA(M,N )
≃
− →RHomA
(
M, RΓ m(N)
{
in D(B⊗Cop, gr), and it is functorial inM and N.
Proof. Choose a resolutionM→IM in C⋆
str(A⊗Bop, gr) where IM is K-graded-
injective overA, eachIp
M is graded-injective overA, and inf(IM) = inf(H((M));
this is possible by Corollary 15.3.7(3). Choose the same sort of resolutionN→IN
in C+
str(A⊗Cop, gr). Then
(16.3.31) RHomA(M,N )∼= HomA(IM,IN)
in D(B⊗Cop, gr), andRΓ m(N)∼= Γ m(IN) in D(A⊗Cop, gr). By Theorem 16.3.25
each Γ m(Ip
N) is graded-injective as anA-module, so Γ m(IN) is a bounded below
complex of graded-injective A-modules, and therefore it is a K-graded-injective
complex overA. We see that
(16.3.32) RHomA
(
M, RΓ m(N)
{∼= HomA
(
IM, Γ m(IN)
{
in D(B⊗Cop, gr).
By Proposition 16.3.29 (in both cases of Notation 16.3.28) the homomorphism
σIM : Γ m(IM)→IM is a quasi-isomorphism. Hence in the commutative diagram
HomA(IM,IN)
Hom(σIM,id)
// HomA
(
Γ m(IM),IN
{
HomA
(
IM, Γ m(IN)
{Hom(σIM,id)
//
Hom(id,σIN )
OO
HomA
(
Γ m(IM), Γ m(IN)
{
Hom(id,σIN )
OO
in Cstr(B⊗Cop, gr) the two horizontal arrows are quasi-isomorphisms. The right
vertical arrow is an isomorphism in Cstr(B⊗Cop, gr) by Lemma 16.3.6(3). It
follows that the left vertical arrow is a quasi-isomorphism. Combining this with the
isomorphisms (16.3.31) and (16.3.32) we obtain the desired isomorphism above.□
The next deﬁnition is a specialization of Deﬁnitions 16.1.3, 16.1.4 and 16.2.1.
Deﬁnition 16.3.33.Under Setup 16.3.1:
(1) A module N ∈M(A⊗Bop, gr) is called graded-m-ﬂasqueif it is a right
Γ m-acyclic object, i.e. ifHq
m(N) = 0 for allq >0.
(2) The functor
Γ m : M(A⊗Bop, gr)→M(A⊗Bop, gr)
is called weakly stable if for every graded-injective module I ∈
M(A⊗Bop, gr), the moduleΓ m(I)∈M(A⊗Bop, gr) is graded-m-ﬂasque.
(3) A complexN∈D(A⊗Bop, gr) is called aK-graded-m-ﬂasque complexif it
is a rightΓ m-acyclic complex, i.e. if the morphismηR
N : Γ m(N)→RΓ m(N)
in D(A⊗Bop, gr) is an isomorphism.
365
Derived Categories | Amnon Yekutieli | 14 Apr 2019
The term “ﬂasque” in this meaning seems to have been ﬁrst used in [190].
Example 16.3.34. Suppose M∈M(A, gr) is an m-torsion module. Consider its
minimal graded-injective resolution0→M→I0→I1→···. By Lemma 16.3.23
and induction onq, we see that all the graded modulesIq are m-torsion; in fact
Iq∼= A∗⊗Wq for someWq∈M(K, gr). Thus RΓ m(M)∼= Γ m(I) = I∼= M, so
RqΓ m(M) = 0 for allq >0, andM is a graded-m-ﬂasqueA-module.
Theorem 16.3.35. Under Setup16.3.1, the torsion functor
Γ m : M(A⊗Bop, gr)→M(A⊗Bop, gr)
is weakly stable.
Proof. Take an injective objectI ∈M(A⊗Bop, gr). According to Proposition
15.2.13(3), the moduleI is graded-injective overA. By Lemma 16.3.24 we know
that there is an isomorphism Γ m(I)∼= A∗⊗W in M(A, gr) for some gradedK-
module W. This is a graded-injectiveA-module, and thereforeΓ m(I) is graded-m-
ﬂasque as an object ofM(A, gr). Finally, by Proposition 16.3.16(4), the property
of being graded-m-ﬂasque is insensitive to the restriction functorM(A⊗Bop, gr)→
M(A, gr), so Γ m(I) is graded-m-ﬂasque as an object ofM(A⊗Bop, gr). □
In Proposition 16.3.16(2) we presented a morphismσR : RΓ m→Id of triangu-
lated functors fromD⋆(A⊗Bop, gr) to itself. Here we are using Notation 16.3.28.
According to Deﬁnition 16.2.3 the pair(RΓ m,σR) is a copointed triangulated func-
tor. Recall that (RΓ m,σR) is an idempotent copointed triangulated functor if for
every complexM∈D⋆(A⊗Bop, gr) the morphisms
σR
RΓm(M), RΓ m(σR
M) : RΓ m(RΓ m(M))→RΓ m(M)
in D(A⊗Bop, gr) are isomorphisms.
Corollary16.3.36 ([157]). With Notation16.3.28, the copointed triangulated func-
tor (RΓ m,σR) on D⋆(A⊗Bop, gr) is idempotent.
Proof. ByTheorem16.3.35thefunctor Γ m isweaklystable, andbyLemma16.3.6(2)
the copointed functor(Γ m,σ) is idempotent. Thus Theorem 16.2.8 applies. □
We end the subsection with an example showing a torsion functor as in Theorem
16.3.35 which is weakly stable but not stable. The example is a slight modiﬁcation
of an example in [157].
Example 16.3.37. Let A := K[t], the polynomial ring in a variablet of degree
1. It is connected noetherian, and its augmentation idealm is generated byt. Let
B :=K[s0,s 1,...], the commutative polynomial ring in countably many variables
s0,s 1,...of degree 1. So B is a graded ring, and it is not noetherian. Theorem
16.3.35 tells us that the functor
Γ m : M(A⊗B, gr)→M(A⊗B, gr)
is weakly stable. (SinceB is commutative, it doesn’t matter whether we writeB
or Bop). We will prove thatΓ m is not stable.
Consider a countable collection{Ip}p∈N of graded-injective B-modules. Then
I :=∏
p∈NIp(−p) is a graded-injectiveB-module, and thereforeJ := HomB(A⊗
B,I ) is a graded-injective(A⊗B)-module. If the functorΓ m on M(A⊗B, gr) were
stable, this would imply thatΓ m(J)is also a graded-injective(A⊗B)-module. Since
B→A⊗B is ﬂat,Γ m(J) is then a graded-injectiveB-module (see Proposition
15.2.13).
As gradedB-modules there are isomorphisms
A⊗B∼=
⨁
p∈N
B·tp∼=
⨁
p∈N
B(−p).
366
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Therefore
J = HomB(A⊗B,I )∼=

p∈N
I(p)
as gradedB-modules, and
Γ m(J)∼= lim
p→
(p
q=0
I(q)
{
∼=
⨁
p∈N
I(p).
Now for each p the graded-module Ip is a direct summand of I(p), and hence⨁
p∈NIp is a direct summand ofΓ m(J), as gradedB-modules. Therefore⨁
p∈NIp
is a graded-injectiveB-module.
The conclusion is that a countable direct sum of graded-injectiveB-modules is
graded-injective. According to the Bass-Papp Theorem [93, Theorem 3.46], that
holds also in the graded sense (cf. Proposition 15.1.26), the graded ringB is noe-
therian. This is a contradiction.
