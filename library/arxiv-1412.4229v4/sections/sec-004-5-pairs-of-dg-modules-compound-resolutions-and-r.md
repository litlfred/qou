---
doc_id: arxiv-1412.4229v4
doc_title: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI"
section_id: sec-004-5-pairs-of-dg-modules-compound-resolutions-and-r
section_title: "Pairs of DG Modules, Compound Resolutions, and Rectangles"
section_number: 5
pages: 26-32
source_pdf: 1412.4229v4.pdf
source_sha256: 248d6a1e28a76a94
doc_brief: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI — Let A → B be a homomorphism of commutative rings."
---
Recall that PDGR is the category of central pairs DG rings. See Deﬁnition 3.6.
Resolutions in PDGR were deﬁned in Deﬁnition 3.8 and 3.15. The category of
central DGA-rings DGR/ceA was deﬁned in Deﬁnition 1.6(4).
Deﬁnition 5.1.Let ˜B/ ˜A be an object of PDGR. The enveloping DG ringof ˜B
over ˜A is the DG ring
˜Ben := ˜B⊗˜A ˜Bop∈DGR/ce ˜A.
Let ˜w/˜v : ˜B1/ ˜A1→˜B0/ ˜A0 be a morphism inPDGR. There is an induced DG
ring homomorphism
˜wen := ˜w⊗˜v ˜wop : ˜Ben
1 →˜Ben
0
in DGR/ce ˜A1.
In this way we obtain a functorPDGR→DGR.
Lemma 5.2. Let w/v : B1/A1→B0/A0 be a quasi-isomorphism inPDGR, and
let ˜w/˜v : ˜B1/ ˜A1→˜B0/ ˜A0 be a K-ﬂat resolution ofw/v. Then ˜wen : ˜Ben
1 →˜Ben
0 is
a quasi-isomorphism.
Proof. The homomorphisms ˜v : ˜A1 →˜A0 and ˜w : ˜B1 →˜B0 are also quasi-iso-
morphisms. We can forget the DG rings structures of˜B0 and ˜B1, and just view
them as K-ﬂat DG modules over˜A0 and ˜A1 respectively. Then Proposition 2.6(1)
applies. □
Deﬁnition 5.3.Let ˜B/ ˜A be an object of PDGR, and let ( ˜Ml, ˜Mr) be an object
of M( ˜B)×M( ˜Bop); namely ˜Ml is a left DG ˜B-module, and ˜Mr is a right DG
˜B-module. We deﬁne the DG module
˜Men := ˜Ml⊗˜A ˜Mr∈M( ˜Ben).
THE SQUARING OPERATION 27
Let ˜w/˜v : ˜B1/ ˜A1→˜B0/ ˜A0 be a morphism inPDGR, let
( ˜Ml
k, ˜Mr
k)∈M( ˜Bk)×M( ˜Bop
k )
for k = 0, 1, and let
(˜θl, ˜θr) : ( ˜Ml
0, ˜Mr
0)→( ˜Ml
1, ˜Mr
1)
be a morphism inM( ˜B1)×M( ˜Bop
1 ). We deﬁne the morphism
˜θen := ˜θl⊗˜v ˜θr : ˜Men
0 →˜Men
1
in M( ˜Ben
1 ).
Remark 5.4.We have omitted reference to the forgetful functors in the deﬁnition
above. Thus, the homomorphism ˜θl in M( ˜B1) is actually a homomorphism ˜θl :
Forw( ˜Ml
0)→Ml
1; andthehomomorphism ˜θr in M( ˜Bop
1 )isactuallyahomomorphism
˜θr : Forwop( ˜Mr
0)→Mr
1.
We shall continue with these omissions, for the sake of clarity. The forgetful func-
tors will only be made explicit when there is more than one given homomorphism
between two DG rings. We hope this shortcut will not be a cause for confusion.
Deﬁnition 5.5.Let B/A be an object of PDGR, let (Ml,M r) be an object of
D(B)×D(Bop), and let˜B/ ˜A be a K-ﬂat resolution ofB/A. Acompound resolution
of (Ml,M r) over ˜B/ ˜A is the following data:
•A K-ﬂat resolutionαl : ˜P l→Ml in M( ˜B).
•A K-ﬂat resolutionαr : ˜P r→Mr in M( ˜Bop).
•A K-injective resolutionβ: ˜P en→˜I in M( ˜Ben).
We denote this compound resolution by
P := ( ˜P l, ˜P r, ˜I;αl,αr,β).
It is easy to see that compound resolutions exist.
Consider a K-ﬂat resolutions/r : ˜B/ ˜A→B/A in PDGR. The left and right
actions of ˜B on B commute with each other, and they commute with the action
of Bce on B (all in the graded sense). ThusB is a DG module over˜Ben⊗˜ABce.
Hence we can make the next deﬁnition, in the spirit of Proposition 2.5.
Deﬁnition 5.6.In the situation of Deﬁnition 5.5, we deﬁne the DG module
Rect
˜B/ ˜A
B/A(P ) := HomBen(B, ˜I)∈M(Bce).
The next setup shall be used in the rest of this section.
Setup 5.7. Fork = 0, 1, 2 we are given a central pairBk/Ak∈PDGR, a K-ﬂat
resolution ˜Bk/ ˜Ak→Bk/Ak in PDGR, and a pair of DG modules
(Ml
k,M r
k)∈D(Bk)×D(Bop
k ).
Fork = 1, 2 we are given a central morphism
wk/vk :Bk/Ak→Bk−1/Ak−1
in PDGR (i.e. a morphism inPDGR⃗ce, see Deﬁnition 3.7(3)), a morphism
(θl
k,θr
k) : (Ml
k−1,M r
k−1)→(Ml
k,M r
k)
in D(Bk)×D(Bop
k ), and a morphism
˜wk/˜vk : ˜Bk/ ˜Ak→˜Bk−1/ ˜Ak−1
abovewk/vk.
When we only considerk = 0, 1, the index 1 on the morphismsw1, v1, θl
1, θr
1,
˜w1 and ˜v1 is redundant, and hence we will suppress it.
28 AMNON YEKUTIELI
Deﬁnition 5.8.Consider Setup 5.7, withk = 0, 1 only. LetPk be a compound
resolution of (Ml
k,M r
k) over ˜Bk/ ˜Ak. A compound morphismη:P 0→P 1 above
(θl,θr) and ˜w/˜v is the following data:
•K-projective resolutions γl
0 : ˜Ql
0→˜P l
0 and γr
0 : ˜Qr
0→˜P r
0 in M( ˜B1) and
M( ˜Bop
1 ) respectively.
•Homomorphisms ˜θl : ˜Ql
0→˜P l
1 and ˜θr : ˜Qr
0→˜P r
1 in M( ˜B1) and M( ˜Bop
1 )
respectively, such that
θl◦Q(αl
0)◦Q(γl
0) = Q(αl
1)◦Q(˜θl)
and
θr◦Q(αr
0)◦Q(γr
0) = Q(αr
1)◦Q(˜θr)
in D( ˜B1) and D( ˜Bop
1 ) respectively.
•A homomorphismη: ˜I0→˜I1 in M( ˜Ben
1 ), such that
Q(η)◦Q(β0)◦Q(γl
0⊗˜vγr
0) = Q(β1)◦Q(˜θen),
as morphisms ˜Ql
0⊗˜A1
˜Qr
0→˜I1 in D( ˜Ben
1 ).
We denote this compound morphism by
η= ( ˜Ql
0, ˜Qr
0;γl
0,γr
0, ˜θl, ˜θr,η).
We also say thatηis acompound resolution of(θl,θr).
Thisdeﬁnitionisillustratedinthenextdiagrams, thatarecommutativediagrams
in the categories D( ˜B1), D( ˜Bop
1 ) and D( ˜Ben
1 ) respectively. The vertical arrows in
these diagrams (namely those whose names do not contain the letters “θ” or “η”)
are isomorphisms. (Note that the letterQ denotes the localization functor, not to
be confused with the DG modules˜Ql
0 etc.)
˜Ql
0
Q(γl
0)

