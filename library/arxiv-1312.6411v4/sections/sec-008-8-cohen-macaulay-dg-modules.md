---
doc_id: arxiv-1312.6411v4
doc_title: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI"
section_id: sec-008-8-cohen-macaulay-dg-modules
section_title: "Cohen-Macaulay DG Modules"
section_number: 8
pages: 43-47
source_pdf: 1312.6411v4.pdf
source_sha256: ceac22eb8ffe87e6
doc_brief: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI — We consider commutative DG rings (better known as nonpositive stronglycommutativeassociativeunitalDGalgebras)."
---
In this section we work with cohomologically pseudo-noetherian commutative
DG rings (see Convention 4.2 and Deﬁnition 1.18).
Let A be such a DG ring. Recall that¯A = H0(A), andD0(A) is the full subcate-
gory ofD(A) consisting of the DG modulesM such thatHi(M) = 0 for alli⁄= 0.
Inside D0(A) we haveD0
f (A) = Df(A)∩ D0(A).
Lemma 8.1. Consider the canonical DG ring homomorphismπ : A→ ¯A. The functor
Q◦ restπ : Mod ¯A→ D0(A)
44 AMNON YEKUTIELI
is an equivalence. It restricts to an equivalence
Q◦ restπ : Modf ¯A→ D0
f (A).
Proof. Smart truncation shows that any object ofD0(A) is isomorphic to an object
of Mod ¯A. Finiteness of ¯A-modules is preserved. It remains to show thatQ◦ restπ
is a fully faithful functor.
So take M, N∈ Mod ¯A, and let ˜M→ M be a semi-free resolution overA with
sup( ˜M)≤ 0. Then
HomD(A)(M, N)∼= H0(
HomA( ˜M, N)
)∼= Hom ¯A(H0( ˜M), N)∼= Hom ¯A(M, N).
□
Deﬁnition 8.2.Let letR be a dualizing DGA-module. A DG moduleM∈ Db
f (A)
is calledCohen-Macaulay with respect toR if RHomA(M, R)∈ D0
f (A).
In other words, the condition is thatRHomA(M, R) is isomorphic, inD(A), to
an object ofModf ¯A. As usual “Cohen-Macaulay” is abbreviated to “CM”. Let us
denoteby Db
f (A)CM:R thefullsubcategoryof Db
f (A)consistingofDGmodulesthat
are CM w.r.t.R.
Remark 8.3. Observe that the functorRHomA(−, R) gives rise to a duality be-
tween Db
f (A)CM:R and D0
f (A). And the latter is equivalent toModf ¯A. Therefore
Db
f (A)CM:R is an artinian abelian category.
If A→ ¯A is not a quasi-isomorphism, thenA does not belong toD0(A), and
therefore R is not a CM DG module w.r.t. itself.
WedonotknowanydeﬁnitionofCohen-MacaulayDGrings;exceptwhen A→
¯Aisaquasi-isomorphism,inwhichcasetheconditionisthatthering ¯Ashouldbe
CM.
For a comparison to Cohen-Macaulay modules and Grothendieck’s notion of
Cohen-Macaulay complexes, see [YZ3, Theorem 6.2] and [YZ4, Section 7].
The groupsDPic0(A)⊆ DPic(A) were introduced in Deﬁnitions 6.2 and 6.16.
Lemma 8.4. Let P be a tilting DGA-module. The following are equivalent:
(i) The auto-equivalenceP⊗L
A− of D(A) preserves the subcategoryD0
f (A).
(ii) The class ofP is inDPic0(A).
Proof. (i)⇒(ii): Let ¯P := ¯A⊗L
A P. Byassumptionitbelongsto D0
f (A). Butthenthe
class of ¯P is inPic( ¯A) = DPic0( ¯A), so by deﬁnition the class ofP is inDPic0(A).
(ii)⇒ (i): Here ¯P := ¯A⊗L
A P is isomorphic to an invertible¯A-module, so ¯P⊗L
¯A−
preserves D0
f ( ¯A). Now take anyM∈ D0
f (A). By Lemma 8.1 we can assume that
M∈ Modf( ¯A). Then
P⊗L
A M∼= P⊗L
A ¯A⊗L
¯A M∼= ¯P⊗L
¯A M∈ D0
f ( ¯A).
We see thatHi(P⊗L
A M) = 0 for alli⁄= 0. □
RecalltheconnectedcomponentidempotentfunctorsofaDGringfromDeﬁni-
tion 4.25.
Theorem8.5. Let f : A→ Bbeacohomologicallypseudo-ﬁnitehomomorphismbetween
cohomologically pseudo-noetherian DG rings. Assume thatA and B have dualizing DG
modules RA and RB respectively, and that¯B is nonzero. LetE1, . . . , En be the connected
component decomposition functors ofB.
COMMUTATIVE DG RINGS 45
(1) There are unique integersk1, . . . , kn such that, letting
R′
B :=
n⨁
i=1
Ei(RB)[ki]∈ D(B),
the class of the tilting DGB-module RHomA(R′
B, RA) is insideDPic0(B).
(2) Let M∈ Db
f (B). The following conditions are equivalent:
(i) M is CM w.r.t. toR′
B.
(ii) rest f (M) is CM w.r.t. toRA.
Note thatR′
B and R′′
B := RHomA(B, RA) are dualizing DGB-modules, so
RHomA(R′
B, RA)∼= RHomB(R′
B, R′′
B)
is a tilting DGB-module (by Theorem 7.10(2)), and hence item (1) above makes
sense.
Proof. (1) Let R′′
B be as above. By the classiﬁcations in Corollaries 7.11 and 6.15,
there are unique k1, . . . , kn ∈ Z, and a tilting DGB-module Q whose class in
DPic0(B) is unique, such thatR′′
B ∼= Q⊗L
B R′
B. Let P := RHomB(Q, B), which
by Corollary 6.6 is the quasi-inverse ofQ. Then R′
B∼= P⊗L
B R′′
B. Using adjunction
we get isomorphisms
RHomA(R′
B, RA)∼= RHomB(R′
B, R′′
B)∼= RHomB(P⊗L
B R′′
B, R′′
B)
∼= RHomB
(
P, RHomB(R′′
B, R′′
B)
)∼= RHomB(P, B)∼= Q
in D(B). This proves (1).
(2)ByLemma8.4thefunctor Q⊗L
B−preserves D0
f (B). Takeany M∈ Db
f (B). Then,
using Lemma 7.13, we get isomorphisms
RHomA(M, RA)∼= RHomB(M, R′′
B)
∼= RHomB(M, Q⊗L
B R′
B)∼= RHomB(M, R′
B)⊗L
B Q.
This gives (i)⇒ (ii). The converse is very similar. □
Corollary 8.6. Let f : A → B be a cohomologically ﬁnite homomorphism between
tractable DG rings. AssumeSpec ¯B is connected. The following are equivalent forM∈
Db
f (B) :
(i) M is CM w.r.t. some dualizing DGB-module.
(ii) rest f (M) is CM w.r.t. some dualizing DGA-module.
Proof. Theimplication(ii) ⇒(i)comesfromTheorem8.5(2)–anddoesnotrequire
Spec ¯B to be connected.
Fortheimplication(i) ⇒(ii), letRB beadualizingDG B-modulesuchthat M is
CMwithrespecttoit. TakeanydualizingDG A-module RA,andlet k∈ Zbesuch
that RHomA(RB[k], RA)isinside DPic0(B). SeeTheorem8.5(1). ThenbyTheorem
8.5(2) we know thatrest f (M) is CM w.r.t.RA[−k]. □
Theorem 8.7. Let f : A → B be a homomorphism between cohomologically pseudo-
noetherian DG rings, such that¯f : ¯A→ ¯B is surjective. AssumeA and B have dualizing
DG modules. LetRB be a dualizing DGB-module and letM, N∈ Db
f (B).
(1) If M is CM w.r.t.RB, and there is an isomorphismrest f (M) ∼= rest f (N) in
D(A), thenN is also CM w.r.t.RB.
(2) If M and N are CM w.r.t.RB, then the homomorphism
rest f : Hom D(B)(M, N)→ HomD(A)
(
rest f (M), restf (N)
)
is bijective.
46 AMNON YEKUTIELI
Proof. (1) We may assume that¯B⁄= 0. Let E1, . . . , En be the connected component
decomposition functors ofB. Write F := rest f, Mi := Ei(M) and Ni := Ei(N).
Choose some dualizing DGA-module RA, and letk1, . . . , kn be the integers from
Theorem 8.5(1). Thus the dualizing DGB-module R′
B :=⨁n
i=1 Ei(RB)[ki] satisﬁes
this: the tilting DGB-module Q := RHomA(R′
B, RA) is inside DPic0(B). Deﬁne
M′ :=⨁
i Mi[ki] and N′ :=⨁
i Ni[ki].
We are given thatM is CM w.r.t.RB. Using the equivalence of Corollary 4.23
we see thatM′ is CM w.r.t.R′
B. Thus by Theorem 8.5(2) the DGA-module F(M′)
is CM w.r.t.RA. Proposition 4.27 implies thatF(M′)∼= F(N′) in D(A), and hence
F(N′)isCMw.r.t. RA. UsingTheorem8.5(2)oncemoreweconcludethat N′ isCM
w.r.t. R′
B; and henceN is CM w.r.t.RB.
(2) Let us write R′′
B := RHomA(B, RA), D′′
B := RHomB(−, R′′
B) and DA :=
RHomA(−, RA). DeﬁneM′ := ⨁
i Mi[ki] and N′ := ⨁
i Ni[ki] as above, so these
are CM w.r.t.R′′
B. There are isomorphisms
HomD(B)(M, N)∼=1 HomD(B)(M′, N′)∼=2 HomD(B)
(
D′′
B(N′), D′′
B(M′)
)
∼=3 HomMod ¯B
(
D′′
B(N′), D′′
B(M′)
)∼=4 HomMod ¯A
(
F(D′′
B(N′)), F(D′′
B(M′))
)
∼=5 HomMod ¯A
(
DA(F(N′)), DA(F(M′))
)∼=2,3 HomD(A)
(
F(M′), F(N′)
)
∼=6 HomD(A)
(
F(M), F(N)
)
.
They are gotten as follows: the isomorphism∼=1 is by Corollary 4.23 and Propo-
sition 4.26; the isomorphism∼=2 is by Proposition 7.2(3); the isomorphism∼=3 is
by Lemma 8.1; the isomorphism∼=4 is because H0( f ) : ¯A→ ¯B is surjective; the
isomorphism∼=5 is becauseF◦ D′′
B∼= DA◦ F as functors; and isomorphism∼=6 is
due to Proposition 4.27. The composition of all these isomorphisms isF. □
Corollary 8.8. Let f : A→ B be a homomorphism between cohomologically pseudo-
noetherian DG rings, such that¯f : ¯A→ ¯B is bijective. Let RA be a dualizing DGA-
module, and deﬁneRB := RHomA(B, RA). Then the functor
rest f : Db
f (B)CM:RB→ Db
f (A)CM:RA
is an equivalence.
Proof. In view of the last theorem, it suﬃces to show thatrest f is essentially sur-
jective on objects. Take anyM ∈ Db
f (A)CM:RA. Then N := RHomA(M, RA) is
(isomorphicto)amodulein Modf ¯A. Becauserest ¯f : Modf ¯B→ Modf ¯Aisanequiv-
alence, there isN′∈ Modf ¯B that is sent toN. Therefore the DG module
M′ := RHomA(N′, RB)∈ Db
f (B)CM:RB
satisﬁesrest f (M′)∼= M. □
Remark 8.9. Here is a quick explanation of the role of CM DG modules in [Ye5].
Suppose K→ A→ Bareringhomomorphisms, M∈ D(A)and N∈ D(B). Under
suitable assumptions we want to have a canonical isomorphism
⌣ : Sq A/K(M)⊗L
A SqB/A(N) ≃− →SqB/K(M⊗L
A N)
in D(B),thatwecallthe cupproduct. Thisisomorphismwasalreadyconstructedin
[YZ1, Theorem 4.11]; but unfortunately this part of [YZ1] also contained a serious
mistake.
The construction in [Ye5] goes like this. We choose a semi-free DG ring resolu-
tion K→ ˜A of K→ A, and then a semi-free DG ring resolution˜A→ ˜B of ˜A→ B.
COMMUTATIVE DG RINGS 47
So
SqA/K(M) = RHom ˜A⊗K ˜A(A, M⊗L
K M)
etc. The construction goes through a few “standard moves” (adjunction formulas
mostly),untilwearriveatthefollowingsituation. ConsiderthesurjectiveDGring
homomorphism f : ˜B⊗K ˜B→ ˜B⊗ ˜A ˜B, and the DG modules
K := N⊗L
A N⊗L
A SqA/K(M)
and
L := RHom ˜B⊗K ˜B
( ˜B⊗ ˜A ˜B, (M⊗L
A N)⊗L
K (M⊗L
A N)
)
in D( ˜B⊗ ˜A ˜B). The “standard moves” give us a canonical isomorphism
χ : rest f (K) ≃− →rest f (L)in D( ˜B⊗K ˜B);butwhatweneedtocontinuetheconstruc-
tion is a canonical isomorphism¯χ : K ≃− →L in D( ˜B⊗ ˜A ˜B) such thatrest f ( ¯χ) = χ.
The only conceivable hope was that something like Theorem 8.7 should appear.
Fortunately, in the situation where we require the cup product, the ringK is
a regular noetherian ring;K→ A is essentially ﬁnite type;A→ B is essentially
Gorenstein (i.e. essentially ﬁnite type, ﬂat, and the ﬁbers are Gorenstein rings);M
is a rigid dualizing complex overA relative toK; and N is a tilting complex over
B (and hence it is a relative dualizing complex forA→ B). These assumptions
imply thatK is a dualizing DG module over the DG ring˜B⊗ ˜A ˜B, and therefore it
is a CM DG module w.r.t. itself. Now Theorem 8.7 says that there exists a unique
isomorphism ¯χ : K ≃− →L satisfying rest f ( ¯χ) = χ.
