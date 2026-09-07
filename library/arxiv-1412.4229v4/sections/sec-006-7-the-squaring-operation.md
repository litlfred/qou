---
doc_id: arxiv-1412.4229v4
doc_title: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI"
section_id: sec-006-7-the-squaring-operation
section_title: "The Squaring Operation"
section_number: 7
pages: 37-43
source_pdf: 1412.4229v4.pdf
source_sha256: 248d6a1e28a76a94
doc_brief: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI — Let A → B be a homomorphism of commutative rings."
---
(∗) Let ˜w/˜v : ˜B′/ ˜A′→˜B/ ˜A be a morphism of K-ﬂat resolutions ofB/A in
PDGR≤0. Then the diagram
RectB/A(Ml,M r)
rect
˜B/ ˜A

rect
˜B′/ ˜A′
**
Rect
˜B/ ˜A
B/A(Ml,M r)
Rect ˜w/˜v
w/v(idM l,idM r)
// Rect
˜B′/ ˜A′
B/A (Ml,M r)
of isomorphisms inD(Bce) is commutative.
Proof. Choose a commutative semi-free resolution˜Aun/Z ofA/Z, and then choose
a noncommutative semi-free resolution˜Bun/ ˜Aun ofB/ ˜Aun, both inPDGR≤0. This
is possible by Theorem 3.21. (The subscript “un” stands for “universal”.) Note
that ˜Bun/ ˜Aun is a K-ﬂat resolution ofB/A. Deﬁne
RectB/A(Ml,M r) := Rect
˜Bun/ ˜Aun
B/A (Ml,M r).
Consider any K-ﬂat resolution˜B/ ˜A of B/A. According to Theorem 3.22 there
is a morphism
˜wun/˜vun : ˜Bun/ ˜Aun→˜B/ ˜A
of resolutions ofB/A. We deﬁne
rect
˜B/ ˜A : Rect
˜Bun/ ˜Aun
B/A (Ml,M r)
≃
− →Rect
˜B/ ˜A
B/A(Ml,M r)
to be
rect
˜B/ ˜A := Rect ˜wun/˜vun
id/id (idM l, idM r)−1.
Theorem 6.11 tells us that the isomorphismrect ˜B/ ˜A does not depend on the choice
of ˜wun/˜vun.
It remains to verify condition (∗). Suppose ˜B′/ ˜A′is another K-ﬂat resolution
of B/A, and ˜w/˜v : ˜B′/ ˜A′→˜B/ ˜A is a morphism of resolutions ofB/A. Choose a
morphism of resolutions
˜w′
un/˜v′
un : ˜Bun/ ˜Aun→˜B′/ ˜A′.
We have a diagram
Rect
˜Bun/ ˜Aun
B/A (Ml,M r)
Rect
˜B/ ˜A
B/A(Ml,M r)
Rect ˜wun/˜vun
id/id (id,id)
OO
Rect ˜w/˜v
w/v(id,id)
// Rect
˜B′/ ˜A′
B/A (Ml,M r)
Rect
˜w′
un/˜v′
un
id/id (id,id)
jj
of isomorphisms inD(Bce). Proposition 5.17 says that
Rect ˜w′
un/˜v′
un
id/id (id, id)◦Rect ˜w/˜v
w/v(id, id) = Rect( ˜w◦˜w′
un)/(˜v◦˜v′
un)
id/id (id, id).
Finally, Theorem 6.11 says that
Rect( ˜w◦˜w′
un)/(˜v◦˜v′
un)
id/id (id, id) = Rect ˜wun/˜vun
id/id (id, id).
We that the diagram in condition (∗) is indeed commutative. □
38 AMNON YEKUTIELI
Remark 6.16.Let K be a regular ﬁnite dimensional noetherian commutative ring,
and letA be a cohomologically pseudo-noetherian commutative DG ring (see [Ye2,
Section 3]). SupposeK→A is a DG ring homomorphism, such thatK→H0(A) is
essentially ﬁnite type. LetD+
f (A) be the full subcategory ofD(A) consisting of DG
modules whose cohomology is bounded below, and whose cohomology modules are
ﬁnite overH0(A).
ForM,N ∈D+
f (A) let us write
M⊗!
A/KN := RectA/K(M,N )∈D(A).
In [Ga], D. Gaitsgory states that when K is a ﬁeld of characteristic0, this is
operation makes D+
f (A) into a monoidal category. No proof of this statement is
given in [Ga].
Now assumeA is a ring (so it is just a noetherian commutative ring, essentially
ﬁnite type overK). According to [YZ3] and its corrections in [Ye5], there is arigid
dualizing complexRA/K overA relative to K. The functorD := RHomA(−,RA/K)
is a duality of the categoryDf(A), and it exchangesD+
f (A) with D−
f (A). Recently
L. Shaul [Sh1] showed that there is a bifunctorial isomorphism
(6.17) M⊗!
A/KN∼=D
(
D(M)⊗L
AD(N)
{
for M,N ∈Db
f (A). The proof relies on the reduction formula for Hochschild co-
homology [AILN, Theorem 1], [Sh2]. The isomorphism (6.17) implies that the
operation−⊗!
A/K−is a monoidal structure on the subcategoryDb
f (A)ﬁd of Db
f (A)
consisting of complexes with ﬁnite injective dimension. The monoidal unit isRA/K.
Work in progress by Shaul indicates that the result above should hold in greater
generality: A can be as in the ﬁrst paragraph of the remark, andM,N can be any
objects in D+
f (A).
7. The Squaring Operation
InthissectionallDGringsarecommutative; namely, weworkinsidethecategory
DGR≤0
sc . SeeDeﬁnition3.3. Thecategory PDGR≤0
sc ofcommutativepairsofDGrings
was introduced in Deﬁnition 3.7(2); it is a full subcategory of the categoryPDGR
of central pairs of DG rings.
Deﬁnition 7.1. (1) Let B/A be an object ofPDGR≤0
sc . A K-ﬂat resolutionof
B/A in PDGR≤0
sc is a resolutions/r : ˜B/ ˜A→B/A in the sense of Deﬁnition
3.8, such that the pair˜B/ ˜A is commutative and K-ﬂat (Deﬁnition 3.11(3)).
(2) Morphisms of resolutions in PDGR≤0
sc , and resolutions of morphisms in
PDGR≤0
sc , are as in Deﬁnition 3.9, but all the pairs are now commutative.
Proposition 7.2. Any object and any morphism inPDGR≤0
sc admits a K-ﬂat res-
olution.
Proof. Like the proof of Corollary 3.25, but using commutative semi-free resolu-
tions. □
For a commutative DG ringB we haveBce = B of course. This is used in the
following deﬁnitions.
Deﬁnition 7.3.LetB/A be a pair of commutative DG rings, and letM be a DG
B-module. Given a K-ﬂat resolution˜B/ ˜A of B/A in PDGR≤0
sc , we let
Sq
˜B/ ˜A
B/A(M) := Rect
˜B/ ˜A
B/A(M,M )∈D(B).
See Proposition 5.15.
THE SQUARING OPERATION 39
Deﬁnition 7.4.Let w/v : B′/A′→B/A be a morphism in PDGR≤0
sc , let M ∈
D(B), let M′∈D(B′), and letθ: M →M′be a morphism in D(B′). Given a
K-ﬂat resolution˜w/˜v : ˜B′/ ˜A′→˜B/ ˜A of w/v in PDGR≤0
sc , we deﬁne
Sq ˜w/˜v
w/v(θ) : Sq
˜B/ ˜A
B/A(M)→Sq
˜B′/ ˜A′
B′/A′(M′)
to be the morphism
Sq ˜w/˜v
w/v(θ) := Rect ˜w/˜v
w/v(θ,θ)
in D(B′) from Proposition 5.16.
Remark 7.5. As explained in Remark 5.18, we can write
Sq
˜B/ ˜A
B/A(M) = RHom ˜Ben(B,M ⊗L
˜AM).
However, the morphismSq ˜w/˜v
w/v(θ) in Deﬁnition 7.4 is not standard, so we have to
use the more explicit approach with compound resolutions, as was done in Section
5.
Still, here we can simplify matters by using symmetric compound resolutions.
A symmetric compound resolution of a DGB-module M is dataP = ( ˜P, ˜I;α,β),
consisting of a K-ﬂat resolutionα: ˜P→M in M( ˜B), and a K-injective resolution
β: ˜P en = ˜P⊗˜A ˜P→˜I in M( ˜Ben).
Likewise, a morphismθ: M→M′can be resolved by a symmetric compound
morphismη:P→P′, whereη= ( ˜Q;γ,˜θ,η) consists of a K-projective resolution
γ: ˜Q→˜P in M( ˜B′); a homomorphism ˜θ: ˜Q→˜P′in M( ˜B′) lifting θ; and a
homomorphism η: ˜I→˜I′in M( ˜B′en) lifting
˜θ⊗˜θ: ˜Q⊗˜A′˜Q→˜P′⊗˜A′˜P′.
Here is the key technical result of our paper (Theorem 0.3.3 in the Introduction).
Actually, it is just a special case of Theorem 6.11.
Theorem 7.6 (Homotopy Invariance). Let w/v : B′/A′→B/A be a morphism
in PDGR≤0
sc , let M ∈D(B), let M′∈D(B′), and let θ: M →M′be a mor-
phism in D(B′). Suppose ˜B/ ˜A and ˜B′/ ˜A′are K-ﬂat resolutions ofB/A and B′/A′
respectively inPDGR≤0
sc , and
˜w0/˜v0, ˜w1/˜v1 : ˜B′/ ˜A′→˜B/ ˜A
are morphisms of resolutions abovew/v. Then the morphisms
Sq ˜w0/˜v0
w/v (θ), Sq ˜w1/˜v1
w/v (θ) : Sq
˜B/ ˜A
B/A(M)→Sq
˜B′/ ˜A′
B′/A′(M′)
in D(B′) are equal.
Proof. TakeMl = Mr := M, M′l = M′r := M′, and θl = θr := θin Theorem
6.11. □
This brings us to the ﬁrst main theorem of the paper (which is Theorem 0.3.4
in the Introduction).
Theorem 7.7(Existence of Squares). LetA→B be a homomorphism of commu-
tative DG rings, and letM be a DGB-module. There is a DG moduleSqB/A(M),
unique up to a unique isomorphism inD(B), together with an isomorphism
sq
˜B/ ˜A : SqB/A(M)
≃
− →Sq
˜B/ ˜A
B/A(M)
in D(B) for each K-ﬂat resolution˜B/ ˜A ofB/A in PDGR≤0
sc , satisfying the following
condition.
40 AMNON YEKUTIELI
(∗) Let ˜w/˜v : ˜B′/ ˜A′→˜B/ ˜A be a morphism of K-ﬂat resolutions ofB/A in
PDGR≤0
sc . Then there is equality
Sq ˜w/˜v
id/id(idM) = sq
˜B′/ ˜A′
◦(sq
˜B/ ˜A)−1
of isomorphisms Sq
˜B/ ˜A
B/A(M)
≃
− →Sq
˜B′/ ˜A′
B/A (M) in D(B).
Proof. The proof is very similar to that of Theorem 6.15: we ﬁx a universal K-ﬂat
resolution ofB/A; but now it has to be a commutative resolution. So let˜Aun/Z
be a commutative semi-free resolution ofA/Z, and let ˜Bun/ ˜Aun be a commutative
semi-free resolution ofB/ ˜Aun, both inPDGR≤0
sc . This is possible by Theorem 3.21.
Deﬁne
SqB/A(M) := Sq
˜Bun/ ˜Aun
B/A (M).
Given any K-ﬂat resolution˜B/ ˜A of B/A in PDGR≤0
sc , Theorem 3.22 says there
is a morphism of resolutions
˜wun/˜vun : ˜Bun/ ˜Aun→˜B/ ˜A.
We deﬁne the isomorphism
sq
˜B/ ˜A : Sq
˜Bun/ ˜Aun
B/A (M)
≃
− →Sq
˜B/ ˜A
B/A(M)
to be
sq
˜B/ ˜A := Sq ˜wun/˜vun
id/id (idM)−1.
The veriﬁcation of condition (∗) is the same as in the proof of Theorem 6.15,
except that here we use Theorem 7.6 instead of Theorem 6.11. □
Deﬁnition 7.8.A triple in DGR≤0
sc is the data of homomorphismsA
u
− →B
v
− →C
in DGR≤0
sc . We refer to this triple asC/B/A.
A commutative K-ﬂat resolution ofC/B/A is a triple ˜A
˜u
− →˜B
˜v
− →˜C in DGR≤0
sc ,
together with homomorphismsr : ˜A→A, s : ˜B→B and t : ˜C→C in DGR≤0
sc ,
such that:
•r is a quasi-isomorphism, ands,t are surjective quasi-isomorphisms.
•s◦˜u =u◦r and t◦˜v =v◦s.
•˜u and ˜v◦˜u are K-ﬂat.
See diagram (0.2.4) in the Introduction. A commutative K-ﬂat resolution˜A
˜u
− →
˜B
˜v
− →˜C can be viewed as follows: K-ﬂat resolutionss/r : ˜B/ ˜A →B/A and
t/r : ˜C/ ˜A→C/A in PDGR≤0
sc , and a morphism of resolutions˜v/id ˜A : ˜B/ ˜A→˜C/ ˜A
above the morphism of pairsv/idA :B/A→C/A.
Proposition 7.9. Commutative K-ﬂat resolutions of triples exist.
Proof. This follows from Theorems 3.21 and 3.22. Compare to the proof of Corol-
lary 3.25. □
Here is the second main theorem of the paper (which is Theorem 0.3.5 in the
Introduction).
Theorem 7.10 (Trace Functoriality). Let A− →B
v
− →C be homomorphisms of
commutative DG rings, letM ∈D(B), let N ∈D(C), and letθ: N →M be a
morphism in D(B). There is a unique morphism
Sqv/idA(θ) : SqC/A(N)→SqB/A(M)
in D(B), satisfying the condition:
THE SQUARING OPERATION 41
(∗∗) For any commutative K-ﬂat resolution˜A→˜B
˜v
− →˜C of the tripleA→B
v
− →
C, there is equality
Sq˜v/id ˜A
v/idA
(θ) = sq
˜B/ ˜A◦Sqv/idA(θ)◦(sq
˜C/ ˜A)−1
of morphisms Sq
˜C/ ˜A
C/A(N)→Sq
˜B/ ˜A
B/A(M) in D(B).
Proof. We begin by choosing a universal K-ﬂat resolution of the tripleA
u
− →B
v
− →C.
We choose, in this order, commutative semi-free resolutionsrun/id : ˜Aun/Z→A/Z,
sun/run : ˜Bun/ ˜Aun→B/ ˜Aun and tun/sun : ˜Cun/ ˜Bun→C/ ˜Bun. In this way we
obtain a K-ﬂat resolving triple˜Aun
˜uun
−−→˜Bun
˜vun
−−→˜Cun of A
u
− →B
v
− →C. Now we
deﬁne
Sqv/idA(θ) := (sq
˜Bun/ ˜Aun)−1◦Sq
˜vun/id ˜Aun
v/idA
(θ)◦sq
˜Cun/ ˜Aun.
Let us verify condition (∗∗). We are given an arbitrary commutative K-ﬂat
resolution ˜A
˜u
− →˜B
˜v
− →˜C of the tripleA→B
v
− →C. According to Theorem 3.22 we
can ﬁnd homomorphisms˜r : ˜Aun→˜A, ˜s : ˜Bun→˜B and ˜t : ˜Cun→˜C, such that
the diagram below inPDGR≤0
sc is commutative.
(7.11) ˜Bun/ ˜Aun
˜vun/id //
˜s/˜r

sun/run
!!
˜Cun/ ˜Aun
˜t/˜r

tun/run
}}
˜B/ ˜A
˜v/id //
s/r

