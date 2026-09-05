---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-101-173-balanced-dc-existence
section_title: "Balanced DC: Existence"
section_number: 17.3
pages: 392-402
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
existence of balanced dualizing complexes in two important situations. We shall
adhere to Conventions 15.1.17 and 15.2.1, and to Setup 17.2.1.
The next lemma is [161, Proposition 4.4].
Lemma 17.3.1. Let R be a graded NC dualizing complex overA, with duality
functors DA,DAop : D(Aen, gr)→D(Aen, gr). The following four conditions are
equivalent.
(i) There is an isomorphismDA(K)∼=K in D(Aen, gr).
(i′) There is an isomorphismDAop(K)∼=K in D(Aen, gr).
(ii) There is an isomorphismRΓ m(R)∼=A∗⊗AL in D(Aen, gr), for some graded
invertible A-bimoduleL generated in algebraic degree0.
(ii′) There is an isomorphism RΓ mop(R)∼= L′⊗A A∗in D(Aen, gr), for some
graded invertibleA-bimoduleL′generated in algebraic degree0.
392
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Note that by Proposition 17.1.9, a graded invertibleA-bimodule L generated in
algebraic degree 0 is isomorphic toA(φ,0) for some automorphismφ.
Proof.
(i)⇒(i′): It is given thatDA(K)∼= K. By Theorem 17.1.6 we know thatK∼=
DAop(DA(K)). Together we getDAop(K)∼=K.
(i′)⇒(i): The same, by op-symmetry (replacingA with Aop).
(
(i) and (i′)
{
⇒(ii): Recall that a graded invertible bimoduleL is free of rank1
on both sides. So it suﬃces to prove separately that
(17.3.2) RΓ m(R)∼=A∗in D(A, gr)
and
(17.3.3) RΓ m(R)∼=A∗in D(Aop, gr).
Let R →I be a minimal graded-injective resolution of R over A, so that
RΓ m(R)∼= Γ m(I) in D(A, gr). By Lemma 16.5.12 the subcomplexW := Soc(I) =
HomA(K,I ) ⊆I has zero diﬀerential. But DA(K) = RHom A(K,R )
∼= HomA(K,I ) =W in D(A, gr). From condition (i) we see thatW∼=Kin D(A, gr);
and therefore alsoW∼=K in Cstr(A, gr). According to Lemma 16.3.24 and Proposi-
tion 16.3.12,Wp⊆Γ m(Ip) is an essential submodule. Again using Lemma 16.3.24
we conclude that Γ m(I)∼= A∗in Cstr(Aen, gr). Hence the isomorphism (17.3.2)
holds.
For the other isomorphism, letMf/K(A, gr)⊆M(A, gr) be the full subcategory
on the modules that are ﬁnite overK, or in other words, the ﬁnite lengthA-
modules. Conditions (i) and (i′) imply, using induction on length of modules, that
the functorH0◦DA : Mf/K(A, gr)op→Mf/K(Aop, gr) is an equivalence, with quasi-
inverse H0◦DAop. For every j ≥1 we haveA/mj ∈Mf/K(A, gr). The duality
provides an isomorphism
HomAop
(
K, H0(DA(A/mj))
{∼= HomA(A/mj,K)∼=K.
This we rewrite as
HomAop
(
K, Ext0
A(A/mj,R )
{∼=K.
By functoriality we can pass to the limit. Using Proposition 16.3.16(5) we ob-
tain an isomorphism HomAop
(
K, H0
m(R)
{∼= K. I.e. the socle of the gradedAop-
module H0
m(R) isK. By Proposition 16.3.12 there is an essential monomorphism
ψ: H0
m(R)↣A∗in M(Aop, gr). But from the previous calculation we already know
that H0
m(R)∼=A∗in M(A, gr), and hence also inM(K, gr). As these are degreewise
ﬁnite gradedK-modules, ψmust be bijective. We conclude that the isomorphism
(17.3.3) holds.
(
(i) and (i′)
{
⇒(ii′): The same, by op-symmetry.
(ii)⇒(i): By Proposition 16.3.30 there is an isomorphism
RHomA(K,R )∼= RHomA
(
K, RΓ m(R)
{
in D(Aen, gr). Now condition (ii) implies thatRΓ m(R)∼=A∗in D(A, gr). So we get
RHomA(K,R )∼= RHomA(K,A∗)∼= HomA(K,A∗)∼=K
in D(K, gr). This implies thatRHomA(K,R )∼=K in D(Aen, gr).
(ii′)⇒(i′): The same, by op-symmetry. □
Deﬁnition 17.3.4([161]). Under Setup 17.2.1, aprebalanced dualizing complex
over A is a graded NC dualizing complexR over A that satisﬁes the equivalent
conditions of Lemma 17.3.1.
393
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Here is the ﬁrst of two existence theorems for balanced dualizing complexes. The
second is Theorem 17.3.19.
Theorem 17.3.5 (Existence of BDC, [161]). Under Setup 17.2.1, assume thatA
has a prebalanced dualizing complex. ThenA has a balanced dualizing complex.
The proof comes after the next lemma. LetMf/K(Aen, gr)⊆M(Aen, gr) be the
full subcategory on the bimodules that are ﬁnite overK.
Lemma 17.3.6. Suppose R is a prebalanced dualizing complex overA such that
RΓ m(R)∼=A∗in D(Aen, gr). Then there is an isomorphismDA∼= HomK(−,K) of
functors Mf/K(Aen, gr)op→Mf/K(Aen, gr).
Proof. Let us choose an isomorphism β: RΓ m(R)
≃
− →A∗in D(Aen, gr). Take
M∈Mf/K(Aen, gr). There is a sequence of functorial isomorphisms
DA(M) = RHomA(M,R )∼=†RHomA
(
M, RΓ m(R)
{
∼=‡RHomA(M,A∗)∼= HomK(M,K)
in D(Aen, gr). The isomorphism∼=†is by Proposition 16.3.30, and the isomorphism
∼=‡comes fromβ. □
Proof of Theorem17.3.5. The proof is in two steps.
Step 1. LetR′be a prebalanced dualizing complex overA. This means that there
is an isomorphism
(17.3.7) RΓ m(R′)∼=A∗⊗AL
in D(Aen, gr), for some graded invertibleA-bimodule L generated in algebraic de-
gree 0. DeﬁneL∨:= HomA(L,A ). Thus, ifL∼=A(φ,i), thenL∨∼=A(φ−1,−i) in
M(Aen, gr).
Next let
(17.3.8) R :=R′⊗AL∨∈D(Aen, gr),
which is a graded dualizing complex. It is clear from (17.3.7) that there is an
isomorphism
(17.3.9) β: RΓ m(R)
≃
− →A∗in D(Aen, gr),
and this is the balancing isomorphism that we take. To complete the proof that
(R,β) is a balanced dualizing complex, it remains to prove that
(17.3.10) RΓ mop(R)∼=A∗in D(Aen, gr).
This will be done in the second step. (We can’t use Theorem 16.5.8 on symmetric
derived torsion, since that would involve circular reasoning.)
Step 2. The graded dualizing complexR is prebalanced, by (17.3.9). So according
to Lemma 17.3.1 there is an isomorphism
(17.3.11) RΓ mop(R)∼=L⋄⊗AA∗
in D(Aen, gr), for some invertible graded A-bimodule L⋄generated in algebraic
degree 0.
394
Derived Categories | Amnon Yekutieli | 14 Apr 2019
For everyj≥1 the bimoduleA/mj belongs toMf/K(Aen, gr), and it ism-torsion
and mop-torsion. Therefore we get isomorphisms
(17.3.12)
DAop(A/mj) = RHomAop(A/mj,R )
∼=(a) RHomAop
(
A/mj, RΓ mop(R)
{
∼=(b) RHomAop(A/mj,L⋄⊗AA∗)
∼=L⋄⊗A RHomAop(A/mj,A∗)
∼=L⋄⊗A HomK(A/mj,K) =L⋄⊗A (A/mj)∗
in D(Aen, gr). Explanation: the isomorphism∼=(a) is by Proposition 16.3.30 (tran-
scribed to the ringAop); and the isomorphism∼=(b) is from equation (17.3.11).
There are also isomorphisms
(17.3.13)
A/mj∼=1 DA
(
DAop(A/mj)
{∼=2 DA
(
L⋄⊗A (A/mj)∗{
∼=3(
L⋄⊗A (A/mj)∗{∗∼=4 (A/mj)⊗A (L⋄)∨
in M(Aen, gr), where (L⋄)∨:= HomA(L⋄,A ). Here is how they arise: the isomor-
phism∼=1 is by Theorem 17.1.6; the isomorphism∼=2 is from equation (17.3.12); and
the isomorphism∼=3 is due to Lemma 17.3.6. For the isomorphism∼=4, sayL⋄∼=
A(ν,k); then (L⋄)∨∼=A(ν−1,−k) and (L⋄)∗∼=A∗(ν−1,−k) =A∗⊗AA(ν−1,−k).
Because the isomorphisms (17.3.13) hold for everyj≥1, it follows that(L⋄)∨∼=
A in M(Aen, gr), and henceL⋄∼=A in M(Aen, gr). Then the isomorphism (17.3.11)
becomes (17.3.10). □
Recall the AS Gorenstein graded rings from Deﬁnition 15.4.8. For an AS Goren-
stein graded ringA there are isomorphisms
RHomA(K,A )∼= RHomAop(K,A )∼=K(l)[−n]
in D(K, gr). The numbers n and l are called the dimension and AS index ofA,
respectively.
Corollary 17.3.14([161]). LetA be an AS Gorenstein graded ring, of dimensionn
and with AS indexl. Then there is a unique automorphismφofA in Rnggr/cK such
that the complexRA := A(φ,−l)[n]∈D(Aen, gr) is a balanced dualizing complex
over A.
Proof. The complexR′:= A(−l)[n]∈D(Aen, gr) is a prebalanced dualizing com-
plex. Theorem 17.3.5 asserts thatA has a balanced dualizing complexRA. The
construction ofRA in formula (17.3.8) in the proof of Theorem 17.3.5 shows that
RA =R′⊗AA(φ,0)∼=A(φ,−l)[n] for some automorphismφof A.
The uniqueness ofn,l andφis a consequence of Theorems 17.2.4 and 17.1.10.□
Here are two important examples of AS regular graded rings and their balanced
dualizing complexes.
Example 17.3.15. Suppose A is anelliptic 3-dimensional Artin-Schelter regular
graded ring; see [8]. There is a normalizing regular elementg∈A3, and it deﬁnes
an automorphism φg of A by the formulaφg(a)·g = g·a for a∈A. There is a
constant λ∈K×arising from the elliptic curve associated toA, and it deﬁnes an
automorphismφλofA by the formulaφλ(a) :=λi·a fora∈Ai. According to [161,
Theorem 7.18] the balanced dualizing complex ofA is RA =A(φg◦φλ,−3)[3].
Example 17.3.16. Let A :=K[t1,...,tn], the commutative polynomial ring inn
variables, of algebraic degreesdeg(ti) = li≥1. This is an Artin-Schelter regular
graded ring, and a calculation with a Koszul complex shows thatRHomA(K,A )∼=
K(l)[−n] in D(Aen, gr), where l := ∑n
i=1li. Because RΓ m(A)∼= A∗(l)[−n] is a
395
Derived Categories | Amnon Yekutieli | 14 Apr 2019
central A-bimodule, it follows that the balanced dualizing dualizing complex ofA
is RA :=A(−l)[n].
If we want to tie this with the commutative theory from Section 13, and to
algebraic geometry, then we should takeRA := Ωn
A/K[n], whereΩn
A/K is the graded-
freeA-module generated by the diﬀerential formd(t1)∧···∧d(tn) that has algebraic
degree l.
Now an example that relies on Example 17.3.16.
Example 17.3.17. Suppose B is a commutative noetherian connected gradedK-
ring. We can ﬁnd a ﬁnite homomorphismA→B in Rnggr/cK from a commutative
polynomial ringA. Let RA := A(−l)[n] be the balanced dualizing complex ofA,
as in the previous example. DeﬁneRB := RHomA(B,RA)∈D(Ben, gr), where we
use a commutative graded-injective resolutionRA→I, so thatRB is a complex of
central gradedB-modules. By the arguments of Proposition 13.1.28,RB is graded
NC dualizing complex overB. A calculation that we won’t perform (but that is
an easy variant of the proof of Theorem 17.4.22 on the balanced trace morphism)
shows thatRB is balanced.
The moral is that the commutative algebraically graded duality theory embeds
within the noncommutative algebraically graded duality theory.
The next theorem is an important converse to Corollary 17.2.13.
Recall that for a graded NC dualizing complexR, the derived homothety mor-
phism through Aop, namely the morphism hmR
R,Aop : A →RHomA(R,R ) in
D(Aen, gr), is an isomorphism. See condition (iii) of Deﬁnition 17.1.4. By Van
den Bergh’s Local Duality (Corollary 16.4.11), for every complexM∈D(Aen, gr)
there is an isomorphism
(17.3.18) δM : RHomA
(
M, (PA)∗{≃
− →RΓ m(M)∗
in D(Aen, gr). HerePA = RΓ m(A)∈M(Aen, gr) is the dedualizing complex ofA.
Theorem 17.3.19(Existence of BDC, Van den Bergh [153]). Under Setup17.2.1,
assume the ringA satisﬁes the specialχcondition, and it has ﬁnite local cohomo-
logical dimension. ThenA has a balanced dualizing complex(RA,βA).
More explicitly, the complexRA := (PA)∗∈D(Aen, gr) is a graded dualizing
complex overA with symmetric derivedm-torsion. It has a balancing isomorphism
βA : RΓ m(RA)
≃
− →A∗, which is the unique isomorphism inD(Aen, gr) such that the
diagram
A
hmR
R,Aop
∼= //
(βA)∗

RHomA(RA,RA) δRA
∼= // RΓ m(RA)∗
in D(Aen, gr) is commutative.
Proof. The proof proceeds in 5 steps.
Step 1. We are given thatA has ﬁnite local cohomological dimension and it satisﬁes
the specialχcondition. By Proposition 16.5.19, the bimoduleA has weakly sym-
metric derivedm-torsion. Theorem 16.5.8 says that the bimoduleA has symmetric
derived m-torsion; namely that there is an isomorphism
(17.3.20) ϵA :PA = RΓ m(A)
≃
− →RΓ mop(A)
in Db(Aen, gr).
The left χcondition for A, with Proposition 16.5.17, tell us that the com-
plex RΓ m(A) has coﬁnite cohomology modules overA. By the same token, the
396
Derived Categories | Amnon Yekutieli | 14 Apr 2019
left χcondition for Aop tells us that the complex RΓ mop(A) has coﬁnite coho-
mology modules over Aop. Using the isomorphism (17.3.20) we conclude that
PA∈Db
(cof,cof)(Aen, gr). Now Graded Matlis Duality (Theorem 15.2.34) says that
the complexRA satisﬁes
(17.3.21) RA = (PA)∗∈Db
(f,f)(Aen, gr).
This is condition (i) of Deﬁnition 17.1.4.
Step 2. Because the functor RΓ m has ﬁnite cohomological dimension, Van den
Bergh’s Local Duality (Corollary 16.4.11) says that the functorRHomA
(
−,R
{
∼= RΓ m(−)∗also has ﬁnite cohomological dimension. This means that the com-
plexRA has ﬁnite graded-injective dimension overA. Similarly, becauseRΓ mop has
ﬁnite cohomological dimension, the complexRA has ﬁnite graded-injective dimen-
sion overAop. This is condition (ii) of Deﬁnition 17.1.4.
Step 3. Now we shall prove thatRA has the derived Morita property on theA side.
We have these isomorphisms in the categoryD(Aen, gr) :
(17.3.22)
RHomA(RA,RA) = RHomA
(
RΓ m(A)∗, RΓ m(A)∗{
∼=1 RHomAop
(
RΓ m(A), RΓ m(A)
{
∼=2 RHomAop
(
RΓ mop(A), RΓ mop(A)
{
∼=3 RHomAop
(
RΓ mop(A),A
{
∼=4 RHomA
(
A∗, RΓ mop(A)∗{
∼=5 RHomA
(
A∗, RΓ m(A)∗{
∼=6 (A∗)∗∼=7 A.
Theisomorphisms∼=1,∼=4 and∼=7 arefromgradedMatlisduality(Theorem15.2.34);
the isomorphisms∼=2 and∼=5 are by the symmetry isomorphismϵA; the isomor-
phism∼=3 is due to Proposition 16.3.30; and the isomorphism∼=6 is due to Van
den Bergh’s Local Duality (Corollary 16.4.11). These isomorphisms respect the
derived homothety morphisms throughAop (in lines 1, 5 and 6), the derived homo-
thety morphisms throughA (in lines 2, 3 and 4); and the canonical isomorphisms
A→(A∗)∗and A→A in line 7. (Compare to the proof of Theorem 18.1.25, and
the use of Lemma 18.1.21 in it.) The conclusion is that the derived homothety
morphism hmR
R,Aop : A→RHomA(RA,RA) is an isomorphism. This establishes
the derived Morita property on theA side forRA.
Step 4. Replacing A with Aop, using the symmetry isomorphism ϵA, the same
calculation as in step 3 shows thatRA has the derived Morita property on theAop
side. Thus condition (iii) of Deﬁnition 17.1.4 is veriﬁed. We conclude thatRA is a
graded NC dualizing complex.
Step 5. In this step we prove thatRA is balanced. By formula (17.3.21), the derived
Morita property on the A side, and Van den Bergh’s Local Duality (Corollary
16.4.11), there are isomorphisms
(17.3.23) A
hmR
RA,Aop
− −−−−−− →∼=
RHomA(RA,RA)
δRA
− −− →∼=
(
RΓ m(RA)
{∗
in D(Aen, gr). See the isomorphism (17.3.18) withM := RA = (PA)∗. After we
apply the functor(−)∗to (17.3.23), Graded Matlis Duality (Theorem 15.2.34) says
that the morphism
β:=
(
δRA◦hmR
RA,Aop
{∗
: Γ m(RA)→A∗
397
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in D(Aen, gr) is an isomorphism. This is a balancing isomorphism forRA, so item
(B2) of Deﬁnition 17.2.2 is satisﬁed.
Similarly, the Derived Morita property on theAop side, Van den Bergh’s Local
Duality forAop, and the symmetry isomorphismϵA give us these isomorphisms
A
hmR
RA,A
−−−−−→∼=
RHomAop(RA,RA)
δRA
− −− →∼=
(
RΓ mop(RA)
{∗
in D(Aen, gr). By Graded Matlis Duality, this yields an isomorphismRΓ mop(RA)
∼= A∗. We see that RA has weakly symmetric derived torsion; and hence, by
Theorem 16.5.8, RA has symmetric derived torsion. This is condition (B1) of
Deﬁnition 17.2.2. □
Corollary 17.3.24 (Two Equivalent Properties). Under Setup 17.2.1, the two
properties below are equivalent:
(i) The graded ringA satisﬁes theχcondition, and it has ﬁnite local cohomo-
logical dimension.
(ii) The graded ringA has a balanced dualizing complex.
Proof. The implication (i)⇒(ii) is the Van den Bergh Existence Theorem 17.3.19.
The reverse implication is Corollary 17.2.13. □
Here are several other consequences of Theorem 17.3.19. Recall that a dualizing
complex RA overA gives rise to the associated duality functors
(17.3.25) DA,DAop : D(Aen, gr)op→D(Aen, gr),
namely DA = RHomA(−,RA) and DAop = RHomAop(−,RA).
Theorem 17.3.26. Under Setup 17.2.1, let RA be a balanced dualizing complex
over A, with associated duality functorsDA and DAop.
(1) There is an isomorphismDA∼=DAop between the triangulated functors in
(17.3.25).
(2) If M∈Db
(f,f)(Aen, gr) then DA(M) belongs to Db
(f,f)(Aen, gr).
(3) The functor
DA : Db
(f,f)(Aen, gr)op→Db
(f,f)(Aen, gr)
is an equivalence of triangulated categories, and it is its own quasi-inverse.
Proof.
(1) By Theorems 17.3.19 and 17.2.4 there is a canonical isomorphismRA∼= (PA)∗
in D(Aen, gr).
Take a complex M ∈Db
(f,f)(Aen, gr). We know that A has the χcondition
and ﬁnite local cohomological dimension. By Proposition 16.5.19 the complexM
has symmetric derived torsion. This means that there’s an isomorphismϵM :
RΓ m(M)
≃
− →RΓ mop(M) in D(Aen, gr). By Theorem 16.4.3 and its opposite ver-
sion (namely the theorem applied to the ringAop instead ofA), this translates to
an isomorphism
(17.3.27) PA⊗L
AM∼=M⊗L
APA
in D(Aen, gr). Applying (−)∗to (17.3.27) we obtain an isomorphism
(17.3.28) (PA⊗L
AM)∗∼= (M⊗L
APA)∗
in D(Aen, gr). Now by Hom-tensor adjunction we get isomorphisms
(17.3.29)
(PA⊗L
AM)∗= HomK(PA⊗L
AM,K)
∼= RHomA
(
M, RHomK(PA,K)
{
∼= RHomA
(
M, (PA)∗{∼= RHomA(M,RA) =DA(M).
398
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Similarly there are isomorphisms
(17.3.30)
(M⊗L
APA)∗= HomK(M⊗L
APA,K)
∼= RHomAop
(
M, RHomK(PA,K)
{
∼= RHomAop
(
M, (PA)∗{∼= RHomAop(M,RA) =DAop(M).
All these isomorphisms are functorial in the argumentM. By combining the iso-
morphisms (17.3.28), (17.3.29) and (17.3.30) we get an isomorphism of functors
DA∼=DAop.
(2) By Theorem 17.1.6 we know thatDA(M) belongs to Db
(..,f)(Aen, gr). The same
theorem, applied to the ringAop, tells us thatDAop(M) belongs to Db
(f,..)(Aen, gr).
ThusDA(M)∼=DAop(M)∈Db
(f,f)(Aen, gr).
(3) We already know, by Theorem 17.1.6, thatDAop◦DA∼= Id as triangulated
functors from Db
(f,f)(Aen, gr) to itself. By item (2) the essential image of DA is
Db
(f,f)(Aen, gr). And by item (1) the functorsDA and DAop are isomorphic on this
triangulated category. □
Lemma 17.3.31. Under Setup 17.2.1, assume A satisﬁes theχcondition and
has ﬁnite local cohomological dimension. Then there are inclusionsDf(A, gr)⊆
D(A, gr)com and Dcof(A, gr)⊆D(A, gr)tor.
Proof. The inclusion Dcof(A, gr)⊆Dtor(A, gr) is trivial. And Proposition 16.3.29
says that Dtor(A, gr) = D(A, gr)tor.
Now to the complete complexes. Take a complexM ∈Df(A, gr). Then there
are isomorphisms
(17.3.32)
ADCm(M) = RHomA(PA,M )
∼=1 RHomAop
(
M∗, (PA)∗{
= RHomAop(M∗,RA)
∼=2 RHomAop
(
M∗, RΓ mop(RA)
{
∼=3 RHomAop(M∗,A∗)∼= (M∗)∗∼=4 M
in D(A, gr). The isomorphism∼=1 is due to Theorem 15.3.32, that applies because
M,PA∈Cdwf(A, gr). The isomorphism∼=2 comes from Proposition 16.3.30, and
it applies sinceM∗∈Dcof(Aop, gr)⊆Dtor(Aop, gr) and RA∈Db(Aop, gr). The
isomorphism∼=3 is becauseRA is a balanced dualizing complex. The isomorphism
∼=4 is by Proposition 15.3.30, that applies becauseM∈Cdwf(A, gr). We see that
M is in the essential image of the functorADCm. According to Theorem 16.6.32(1)
it follows thatM∈Db(A, gr)com. □
The next theorem is a reﬁnement of the NC graded MGM Equivalence (Theorem
16.6.32). Given another graded ringB, there are triangulated functors
RΓ m, ADCm : D(A⊗Bop, gr)→D(A⊗Bop, gr).
They are the derivedm-torsion and the abstract derivedm-adic completion, respec-
tively.
Theorem 17.3.33. Under Setup 17.2.1, assume A satisﬁes theχcondition and
has ﬁnite local cohomological dimension. LetB be some graded ring.
(1) If M∈Db
(f,..)(A⊗Bop, gr) then RΓ m(M)∈Db
(cof,..)(A⊗Bop, gr).
(2) For N ∈Db
(cof,..)(A⊗Bop, gr) there is an isomorphism ADCm(N) ∼=
DAop(N∗) in D(A⊗Bop, gr), and it is functorial inN.
(3) If N∈Db
(cof,..)(A⊗Bop, gr) then ADCm(N)∈Db
(f,..)(A⊗Bop, gr).
399
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(4) The functor
RΓ m : Db
(f,..)(A⊗Bop, gr)→Db
(cof,..)(A⊗Bop, gr)
is an equivalence of triangulated categories, with quasi-inverseADCm.
Proof.
(1) The ringB is irrelevant, so we may omit it. Theχcondition and ﬁniteness of
local cohomology imply thatRΓ m(M)∈Db
cof(A, gr).
(2) Take a complexN∈Db
cof(A⊗Bop, gr). We have these isomorphisms
ADCm(N) = RHomA(PA,N )∼=†RHomAop
(
N∗, (PA)∗{
= RHomAop(N∗,RA) =DAop(N∗)
in D(A⊗Bop, gr). The isomorphism∼=†is due to Theorem 15.3.32, that applies
because N∈Cdwf(A⊗Bop, gr) and PA∈Cdwf(Aen, gr).
(3) Again we can forget aboutB. TakeN∈Db
cof(A, gr). Then N∗∈Df(Aop, gr),
so by Theorem 17.1.6 we haveDAop(N∗)∈Db
f (A, gr). But by item (2) we know
that ADCm(N)∼=DAop(N∗).
(4) Items (1) and (3) tell us that the functorsRΓ m and ADCm send the categories
Db
(f,..)(A⊗Bop, gr) and Db
(cof,..)(A⊗Bop, gr) to each other, respectively. Lemma
17.3.31 says that the NC MGM Equivalence (Theorem 16.6.32) applies here, namely
that there is an isomorphism of triangulated functors ADCm◦RΓ m ∼= Id from
Db
(f,..)(A⊗Bop, gr) to itself, and an isomorphism of triangulated functorsRΓ m◦
ADCm∼= Id from Db
(cof,..)(A⊗Bop, gr) to itself. □
In Theorem 16.5.27 we saw that there is an isomorphismϵ: RΓ m
≃
− →RΓ mop
of triangulated functors Db
(f,f)(Aen)→D(Aen, gr). The next corollary produces a
similar isomorphism for the abstract derived completion functors
(17.3.34) ADCm, ADCmop : D(Aen, gr)→D(Aen, gr),
where we deﬁneADCmop := RHomAop(PA,−).
Corollary 17.3.35. Under Setup 17.2.1, assumeA satisﬁes theχcondition and
has ﬁnite local cohomological dimension. Then there is an isomorphism γ:
ADCm
≃
− →ADCmop of triangulated functorsDb
(cof,cof)(Aen, gr)→D(Aen, gr).
Proof. Take a complexN ∈Db
(cof,cof)(Aen, gr). By Theorem 17.3.33(2), there is
an isomorphism ADCm(N)∼= DAop(N∗) in Db(Aen, gr). Similarly (replacing A
with Aop) there is an isomorphismADCmop(N)∼= DA(N∗) in Db(Aen, gr). Now
N∗∈Db
(f,f)(Aen, gr), so by Theorem 17.3.26 we haveDAop(N∗)∼=DA(N∗). Since
we relied on functorial isomorphisms, this is also a functorial isomorphism. □
Corollary 17.3.36. AssumeA satisﬁes theχcondition and has ﬁnite local coho-
mological dimension. Then the functor
RΓ m : Db
(f,f)(Aen, gr)→Db
(cof,cof)(Aen, gr)
is an equivalence of triangulated categories, with quasi-inverseADCm.
Proof. TakingB :=A in Theorem 17.3.33(4) we get an equivalence
(17.3.37) RΓ m : Db
(f,..)(Aen, gr)→Db
(cof,..)(Aen, gr),
with with quasi-inverseADCm. From the same theorem, but switchingA andAop,
we get an equivalence
RΓ mop : Db
(..,f)(Aen, gr)→Db
(..,cof)(Aen, gr),
400
Derived Categories | Amnon Yekutieli | 14 Apr 2019
with with quasi-inverse ADCmop. According to Theorem 16.5.27 there is an iso-
morphism RΓ m(M)∼= RΓ mop(M) for M ∈Db
(f,f)(Aen, gr). Therefore, for such a
complex M we have RΓ m(M)∈Db
(cof,cof)(Aen, gr). Corollary 17.3.35 says that
ADCm(N)∼= ADCmop(N) for a complexN∈Db
(cof,cof)(Aen, gr); so for such a com-
plexN we haveADCm(N)∈Db
(f,f)(Aen, gr). The conclusion is that the equivalence
(17.3.37) restricts to the equivalence stated in the corollary. □
Question 17.3.38. A consequence of Theorem 16.4.3 is that the complexPA has
ﬁnite ﬂat dimension overA. Is it true that the complexPA has ﬁnite projective
dimension overA ? I.e., does the functor
ADCm = RHomA(PA,−) : D(A, gr)→D(A, gr)
have ﬁnite cohomological dimension?
In the commutative weakly proregular case this is true – see Examples 12.4.6
and 16.6.33. Indeed, ifa is a WPR ideal in a commutative ringA, then the coho-
mological dimension of the functorADCa∼= LΛ a is at most the length of a ﬁnite
generating sequence ofa.
Remark 17.3.39. The proof of Theorem 17.3.19 provided here is not the original
proof from [153]. Our proof, which relies on the NC MGM Equivalence, seems to
allow a generalization to the case of a base ringK that is not a ﬁeld (as long as the
ring A is ﬂat overK). See [157] for some results in this direction.
Remark 17.3.40. Q.S. Wu and J.J. Zhang [159], [160] studied prebalanced dual-
izing complexes over complete semilocal noncommutative rings that contain a ﬁeld.
Some of their technical results are included in Subsection 17.4 below.
An ongoing project of R. Vyas and A. Yekutieli (a continuation of [157]) aims
to study balanced dualizing complexes over complete semilocal noncommutative
rings in the arithmetic setting, namely without the presence of a base ﬁeld. A
prototypical example is the ringA = K[[G]]/I, where K = ˆZp, G is a compact
p-adic Lie group,K[[G]] is the noncommutative Iwasawa algebra, andI⊆K[[G]] is
some two-sided ideal. Because the ringA could fail to be ﬂat overK, the balanced
dualizingcomplexof Awillbeanobjectofthe derived category of bimodulesD( ˜Aen),
where ˜A→A is a K-ﬂat DG ring resolution ofA and ˜Aen := ˜A⊗K ˜Aop; see [180].
Remark 17.3.41. Suppose A is a commutative noetherian complete local ring,
with maximal ideal m. In the paper [1] the authors discuss two kinds of dualiz-
ing complexes overA : the usual dualizing complexes (see Subsection 13.1), that
they call c-dualizing complexes, which have ﬁnite (and thus complete) cohomol-
ogy modules; and thet-dualizing complexes, that have coﬁnite (and thus torsion)
cohomology modules. The torsion injective moduleI = A∗(the injective hull of
the residue ﬁeld) is a t-dualizing complex in their sense. One of the results of
[1] is that the MGM Equivalence (that they, in that early paper, calledGM Du-
ality) exchanges t-dualizing complexes and c-dualizing complexes. In particular,
by applying the derivedm-adic completion functorLΛ m one obtains a c-dualizing
complex R := LΛ m(A∗).
It was observed by Vyas that the Van den Bergh Existence Theorem (Theorem
17.3.19) can be understood as a noncommutative variant of that very same result.
In our noncommutative graded setting we must replace the true derivedm-adic
completion functor LΛ m with its abstract avatarADCm. The gradedA-bimodule
A∗is a t-dualizing complex (if we adjust the deﬁnition from [1] to the NC connected
graded setting), and indeed, as Theorem 17.3.19 says, the complex
RA := ADCm(A∗) = RHomA(PA,A∗) = (PA)∗
is a graded NC dualizing complex (as deﬁned in Deﬁnition 17.1.4).
401
Derived Categories | Amnon Yekutieli | 14 Apr 2019
