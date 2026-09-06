---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-105-184-graded-rigid-nc-dc
section_title: "Graded Rigid NC DC"
section_number: 18.4
pages: 429-435
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
complexesand rigid dualizing complexes. This is done by introducing an intermedi-
ate kind of object: thegraded rigid dualizing complex. All is in the noncommutative
setting of course.
The results of this subsection were originally in [153], with a few improvements
later in [183]. Here we give a much more detailed discussion, and some corrections.
429
Derived Categories | Amnon Yekutieli | 14 Apr 2019
We continue with Convention 18.1.1. In particularK is a base ﬁeld, and all rings
are by default central overK. Throughout this subsection we assume the following
setup:
Setup 18.4.1. We are given a noetherian connected graded centralK-ring ˜A and
a central homogeneous elementt∈˜A of degree 1. We deﬁne the centralK-ring
A := ˜A/(t−1).
Note that the ringA is not graded. Also the rings ˜Aen and Aen need not be
noetherian. However:
Proposition 18.4.2. Under Setup 18.4.1, the ring A is noetherian, andA is a
derived pseudo-ﬁnite complex overAen.
Proof. Use Theorem 18.3.20. □
The concepts of outside and inside actions from the beginning of Subsection
18.2 make sense in the graded setting. Thus we have a connected graded ring
˜Afour = ˜Aen,out⊗˜Aen,in. For a complex ˜M∈D( ˜Aen, gr), its tensor product with
itself ˜M⊗˜M is an object ofD( ˜Afour, gr), and
(18.4.3) RHom ˜Aen,out( ˜A, ˜M⊗˜M)∈D( ˜Aen,in, gr) = D( ˜Aen, gr).
Recall that D(f,..)( ˜Aen, gr) (resp. D(..,f)( ˜Aen, gr)) is the full subcategory of
D( ˜Aen, gr) on the complexes whose cohomology bimodules are ﬁnite over˜A (resp.
˜Aop), and
D(f,f)( ˜Aen, gr) = D(f,..)( ˜Aen, gr)∩D(..,f)( ˜Aen, gr).
Deﬁnition 18.4.4.Under Setup 18.4.1, agraded rigid NC dualizing complexover
˜A is a pair( ˜R, ˜ρ), where ˜R∈Db
(f,f)( ˜Aen, gr) is a graded NC dualizing complex over
˜A, in the sense of Deﬁnition 17.1.4; and
˜ρ: ˜R
≃
− →RHom ˜Aen,out( ˜A, ˜R⊗˜R)
is an isomorphism inD( ˜Aen, gr), see (18.4.3) with ˜M := ˜R.
Balanced dualizing complexes were introduced in Deﬁnition 17.2.2.
Theorem 18.4.5. Under Setup 18.4.1, if ˜R is a balanced NC dualizing complex
over ˜A, then ˜R is a graded rigid NC dualizing complex over˜A.
We are a bit sloppy in stating the theorem; the proper way to state it is this: if
( ˜R, ˜β) is a balanced dualizing complex over˜A, then there exists an isomorphism˜ρ
such that ( ˜R, ˜ρ) is a graded rigid NC dualizing complex over˜A.
We need a lemma ﬁrst. Recall (from Deﬁnition 15.2.27) that a graded˜A-module
˜M = ⨁
i ˜Mi is called degreewise ﬁnite overK if each homogeneous component
˜Mi is a ﬁniteK-module. We denoted by Mdwf( ˜A, gr) the full subcategory of
M( ˜A, gr) on the degreewise ﬁnite graded modules. This is a thick abelian sub-
category of M( ˜A, gr), closed under subobjects and quotients. Then we denoted
by Ddwf( ˜A, gr) the full subcategory of D( ˜A, gr) on the complexes ˜M such that
Hq( ˜M)∈Mdwf( ˜A, gr) for allq. This is a full triangulated subcategory.
Lemma 18.4.6. Let ˜M, ˜N∈Db
(f,..)( ˜Aen, gr). Then:
(1) The complexes ˜M and ˜M⊗˜N satisfy ˜M ∈Db
dwf( ˜Aen, gr) and ˜M⊗˜N ∈
Db
dwf( ˜Afour, gr).
(2) The canonical morphismθ: ˜M∗⊗˜N∗→( ˜M⊗˜N)∗in Db
dwf( ˜Afour, gr) is
an isomorphism.
430
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof.
(1) For everyq the ˜A-module Hq( ˜M) is ﬁnite, so it is the image of a ﬁnite di-
rect sum of algebraic degree shifts of ˜A. Since ˜A∈Mdwf(K, gr), and since the
subcategory Mdwf(K, gr) is closed under quotients inside M(K, gr), we see that
Hq( ˜M)∈Mdwf(K, gr). We conclude that
Hq( ˜M)∈Mdwf(K, gr)∩M( ˜Aen, gr) = Mdwf( ˜Aen, gr).
Let [q0,q 1] be a ﬁnite integer interval that containscon(H( ˜M)). For everyp∈Z
there is an isomorphism
Hp( ˜M⊗˜N)∼=
⨁
q∈[q0,q1]
(
Hq( ˜M)⊗Hp−q( ˜N)
{
in M(K, gr). Each Hq( ˜M) and Hp−q( ˜N) is a ﬁnite graded˜A-module, so it is de-
greewise ﬁnite and bounded below (in algebraic degree). Therefore
Hq( ˜M)⊗Hp−q( ˜N)∈Mdwf(K, gr),
and hence so isHp( ˜M⊗˜N). This means that ˜M⊗˜N∈Db
dwf( ˜Afour, gr).
(2) We start by giving an explicit formula for the canonical morphismθ. There is
a canonical homomorphism
(18.4.7) ˜θ: ˜M∗⊗˜N∗→( ˜M⊗˜N)∗
in Cstr(Afour, gr); it is
˜θ(φ⊗ψ)(m⊗n) := (−1)j·k·φ(m)⊗ψ(n)∈K
for φ∈( ˜M∗)i, ψ∈( ˜N∗)j, m∈˜Mk and n∈˜Nl. Then θ= Q( ˜θ) in D(Afour, gr).
We need to show that under the given ﬁniteness and boundedness conditions,θis
an isomorphism. For that we can forget theAfour-module structures, and viewθ
as a morphism inD(K, gr).
But in D(K, gr) there are canonical isomorphisms ˜M∼= H( ˜M) and ˜N∼= H( ˜N).
This means that we can assume that the diﬀerentials of the complexes˜M and ˜N are
zero. We know that for every
p
i

∈
Z
Z

=Z2, in the notation from Subsection 15.1,
theK-modules ˜Mp
i and ˜Np
i are ﬁnite. Also there are uniform bounds on vanishing:
there are integersp0,p 1,i 0 such that ˜Mp
i = ˜Np
i = 0 unless p0≤p≤p1 and i0≤i.
An easy calculation shows that for these objects˜M and ˜N, the homomorphism ˜θ
of (18.4.7) is bijective. □
Proof of Theorem18.4.5. We need to produce a graded rigidifying isomorphism˜ρ
for the graded NC dualizing complex˜R.
Consider the complex ˜R∈Db
(f,f)( ˜Aen, gr). According to Lemma 18.4.6(1) we
know that
(18.4.8) ˜R⊗˜R∈Db
dwf( ˜Afour, gr)
and
(18.4.9) ˜A∈Db
dwf( ˜Aen, gr).
There is a sequence of isomorphisms inD( ˜Aen, gr) :
(18.4.10)
RHom ˜Aen,out( ˜A, ˜R⊗˜R)∼=1 RHom ˜Aen,out
(
( ˜R⊗˜R)∗, ˜A∗{
∼=2 RHom ˜Aen,in( ˜R∗⊗˜R∗, ˜A∗)
∼=3 RHom ˜Aen,in( ˜P⊗˜P, ˜A∗)
∼=4 RHom ˜A
(˜P, RHom ˜Aop( ˜P, ˜A∗)
{
∼=5 RHom ˜A( ˜P, ˜R)∼=6 ˜R.
431
Derived Categories | Amnon Yekutieli | 14 Apr 2019
The explanations for the isomorphisms are:
∼=1 : By Theorem 15.3.32, that applies by formulas (18.4.8) and (18.4.9).
∼=2 : This is by Lemma 18.4.6(2). Note that the outside action changes to an
inside action.
∼=3 : Here ˜P := RΓ ˜m( ˜A), where ˜m is the augmentation ideal of˜A. According to
Theorems 17.3.19 and 17.2.4 there is an isomorphism˜R∼= ˜P∗in D( ˜Aen, gr);
dualizing we get an isomorphism˜R∗∼= ˜P in D( ˜Aen, gr).
∼=4 : This is one of the standard Hom-tensor identities.
∼=5 : This is another instance of the isomorphism˜P∗∼= ˜R.
∼=6 : By Lemma 17.3.31, the restriction of˜R to D( ˜A, gr) satisﬁes˜R∈Df( ˜A, gr)
⊆D( ˜A, gr)com, so ˜R is isomorphic, in D( ˜Aen, gr), to its abstract derived
completion ADC˜m( ˜R) = RHom ˜A( ˜P, ˜R). See Subsection 16.6.
The composition of the isomorphisms in (18.4.10) is the graded rigidifying iso-
morphism ˜ρ. □
The localization homomorphism˜A→˜At induces a ﬂat homomorphism of graded
rings ˜Aen →( ˜At)en = ˜At⊗˜Aop
t . This homomorphism can also be viewed as a
localization of ˜Aen with respect to the degree1 central elementst⊗1 and 1⊗t.
There is a corresponding induction functor
(18.4.11) Ind( ˜At)en : D( ˜Aen, gr)→D
(
( ˜At)en, gr
{
.
Here is what it does on objects: given a complex˜M∈D( ˜Aen, gr), we have
Ind ˜Aen( ˜M) = ( ˜At)en⊗˜Aen ˜M∼= ˜At⊗˜A ˜M⊗˜A ˜At.
There is a ring homomorphism
inc : ( ˜At)en
0 = Deg0
(
( ˜At)en{
→( ˜At)en,
the inclusion of the degree0 component. And there is a functor
(18.4.12) Deg0 : D
(
( ˜At)en, gr
{
→D
(
( ˜At)en
0
{
.
We have a ring isomorphismh :A
≃
− →( ˜At)0; see formula (18.3.18). It gives rise
to ring homomorphisms
Aen hen
−−→∼=
( ˜At)0⊗( ˜Aop
t )0
inc
−−→
⊆
( ˜At⊗˜Aop
t )0 = ( ˜At)en
0 .
Relative to this composed ring homomorphism we have the restriction functor
(18.4.13) RestAen : D
(
( ˜At)en
0
{
→D(Aen).
Composingthefunctorsfrom(18.4.11), (18.4.12)and(18.4.13)wegetatriangulated
functor
(18.4.14) RestAen◦Deg0◦Ind( ˜At)en : D( ˜Aen, gr)→D(Aen).
Theorem 18.4.15. Under Setup 18.4.1, let ˜R∈D( ˜Aen, gr) be a graded rigid NC
dualizing complex. Deﬁne the complex
R := (RestAen◦Deg0◦Ind( ˜At)en)( ˜R)[−1]∈D(Aen).
Then R is a rigid NC dualizing complex overA.
Once more we were a bit sloppy. The proper statement is this: we are given a
graded rigid NC dualizing complex( ˜R, ˜ρ); then the complexR deﬁned above admits
a rigidifying isomorphismρ, such that(R,ρ) is a rigid NC dualizing complex over
A. The proof will come after two lemmas.
Lemma 18.4.16.Assume that ˜R is a graded rigid dualizing complex over˜A. Then
for everyp the graded bimoduleHp( ˜R) is central overCent( ˜A).
432
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. We know that the central homotheties
chm ˜A, ˜A, chm ˜A, ˜Aop : Cent( ˜A)→EndM( ˜Aen,gr)( ˜A)
are equal graded ring isomorphism. Therefore the graded version of Theorem
18.2.23 – that is proved the same way – tells us that the ring homomorphisms
chmD
R, ˜A, chmD
R, ˜Aop : Cent( ˜A)→EndD( ˜Aen,gr)( ˜R)
are equal isomorphisms.
The left Cent( ˜A)-module structure onHp( ˜R) coincides with the categorical ac-
tion chmD
R, ˜A; and likewise from the right. We see that the left and rightCent( ˜A)-
module structure onHp( ˜R) are the same, so it is a central bimodule. □
Lemma 18.4.17.Assume that ˜R is a graded rigid dualizing complex over˜A. Then
the homomorphisms
(l) ˜At⊗˜A ˜R→˜At⊗˜A ˜R⊗˜A ˜At
and
(r) ˜R⊗˜A ˜At→˜At⊗˜A ˜R⊗˜A ˜At
in Cstr( ˜Aen, gr) are quasi-isomorphisms.
Proof. We shall only treat (l); the homomorphism (r) is treated similarly. Let
˜C := Cent( ˜A). Then ˜At = ˜A⊗˜C ˜Ct = ˜Ct⊗˜C ˜A. Hence (l) is true if (and only if)
the homomorphism ˜Ct⊗˜C ˜R→˜Ct⊗˜C ˜R⊗˜C ˜Ct is a quasi-isomorphism.
Because of ﬂatness of localization, for everyp there is a commutative diagram
(18.4.18) Hp(˜Ct⊗˜C ˜R
{ //
∼=

Hp(˜Ct⊗˜C ˜R⊗˜C ˜Ct
{
∼=

˜Ct⊗˜C Hp( ˜R) // ˜Ct⊗˜C Hp( ˜R)⊗˜C ˜Ct
in M( ˜Aen, gr), with vertical isomorphisms. By Lemma 18.4.16,Hp( ˜R) is a central˜C
bimodule. And localization satisﬁes˜Ct = ˜Ct⊗˜C ˜Ct. This implies that the bottom
arrow in diagram (18.4.18) is bijective. Hence the top arrow is also bijective.□
Proof of Theorem18.4.15. The proof is divided into several steps.
Step 1. This is the easiest step: we prove that for everyq the bimodule Hq(R) is a
ﬁnite module overA and overAop. In fact, we are going to treat the left module
structure of Hq(R) only; the right module structure is treated the same way, by
replacing A with Aop.
Let us write
˜Rt := Ind( ˜At)en( ˜R)∼= ˜At⊗˜A ˜R⊗˜A ˜At∈D
(
( ˜At)en, gr
{
.
According to Lemma 18.4.17 there is an isomorphism˜Rt∼= ˜At⊗˜A ˜R in D( ˜At, gr).
Since ˜R∈Df( ˜A, gr), it follows that ˜Rt∈Df( ˜At, gr). We identify ( ˜At)0 with A
using the canonical isomorphismh from (18.3.18). By Lemma 18.3.5(2) we get
Deg0( ˜Rt)∈Df
(
( ˜At)0
{
= Df(A). Hence
(18.4.19) R = Deg0( ˜Rt)[−1]∈Df(A).
We see thatHq(R) is a ﬁniteA-module for allq.
Step 2. Here we prove thatR has ﬁnite injective dimension overA and overAop.
Again, we only examine the left side; the right side is done similarly, just replacing
A with Aop.
433
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Because A is noetherian, it suﬃces to ﬁnd a uniform bound for the cohomology
of RHomA(M,R ), for allM ∈Mf(A). Take such an A-module M. By Lemma
18.3.4(3) there exists a graded module ˜M ∈Mf( ˜A, gr) such that, letting ˜Mt :=
˜At⊗˜AM, we have
(18.4.20) M∼= Deg0( ˜Mt)
in Mf(A). There are isomorphisms
(18.4.21)
RHom ˜A( ˜M, ˜R)⊗˜A ˜At∼=1 RHom ˜A( ˜M, ˜R⊗˜A ˜At)
∼=2 RHom ˜A( ˜M, ˜Rt)∼=3 RHom ˜At( ˜Mt, ˜Rt)
in D( ˜Aop
t , gr). The isomorphism∼=1 is an instance of the graded tensor-evaluation
isomorphism (Theorem 15.3.27), that is valid because ˜A is noetherian, ˜M ∈
Mf( ˜A, gr), ˜R ∈Db( ˜Aen, gr), and ˜At is ﬂat over ˜A. The isomorphism ∼=2 is by
Lemma 18.4.17. And the isomorphism ∼=3 is adjunction for the ring homomor-
phism ˜A→˜At.
Next, according to Lemma 18.3.7, and using the isomorphisms (18.4.20) and
(18.4.19), there is an isomorphism
Deg0
(
RHom ˜At( ˜Mt, ˜Rt)
{∼= RHomDeg0( ˜At)
(
Deg0( ˜Mt), Deg0( ˜Rt)
{
∼= RHomA(M,R )[1]
in D(Aop). Combining this with formula (18.4.21), we see that the injective dimen-
sion ofR overA is at most one more than the graded injective dimension of˜R over
˜A; and this is known to be ﬁnite.
Step 3. In this step we prove thatR has the derived Morita property on both sides.
As before, we only prove this property on theA side; theAop side is done similarly.
The isomorphisms (18.4.21), but for the complex of bimodules˜R instead of the
for the module ˜M, become isomorphisms
(18.4.22)
RHom ˜A( ˜R, ˜R)⊗˜A ˜At∼=1 RHom ˜A( ˜R, ˜R⊗˜A ˜At)
∼=2 RHom ˜A( ˜R, ˜Rt)∼=3 RHom ˜At( ˜At⊗˜A ˜R, ˜Rt)
∼=4 RHom ˜At( ˜Rt, ˜Rt)
in D( ˜Aop
t , gr). The last isomorphism∼=4 is another case of Lemma 18.4.17. Deﬁne
R′:= Deg0( ˜Rt)∈Df(A); soR =R′[−1]. We now applyDeg0 to the last object in
(18.4.22), obtaining the isomorphisms
(18.4.23)
Deg0
(
RHom ˜At( ˜Rt, ˜Rt)
{
∼=(i) RHomDeg0( ˜At)
(
Deg0( ˜Rt), Deg0( ˜Rt)
{
∼=(ii) RHomA(R′,R′)∼=(iii) RHomA(R,R )
in D(Aop). The isomorphism ∼=(i) is due to Lemma 18.3.7, with ˜B = ˜C := ˜At.
The isomorphism∼=(ii) is simply the deﬁnition ofR′, and the isomorphism∼=(iii) is
because R =R′[−1].
We know that˜Rhas the graded derived NC Morita property on the˜Aside. Using
Lemma 18.1.21 (that is true also in the graded situation) we see that
Hq(
RHom ˜A( ˜R, ˜R)
{
= 0 for all q⁄= 0. Because the functors Hq and Deg0 com-
mute with each other, the isomorphisms (18.4.22) and (18.4.23) tell us that
(18.4.24) Hq(
RHomA(R,R )
{
= 0
for allq⁄= 0.
434
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Forq = 0 we know that H0(
RHom ˜A( ˜R, ˜R)
{
is a graded-free ˜Aop-module with
basis id ˜R. This is by Lemma 18.1.21, applied in the graded situation. The isomor-
phisms (18.4.22) send the element id ˜R⊗1 to id ˜Rt; and therefore
H0(
RHom ˜At( ˜Rt, ˜Rt)
{
is a graded-free ˜Aop
t -module with basis id ˜Rt. The element
id ˜Rt has degree 0, and hence
H0(
Deg0
(
RHom ˜At( ˜Rt, ˜Rt)
{{∼= Deg0
(
H0(
RHom ˜At( ˜Rt, ˜Rt)
{{
is a freeAop-module with basisid ˜Rt. The isomorphisms (18.4.23) send the element
id ˜Rt to idR; so H0(
RHomA(R,R )
{
is a free Aop-module with basis idR. Again
invoking Lemma 18.1.21, this fact, with formula (18.4.24), say that R has the
derived NC Morita property on theA side.
Step 4. Here we produce a rigidifying isomorphismρfor R, starting with a given
graded rigidifying isomorphism
˜ρ: ˜R
≃
− →RHom ˜Aen,out( ˜A, ˜R⊗˜R)
in D( ˜Aen, gr). Here is a list of isomorphisms inD
(
( ˜At)en, gr
{
.
(18.4.25)
˜Rt∼=1 RHom ˜Aen,out( ˜A, ˜R⊗˜R)⊗˜Aen ( ˜At)en
∼=2 RHom ˜Aen,out
(˜A, ( ˜R⊗˜R)⊗˜Aen ( ˜At)en{
∼=3 RHom ˜Aen,out
(˜A, ( ˜R⊗˜A ˜At)⊗( ˜At⊗˜A ˜R)
{
∼=4 RHom ˜Aen,out( ˜A, ˜Rt⊗˜Rt)
∼=5 RHom( ˜At)en,out( ˜At, ˜Rt⊗˜Rt).
The justiﬁcations are:
∼=1 : Here we apply the functorInd( ˜At)en to the isomorphism˜ρ. The inside action
of ˜Aen on ˜R⊗˜R is treated as a right action.
∼=2 : This is by the graded tensor-evaluation isomorphism (Theorem 15.3.27). It
holds because ˜A is a derived graded-pseudo-ﬁnite complex over˜Aen, see
Corollary 15.3.26; ˜R⊗˜R∈Db( ˜Afour, gr); and ( ˜At)en is ﬂat over˜Aen.
∼=3 : This is a rearrangement of derived tensor factors.
∼=4 : By Lemma 18.4.17.
∼=5 : This is adjunction for the graded ring homomorphism˜Aen→( ˜At)en, with
the fact that ˜At = ˜At⊗˜A ˜A⊗˜A ˜At as graded rings.
Now we applyDeg0 to (18.4.25), and we obtain the ﬁrst isomorphism below in
D(Aen).
(18.4.26)
R′= Deg0( ˜Rt)∼=(i) Deg0
(
RHom( ˜At)en,out( ˜At, ˜Rt⊗˜Rt)
{
∼=(ii) RHomAen,out(A,R′⊗R′)[−1]
The isomorphism∼=(ii) is by Theorem 18.3.10, with˜B := ˜At, that we are allowed
to use becauseA is a derived pseudo-ﬁnite complex overAen; see Theorem 18.3.20.
Plugging inR =R′[−1] we getR∼= RHomAen,out(A,R⊗R) in D(Aen). This is the
rigidifying isomorphismρ. □
