---
doc_id: arxiv-1312.6411v4
doc_title: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI"
section_id: sec-009-9-rigid-dg-modules
section_title: "Rigid DG Modules"
section_number: 9
pages: 47-51
source_pdf: 1312.6411v4.pdf
source_sha256: ceac22eb8ffe87e6
doc_brief: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI — We consider commutative DG rings (better known as nonpositive stronglycommutativeassociativeunitalDGalgebras)."
---
RecallthatallourDGringsarecommutative(Convention4.2);namelywework
inside the categoryDGR≤0
sc . At the beginning of this section we do not make any
ﬁniteness assumptions on DG rings.
In our new paper [Ye5] we introduced thesquaring operationfor commutative
DG rings. It is summarized in Theorem 9.1 below, which is a combination of [Ye5,
Theorems 0.3.4, 0.3.5 and 7.16].
Given a homomorphismu : A → B of DG rings, aK-ﬂat resolutionof u is a
commutative diagram
˜A ˜u //
v

qu-isom ˜B
w

K-ﬂat
surj qu-isom
A u
// B
in DGR≤0
sc , where v is a quasi-isomorphism,w is a surjective quasi-isomorphism,
and ˜B is K-ﬂat as a DG˜A-module. Such resolutions always exist.
A K-ﬂat resolution˜A→ ˜B of A→ B gives rise to a functorSq ˜B/ ˜A
B/A : D(B)→
D(B),
Sq ˜B/ ˜A
B/A(M) := RHom ˜B⊗ ˜A ˜B(B, M⊗L
˜A M).
Theorem 9.1([Ye5]). Let A→ B be a homomorphism of DG rings.
(1) There is a functor
SqB/A : D(B)→ D(B) ,
called the squaring operation, together with a compatible system of isomorphisms
of functors SqB/A ∼= Sq ˜B/ ˜A
B/A, where ˜A→ ˜B runs over all K-ﬂat resolutions of
A→ B in DGR≤0
sc .
48 AMNON YEKUTIELI
(2) The functor SqB/A is quadratic, in the following sense: for any morphismφ :
M→ N in D(B), and any elementb∈ ¯B, there is equality
SqB/A(b· φ) = b2· φ .
The compatible system of isomorphisms of functors in item (1) of the theorem
is stated in detail in [Ye5, Theorem 0.3.4]. These isomorphisms make the functor
SqB/A unique up to a unique isomorphism. In part (2) we use the fact thatD(B) is
a ¯B-linear category (see Proposition 4.4).
Deﬁnition 9.2.Let A→ B be a homomorphism of DG rings.
(1) Let M be a DGB-module. Arigidifying isomorphismfor M relative toA is
an isomorphism
ρ : M ≃− →SqB/A(M)
in D(B).
(2) A rigid DG module overB relative to A is a pair(M, ρ), consisting of a DG
B-module M, and a rigidifying isomorphismρ : M ≃− →SqB/A(M) in D(B).
Unlike in [YZ1], here we do not impose any ﬁniteness conditions onM as part
of the deﬁnition of rigidity.
Deﬁnition 9.3.Let A→ B be a homomorphism of DG rings.
(1) Let (M, ρ) and (M′, ρ′) be rigid DG modules overB relative toA. A rigid
morphism
φ : (M, ρ)→ (M′, ρ′)
is a morphismφ : M→ M′ in D(B), such that the diagram
M
ρ //
φ

SqB/A(M)
SqB/A(φ)

M′ ρ′
// SqB/A(M′)
in D(B) is commutative.
(2) The category of rigid DG modules over B relative to A is denoted by
D(B)rig/A.
Theorem 9.4(Uniqueness of Rigid Automorphisms). Let A → B be a homomor-
phism of DG rings, and let(M, ρ) be a rigid DG module overB relative to A. Assume
that the adjunction morphismB→ RHomB(M, M) is an isomorphism. Then the only
automorphism of(M, ρ) in D(B)rig/A is the identity.
Proof. The idea of the proof is already in [Ye2, Theorem 5.2]. The adjunction con-
dition implies that the ring homomorphism¯B→ EndD(B)(M) is bijective. Take
any automorphism φ of (M, ρ) in D(B)rig/A. Then φ = b· idM, for a unique in-
vertible element b ∈ ¯B. By item (2) of Theorem 9.1 we know thatSqB/A(φ) =
b2· SqB/A(idM). On the other hand, becauseφ and idM are both rigid, we get
SqB/A(φ) = ρ◦ φ◦ ρ−1 = ρ◦ (b· idM)◦ ρ−1
= b· (ρ◦ idM◦ρ−1) = b· SqB/A(idM).
This shows thatb2· idM = b· idM, sob2 = b, and henceb = 1. □
Deﬁnition 9.5.Let A be a tractable cohomologically pseudo-noetherian DG ring,
withtraction K→ A(seeDeﬁnition7.7). ArigiddualizingDGmoduleover Arelative
to K is a rigid DG module(R, ρ) over A relative toK (Deﬁnition 9.2), such thatR
is a dualizing DG module overA (Deﬁnition 7.1).
COMMUTATIVE DG RINGS 49
Lemma 9.6. Suppose K is a noetherian ring,A is a cohomologically pseudo-noetherian
DG ring, andK→ A is a cohomologically essentially ﬁnite type homomorphism. Let
K→ ˜A be a K-ﬂat resolution ofK→ A, and deﬁne˜Aen := ˜A⊗K ˜A.
(1) The DG ring ˜Aen is cohomologically pseudo-noetherian, and the homomorphism
K→ ˜Aen is a cohomologically essentially ﬁnite type.
(2) Let P∈ D(A) be a tilting DGA-module. Then P⊗L
K P∈ D( ˜Aen) is a tilting
DG ˜Aen-module.
The derived tensor productP⊗L
K P in item (2) is calculated as follows: we take
any K-ﬂat resolution˜P→ P in C( ˜A), and deﬁneP⊗L
K P := ˜P⊗K ˜P. Because ˜P is
K-ﬂatoverK,thisisindependentoftheresolution,uptoacanonicalisomorphism
in D( ˜Aen).
Proof. (1) As in the proof of Lemma 7.8, we can ﬁnd a commutative diagram in
DGR≤0
sc
K //

