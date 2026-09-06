---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-087-145-tilting-bimodule-complexes-over-rings
section_title: "Tilting Bimodule Complexes over Rings"
section_number: 14.5
pages: 314-323
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
14.3.8, but in this subsection we only look at rings. So our rings are ﬂat central
over the base ringK,⊗=⊗K, andAen =A⊗Aop for a ringA. All bimodules are
K-central, and all additive functors areK-linear. Rather than speaking about DG
314
Derived Categories | Amnon Yekutieli | 14 Apr 2019
bimodules, here we speak about complexes of bimodules. By default our rings are
nonzero.
In classical Morita theory, aninvertibleB-A-bimoduleis a bimoduleP for which
there exists anA-B-bimoduleQ, such thatQ⊗BP∼=A in M(Aen) andP⊗AQ∼=B
in M(Ben). It is known thatP is a ﬁnitely generated projective module overB and
over Aop; and the reverse is true forQ. Furthermore, everyK-linear equivalence
F : M(A)→M(B) is isomorphic, as a functor, to the functorP⊗A (−) for an
invertible bimoduleP, and thisP is unique up to a unique isomorphism. See [130,
Section 4.1] for proofs.
We see that invertible bimodules are a very special kind of tilting bimodule
complexes. Proposition 14.5.3 clariﬁes matters. But ﬁrst a lemma, which is a
noncommutative variant of Lemma 13.1.36
Lemma 14.5.1(Künneth Trick). LetM∈D−(B⊗Aop) and N∈D−(A⊗Cop),
and leti1,j 1∈Z be such thatsup(H(M))≤i1 and sup(H(N))≤j1. Then
Hi1+j1(M⊗L
AN)∼= Hi1(M)⊗A Hj1(N)
in M(B⊗Cop).
Exercise 14.5.2. Prove Lemma 14.5.1.
Proposition 14.5.3.The following conditions are equivalent for a tilting bimodule
complexT∈D(B⊗Aop), with quasi-inverseS =T∨.
(i) There is an isomorphismT∼= P in D(B⊗Aop) for some invertibleB-A-
bimoduleP.
(ii) H0(T ) is a projectiveB-module, and Hi(T ) = 0 for alli⁄= 0.
(iii) Hi(T ) = 0 and Hi(S) = 0 for alli⁄= 0.
Proof.
(i)⇒(ii): this is trivial.
(ii)⇒(iii): Let P := H 0(T )∈M(B⊗Aop), so there is an isomorphismT ∼= P
in D(B⊗Aop). According to Corollary 14.4.27 we have S ∼= RHomB(T,B )∼=
HomB(P,B ).
(iii)⇒(i): DeﬁneP := H0(T )∈M(B⊗Aop) andQ := H0(S)∈M(A⊗Bop). The
Künneth Trick (Lemma 14.5.1) says thatP⊗BQ∼= H0(T⊗L
BS)∼= H0(A) =A and
Q⊗AP∼= H0(S⊗L
AT )∼= H0(B) =B in M(Aen) and M(Ben) respectively. ThusP
and Q are invertible bimodules. ButT∼=P in D(B⊗Aop). □
The Jacobson radicalof a ringA is the intersection of all maximal left (or right)
ideals ofA. See [71, Section 4.4.2] or [130, Section 2.5].
Deﬁnition 14.5.4.A ringA, with Jacobson radical r, is calledlocal if A/r is a
simple artinian ring.
Note that this deﬁnition is wider than what is found in some books (e.g. [130]),
where the condition is thatA/r is a division ring.
Example 14.5.5. If C is a commutative local ring with maximal idea m, and
n ≥1, then the matrix ring A := Mat n×n(C) is local, with Jacobson radical
m·A = Matn×n(m).
Lemma 14.5.6. LetA be a local ring, letM be a nonzero ﬁnitely generated right
A-module, and letN be a nonzero ﬁnitely generated leftA-module. ThenM⊗AN
is nonzero.
315
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. DeﬁneK :=A/r, which is a simple artinian ring. By the noncommutative
Nakayama Lemma (see [130, Proposition 2.5.24]) the rightK-module M⊗AK is
nonzero, and also the leftK-module K⊗A N is nonzero. There is a canonical
surjection
M⊗AN→(M⊗AK)⊗K (K⊗AN).
It suﬃces to prove that the target is nonzero. Thus we can assume thatA =K is
a simple artinian ring.
Every left module overK is a direct sum of simple ones; so we can assume that
N is simple. Likewise we can assume thatM is a simple rightK-module.
There is a ring isomorphismK∼= Matn×n(D), whereD is a division ring and
n is a positive integer. The simple left K-module N is isomorphic to Dn, seen
as a column module; thus it is in fact aK-D-bimodule. Similarly M∼= Dn, seen
as a row module; thus it is aD-K-bimodule. By an easy calculation (this is an
elementary case of Morita equivalence) there is an isomorphismM⊗K N∼= D of
D-D-bimodules. This is nonzero. □
Theorem 14.5.7([132], [165]). LetA and B be ﬂat centralK-rings, withA local,
and letT be a tiltingB-A-bimodule complex. Then there is an isomorphismT∼=
P [n] in D(B⊗Aop) for some invertibleB-A-bimoduleP and some integern.
See Remark 14.5.32 regarding the history of this theorem.
Proof. Let S∈D(A⊗Bop) be the quasi-inverse ofT. From Corollary 14.4.28 and
Theorem 14.1.22 we know thatT andS are algebraically perfect complexes on both
sides. ByLemma14.1.27weknowthat con(H(T )) = [i0,i 1]and con(H(S)) = [j0,j 1]
for some integersi0≤i1 and j0≤j1; and also thatP := Hi1(T ) and Q := Hj1(S)
are ﬁnitely presented modules on both sides.
We now use the Künneth trick to obtain an isomorphism
P⊗AQ∼= Hi1+j1(T⊗L
AS)∼= Hi1+j1(B)
in M(Ben). ByLemma14.5.6weknowthat P⊗AQisnonzero. Therefore i1+j1 = 0,
and P⊗A Q∼= B in M(Ben). For similar reasons, on the reverse side we have
Q⊗BP∼= H0(S⊗L
BT )∼=A in M(Aen). ThusP and Q are invertible bimodules.
We now restrictT to D(Aop). Because its top cohomology moduleHi1(T ) = P
is projective, we can split it oﬀ (see Lemma 13.1.38, that holds also for a non-
commutative ring), to get an isomorphism T ∼= T′⊕P [−i1] in D(Aop), with
sup(H(T′))≤i1−1. Similarly there’s an isomorphismS∼= S′⊕Q[−j1] in D(A)
with sup(H(S′))≤j1−1. It follows that
B∼=T⊗L
AS∼=
(
T′⊕P [−i1]
{
⊗L
A
(
S′⊕Q[−j1]
{
∼= (T′⊗L
AS′)⊕
(
P [−i1]⊗AS′{
⊕
(
T′⊗AQ[−j1]
{
⊕B
in D(K). The object B∈D(K) has cohomology concentrated in degree0. The
direct summandT′⊗AQ[−j1] has cohomology concentrated in degrees≤−1, so
its cohomology must be zero, and thereforeT′⊗AQ[−j1] = 0 in D(K). But Q is
an invertible bimodule, and this forcesT′= 0 in D(Aop). The conclusion is that
Hi(T ) = 0 for alli⁄=i1.
Returning to the categoryD(A⊗Bop) we see thatT∼=P [−i1]. Finally we take
n :=−i1. □
Corollary 14.5.8. Let A and B be rings, withA local. If there is an equivalence
of triangulated categories D(A)→D(B), then there is an equivalence of abelian
categories M(A)→M(B). In other words,A and B are Morita equivalent.
316
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. According to Theorem 14.4.30 there exists a tiltingB-A-bimodule complex
T. Theorem 14.5.7 says thatT ∼= P [n] for an invertibleB-A-bimodule P. Then
P⊗A (−) : M(A)→M(B) is an equivalence of abelian categories. □
Deﬁnition 14.5.9.For a centralK-ring A we deﬁne thenoncommutative Picard
group ofA relative toK to be the groupPicK(A), whose elements are the isomor-
phism classes inM(Aen) of the invertible bimodules. The operation is induced by
(−⊗A−), and the unit element is the class ofA.
The derived Picard group was introduced in Deﬁnition 14.4.8.
Corollary 14.5.10. If A is a local ring, then
DPicK(A) = PicK(A)×Z.
Proof. By Theorem 14.5.7 there is a surjective group homomorphismPicK(A)×
Z →DPicK(A), deﬁned by(P,n ) ↦→P [n]. It is injective because the functor
M(Aen)→D(Aen) is fully faithful. □
The center of a ringA is denoted byCent(A). Of courseCent(A) = Cent(Aop).
Given a complexM∈D(B⊗Aop), there are ring homomorphisms
(14.5.11) chmD
M,Aop : Cent(A)→EndD(B⊗Aop)(M)
and
(14.5.12) chmD
M,B : Cent(B)→EndD(B⊗Aop)(M)
that we call the central homotheties through Aop and B respectively. The for-
mulas are the obvious ones: for an element a ∈Cent(A) the action on M is
chmD
M,Aop(a)(m) :=m·a for m∈Mi. Likewise forchmD
M,B.
Lemma 14.5.13. IfT is a tiltingB-A-bimodule complex, then the ring homomor-
phisms chmD
M,Aop and chmD
M,B are both isomorphisms.
Proof. Let S be the quasi-inverse ofT. The functor
G := (−)⊗L
AS : D(B⊗Aop)→D(B⊗Bop) = D(Ben)
is an equivalence. It induces a ring isomorphism
G : EndD(B⊗Aop)(T )
≃
− →EndD(Ben)(B),
and G◦chmD
T,B = chm D
B,B. But EndD(Ben)(B) ∼= EndM(Ben)(B), and the ring
homomorphism Cent(B)→EndM(Ben)(B) is bijective.
The proof forchmD
T,Aop is similar. □
Deﬁnition 14.5.14.Given a tiltingB-A-bimodule complexT, we denote bygT :
Cent(A)→Cent(B) the ring isomorphism such thatchmD
T,Aop = chmD
T,B◦gT.
Even though the localization of a noncommutative ringB with respect to a
multiplicatively closed subsetZ⊆B is problematic in general, there is no diﬃculty
at all ifZ⊆Cent(B). In this case, lettingC := Cent(B), we get canonicalA-ring
isomorphisms BZ∼=CZ⊗CB∼=B⊗CCZ.
Lemma 14.5.15. Let T be a tiltingB-A-bimodule complex, and assume that the
ring A is commutative. Let Z ⊆A be a multiplicatively closed set, and deﬁne
A′:=AZ andB′:=BgT (Z). Then the complexT′:=B′⊗BT⊗AA′in D(B′⊗A′op)
is a tiltingB′-A′-bimodule complex.
317
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. The cohomologyH(T ) is a central gradedA-bimodule, where the left action
of A on H(T ) is via the isomorphismgT. (Warning: the complex of bimodulesT
need not be central overA.) The ﬂatness ofA→A′and B→B′gives
H(T′) = H(B′⊗BT⊗AA′)∼=B′⊗B H(T )⊗AA′∼=A′⊗A H(T )⊗AA′.
Therefore H(T )⊗A A′→H(T′) is an isomorphism of graded modules, and this
implies that
(14.5.16) T⊗AA′→T′
is an isomorphism inD(B⊗A′op).
Let S := RHomB(T,B ) in D(A⊗Bop) be the quasi-inverse ofT. In analogy
to Deﬁnition 14.5.14, there is a ring isomorphismhS : A→Cent(B) such that
chmD
S,A = chm D
S,Bop◦hS. The cohomology H(S) is a central gradedA-bimodule,
where the right action ofA on H(S) is viahS.
Let us consider the derived tensor productS⊗L
BT∈D(Aen), and the four ways
that an elementa∈A acts on it as an object ofD(Aen). The action of a from
the right side ofT the same as the action ofgT (a)∈Cent(B) from the left side of
T. This is also the action ofgT (a) from the right side ofS, and also the action of
h−1
S (gT (a)) from the left onS. But there are ring isomorphisms
EndD(Aen)(S⊗L
BT )∼= EndD(Aen)(A)∼=A,
anda acts onA the same from both sides. The conclusion is thath−1
S (gT (a)) =a.
Because a is an arbitrary element, we see thatgT = hS as isomorphisms A
≃
− →
Cent(B). So we have a single ring isomorphismA∼= Cent(B), for which bothH(T )
and H(S) are central gradedA-bimodules.
DeﬁneS′:=A′⊗AS⊗BB′∈D(A′⊗B′op). The same arguments as forT show
that A′⊗AS→S′is an isomorphism inD(A′⊗Bop).
We now calculate:
S′⊗L
B′T′= (A′⊗AS⊗BB′)⊗L
B′(B′⊗BT⊗AA′)
∼= (A′⊗AS)⊗L
B (B′⊗BT⊗AA′)∼=†(A′⊗AS)⊗L
B (T⊗AA′)
∼=A′⊗A (S⊗L
BT )⊗AA′)∼=A′⊗AA⊗AA′∼=A′
in D(A′en). We used the associativity of (−⊗L
(−)−) several times, and also the
ring isomorphism A′⊗A A′∼= A′. The isomorphism ∼=†is by formula (14.5.16).
Similarly we show thatT′⊗L
A′S′∼=B′in D(B′en). □
Theorem 14.5.17([132], [165]). LetA and B be ﬂat centralK-rings, and assume
A is commutative with connected spectrum. LetT be a tiltingB-A-bimodule com-
plex. Then there is an isomorphismT∼=P [n] in D(B⊗Aop), for some invertible
B-A-bimoduleP and some integern.
See Remark 14.5.32 regarding the history of this theorem.
Proof. Because A is commutative we haveA = Aop. The ring homomorphismgT
makes B into a centralA-ring. We may assumed thatA⁄= 0, and henceT ⁄= 0.
The complexT is algebraically perfect overA, so it has bounded cohomology, say
with sup(H(T )) =i1∈Z. By Lemma 14.1.27 theA-module P := Hi1(T ) is ﬁnitely
presented.
For a prime p∈Spec(A), with corresponding local ring Ap, we write Pp :=
P⊗AAp. DeﬁneY ⊆Spec(A) to be the support ofP, i.e.
Y :={p∈Spec(A)|Pp⁄= 0}.
This is a nonempty set. SinceP is ﬁnitely generated it follows thatY is a closed
subset of Spec(A); see [28, Proposition II.4.17].
318
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Take any primep∈Y, and letBp := B⊗AAp. Then, by Lemma 14.5.15, the
complex
Tp :=Bp⊗BT⊗AAp∈D(Bp⊗Aop
p )
is a tiltingBp-Ap-bimodule complex. Since Hi1(Tp)∼= Pp ⁄= 0, Theorem 14.5.7
implies that
(14.5.18) Tp∼=Pp[−i1]∈D(Bp⊗Aop
p ),
and thatPp is an invertibleBp-Ap-bimodule. In particular,Pp is a nonzero ﬁnitely
generated projective Ap-module. Thus Pp is a free Ap-module, of rank rp > 0.
Recall that P is a ﬁnitely presentedA-module. According to [28, Section II.5.1,
Corollary] there is an open neighborhoodU of p in Spec(A) on whichP is free of
rank rp. In particularPq⁄= 0 for all q∈U. ThereforeU⊆Y.
The conclusion is thatY is also open inSpec(A). Since Spec(A) is connected,
it follows that Y = Spec(A). Another conclusion is that P is projective as an
A-module – see [28, Section II.5.2, Theorem 1].
Going back to equation (14.5.18) we see thatHi(T )p∼= Hi(Tp) = 0 for alli⁄=i1.
Therefore Hi(T ) = 0 for i⁄=i1. By truncation we get an isomorphismT∼=P [n] in
D(B⊗Aop), wheren :=−i1. Finally, by Proposition 14.5.3 theB-A-bimodule P
is invertible. □
Let A be a commutative ring. AnA-module P can be viewed as a centralA-
bimodule. IfP is a rank1 projectiveA-module, then as a bimodule it is invertible.
The usual Picard group ofA (see [63, Section II.6]) is then the subgroupPicA(A) of
PicK(A), whose elements are the isomorphism classes of the centralA-bimodules;
and we refer to it here as thecommutative Picard group ofA.
Exercise 14.5.19.LetAbe a commutative ring. We denote byAutK(A)the group
of ring automorphisms ofA (i.e. the Galois group). Show that
PicK(A)∼= AutK(A)⋉ PicA(A).
(Hints: (1) Every invertibleA-bimodule P is isomorphic toP′⊗AP′′, whereP′is
free of rank 1 as a leftA-module, and P′′is a central invertible bimodule. This
is proved like Theorem 14.5.17. (2) IfP′is an invertibleA-bimodule that’s free
of rank 1 as a leftA-module, then it is also free as a rightA-module, with the
same basis elemente∈P′. The proof is like those of Lemma 14.5.6 and Theorem
14.5.17. Conclude that P′∼= A(γ), whereγ∈AutK(A), andA(γ) is the twisted
bimodule that is the leftA-module A, with right actionp·a :=γ(a)·p forp∈A(γ)
and a∈A.)
Corollary 14.5.20. LetA be a commutative ring with connected spectrum. Then
DPicK(A) = PicK(A)×Z.
Proof. The same as that of Corollary 14.5.10. □
Corollary 14.5.21. Let A and B be rings, and assume thatA is commutative
ring with connected spectrum. If there is an equivalence of triangulated categories
D(A)→D(B), then there is an equivalence of abelian categoriesM(A)→M(B).
In other words,A and B are Morita equivalent.
Proof. According to Theorem 14.4.30 there exists a tilting B-A-bimodule com-
plex T. Theorem 14.5.17 says thatT ∼= P [n] for an invertibleB-A-bimodule P.
Then P⊗A (−) : M(A) →M(B) is K-linear equivalence of abelian categories.
Moreover, P is a projectiveA-module of rankr for some positive integerr, and
B∼= EndA(P )op. □
319
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Remark 14.5.22.In the situation of Corollary 14.5.21, we can viewB as a central
A-ring, using the homomorphismgT from Deﬁnition 14.5.14. ThenB is an Azu-
mayaA-ring; see [130, Section 5.3]. Moreover, lettingX := Spec(A), and lettingB
be the sheaﬁﬁcation ofB to X, thenB is a trivial AzumayaOX-ring, in the sense
of [108, Section IV.2].
Let A be a commutative ring. If Spec(A) has a ﬁnite connected component
decomposition, in the sense of Deﬁnition 13.1.50(1), then the connected component
decomposition ofA is A =∏m
i=1 Ai, see Deﬁnition 13.1.50(2).
Corollary 14.5.23. LetA and B be rings. AssumeA is commutative, and it has
a ﬁnite connected component decompositionA =∏m
i=1 Ai. LetT be a tiltingB-A-
bimodule complex. We considerB as a centralA-ring via the isomorphismgT from
Deﬁnition14.5.14. Then T∼=⨁m
i=1Pi[ni] in D(B⊗Aop), whereBi := Ai⊗AB,
Pi is an invertibleBi-Ai-bimodule, andni∈Z.
Corollary 14.5.24. LetA be a commutative ring, and assume it has a ﬁnite con-
nected component decompositionA =∏m
i=1 Ai. Then
DPicK(A) = PicK(A)×Zm.
Corollary 14.5.25. LetA and B be rings. Assume thatA is commutative and it
has a ﬁnite connected component decomposition. If there is an equivalence of trian-
gulated categoriesD(A)→D(B), then there is an equivalence of abelian categories
M(A)→M(B).
Exercise 14.5.26. Prove Corollaries 14.5.23, 14.5.24 and 14.5.25. Cf. Exercise
13.1.54.
The general case of these last three corollaries, namely whenA does not have a
ﬁnite connected component decomposition, is dealt with in [172, Theorem 6.13].
Remark 14.5.27.The results in this subsection have variants in which the ﬂatness
condition on theK-rings A and B is dropped.
For instance, Theorem 14.5.7 can be modiﬁed as follows: IfA and B are rings,
with A local, and if T is a pretilting B-A-bimodule complex, then there is an
isomorphism T ∼= P [n] in D(A⊗Bop) for some invertibleB-A-bimodule P and
some integern. Here is an outline of the proof. One chooses nonpositive K-ﬂat
resolutions ˜A→A and ˜B→B in DGRng/cK. Next a version of the Künneth trick
(Lemma 14.5.1) for nonpositive DG rings has to be proved: ForM∈D−( ˜B⊗˜Aop)
andN∈D−( ˜A⊗˜Bop) satisfying sup(H(M))≤i1 and sup(H(N))≤j1, there is an
isomorphism
Hi1+j1(M⊗L
˜AN)∼= Hi1(M)⊗A Hj1(N)
in M(Ben). Then the proof of Theorem 14.5.7 is repeated, for the tilting DG
bimodule T∈D( ˜A⊗˜Bop).
The proofs of the other results are along the same lines.
Remark 14.5.28. Assume A is a commutative DG ring (Deﬁnitions 3.1.22 and
3.3.4), with reduction ¯A = H0(A). Here we do not need to assume ﬂatness over the
base ringK. A DG A-module can be viewed as a central DGA-bimodule, so we
have a derived tensor product
(−⊗L
A−) : D(A)×D(A)→D(A).
This operation is symmetric, i.e.S⊗L
AT∼=T⊗L
AS.
A DGA-module T is called atilting DGA-module if there is someS∈D(A)
such thatS⊗L
AT∼= A. The commutative derived Picard groupof A is the group
DPicA(A), whose elements are the isomorphism classes inD(A) of the tilting DG
320
Derived Categories | Amnon Yekutieli | 14 Apr 2019
modules, the multiplication is induced by(−⊗L
A−), and the unit is the class ofA.
It is an abelian group.
In[172, Theorem6.14]itwasprovedthatthegrouphomomorphism DPicA(A)→
DPic ¯A( ¯A), which induced by the derived reduction functor¯A⊗L
A (−), is bijective.
If the commutative ring ¯A has a ﬁnite connected component decompositionA =∏m
i=1Ai, then there is an isomorphism
DPic ¯A( ¯A)∼= Pic ¯A( ¯A)×Zm.
This is according to Corollary 14.5.24 withK = ¯A.
As Corollaries 14.5.10 and 14.5.20 show, if the ringA is either local, or commu-
tative with connected spectrum, then the groupDPicK(A) is not very interesting:
it is
(14.5.29) DPicK(A) = PicK(A)×⟨σ⟩,
where PicK(A) is the classical contribution, and⟨σ⟩∼=Z is the subgroup generated
by the elementσ, which is the class of the tilting complexA[1].
The next example shows that matters are very diﬀerent whenA is neither com-
mutative nor local.
Example 14.5.30. LetK be an algebraically closed ﬁeld and letn be an integer
≥2. Consider the ring A of upper-triangular n×n matrices. For n = 2 it is
A =
K K
0 K

. The groupDPicK(A) contains a new element in this case. The classical
NC Picard groupPicK(A) is trivial here. But the bimoduleA∗:= HomK(A,K) is
tilting, and its classµ∈DPicK(A) satisﬁes
(14.5.31) µn+1 =σn−1.
This was calculated by A. Yekutieli (forn = 2) and E. Kreines (forn≥3) in
[165]. Whenn = 2 this says thatσ=µ3, so the groupDPicK(A) is larger than the
classical part PicK(A)×⟨σ⟩=⟨σ⟩∼=Z.
Later, in [109], J.-I. Miyachi and Yekutieli showed that the groupDPicK(A) is
abelian, it is generated byσand µ, and the only relation is (14.5.31). Note that
the ringA is isomorphic to the path ringK[Q] of the Dynkin quiverQ of type An
with all arrows going in the same direction. The paper [109] contains calculations
of the groupsDPicK(A) for several other types of path rings of quivers.
M. Kontsevich interprets the relation (14.5.31) as follows: thefractional Calabi-
Yau dimensionof the “noncommutative smooth proper space”Db
f (A) is n−1
n+1. More
on this in Remark 18.6.20 and Example 18.6.24.
Remark 14.5.32.Here are a few historical notes on Theorems 14.5.7 and 14.5.17.
The concept of derived Picard group was discovered independently, around 1997,
by R. Rouquier and A. Zimmermann [132] (who had used the notationTrPic(A)
for this group) and Yekutieli [165]. The motivations of the two teams of authors
were very diﬀerent: Rouquier and Zimmermann were interested in invariants of ﬁ-
nite dimensional algebras, whereas Yekutieli was trying to classify noncommutative
dualizing complexes (See Section 18).
Remark 14.5.33. Suppose K is an algebraically closed ﬁeld andA is a ﬁnite
K-ring. It turns out that in this case the group DPicK(A) is a locally algebraic
group. Namely there is a connected algebraic groupDPic0
K(A), and DPicK(A) it
is a (usually inﬁnite) disjoint union of connected algebraic varieties, that are left
and right cosets ofDPic0
K(A). This same sort of geometric structure can be found
in the Picard scheme of a smooth projective algebraic variety X, in which the
identity component is theJacobian varietyof X. But whereas the Picard scheme
is an abelian group scheme, the groupDPicK(A) is not abelian; and this means
321
Derived Categories | Amnon Yekutieli | 14 Apr 2019
that there is a nontrivial geometric action ofDPic0
K(A), by conjugation, on the
connected components.
The result above is in the paper [167], and it is based on the papers [69] by B.
Huisgen-Zimmermann and M. Saorin, and [131] by Rouquier.
Later B. Keller [81] used an abstraction of this idea – essentially viewing the
derived Picard group as a derived group stack (evaluating it on commutative ar-
tinian DG rings) – to prove that theHochschild cohomologyofA is theLie algebra,
in the derived sense, ofDPicK(A). This allowed him to prove that the Hochschild
cohomology ofA, with itsGerstenhaber Lie bracket, is a derived invariant ofA.
322
Derived Categories | Amnon Yekutieli | 14 Apr 2019