˜C/ ˜A
t/r

B/A
v/id //C/A
Now let us look at the corresponding diagram with the squaring operation. It is
a diagram inD(B).
Sq
˜Bun/ ˜Aun
B/A (M) Sq
˜Cun/ ˜Aun
C/A (N)
Sq˜vun/id
v/id (θ)
oo
Sq
˜B/ ˜A
B/A(M)
Sq˜s/˜r
id/id(id)
OO
Sq
˜C/ ˜A
C/A(N)
Sq
˜t/˜r
id/id(id)
OO
Sq˜v/id
v/id(θ)
oo
SqB/A(M)
sq
˜Bun/ ˜Aun
==
sq
˜B/ ˜A
OO
SqC/A(N)
sq
˜C/ ˜A
OO
Sqv/id(θ)
oo
sq
˜Cun/ ˜Aun
]]
The top square is commutative by Proposition 5.17 (applied twice). The two
half-moons are commutative by condition (∗) of Theorem 7.7. The outer paths are
equal by deﬁnition ofSqv/id(θ). Because the vertical arrows are isomorphisms, we
conclude that the bottom square is commutative. This is what we had to prove.□
Corollary 7.12. LetB/A be a pair of commutative DG rings. The assignments
M↦→SqB/A(M) and θ↦→SqidB/idA(θ)
are a functor
SqB/A : D(B)→D(B).
42 AMNON YEKUTIELI
Proof. Consider morphismsM0
θ1
−→M1
θ2
−→M2 in D(B). A combination of Propo-
sition 5.17 and condition (∗∗) of Theorem 7.10 shows that
Sqid/id(θ2)◦Sqid/id(θ1) = Sqid/id(θ2◦θ1).
And by Lemma 5.12,Sqid/id(idM) = idSqB/A(M). □
Deﬁnition 7.13.The object SqB/A(M) from Theorem 7.7 is called thesquare
of M over B relative toA. The functor SqB/A from Corollary 7.12 is called the
squaring operation overB relative toA.
The following result says that the squaring operationSqB/A is also functorial in
the DG ringB.
Proposition 7.14. We are given homomorphisms of commutative DG ringsA→
B2
v2
−→B1
v1
−→B0, DG modulesMk∈D(Bk), and morphismsθk :Mk−1→Mk in
D(Bk). Then
Sqv2/idA(θ2)◦Sqv1/idA(θ1) = Sq(v1◦v2)/idA(θ2◦θ1),
as morphisms SqB0/A(M0)→SqB2/A(M2) in D(B2).
Proof. Choose a K-ﬂat resolution˜A− →˜B2
˜v2
−→˜B1
˜v1
−→˜B0 ofA→B2
v2
−→B1
v1
−→B0,
in the obvious sense that generalizes Deﬁnition 7.8. According to condition (∗∗) of
Theorem 7.10, it suﬃces to prove that
Sq˜v2/id
v2/id(θ2)◦Sq˜v1/id
v1/id(θ1) = Sq(˜v1◦˜v2)/id
(v1◦v2)/id(θ2◦θ1),
as morphisms Sq
˜B0/ ˜A
B0/A(M0)→Sq
˜B2/ ˜A
B2/A(M2) in D(B2). This is true by Proposition
5.17. □
Proposition 7.15.LetA be a commutative DG ring. The action from Proposition
2.5(1) makes D(A) into an H0(A)-linear category.
Proof. BecauseA0 is in the center ofA, andd(A0) = 0, we see thatM(A) is anA0-
linear category. See formula (1.15). Next, from formula (2.1) we see thatK(A) is an
H0(A)-linear category. Hence its localizationD(A) is anH0(A)-linear category. □
Given a homomorphismB→C of commutative DG rings, and objectsM ∈
D(B) and N ∈D(C), the set HomD(B)(N,M ) is an H0(C)-module, with action
coming the action ofH0(C) onN as an object ofD(C), as in the proposition above.
We end the paper with the next result.
Theorem 7.16. In the situation of Theorem7.10, letc∈H0(C). Then
Sqv/id(c·θ) =c2·Sqv/id(θ),
as morphisms
SqC/A(N)→SqB/A(M)
in D(B).
Proof. Choose a K-ﬂat resolution˜B/ ˜A of B/A. Then choose a strict commuta-
tive semi-free resolution ˜C/ ˜B of C/ ˜B. Putting them together we obtain a K-ﬂat
resolution ˜A− →˜B
˜v
− →˜C of A→B
v
− →C, where ˜v is commutative semi-free. Let
PM = ( ˜PM, ˜IM;αM,βM) be a symmetric compound resolution ofM over ˜B/ ˜A,
and letPN = ( ˜PN, ˜IN;αN,βN) be a symmetric compound resolution ofN over
˜C/ ˜A. See Remark 7.5 and Deﬁnition 5.8.
Because ˜PN is K-projective over ˜B, we can ﬁnd a homomorphism˜θ: ˜PN→˜PM
in M( ˜B) that liftsθ. We obtain a symmetric compound morphismη:PN→PM,
THE SQUARING OPERATION 43
η:= ( ˜PN; id˜PN, ˜θ,η) aboveθand ˜v/id ˜A. Speciﬁcally, the homomorphismη: ˜IN→
˜IM in M( ˜Ben) is a lift of
˜θ⊗˜θ: ˜PN⊗˜A ˜PN→˜PM⊗˜A ˜PM.
By Proposition 5.16,Sqv/id(θ) is represented by
Homven(v,η) : HomCen(C, ˜IN)→HomBen(B, ˜IM).
We remind that ˜Ben = ˜B⊗˜A ˜Bop and ˜Cen = ˜C⊗˜A ˜Cop.
Now choose some ˜c∈˜C0 that represents the cohomology classc∈H0(C)∼=
H0( ˜C). Then ˜c·˜θ: ˜PN→˜PM lifts c·θ: N→M, and (˜c⊗˜c)·η: ˜IN→˜IM lifts
(˜c·˜θ)⊗(˜c·˜θ). We get a symmetric compound morphismηc :PN→PM,
ηc :=
(˜PN; id˜PN, ˜c·˜θ,(˜c⊗˜c)·η
{
resolving c·θ. But then the homomorphism
Homven(v, (˜c⊗˜c)·η) = Homven(˜c2·v,η) = ˜c2·Homven(v,η)
represents Sqv/id(c·θ). □
This theorem shows that the functorSqB/A is aquadratic functor.