˜A //
˜f

A //

¯A
˜Aeft
˜g // ˜Aloc // Aloc
>>
such that ˜f is a K-ﬂat quasi-isomorphism,˜g is a quasi-isomorphism, the DG ring
˜Aeft isK-ﬂatover K,thering ˜A0
eft isessentiallyﬁnitetypeover K,andeachmodule
˜Ai
eft is ﬁnite over˜A0
eft. Now ˜A, ˜Aeft and ˜Aloc are all K-ﬂat overK. Hence, letting
˜Aen
loc := ˜Aloc⊗K ˜Alocand ˜Aen
eft := ˜Aeft⊗K ˜Aleft,wegetDGringquasi-isomorphisms
˜Aen
eft→ ˜Aen
loc and ˜Aen→ ˜Aen
loc. Therefore it suﬃces to prove the required assertions
for ˜Aen
eft.
Considerthering ( ˜Aen
eft)0 = ˜A0
eft⊗K ˜A0
eft. Itisessentiallyﬁnitetypeover K,and
thus it is also noetherian. For anyi≤ 0 we have
( ˜Aen
eft)i =
⨁
i≤p≤0
˜Ap
eft⊗K ˜Ai−p
eft ,
and this is a ﬁnite module over( ˜Aen
eft)0. Therefore the ringH0( ˜Aen
eft), being a quo-
tientof ( ˜Aen
eft)0,isessentiallyﬁnitetypeover K. EachHi( ˜Aen
eft),beingasubquotient
of ( ˜Aen
eft)i, is a ﬁnite module overH0( ˜Aen
eft).
(2) LetQ∈ D(A) be a quasi-inverse ofP. Then
(Q⊗L
K Q)⊗L
A (P⊗L
K P)∼= (Q⊗L
A P)⊗L
K (Q⊗L
A P)∼= A⊗L
K A∼= ˜Aen
in D( ˜Aen). □
Theorem9.7 (UniquenessofRigidDualizingDGModules) . InthesituationofDeﬁ-
nition9.5,supposethat (R, ρ)and (R′, ρ′)arerigiddualizingDGmodulesover Arelative
to K. Then there is a unique isomorphism(R, ρ)∼= (R′, ρ′) in D(A)rig/K.
Proof. The idea of ﬁrst half of the proof goes back to the original work of Van den
Bergh [VdB]. According to Theorem 7.10(2), there is a tilting DG moduleP such
that R′∼= P⊗L
A R in D(A). Choose a K-ﬂat DG ring resolutionK→ ˜A of K→ A,
50 AMNON YEKUTIELI
and let ˜Aen := ˜A⊗K ˜A. Then we have isomorphisms
P⊗L
A R∼=1 R′∼=2 RHom ˜Aen (A, R′⊗L
K R′)
∼=1 RHom ˜Aen
(
A, (P⊗L
A R)⊗L
K (P⊗L
A R)
)
∼=3 RHom ˜Aen
(
A, (R⊗L
K R)⊗L
˜Aen (P⊗L
K P)
)
∼=4 RHom ˜Aen (A, R⊗L
K R)⊗L
˜Aen (P⊗L
K P)
∼=2 R⊗L
˜Aen (P⊗L
K P)∼=3 R⊗L
A P⊗L
A P
in D(A). The isomorphisms∼=1 come from the given isomorphismR′∼= P⊗L
A R
in D(A); the isomorphisms∼=2 come from the rigidifying isomorphismsρ′ and ρ,
together with the isomorphisms from Theorem 9.1(1); the isomorphism∼=3 is by a
standard tensor product identity (that is valid also in this derived setting, because
˜A is K-ﬂat overK); and the the isomorphism∼=4 is by Lemma 7.13, that applies
because ˜Aen is cohomologically pseudo-noetherian, R⊗L
K R is in D+( ˜Aen), and
P⊗L
K P is perfect over ˜Aen – thanks to Lemma 9.6. Now Theorem 7.10(3) tells us
that P⊗L
A P∼= P in D(A). This implies thatP∼= A. We conclude thatR′∼= R in
D(A).
Theremainderoftheproofisthesameasintheproofof[Ye2,Theorem5.2]. Let
φ : R ≃− →R′ be any isomorphism inD(A). The calculation in the proof of Theorem
9.4 shows thatSqA/K(φ) = a· (ρ′◦ φ◦ ρ−1) for a unique invertible elementa∈ ¯A.
Then a−1· φ : R→ R is a rigid isomorphism; and it is unique by Theorem 9.4.□
ExistenceofrigiddualizingDGmodulesinthisgeneralityisnotknown,butwe
believe it it true – this is Conjecture 0.12 in the Introduction. Conjecture 9.8 below
implies Conjecture 0.12.
Suppose u : A → B is a homomorphism between cohomologically pseudo-
noetherian DG rings. We say thatu is cohomologically essentially smooth of relative
dimension n if ¯u : ¯A→ ¯B is essentially smooth of relative dimensionn, and the
inducedhomomorphism H(A)⊗ ¯A ¯B→ H(B)isbijective. Inthiscase,themodule
ofdiﬀerentialsΩ1
¯B/ ¯A isprojectiveofrank n,andhence Ωn
¯B/ ¯A isprojectiveofrank 1.
We deﬁneΩn
B/A[n]∈ D(B) to be the lift ofΩn
¯B/ ¯A[n]∈ D( ¯B), under the group iso-
morphism DPic(B)∼= DPic( ¯B)ofTheorem6.14. Thereisanalternativedescription
of Ωn
B/A[n] in terms of thecotangent complexof B/A.
Conjecture 9.8. In the situation of Deﬁnition 9.5, suppose(RA, ρA) is a rigid du-
alizing DG module overA relative toK. Let B be another DG ring, and letA→ B
be a cohomologically essentially ﬁnite type homomorphism.
(1) If A→ B is cohomologically pseudo-ﬁnite, then the DG module
RB := RHomA(B, RA)∈ D(B)
has an induced rigidifying isomorphismρB relative toK.
(2) If A→ B is cohomologically essentially smooth of relative dimensionn,
then the DG module
RB := Ωn
B/A[n]⊗L
A RA∈ D(B)
has an induced rigidifying isomorphismρB relative toK.
Inthecasewhen Aand Barerings,Conjectures0.12and9.8werealreadyproved
in [YZ1]. The proofs will be repeated, with improvements, in [Ye7]. In the case
when the cohomology ofA is bounded, Conjectures 0.12 and 9.8 were very re-
cently proved by Shaul [Sh2]. What remains to prove is the case whenH(A) is
unbounded.
COMMUTATIVE DG RINGS 51
Remark 9.9. Finally, a few words on Conjecture 0.13 from the Introduction. We
canseethreepossibleroutestotrytoproveit. Theﬁrstrouteisbygeneralizingthe
originalproofof[YZ2,Theorem1.2],thattalkedaboutaregulartractablering A,to
the DG ring case. The second route is by generalizing the proof of [AIL, Theorem
4], which applied to any tractable ringA, to the DG ring case.
There is also a more conceptual route. In [Ye5] we introduced therectangle oper-
ation
RectA/K(M, N) := RHom ˜A⊗K ˜A(A, M⊗L
K N),
for M, N∈ D(A). Here K→ ˜A is a K-ﬂat resolution ofK→ A, but the rectan-
gle operation is independent of this resolution. Notice that the square is a special
instance of the rectangle:SqA/K(M) = RectA/K(M, M).
Recently Shaul [Sh1] proved that whenA is a tractable ring, and under certain
ﬁniteness conditions onM and N, there is a canonical isomorphism
RectA/K(M, N)∼= D
(
D(M)⊗L
A D(N)
)
,
where D := RHomA(−, RA), andRA is the rigid dualizing complex ofA relative
to K. Thus,writing M⊗!
A/K N := RectA/K(M, N),thisoperationbecomesasym-
metric monoidal structure on (a suitable subcategory of)D+
f (A).
Suppose now that M ∈ Db
f (A) is rigid relative toK. Deﬁne L := D(M) ∈
Db
f (A). ThenLsatisﬁesL⊗L
A L∼= L. IfMisnonzerooneachconnectedcomponent
of Spec ¯A, then the same holds forL. It is not hard to show that in this caseL∼= A
in D(A). Therefore M∼= RA, so it is a rigid dualizing complex.
If this work of Shaul could be extended to cover tractable DG rings, we would
have a proof of Conjecture 0.13, at least whenA is cohomologically bounded.
