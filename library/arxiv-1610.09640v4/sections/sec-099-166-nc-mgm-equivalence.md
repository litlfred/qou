---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-099-166-nc-mgm-equivalence
section_title: "NC MGM Equivalence"
section_number: 16.6
pages: 377-385
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
explained in Example 12.4.6. A noncommutative variant of this theory was re-
cently developed by R. Vyas and A. Yekutieli [157], and in this subsection we give
an adaptation of it to the case of a NC connected graded ringA. In Section 17 be-
low we shall use the NC MGM Equivalence to prove the existence of balanced trace
morphisms (Theorem 17.4.22), and in Section 18 the NC MGM Equivalence will
help us prove that a balanced dualizing complex is graded rigid (Theorem 18.4.5).
We continue with Conventions 15.1.17 and 15.2.1, soK is a base ﬁeld, andA
and B are gradedK-rings.
Recall (from Remark 14.3.23) that the derived categoryD(Aen, gr) has a biclosed
monoidal structure on it, with monoidal operation(−⊗L
A−) and monoidal unitA.
For complexesM ∈D(A⊗Bop, gr) and N ∈D(B⊗Aop, gr) the left and right
unitor isomorphisms arelu : A⊗L
AM
≃
− →M and ru : M⊗L
AA
≃
− →M respectively.
The left co-unitor isomorphism islcu : RHomA(A,M )
≃
− →M.
Deﬁnition 16.6.1([157]).
(1) A copointed objectin the monoidal category D(Aen, gr) is a pair (P,σ),
consisting of an object P ∈D(Aen, gr) and a morphism σ: P →A in
D(Aen, gr).
(2) The copointed object(P,σ) is calledidempotent if the morphisms
lu◦(σ⊗L
A id), ru◦(id⊗L
Aσ) : P⊗L
AP→P
in D(Aen, gr) are both isomorphisms.
Remark 16.6.2. Here is an explanation of the name “copointed”. In a monoidal
category, with unit objectA, a point of an objectP is a morphismA→P. It
thus makes sense to refer to a morphism in the dual direction, sayσ:P→A, as a
copointof P.
Deﬁnition 16.6.3.Let (P,σ) be a copointed object inD(Aen, gr).
(1) Deﬁne the triangulated functors
F,G : D(A⊗Bop, gr)→D(A⊗Bop, gr)
to beF :=P⊗L
A (−) and G := RHomA(P,−).
377
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(2) Let σ:F→Id and τ: Id→G be the morphisms of triangulated functors
from D(A⊗Bop, gr) to itself that are induced by the morphismσ:P→A.
Namely
σM := lu◦(σ⊗L
A idM) :F (M) =P⊗L
AM→M
and
τM := RHomA(σ,idM)◦lcu−1 :M→RHomA(P,M ) =G(M).
We refer to (F,σ) and (G,τ) as the copointed and pointed triangulated functors
induced by the copointed object(P,σ).
Item (2) of the deﬁnition is shown in the commutative diagrams below in the
category D(A⊗Bop, gr).
P⊗L
AM
σ⊗L
AidM

σM
$$
A⊗L
AM lu
//M
M
τM
%%
RHomA(A,M )
RHomA(σ,idM)

