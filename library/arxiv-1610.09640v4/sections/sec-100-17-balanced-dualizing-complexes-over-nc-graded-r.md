---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-100-17-balanced-dualizing-complexes-over-nc-graded-r
section_title: "Balanced Dualizing Complexes over NC Graded Rings"
section_number: 17
pages: 385-392
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
Let A = ⨁
i≥0Ai be a noncommutative noetherian connected gradedK-ring,
with augmentation ideal m =⨁
i≥1Ai. A balanced dualizing complexover A is a
dualizing complexR overA, in the noncommutative graded sense, that satisﬁes the
Noncommutative Graded Local Duality Theorem(Theorem 17.2.7 below). Balanced
dualizing complexes were introduced in 1992 by A. Yekutieli [161].
In this section we deﬁne balanced dualizing complexes, and then we prove their
uniqueness and existence, the local duality theorem, and the trace functoriality.
One of the main results of this section is Corollary 17.3.24, which says that the
following two properties are equivalent:
(i) The ringA satisﬁes theχcondition, and it has ﬁnite local cohomological
dimension.
(ii) The ringA has a balanced dualizing complex.
This result is the product of the combined eﬀorts of Yekutieli, J.J. Zhang and M.
Van den Bergh. Theχcondition was already discussed in Subsection 16.5. M. Artin
and Zhang had introduced theχcondition and the ﬁniteness of local cohomological
dimension in their 1994 paper [10], to ensure that thenoncommutative projective
scheme Proj(A) has “good geometric properties”. On the other hand, as mentioned
above, balanced dualizing complexes were designed to satisfy the Noncommutative
Local Duality Theorem. It is remarkable that in the end, these two properties
turned out to be equivalent.
Throughout this section we adhere to Conventions 15.1.17 and 15.2.1. Thus
K is a base ﬁeld, and all graded rings are algebraically graded centralK-rings,
as deﬁned in Section 15. See Remark 17.3.40 regarding the complete case (A is
adically complete instead of graded) and the arithmetic case (the base ringK is
not a ﬁeld).
17.1. GradedNCDualizingComplexes. Inthissubsectionweintroduce graded
noncommutative dualizing complexes. This is a generalization of Grothendieck’s
original commutative deﬁnition from [62] (see Section 13).
Consider a gradedK-ring A. Complexes of gradedA-modules were studied in
Subsections 15.1 and 15.3, and here we use these constructions and results. Let us
recall that M(A, gr) is the abelian category of gradedA-modules, and D(A, gr) is
its derived category.
Suppose B is a second graded ring. Given complexesM∈D(A⊗Bop, gr) and
N∈D(Aen, gr), there is thenoncommutative derived Hom-evaluation morphism
(17.1.1) evR,R
M,N :M→RHomAop
(
RHomA(M,N ),N
{
in D(A⊗Bop, gr). For a choice of a K-injective resolutionN→I in Cstr(Aen, gr),
the morphism evR,R
M,N is represented by the homomorphism
evM,I :M→HomAop
(
HomA(M,I ),I
{
in Cstr(A⊗Bop, gr), whose formula isevM,I(m)(φ) := (−1)p·q·φ(m) for m∈Mp
and φ∈HomA(M,I )q.
In the special case B = A and M = A∈D(Aen, gr) we have the canonical
isomorphisms N ∼= RHomA(A,N )∼= RHomAop(A,N ), i.e. the left and right co-
unitor isomorphisms of the biclosed monoidal structure. Then the derived NC Hom-
evaluation morphismevR,R
M,N from (17.1.1) specializes to theNC derived homothety
ThismaterialwillbepublishedbyCambridgeUniversityPressas Derived CategoriesbyAmnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works.c© Amnon Yekutieli, 2019.
385
Derived Categories | Amnon Yekutieli | 14 Apr 2019
morphism throughA :
(17.1.2) hmR
N,A = evR,R
A,N :A→RHomAop(N,N )
in D(Aen, gr). Similarly, after exchangingA and Aop, we recover theNC derived
homothety morphism throughAop :
(17.1.3) hmR
N,Aop = evR,R
A,N :A→RHomA(N,N ),
also in D(Aen, gr). This should be compared to Deﬁnition 14.4.13, which refers to
the ungraded NC setting.
Deﬁnition 17.1.4([161]). Let A be a noetherian graded ring. A graded NC
dualizing complex over A is a complexR∈Db(Aen, gr) with the following three
properties:
(i) Finiteness of cohomology: for every integerp the A-bimodule Hp(R) is a
ﬁnite graded module overA and overAop.
(ii) Finite injective dimension: the complex R has ﬁnite graded-injective di-
mension overA and overAop.
(iii) NC Derived Morita property: the noncommutative derived homothety mor-
phisms
hmR
R,A :A→RHomAop(R,R )
and
hmR
R,Aop :A→RHomA(R,R )
in D(Aen, gr) are both isomorphisms.
Condition(i)canberestatedas R∈D(f,f)(Aen, gr). Itcanbeshown(usingCorol-
lary 15.3.7(3) and smart truncation, as in the proof of Proposition 12.4.13) that
condition (ii) is equivalent to the existence of an isomorphismR∼=I in D(Aen, gr),
where I is a bounded complex, and every bimoduleIp is graded-injective overA
and overAop.
Deﬁnition 17.1.5.In the situation of Deﬁnition 17.1.4, given another graded ring
B, theduality functorsassociated to the dualizing complexR are the triangulated
functors
DA : D(A⊗Bop, gr)op→D(B⊗Aop, gr), D A := RHomA(−,R )
and
DAop : D(B⊗Aop, gr)op→D(A⊗Bop, gr), D Aop := RHomAop(−,R ).
Since the dualizing complexR is usually clear from the context, we can omit
it from the notation of the duality functorsDA and DAop. We can also omitR
from the notation of the related derived Hom-evaluation morphisms, and just write
evR,R
M : M →DAop(DA(M)) and evR,R
M′: M′→DA(DAop(M′)) for complexes
M∈D(A⊗Bop, gr) and M′∈D(B⊗Aop, gr).
Theorem 17.1.6. Let A and B be graded rings, withA noetherian. Let R ∈
D(Aen, gr) be a graded NC dualizing complex overA, with associated duality func-
tors DA and DAop. Let ⋆be a boundedness indicator, and let M ∈
D⋆
(f,..)(A⊗Bop, gr). Then the following hold:
(1) The complexDA(M) belongs toD−⋆
(..,f)(B⊗Aop, gr), where−⋆is the reversed
boundedness indicator.
(2) The derived Hom-evaluation morphism evR,R
M : M →DAop(DA(M)) in
D(A⊗Bop, gr) is an isomorphism.
386
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(3) The functor
DA : D⋆
(f,..)(A⊗Bop, gr)op→D−⋆
(..,f)(B⊗Aop, gr)
is an equivalence of triangulated categories, with quasi-inverseDAop.
Proof.
(1) We can forget the ringB. Since the functor DA : D(A, gr)op→D(Aop, gr)
has ﬁnite cohomological dimension, and sinceDA(A) = R∈Mf(Aop, gr), this is
a consequence of Theorem 12.5.7(2), slightly modiﬁed to handle the algebraically
graded situation.
(2) Because the restriction functorD(A⊗Bop, gr)→D(A, gr) is conservative, we
can forget about the ringB. The derived Morita property says thatevR,R
M :M→
DAop(DA(M)) is an isomorphism forM =A. The functorsId andDAop◦DA have
ﬁnite cohomological dimensions. The assertion is then a consequence of Theorem
12.5.2(2), slightly modiﬁed to handle the algebraically graded situation.
(3) This is clear from items (2) and (3). □
We shall require a notion of twisting in the NC graded setting.
Deﬁnition 17.1.7.Let φbe an automorphism ofA in the category Rnggr/cK,
and leti be an integer. The (φ,i)-twist of the bimoduleA is the objectA(φ,i)∈
M(Aen, gr) deﬁned as follows: as a left gradedA-module it is the graded-freeA-
module A(i) with basis elemente in degree−i. The rightA-module action is given
by the formulae·φa :=φ(a)·e for a∈A.
Tobemoreexplicit, anelement m∈A(φ,i)canbeexpresseduniquelyas m =b·e
with b∈A. Thenm·φa = (b·e)·φa = (b·φ(a))·e∈A(φ,i).
Deﬁnition 17.1.8. An invertible graded A-bimodule is a bimodule L ∈
M(Aen, gr) such that there exists someL∨∈M(Aen, gr) satisfying L⊗A L∨∼=
L∨⊗AL∼=A in M(Aen, gr). The bimoduleL∨is called a quasi-inverse ofL.
Proposition 17.1.9. AssumeA is connected graded. LetL be an invertible graded
A-bimodule. ThenL∼=A(φ,i), for a unique automorphismφand a unique integer
i.
Proof. Take a quasi-inverseL∨of L. Since the tensor product commutes with the
ungrading functor, we see thatL⊗AL∨∼=L∨⊗AL∼=A in M(Ungr(A)en). Classical
Morita theory (see e.g. [130, Chapter 4]) says thatL and L∨are ﬁnite projective
Ungr(A)-modules on both sides. Hence they are ﬂat overA and Aop.
Consider the obvious surjection
K∼=K⊗AL∨⊗AL↠ (K⊗AL∨⊗AK)⊗(K⊗AL)
in M(Aen, gr). Since L is a nonzero ﬁnite gradedA-module and Aop-module, by
the graded Nakayama Lemma (Proposition 15.2.30) theK-modulesK⊗AL∨⊗AK
andK⊗AL are nonzero. ThereforeK⊗AL is a graded-freeK-module of rank1,
soK⊗AL∼=K(i) in M(K, gr) for some integeri. But L is a ﬂatA-module, and
therefore, as in the classical commutative proof, we get an isomorphismL∼= A(i)
in M(A, gr).
By symmetry we also have an isomorphismL∼=A(i) in M(Aop, gr). Thus there
is an elemente∈L−i which is a basis ofL on both sides. Fora∈A let φ(a)∈A
be the unique element such thate·a =φ(a)·e. Then φis aK-ring automorphism
of A, andL∼=A(φ,i) in M(Aen, gr).
Because the only invertible elements ofA are the nonzero elements ofA0∼=K,
and these are central elements,A does not have nontrivial inner automorphisms.
Thus the automorphismφis unique. □
387
Derived Categories | Amnon Yekutieli | 14 Apr 2019
The next theorem is a variant of Theorem 13.1.35.
Theorem 17.1.10(Uniqueness of NC Graded DC, [161]). LetA be a noetherian
connected graded ring, and letR and R′be graded NC dualizing complexes overA.
Then there is an isomorphism
R′∼=R⊗AA(φ,i)[j]
in D(Aen, gr), for a unique automorphismφand unique integersi,j.
For the proof we shall need a few lemmas. Recall that a moduleN∈M(A, gr)
is called bounded below ifNi = 0 for i≪0.
Lemma 17.1.11. LetT,T′∈D−(Aen, gr) satisfy these conditions:
•For everyk the graded bimodulesHk(T ) and Hk(T′) are bounded below.
•There are isomorphismsT⊗L
AT′∼=T′⊗L
AT∼=A in D(Aen, gr).
Then T∼=A(φ,i)[j], for a unique automorphismφand unique integersi,j.
Proof. This is similar to the proof of Lemma 13.1.42. Deﬁnej1 := sup(H(T ))
and j′
1 := sup(H(T′)). By smart truncation we can assume thatj1 = sup(T ) and
j′
1 := sup(T′). The Künneth trick (see Lemma 13.1.36; it works also in the graded
setting) we have
Hj1(T )⊗A Hj′
1(T′)∼= Hj1+j′
1(T⊗L
AT′)∼= Hj1+j′
1(A)
in M(Aen, gr). The graded Nakayama Lemma (Proposition 15.2.30) implies that
Hj1(T )⊗AHj′
1(T′)⁄= 0. Hence we must havej1+j′
1 = 0and Hj1(T )⊗AHj′
1(T′)∼=A.
By symmetry, we also haveHj′
1(T′)⊗A Hj1(T )∼= A. According to Proposition
17.1.9 we know thatHj1(T )∼= L, whereL := A(φ,i) for someφand i. Therefore
Hj′
1(T′)∼=L′, whereL′:=A(φ−1,−i).
Wenowforgettheleft A-modulestructureof T, andtheright A-modulestructure
of T′. By the projective truncation trick (Lemma 13.1.38) we get an isomorphism
T ∼= L[−j1]⊕N in D(Aop, gr), where sup(N)≤j1−1. Similarly there is a an
isomorphismT′∼=L′[−j′
1]⊕N′in D(A, gr), wheresup(N′)≤j′
1−1. Then there is
an isomorphism
(17.1.12)
A∼= H(T⊗L
AT′)∼= (L⊗AL′)
⊕
(
L[−j1]⊗A H(N′)
{
⊕
(
H(N)⊗AL′[−j′
1]
{
⊕H(N⊗L
AN′)
in Gstr(K, gr). ButA is concentrated in cohomological degree0, and this forces the
three summands in the second line of (17.1.12) to be zero. SinceL′is graded-free
of rank 1 over A, it follows thatH(N) = 0. Therefore Hk(T ) = 0 for allk⁄= j1.
Letting j :=−j1 we getT∼= H−j(T )[j]∼=L[j] =A(φ,i)[j] in D(Aen, gr). □
Lemma 17.1.13. Let R,R′∈D(Aen, gr) be graded NC dualizing complexes, and
let M∈D(Aen, gr). Then there a morphism
ψM :M⊗L
A RHomA(R,R′)
≃
− →RHomA
(
RHomAop(M,R ),R′{
in D(Aen, gr), that is functorial in M. If M ∈D−
(..,f)(Aen, gr) then ψM is an
isomorphism.
Proof. This is the NC graded version of the isomorphism that was used in the proof
of Theorem 13.1.35. To deﬁneψM we choose a K-projective resolutionP →M,
and K-injective resolutionsR→I and R′→I′, all in Cstr(Aen, gr). Then ψM is
represented by the obvious homomorphism
˜ψP,I,I′:P⊗A HomA(I,I′)→HomA
(
HomAop(P,I ),I′{
in Cstr(Aen, gr).
388
Derived Categories | Amnon Yekutieli | 14 Apr 2019
To show thatψM is an isomorphism whenM ∈D−
(..,f)(Aen, gr), we can forget
the A-module structure onM, and viewψM as a morphism in D(K, gr). So we
have a morphismψM between triangulated functorsD−
f (Aop, gr)→D(K, gr). It is
clear thatψA is an isomorphism. By Theorem 12.5.2(1), which is valid also in the
algebraically graded context,ψM is an isomorphism for everyM∈D−
f (Aop, gr). □
Proof of Theorem17.1.10. Deﬁne the duality functors
DA := RHomA(−,R ), D Aop := RHomAop(−,R ),
D′
A := RHomA(−,R′), D ′
Aop := RHomAop(−,R′).
These are contravariant triangulated functors fromD(Aen, gr) to itself. Then deﬁne
the complexes T := ( D′
A ◦DAop)(A) = RHom A(R,R′) and T′:=
(DA◦D′
Aop)(A) = RHom A(R′,R ) in D(Aen, gr). Note that by Theorem 17.1.6
we haveT,T′∈Db
(f,..)(Aen, gr). Hence the graded bimodulesHk(T ) and Hk(T′) are
all bounded below.
According to Lemma 17.1.13 and Theorem 17.1.6 (applied twice) there are iso-
morphisms
T′⊗L
AT∼= (D′
A◦DAop)(T′) = (D′
A◦DAop◦DA◦D′
Aop)(A)
∼= (D′
A◦D′
Aop)(A)∼=A
in D(Aen, gr). By symmetry, there is also an isomorphism T⊗L
A T′∼= A in
D(Aen, gr). By Lemma 17.1.11 there is an isomorphismT∼=A(φ,i)[j]in D(Aen, gr),
for a unique automorphismφand unique integersi,j.
Finally we obtain these isomorphisms
R⊗AA(φ,i)[j]∼=R⊗L
AT∼=†(D′
A◦DAop)(R)
∼= (D′
A◦DAop◦DA)(A)∼=D′
A(A) =R′
in D(Aen, gr). The isomorphism∼=†is from Lemma 17.1.13. □
17.2. Balanced DC: Deﬁnition, Uniqueness and Local Duality.Our goal in
this subsection is to relate graded NC dualizing complexes with derived torsion. We
continue with Conventions 15.1.17 and 15.2.1, and we assume the following setup:
Setup 17.2.1.K is a base ﬁeld, andA is a noetherian connected gradedK-ring,
with augmentation ideal m. The augmentation ideal of the opposite ringAop is
mop.
Recall the graded bimoduleA∗= HomK(A,K).
Deﬁnition 17.2.2([161]). Under Setup 17.2.1, abalanced dualizing complexover
A is a pair(R,β), where:
(B1) R∈D(Aen, gr)is a graded NC dualizing complex overA(Deﬁnition 17.1.4),
with symmetric derivedm-torsion (Deﬁnition 16.5.7).
(B2) β: RΓ m(R)
≃
− →A∗is an isomorphism in D(Aen, gr), called a balancing
isomorphism.
The lack of left-right symmetry in item (B2) of this deﬁnition will be removed
in Corollary 17.2.16 below.
Remark 17.2.3. Deﬁnition 17.2.2 is a bit more sophisticated than the original
deﬁnition in [161]. There the condition was thatRΓ m(R)∼= RΓ mop(R)∼= A∗in
D(Aen, gr), but a balancing isomorphismβwas not speciﬁed. The current improved
deﬁnition is inﬂuenced by later research, especially [183] and [157].
The next theorem is implicit in [161] and [183].
389
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Theorem 17.2.4 (Uniqueness of BDC). Under Setup 17.2.1, suppose that(R,β)
and (R′,β′) are balanced dualizing complexes overA. Then there is a unique iso-
morphism ψ:R′≃
− →R in D(Aen, gr), such thatβ◦RΓ m(ψ) =β′as isomorphisms
RΓ m(R′)
≃
− →A∗in D(Aen, gr).
Proof. ByTheorem17.1.10thereisanisomorphism ψ†:R′≃
− →R⊗ALin D(Aen, gr),
whereL =A(φ,i)[j]is a translate of a twisted bimodule. Applying the functorRΓ m
to ψ†we get a diagram of isomorphisms
(17.2.5) RΓ m(R′)
RΓm(ψ†)
∼=
//
β′∼=

RΓ m
(
R⊗AL
{ γ
∼=
// RΓ m(R)⊗AL
β⊗id ∼=

A∗ A∗⊗AL
in D(Aen, gr). The isomorphism γis the obvious one. ThereforeA∗∼= A∗⊗AL
in M(Aen, gr). Due to the NC Graded Matlis Duality (Theorem 15.2.34) we have
L∼=A in M(Aen, gr).
Let us now rewrite diagram (17.2.5) withL =A. This is the solid diagram
(17.2.6) RΓ m(R′)
RΓm(ψ†)
∼=
//
β′∼=

RΓ m(R)
β∼=

A∗ c·(−)
∼=
//A∗
in D(Aen, gr). Because the automorphisms ofA∗in D(Aen, gr) are multiplication
by nonzero elements ofK, there is a uniquec∈K×for which the diagram (17.2.6)
is commutative. Henceψ:=c−1·ψ†is the unique isomorphismR′≃
− →R satisfying
β◦RΓ m(ψ) =β′. □
The next theorem is a noncommutative version of Grothendieck’s Local Duality
Theorem [62, Theorem V.6.2]. Balanced dualizing complexes were invented in order
to make this theorem hold. Theorem 17.2.7 ﬁrst appeared in [161], in a slightly
diﬀerent formulation, and with a complicated proof. The current formulation of
the theorem, as well as the proof, are taken from [39, Proposition 3.4]. We thank
R. Vyas for pointing out this proof to us.
Theorem 17.2.7 (Local Duality). Under Setup 17.2.1, let (R,β) be a balanced
dualizing complex overA. There is a morphism
ξ: RHomA(−,R )→
(
RΓ m(−)
{∗
of triangulated functors D(A, gr)op →D(Aop, gr), such that for every M ∈
D+
f (A, gr) the morphism
ξM : RHomA(M,R )→
(
RΓ m(M)
{∗
in D(Aop, gr) is an isomorphism.
Note that this result resembles Van den Bergh’s Local Duality, Corollary 16.4.11
– but this is misleading: the assumptions are not the same.
Proof. The proof is divided into three steps.
Step 1. Choose K-injective resolutionsR→J and ρ: Γ m(J)→K in Cstr(Aen, gr).
For eachM ∈D(A, gr) choose a K-injective resolutionM →IM in Cstr(A, gr).
There is an obvious homomorphism
φM : HomA(IM,J )→HomA
(
Γ m(IM), Γ m(J)
{
390
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in Cstr(Aop, gr). Next we have the homomorphism
HomA(id,ρ) : HomA
(
Γ m(IM), Γ m(J)
{
→HomA
(
Γ m(IM),K
{
in Cstr(Aop, gr). Composing these homomorphisms, and then going to the derived
category, we obtain a morphism
(17.2.8)
θM := Q
(
HomA(id,ρ)◦φM
{
:
RHomA(M,R )→RHomA
(
RΓ m(M), RΓ m(R)
{
in D(Aop, gr). We have the balancing isomorphism
(17.2.9) β: RΓ m(R)
≃
− →A∗
in D(Aen, gr). According to Proposition 15.2.5 there is an isomorphism
αM : RHomA
(
RΓ m(R),A∗{≃
− →
(
RΓ m(R)
{∗
in D(Aop, gr), and it is functorial inM. Let us deﬁne the morphism
(17.2.10) ξM :=αM◦RHom(id,β)◦θM : RHomA(M,R )→
(
RΓ m(M)
{∗
in D(Aop, gr). By construction the morphismξM is functorial inM.
Step 2. Take the complexM := R. By deﬁnitionR has the NC derived Morita
property on theA side. This implies that the elementidR∈H0(
RHomA(R,R )
{
is
a basis of this rank1 graded-freeAop-module. Because of the isomorphism (17.2.9)
and by graded Matlis Duality, we know thatRΓ m(R) has the NC derived Morita
property on theA side. Therefore the element
idRΓm(R)∈H0(
RHomA
(
RΓ m(R), RΓ m(R)
{{
is a basis of this rank1 graded-freeAop-module. The construction of the morphism
θR in (17.2.8) shows thatH0(θR)(idR) = idRΓm(R). We conclude thatH0(θR) is an
isomorphism. Since all other cohomologies of the complexes below vanish, it follows
that
(17.2.11) θR : RHomA(R,R )→RHomA
(
RΓ m(R), RΓ m(R)
{
is an isomorphism in D(Aop, gr). Therefore, in view of (17.2.10), ξR is also an
isomorphism.
Step 3. Deﬁne the functor
F :=
(
RΓ m(−)
{∗
: D(A, gr)op→D(Aop, gr).
Thusξ:DA→F is a morphism of triangulated functors, and we must prove that
ξM :DA(M)→F (M) is an isomorphism for everyM∈D+
f (A, gr). We know that
DAop : D−
f (Aop, gr)op→D+
f (A, gr) is an equivalence. Thus it suﬃces to prove that
the morphism
(17.2.12) ζ:=ξ◦idDAop :DA◦DAop→F◦DAop
of functors D−
f (Aop, gr)→D(Aop, gr) is an isomorphism.
Consider the objectA∈D−
f (Aop, gr). By formula (17.2.12) the diagram
(DA◦DAop)(A)
ζA

id // RHomA(R,R )
ξR

(F◦DAop)(A) id //(
RΓ m(R)
{∗
in D(Aop, gr) is commutative. In step 2 we proved that ξR is an isomorphism.
Hence ζA is an isomorphism.
391
Derived Categories | Amnon Yekutieli | 14 Apr 2019
The functors DA and DAop have bounded cohomological displacements, and
hence so does their compositionDA◦DAop. (In fact the composition is isomor-
phic to the identity functor, so it has cohomological displacement [0, 0].) The
functor RΓ m has bounded below cohomological displacement, and the contravari-
ant functor (−)∗has cohomological displacement [0, 0], so their composition F
has bounded above cohomological displacement. We conclude that the functors
DA◦DAop and F◦DAop have bounded above cohomological displacements. We
have already established thatζA is an isomorphism. Theorem 12.5.2(1), which is
valid also in the algebraically graded setting, says thatζN is an isomorphism for
everyN∈D−
f (Aop, gr). □
Corollary 17.2.13([182]). Under Setup17.2.1, assumeA has a balanced dualizing
complex. Then A satisﬁes theχcondition, and it has ﬁnite local cohomological
dimension.
Proof. GivenM∈Mf(A, gr), Theorem 17.2.7 provides an isomorphism
ξM : RHomA(M,R )
≃
− →
(
RΓ m(M)
{∗
in D(Aop, gr). This gives an isomorphism
(17.2.14) H−p(ξM) : Ext−p
A (M,R )
≃
− →
(
Hp
m(M)
{∗
in M(Aop, gr) for every p. By Theorem 17.1.6(1) we know that Ext−p
A (M,R )∈
Mf(Aop, gr). Using NC graded Matlis Duality (Theorem 15.2.34) we get
(17.2.15) Hp
m(M)∼=
(
Ext−p
A (M,R )
{∗
∈Mcof(A, gr).
By Proposition 16.5.17 we conclude thatA satisﬁes the leftχcondition. The op-
symmetry of the situation implies thatAop also satisﬁes the leftχcondition.
Because R∈Db(Aen, gr) and is nonzero, we haveq0 := inf(H(R))∈Z. So
Extq
A(M,R ) = 0 for all M ∈M(A, gr) and q < q0. Taking p :=−q and using
(17.2.15) we getHp(RΓ m(M)) = Hp
m(M) = 0 for allp> −q0. So the functorRΓ m
has ﬁnite cohomological dimension. The op-symmetry of the situation implies that
the functor RΓ mop also has ﬁnite cohomological dimension. □
Corollary 17.2.16.Let (R,β) be a balanced dualizing complex overA. Then there
is a unique symmetry isomorphismϵR : RΓ m(R)
≃
− →RΓ mop(R) in D(Aen, gr), in the
sense of Deﬁnition16.5.7. Hence there is a unique isomorphismβop : RΓ mop(R)
≃
− →
A∗D(Aen, gr) such thatβop◦ϵR =β.
Proof. By Corollary 17.2.13 the ringA has ﬁnite local cohomological dimension.
So Theorem 16.5.8 applies. □
