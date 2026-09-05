---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-081-135-rigid-dualizing-and-residue-complexes
section_title: "Rigid Dualizing and Residue Complexes"
section_number: 13.5
pages: 280-285
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
these assumptions:
Setup 13.5.1. K is a nonzero regular noetherian commutative ring (Deﬁnition
13.1.10). All other rings are in the category Rngc/feftK of FEFT commutative
K-rings, where “FEFT” is short for “ﬂat essentially ﬁnite type”.
Deﬁnition13.5.2.Arigid dualizing complexoverArelativeto Kisarigidcomplex
(R,ρ) over A relative toK, as in Deﬁnition 13.4.14, such thatR is a dualizing
complex overA, in the sense of Deﬁnition 13.1.9.
See Remark 13.4.24 regarding the ﬂatness condition.
Deﬁnition 13.5.3.ForA∈Rngc/feftK we writeAen :=A⊗KA for theenveloping
ring of A relative toK.
With this notation the square of a complexM∈D(A) relative toK is
SqA/K(M) = RHomAen(A,M⊗L
KM)∈D(A).
Recall the category D(A)rig/K of rigid complexes over A relative to K, from
Deﬁnition 13.4.15.
Theorem 13.5.4 (Uniqueness). Let A be a ﬂat essentially ﬁnite type ring over
the regular noetherian ringK. If A has a rigid dualizing complex(R,ρ), then it is
unique up to a unique isomorphism inD(A)rig/K.
Proof. Suppose (R′,ρ′) is another rigid dualizing complex overA relative toK. Let
A =∏r
i=1Ai be the connected component decomposition ofA. Corollary 13.1.53
says thatR′∼=R⊗L
AP, whereP∼=⨁r
i=1Li[ni] for integersni and rank1 projective
Ai-modules Li. There is an isomorphism
(13.5.5) R′⊗L
KR′= (R⊗L
AP )⊗L
K (R⊗L
AP )∼= (R⊗L
KR)⊗L
Aen (P⊗L
KP )
in D(Aen), andP⊗L
KP has ﬁnite ﬂat dimension overAen. So we have this sequence
of isomorphisms inD(A) :
(13.5.6)
R⊗L
AP∼=R′∼= SqA/K(R′) = RHomAen(A,R′⊗L
KR′)
∼=♦RHomAen
(
A, (R⊗L
KR)⊗L
Aen (P⊗L
KP )
{
∼=†RHomAen(A,R⊗L
KR)⊗L
Aen (P⊗L
KP )
= SqA/K(R)⊗L
Aen (P⊗L
KP )
∼=R⊗L
Aen (P⊗L
KP )∼=R⊗L
AP⊗L
AP.
Theisomorphism∼=♦isby(13.5.5), andtheisomorphism ∼=†isbyTheorem12.10.14.
We also used the rigidifying isomorphisms ofR and R′. Now
RHomA(R,R⊗L
AP )∼= RHomA(R,R )⊗L
AP∼=P,
280
Derived Categories | Amnon Yekutieli | 14 Apr 2019
again using Theorem 12.10.14, and by the derived Morita property ofR. Likewise
there are isomorphisms
RHomA(R,R⊗L
AP⊗L
AP )∼= RHomA(R,R⊗L
AP )⊗L
AP
∼= RHomA(R,R )⊗L
AP⊗L
AP∼=P⊗L
AP
in D(A). Thus, together with (13.5.6), we deduce thatP⊗L
AP∼=P. But then on
each connected componentAi we have
Li[ni]∼=Li[ni]⊗ALi[ni] = (Li⊗ALi)[2·ni].
This implies thatLi∼=Ai and ni = 0. We see that actuallyP∼=A, so there is an
isomorphism φ0 :R
≃
− →R′in D(A).
The isomorphismφ0 might not be rigid; but due to the derived Morita property
of the complexR′, there is an invertible elementa∈A such that SqA/K(φ0)◦ρ=
a·ρ′◦φ0 as isomorphismsR
≃
− →SqA/K(R′). Deﬁneφ:=a−1·φ0. Then, according
to Theorem 13.4.12, we have
SqA/K(φ)◦ρ=a−2·SqA/K(φ0)◦ρ=a−2·a·ρ′◦φ0 =ρ′◦φ.
We see thatφ: (R,ρ)
≃
− →(R′,ρ′) is a rigid isomorphism. Its uniqueness is already
known by Theorem 13.4.16, sinceR′has the derived Morita property. □
Theorem 13.5.7(Existence). LetA be a ﬂat essentially ﬁnite type ring over the
regular noetherian ringK. ThenA has a rigid dualizing complex(RA,ρA).
The proof of this theorem is beyond the scope of the book, as it requires the
study ofinduced and coinduced rigid structures. For a proof see [175]. (There is an
incomplete proof in [189, Theorem 1.1].) The next two examples provide proofs in
some cases.
Example 13.5.8. Suppose A =K[t1,...,tn], the polynomial ring inn variables.
(More generally, we can takeA to be any essentially smoothK-ring of relative
dimension n). Deﬁne the complexRA := Ωn
A/K[n]. According to Example 13.4.20
there is a rigidifying isomorphismρA :RA
≃
− →SqA/K(RA). Because A is a regular
ring, it follows thatRA is a dualizing complex. We see that (RA,ρA) is a rigid
dualizing complex.
Example 13.5.9. Suppose A is a ﬁnite typeK-ring. As explained in Example
18.5.6,A has a noncommutative rigid dualizing complex, that is actuallyA-central.
Thus it is a rigid dualizing complex overA relative toK in the sense of Deﬁnition
13.5.2.
The dimension functiondimR relative to a dualizing complexR was introduced
in Deﬁnition 13.3.2. IfR′∼= R, then of course the dimension functions satisfy
dimR′= dimR. In view of the previous theorem, the next deﬁnition is valid.
Deﬁnition 13.5.10.LetA∈Rngc/feftK. Therigid dimension function relative to
K is the function
rig.dimK : Spec(A)→Z
given by the formularig.dimK(p) := dimR(p), whereR is any rigid dualizing com-
plex overA relative toK.
The next examples (taken from [175]) give an idea what the rigid dimension
function looks like.
Example 13.5.11. Let K be a ﬁeld andA a ﬁnite typeK-ring. Then for every
p∈Spec(A) there is equalityrig.dimK(p) = dim(A/p), where the latter is the Krull
dimension of the ringA/p.
281
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Example 13.5.12. Again K is a ﬁeld, but nowL is a ﬁnitely generated ﬁeld
extension ofK; or in other words,L is a ﬁeld inRngc/feftK . Then, writing p :=
(0)⊆L, we haverig.dimK(p) = tr.degK(L), the transcendence degree of the ﬁeld
extensionK→L.
Example 13.5.13. TakeK =A =Z. For a maximal idealm = (p)⊆Z we have
rig.dimK(m) =−1; and for the generic idealp = (0)⊆Z we haverig.dimK(p) = 0.
Residue complexes were introduced in Subsection 13.3.
Deﬁnition 13.5.14.Arigid residue complexoverArelative toKis a rigid complex
(KA,ρA) overA relative toK, such thatKA is a residue complex overA.
Using the rigid dimension function relative toK, we have this decomposition
of the A-moduleK−i
A for each i : K−i
A
∼= ⨁
rig.dimK(p)=iJ(p), where J(p) is the
indecomposable injective module corresponding to the prime idealp.
In Deﬁnition 13.4.15 we introduced the categoryD(A)rig/K. Recall that the
objects of D(A)rig/K are rigid complexes(M,ρ) overA relative toK; and the mor-
phismsφ: (M,ρ)→(N,σ) are the morphismsφ:M→N in D(A) for which there
is equalityσ◦φ= SqA/K(φ)◦ρ. Rigid residue complexes live, or rather move, in
another category.
Deﬁnition 13.5.15.The category C(A)rig/K is deﬁned as follows. Its objects are
the rigid complexes (M,ρ) over A relative toK. Given two objects (M,ρ) and
(N,σ), a morphismφ: (M,ρ)→(N,σ) in C(A)rig/K is a morphismφ:M→N in
Cstr(A), such that the diagram
M
Q(φ)

ρ
∼=
// SqA/K(M)
SqA/K(Q(φ))

N σ
∼=
// SqA/K(N)
in D(A) is commutative.
Let us emphasize the hybrid nature of the categoryC(A)rig/K : the morphisms
are homomorphisms of complexes (literally degree0 homomorphisms of gradedA-
modules φ:M→N that commute with the diﬀerentials); but they must satisfy a
compatibility condition (rigidity) in the derived category.
Theorem 13.5.16. Let A be an FEFT ring over the regular noetherian ringK.
The ringA has a rigid residue complex(KA,ρA) relative toK, and it is unique, up
to a unique isomorphism inC(A)rig/K.
Proof. Existence: by Theorem 13.5.7 there is a rigid dualizing complex(RA,ρA)
overA relative toK. LetKA be the minimal injective resolution of the complexRA.
According to Theorem 13.3.17,KA is a residue complex. It inherits the rigidifying
isomorphism ρA from RA. So the pair(KA,ρA) is a rigid residue complex overA
relative toK.
Uniqueness: suppose (K′,ρ′) is another rigid residue complex overA relative to
K. Theorem 13.5.4 tells us that there is a unique isomorphismφ: (KA,ρA)
≃
− →
(K′,ρ′) in D(A)rig/K. Now the dimension functions of these two residue complexes
are equal (both arerig.dimK). So by Theorem 13.3.15 the function
Q : HomC(A)rig/K
(
(KA,ρA), (K′,ρ′)
{
→HomD(A)rig/K
(
(KA,ρA), (K′,ρ′)
{
is bijective. Thusφlifts uniquely to an isomorphism inC(A)rig/K. □
282
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Remark 13.5.17. The rigid residue complexKA is functorial in the ringA in
two diﬀerent ways, that we brieﬂy explain here. As in Setup 13.5.1, we work in
the category Rngc/feftK. The ﬂatness condition can be removed (at a price, see
Remark 13.4.24), but it seems that the assumption that the base ringK is regular,
and the other rings are EFT over it, are necessary.
Suppose u : A→B is a ﬁnite homomorphism inRngc/feftK. Then there is a
homomorphism trB/A :KB→KA in Cstr(A), called therigid trace homomorphism.
It is a nondegenerate rigid trace morphism overu (see Remark 13.4.22), namely
it respects the rigidifying isomorphisms, and the induced homomorphismKB →
HomA(B,KA) in Cstr(B) is an isomorphism. Furthermore, generalizing Theorem
13.5.16, trB/A is the unique nondegenerate rigid trace morphism overu. IfB→C
is another ﬁnite homomorphism inRngc/feftK, then trB/A◦trC/B = trC/A.
Suppose v :A→A′is an essentially étale homomorphism inRngc/feftK. Then
there is a homomorphismqA′/A :KA→KA′in Cstr(A), called therigid localiza-
tion homomorphism. It is a nondegenerate rigid localization morphism overv (see
Remark 13.4.22), namely it respects the rigidifying isomorphisms, and the induced
homomorphismA′⊗AKA→KA′in Cstr(A′)isanisomorphism. Furthermore, qA′/A
is the unique nondegenerate rigid localization morphism overv. IfA′→A′′is an-
other essentially étale homomorphism inRngc/feftK, then qA′′/A′◦qA′/A = qA′′/A.
The two functorialities of the rigid residue complexKA commute with each other,
in the following sense. Suppose we are given the ﬁrst commutative diagram below
in Rngc/feftK, which is cocartesian (i.e.B′∼=A′⊗AB),A→B is ﬁnite, andA→A′
is essentially étale. Then the second diagram inCstr(A) is commutative.
A //

B

A′ //B′
KA
qA′/A

KB
trB/A
oo
qB′/B

KA′ KB′
trB′/A′
oo
Imprecise proofs of these assertions can be found in the papers [188] and [189].
A correct treatment will appear in [175].
Remark 13.5.18. The functorialities of the rigid residue complexes that were
outlined in Remark 13.4.22 enable similar construction for schemes. In this remark
we shall dispense with the ﬂatness condition (invoking Remark 13.4.24); soK is a
nonzero regular noetherian base ring (e.g. a ﬁeld or the ring of integersZ), and we
consider the categorySch/eftK of EFTK-schemes.
Let X be an EFTK-scheme. A rigid residue complexon X is a pair(KX,ρX),
consisting of a bounded complex of injective quasi-coherentOX-modulesKX, and a
rigid structureρX onKX, to be explained below. For every aﬃne open setU⊆X
which is strictly EFT, namely A := Γ( U,OX) is an EFT K-ring, the complex
KA := Γ(U,KX) is equipped with a rigidifying isomorphismρU, making it into a
rigid residue complex overA relative toK. IfU′⊆U is a smaller strictly EFT open
set ofX, then the restriction homomorphismKA→KA′must be the unique rigid
localization homomorphism, for the given rigidifying isomorphisms ρU and ρU′.
The collection of these rigidifying isomorphismsρX :={ρU}is the rigid structure
onKX. The schemeX admits a rigid residue complex(KX,ρX), and it is unique
up to a unique rigid isomorphism.
If f : Y →X is a ﬁnite map inSch/eftK, then there is the rigid trace homo-
morphism trf :f∗(KY )→KX in Cstr(X) := Cstr(ModOX); and it is nondegener-
ate, in the sense that the induced homomorphismf∗(KY )→HomX
(
f∗(OY ),KX
{
in Cstr(X) is an isomorphism. If g : X′→X is an essentially étale map in
Sch/eftK, then there is the rigid localization homomorphismqg :KX→g∗(KX′)
283
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in Cstr(X); and it is nondegenerate, in the sense that the induced homomorphism
g∗(KX)→KX′is an isomorphism inCstr(X′). In this way the rigid residue com-
plexes become a sheaf on the small étale site ofX.
Actually, aninﬁnitesimallocalconstructiongives, foreverymorphism f :Y →X
Sch/eftK, theind-rigid trace homomorphismtrf :f∗(KY )→KX in Gstr(X); namely
this is a homomorphism of graded quasi-coherent sheaves on X. The Residue
Theorem says that whenf is proper, the homomorphism trf commutes with the
diﬀerentials. And theDuality Theoremsays that in the proper case, the ind-rigid
trace trf induces an isomorphism
Rf∗
(
RHomY (N,KY )
{
→RHomX
(
Rf∗(N ),KX
{
in D(X) for everyN∈Db
c(X). This explicit rigid version of the original theorems
of Grothendieck from [62] will appear in [176].
Remark 13.5.19. In this remark we considerDeligne-Mumford stacks, of ﬁnite
type over the regular noetherian base ringK. Due to the étale functoriality of the
rigid residue complexes, as explained in Remark 13.5.17, every such stackX admits
a rigid residue complex(KX,ρX). Here the rigid structureρX ={ρ(U,g)}is indexed
by the étale mapsg :U→X from strictly EFT aﬃneK-schemesU.
To a map f : Y →X between DM stacks we associate the ind-rigid trace
trf :f∗(KY)→KX, which is a homomorphism of graded quasi-coherent sheaves on
X. In order to construct the ind-rigid trace for stacks we need another property of
rigid residue complexes over rings, that we callétale codescent. Supposev :A→A′
is a faithfully étale ring homomorphism of EFTK-rings. Letw1,w 2 :A′→A′⊗AA′
be the two inclusions. Étale codescent says that in every degreei the sequence of
A-module homomorphisms
Ki
A′⊗AA′
trw1−trw2
−−−−−−−−→Ki
A′
trv
−−→Ki
A→0
is exact.
As for the Residue Theorem: we can only prove it for a proper map of DM
stacks f : Y→X which is coarsely schematic. Likewise, we can only prove the
Duality Theorem for a proper map of DM stacksf which is coarsely schematic and
tame. These conditions, and a sketch of the proofs, can be found in the lecture notes
[174]. These results shall be written in detail in the future paper [177]. Observe that
duality is not expected to hold without the tameness condition; but the coarsely
schematic condition seems to be a temporary technical hitch.
284
Derived Categories | Amnon Yekutieli | 14 Apr 2019
