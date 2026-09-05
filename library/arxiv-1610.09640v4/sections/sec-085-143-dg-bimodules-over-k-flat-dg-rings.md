---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-085-143-dg-bimodules-over-k-flat-dg-rings
section_title: "DG Bimodules over K-Flat DG Rings"
section_number: 14.3
pages: 302-308
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
is in eﬀect. In particular all DG rings areK-central, and⊗=⊗K.
Deﬁnition 14.3.1.Let A be a DGK-ring. We call A a K-ﬂat DGK-ring if A
is K-ﬂat as a DGK-module (see Deﬁnition 10.3.1). The category of K-ﬂat central
DGK-rings is denoted byDGRng/fcK.
Example 14.3.2. IfK is aﬁeld, then every DGK-ring A is K-ﬂat overK.
Example 14.3.3. If A is asemi-freeDGK-ring (either commutative or noncom-
mutative), thenA is a K-ﬂat DGK-ring. See Deﬁnition 12.8.4, Proposition 12.8.5
and Remark 12.8.22.
Example 14.3.4.IfA is anonpositiveDGK-ring, and eachAi is aﬂatK-module,
then A is a K-ﬂat DGK-ring. This includes the case of a ﬂatK-ring A. See
Proposition 11.3.23.
Example 14.3.5. A very special case of Examples 14.3.2 and 14.3.4 is whenK is
a ﬁeld andA is aK-ring (better known as a unital associativeK-algebra). This
setting is the one commonly used in ring theory, see [8], [10], [161], [153], [145],
[183].
Deﬁnition 14.3.6.Let A and B be K-ﬂat DGK-rings. The derived category of
DG B-A-bimodules is theK-linear triangulated categoryD(B⊗Aop).
302
Derived Categories | Amnon Yekutieli | 14 Apr 2019
See Remark 14.3.24 regarding the derived category of DGB-A-bimodules in the
nonﬂat case.
Deﬁnition 14.3.7.For a K-ﬂat DGK-ring A we writeAen :=A⊗Aop, and call
it theenveloping DG ringof A (relative toK).
A explained in formula (14.2.8), the enveloping DG ring has a canonical isomor-
phism Aen ≃
− →(Aen)op.
From here to the end of this section we assume the next convention, that
strengthens Convention 14.0.1.
Convention 14.3.8.In addition to the stipulations of Convention 14.0.1, we also
assume by default that all DG rings areK-ﬂat central DGK-rings.
Recall that a homomorphism of DG ringsf :A→B induces a forgetful functor
Restf : C(B)→C(A) that we callrestriction. This is an exact DG functor, and
thus it induces a triangulated functor
(14.3.9) Restf : D(B)→D(A).
Proposition 14.3.10. Let f : A→B be a DG ring homomorphism. The trian-
gulated functor Restf is conservative. Namely a morphismφ:M→N in D(B) is
an isomorphism if and only if the morphism
Restf(φ) : Restf(M)→Restf(N)
in D(A) is an isomorphism.
Proof. We know by Corollary 7.2.13 that the functorH : D(B)→G(K) is conser-
vative. But H = H◦Restf. □
Lemma 14.3.11. LetA and B be DG rings.
(1) If P∈C(A⊗Bop) is K-ﬂat, thenP is K-ﬂat overA.
(2) If I∈C(A⊗Bop) is K-injective, thenI is K-injective overA.
(3) If B is K-projective as a DGK-module, and ifP ∈C(A⊗K Bop) is K-
projective, thenP is K-projective overA.
(4) If B is a semi-free DGK-ring, and ifP∈C(A⊗KBop) is semi-free, then
P is semi-free overA.
Proof. (1) and (2) are direct consequences of the canonical isomorphisms
M⊗AP∼= (M⊗B)⊗A⊗BP
and
HomA(N,I )∼= HomA⊗B(N⊗B,I )
in Cstr(K), forM∈C(Aop) and N∈C(A), together with the fact thatB is K-ﬂat
overK. Items (3) and (4) are left as an exercise. □
Exercise 14.3.12. Prove items (3) and (4) in this lemma.
Proposition 14.3.13. LetA, B and C be DG rings.
(1) The DG bifunctor
(−⊗B−) : C(A⊗Bop)×C(B⊗Cop)→C(A⊗Cop)
has a triangulated left derived bifunctor
(
(−⊗L
B−),ηL{
: D(A⊗Bop)×D(B⊗Cop)→D(A⊗Cop).
(2) Given M∈C(A⊗Bop) and N∈C(B⊗Cop), such thatM is K-ﬂat over
Bop or N is K-ﬂat overB, the morphism
ηL
M,N :M⊗L
BN→M⊗BN
in D(A⊗Cop) is an isomorphism.
303
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(3) Suppose we are given DG ring homomorphismsA′→A, f : B′→B and
C′→C, such thatf is a quasi-isomorphism. Then the diagram
D(A⊗Bop)×D(B⊗Cop)
(−⊗L
B−) //
Rest×Rest

D(A⊗Cop)
Rest

D(A′⊗B′op)×D(B′⊗C′op)
(−⊗L
B′−)
// D(A′⊗C′op)
is commutative up to an isomorphism of triangulated bifunctors.
(4) SupposeD is another DG ring. Then there is an isomorphism
((−⊗L
B−)⊗L
C−)∼= (−⊗L
B (−⊗L
C−))
of triangulated trifunctors
D(A⊗Bop)×D(B⊗Cop)×D(C⊗Dop)→D(A⊗Dop).
Proof.
(1) The DG bifunctor(−⊗B−) induces a triangulated bifunctor
(−⊗B−) : K(A⊗Bop)×K(B⊗Cop)→K(A⊗Cop)
on the homotopy categories, in the obvious way. By Corollary 11.4.26, Proposition
10.3.4 and Lemma 14.3.11(1), every DG bimodule N ∈C(B⊗Cop) admits a
quasi-isomorphism ρN : P→N, whereP∈C(B⊗Cop) is K-ﬂat overB. Given
M∈D(A⊗Bop), let us deﬁne the object
M⊗L
BN :=M⊗BP∈D(A⊗Cop),
with the morphism
ηL
M,N := idM⊗BρN :M⊗L
BN→M⊗BN.
The pair
(
(−⊗L
B−),ηL{
is a left derived bifunctor of(−⊗B−).
(2)Undereitherassumptionthehomomorphism idM⊗BρN isaquasi-isomorphism;
cf. Lemma 12.3.2.
(3) This is similar to the proof of item (2) of Theorem 12.7.2. TakeM∈C(A⊗Bop)
and N∈C(B⊗Cop). Let ρN : P→N be the resolution from item (1). Choose
a resolutionρ′
P :P′→P in Cstr(B′⊗C′op) where P′is K-ﬂat overB′. Then we
have a canonical isomorphism
Rest(M)⊗L
B′Rest(N)∼=M⊗B′P′
in D(A′⊗C′op). Now in the commutative diagram
B′⊗B′P′ ∼= //
f⊗idP′

P′
ρ′
P

B⊗B′P′idB⊗ρ′
P //P
in Cstr(B′) the vertical arrows are quasi-isomorphisms, becauseP′is K-ﬂat over
B′. Therefore the bottom arrowidB⊗ρ′
P is a quasi-isomorphism.
We now look at this commutative diagram
M⊗B′P′
idM⊗ρ′
P
((∼= //M⊗BB⊗B′P′φ //M⊗BP
in Cstr(A′⊗C′op), whereφ:= idM⊗idB⊗ρ′
P. Because bothP and B⊗B′P′are
K-ﬂat overB, andidB⊗ρ′
P is a quasi-isomorphism, Lemma 12.3.2 tells us thatφis
304
Derived Categories | Amnon Yekutieli | 14 Apr 2019
a quasi-isomorphism. Hence idM⊗ρ′
P is a quasi-isomorphism. We get the desired
canonical isomorphism
Q(idM⊗ρ′
P ) : Rest(M)⊗L
B′Rest(N)
≃
− →Rest(M⊗L
BN)
in D(A′⊗C′op).
(4) GivenM,N,P as above andL∈C(C⊗Dop), we choose a quasi-isomorphism
ρL : Q→L, whereQ∈C(C⊗Dop) is K-ﬂat overC. A small calculation shows
that P⊗CQ is K-ﬂat overB. The desired isomorphism
(M⊗L
BN)⊗L
CL∼=M⊗L
B (N⊗L
CL)
in D(A⊗Dop) comes from the obvious isomorphism
(M⊗BP )⊗CQ∼=M⊗B (P⊗CQ)
in Cstr(A⊗Dop). □
Here is some notation: suppose we are given morphismsφ:M′→M in D(A⊗
Bop) andψ:N′→N in D(B⊗Cop). The result of applying the bifunctor(−⊗L
B−)
is the morphism
(14.3.14) φ⊗L
Bψ:M′⊗L
BN′→M⊗L
BN
in D(A⊗Cop).
Proposition 14.3.15. LetA, B and C be DG rings.
(1) The DG bifunctor
HomB(−,−) : C(B⊗Aop)op×C(B⊗Cop)→C(A⊗Cop)
has a triangulated right derived bifunctor
(
RHomB(−,−),ηR{
: D(B⊗Aop)op×D(B⊗Cop)→D(A⊗Cop).
(2) Given M ∈C(B⊗Aop) and N ∈C(B⊗Cop), such that either M is
K-projective overB or N is K-injective overB, the morphism
ηR
M,N : HomB(M,N )→RHomB(M,N )
in D(A⊗Cop) is an isomorphism.
(3) Suppose we are given DG ring homomorphismsA′→A, f : B′→B and
C′→C, such thatf is a quasi-isomorphism. Then the diagram
D(B⊗Aop)op×D(B⊗Cop)
RHomB(−,−) //
Rest×Rest

D(A⊗Cop)
Rest

D(B′⊗A′op)op×D(B′⊗C′op)
RHomB′(−,−) // D(A′⊗C′op)
is commutative up to an isomorphism of triangulated bifunctors.
Exercise 14.3.16. Prove Proposition 14.3.15. Hints: this is similar to the proof
of items (1)-(3) of Proposition 14.3.13, but now we rely on Corollary 11.6.30 and
Lemma 14.3.11(2) for the existence of resolutionsρN :N→I in Cstr(B⊗Cop) by
DG bimodulesI that are K-injective overB. For item (3) use Lemma 12.2.2.
Again there is related notation: suppose we are given morphismsφ:M→M′in
D(B⊗Aop) and ψ:N′→N in D(B⊗Cop). The result of applying the bifunctor
RHomB(−,−) is the morphism
(14.3.17) RHomB(φ,ψ) : RHomB(M′,N′)→RHomB(M,N )
in D(A⊗Cop).
305
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proposition 14.3.18. Let A, B, C and D be DG rings. ForM∈D(B⊗Aop),
N∈D(C⊗Bop) and L∈D(C⊗Dop) there is an isomorphism
RHomB
(
M, RHomC(N,L )
{∼= RHomC(N⊗L
BM,L )
in D(A⊗Dop) called derived Hom-tensor adjunction. This isomorphism is functo-
rial in the objectsM,N,L .
Proof. We choose a quasi-isomorphismL→J in Cstr(C⊗Dop) into a DG module
J that is K-injective overC, and a quasi-isomorphismQ→N in Cstr(C⊗Bop)
from a DG moduleQ that is K-ﬂat overBop. A calculation shows that the DG
bimodule HomC(Q,J ) is K-injective overB. The desired isomorphism comes from
the obvious adjunction isomorphism
HomB(M, HomC(Q,J ))∼= HomC(Q⊗BM,J )
in Cstr(A⊗Dop). □
Proposition 14.3.19. Let A, B, C and D be DG rings. ForL∈D(A⊗Cop),
M∈D(A⊗Bop) and N∈D(B⊗Dop) there is a morphism
evR,L
L,M,N : RHomA(L,M )⊗L
BN→RHomA(L,M⊗L
BN)
in D(C⊗Dop), calledderived tensor-evaluation. This morphism is functorial in the
objects L,M,N . Moreover, after applying the restriction functorD(C⊗Dop)→
D(K), the morphismevR,L
L,M,N coincides with the morphism from Theorem12.9.10.
Thereasonwecangivestrongerstatementhere, ascomparedtoTheorem12.9.10,
is because here our DG rings are K-ﬂat overK.
Proof. Choose a quasi-isomorphismQ→N in Cstr(B⊗Dop) from a DG module
Q that is K-ﬂat overB, a quasi-isomorphismM→I in Cstr(A⊗Bop) into a DG
module I that is K-injective overA, and a quasi-isomorphismρ: I⊗B Q→J in
Cstr(A⊗Dop) into a DG moduleJ that is K-injective overA. Then evR,L
L,M,N is
represented by the composed homomorphism
HomA(L,I )⊗BQ
evL,I,Q
−−−−−→HomA(L,I⊗BQ)
˜ρ
− →HomA(L,J )
in Cstr(C⊗Dop), where ˜ρ:= Hom(idL,ρ).
When we forgetC and D, then we can choose a K-projective resolutionP→L
in Cstr(A). Then we have a commutative diagram
HomA(P,I )⊗BQ
evP,I,Q // HomA(P,I⊗BQ)
q.i. // HomA(P,J )
HomA(L,I )⊗BQ
evL,I,Q //
q.i.
OO
HomA(L,I⊗BQ)
˜ρ //
OO
HomA(L,J )
q.i.
OO
in Cstr(K), in which the arrows marked “q.i.” are quasi-isomorphisms. By compar-
ing to the proof of Theorem 12.9.10 this proves that last assertion. □
According to Propositions 14.3.13 and 14.3.15 there are triangulated bifunctors
(14.3.20) (−⊗L
A−) : D(Aen)×D(Aen)→D(Aen),
(14.3.21) (−⊗L
A−) : D(Aen)×D(A⊗Bop)→D(A⊗Bop)
and
(14.3.22) RHomA(−,−) : D(Aen)op×D(A⊗Bop)→D(A⊗Bop).
306
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Remark 14.3.23. The category D(Aen), with the tensor operation(−⊗L
A−), is
a monoidal category. Moreover, D(Aen) is a biclosed monoidal category: the two
internal Hom operations are RHomA(−,−) and RHomAop(−,−). If A is weakly
commutative, thenD(Aen) is a symmetric monoidal category. See [157, Section 5],
[102] and [115].
Remark 14.3.24. Here is an outline of our way to handle derived categories of
DG bimodules in the absence of ﬂatness. The idea is to choose K-ﬂat resolutions
˜A→A and ˜B→B in the categoryDGRng/cK of DG centralK-rings. This can be
done by Theorem 12.8.7 and Proposition 12.8.5. Then thederived category of DG
A-B-bimodules is the triangulated categoryD( ˜A⊗˜Bop). Note that the restriction
functors D( ˜A)→D(A) and D( ˜Bop)→D(Bop) are equivalences. This says that we
have triangulated bifunctors
(−⊗L
˜B−) : D( ˜A⊗˜Bop)×D(B)→D(A)
and
RHom ˜A(−,−) : D( ˜A⊗˜Bop)op×D(A)→D(B).
We also have the “tilde” versions of the functors (14.3.20), (14.3.21) and (14.3.22).
These are collectively called thepackage of standard derived functors.
The triangulated category D( ˜A⊗˜Bop) is independent of the resolutions, up
to a canonical equivalence. The argument is this. Suppose we are given K-ﬂat
resolutions ˜Ai→A and ˜Bi→B in the categoryDGRng/cK, indexed byi∈I for
some setI. For eachi,j ∈I, the the DG moduleA⊗L
KB has an outside action by
the DG ring ˜Aj⊗˜Bop
j and an inside action the DG ring˜Ai⊗˜Bop
i . (See Subsection
18.2 regarding outside and inside actions.) These give rise to a DG bimodule
Ti,j :=A⊗L
KB∈D
(
( ˜Aj⊗˜Bop
j )⊗( ˜Ai⊗˜Bop
i )op{
.
It turns out thatTi,j is a tilting DG bimodule, as deﬁned in the next subsection;
and hence the triangulated functor
(14.3.25) Gi,j :=Ti,j⊗L
˜Ai⊗˜Bop
i
(−) : D( ˜Ai⊗˜Bop
i )→D( ˜Aj⊗˜Bop
j )
is an equivalence. For a third indexk∈I there is a canonical isomorphism
Tj,k⊗L
˜Aj⊗˜Bop
j
Ti,j∼=Ti,k in D
(
( ˜Ak⊗˜Bop
k )⊗( ˜Ai⊗˜Bop
i )op{
.
Thus there are isomorphisms of triangulated functors
(14.3.26) Gj,k◦Gi,j
≃
− →Gi,k,
and they satisfy the pentagon axiom. The equivalencesGi,j respect the packages
of standard derived functors.
We see that there is aK-linear triangulated category that we will symbolically
denote by D(A⊗L
K Bop), and it is canonically equivalent to all the triangulated
categories D( ˜Ai⊗˜Bop
i ). For more details see the lecture notes [180] or the paper
[178].
Remark 14.3.27. Actually, we can say more. Recall the2-category TrCat/K of
K-linear triangulated categories that was brieﬂy mentioned at the end of Subsection
8.1. There is a pseudofunctor
(14.3.28) DerCat : DGRng/cK→TrCat/K
that sends a DG ringA to the triangulated categoryDerCat(A) := D(A), and a
homomorphism f :A→B in DGRng/cK is sent to the triangulated functor
DerCat(f) := LIndf =B⊗L
A (−) : D(A)→D(B).
307
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Note that the categoryDGRng/cK is not linear (the morphisms sets have no linear
structure), whereas the2-category TrCat/K is linear (in the sense that the sets of
2-morphisms areK-modules).
DeﬁneD(DGRng/cK)tobethecategoricallocalizationofthecategory DGRng/cK
with respect to the quasi-isomorphisms in it. Then the pseudofunctorDerCat from
(14.3.28) localizes, in the categorical sense, to a pseudofunctor
DerCat : D(DGRng/cK)→TrCat/K.
The (nonlinear) bifunctor
(−⊗K−) : (DGRng/cK)×(DGRng/cK)→DGRng/cK
has a left derived bifunctor
(−⊗L
K−) : D(DGRng/cK)×D(DGRng/cK)→D(DGRng/cK).
Given a pair of DG ringsA and B, we thus have DG ringA⊗L
KBop, well-deﬁned
up to a unique isomorphism in D(DGRng/cK). The derived category of DG A-
B-bimodules described at the end of Remark 14.3.24 is canonically equivalent to
DerCat(A⊗L
KBop) in TrCat/K.