Q(˜θl)
!!˜P l
0
Q(αl
0)

˜P l
1
Q(αl
1)

Ml
0 θl
//Mr
1
˜Qr
0
Q(γr
0)

Q(˜θr)

˜P r
0
Q(αr
0)

˜P r
1
Q(αr
1)

Mr
0 θr
//Mr
1
˜Ql
0⊗˜A1
˜Qr
0
Q(γl
0⊗˜vγr
0)

Q(˜θen)
$$˜P en
0
Q(β0)

˜P en
1
Q(β1)

˜I0 Q(η)
// ˜I1
There is no composition rule for the compound morphismsη; but this is taken
care of by the following lemmas.
Lemma 5.9. In the situation of Deﬁnition5.8, compound resolutionsηof the
morphism (θl,θr) exist.
Proof. The homomorphisms ˜θl and ˜θr exist because ˜Ql
0 and ˜Qr
0 are K-projective in
the respective categories. The homomorphism ηexists because ˜I1 is K-injective.
See Proposition 2.4. □
In the next deﬁnition, it is crucial that the homomorphismw : B1 →B0 is
central; thisisguaranteedbySetup5.7, inwhichwedemandthat w/v isamorphism
in PDGR⃗ce. Since w is central, we get an induced DG ring homomorphismwce :
Bce
1 →Bce
0 . So Proposition 2.5(2) applies.
THE SQUARING OPERATION 29
Deﬁnition 5.10.In the situation of Deﬁnition 5.8, we let
Rect ˜w/˜v
w/v(η) : Rect
˜B0/ ˜A0
B0/A0
(P 0)→Rect
˜B1/ ˜A1
B1/A1
(P 1)
be the morphism
Rect ˜w/˜v
w/v(η) := Q
(
Homwen(w,η)
{
in D(Bce
1 ).
Lemma 5.11. The morphism Rect ˜w/˜v
w/v(η) is independent of the compound reso-
lution η. Namely, if η′is another compound resolution of(θl,θr), then there is
equality
Rect ˜w/˜v
w/v(η) = Rect ˜w/˜v
w/v(η′)
of morphisms
Rect
˜B0/ ˜A0
B0/A0
(P 0)→Rect
˜B1/ ˜A1
B1/A1
(P 1)
in D(Bce
1 ).
Proof. Say
η′= ( ˜Q′l
0, ˜Q′r
0 ;γ′l
0,γ′r
0 , ˜θ′l, ˜θ′r,η′).
The DG modules ˜Q′l
0 and ˜Ql
0 are homotopy equivalent inM( ˜B1), and under this
equivalence the homomorphisms ˜θ′l : ˜Q′l
0 →˜P l
1 and ˜θl : ˜Ql
0→˜P l
1 are homotopic.
Likewise for “r”. Therefore the DG modules˜Q′en
0 and ˜Qen
0 are homotopy equivalent
in M( ˜Ben
1 ), and under this equivalence the homomorphisms˜θ′en : ˜Q′en
0 →˜P en
1 and
˜θen : ˜Qen
0 →˜P en
1 are homotopic. This implies that the homomorphismsη′and η
are homotopic. □
Lemma 5.12. Assume that B1/A1 = B0/A0, ˜B1/ ˜A1 = ˜B0/ ˜A0, (Ml
1,M r
1) =
(Ml
0,M r
0), and all the morphisms between them are the identities. Also assume that
P 1 =P 0. Then for any compound morphismη:P 0→P 0 above (idM l
0
, idM r
0), the
morphism Rectid/id
id/id(η) is the identity automorphism ofRect
˜B0/ ˜A0
B0/A0
(P 0).
Proof. Clear. □
Lemma 5.13. Consider Setup 5.7, with k = 0, 1, 2. We are given a compound
resolutionPk of (Ml
k,M r
k) over ˜B/ ˜A. Fork = 1, 2 we are given a compound mor-
phismηk :Pk−1→Pk above (θl
k,θr
k) and ˜wk/˜vk. Also, we are given a compound
morphism η0,2 : P 0→P 2 above (θl
2,θr
2)◦(θl
1,θr
1) and ( ˜w1/˜v1)◦( ˜w2/˜v2). Then
there is equality
Rect( ˜w1/˜v1)◦( ˜w2/˜v2)
(w1/v1)◦(w2/v2)(η0,2) = Rect ˜w2/˜v2
w2/v2
(η2)◦Rect ˜w1/˜v1
w1/v1
(η1)
of morphisms
Rect
˜B0/ ˜A0
B0/A0
(P 0)→Rect
˜B2/ ˜A2
B2/A2
(P 2)
in D(Bce
2 ).
Proof. By choosing homomorphisms ˜Ql
0→˜Ql
1 and ˜Qr
0→˜Qr
1 that liftθl
1 and θr
1
respectively, we can concoct a “composed” morphismη2◦η1, well-deﬁned up to
homotopy, whose component˜I0→˜I2 is η2◦η1. Thus
Rect( ˜w1/˜v1)◦( ˜w2/˜v2)
(w1/v1)◦(w2/v2)(η2◦η1) = Rect ˜w2/˜v2
w2/v2
(η2)◦Rect ˜w1/˜v1
w1/v1
(η1).
On the other hand, by Lemma 5.11 we know that
Rect( ˜w1/˜v1)◦( ˜w2/˜v2)
(w1/v1)◦(w2/v2)(η2◦η1) = Rect( ˜w1/˜v1)◦( ˜w2/˜v2)
(w1/v1)◦(w2/v2)(η0,2).
□
30 AMNON YEKUTIELI
Lemma 5.14. If w/v :B1/A1→B0/A0 is a quasi-isomorphism inPDGR, and if
(θl,θr) : (Ml
0,M r
0)→(Ml
1,M r
1)
is an isomorphism in D(B1)×D(Bop
1 ), then Rect ˜w/˜v
w/v(η) is an isomorphism in
D(Bce
1 ).
Proof. Herew :B1→B0, ˜wen :Ben
1 →Ben
0 , ˜θl, ˜θr, ˜θen andη: ˜I0→˜I1 arequasi-iso-
morphism. According to Proposition 2.6(2),Homwen(w,η) is a quasi-isomorphism.
□
Proposition 5.15. LetB/A be a pair inPDGR, with K-ﬂat resolution˜B/ ˜A. Let
(Ml,M r) be a pair inD(B)×D(Bop). There is an object
Rect
˜B/ ˜A
B/A(Ml,M r)∈D(Bce),
unique up to a unique isomorphism, together with an isomorphism
rect(P ) : Rect
˜B/ ˜A
B/A(Ml,M r)
≃
− →Rect
˜B/ ˜A
B/A(P )
in D(Bce) for every compound resolutionP of the pair(Ml,M r) over ˜B/ ˜A, satis-
fying this condition:
(†) LetP 0 and P 1 be compound resolutions of the pair(Ml,M r) over ˜B/ ˜A,
and let η: P 0 →P 1 be a compound morphism above(idM l, idM r) and
id ˜B/ id ˜A. Then the diagram
Rect
˜B/ ˜A
B/A(Ml,M r)
rect(P 0)

rect(P 1)
))
Rect
˜B/ ˜A
B/A(P 0)
Rectid/id
id/id(η)
// Rect
˜B/ ˜A
B/A(P 1)
of isomorphisms inD(Bce) is commutative.
Proof. The uniqueness is clear. As for existence, let us ﬁx some resolutionP of
(Ml,M r), and deﬁne
Rect
˜B/ ˜A
B/A(Ml,M r) := Rect
˜B/ ˜A
B/A(P ).
The isomorphism rect(P ) is the identity.
Given any resolutionP 0 of (Ml,M r), letη0 :P→P 0 be any morphism above
the identity. Deﬁne the isomorphism
rect(P 0) := Rectid/id
id/id(η0).
By Lemma 5.11 this does not depend on the choice ofη0.
To verify condition (†), letη1 :P →P 1 be any morphism above the identity.
Then, according to Lemma 5.13, we have
Rectid/id
id/id(η1) = Rectid/id
id/id(η)◦Rectid/id
id/id(η0).
□
Proposition 5.16. In the situation of Setup5.7, with k = 0, 1 only, there is a
unique morphism
Rect ˜w/˜v
w/v(θl,θr) : Rect
˜B0/ ˜A0
B0/A0
(Ml
0,M r
0)→Rect
˜B1/ ˜A1
B1/A1
(Ml
1,M r
1)
in D(Bce
1 ) satisfying this condition:
THE SQUARING OPERATION 31
(††) Fork = 0, 1 letPk be a compound resolution of(Ml
k,M r
k) over ˜Bk/ ˜Ak, and
let η:P 0→P 1 be a compound morphism above(θl,θr) and ˜w/˜v. Then
the diagram
Rect
˜B0/ ˜A0
B0/A0
(Ml
0,M r
0)
rect(P 0)

