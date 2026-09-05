---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-029-37-the-long-exact-cohomology-sequence
section_title: "The Long Exact Cohomology Sequence"
section_number: 3.7
pages: 66-74
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
M is aK-linear abelian category. Here we give a detailed proof of the existence and
functoriality of the long exact cohomology sequence, using oursheaf tricks from
Subsection 2.4. This allows us to avoid the Freyd-Mitchell Theorem.
66
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Consider a short exact sequence
(3.7.1) E =
(
0→L
φ
− →M
ψ
− →N→0
{
intheabeliancategory Cstr(M). Thismeansthat φandψaremorphismsin Cstr(M),
and in each degreei there is a short exact sequence
0→Li φi
−→Mi ψi
−→Ni→0
in M. The next deﬁnitions and lemmas refer to the short exact sequenceE. In
them we shall make use the notation from Subsection 2.4.
Let us denote byπN : Zi(N)↠ Hi(N) the canonical epimorphism in M; and
likewise forL and M.
Deﬁnition 3.7.2.Let ¯n∈Γ(U, Hi(N)) for some U ∈M, and letV ↠ U be a
covering ofU. By a connecting triplefor ¯n over V we mean a triple (n,m,l ) of
sections n∈Γ(V, Zi(N)), m∈Γ(V,M i) and l∈Γ(V, Zi+1(L)), such thatπN(n) =
¯n∈Γ(V, Hi(N)), ψ(m) =n∈Γ(V,N i) and φ(l) = d(m)∈Γ(V,M i+1).
Here is the relevant diagram inM :
Hi+1(L) Z i+1(L)
πLoooo φ //Mi+1
Mi
d
OO
ψ // Zi(N)
πN // // Hi(N)
It is possible that some coverings do not admit a connecting triple. But some
do:
Lemma 3.7.3. Let ¯n∈Γ(U, Hi(N)). There exists a covering ρ: V ↠ U that
admits a connecting triple(n,m,l ) for ¯n.
Proof. Because πN : Zi(N)→Hi(N) is an epimorphism, by the ﬁrst sheaf trick
there is a coveringV′↠U with a sectionn∈Γ(V′, Zi(N)) such thatπN(n) = ¯n.
Because ψ: Mi→Ni is an epimorphism, there is a coveringV′′↠ V′with a
section m∈Γ(V′′,M i) such thatψ(m) =n.
Consider the section d(m)∈Γ(V′′,M i+1). We have ψ(d(m)) = d( ψ(m)) =
d(n) = 0 . By exactness at Mi+1, there is a coveringV ↠ V′′with a section
l∈Γ(V,Li+1) such thatφ(l) = d(m) in Γ(V,M i+1).
Nowφ(d(l)) = d(φ(l)) = d(d(m))) = 0. Becauseφis a monomorphism, it follows
that d(l) = 0. Thusl∈Γ(V, Zi+1(L)). □
Lemma 3.7.4. Let ¯n ∈Γ(U, Hi(N)). Suppose V ↠ U is a covering that ad-
mits connecting triples (n,m,l ) and (n′,m′,l′) for ¯n. Then πL(l′) = πL(l) in
Γ(V, Hi+1(L)).
Proof. We know that πN(n) = ¯n = πN(n′) in Γ(V, Hi(N)). Thus n−n′∈
Ker(πN)⊆Γ(V, Zi(N)). Looking at the exact sequence
Ni−1 d
− →Zi(N)
πN
−−→Hi(N)→0
and invoking the ﬁrst sheaf trick, we see that there’s a coveringW ↠ V with a
section ˜n∈Γ(W,Ni−1) such that d(˜n) =n−n′.
Again invoking the ﬁrst sheaf trick, there’s a coveringW′↠ W with a section
˜m∈Γ(W′,M i−1) such thatψ( ˜m) = ˜n.
Consider the section(m−m′)−d( ˜m)∈Γ(W′,M i). It satisﬁes
ψ
(
(m−m′)−d( ˜m)
{
= (n−n′)−d(˜n) = 0.
67
Derived Categories | Amnon Yekutieli | 14 Apr 2019
By the ﬁrst sheaf trick, there’s a coveringW′′↠W′with a section˜l∈Γ(W′′,Li)
such thatφ(˜l) = (m−m′)−d( ˜m). Now
φ
(
d(˜l)−(l−l′)
{
= d(m−m′)−φ(l−l′) = 0.
Becauseφis a monomorphism, it follows thatl−l′= d(˜l). ThereforeπL(l) =πL(l′)
in Γ(W′′, Hi+1(L)). ButW′′↠V is a covering, soπL(l) =πL(l′) in Γ(V, Hi+1(L)).
□
Lemma 3.7.4 justiﬁes the next deﬁnition.
Deﬁnition 3.7.5.Let ¯n∈Γ(U, Hi(N)). SupposeV ↠U is a covering that admits
a connecting triple. We deﬁneδV (¯n)∈Γ(V, Hi+1(L)) to be the unique section such
that δV (¯n) =πL(l) for every connecting triple(n,m,l ) for ¯n overV.
Lemma 3.7.6. Let ¯n∈Γ(U, Hi(N)), and let
V′ρ′
// //
τ

U′
σ

V
ρ // //U
be a commutative diagram in M, in which the horizontal arrows are coverings.
Suppose V admits a connecting triple for¯n. Then V′admits a connecting triple
for ¯n′:= σ∗(¯n) ∈Γ(U′, Hi(N)), and there is equality δV′(¯n′) = τ∗(δV (¯n)) in
Γ(V′, Hi+1(L)).
Proof. If (n,m,l ) is a connecting triple for ¯n over V, then
(
τ∗(n),τ∗(m),τ∗(l)
{
is a connecting triple for ¯n′over V′. Thus δV′(¯n′) = πL(τ∗(l)) = τ∗(πL(l)) =
τ∗(δV (¯n)). □
Lemma 3.7.7. Let ¯n ∈Γ(U, Hi(N)). Suppose ρ: V ↠ U is a covering that
admits a connecting triple for¯n. ThenδV (¯n) lies in the subgroupΓ(U, Hi+1(L)) of
Γ(V, Hi+1(L)).
Proof. This is a “descent” argument, using the second sheaf trick. LetV1,V 2 :=V
and ρ1,ρ2 := ρ. In the notation of Proposition 2.4.11, applied to the objectQ :=
Hi+1(L)∈M, there is an exact sequence
0→Γ(U,Q )
(ρ∗
1,ρ∗
2)
−−−−→Γ(V1,Q )×Γ(V2,Q )
(σ∗
1,−σ∗
2)
−−−−−−→Γ(W,Q ).
Here
ρ1◦σ1 =ρ2◦σ2 :W =V1×U V2→U
is a covering too. According to Lemma 3.7.6, the section
(
δV1(¯n),δV2(¯n)
{
∈Γ(V1,Q )×Γ(V2,Q )
satisﬁes
(σ∗
1,−σ∗
2)
(
δV1(¯n),δV2(¯n)
{
=δW (¯n)−δW (¯n) = 0.
Hence δV (¯n) is in the image ofρ∗. □
Lemma 3.7.8. There is a unique morphismδi
E : Hi(N)→Hi+1(L) in M with the
following property:
(†) For everyU∈M, every section¯n∈Γ(U, Hi(N)), and every coveringV ↠
U that admits a connecting triple for¯n, there is equalityδi
E(¯n) =δV (¯n) in
Γ(U, Hi+1(L)).
68
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. We look at the universal section ofHi(N), namely we takeU0 := Hi(N)
and ¯n0 := idU0 ∈Γ(U0, Hi(N)). Let ρ0 : V0↠ U0 be a covering that admits a
connecting triple for¯n0; see Lemma 3.7.3. According to Lemma 3.7.7 we know that
δV0(¯n0)∈Γ(U0, Hi+1(L)) = HomM
(
Hi(N), Hi+1(L)
{
.
Deﬁneδi
E :=δV0(¯n0).
We need to prove thatδi
E has property (†). So letU∈M, let ¯n∈Γ(U, Hi(N)),
and let ρ: V ↠ U a covering that admits a connecting triple for¯n. Deﬁne the
morphism σ:= ¯n : U →U0. We get a morphism σ◦ρ: V →U0. Deﬁne
V′:=V×U0 V0. By Lemma 2.4.3(2) the induced morphismV′→V is a covering.
Therefore, by composing it withρwe get a coveringρ′:V′↠U.
Consider the commutative diagram
V′ρ′
// //
τ

U
σ

V0
ρ0 // //U0
in M. The horizontal arrows are coverings. Now¯n = σ= σ◦idU0 = σ∗(¯n0). So,
according to Lemma 3.7.6, there is equality
δV′(¯n) =τ∗(δV0(¯n0)) =τ∗(δi
E◦ρ0) =δi
E◦ρ0◦τ=δi
E◦σ◦ρ′=δi
E(¯n)
in Γ(V′, Hi+1(L)). But ρ′: V′↠ U is a covering, and hence there is equality
δV′(¯n) =δi
E(¯n) in Γ(U, Hi+1(L)). □
Deﬁnition 3.7.9.The morphism δi
E : Hi(N)→Hi+1(L) is called thei-th con-
necting morphismof the short exact sequenceE from (3.7.1).
Theorem 3.7.10 (Long Exact Sequence in Cohomology). Let M be an abelian
category. Given a short exact sequence
E =
(
0→L
φ
− →M
ψ
− →N→0
{
in Cstr(M), the sequence
···→Hi(L)
Hi(φ)
−−−→Hi(M)
Hi(ψ)
−−−−→Hi(N)
δi
E
− − →Hi+1(L)→···
in M is exact.
Proof. Weneedtocheckexactnessat Hi(N), Hi+1(L)and Hi(M). Thiswillbedone
using the ﬁrst sheaf trick (Proposition 2.4.9) and the second sheaf trick (Proposition
2.4.11).
. Step 1. Exactness atHi(N). This is done in two substeps. For simpliﬁcation we
shall write ¯ψ:= Hi(ψ).
. .Substep 1.a. We start by proving thatδi
E◦¯ψ= 0. According to Proposition
2.4.9(1) it suﬃces to show that given an element¯m∈Γ(U, Hi(N)), with image
¯n := ¯ψ( ¯m)∈Γ(U, Hi(N)), the elementδi
E(¯n) is zero.
By Proposition 2.4.9(3) there is a covering V ↠ U, and an element m ∈
Γ(V, Zi(M)), such that πM(m) = ¯m ∈Γ(V, Hi(M)). Letting n := ψ(m) ∈
Γ(V, Zi(N)), we see thatπN(n) = ¯n∈Γ(V, Hi(N)). Now dM(m) = 0, and hence,
taking l := 0, the triple (n,m,l ) is a connecting triple for ¯n over V. Therefore
δi
E(¯n) =πL(l) = 0.
. . Substep 1.b. Now we prove that the morphism ¯ψ: Hi(M) →Ker(δi
E) is
an epimorphism. We shall use Proposition 2.4.9(3). Let ¯n∈Γ(U, Ker(δi
E)); so
69
Derived Categories | Amnon Yekutieli | 14 Apr 2019
¯n∈Γ(U, Hi(N)) andδi
E(¯n) = 0. It suﬃces to ﬁnd a coveringV′↠U and a section
¯m∈Γ(V′, Hi(M)) such that ¯ψ( ¯m) = ¯n in Γ(V′, Hi(N)).
Take a coveringV ↠ U that admits a connecting triple(n,m,l ) for ¯n. Then
πL(l) =δV (¯n) =δi
E(¯n) = 0 in Γ(V, Hi+1(L)). By Proposition 2.4.9(3) there is some
coveringV′↠V and a sectionl′∈Γ(V′,Li) s.t. dL(l′) =l in Γ(V′,Li+1). Deﬁne
m′:=φ(l′)∈Γ(V′,M i). Now dM(m−m′) = dM(m)−dM(m′) =φ(l)−φ(l) = 0, so
m−m′belongs toΓ(V′, Zi(M)). Becauseψ(m−m′) =ψ(m) =n, the cohomology
class ¯m :=πM(m−m′) in Γ(V′, Hi(M)) satisﬁes¯ψ( ¯m) = ¯n in Γ(V′, Hi(N)).
. Step 2. Exactness atHi+1(L). This is also done in two substeps. We will use the
abbreviation ¯φ:= Hi+1(φ).
. .Substep 2.a. We start by proving that ¯φ◦δi
E = 0. Take ¯n∈Γ(U, Hi(N)),
and let ¯l := δi
E(¯n). We need to prove that ¯φ(¯l) = 0. Let V ↠ U be a covering
that admits a connecting triple(n,m,l ) for ¯n. This says that¯l =πL(l), and hence
¯φ(¯l) =πL(φ(l)) =πM(dM(m)) = 0.
. .Substep 2.b. Now we prove thatδi
E : Hi(N)→Ker(¯φ) is an epimorphism.
Let ¯l∈Γ(U, Hi+1(L)) be such that ¯φ(¯l) = 0. Take a coveringV ↠ U for which
there’s a sectionl∈Γ(V, Zi+1(L)) s.t.πL(l) = ¯l. The sectionφ(l)∈Γ(V, Zi+1(M))
satisﬁesπM(φ(l)) = ¯φ(¯l) = 0in Γ(V, Hi+1(M)), and therefore there is some covering
V′↠V and a sectionm∈Γ(V′,M i) s.t. dM(m) =φ(l) in Γ(V′,M i+1).
Deﬁnen := ψ(m) ∈Γ(V′,N i). Then dN(n) = d N(ψ(m)) = ψ(dM(m)) =
ψ(φ(l)) = 0, so in factn∈Γ(V′, Zi(N)). Let ¯n :=πN(n)∈Γ(V′, Hi(N)). We see
that (n,m,l ) is a connecting triple for¯n overV′. Therefore ¯l =πL(l) = δV′(¯n) =
δi
E(¯n) in Γ(V′, Hi+1(L)).
. Step 3. Exactness at Hi(M): let’s use the abbreviations¯φ:= Hi(φ) and ¯ψ:=
Hi(ψ). It is clear that ¯ψ◦¯φ= 0. It remains to prove that¯φ: Hi(L)→Ker( ¯ψ) is
an epimorphism.
Let ¯m∈Γ(U, Hi(M)) be such that ¯ψ( ¯m) = 0. We are going to ﬁnd a covering
W→U and a section¯l∈Γ(W, Hi(L)) such that ¯φ(¯l) = ¯m in Γ(W, Hi(M)).
Take a covering V ↠ U for which there’s a sectionm ∈Γ(V, Zi(M)) s.t.
πM(m) = ¯m. The section n := ψ(m)∈Γ(V, Zi(N)) satisﬁesπN(n) = ¯ψ( ¯m) =
0 in Γ(V, Hi(N)), and therefore there is some covering V′↠ V and a section
n′∈Γ(V′,N i−1) s.t. d(n′) =n in Γ(V′,N i).
Take a coveringV′′↠ V′for which there is a sectionm′′∈Γ(V′′,M i−1) s.t.
ψ(m′′) =n′. Thesection m−dM(m′′)∈Γ(V′′, Zi(M))satisﬁesπM(m−d(m′′)) = ¯m
in Γ(V′′, Hi(M), and alsoψ(m−dM(m′′)) =ψ(m)−ψ(dM(m′′)) =n−n = 0.
There is a coveringW↠V′′with a sectionl∈Γ(W,Li) s.t.φ(l) =m−dM(m′′).
Because φis a monomorphism, andm−dM(m′′) is a cocycle, it follows that the
section l belongs to Γ(W, Zi(L)). Its cohomology class ¯l := πL(l) in Γ(W, Hi(L))
satisﬁes¯φ(¯l) =πM(φ(l)) =πM(m−dM(m′′)) = ¯m in Γ(W, Hi(M)). □
Proposition 3.7.11. Let χ:E→E′be a morphism of short exact sequences in
Cstr(M). Namelyχ= (χL,χM,χN) in the commutative diagram with exact rows
0 //L
φ //
χL

M
ψ //
χM

N //
χN

0
0 //L′ φ′
//M′ψ′
//N′ // 0
70
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in Cstr(M). Then for everyi the diagram
Hi(N)
δi
E //
Hi(χN)

Hi+1(L)
Hi+1(χL)

Hi(N′)
δi
E′
// Hi+1(L′)
is commutative.
Exercise 3.7.12.Prove Proposition 3.7.11. (Hint: study the proof of the previous
theorem.)
3.8. The DG CategoryC(A, M). We now combine material from previous sub-
sections. The concept introduced in the deﬁnition below is new. It is the DG
version of Deﬁnition 3.1.45.
Conventions 1.2.4, 3.3.3, 3.4.3 and 3.5.2 are in place. Thus all linear structures
and operations areK-linear, and rings and bimodules are central overK.
Recall that given an abelian category M, the category of complexes C(M) is
a DG category. For a complex M ∈C(M) we have the DG ring EndM(M) =
HomM(M,M ). The multiplication in this ring is composition.
Deﬁnition 3.8.1.Let M be an abelian category, and letA be a DG ring. ADG
A-module in M is an objectM∈C(M), together with a DG ring homomorphism
f :A→EndM(M).
IfM is a DGA-module in M, then after forgetting the diﬀerentials,M becomes
a gradedA-module in M.
Deﬁnition 3.8.2.Let M be an abelian category, letA be a DG ring, and letM,N
be DGA-modules in M. In Deﬁnition 3.1.47 we introduced the gradedK-module
HomA,M(M,N ). This is made into a DGK-module with diﬀerential
d(φ) := dN◦φ−(−1)i·φ◦dM
for φ∈HomA,M(M,N )i.
When we have to be speciﬁc, we denote the diﬀerential ofHomA,M(M,N ) by
dHom, dA,M, or some similar expression.
As we have seen before (in Lemmas 3.6.5 and 3.4.5), given morphisms
φk∈HomA,M(Mk,Mk+1)ik
for k∈{0, 1}, we have
φ1◦φ0∈HomA,M(M0,M 2)i0+i1,
and
d(φ1◦φ0) = d(φ1)◦φ0 + (−1)i1·φ1◦d(φ0).
Also the identity automorphismidM belongs toHomA,M(M,M )0, andd(idM) = 0.
Therefore the next deﬁnition is legitimate.
Deﬁnition 3.8.3.Let M be an abelian category, and letA be a DG ring. The
DG category of DGA-modules in M is denoted by C(A, M). The morphism DG
K-modules are
HomC(A,M)(M0,M 1) := HomA,M(M0,M 1)
from Deﬁnition 3.8.2. The composition is that ofC(M).
Notice that forgetting the action ofA is a faithful DG functorC(A, M)→C(M).
Example 3.8.4. If A = K, then C(A, M) = C(M); and if M = ModK, then
C(A, M) = C(A) = DGModA.
71
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 3.8.5.In the situation of Deﬁnition 3.8.3:
(1) The strict category of C(A, M) (see Deﬁnition 3.4.6(1)) is denoted by
Cstr(A, M).
(2) The homotopy category ofC(A, M) (see Deﬁnition 3.4.6(2)) is denoted by
K(A, M).
To say this in words: a morphismφ:M→N in C(A, M) is strict if and only if
it has degree0 andφ◦dM = dN◦φ. The morphisms inK(A, M) are the homotopy
classes of strict morphisms.
An additive functorF : M→N between abelian categories is calledfaithfully
exact if for every sequenceE in Cstr(A, M), the sequenceE is exact if and only if
the sequenceF (E) in N is exact.
Proposition 3.8.6. The category Cstr(A, M) is aK-linear abelian category, and
the forgetful functors
Cstr(A, M)− →Cstr(M)
Und
−−→Gstr(M)
are faithfully exact.
Exercise 3.8.7. Prove the proposition above.
Like Deﬁnition 3.2.4, given a DG moduleM∈C(A, M) and an integeri, we can
consider the objects of degreei cocycles Zi(M), decocycles Yi(M), coboundaries
Bi(M) and cohomology Hi(M). These are all objects of M. As M varies we get
linear functors
(3.8.8) Z, Y, B, H : Cstr(A, M)→Gstr(M).
These objects are related by the following exact sequences inM :
(3.8.9) 0→Zi(M)→Mi di
M
−−→Mi+1,
(3.8.10) Mi−1 di−1
M
−−−→M→Yi(M)→0,
(3.8.11) 0→Bi(M)→Zi(M)→Hi(M)→0,
(3.8.12) 0→Hi(M)→Yi(M)→Bi+1(M)→0.
Remark 3.8.13.Actually, the cohomology functorH from equation (3.8.8) factors
through the category Gstr(H(A), M). See formula (3.1.49). We will not need this
fact.
Proposition 3.8.14. The functor Z in equation(3.8.8) is left exact, and the func-
tor Y in equation(3.8.8) is right exact.
Proof. It is enough to consider each degree separately. And by Proposition 3.8.6
we may ignore the DG ringA. Let Fi : Gstr(M)→M be the functor that sends a
graded moduleM to its degreei component Mi. This is an exact functor.
Formula (3.8.9) exhibitsZi as the kernel of the homomorphism of functorsdi :
Fi→Fi+1. According to Proposition 2.5.18(2) the functorZi is left exact.
Similarly, formula (3.8.10) exhibitsYi as the cokernel of the homomorphism of
functors di−1 : Fi−1→Fi. According to Proposition 2.5.18(2) the functorYi is
right exact. □
Proposition 3.8.15. Let{Mx}x∈X be a collection of objects ofC(A, M), indexed
by a setX. Assume that for everyi∈Z the direct sumMi :=⨁
x∈XMi
x exists in
M. Then the graded objectM :={Mi}i∈Z∈G(M) has a canonical structure of DG
A-module in M, andM is a direct sum of the collection{Mx}x∈X in Cstr(A, M).
72
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Exercise 3.8.16. Prove Proposition 3.8.15. (Hint: look at the proof of Theorem
3.9.16.)
Example3.8.17. Since M(K)hasinﬁnitedirectsums, thepropositionaboveshows
that Cstr(A) has inﬁnite direct sums.
Proposition 3.8.18. Given a DG ring A, let A♮be the graded ring gotten by
forgetting the diﬀerential. Consider the forgetful functorUnd : C(A, M)→G(A♮, M)
that forgets the diﬀerentials of DG modules, i.e.Und(M, dM) :=M.
(1) Und is a fully faithful graded functor.
(2) On the strict categories,Str(Und) : Cstr(A, M)→Gstr(A, M) is a faithfully
exact additive functor.
Exercise 3.8.19. Prove Proposition 3.8.18.
A graded object M = {Mi}i∈Z in M is said to be bounded above if the set
{i|Mi⁄= 0}is bounded above. Likewise we deﬁnebounded belowand bounded
graded objects.
Deﬁnition 3.8.20.We deﬁneC−(A, M), C+(A, M) and Cb(A, M) to be the full
subcategories ofC(A, M) consisting of bounded above, bounded below and bounded
DG modules respectively.
The symbols “−”, “+” and “b” and “⟨empty⟩” (the empty symbol) are called
boundedness indicators. We shall usually use the symbol “⋆” to denote an unspec-
iﬁed boundedness indicator. Thus the expressionC⋆(A, M) can refer to any of the
four full subcategories ofC(A, M) that are mentioned in the deﬁnition above.
Remark 3.8.21. Here is a generalization of Deﬁnition 3.8.3. Instead of a DG
centralK-ring A we can take a smallK-linear DG categoryA. We then deﬁne the
K-linear DG categoryC(A, M) := DGFun(A, C(M)) as in Exercise 3.5.8.
This is indeed a generalization of Deﬁnition 3.8.3: whenA has a single objectx,
and we writeA := EndA(x), then the functorM↦→M(x) is an isomorphism of DG
categories C(A, M)
≃
− →C(A, M).
In the special case ofM = M(K) = ModK, the DG category C(A, M) is what
Keller [79] calls the DG category ofDG A-modules.
Almost everything we do in this book forC(A, M) holds in the more general
context of C(A, M). However, in the more general context a lot of the intuition
is lost, and some aspects become pretty cumbersome. This is the reason we have
decided to stick with the less general context.
Remark 3.8.22. The theory of DG categories has a generalization – this is the
theory of A∞categories, which will be outlined in this remark. All set theoretical
issues are going to be ignored.
The concept of anA∞algebra, namely a single-objectA∞category, was intro-
duced by J. Stasheﬀ [146], [147] in the 1960’s, in relation with his work onhigher
operations on H-spacesin topology.
A∞categories are at the core ofHomological Mirror Symmetry, conceived by K.
Fukaya and M. Kontsevich during the 1990’s. Indeed, a symplectic manifoldY gives
rise to theFukaya categoryF(Y ), which is anA∞category, and is a categoriﬁcation
of Floer cohomology. See [48], [86], [87], [141] and [88].
Further developments on A∞algebras and categories were made, among oth-
ers, by T.V. Kadeishvili [73], K. Lefèvre-Hasegawa [94], B. Keller [80], [83], and
Canonaco-Ornaghi-Stellari [37]. For the analogous theory ofL∞algebras, general-
izing DG Lie algebras, see [169].
We shall only discuss strictly unitalA∞categories, giving very few details (full
details can be found in [83] and [37]), and our notation deviates somewhat from
73
Derived Categories | Amnon Yekutieli | 14 Apr 2019
the references (because we want it to be compatible with the rest of the book).
The base ringK is assumed to be a ﬁeld. AnA∞category A overK has a set
of objects Ob(A). For each pair of objects x,y ∈Ob(A) there is a graded K-
module A(x,y ) = Hom A(x,y ). For each x∈Ob(A) there is a degree 0 element
idx∈A(x,x ). For each i≥1 and each sequencex0,...,xi∈Ob(A), there is a
degree 2−i homomorphism
(3.8.23) mi : A(xi−1,xi)⊗···⊗A(x0,x 1)→A(x0,xi)
G(K). The operationsmi satisfy certain relations. Roughly speaking, the operation
m1 is a diﬀerential, the operationm2 is a multiplication, the elementidx is a unit
for the multiplicationm2, the multiplicationm2 is associative up to the hotomopy
m3, etc. The relations imply that the cohomologyH(A), w.r.t. the diﬀerentialm1,
is a graded category, in the sense of Deﬁnition 3.1.32. If the higher (i.e.i > 2)
operations mi vanish, then A is a DG category, in the sense of Deﬁnition 3.4.1.
Suppose A and B are A∞categories. An A∞functor F : A→B consists of a
function Fob : Ob(A)→Ob(B), and for eachi≥1 and each sequencex0,...,xi∈
Ob(A), a degree1−i homomorphism
(3.8.24) Fi : A(xi−1,xi)⊗···⊗A(x0,x 1)→B
(
Fob(x0),F ob(xi)
{
in G(K). There are relations that theFi have to satisfy. Given anotherA∞functor
G : B→C, there is a composedA∞functorG◦F : A→C, which is hard to describe
directly (it is usually deﬁned in terms ofcocategories, via thebar construction). We
denote by A∞Cat the category whose objects are the A∞categories and whose
morphisms are theA∞functors.
For a pairA, B∈Ob(A∞Cat) we denote byA∞Fun(A, B) the set ofA∞functors
from A to B, so that
(3.8.25) HomA∞Cat(A, B) = A∞Fun(A, B).
An important fact is thatA∞Fun(A, B) is itself the set of objects of anA∞category,
i.e. A∞Fun(A, B)∈Ob(A∞Cat). If B is a DG category (i.e. its higher operations
vanish), then A∞Fun(A, B) is also a DG category.
We shall discuss more aspects ofA∞categories in Remarks 6.2.38 and 7.2.15.
