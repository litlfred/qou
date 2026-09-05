---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-103-18-rigid-noncommutative-dualizing-complexes
section_title: "Rigid Noncommutative Dualizing Complexes"
section_number: 18
pages: 411-425
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
In this section of the book we are going to work with noncommutative (namely
not necessarily commutative) rings. We shall often use the abbreviation “NC” for
“noncommutative”. The goal is to introducerigid NC dualizing complexesin the
sense of M. Van den Bergh [153], and to prove their existence and uniqueness under
certain conditions.
18.1. Noncommutative Dualizing Complexes.Here we will deﬁne NC dual-
izing complexes over a NC ringA. The deﬁnition is almost identical to that in
the NC graded setting (see Subsection 17.1). We will prove that the NC dualizing
complexes overA are parameterized by the derived Picard group ofA. The content
of this subsection is adapted from the paper [165].
LetKbe a commutative ring. Recall (from Deﬁnition 1.2.1) that acentralK-ring
is a ringA equipped with a ring homomorphismK→Cent(A), where Cent(A) is
the center ofA. In more traditional texts, a centralK-ring is called anassociative
unitalK-algebra. The category of centralK-rings, withK-ring homomorphisms, is
denoted by Rng/cK.
Here is the convention that is in force throughout this section:
Convention 18.1.1. There is a base ﬁeldK. All rings are by default centralK-
rings, and all homomorphisms betweenK-rings are overK; namely we work within
the category Rng/cK. All bimodules are K-central, and all additive functors are
K-linear. We use the notation⊗for⊗K. For a ringA we writeAen := A⊗Aop,
the enveloping ring ofA.
See Remark 18.1.30 regarding the assumption that the base ringK is a ﬁeld.
Recall that a NC ringA is called noetherian if it is both left noetherian and right
noetherian. See Remark 15.1.30 regarding the failure of the noetherian property to
be preserved under ﬁnitely generated ring extensions.
LetA be a ring. As before,M(A) is the category of leftA-modules. The category
of rightA-modules is M(Aop), and the category ofA-bimodules is M(Aen). Given
another ringB, the category ofA-B-bimodules is M(A⊗Bop). These areK-linear
abelian categories.
The derived category of M(A) is D(A) := D(M(A)); its objects are the com-
plexes of (left)A-modules. The other derived categories areD(Aop) := D(M(Aop)),
D(Aen) := D(M(Aen)) and D(A⊗Bop) := D(M(A⊗Bop)).
Consider the canonical ring anti-automorphismop :B→Bop, that is the iden-
tity on the underlyingK-module. There is a canonical ring isomorphism
(18.1.2) A⊗Bop ≃
− →Bop⊗A, a ⊗op(b)↦→op(b)⊗a.
The induced isomorphism on the bimodule categories M(A ⊗Bop)
≃
− →
M(Bop⊗A) is the identity on the underlyingK-modules. Indeed, forM∈M(A⊗
Bop), m ∈M and a⊗op(b) ∈A⊗Bop, we have (op(b)⊗a)·m = a·m·b =
(a⊗op(b))·m. Now takeB =A in (18.1.2). Since (Aop)op =A, there is a canoni-
cal ring isomorphism
(18.1.3) Aen =A⊗Aop ≃
− →Aop⊗A = (Aop)en
and an induced isomorphism on the bimodule categories
(18.1.4) M(Aen)
≃
− →M((Aop)en).
ThismaterialwillbepublishedbyCambridgeUniversityPressas Derived CategoriesbyAmnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works.c© Amnon Yekutieli, 2019.
411
Derived Categories | Amnon Yekutieli | 14 Apr 2019
All these categorical relations pass to derived categories.
The ringAen is isomorphic to its opposite ring. There is a ring isomorphism
(18.1.5) trop :Aen ≃
− →(Aen)op
with this formula: fora1,a 2∈A it sends the elementa1⊗op(a2)∈Aen to
(18.1.6) trop(a1⊗op(a2)) := op(a2⊗op(a1))∈(Aen)op.
On the underlyingK-moduleA⊗A this is just the transpositiona1⊗a2↦→a2⊗a1,
and hence the name “transpose opposite” and the acronym “trop”.
Usually anA-A-bimodule M is seen as a leftAen-module, with this action of an
elementa1⊗op(a2)∈Aen on an elementm∈M :
(18.1.7) (a1⊗op(a2))·m =a1·m·a2.
But using the ring isomorphismtrop from formula (18.1.5) we can also consider
M as a left(Aen)op-module, and thus as a rightAen-module. Explicitly, the right
action of an elementa2⊗op(a1)∈Aen on an elementm∈M is:
(18.1.8)
m·(a2⊗op(a1)) =♥op(a2⊗op(a1))·m
=†(a1⊗op(a2))·m =♦a1·m·a2.
In equality =♥we move from a right action byAen to the left action by(Aen)op,
and in equality=†we made use of formula (18.1.6) to move from(Aen)op to Aen.
Finally, the equality=♦is formula (18.1.7). This game of musical chairs will be
played in Subsections 18.5 and 18.2.
Let A and B be rings. The canonical ring homomorphisms
A→A⊗Bop←Bop
induce restriction functors
(18.1.9) D(A)
RestA
←−−−−D(A⊗Bop)
RestBop
−−−−−→D(Bop).
See the commutative diagram 14.2.3. We shall usually keep these restriction func-
tors implicit, and instead use terminology like in Deﬁnition 14.2.18.
In Deﬁnition 12.5.1 we introduced this notation: for a ringAwe denote byMf(A)
the full subcategory ofM(A) on the ﬁnite (i.e. ﬁnitely generated)A-modules. And
Df(A) is the full subcategory ofD(A) on the complexes ofA-modules M such that
Hi(M)∈Mf(A) for everyi.
If A is left noetherian, thenMf(A) is a thick abelian subcategory ofM(A); and
hence Df(A) is a full triangulated subcategory ofD(A). As usual we can combine
indicators: D⋆
f (A) := Df(A)∩D⋆(A), where⋆is some boundedness indicator (+,
−, b or⟨empty⟩).
Now to ﬁniteness ofA-B-bimodules. The expression M(f,..)(A⊗Bop) denotes
the full subcategory ofM(A⊗Bop) on the bimodules that are ﬁnite overA; and
the expression M(..,f)(A⊗Bop) denotes the full subcategory on the bimodules that
are ﬁnite overBop. Of course we deﬁne
M(f,f)(A⊗Bop) := M(f,..)(A⊗Bop)∩M(..,f)(A⊗Bop).
The same notation shall apply to derived categories.
To a complex of bimodulesM∈D(A⊗Bop) we associated two derived homo-
thety morphisms in Subsection 14.4. Let us recall them. The derived homothety
morphism throughBop is the morphism
(18.1.10) hmR
M,Bop :B→RHomA(M,M )
in D(Ben); and the derived homothety morphism throughA is the morphism
(18.1.11) hmR
M,A :A→RHomBop(M,M )
412
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in D(Aen). According to Deﬁnition 14.4.14, the complexM has the noncommuta-
tive derived Morita property on theA side (resp. on theBop side) if the morphism
hmR
M,Bop (resp. hmR
M,A) is an isomorphism.
Deﬁnition 18.1.12([165]). Let A be a noetherian ring. Anoncommutative du-
alizing complex over A is an object R∈Db(Aen) satisfying the following three
conditions:
(i) For everyp the A-bimodule Hp(R) is ﬁnite overA and overAop.
(ii) The complexR has ﬁnite injective dimension overA and overAop.
(iii) The complex of bimodulesR has the noncommutative derived Morita prop-
erty on both sides.
Note that conditions (i) and (ii) are one-sided, namely they refer separately to
RestA(R)∈D(A) and to RestAop(R)∈D(Aop); whereas condition (iii) is more
complicated, and we will study it further in Lemma 18.1.21 below. Also note that
condition (i) can be stated as “R belongs to D(f,f)(Aen)”.
Before going on, we need to say something about the op-symmetry of Deﬁnition
18.1.12. Given a complexR∈D(Aen), by formula (18.1.4) the complexR is also
an object of D((Aop)en), and we could ask whetherR is a dualizing complex over
the ring Aop. The answer is positive of course, because all three conditions are
op-symmetric. We record this fact as the next proposition.
Proposition 18.1.13. If R is a NC dualizing complex overA, then R is also a
NC dualizing complex overAop.
Example18.1.14. ANCring Aiscalled regularifithasﬁniteglobalcohomological
dimension on both sides. This is very similar to the graded deﬁnition (see Deﬁnition
15.4.1). Let us recall what it means: there is some natural numberd such that
Exti
A(M,N ) = 0 for alli>d and allM,N ∈M(A); and alsoExti
Aop(M′,N′) = 0
for alli > dand allM′,N′∈M(Aop). The smallest such numberd is the global
cohomological dimension ofA.
Such rings are easy to ﬁnd; for instance, ifK is a ﬁeld, andg is ﬁnite Lie
algebra overK, then theuniversal enveloping ringA := U(g) is regular; the global
cohomological dimension ofA is d := rankK(g).
A weaker condition is this:A is calledGorensteinifA has ﬁnite injective dimen-
sion both as a left module and as a right module over itself. Namely there is some
natural numberd such that Exti
A(M,A ) = 0 for alli>d and allM∈M(A); and
also Exti
Aop(M′,A ) = 0 for alli>d and allM′∈M(Aop).
Assume A is Gorenstein. Then the complex of bimodulesR :=A satisﬁes con-
dition (ii) of Deﬁnition 18.1.12. Conditions (i) and (iii) of this deﬁnition are auto-
matically true. We conclude thatR :=A is a NC dualizing complex over itself.
Deﬁnition 18.1.15.LetA be a noetherian ring, letR be a NC dualizing complex
overA, and letB be a second ring. Theduality functors associated toR are the
triangulated functors
DA : D(A⊗Bop)op→D(B⊗Aop), D A := RHomA(−,R )
and
DAop : D(B⊗Aop)op→D(A⊗Bop), D Aop := RHomAop(−,R ).
Notice that the expressionsDA andDAop leaveR andB implicit; this is because
thedualizingcomplex Ristakentobeﬁxed, andthesecondring B islessimportant.
TheNCderivedHom-evaluationmorphismswerealreadydiscussedinSubsection
17.1, in the algebraically graded context. The nongraded deﬁnition is very similar.
Given a complexM∈D(A⊗Bop), there is a morphism
(18.1.16) evR,R
M :M→DAop(DA(M)) = RHomAop
(
RHomA(M,R ),R
{
413
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in D(A⊗Bop), which is functorial inM. If we choose a K-injective resolution
R→I in D(Aen), then we have an isomorphism
DAop(DA(M))∼= HomAop
(
HomA(M,I ),I
{
in D(A⊗Bop), and the morphism evR,R
M is represented by the Hom-evaluation
homomorphism
evM,I :M→HomAop
(
HomA(M,I ),I
{
in Cstr(A⊗Bop). For this we use the results of Subsection 14.3, that apply because
A and B are ﬂat overK.
In the special case whenB =A and M =A, the morphismevR,R
A recovers the
derived homothety morphism throughA, see (18.1.11); i.e.
(18.1.17) hmR
R,A = evR,R
A :A→RHomAop(R,R )
in D(Aen). This formula makes implicit use of the left co-unitor isomorphismlcu :
RHomA(A,R )
≃
− →R in D(Aen). Likewise for the homothety morphismhmR
R,Aop.
Theorem 18.1.18. Let A be a noetherian ring, letR be a NC dualizing complex
over A, letB be a second ring, and letDA and DAop be the duality functors asso-
ciated toR. Let⋆be a boundedness indicator, and letM∈D⋆
(f,..)(A⊗Bop). Then
the following hold:
(1) The complexDA(M) belongs to D−⋆
(..,f)(B⊗Aop), where−⋆is the reversed
boundedness indicator.
(2) The derived Hom-evaluation morphism evR,R
M : M →DAop(DA(M)) in
D(A⊗Bop) is an isomorphism.
Proof. The proof is the same as that of Theorem 17.1.6, with the obvious modiﬁ-
cations (i.e. neglecting the algebraic grading). It all boils down to Theorems 12.5.7
and 12.5.2. □
Corollary 18.1.19. Under the assumptions of Theorem18.1.18, the functor
DA : D⋆
(f,..)(A⊗Bop)op→D−⋆
(..,f)(B⊗Aop)
is an equivalence of triangulated categories, with quasi-inverseDAop.
Proof. First we note that the op-symmetry (Proposition 18.1.13) implies that The-
orem 18.1.18 is true after exchangingA withAop. Thus evR,R
N :N→DA(DAop(N))
is an isomorphism for everyN∈D−⋆
(..,f)(B⊗Aop). Now the assertion is clear. □
We need a better understanding of the derived homothety morphisms. Suppose
M∈C(A⊗Bop). The right action ofB onM is the homothety ring homomorphism
through Bop, hmM,Bop : Bop→EndCstr(A)(M). Namely for elementsb∈B and
m∈Mi we have hmM,Bop(op(b))(m) = m·b∈Mi. By composing hmM,Bop with
the localization functorQ : Cstr(A)→D(A) we obtain the ring homomorphism
(18.1.20) hmD
M,Bop := Q◦hmM,Bop :Bop→EndD(A)(M).
Lemma 18.1.21.LetM∈D(A⊗Bop). The three conditions below are equivalent.
(i) M has the derived Morita property on theA side, i.e. (18.1.10) is an iso-
morphism.
(ii) For everyp⁄= 0 the moduleHomD(A)(M,M [p]) is zero, and the ring homo-
morphism hmD
M,Bop :Bop→EndD(A)(M) is bijective.
(iii) For every p ⁄= 0 the module Hp(
RHomA(M,M )
{
is zero, and the Bop-
module H0(
RHomA(M,M )
{
is free, with basis the elementidM.
414
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. This is clear from the canonical isomorphisms
HomD(A)
(
M,M [p]
{∼= Hp(
RHomA(M,M )
{
of Corollary 12.2.8. □
Lemma 18.1.22. LetT∈D(Aen), and consider the triangulated functor
G :=T⊗L
A (−) : D(A⊗Bop)→D(A⊗Bop).
For everyM∈D(A⊗Bop) the diagram
Bop hmD
M,Bop
//
hmD
G(M),Bop
((
EndD(A)(M)
G

EndD(A)(G(M))
of ring homomorphisms is commutative.
Proof. This is because the action ofBop onM is categorical, i.e. by endomorphisms
in D(A). □
Lemma 18.1.23. LetR∈D(Aen), and consider the triangulated functor
D := RHomA(−,R ) : D(A⊗Bop)op→D(B⊗Aop).
For everyM∈D(A⊗Bop) the diagram
Bop hmD
M,Bop
//
Op(hmD
D(M),B)
))
EndD(A)(M)
D

EndD(Aop)(D(M))op
of ring homomorphisms is commutative.
Proof. Same as the previous lemma, only hereD is contravariant. □
Tilting DG bimodules were deﬁned in Deﬁnition 14.4.1. Here we call themtilting
complexes. Given a tilting complexT∈D(Aen), we know that its quasi-inverseT∨
satisﬁesT∨∼= RHomA(T,A )∼= RHomAop(T,A ) in D(Aen). See Corollary 14.4.27
with B =A, and use the ring isomorphism (18.1.3).
Lemma 18.1.24. Let T be a tilting complex complex overA, with quasi-inverse
T∨. Then there is an isomorphism T⊗L
A (−)∼= RHomA(T∨,−) of triangulated
functors from D(A⊗Bop) to itself.
Proof. Let’s writeS := T∨. Then T ∼= S∨∼= RHomA(S,A ). We know thatS is
perfect on theA side (see Corollary 14.4.28), so by Theorem 14.1.22 we have
T⊗L
AM∼= RHomA(S,A )⊗L
AM
∼= RHomA(S,A⊗L
AM)∼= RHomA(T∨,M ). □
Theorem 18.1.25([165]). LetA be a noetherian ring, and letR be a NC dualizing
complex overA.
(1) Given a tilting complexT over A, the complexR′:=T⊗L
AR is also a NC
dualizing complex overA.
(2) Given a second NC dualizing complex R′over A, the complex T :=
RHomA(R,R′) is a tilting complex overA, andR′∼=T⊗L
AR in D(Aen).
(3) IfT is a tilting complex overA, and ifT⊗L
AR∼=R in D(Aen), thenT∼=A
in D(Aen).
415
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof.
(1) We need to verify thatR′satisﬁes conditions (i)-(iii) of Deﬁnition 18.1.12.
Consider the equivalence of triangulated categoriesG := T⊗L
A (−) : D(A)→
D(A). The functor G has ﬁnite cohomological dimension (see Theorem 14.1.22,
Corollary 14.4.28 and Proposition 14.1.5). Now G(A) = T, and T ∈Db
f (A) by
Theorem 14.1.26, so Theorem 12.5.8 tells us thatG(M)∈Db
f (A) for everyM∈
Db
f (A). TakingM :=R we see thatR′=G(R)∈Db
f (A).
Let T∨be the quasi-inverse ofT. By Lemma 18.1.24, withB =A, we see that
(18.1.26) R′=T⊗L
AR∼= RHomA(T∨,R ) =DA(T∨)
in D(Aen). The tilting complex T∨belongs to Db
f (A), so according to Theorem
18.1.18(1) withB =K, we see thatDA(T∨)∈Db
f (Aop). Thus R′∈Db
f (Aop). We
have now veriﬁed condition (i) of Deﬁnition 18.1.12 forR′.
To prove thatR′has ﬁnite injective dimension overA, we need to ﬁnd a uniform
bound on the cohomology ofRHomA(M,R′), for allM∈M(A). This is the same
as ﬁnding a natural numberd such that HomD(A)(M,R′[i]) = 0 for allM∈M(A)
and|i|>d . We shall use the equivalence of triangulated categories
G∨:=T∨⊗L
A (−)∼= RHomA(T,−) : D(A)→D(A).
Since R∼=G∨(R′), we obtain aK-module isomorphism
G∨: HomD(A)
(
M,R′[i]
{≃
− →HomD(A)
(
G∨(M),R [i]
{
for everyi. The functor G∨has ﬁnite cohomological dimension, andR has ﬁnite
injective dimension; their sumd serves as the required bound.
Now let us prove thatR′has ﬁnite injective dimension overAop. Take a module
M∈M(Aop). We have these isomorphisms for every integeri :
Hi(
RHomAop(M,R′)
{∼=1 HomD(Aop)
(
M,R′[i]
{
∼=2 HomD(Aop)
(
M,DA(T∨)[i]
{
∼=3 HomD(A)
(
T∨,DAop(M)[i]
{
∼=4 Hi(
RHomA
(
T∨, RHomAop(M,R )
{{
∼=5 Hi(
T⊗L
A RHomAop(M,R )
{
= Hi(
(G◦DAop)(M)
{
.
The justiﬁcations are as follows:
∼=1 : This is by Corollary 12.2.8.
∼=2 : This is by formula (18.1.26).
∼=3 : This relies on Corollary 18.1.19.
∼=4 : Again we use Corollary 12.2.8.
∼=5 : It is due to Lemma 18.1.24.
The functorsG and DAop have ﬁnite cohomological dimensions, so we have a uni-
form bound on the cohomology of(G◦DAop)(M). This completes the proof that
R′satisﬁes condition (ii) of Deﬁnition 18.1.12.
To prove thatR′has the derived Morita property on theA side we use the
fact thatR has the derived Morita property on theA side, and we invoke Lemma
18.1.21 withB := A and M := R. Since R′= G(R), for everyi∈Z we have an
isomorphism ofK-modules
G : HomD(A)
(
R,R [i]
{≃
− →HomD(A)
(
R′,R′[i]
{
,
416
Derived Categories | Amnon Yekutieli | 14 Apr 2019
andthisiszerowhen i⁄= 0. Fori = 0weuseLemma18.1.22: thereisacommutative
diagram of rings
Aop hmD
Aop,R
∼=
//
hmD
Aop,R′
((
EndD(A)(R)
G∼=

EndD(A)(R′)
and the vertical arrowG is an isomorphism. ThereforehmD
Aop,R′is a ring isomor-
phism.
Finally, to prove thatR′has the derived Morita property on theAop side we
use the fact that the tilting complexT∨has the derived Morita property on theA
side (by Corollary 14.4.28), together with Lemma 18.1.21, applied to the complexes
T∨∈M(A⊗Aop) andR′∈M(Aop⊗A). Recall from (18.1.26) thatR′∼=DA(T∨)
in D(Aen). By Corollary 18.1.19, for everyi∈Z we have an isomorphism ofK-
modules
DA : HomD(A)
(
T∨,T∨[i]
{≃
− →HomD(Aop)
(
R′,R′[i]
{
,
andthisiszerowhen i⁄= 0. Fori = 0weuseLemma18.1.23: thereisacommutative
diagram of rings
Aop
hmD
Aop,T∨
∼=
//
Op(hmD
A,R′)
((
EndD(A)(T∨)
DA∼=

EndD(Aop)(R′)op
It follows thathmD
A,R′:A→EndD(Aop)(R′) is a ring isomorphism.
(2) The proof of this item is a minor modiﬁcation of the proof of Theorem 17.1.10.
Indeed, an ungraded version of Lemma 17.1.13 holds here, and we use Theorem
18.1.18 instead of Theorem 17.1.6.
(3) Assume thatT⊗L
AR∼=R in D(Aen). Of courseR =DA(A). Formula (18.1.26)
says that DA(A)∼= DA(T∨) in D(Aen). By Corollary 18.1.19 we conclude that
A∼=T∨in D(Aen). But thenA∼=T in D(Aen). □
The op-symmetry that gave rise to Proposition 18.1.13 implies that several vari-
ations of Theorem 18.1.25 are true. We wish to write down only one of them, that
will be needed later.
Corollary 18.1.27.LetA be a noetherian ring, and letR and R′be NC dualizing
complexes overA. Then there is a tilting complexT′such thatR′∼= R⊗L
AT′in
D(Aen).
Proof. This is a trivial (yet confusing) consequence of item (2) of Theorem 18.1.25,
when viewingR and R′as NC dualizing complexes over the ringAop. □
Recall that a left action of a groupG on a nonempty setX is called simply
transitive if there is oneG-orbit inX, and the stabilizer of every pointx∈X is
trivial. I.e. for every (or equivalently, for some) pointx∈X the action function
G×{x}→X, (g,x )↦→g(x), is bijective.
Corollary 18.1.28. LetA be a ring, and assume it has at least one NC dualizing
complex. Then the left action of the group DPicK(A) on the set of isomorphism
classes of NC dualizing complexes, induced by the bifunctor(T,R )↦→T⊗L
AR, is
simply transitive.
417
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. By Theorem 18.1.25(1) this is a well-deﬁned action:T⊗L
AR is a NC dual-
izing complex. The action is transitive by Theorem 18.1.25(2), and it has trivial
stabilizers by Theorem 18.1.25(3). □
Remark 18.1.29. Suppose A is a noetherian commutativeK-ring. A noncom-
mutative dualizing complex overA is not the same as a commutative dualizing
complex overA, in the sense of Deﬁnition 13.1.9. Indeed, there is aK-ring ho-
momorphism Aen→A, and this induces a restriction functorD(A)→D(Aen). If
R∈D(A) is a commutative dualizing complex overA, then its image inD(Aen)
is a noncommutative dualizing complex overA. However, according to Theorem
18.1.25(1), given any tilting complexT overA, the complexR′:=T⊗L
AR is also
a NC dualizing complex overA. And R′can very easily fail to be in the essential
image of D(A); e.g. by takingT :=A(ψ), the twist by an automorphismψof the
trivial bimoduleA.
Remark 18.1.30. In case the base ringK is not a ﬁeld, butA is aﬂat noetherian
K-ring, then the deﬁnitions and results in this subsection are still valid.
In case the ringA is noetherian, but is not ﬂat over the base ringK, we can
still deﬁne NC dualizing complexes over it. For that we choose a K-ﬂat DG ring
resolution ˜A →A over K; see Theorem 12.8.7 and Proposition 12.8.5. A NC
dualizing complex overA is then a complexR∈D( ˜Aen) that satisﬁes the three
conditions of Deﬁnition 18.1.12. As explained in Remark 14.3.24, the triangulated
category D( ˜Aen) is independent of the resolution˜A, up to a canonical equivalence.
This means that the dualizing complexR is also independent of the resolution.
It is expected that Theorems 18.1.18 and 18.1.25 will still hold in this general
situation; but we did not verify this assertion.
However, ﬂatness alone is not suﬃcient for many of the results in the following
subsections (mainly in Subsection 18.5, in which we rely on results from Section
17, that assumed Convention 15.1.17.) Therefore we decided to assumeK is a ﬁeld
in the current subsection as well.
18.2. Rigid NC DC: Deﬁnition and Uniqueness.In this subsection we intro-
duce rigid NC dualizing complexes, and prove their uniqueness. The material is
mostly from Van den Bergh’s paper [153], with some improvements coming from
[165]. We continue with Convention 18.1.1; in particular,K is a base ﬁeld, and all
rings are central overK.
Let A be a ring, and letM,N ∈M(Aen). The K-module M⊗N has twoA-
module structures and twoAop-module structures, all commuting with each other.
We organize them into anoutside actionand aninside actionof the ringAen. Here
are the formulas: given elementsm∈M, n∈N and a1,a 2∈A, we let
(18.2.1) (a1⊗op(a2))·out (m⊗n) := (a1·m)⊗(n·a2)
and
(18.2.2) (a1⊗op(a2))·in (m⊗n) := (m·a2)⊗(a1·n).
In these formulas we are using the canonical anti-automorphismop :A→Aop. We
shall denote the two copies ofAen that act onM⊗N by
(18.2.3) Aen,out =Aout⊗Aop,out
and
(18.2.4) Aen,in =Ain⊗Aop,in.
Namely the ringAen,out acts onM⊗N by the outside action (18.2.1), and the ring
Aen,in acts by the inside action (18.2.2).
418
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Let us deﬁne the ring
(18.2.5) Afour :=Aen,out⊗Aen,in.
There are ring homomorphisms
(18.2.6) Aen,out→Afour←Aen,in.
With this notation we haveM⊗N∈M(Afour). The action of the ringAfour on
the moduleM⊗N is this, explicitly: an element
(
a1⊗op(a2)
{
⊗
(
a3⊗op(a4)
{
∈Afour
acts on an elementm⊗n∈M⊗N by
(
(a1⊗op(a2))⊗(a3⊗op(a4))
{
·(m⊗n) = (a1·m·a4)⊗(a3·n·a2).
In some situations we prefer to view the inside action ofAen on M⊗N as a
right action. This is possible by the isomorphismtrop from formula (18.1.5). To
be explicit, for elementsm⊗n∈M⊗N and a3⊗op(a4)∈Aen,in the action is as
follows, using formula (18.1.8):
(18.2.7)
(m⊗n)·in (a3⊗op(a4)) = (a4⊗op(a3))·in (m⊗n)
= (m·a3)⊗(a4·n).
Example 18.2.8.Suppose we takeM =N :=A∈M(Aen). ThenP :=M⊗N =
A⊗A can also be viewed asP∼= Aen, and then in it anAen-bimodule. The left
Aen-module structure onP∼=Aen is this: for a module elementb1⊗b2∈P and a
ring elementa1⊗op(a2)∈Aen we have
(
a1⊗op(a2)
{
·(b1⊗b2) = (a1·b1)⊗(b2·a2);
so this is the outside action onP = A⊗A. The right Aen-module structure on
P∼=Aen is this: for a ring elementa3⊗op(a4)∈Aen we have
(b1⊗b2)·
(
a3⊗op(a4)
{
= (b1·a3)⊗(a4·b2);
so this is the inside action onP =A⊗A, cf. (18.2.7).
Given bimodulesL,M,N ∈M(Aen), we denote byHomAen,out(L,M ⊗N) the
K-module of homomorphismsφ: L→M⊗N that areAen-linear for the outside
action ofAen on M⊗N. This is anAen-module by the inside action onM⊗N.
Namely
HomAen,out(L,M⊗N)∈M(Aen,in) = M(Aen).
All these four-module operations extend in an obvious way to complexes, and
can be derived.
Deﬁnition 18.2.9.Let A be a ring andM∈D(Aen). The NC square ofM is
the complex
SqA(M) := RHomAen,out(A,M⊗M)∈D(Aen,in) = D(Aen).
Of course the square is relative to the base ﬁeldK, which is implicit in the
formulas.
The square of the complexM is calculated as follows. First note that M is
K-ﬂat overK, sinceK is a ﬁeld; soM⊗M = M⊗L
KM∈D(Afour). We choose a
K-injective resolutionM⊗M→I in Cstr(Afour). The complexI is unique up to
a homotopy equivalence, that itself is unique up to homotopy (in other words,I
is unique up to a unique isomorphism inK(Afour)). Because of the ﬂatness of the
ring homomorphisms (18.2.6), the complexI is K-injective overAen,out, and
(18.2.10) SqA(M) = HomAen,out(A,I )∈D(Aen,in) = D(Aen).
419
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 18.2.11.Let φ: M→N be a morphism inD(Aen). The NC square
of φis the morphism
SqA(φ) := RHomAen,out(idA,φ⊗φ) : SqA(M)→SqA(N)
in D(Aen).
The square of the morphismφis calculated as follows. Choose a K-projective
resolution P →M in Cstr(Aen). Then φis represented by a homomorphism˜φ:
P →N in Cstr(Aen). The morphism φ⊗φ: M⊗M →N⊗N in D(Afour) is
represented by the homomorphism˜φ⊗˜φ: P⊗P→N⊗N in Cstr(Afour). Next
we choose K-injective resolutionsP⊗P→I and N⊗N→J in Cstr(Afour). The
homomorphism ˜φ⊗˜φinduces a homomorphism˜ψ:I→J in Cstr(Afour). Note that
˜ψis unique up to homotopy. Finally
SqA(φ) = Q
(
HomAen,out(idA, ˜ψ)
{
:
SqA(M) = HomAen,out(A,I )→SqA(N) = HomAen,out(A,J )
in D(Aen,in) = D(Aen).
Deﬁnition 18.2.12.LetA be a ring. ANC rigid complex overA is a pair(M,ρ),
where M∈D(Aen), andρ:M
≃
− →SqA(M) is an isomorphism inD(Aen), called a
NC rigidifying isomorphism.
Deﬁnition 18.2.13.Let (M,ρ) and (N,σ) be NC rigid complexes overA. A NC
rigid morphism overA
φ: (M,ρ)→(N,σ)
is a morphismφ:M→N in D(Aen), such that the diagram
M
ρ //
φ

SqA(M)
SqA(φ)

N σ // SqA(N)
in D(Aen) is commutative.
Deﬁnition 18.2.14.LetA be a ring. The category ofNC rigid complexes overA
is the category whose objects are the NC rigid complexes from Deﬁnition 18.2.12,
and whose morphisms are the NC rigid morphisms Deﬁnition 18.2.13.
Deﬁnition 18.2.15(Van den Bergh [153]). Let A be a noetherian ring. Arigid
NC dualizing complex overA is a NC rigid complex(R,ρ), such thatR is a NC
dualizing complex overA, in the sense of Deﬁnition 18.1.12.
Again, we remind that the notion of rigidity is relative to the base ﬁeldK.
Recall that the center of the ringA is denoted byCent(A). Of courseCent(A) =
Cent(Aop). Given a bimoduleM∈M(Aen), there are two ring homomorphisms
chmM,A, chmM,Aop : Cent(A)→EndM(Aen)(M),
that we call thecentral homothetiesthrough A and throughAop respectively. In
terms of elements they arechmM,A(a)(m) :=a·m and chmM,Aop(a)(m) :=m·a for
a∈Cent(A) and m∈M.
Example 18.2.16. For the bimoduleM =A, both ring homomorphisms
chmA,A, chmA,Aop : Cent(A)→EndM(Aen)(A)
are isomorphisms, and they are equal.
420
Derived Categories | Amnon Yekutieli | 14 Apr 2019
The ring homomorphismschmM,A and chmM,Aop extend to complexes, namely
for M∈C(Aen) there are ring homomorphisms
chmM,A, chmM,Aop : Cent(A)→EndCstr(Aen)(M).
By postcomposing them with the categorical localization functorQ we obtain ring
homomorphisms
chmD
M,A, chmD
M,Aop : Cent(A)→EndD(Aen)(M).
These central homotheties were already used in Subsection 14.5.
Example 18.2.17. For the complex of bimodulesM = A, both ring homomor-
phisms
chmD
M,A, chmD
M,Aop : Cent(A)→EndD(Aen)(A)
are isomorphisms, and they are equal. This is because of the fully faithful embed-
ding M(Aen)→D(Aen) and the previous example.
Lemma 18.2.18. Given R∈D(Aen), consider the functor
D := HomA(−,R ) : D(Aen)op→D(Aen).
Then for everyM∈D(Aen) the diagram of rings
Cent(A)
chmD
M,Aop
//
chmD
D(M),A
))
EndD(Aen)(M)
D

EndD(Aen)
(
D(M)
{op
is commutative.
Proof. Choose a K-injective resolutionR→I in Cstr(Aen), and consider the functor
˜D := HomA(−,I ). So D∼= ˜D as functors D(Aen)op→D(Aen). Because of the
contravariance of ˜D, the diagram of rings
Cent(A)
chmM,Aop
//
chm ˜D(M),A
))
EndCstr(Aen)(M)
˜D

EndCstr(Aen)
(˜D(M)
{op
is commutative. After applying the localization functorQ to the vertical arrow˜D
in the diagram above, we obtain the commutative diagram on the derived level.□
Lemma 18.2.19. Given M,N ∈D(Aen), consider the complex
L := RHomAen,out(A,M⊗N)∈D(Aen,in) = D(Aen).
Let a,a′,a′′∈Cent(A) be elements such that chmD
N,A(a) = chm D
N,Aop(a′) in
EndD(Aen)(N) and chmD
M,A(a′) = chm D
M,Aop(a′′) in EndD(Aen)(M). Then
chmD
L,A(a) = chmD
L,Aop(a′′) in EndD(Aen)(L).
Proof. The proof resembles that of Lemma 14.5.15. Consider the objectM⊗N∈
D(Afour). There are four ring homomorphisms
chmD
M⊗N,B : Cent(A)→EndD(Afour)(M⊗N),
corresponding to these four options for the ringB, in terms of formulas (18.2.3)
and (18.2.4):B :=Aout,A op,out,A in,A op,in. We know that
(18.2.20)
chmD
M⊗N,Ain(a) = chmD
M⊗N,Aop,out(a′)
chmD
M⊗N,Aout(a′) = chmD
M⊗N,Aop,in(a′′).
421
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Let M⊗N→J be a K-injective resolution inCstr(Afour), so
EndD(Afour)(M⊗N)∼= H0(
EndCstr(Afour)(J)
{
as rings. Formulas (18.2.20) imply that
(18.2.21)
chmJ,Ain(a)∼chmJ,Aop,out(a′),
chmJ,Aout(a′)∼chmJ,Aop,in(a′′),
where “∼” means the homotopy relation on degree0 cocycles in the DG ring
EndAfour(J).
Now let us write˜L = HomAen,out(A,J )∈C(Aen,in). The complex˜Lis K-injective
overAen,in, again by the ﬂatness of the ring homomorphism (18.2.6), and˜L∼=L in
D(Aen,in). Hence there is a ring isomorphism
(18.2.22) H0(
EndAen,in(˜L)
{∼= EndD(Aen,in)(L).
Now A is a central bimodule over its center. This implies that the two actions
of Cent(A) on ˜L that come from chmJ,Aout and chmJ,Aop,out are equal. The two
actions of Cent(A) on ˜L that come fromchmJ,Ain and chmJ,Aop,in are the actions
chm˜L,Ain and chm˜L,Aop,in respectively. From formulas (18.2.21) we conclude that
chm˜L,Ain(a)∼chm˜L,Aop,in(a′′). By formula (18.2.22) we see that chmD
L,Ain(a) =
chmD
L,Aop,in(a′′) as claimed. □
Theorem 18.2.23([165]). LetA be a noetherian ring, and letR be a NC dualizing
complex overA.
(1) The two ring homomorphisms
chmD
R,A, chmD
R,Aop : Cent(A)→EndD(Aen)(R)
are bijective.
(2) If R is a rigid NC dualizing complex, thenchmD
R,A = chmD
R,Aop.
Proof.
(1) Recall the duality functorDA from Deﬁnition 18.1.15, withB =A. By Corol-
lary 18.1.19 it gives rise to an equivalenceDA : Db
(f,..)(Aen)op→Db
(..,f)(Aen). By
Lemma 18.2.18, for everyM∈Db
(f,..)(Aen) we get a commutative diagram of rings
Cent(A)
chmD
M,Aop
//
chmD
DA(M),A
))
EndD(Aen)(M)
DA∼=

EndD(Aen)
(
DA(M)
{op
Note that the vertical arrow DA is an isomorphism. Taking M = R we have
DA(R)∼=A in D(Aen). As we saw in Example 18.2.17, the homomorphismchmD
A,A
is bijective. This proves thatchmD
R,Aop is bijective.
Likewise for chmD
R,A, but this time we use the duality functorDAop.
(2) Now there is a rigidifying isomorphism ρ: R
≃
− →SqA(R) in D(Aen). Let
f : Cent(A)→Cent(A) be the ring automorphismf := (chm D
R,Aop)−1◦chmD
R,A.
We need to prove thatf = id.
For this we shall use Lemma 18.2.19, withM = N := R, so L∼= SqA(R) in
D(Aen). Take an element a∈Cent(A), and let a′:= f(a) and a′′:= f(a′) in
Cent(A). The lemma says thatchmD
L,A(a) = chm D
L,Aop(a′′). But by the deﬁnition
of f and a′we havechmD
R,A(a) = chmD
R,Aop(a′). SinceR∼=L in D(Aen), and since
422
Derived Categories | Amnon Yekutieli | 14 Apr 2019
chmD
R,Aop is bijective, we conclude thata′=a′′. This means thatf(a) = f(f(a)),
so a =f(a). Finally, the elementa was arbitrary, and hencef = id. □
Lemma 18.2.24. Let (R,ρ) and (R′,ρ′) be rigid dualizing complexes, letφ:R→
R′be a morphism inD(Aen), and leta∈Cent(A). Then
SqA
(
φ◦chmD
R,A(a)
{
= SqA(φ)◦chmD
SqA(R),A(a2)
as morphisms SqA(R)→SqA(R′) in D(Aen).
Proof. Because SqA is a functor, there is equality
SqA
(
φ◦chmD
R,A(a)
{
= SqA(φ)◦SqA
(
chmD
R,A(a)
{
.
So we can assume thatR′=R and φ= idR. We need to prove that the equality
(18.2.25) SqA
(
chmD
R,A(a)
{
= chmD
SqA(R),A(a2)
holds for these endomorphisms ofSqA(R) in D(Aen).
From Deﬁnition 18.2.11, applied to the morphismchmD
R,A(a) :R→R in D(Aen),
we see that
(18.2.26) SqA
(
chmD
R,A(a)
{
= chmD
SqA(R),Aout(a)◦chmD
SqA(R),Ain(a)
as endomorphisms ofSqA(R) in D(Aen) = D(Aen,in). But becauseR is a rigid dual-
izing complex, Theorem 18.2.11(2) says thatchmD
R,A(a) = chmD
R,Aop(a). Therefore,
in formula (18.2.26) we can replace the action ofa through Aout with its action
through Aop,in. This gives
(18.2.27) SqA
(
chmD
R,A(a)
{
= chmD
SqA(R),Aop,in(a)◦chmD
SqA(R),Ain(a).
Next, using Lemma 18.2.19, withM =N :=R and a′=a′′:=a, we obtain
chmD
SqA(R),Aop,in(a) = chmD
SqA(R),Ain(a).
Plugging this into (18.2.27) we get
SqA
(
chmD
R,A(a)
{
= chmD
SqA(R),Ain(a)2.
Finally, sincechmD
SqA(R),Ain is a ring homomorphism, we end up with (18.2.25).□
In Deﬁnition 12.9.1 we introduced derived pseudo-ﬁnite DG modules over a DG
ring A. Recall that a DG moduleM ∈D(A) is called derived pseudo-ﬁnite if it
belongs to the saturated full triangulated subcategory ofD(A) generated by the
pseudo-ﬁnite semi-free DG modules. WhenA is a ring, the pseudo-ﬁnite semi-free
DGA-modules are precisely the bounded above complexes of ﬁnite freeA-modules.
Theorem 18.2.28 (Uniqueness, [153], [165]). Let A be a noetherian ring, and
assume A is a derived pseudo-ﬁnite complex overAen. Suppose (R,ρ) is a NC
rigid dualizing complex overA. Then (R,ρ) is unique, up to a unique NC rigid
isomorphism.
Proof. Suppose (R′,ρ′) is another NC rigid dualizing complex overA. According
to Theorem 18.1.25 and Corollary 18.1.27, there are tilting complexesT and T′
overA such that
(18.2.29) R′∼=T⊗L
AR∼=R⊗L
AT′
423
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in D(Aen). We have the following sequence of isomorphisms inD(Aen) :
(18.2.30)
T⊗L
AR∼=1 R′∼=2 RHomAen,out(A,R′⊗R′)
∼=1 RHomAen,out
(
A, (R⊗L
AT′)⊗(T⊗L
AR)
{
∼=3 RHomAen,out
(
A, (R⊗R)⊗L
Aen (T′⊗T )
{
∼=4 RHomAen,out(A,R⊗R)⊗L
Aen (T′⊗T )
∼=5 R⊗L
Aen (T′⊗T )∼=6 T⊗L
AR⊗L
AT′.
Here are the explanations for the various isomorphisms:
∼=1 : These are due to (18.2.29).
∼=2 : This is the rigidifying isomorphismρ′.
∼=3 : This isomorphism is by rearranging the tensor factors, and in it the inside
action ofAen on R⊗R is viewed as a right action, and this matches the
left outside action ofAen on T′⊗T. Cf. formulas (18.2.7) and (18.2.1).
∼=4 : It is an application of the tensor-evaluation isomorphism (see Theorem
12.9.10). This is where we needA to be a derived pseudo-ﬁnite complex
overAen – so that condition (i) of Theorem 12.9.10 will hold. Condition (ii)
that theorem holds since the complexR⊗R has bounded cohomology. As
for condition (iii) of the theorem: the complexT′⊗T is a tilting complex
over the ringAen, so it has ﬁnite ﬂat dimension, and thus it certainly has
derived bounded below tensor displacement.
∼=5 : This uses the rigidifying isomorphismρ.
∼=6 : It is a rearranging the tensor factors. Recall that the left action ofAen on
T′⊗T is the outside action, cf. formula(18.2.1).
LetT∨be the quasi-inverse ofT. After applyingT∨⊗L
A (−) to the isomorphisms
(18.2.30) we getR∼=R⊗L
AT′in D(Aen). Equation (18.2.29) tells us that there is
an isomorphismφ†:R
≃
− →R′in D(Aen).
The isomorphismφ†above need not be rigid. What we do know is that both
morphisms ρ′◦φ†, SqA(φ†)◦ρ: R→SqA(R′) are isomorphisms in D(Aen). By
Theorem 18.2.23 the automorphisms ofR in D(Aen) are all of the formchmD
R,A(a),
for elementsa∈Cent(A)×. Thus there is a unique invertible central elementa∈A
such that
(18.2.31) SqA(φ†)◦ρ=ρ′◦φ†◦chmD
R,A(a).
Deﬁne the isomorphism
φ:=φ†◦chmD
R,A(a−1) :R
≃
− →R′
in D(Aen). Then we have the following equalities:
SqA(φ)◦ρ= SqA
(
φ†◦chmD
R,A(a−1)
{
◦ρ
=(i) SqA(φ†)◦chmD
SqA(R),A(a−2)◦ρ
=(ii) SqA(φ†)◦ρ◦chmD
R,A(a−2)
=(iii) ρ′◦φ†◦chmD
R,A(a)◦chmD
R,A(a−2)
=(iv) ρ′◦φ†◦chmD
R,A(a−1) =ρ′◦φ.
The equality =(i) is due to Lemma 18.2.24. In the equality=(ii) we have used the
fact thatρis a Cent(A)-linear morphism for the action throughA, soρcommutes
with chmD
R,A(a−2). Equality =(iii) is from (18.2.31). And equality=(iv) is because
chmD
R,A is a ring homomorphism. We see thatφ:R
≃
− →R′is a rigid isomorphism.
The uniqueness of the elementa implies the uniqueness of the rigid isomorphismφ
(by the same sort of calculation). □
424
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Remark 18.2.32.As mentioned in Remark 18.1.30, for the purposes of Subsection
18.1, the only requirement on the base ringK is that the centralK-ring A is ﬂat
over it.
In this subsection that is not enough. Suppose thatA is ﬂat overK. In order to
prove the uniqueness of a rigid dualizing complexR∈Db(Aen), utilizing Theorem
12.9.10, we need that the complexR⊗L
K R∈D(Aen) will have bounded below
cohomology. The only way we know to guarantee this is if the base ringK is
regular. Notice that the regularity requirement is also needed in the commutative
theory (see Setup 13.5.1 and Remark 13.5.18).
Presumably the regularity of the base ringK is the only obstruction. The lack
of ﬂatness ofA can be handled using a suitable DG ring resolution ˜A→A, as
explained in Remark 18.1.30. Thus we predict that the deﬁnitions and results of
this subsection will remain valid ifK is a regular nonzero commutative base ring,
and A is a noetherian centralK-ring.