Rect ˜w/˜v
w/v(θl,θr)
// Rect
˜B1/ ˜A1
B1/A1
(Ml
1,M r
1)
rect(P 1)

Rect
˜B0/ ˜A0
B0/A0
(P 0)
Rect ˜w/˜v
w/v(η)
// Rect
˜B1/ ˜A1
B1/A1
(P 1)
of morphisms inD(Bce
1 ) is commutative.
Proof. Choose a compound resolutionP bs
k of (Ml
k,M r
k) over ˜Bk/ ˜Ak, fork = 0, 1.
Then choose a compound morphismηbs :P bs
0 →P bs
1 . (The superscript “bs” stands
for “basic”.) This can be done by Lemma 5.9. LetRect ˜w/˜v
w/v(θl,θr) be the the unique
morphism for which condition (††) holds, with respect to these choices.
We have to prove that condition (††) holds for an arbitrary choice of compound
resolutionsPk and a compound morphismη. Let us choose compound morphisms
ηk :P bs
k →Pk above (idM l, idM r) and id ˜Bk/ id ˜Ak. Consider the following diagram
in D(Bce
1 ).
Rect
˜B0/ ˜A0
B0/A0
(Ml
0,M r
0)
rect(P bs
0 )

Rect ˜w/˜v
w/v(θl,θr)
//
rect(P 0)
""
Rect
˜B1/ ˜A1
B1/A1
(Ml
1,M r
1)
rect(P bs
1 )