lcuoo
RHomA(P,M )
Deﬁnition16.6.4.Let (F,σ)and (G,τ)bethecopointedandpointedtriangulated
functors on D(A⊗Bop, gr) from Deﬁnition 16.6.3.
(1) Let D(A⊗Bop, gr)F be the full triangulated subcategory ofD(A⊗Bop, gr)
on the set of objects
{
M|σM :F (M)→M is an isomorphism
}
.
(2) Let D(A⊗Bop, gr)G be the full triangulated subcategory ofD(A⊗Bop, gr)
on the set of objects
{
M|τM :M→G(M) is an isomorphism
}
.
Idempotent (co)pointed triangulated functors were introduced in Deﬁnitions
16.2.3 and 16.2.10.
Lemma 16.6.5. If the copointed object(P,σ) is idempotent, then the copointed
triangulated functor (F,σ) and the pointed triangulated functor(G,τ) on D(A⊗
Bop, gr) are idempotent.
Proof. ForM∈D(A⊗Bop, gr) there are equalities (up to the associativity isomor-
phism of (−⊗L
A−), that should be inserted in the locations marked by “†”):
(16.6.6) F (σM) = idP⊗L
A
(
lu◦(σ⊗L
A idM)
{
=†(
ru◦(idP⊗L
Aσ)
{
⊗L
A idM
and
(16.6.7) σF(M) = lu◦
(
σ⊗L
A (idP⊗L
A idM)
{
=†(
lu◦(σ⊗L
A idP )
{
⊗L
A idM
of morphisms
F (F (M)) =P⊗L
AP⊗L
AM→F (M) =P⊗L
AM
in D(A⊗Bop, gr). Because bothlu◦(σ⊗L
AidP )and ru◦(idP⊗L
Aσ)are isomorphisms
in D(Aen), it follows that the morphismsF (σM) and σF(M) are isomorphisms in
D(A⊗Bop).
There are also equalities (up to the associativity and adjunction isomorphisms
of (−⊗L
A−) and RHomA(−,−), that should be inserted in the locations marked
by by “‡”):
(16.6.8)
G(τM) = RHomA
(
idP, RHomA(σ,idM)
{
◦RHomA(idP, lcu)
=‡RHomA(σ⊗L
A idP, idM)◦RHomA(lu, idM)
378
Derived Categories | Amnon Yekutieli | 14 Apr 2019
and
(16.6.9)
τG(M) = RHomA(σ,idRHomA(P,M))◦lcu
=‡RHomA(idP⊗L
Aσ,idM)◦RHomA(ru, idM)
of morphisms
G(M) = RHomA(P,M )→G(G(M))
= RHomA
(
P, RHomA(P,M )
{∼= RHomA(P⊗L
AP,M )
in D(A⊗Bop, gr). Because both lu◦(σ⊗L
A idP ) and ru◦(idP⊗L
Aσ) are isomor-
phisms in D(Aen, gr), it follows that the morphismsG(τM) and τG(M) are isomor-
phisms in D(A⊗Bop, gr). □
Lemma 16.6.10.Consider the functorsF andG on D(A⊗Bop, gr) from Deﬁnition
16.6.3. For everyM,N ∈D(A⊗Bop, gr) there is a bijection
HomD(A⊗Bop,gr)
(
F (M),N
{∼= HomD(A⊗Bop,gr)
(
M,G (N)
{
,
and it is functorial inM and N.
Proof. Choose a K-injective resolution N →J in C(A⊗Bop, gr), and a K-ﬂat
resolution ˜P→P in C(Aen, gr). The usual Hom-tensor adjunction gives rise to an
isomorphism
(16.6.11) HomA⊗Bop( ˜P⊗AM,J )∼= HomA⊗Bop
(
M, HomA( ˜P,J )
{
in Cstr(K, gr). From this we deduce that HomA( ˜P,J ) is K-injective in
C(A⊗Bop, gr). We see that the isomorphism (16.6.11) represents an isomorphism
(16.6.12) RHomA⊗Bop(P⊗L
AM,N )∼= RHomA⊗Bop
(
M, RHomA(P,N )
{
in D(K, gr). Taking H0 in (16.6.12) gives us the isomorphism
HomD(A⊗Bop,gr)(P⊗L
AM,N )∼= HomD(A⊗Bop,gr)
(
M, RHomA(P,N )
{
in M(K, gr). This is what we want. □
Lemma 16.6.13.Consider the functorsF andG on D(A⊗Bop, gr) from Deﬁnition
16.6.3. Assume that the copointed object(P,ρ) is idempotent. Then the kernel ofF
equals the kernel ofG. Namely for everyM∈D(A⊗Bop, gr) we haveF (M) = 0
if and only ifG(M) = 0.
Proof. We shall use the adjunction formula from Lemma 16.6.10, withN =M.
First assume F (M) = 0 . Then HomD(A⊗Bop,gr)
(
F (M),M
{
is zero, and by
Lemma 16.6.10 we see thatHomD(A⊗Bop,gr)
(
M,G (M)
{
is zero too. This implies
that the morphismτM :M→G(M) is zero. ApplyingG to it we deduce that the
morphism G(τM) : G(M)→G(G(M)) is zero. But by Lemma 16.6.5 the pointed
functor (G,τ) is idempotent, and this means thatG(τM) is an isomorphism. There-
fore G(M) = 0.
Now assume thatG(M) = 0. Again using Lemma 16.6.10, but now in the re-
verse direction, we see that the morphismσM : F (M)→M is zero. Therefore
the morphismF (σM) : F (F (M))→F (M) is zero. But by Lemma 16.6.5 the co-
pointedfunctor (F,σ)isidempotent, andthismeansthat F (σM)isanisomorphism.
Therefore F (M) = 0. □
Recall that Convention 15.1.17 is in eﬀect.
Theorem 16.6.14(Abstract Equivalence, [157]). LetA and B be gradedK-rings,
and let (P,σ) be an idempotent copointed object inD(Aen, gr). Consider the trian-
gulated functors
F,G : D(A⊗Bop, gr)→D(A⊗Bop, gr)
379
Derived Categories | Amnon Yekutieli | 14 Apr 2019
and the categories D(A⊗Bop, gr)F and D(A⊗Bop, gr)G from Deﬁnitions16.6.3
and 16.6.4. The following hold:
(1) The functorG is a right adjoint toF.
(2) The copointed triangulated functor(F,σ) and the pointed triangulated func-
tor (G,τ) are idempotent.
(3) The categoriesD(A⊗Bop, gr)F and D(A⊗Bop, gr)G are the essential images
of the functorsF and G respectively.
(4) The functor
F : D(A⊗Bop, gr)G→D(A⊗Bop, gr)F
is an equivalence of triangulated categories, with quasi-inverseG.
Proof. (1) This is Lemma 16.6.10.
(2) This is Lemma 16.6.5.
(3) Take an objectM∈D(A⊗Bop, gr)G. Then M∼= G(M), so thatM is in the
essential image ofG. Conversely, suppose there is an isomorphismφ:M
≃
− →G(N)
for someN∈D(A⊗Bop, gr). We have to prove thatτM is an isomorphism. There
is a commutative diagram
M
φ //
τM

G(N)
τG(N)

G(M)
G(φ) //G(G(N))
in D(A⊗Bop, gr) with horizontal isomorphisms. The idempotence of(G,τ) says
that the morphismτG(N) is an isomorphism. ThereforeτM is an isomorphism.
A similar argument (with reversed arrows, and using the idempotence of(F,σ))
tells us that the essential image ofF is D(A⊗Bop, gr)F.
(4) The morphismσ:P→A sits inside a distinguished triangle
(16.6.15) P
σ
− →A→N
∆
−−→
in D(Aen, gr). Letusapplythefunctor P⊗L
A(−)to(16.6.15). Wegetadistinguished
triangle
P⊗L
AP
ru◦(id⊗L
Aσ)
−−−−−−−−→P→P⊗L
AN
∆
−−→
in D(Aen, gr). By the idempotence of (P,σ), the ﬁrst morphism above is an iso-
morphism; and henceP⊗L
AN = 0. Therefore for everyM∈D(A⊗Bop, gr) the
complex F (N⊗L
AM) =P⊗L
AN⊗L
AM is zero. Lemma 16.6.13 tells us that
(16.6.16) G(N⊗L
AM) = RHomA(P,N ⊗L
AM)
is zero.
Now we go back to the distinguished triangle (16.6.15) and we apply to it the
functor (−)⊗L
AM, and then the functorRHomA(P,−). The result is the distin-
guished triangle
RHomA(P,P ⊗L
AM)
αM
−−→RHomA(P,M )→RHomA(P,N ⊗L
AM)
∆
−−→
in D(A⊗Bop, gr). By (16.6.16) the third object in this triangle is zero, and it follows
thatαM :G(F (M))→G(M)isanisomorphism. Ifmoreover M∈D(A⊗Bop, gr)G,
then τM is an isomorphism too, and thus we have an isomorphism
(16.6.17) τ−1
M ◦αM :G(F (M))→M
in D(A⊗Bop, gr)G that’s functorial inM.
380
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Similarly, if we apply the functor(−)⊗L
AP to (16.6.15), we get a distinguished
triangle
P⊗L
AP
lu◦(σ⊗L
Aid)
−−−−−−−−→P→N⊗L
AP
∆
− →
in D(Aen, gr). By the idempotence condition, the ﬁrst morphism above is an iso-
morphism; and henceN⊗L
AP = 0. Therefore for everyM∈D(A⊗Bop, gr) the
complex
G
(
RHomA(N,M )
{
= RHomA
(
P, RHomA(N,M )
{∼= RHomA(N⊗L
AP,M )
is zero. Lemma 16.6.13 tells us that
(16.6.18) F
(
RHomA(N,M )
{
=P⊗L
A RHomA(N,M )
is zero.
Next we apply the functorRHomA(−,M ), and then the functorP⊗L
A (−), to
the distinguished triangle (16.6.15). We obtain distinguished triangle
P⊗L
A RHomA(N,M )→P⊗L
AM
βM
−−→P⊗L
A RHomA(P,M )
∆
−−→
in D(A⊗Bop, gr). By (16.6.18) the ﬁrst object in this triangle is zero, and so
βM : F (M)→F (G(M)) is an isomorphism. If moreoverM∈D(A⊗Bop, gr)F,
then σM is an isomorphism too, and thus we have an isomorphism
(16.6.19) βM◦σ−1
M :M→F (G(M))
in D(A⊗Bop, gr)F that’s functorial inM.
The isomorphisms (16.6.17) and (16.6.19) tell us thatF andG are equivalences
between D(A⊗Bop, gr)G and D(A⊗Bop, gr)F, quasi-inverse to each other. □
We now leave the abstract setting, and return tom-torsion. So we are in the
situation of Setup 16.4.1. The dedualizing complex PA := Γ m(A)∈D(Aen, gr)
from Deﬁnition 16.4.2 is equipped with the morphismσR
A : PA = RΓ m(A)→A
from Proposition 16.3.16.
Deﬁnition 16.6.20.The pair (PA,σR
A) is called thededualizing copointed object
of the monoidal categoryD(Aen, gr).
Theorem 16.6.21 ([157]). Under Setup 16.4.1, the dedualizing copointed object
(PA,σR
A) in the monoidal categoryD(Aen, gr) is idempotent.
Proof. Let’s writeσ:=σR
A and P :=PA. We shall start by proving that
(16.6.22) lu◦(σ⊗L
A id) :P⊗L
AP→P
is an isomorphism in D(Aen, gr). Because the forgetful functor Rest : D(Aen, gr)
→D(A, gr) is conservative, it is enough if we prove thatRest(lu◦(σ⊗L
A id)) is an
isomorphism. Let us introduce the temporary notationP′:= Rest(P )∈D(A, gr).
With this notation, what we have to show is that
(16.6.23) lu◦(σ⊗L
A id) :P⊗L
AP′→P′
is an isomorphism inD(A, gr).
Consider Theorem 16.4.3 with B = K and M = P′∈D(A, gr). There is a
commutative diagram
P⊗L
AP′
evR,L
m,P′
//
σ⊗L
A id

RΓ m(P′)
σR
P′

A⊗L
AP′ lu //P′
381
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in D(A, gr), and the horizontal arrows are isomorphisms. It suﬃces to prove that
σR
P′: RΓ m(P′)→P′is an isomorphism inD(A, gr). But there is an isomorphism
P′∼= RΓ m(A′), whereA′:= Rest(A)∈D(A, gr). So what we need to prove is that
σR
RΓm(A′) : RΓ m(RΓ m(A′))→RΓ m(A′)
is an isomorphism in D(A, gr). This is true because the copointed triangulated
functor (RΓ m,σR) on D(A, gr) is idempotent; see Corollary 16.3.36 withB :=K.
Now we are going to prove that
(16.6.24) ru◦(id⊗L
Aσ) :P⊗L
AP→P
is an isomorphism inD(Aen, gr).
Wehavethiscommutative(uptoacanonicalisomorphism)diagramin D(Aen, gr)
(16.6.25) P⊗L
AP
id⊗L
Aσ

P⊗L
AP⊗L
AA
id⊗L
A ruoo
id⊗L
Aσ⊗L
Aid

P⊗L
AA P ⊗L
AA⊗L
AA
id⊗L
A ruoo
Using Theorem 16.4.3 with B = A and M = A∈D(Aen, gr), we have this
commutative diagram inD(Aen, gr) :
(16.6.26) PA⊗L
AA
evR,L
m,A //
σ⊗L
A id

RΓ m(A)
σR
A

A⊗L
AA lu //A
Applyingthefunctor P⊗L
A(−)tothisdiagram, weobtainthiscommutativediagram
(16.6.27) P⊗L
AP⊗L
AA
id⊗L
Aσ⊗L
A id

id⊗L
A evR,L
m,A //P⊗L
A RΓ m(A)
id⊗L
AσR
A

P⊗L
AA⊗L
AA
id⊗L
A lu //P⊗L
AA
in D(Aen, gr). The last move is using the fact thatevR,L
m,(−) is an isomorphism of
functors; this yields the next commutative diagram:
(16.6.28) P⊗L
A RΓ m(A)
id⊗L
AσR
A

evR,L
m,RΓm(A)
// RΓ m(RΓ m(A))
RΓm(σR
A)

P⊗L
AA
evR,L
m,A // RΓ m(A)
All horizontal arrows in diagrams (16.6.25), (16.6.26), (16.6.27) and (16.6.28) are
isomorphisms. Since ru is an isomorphism, to prove that (16.6.24) is an isomor-
phism, it is enough to prove that the morphismid⊗L
Aσ, which is the left vertical
arrow in diagram (16.6.25), is an isomorphism. Now this last morphism coincides
with the left vertical arrow in diagram (16.6.28). Therefore it is enough to prove
that the right vertical arrow in diagram (16.6.28) is an isomorphism. This is
(16.6.29) RΓ m(σR
A) : RΓ m(RΓ m(A))→RΓ m(A).
Because the functorRest is conservative, it suﬃces to prove that
RΓ m(σR
A′) : RΓ m(RΓ m(A′))→RΓ m(A′)
382
Derived Categories | Amnon Yekutieli | 14 Apr 2019
is an isomorphism inD(A, gr), where, as before, we writeA′:= Rest(A)∈D(A, gr).
This is true because the copointed triangulated functor(RΓ m,σR) on D(A, gr) is
idempotent. □
Deﬁnition 16.6.30.UnderSetup16.4.1, considerthededualizingcopointedobject
(PA,σR
A) in the monoidal categoryD(Aen, gr); see Deﬁnition 16.6.20.
(1) The abstract derived m-adic completion functor is the triangulated
pointed functor (ADCm,τ) on D(A⊗Bop, gr) that’s induced by the co-
pointed object (PA,σR
A), in the sense of Deﬁnition 16.6.3
(2) The full subcategory of D(A⊗Bop, gr) on the complexes M such that
τM :M→ADCm(M) is an isomorphism is denoted byD(A⊗Bop, gr)com.
To put item (1) in explicit terms,ADCm(M) = RHomA(PA,M ), and the mor-
phism τM :M→ADCm(M) is τM = RHomA(σR
A, idM).
We already have the copointed triangulated functor(RΓ m,σR) on the category
D(A⊗Bop, gr). In analogy with Deﬁnition 16.6.30(2) we make the next deﬁnition.
Deﬁnition 16.6.31.Under Setup 16.4.1, we denote byD(A⊗Bop, gr)tor the full
subcategory of D(A⊗Bop, gr) on the complexesM such thatσR
M : RΓ m(M)→M
is an isomorphism.
Proposition 16.3.29 says that
D(A⊗Bop, gr)tor = Dtor(A⊗Bop, gr),
where the latter is the full subcategory ofD(A⊗Bop, gr) on the complexesM whose
cohomology modules arem-torsion.
Theorem 16.6.32(NC MGM Equivalence, [157]). Under Setup16.4.1 the follow-
ing hold.
(1) The categories D(A⊗Bop, gr)com and D(A⊗Bop, gr)tor are the essential
images of the functorsADCm and RΓ m respectively.
(2) The pointed triangulated functor(ADCm,τ) and the copointed triangulated
functor (RΓ m,σR) are idempotent.
(3) The functor
RΓ m : D(A⊗Bop, gr)com→D(A⊗Bop, gr)tor
is an equivalence of triangulated categories, with quasi-inverseADCm.
Proof. By Deﬁnition 16.6.30, the pointed triangulated functor(ADCm,τ) is the one
induced by the copointed object(PA,σR
A). And by Theorem 16.4.3, the copointed
triangulated functor(RΓ m,σR)is the one induced by the copointed object(PA,σR
A).
According to Theorem 16.6.21, the copointed object(PA,σR
A) is idempotent. This
means that we can use Theorem 16.6.14 on abstract equivalence. Item (1) here is
then a special case of item (3) of Theorem 16.6.14; item (2) here is a special case
of item (2) of Theorem 16.6.14; and item (3) here is a special case of item (4) of
Theorem 16.6.14. □
Example 16.6.33.In Example 12.4.6 we presented the commutative MGM Equiv-
alence. Recall the setting: a commutative ringA, and an ideala⊆A generated
by a weakly proregular sequencea. The module category there wasM(A). If we
want to transfer this to the connected graded setting of the current section, where
the module category isM(A, gr), then we should takeA to be a commutative con-
nected gradedK-ring, anda is a sequence of homogeneous elements that generates
the augmentation idealm. Then A =K[a] is a ﬁnitely generated commutativeK-
ring, and thus noetherian. BecauseA is commutative, leftA-modules are the same
as centralA-bimodules. This is the reason we work with the categoryM(A, gr) and
not with M(Aen, gr).
383
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Regardless of which setting we choose (graded or ungraded), the dedualizing
complexPA over the ringA (as an object ofD(A, gr) or D(A) respectively) can be
made explicit: PA∼= K∨
∞(A;a)∼= Tel(A;a), where K∨
∞(A;a) is the inﬁnite dual
Koszul complex, andTel(A;a) is thetelescope complex. Since the telescope complex
is a bounded complex of freeA-modules (of countable rank), the derived torsion and
completion functors have particularly nice presentations:RΓ m = Tel(A;a)⊗A (−)
and ADCm = HomA
(
Tel(A;a),−
{
. Also the abstract derived completion functor
ADCm is canonically isomorphism toLΛ m, the left derived functor of them-adic
completion functor Λ m. See [118] for details.
384
Derived Categories | Amnon Yekutieli | 14 Apr 2019
