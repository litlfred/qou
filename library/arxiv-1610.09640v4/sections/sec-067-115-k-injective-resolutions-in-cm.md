---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-067-115-k-injective-resolutions-in-cm
section_title: "K-Injective Resolutions in C+(M)"
section_number: 11.5
pages: 208-221
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
category, and C(M) is the category of complexes in M. Coﬁltrations and their
limits were introduced in Deﬁnition 11.2.23.
Deﬁnition 11.5.1.Let I be a complex inC(M).
(1) A semi-injective coﬁltrationon I is a coﬁltrationG = {Gq(I)}q≥−1 in
Cstr(M) such that:
•G−1(I) = 0.
•Each GrG
q (I) is a complex of injective objects ofM with zero diﬀeren-
tial.
•I = lim←q Gq(I).
(2) The complex I is called asemi-injective complexif it admits some semi-
injective coﬁltration.
Theorem 11.5.2. Let M be an abelian category, and letI be a semi-injective
complex in C(M). ThenI is K-injective.
Proof. The proof is very similar to that of Theorem 11.3.2.
Step 1. We start by proving that ifI = Tp(J), the translation of an injective object
J∈M, thenI is K-injective. This is easy: given an acyclic complexN∈C(M), we
have
HomM(N,I ) = HomM
(
N, Tp(J)
{∼= Tp(
HomM(N,J )
{
in Cstr(K). But HomM(−,J ) is an exact functorM→M(K), so HomM(N,J ) is an
acyclic complex.
Step 2. Now I is a complex of injective objects ofM with zero diﬀerential. This
means thatI∼=∏
p∈Z Tp(Jp) in Cstr(M), where eachJp is an injective object inM.
But then
HomM(N,I )∼=

p∈Z
HomM
(
N, Tp(Jp)
{
.
208
Derived Categories | Amnon Yekutieli | 14 Apr 2019
This is an easy case of Proposition 1.8.6(2). By step 1 and the fact that a product
of acyclic complexes inCstr(K) is acyclic (itself an easy case of the Mittag-Leﬄer
argument), we conclude thatHomM(N,I ) is acyclic.
Step 3. Fix a semi-injective coﬁltrationG ={Gq(I)}q≥−1 ofI. Here we prove that
for everyq the complexGq(I) is K-injective. This is done by induction onq. For
q =−1 it is trivial. Forq≥0 there is an exact sequence of complexes
(11.5.3) 0→GrG
q (I)→Gq(I)→Gq−1(I)→0
in Cstr(M). In each degreep∈Z the exact sequence
0→GrG
q (I)p→Gq(I)p→Gq−1(I)p→0
in Msplits, becauseGrG
q (I)p is an injective object. Thus the exact sequence (11.5.3)
is split in the categoryGstr(M) of graded objects inM.
LetN∈C(M) be an acyclic complex. Applying the functorHomM(N,−) to the
sequence of complexes (11.5.3) we obtain a sequence
(11.5.4) 0→HomM
(
N, GrG
q (I)
{
→HomM
(
N,Gq(I)
{
→HomM
(
N,Gq−1(I)
{
→0
in Cstr(K). Because (11.5.3) is split exact inGstr(M), the sequence (11.5.4) is split
exact in Gstr(K). Therefore (11.5.4) is exact inCstr(K).
By the induction hypothesis the complexHomM
(
N,Gq−1(I)
{
is acyclic. By step
2 the complexHomM
(
N, GrG
q (I)
{
is acyclic. The long exact cohomology sequence
associated to (11.5.4) shows that the complexHomM
(
N,Gq(I)
{
is acyclic too.
Step 4. We keep the semi-injective coﬁltrationG ={Gq(I)}q≥−1 from step 3. Take
any acyclic complexN∈C(M). By Proposition 1.8.6 we know that
HomM(N,I )∼= lim
←q
HomM
(
N,Gq(I)
{
in Cstr(K). According to step 3 the complexesHomM
(
N,Gq(I)
{
are all acyclic. The
exactness of the sequences (11.5.4) implies that the inverse system{
HomM
(
N,Gq(I)
{}
q≥−1 in Cstr(K) has surjective transitions. Now the Mittag-
Leﬄer argument (Corollary 11.1.8) says that the inverse limit complexHomM(N,I )
is acyclic. □
Proposition 11.5.5.Let M be an abelian category. IfI is a bounded below complex
of injectives, thenI is a semi-injective complex.
Proof. We can assume thatI⁄= 0. Let p0 := inf(I)∈Z. Forq≥−1 let Gq(I) :=
stt≤p0+q(I), the stupid truncation from Deﬁnition 11.2.11. The coﬁltrationG =
{Gq(I)}q≥−1 is semi-injective. □
The next theorem is [62, Lemma I.4.6(1)]. See also [75, Proposition 1.7.7(i)].
Theorem 11.5.6.Let M be an abelian category, and letJ⊆M be a full subcategory
such that every objectM ∈M admits a monomorphism M ↣ I to some object
I∈J. Then every complexM∈C+(M) admits a quasi-isomorphismρ:M→I in
C+
str(M), such thatinf(I) = inf(M), and eachIp is an object ofJ.
Proof. The proof is the same as that of Theorem 11.3.6, except for a mechanical
reversal of arrows. To be more explicit, let us takeN := Mop and Q := J. Since
monomorphisms in M become epimorphisms in N, the full subcategory Q ⊆N
satisﬁes the assumptions of Theorem 11.3.6. By Theorem 3.9.16 we have a canonical
isomorphismofcategories C−
str(N)
≃
− →C+
str(M)op. Thusaquasi-isomorphism Q→N
in C−
str(N) gives rise to a quasi-isomorphismM→I in C+
str(M). □
209
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 11.5.7.Let M be an abelian category, and letM′⊆M be a full abelian
subcategory. We say that M′has enough injectives relative toM if every object
M ∈M′admits a monomorphism M ↣ I, where I is an object of M′that is
injective in the bigger categoryM.
Of course, in this situation the categoryM′itself has enough injectives.
Thick abelian categories were deﬁned in Deﬁnition 7.4.1. The next theorem is
[62, Lemma I.4.6(3)]. See also [75, Proposition 1.7.11].
Theorem 11.5.8.Let M be an abelian category, and letM′⊆M be a thick abelian
subcategory that has enough injectives relative toM. Let M∈C(M) be a complex
with bounded below cohomology, such thatHi(M)∈M′for all i. Then there is a
quasi-isomorphism ρ: M →I in Cstr(M), such thatI∈C+(M′), each Ip is an
injective object inM, and inf(I) = inf(H(M)).
Before the proof we need some auxiliary material.
Suppose we are given morphismsψ1 : K→L1 and ψ2 : K→L2 in M. The
ﬁbered coproductis the object
(11.5.9) L1⊕KL2 := Coker
(
(ψ1,−ψ2) :K→L1⊕L2
{
in M. It has an obvious universal property. The commutative diagram
(11.5.10) K
ψ1 //
ψ2

L1
ϵ1

L2
ϵ2 //L1⊕KL2
in whichϵi are the morphisms induced by the embeddingsLi→L1⊕L2, is some-
times called apushout diagram.
Lemma 11.5.11. In the situation above:
(1) The sequence
Ker(ψ1)
ψ2
− − →L2
ϵ2
−→L1⊕KL2
π1
−→Coker(ψ1)→0,
in whichπ1 is the morphism induced by the projectionL1⊕L2→L1, is
exact.
(2) SupposeL1→L′
1 be a monomorphism. Then the induced morphismL1⊕K
L2→L′
1⊕KL2 is a monomorphism.
Exercise 11.5.12. Prove Lemma 11.5.11. (Hint: use the ﬁrst sheaf trick, Propo-
sition 2.4.9.)
Proof of Theorem11.5.8. The proof is an adaptation of the proof of [75, Proposi-
tion 1.7.11]. In the proof we use the objects of cocyclesZp(L), coboundaries Bp(L)
and decocycles Yp(L), that are associated to a complexL and an integerp; see
Deﬁnition 3.2.4.
Step 1. We can assume thatH(M)⁄= 0. By translatingM, we may further assume
that inf(H(M)) = 0. Then, after replacingM with its smart truncationsmt≥0(M),
we can assume thatinf(M) = 0.
We are going to construct an inverse system
(11.5.13) Fp(I) =
(
···→0→I0 d0
I
−→I1 d1
I
−→···
dp−1
I
−−−→Ip→0→···
{
in Cstr(M′), indexed byp≥−1, such that the objectsIp∈M′are injective inM.
The morphismFp+1(I)→Fp(I) will send the objectIp+1 =Fp+1(I)p+1 to 0, and
210
Derived Categories | Amnon Yekutieli | 14 Apr 2019
will be the identity in all other degrees. Simultaneously we will construct an inverse
system of morphisms
(11.5.14) Fp(φ) :M→Fp(I)
in Cstr(M). The construction will be inductive. The morphismsFp(φ) will satisfy
this condition:
(♥) The morphismHq(Fp(φ)) : Hq(M)→Hq(Fp(I)) is a monomorphism for all
q≤p and an isomorphism for allq≤p−1.
Then the complexI := lim←pFp(I) in C(M′) is going to be of the required kind,
and the morphismφ:= lim←pFp(φ) in Cstr(M) is going to be a quasi-isomorphism.
Notethattheseinverselimitsareinnocent, sinceineachdegree q theinversesystems
{Fp(I)q}p≥−1 and{Fp(φ)q}p≥−1 are eventually stationary.
Step 2. In this step we begin the construction. Here p≥ −1, and we have a
complexFp(I) as in (11.5.13) of the kind described above, and a morphismFp(φ) :
M→Fp(I) in Cstr(M) satisfying condition (♥). If p =−1 then F−1(I) = 0 and
F−1(φ) = 0 of course.
Weclaimthattheobjects Fp(I)q, Hq(Fp(I)), Bq(Fp(I)), Yq(Fp(I))and Zq(Fp(I))
belong to M′for allq∈[0,p + 1]. For q = p + 1 all these objects are zero. For
Fp(I)q = Iq it is given. For Hp(Fp(I)) = Coker(d p−1
I ) it is because M′is a full
abelian subcategory of M. For Hq(Fp(I)) when q < pwe use the isomorphisms
Hq(Fp(φ)) and the fact thatHq(M)∈M′. As for the rest of the objects listed, this
is shown by descending induction onq, starting fromq =p, using these short exact
sequences
0→Zq(Fp(I))→Fp(I)q→Bq+1(Fp(I))→0,
0→Bq(Fp(I))→Fp(I)q→Yq(Fp(I))→0,
0→Bq(Fp(I))→Zq(Fp(I))→Hq(Fp(I))→0,
and the fact thatM′is a full abelian subcategory ofM.
Step 3. The construction continues. Let us denote the components of the morphism
Fp(φ) byφq :=Fp(φ)q :Mq→Fp(I)q =Iq for q∈[0,p ]; outside this degree range
we haveFp(φ)q = 0.
The diﬀerentialdp
M :Mp→Mp+1 induces a morphismψ1 : Yp(M)→Zp+1(M).
There is also the morphismψ2 := Yp(φ) : Yp(M)→Yp(Fp(I)). We deﬁneN to be
the ﬁbered coproduct
(11.5.15) N := Zp+1(M)⊕Yp(M) Yp(Fp(I))
relative to the morphismsψ1 and ψ2. In the notation of Lemma 11.5.11, with
the objects K := Yp(M), L1 := Zp+1(M) and L2 := Yp(Fp(I)), and with the
morphismψ1,ψ2 thatwehavejustdeﬁned, therearemorphisms ϵ1 : Zp+1(M)→N,
ϵ2 : Yp(Fp(I))→N and π1 : N→Coker(ψ1) = Hp+1(M). According to Lemma
11.5.11(1) there is an exact sequence
(11.5.16) Hp(M)
ψ2
− − →Yp(Fp(I))
ϵ2
−→N
π1
−→Hp+1(M)→0
in M. However, letting β: Hp(Fp(I))→Yp(Fp(I)) be the canonical monomor-
phism, there is equalityψ2 =β◦Hp(Fp(φ)). By condition (♥) with indicesq =p
we know that Hp(Fp(φ)) is a monomorphism. Therefore ψ2 is a monomorphism,
and (11.5.16) extends to a slightly longer exact sequence
(11.5.17) 0→Hp(M)
ψ2
− − →Yp(Fp(I))
ϵ2
−→N
π1
−→Hp+1(M)→0
in M.
211
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Let γ: Zp+1(M)↣ Mp+1 be the canonical monomorphism, and deﬁneψ+
1 :=
γ◦ψ1 : Yp(M)→Mp+1. Let ψ+
2 := ψ2 : Yp(M)→Yp(Fp(I)). We have the
corresponding ﬁbered coproduct
(11.5.18) N+ :=Mp+1⊕Yp(M) Yp(Fp(I)).
The monomorphism γ: Zp+1(M)↣ Mp+1 induces a morphism ω: N →N+
between these ﬁbered coproducts, and Lemma 11.5.11(2) says thatωis also a
monomorphism.
Step 4. We now produce the object Ip+1 ∈M′. In step 2 we showed that
Yp(Fp(I)) ∈M′. It is given that Hq(M) ∈M′for all q. The exact sequence
(11.5.16) and Proposition 7.4.2 say thatN ∈M′too. By assumption there is a
monomorphism χ: N↣ Ip+1 into some objectIp+1∈M′that’s injective inM.
Because ω: N→N+ is a monomorphism, there is a morphismχ+ : N+→Ip+1
such thatχ+◦ω=χ.
We have a canonical epimorphismαI : Ip↠ Yp(Fp(I)). Deﬁne the morphism
dp
I : Ip→Ip+1 by the formuladp
I := χ◦ϵ2◦αI. Since αI·dp−1
I = 0, we see that
dp
I◦dp−1
I = 0. This is depicted in the commutative diagram below.
Ip−1
dp−1
I
//
0
%%
Ip αI //
dp
I
88Yp(Fp(I))
ϵ2 //N
χ //Ip+1
Therefore we obtain a new complex
(11.5.19) Fp+1(I) :=
(
···→0→I0 d0
I
−→I1 d1
I
−→···
dp−1
I
−−−→Ip dp
I
−→Ip+1→0→···
{
in C(M′), and it projects ontoFp(I).
Step 5. In this step we construct the morphismφp+1 : Mp+1→Ip+1. Let ϵ+
1 :
Mp+1→N+ be the morphism that’s part of the ﬁbered coproduct (11.5.18). We
deﬁne the morphismφp+1 :Mp+1→Ip+1 by the formulaφp+1 :=χ+◦ϵ+
1 .
Let’s examine the next diagram, whereαM : Mp ↠ Yp(M) is the canonical
epimorphism, andψ+
1 , ψ+
2 =ψ2, ϵ+
1 , ϵ+
2 and ϵ2 are the morphisms involved in the
two ﬁbered coproducts.
(11.5.20) Mp αM //
φp

Yp(M)
ψ+
1 //
ψ+
2

Mp+1 ϵ+
1 //N+ χ+
//Ip+1
id

Ip αI // Yp(Fp(I))
ϵ2 //
ϵ+
2
55
N
χ //
ω
OO
Ip+1
The left square is commutative becauseα: Id→Y is a morphism of functors. The
triangle that hasYp(M) as a vertex is commutative becauseN+ is the ﬁbered co-
product. The other triangle, the one that hasN as a vertex, is commutative because
ωis a morphism between ﬁbered coproducts. The right square is commutative by
the deﬁning property ofχ+. So the whole diagram is commutative.
212
Derived Categories | Amnon Yekutieli | 14 Apr 2019
We now take part of the commutative diagram (11.5.20), and add to it three
curved arrows.
(11.5.21) Mp αM //
φp

dp
M
’’
Yp(M)
ψ+
1 //Mp+1 ϵ+
1 //
φp+1
%%
N+ χ+
//Ip+1
id

Ip αI //
dp
I
66Yp(Fp(I))
ϵ2 //N
χ //Ip+1
The curved polygons are commutative, as can be seen from the deﬁnitions of the
morphisms ψ+
1 , φp+1 and dp
I. We conclude thatdp
I◦φp =φp+1◦dp
M, so there is a
new morphism of complexesFp+1(φ) :M→Fp+1(I) whose degreep+1 component
is φp+1.
Step 6. Here we prove thatHp+1(Fp+1(φ)) is a monomorphism andHp(Fp+1(φ)) is
an isomorphism. This will verify condition (♥) with indexp + 1.
Consider the ﬁbered coproduct
(11.5.22) N♦ :=Ip+1⊕Yp(Fp(I)) Yp(Fp(I))
of the morphisms ψ♦
1 and ψ♦
2, where ψ♦
1 : Yp(Fp(I)) →Ip+1 is the morphism
induced bydp
I, andψ♦
2 is the identity ofYp(Fp(I)). Note thatϵ♦
1 :Ip+1→N♦ is an
isomorphism, and Coker(ψ♦
1 ) = Yp+1(Fp+1(I)) = Hp+1(Fp+1(I)). The morphisms
φp+1 : Zp+1(M)→Ip+1 and Yp(Fp(φ)) : Yp(M)→Yp(Fp(I)) induce a morphism
ω♦ : N→N♦ between the ﬁbered coproducts (11.5.15) and (11.5.22). According
to Lemma 11.5.11(1) there is an induced commutative diagram
(11.5.23) 0 // Hp(M)
ψ2 //
Hp(Fp+1(φ))

Yp(Fp(I))
ϵ2 //
id

N
π2 //
ω♦

Hp+1(M) //
Hp+1(Fp+1(φ))

0
0 // Hp(Fp+1(I))
ψ♦
2 // Yp(Fp(I))
ϵ♦
2 //N♦ π♦
2 // Hp+1(Fp+1(I)) // 0
The ﬁrst row is an exact sequence, since it is (11.5.17). The second row is also
exact: exactness at the last three objects is by Lemma 11.5.11(1). As for exactness
at Hp(Fp+1(I)), we use the fact that the morphismYp(Fp+1(I))→Yp(Fp(I)) is an
isomorphism, and its composition with the canonical embeddingHp(Fp+1(I))↣
Yp(Fp+1(I)) is ψ♦
2, so the latter is a monomorphism. A little calculation shows
that ω♦ =ϵ♦
1◦χ, so it is a monomorphism.
Finally, a diagram chase in (11.5.23), using the ﬁrst sheaf trick, shows that
Hp+1(Fp+1(φ)) is a monomorphism, and thatHp(Fp+1(φ)) is an isomorphism. □
Corollary 11.5.24.Under the assumptions of Theorem11.5.8, the canonical func-
tor D+(M′)→D+
M′(M) is an equivalence.
Proof. This is very similar to the proof of Corollary 11.3.21, and there is no need
to repeat it. □
Here is an important instance in which Theorem 11.5.8 and Corollary 11.5.24
apply.
Example 11.5.25. Let (X,OX) be a noetherian scheme. Associated to it are
these abelian categories: the categoryM := ModOX ofOX-modules, and the thick
abelian subcategory M′:= QCohOX of quasi-coherentOX-modules. According to
213
Derived Categories | Amnon Yekutieli | 14 Apr 2019
[62, Proposition II.7.6] the category M′has enough injectives relative to M. By
Corollary 11.5.24 the canonical functor
D(QCohOX)→D+
qc(ModOX)
is an equivalence.
For a more general statement, using other methods, see [23, Corollary 5.5].
Corollary 11.5.26.If M is an abelian category with enough injectives, thenC+(M)
has enough K-injectives.
Proof. According to either Theorem 11.5.6 or Theorem 11.5.8, everyM∈C+(M)
admits a quasi-isomorphismM→I to bounded below complex of injectivesI. Now
use Proposition 11.5.5 and Theorem 11.5.2. □
Corollary 11.5.27. Let M be an abelian category with enough injectives, and let
M∈C(M) be a complex with bounded below cohomology. ThenM has a K-injective
resolutionM→I, such thatinf(I) = inf(H(M)), and everyIp is an injective object
of M.
Proof. We may assume thatH(M) is nonzero. Let p := inf(H(M))∈Z, and let
N := smt≥p(M), the smart truncation from Deﬁnition 7.3.6. SoM→N is a quasi-
isomorphism, and inf(N) = p. According to either Theorem 11.5.6 or Theorem
11.5.8, there is a quasi-isomorphismN→I, whereI is a complex of injectives and
inf(I) =p. By Proposition 11.5.5 and Theorem 11.5.2 the complexI is K-injective.
The composed quasi-isomorphismM→I is what we are looking for. □
11.6. K-Injective Resolutions inC(A). Recall that we are working over a non-
zero commutative base ringK, andA is a central DGK-ring.
An injective cogeneratorof the abelian categoryM(K) = ModK is an injective
K-moduleK∗with this property: ifM is a nonzeroK-module, then HomK(M,K∗)
is nonzero. These always exist. Here are a few examples.
Example 11.6.1. For everyK there is a canonical choice for an injective cogen-
erator: K∗:= HomZ(K,Q/Z). See proof of Theorem 2.7.13. Usually this is a very
big module!
Example 11.6.2. Assume K is a complete noetherian local ring, with maximal
ideal m and residue ﬁeldℸ =K/m. In this case we would prefer to take the smallest
possible injective cogeneratorK∗, and this is the injective hull ofℸ as aK-module.
Here are some special cases. IfK is a ﬁeld, thenK∗=K =ℸ. IfK =ˆZp, the ring
of p-adic integers, thenℸ =Fp, andK∗∼= ˆQp/ˆZp, which is thep-primary part of
Q/Z. IfK contains some ﬁeld, then there exists a ring homomorphismℸ→K that
lifts the canonical surjectionK→ℸ. (This is by the Cohen Structure Theorem,
see [46, Theorem 7.7].) After choosing such a lifting, there is an isomorphism of
K-modulesK∗∼= Homcont
ℸ (K,ℸ), where continuity is for them-adic topology onK
and the discrete topology onℸ.
In this subsection we have the following standing convention.
Convention 11.6.3.There is a ﬁxed injective cogeneratorK∗of M(K).
We viewK∗as a DGK-module concentrated in degree0 (with zero diﬀerential).
For everyp∈Z there is the DGK-module T−p(K∗), which is concentrated in
degree p.
It will be convenient to blur the distinction between DGK-modules with zero
diﬀerentials and gradedK-modules. Namely, if N is a DGK-module such that
dN = 0, we will identifyN with the graded modulesN♮, H(N), etc.
214
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 11.6.4.For a DGK-module V we deﬁne the DGK-module V∗:=
HomK(V,K∗).
The operation (−)∗is an exact contravariant functor fromCstr(K) to itself, and
also from Gstr(K) to itself. Note that givenM∈C(A), its dualM∗is an object of
C(Aop), so that we have an exact functor
(11.6.5) (−)∗: Cstr(A)op→Cstr(Aop).
Deﬁnition 11.6.6.A DGK-module W is calledcofreeif there is an isomorphism
W∼=V∗in Cstr(K), for some free DGK-module V.
Since the diﬀerential of a free DGK-module V is zero, we see that a cofree DG
module W also has zero diﬀerential.
Lemma 11.6.7. LetV be a free DGK-module, and letW :=V∗.
(1) If V ∼=⨁
s∈S Tps(K) for some indexing setS and some collection of inte-
gers{ps}s∈S, thenW∼=∏
s∈S T−ps(K∗).
(2) As an object of the abelian categoryGstr(K), W is injective.
In item (1) the isomorphisms can be considered either inCstr(K) or in Gstr(K);
it doesn’t matter, becauseV and W have zero diﬀerentials. However, item (2) is
true only in the categoryGstr(K).
Lemma 11.6.8. Letφ:U→V be a homomorphism inGstr(K).
(1) φis injective iﬀφ∗:V∗→U∗is surjective.
(2) φis surjective iﬀφ∗:V∗→U∗is injective.
(3) The canonical homomorphismU→U∗∗= (U∗)∗in Gstr(K) is injective.
(4) There exists an injective homomorphismU ↣ W in Gstr(K) into some
cofree DGK-moduleW.
Exercise 11.6.9. Prove Lemmas 11.6.7 and 11.6.8.
Deﬁnition 11.6.10.Let W be a cofree DGK-module. The cofree DGA-module
coinduced fromW is the DGA-module IW := HomK(A,W ). There is a homomor-
phism θW :IW→W in Cstr(K), with formulaθW (χ) :=χ(1A)∈W.
Deﬁnition 11.6.11.A DGA-module J is calledcofreeif there is an isomorphism
J∼=IW in Cstr(A) for some cofree DGK-module W.
Lemma 11.6.12. Consider the free DGK-module V := ⨁
s∈S Tps(K) and the
cofree DGK-moduleW :=V∗. There are canonical isomorphisms
IW∼= (A⊗V )∗∼=
(⨁
s∈S
Tps(A)
{∗
∼=

s∈S
T−ps(A∗)
in Cstr(A).
Exercise 11.6.13. Prove the lemma above.
Lemma 11.6.14. LetW be a cofree DGK-module, and letM be a DGA-module.
The homomorphism
Hom(idM,θW ) : HomA(M,IW )→HomK(M,W )
in Cstr(K) is an isomorphism.
Proof. The homomorphism
Hom(idM,θW ) : HomA
(
M, HomK(A,W )
{≃
− →HomK(M,W )
is just adjunction for the DG ring homomorphismK→A, so it is bijective. □
215
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Recall that Gstr(A♮) is the abelian category whose objects are the gradedA♮-
modules, and the morphisms are theA-linear homomorphisms of degree 0. The
forgetful functor Und : Cstr(A)→Gstr(A♮), M↦→M♮, is faithful.
Lemma 11.6.15. Let I be a cofree DGA-module. Then I♮is an injective object
of Gstr(A♮).
Proof. We can assume thatI = IW for some cofree DGK-module W. For every
M∈Gstr(A♮) there are isomorphisms
HomGstr(A♮)
(
M,I ♮
W
{
= HomA(M,IW )0
∼=♥HomK(M,W )0 =

p∈Z
HomK(Mp,W p)
in M(K). The isomorphism ∼=♥is by Lemma 11.6.14. For every p the functor
Gstr(A♮)→M(K), M↦→Mp, is exact. Because eachWp is an injective object of
M(K), the contravariant functorHomK(−,W p) from M(K) to itself is exact. And
the product of exact functors intoM(K) is exact. We conclude that the functor
HomGstr(A♮)
(
−,I♮
W
{
is exact. □
Recall that for a DGK-module M we have the object of decocycles
Y(M) := Coker
(
dM : T−1(M)→M
{
=M/ B(M)∈G(K).
Lemma 11.6.16. Let W be a cofree DGK-module, let M be a DGA-module,
and let χ: Y(M)→W be a homomorphism inGstr(K). Then there is a unique
homomorphism ψ:M→IW in Cstr(A), such that the diagram
Y(M)
Y(ψ) //
χ

Y(IW )
Y(θW ) // Y(W ) =W
in Gstr(K) is commutative.
Proof. Since the diﬀerentials ofW and Y(M) are zero, the canonical homomor-
phism
α: HomK(Y(M),W )0 = Z0(
HomK(Y(M),W )
{
→Z0(
HomK(M,W )
{
,
that’s induced by the canonical surjectionM↠ Y(M), is bijective. This gives us
a unique homomorphismα(χ) : M→W in Cstr(K). Next we use Lemma 11.6.14
to obtain a uniqueψ:M→IW in Cstr(A) s.t. θW◦ψ=α(χ). Thisψis what we
are looking for. □
The next deﬁnition is dual to Deﬁnition 11.4.3.
Deﬁnition 11.6.17.Let I be an object ofC(A).
(1) A semi-cofree coﬁltrationon I is a coﬁltrationG ={Gq(I)}q≥−1 on I in
Cstr(A) such that:
•G−1(I) = 0.
•Each GrG
q (I) is a cofree DGA-module.
•I = lim←q Gq(I).
(2) The DGA-module I is called asemi-cofreeif it admits a semi-cofree coﬁl-
tration.
Proposition 11.6.18. If I is a semi-cofree DGA-module, thenI♮is an injective
object in the abelian categoryGstr(A♮).
Proposition 11.6.19. Assume A is a ring. If I is a semi-cofree DGA-module,
then eachIp is an injectiveA-module.
216
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Exercise 11.6.20. Prove the two propositions above.
Theorem 11.6.21. Let I be an object of C(A). If I is semi-cofree, then it is
K-injective.
Proof. The proof is very similar to those of Theorems 11.3.2 and 11.4.14. But
because the arguments involve limits, we shall give the full proof.
Step 1. SupposeI is cofree; sayI∼=∏
s∈S T−ps(A∗). Lemma 11.6.14 implies that
for every DGA-module N there is an isomorphism
HomA(N,I )∼=

s∈S
HomK
(
Tps(N),K∗{
of gradedK-modules. It follows that ifN is acyclic, then so isHomA(N,I ).
Step 2. Fix a semi-cofree coﬁltrationG ={Gq(I)}q≥−1 of I. Here we prove that
for everyq≥−1 the DG moduleGq(I) is K-injective. This is done by induction
on q≥−1. Forq =−1 it is trivial. Forq≥0 there is an exact sequence
(11.6.22) 0→GrG
q (I)→Gq(I)→Gq−1(I)→0
in the categoryCstr(A). Because GrG
q (I) is a cofree DGA-module, it is an injective
object in the abelian categoryGstr(A♮); see Lemma 11.6.15. Therefore the sequence
(11.6.22) is split exact inGstr(A♮).
Let N∈C(A) be an acyclic DG module. Applying the functorHomA(N,−) to
the sequence (11.6.22) we obtain a sequence
(11.6.23)
0→HomA
(
N, GrG
q (I)
{
→HomA
(
N,Gq(I)
{
→HomA
(
N,Gq−1(I)
{
→0
in Cstr(K). If we forget diﬀerentials this is a sequence inGstr(K). Because (11.6.22)
is split exact inGstr(A♮), it follows that (11.6.23) is split exact inGstr(K). Therefore
(11.6.23) is exact inCstr(K).
By the induction hypothesis the DG K-module HomA
(
N,Gq−1(I)
{
is
acyclic. By step 1 the DGK-module HomA
(
N, GrG
q (I)
{
is acyclic. The long ex-
act cohomology sequence associated to (11.6.23) shows that the DG K-module
HomA
(
N,Gq(I)
{
is acyclic too.
Step 3. We keep the semi-cofree coﬁltrationG ={Gq(I)}q≥−1 from step 2. Take
any acyclicN∈C(A). By Proposition 1.8.6 we know that
HomA(N,I )∼= lim
←j
HomA
(
N,Gq(I)
{
in Cstr(K). According to step 2 the complexesHomA
(
N,Gq(I)
{
are all acyclic. The
exactness of the sequences (11.6.23) implies that the inverse system{
HomA
(
N,Gq(I)
{}
q≥−1 in Cstr(K) has surjective transitions. Now the Mittag-
Leﬄer argument (Corollary 11.1.8) says that the inverse limit complexHomA(N,I )
is acyclic. □
Theorem 11.6.24. LetA be a DG ring. Every DGA-moduleM admits a quasi-
isomorphism ρ:M→I in Cstr(A) to a semi-cofree DGA-moduleI.
The proof of this theorem was communicated to us by B. Keller. We need a
lemma ﬁrst.
The semi-free DGA-module C was deﬁned in formula (11.4.18). Its dual DG
A-module C∗= Hom K(C,K∗) is a semi-cofree DG A-module, with semi-cofree
coﬁltrationGq(C∗) :=Fq(C)∗, whereFq(C) is from (11.4.19).
Lemma 11.6.25. LetM∈C(A).
217
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(1) There is a homomorphismψ:M→J in Cstr(A), such thatZ(ψ) : Z(M)→
Z(J) is injective, and J = ∏
s∈S T−ps(A∗) for a collection of integers
{ps}s∈S.
(2) There is an injective homomorphismψ′: M →J′in Cstr(A), such that
J′=∏
s∈S′T−ps(C∗) for some collection of integers{ps}s∈S′.
To clarify the notation in the lemma: we have two distinct collections of integers,
{ps}s∈S and{ps}s∈S′.
Proof.
(1) By Lemma 11.6.8 there is an injective homomorphismχ: Y(M)↣W for some
cofree gradedK-module W =∏
s∈S T−ps(K∗). LetJ :=IW. According to Lemma
11.6.16 there is a homomorphismψ: M→J in Cstr(A) s.t. Y(θW )◦Y(ψ) = χ.
Because χis injective, so isY(ψ).
(2) Consider the DGAop-module M∗. By Lemma 11.4.20 there is a collection of
integers{ps}s∈S′, and a surjective homomorphism φ: Q →M∗in Cstr(Aop),
where Q := ⨁
s∈S′Tps(C). Dualizing we get a DG A-module J′:= Q∗∼=∏
s∈S′T−ps(C∗), and an injective homomorphismφ∗:M∗∗→Q∗=J′in Cstr(A).
Composing φ∗with the canonical embeddingM↣M∗∗gives usψ′:M↣J′. □
The DGA-moduleJ in item (1) of the lemma is cofree. The DGA-moduleJ′in
item (2) is semi-cofree, with semi-cofree coﬁltration induced by that ofC∗, namely
(11.6.26) Gq(J′) :=

s∈S′
T−ps(Gq(C∗)).
Proof of Theorem11.6.24.
Step 1. We are going to produce an exact sequence
(11.6.27) 0→M
η
− →J0 ∂0
−→J1 ∂1
−→J2→···
in Cstr(A) with these properties:
(a) The sequence
0→Y(M)
Y(η)
−−−→Y(J0)
Y(∂0)
− −−− →Y(J1)
Y(∂1)
− −−− →Y(J2)→···
is exact inGstr(K).
(b) For everyp≥0 the DGA-module Jp has the following decomposition in
Cstr(A) : Jp = Jp⊕J′
p, where Jp = ∏
s∈Sp T−qs(A∗) and J′
p =∏
s∈S′p
T−qs(C∗) for some collection of integers{qs}s∈Sp⊔S′p.
This will be done recursively onp.
By Lemma 11.6.25 we can ﬁnd DGA-modules J0,J′
0 and homomorphismsψ0 :
M→J0,ψ′
0 :M→J′
0, suchthatboth Y(ψ0)andψ′
0 areinjective. TheDGmodules
J0,J′
0 are of the required form (property (b) withp = 0). We letJ0 :=J0⊕J′
0 and
η:=ψ0⊕ψ′
0.
Let N0 := Coker(η). Then the sequence
(11.6.28) 0→M
η
− →J0→N0→0
in Cstr(A) is exact. The sequence
0→Y(M)
Y(η)
−−−→Y(J0)→Y(N0)→0
in Gstr(K) is also exact. Indeed, the exactness at Y(J0) and Y(N0) is because
the functor Y : Cstr(K) →Gstr(K) is right exact (see Proposition 3.8.14), and
the sequence (11.6.28) is exact. The exactness at Y(M) is by the injectivity of
Y(ψ0) : Y(M)→Y(J0).
218
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Next we repeat this procedure withN0 instead ofM, to obtain an exact sequence
(11.6.29) 0→N0 ∂0
−→J1→N1→0,
with J1 of the required form (property (b) withp = 1), and such that
0→Y(N0)
Y(∂0)
− −−− →Y(J1)→Y(N1)→0
is also exact. We then splice (11.6.28) and (11.6.29) to get the exact sequence
0→M
η
− →J0 ∂0
−→J1→N1→0.
Continuing recursively we obtain an exact sequence (11.6.27) that has properties
(a) and (b).
Step 2. We view the exact sequence (11.6.27) as an acyclic complex with entries in
Cstr(A), that hasJ0 in degree 0. Deﬁne the total DGA-modules
I := TotΠ(
···→0→J0 ∂0
−→J1 ∂1
−→J2→···
{
and
Iaug := TotΠ(
···→0→M
η
− →J0 ∂0
−→J1 ∂1
−→J2→···
{
.
Because the sequence (11.6.27) and the sequence appearing in property (a) are
exact, we can use Proposition 11.2.24 (with anyj0∈Z). The conclusion is that
the DGA-module Iaug is acyclic. Then, by Corollary 11.2.22, the homomorphism
ρ:M→I in Cstr(A) is a quasi-isomorphism.
Step 3. It remains to produce a semi-cofree coﬁltration{Gq(I)}q≥−1 on the DG
A-module I. Our formula is this:G−1(I) := 0 of course. Forr≥0 we let
G2·r(I) :=
(⨁r−1
p=0
T−p(Jp)
{
⊕T−r(
Jr⊕G0(J′
r)
{
,
where G0(J′
r) comes from (11.6.26), and
G2·r+1(I) :=
⨁r
p=0
T−p(Jp).
We leave it to the reader to verify that this is a semi-cofree coﬁltration. □
Corollary 11.6.30. Let A be a DG ring. The category C(A) has enough K-in-
jectives.
Proof. Combine Theorems 11.6.21 and 11.6.24. □
Recall that a DG ringA is nonpositive if Ai = 0 for all i > 0. When A is
nonpositive, the DG moduleA∗is concentrated in degrees≥0.
Corollary 11.6.31.If the DG ringA is nonpositive, then everyM∈C(A) admits
a quasi-isomorphismρ:M→I in Cstr(A) to a semi-cofree DGA-moduleI, such
that inf(I) = inf(H(M)).
Proof. Let p0 := inf(H(M)). If p0 =±∞then there is nothing to prove beyond
Theorem 11.6.24; so let us assume thatp0∈Z. DeﬁneM′:= smt≥p0(M). Then
M→M′is a quasi-isomorphism, andinf(M′) = p0. By replacingM with M′we
can now assume thatinf(M) =p0.
Since inf(M) =p0 it follows thatMp0 = Yp0(M). This means that in step 1 of
the proof of the theorem, the homomorphismψ0 :Mp0→Jp0
0 is already injective.
So, like in the proof of Corollary 11.4.27, we can arrange to haveinf(J0)≥p0.
Then, recursively, we can arrange to haveinf(Jq)≥p0 for allq. Therefore in step
2 of the proof we getinf(I)≥p0.
Finally, becauseinf(H(M)) =p0 we must haveinf(I) =p0. □
We end with the K-injective analogue of Remark 11.4.45.
219
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Remark 11.6.32. Suppose (X,A) is a ringed space. We know that the abelian
category M(A) = ModAofsheavesof A-moduleson X hasenoughinjectiveobjects.
Theorem 11.5.6 tells us that the subcategoryC+(A) has enough K-injective objects.
But in fact more is true: the category of unbounded complexes C(A) also has
enough K-injective objects; see [143]. (There is another, more abstract proof of this
statement: because M(A) is a Grothendieck abelian category, it follows thatC(A)
has enough K-injectives. See [76, Corollary 14.1.8].)
Now let’s consider a DG ringed space(X,A). Fix an injective cogeneratorK∗of
M(K). For a pointx∈X, consider the cofree DGAx-moduleIx := HomK(Ax,K∗).
Pushing this module forward along the inclusion{x}⊆X we get a constant sheaf
Ix with support the closed set{x}, that we refer to as the cofree DGA-module
associated to x. By deﬁnition, acofree DGA-module is a product of sheavesIx
(for varying pointsx∈X). Combining this notion with that of a semi-cofree DG
module, we can talk aboutsemi-cofree DGA-modules. Like Theorem 11.6.21, one
can show that a semi-cofree DGA-moduleI is K-injective.
Assume that the topological space X is ﬁnite dimensional, in the sense that
there is a natural numberd such that for every open setU ⊆X, every sheaf of
K-moduleN onU, and everyp>d , the sheaf cohomologyHp(U,N ) vanishes. This
condition is quite mild – it is satisﬁed whenX is a ﬁnite dimensional noetherian
scheme, and also whenX is a subspace of a ﬁnite dimensional topological manifold.
Then a geometric variant of Theorem 11.6.24 is true: every DGA-module M
admits a quasi-isomorphismM→Ito a semi-cofree DGA-moduleI. The ﬁnite
dimensionality ofX is needed to invoke the ML argument. A detailed proof of this
assertion will be published in the future.
220
Derived Categories | Amnon Yekutieli | 14 Apr 2019