rect(P 1)
||
Rect
˜B0/ ˜A0
B0/A0
(P bs
0 )
Rect ˜w/˜v
w/v(ηbs)
//
Rectid/id
id/id(η0)

Rect
˜B1/ ˜A1
B1/A1
(P bs
1 )
Rectid/id
id/id(η1)

Rect
˜B0/ ˜A0
B0/A0
(P 0)
Rect ˜w/˜v
w/v(η)
// Rect
˜B1/ ˜A1
B1/A1
(P 1)
The top square is commutative by deﬁnition. The bottom square is commutative
by Lemmas 5.9 and 5.13. The half-moons are commutative by condition (†) of
Proposition 5.15. Therefore the outer paths are equal; and this is what we had to
prove. □
Proposition 5.17. In the situation of Setup5.7, withk = 0, 1, 2, the diagram
Rect
˜B0/ ˜A0
B0/A0
(Ml
0,M r
0)
Rect( ˜w1 /˜v1 )◦( ˜w2 /˜v2 )
(w1 /v1 )◦(w2 /v2 )(θl
2◦θl
1,θr
2◦θr
1)
**
Rect ˜w1 /˜v1
w1 /v1
(θl
1,θr
1)
// Rect
˜B1/ ˜A1
B1/A1
(Ml
1,M r
1)
Rect ˜w2 /˜v2
w2 /v2
(θl
2,θr
2)

