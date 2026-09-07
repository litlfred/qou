---
doc_id: arxiv-1312.6411v4
doc_title: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI"
section_id: sec-006-6-tilting-dg-modules
section_title: "Tilting DG Modules"
section_number: 6
pages: 30-35
source_pdf: 1312.6411v4.pdf
source_sha256: ceac22eb8ffe87e6
doc_brief: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI — We consider commutative DG rings (better known as nonpositive stronglycommutativeassociativeunitalDGalgebras)."
---
RecallthatallDGringsherearecommutative(Convention4.2). Inparticularall
rings are commutative.
Deﬁnition6.1. Let AbeaDGring. ADG A-module Piscalleda tiltingDGmodule
if there exists some DGA-module Q such thatP⊗L
A Q∼= A in D(A).
The DG module Q in the deﬁnition is called aquasi-inverse of P. Due to the
symmetryoftheoperation −⊗ L
A−, Qisalsotilting. Itiseasytoseethatthequasi-
inverse Qisunique,uptoanonuniqueisomorphism. If P1and P2aretiltingthenso
is P1⊗L
A P2;thisisbecauseoftheassociativityof −⊗ L
A−. Hencethenextdeﬁnition
makes sense.
Deﬁnition 6.2.The commutative derived Picard groupof A is the abelian group
DPic(A), whose elements are the isomorphism classes, inD(A), of tilting DGA-
modules. The product is induced by the operation−⊗ L
A−, and the unit element
is the class ofA.
Lemma 6.3. Let f : A→ B be a homomorphism of DG rings.
(1) For anyM, N∈ D(A) there is an isomorphism
(B⊗L
A M)⊗L
B (B⊗L
A N)∼= B⊗L
A (M⊗L
A N)
in D(A).
(2) If P is a tilting DGA-module, thenB⊗L
A P is a tilting DGB-module.
(3) If f is a quasi-isomorphism andQ is a tilting DGB-module, thenrest f (Q) is a
tilting DGA-module.
Proof. (1) Choose K-ﬂat resolutions˜M→ M and ˜N→ N over A. Then B⊗A ˜M
and B⊗A ˜N are K-ﬂat overB, ˜M⊗A ˜N is K-ﬂat overA, and
(B⊗L
A M)⊗L
B (B⊗L
A N)∼= (B⊗A ˜M)⊗B (B⊗A ˜N)
∼= B⊗A ( ˜M⊗A ˜N)∼= B⊗L
A (M⊗L
A N).
(2) LetP, Q∈ D(A) be such thatP⊗L
A Q∼= A. By (1) we have
(B⊗L
A P)⊗L
B (B⊗L
A Q)∼= B.
(3) SayQ1, Q2∈ D(B) satisfy Q1⊗L
B Q2∼= B. Let Pi := rest f (Qi)∈ D(A). By the
equivalence for DG ring quasi-isomorphisms (see [YZ1, Proposition 1.4]) we have
P1⊗L
A P2∼= rest f (Q1⊗L
B Q2)∼= rest f (B)∼= A.
□
Proposition 6.4. Let f : A→ B be a homomorphism of DG rings.
COMMUTATIVE DG RINGS 31
(1) There is a group homomorphism
DPic( f ) : DPic(A)→ DPic(B)
with formulaP↦→ B⊗L
A P.
(2) If f is a quasi-isomorphism thenDPic( f ) is bijective.
Proof. (1) This follows from parts (1) and (2) of the lemma above.
(2)Part(3)ofLemma6.3showsthatincase f isaquasi-isomorphism,thefunction
Q↦→ rest f (Q) is an inverse ofDPic( f ). □
Theorem 6.5. Let A be a DG ring andP∈ D(A). The following four conditions are
equivalent.
(i) The DGA-module P is tilting.
(ii) The functorP⊗L
A− is an equivalence ofD(A).
(iii) The functorRHomA(P,−) is an equivalence ofD(A).
(iv) TheDG A-module Pisperfect,andtheadjunctionmorphism A→ RHomA(P, P)
in D(A) is an isomorphism.
Proof. (i)⇒ (ii): LetQ be a quasi-inverse ofP. Then the functorG(M) := Q⊗L
A M
is a quasi-inverse of the functorF(M) := P⊗L
A M.
(ii)⇒ (i): The functorF := P⊗L
A− is essentially surjective on objects, so there is
some Q∈ D(A) such thatF(Q)∼= A. Then Q is a quasi-inverse ofP.
(ii)⇔ (iii): The functorsF := P⊗L
A− and G := RHomA(P,−) are adjoints, soF is
an equivalence iﬀG is an equivalence.
(ii)⇒(iv): Considertheauto-equivalence F := P⊗L
A−of D(A). SinceAiscompact
and P = F(A),itfollowsthat Piscompact. NowaccordingtoTheorem5.20,perfect
is the same as compact.
For any M∈ D(A), the adjunction morphismA→ RHomA(M, M) is an iso-
morphism iﬀ the canonical graded ring homomorphism
αM : H(A)→
⨁
k∈Z
HomD(A)(M, M[k])
is bijective. The equivalenceF induces a commutative diagram of graded rings
H(A)
αM

αF(M)
**⨁
k∈Z
HomD(A)(M, M[k]) F // ⨁
k∈Z
HomD(A)
(
F(M), F(M)[k]
)
in which the horizontal arrow is an isomorphism. Now takeM := A. Because αA
is an isomorphism, so isαP.
(iv)⇒ (i): DeﬁneQ := RHomA(P, A)∈ D(A). The implication (i)⇒ (iii) of Theo-
rem 5.20 shows that
Q⊗L
A P = RHomA(P, A)⊗L
A P∼= RHomA(P, P)∼= A
in D(A). So P is tilting, with quasi-inverseQ. □
Corollary 6.6. Let P be a tilting DG A-module. Then the DG A-module Q :=
RHomA(P, A) is a quasi-inverse ofP.
Proof. This was shown in the proof of the implication (iv)⇒ (i) above. □
32 AMNON YEKUTIELI
Remark 6.7. A DG A-module M for which the adjunction morphism A →
RHomA(M, M)isanisomorphism,issometimescalled semidualizing;cf.[AIL]. In-
deed,thisconditionispartofthedeﬁnitionofa dualizingDGmodule (seeDeﬁnition
7.1below). ButaswesawinTheorem6.5,thisconditionisalsocharacteristicoftilt-
ing DG modules – so the name semidualizing might be confusing.
Corollary6.8. Let PbeatiltingDG A-module,andlet F := P⊗L
A−bethecorresponding
auto-equivalence ofD(A).
(1) Thefunctor Fhasﬁnitecohomologicaldimension,anditpreserves D+(A), D−(A)
and Db(A).
(2) If A is cohomologically pseudo-noetherian, then the auto-equivalenceF preserves
the subcategoryDf(A).
Proof. (1) The theorem says thatP is perfect. Let s1, . . . , sn ∈ ¯A and P1, . . . , Pn
be as in Deﬁnition 5.1. Letd0≤ d1 be integers such that eachPi is generated in
theintegerinterval [d0, d1]. Thenthefunctor F hascohomologicaldisplacementat
most [d0, d1] relative toD(A), and cohomological dimension at mostd1− d0. The
claim aboutD⋆(A) is now clear.
(2) Use Theorem 2.13(2), noting thatF(A) = P∈ D−
f (A), by Theorems 6.5 and
5.11. □
Proposition6.9. Let AbeaDGring,andlet e = ( e1, . . . , en)beanidempotentcovering
sequenceof ¯A = H0(A). Forany iwehavethelocalizedDGring Ai = Aei fromDeﬁnition
4.5, and the DG ring homomorphismλi : A→ Ai. Then the group homomorphisms
DPic(λi) : DPic(A)→ DPic(Ai)
induce a group isomorphism
DPic(A) ≃− →
n
∏
i=1
DPic(Ai).
Proof. (1) According to Proposition 4.22 there is a DG ring quasi-isomorphismλ :
A→ ∏n
i=1 Ai. By Proposition 6.4(2) there is a group isomorphism
DPic(λ) : DPic(A) ≃− →DPic
(
∏
n
i=1 Ai
)
.
And there is an obvious group isomorphism
DPic
(
∏
n
i=1 Ai
)
∼=
n
∏
i=1
DPic(Ai).
□
From here to Theorem 6.13 we consider a ringA. The ﬁrst lemma goes back to
[RD, Lemma V.3.3], and it reappeared, in a noncommutative guise, in [Ye2] and
[RZ]. But inthe priortreatments the ringA was assumedto benoetherian. There-
fore we give a full proof of the general case.
Lemma 6.10. Let A be a local ring, and letP be a tilting DGA-module. Then P∼= A[k]
in D(A) for some integerk.
Proof. Since P is a perfect complex ofA-modules (Theorem 6.5), it is isomorphic
in D(A) to a bounded complex of ﬁnite projectiveA-modules. Say con(H(P)) =
[i0, i1] for some integersi0≤ i1. By replacing P with such a resolution, and then
splittingoﬀextratermsinhighandlowdegrees,wecanassumethat Pisacomplex
of ﬁnite projectiveA-modules, concentrated in the degree interval[i0, i1]. Then
P′ := Hi1 (P) is a nonzero ﬁnitely presentedA-module.
COMMUTATIVE DG RINGS 33
Let Q be a quasi-inverse ofP. By the same reasoning, we can assume thatQ is
a complex of ﬁnite projectiveA-modules, concentrated in a degree interval[j0, j1],
and Q′ := Hj1 (Q) is a nonzero ﬁnitely presentedA-module.
Now by the Künneth trick we have isomorphisms ofA-modules
P′⊗A Q′∼= Hi1+j1 (P⊗L
A Q)∼= Hi1+j1 (A).
On the other handP′⊗A Q′⁄= 0, by Nakayama. The conclusion is thati1 + j1 = 0
and P′⊗A Q′ ∼= A. This tells us that P′ and Q′ are ﬂatA-modules. Again by
Nakayama, we see thatP′∼= Q′∼= A.
Finally, we can split the complexesP and Q into P∼= P′[−i1]⊕ Pex and Q∼=
Q′[−j1]⊕ Qex, where Pex and Qex are complexes of ﬁnite projectiveA-modules,
concentrated in the degree intervals[i0, i1− 1] and [j0, j1− 1] respectively. Then
H(Pex⊗A Q′[−j1])isadirectsummandofthegradedmodule H(P⊗L
A Q)∼= H(A).
Since H(Pex⊗A Q′[−j1])isconcentratedintheinterval [i0 + j1,−1],itmustbezero.
So Pex = 0 in D(A), andP∼= P′[−i1]. □
Recallthatan A-module Piscalled invertibleifitisprojectiveofrank 1. Inother
words, ifP is locally free of rank1. See [Bo, Section II.5.2, Theorem 1].
Proposition 6.11. The following conditions are equivalent for anA-module P :
(i) P is invertible.
(ii) When viewed as a DG module,P is tilting.
Proof. Theimplication(i) ⇒(ii)istrivial. Fortheotherdirection: theargumentsin
theﬁrstparagraphoftheproofofLemma6.10showthat Pisaﬁnitelypresented A-
module. Takeanyprimeideal p. ByLemma6.3,theDG Ap-module Pp := Ap⊗A P
istilting. Hence,byLemma6.10,wehave Pp∼= Ap. Accordingto[Bo,SectionII.5.2,
Theorem 1] the moduleP is invertible. □
Lemma 6.12. Let A be a ring, and letP be a tilting DGA-module. WriteX := Spec A,
and for any integeri deﬁne the set
Yi :={p∈ X| Hi(P)p⁄= 0}.
Then:
(1) Only ﬁnitely many of theYi are nonzero.
(2) Yi∩ Yj = ∅ if i⁄= j.
(3) X =⋃
i Yi.
(4) For anyi, the setYi is open-closed.
Proof. We may assume thatA ⁄= 0, i.e. that X ⁄= ∅. This implies that P ⁄= 0.
We know from Theorem 6.5 thatP is a perfect complex ofA-modules. Therefore
the cohomologyH(P) is bounded, and thuscon(H(P)) = [ i0, i1] for some integers
i0≤ i1. This proves claim (1).
Take any primep∈ X. By Lemma 6.3 the DGAp-module Pp := Ap⊗A P is
tilting. So by Lemma 6.10 we havePp ∼= Ap[k] for some integerk. We see that
p∈ Y−k, andp /∈ Yi for i⁄=−k. This proves claims (2) and (3).
It remains to prove claim (4). By induction oni1− i0 = amp(H(P)), it suﬃces
to prove thatY′ := Yi1 is open-closed inX. The reason is this: once we know that
Y′ is open-closed, then so is its complementY′′ :=⋃
i0≤i<i1 Yi. So X = Y′ ∐ Y′′ as
schemes, and correspondinglyA = A′× A′′ as rings, andP∼= P′⊕ P′′ in D(A).
But amp(H(P′′)) < i1− i0.
As explained in the proof of Lemma 6.10, we can assume thatP is a complex
of ﬁnite projectiveA-modules, concentrated in the degree interval[i0, i1]. So Q :=
Hi1 (P) is a ﬁnitely presentedA-module. Because Y′ is the support of the module
Q, it is closed inX.
34 AMNON YEKUTIELI
Take a primep ∈ Y′. As we have already seen above, theAp-module Qp is
isomorphic to Ap. According to [Bo, Section II.5.1, Corollary] there is an open
neighborhood U of p in X such that Qq ∼= Aq for all q ∈ U. This shows that
U⊂ Y′. ThereforeY′ is open inX. □
For a ringA we have the following theorem, due to Negron [Ng]. It is a re-
ﬁnement of earlier results, that are due (independently) to the author [Ye2] and to
Rouquier-Zimmermann [RZ]. The earlierresults focused on noetherian rings, and
hence there was an assumption thatSpec A has ﬁnitely many connected compo-
nents. Negron recently noticed that this assumption is superﬂuous.
Asusual, Pic(A)denotesthe(commutative)Picardgroupof A,whoseelements
are the isomorphism classes of invertibleA-modules.
The abelian groupFlc(Spec A, Z) was introduced in Deﬁnition 4.18. As shown
in Proposition 4.19, each functionf ∈ Flc(Spec A, Z) determines a decomposi-
tion A = ∏n
i=1 Ai of the ringA, and a nondecreasing sequence of integersk =
(k1, . . . , kn). The relation is this:f (Spec Ai) = ki.
Theorem 6.13. Let A be a commutative ring. There is a canonical group isomorphism
DPic(A)∼= Pic(A)× Flc(Spec A, Z) ,
characterized as follows:
• Thehomomorphism Pic(A)→ DPic(A)sendstheclassofaninvertible A-module
P to its class as a tilting DGA-module.
• Let f ∈ Flc(Spec A, Z), with corresponding ring decompositionA = ∏n
i=1 Ai
and integer sequence(k1, . . . , kn). The tilting DG A-module associated to f is⨁n
i=1 Ai[ki].
Proof. For an invertibleA-module Q and a functionf∈ Flc(Spec A, Z) let
G(Q, f ) := Q⊗A
(⨁n
i=1 Ai[ki]
)
,
whichisatiltingDG A-module. Wehavetoprovethatthegrouphomomorphism
Pic(A)× Flc(Spec A, Z)→ DPic(A)
induced byG is bijective. It is certainly injective: ifG(Q, f )∼= A, then f must be
the constant function0, as can be checked inDPic(Ap) for eachp∈ Spec A. But
then Q∼= A in D(A), which implies thatQ∼= A in Mod A.
It remains to prove that the group homomorphism induced byG is surjective.
TakeanytiltingDG A-module P. LetSpec A = ∐i1
i=i0
Yi bethedecompositioninto
open-closed sets induced byP, from Lemma 6.12. Consider the locally constant
function f : X → Z deﬁned byf|Yi := i. Then the tilting DG moduleQ :=
P⊗L
A G(A, f ) has the property thatHi(Q) = 0 for alli⁄= 0. By Proposition 6.11
we know thatQ is isomorphic to an invertibleA-module, say Q′. But then P∼=
G(Q′,− f ). □
Let Abeanoetherianring, a-adicallycompletewithrespecttosomeideal a,with
reduction ¯A := A/a. Itisknownthatthegrouphomomorphism Pic(A)→ Pic( ¯A)
is bijective. For a proof see [Ha, Exercises II.9.6 and III.4.6].
ThenexttheoremisaDGanalogueofthisfact. RecallthatforaDGring Athere
is a canonical homomorphismA→ ¯A.
Theorem 6.14. Let A be a commutative DG ring. Then the canonical group homomor-
phism
DPic(A)→ DPic( ¯A)
is bijective.
COMMUTATIVE DG RINGS 35
Proof. Let us denote byπ : A→ ¯A the canonical DG ring homomorphism. We
begin by proving that the homomorphismDPic(π) is injective. Suppose P is a
tiltingDG A-modulesuchthat ¯A⊗L
A P∼= ¯Ain D( ¯A). ByCorollary6.8(1)weknow
that P∈ D−(A). Then Proposition 3.3(1) says thatP∼= A in D(A).
Nowletusprovethat DPic(π)issurjective. TakeanytiltingDG ¯A-module ¯P. By
Theorem6.13thereisanisomorphism ¯P∼= G( ¯P0, f )forsomeinvertible ¯A-module
¯P0 and some functionf∈ Flc(Spec A, Z).
By Proposition 3.5, there exists some DG module P0 ∈ D−(A) such that
¯A⊗L
A P0∼= ¯P0 in D( ¯A). Let ¯Q0∈ Mod ¯Abeaquasi-inverseoftheinvertiblemodule
¯P0. Bythesamereason,thereexists Q0∈ D−(A)suchthat ¯A⊗L
A Q0∼= ¯Q0 in D( ¯A).
Now by Lemma 6.3(1) we have
¯A⊗L
A (P0⊗L
A Q0)∼= ¯P0⊗L
¯A
¯Q0∼= ¯A
in D( ¯A). SinceP0⊗L
A Q0∈ D−(A),byProposition3.3(1)weknowthat P0⊗L
A Q0∼=
A in D(A). This shows thatP0 is a tilting DGA-module.
Finally, lete = ( e1, . . . , en) and k = ( k1, . . . , kn) be the data corresponding tof
from Proposition 4.19, and letA→ ∏n
i=1 Ai be thee-induced decomposition ofA
from Deﬁnition 4.25. Consider the tilting DGA-module
P := P0⊗A
(⨁n
i=1 Ai[ki]
)
.
Then ¯P∼= ¯A⊗L
A P. □
Corollary 6.15. Let A be a DG ring. There is a canonical group isomorphism
DPic(A)∼= Pic( ¯A)× Flc(Spec ¯A, Z) .
Proof. Combine Theorems 6.14 and 6.13. □
Deﬁnition 6.16.Let A be a DG ring. We deﬁneDPic0(A) to be the subgroup of
DPic(A) that corresponds toPic( ¯A), under the canonical group isomorphism of
Corollary 6.15.
Corollary 6.17. If ¯A is a local ring, thenDPic(A)∼= Z.
Proof. Weknowthat Pic( ¯A)istrivial,and Spec ¯Aisconnected. NowuseCorollary
6.15. □