Rect
˜B2/ ˜A2
B2/A2
(Ml
2,M r
2)
of morphisms inD(Bce
2 ) is commutative.
IfB1/A1 =B0/A0, ˜B1/ ˜A1 = ˜B0/ ˜A0, (Ml
1,M r
1) = (Ml
0,M r
0), and the morphisms
w1/v1, ˜w1/˜v1 and (θl
1,θr
1) are the identity automorphisms, thenRect ˜w1/˜v1
w1/v1
(θl
1,θr
1)
is the identity automorphism ofRect
˜B0/ ˜A0
B0/A0
(Ml
0,M r
0).
32 AMNON YEKUTIELI
Proof. The triangular diagram is commutative by Lemmas 5.9 and 5.13, with con-
dition (††) of Proposition 5.16. The assertion about the identity automorphisms is
true by Lemma 5.12. □
Remark 5.18. We could have deﬁned the rectangle object directly as
Rect
˜B/ ˜A
B/A(Ml,M r) := RHom ˜Ben(B,M l⊗L
˜AMr)∈D(Bce),
i.e. as the composition of these three functors:
For×For : D(B)×D(Bop)→D( ˜B)×D( ˜Bop),
−⊗L
˜A−: D( ˜B)×D( ˜Bop)→D( ˜Ben)
and
RHom ˜Ben(B,−) : D( ˜Ben)→D(Bce).
In other words, Proposition 5.15 would have become a deﬁnition.
However, this approach would have made it hard to make precise sense of the
morphism Rect ˜w/˜v
w/v(θl,θr), and to prove the functoriality result (Proposition 5.17).
