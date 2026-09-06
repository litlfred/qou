---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-078-13-dualizing-complexes-over-commutative-rings
section_title: "Dualizing Complexes over Commutative Rings"
section_number: 13
pages: 253-265
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
In this section we ﬁnally explain what was outlined, as a motivating discussion,
in Subsection 0.2 of the Introduction. Dualizing complexes are perhaps the most
compelling reason to study derived categories. In the commutative ring setting of
the current section the technicalities are milder than in the geometric setting (see
Remark 13.5.18) and the noncommutative ring setting (that is treated in Sections
17 and 18).
In the ﬁrst and third subsections of this section we talk aboutdualizing complexes
and residue complexes, respectively, over commutative rings. This material is based
on the original treatment by A. Grothendieck in [62], but with a much more detailed
discussion. Sandwiched between them is a reminder on the classiﬁcation of injective
modules, due to E. Matlis.
The last two subsections are onrigid dualizing complexesin the sense of M. Van
den Bergh.
In this section all rings are commutativeK-rings by default (see Convention
1.2.4). However, the base ringK will remain implicit most of the time.
13.1. Dualizing Complexes. Let A be a commutative ring. The category ofA-
modules is M(A) = ModA. Because A is commutative, the Hom bifunctor has its
target in M(A) :
HomA(−,−) : M(A)op×M(A)→M(A).
Likewise for the right derived bifunctor:
RHomA(−,−) : D(A)op×D(A)→D(A).
See Proposition 12.10.11.
Let M∈C(A). The DGA-module EndA(M) = HomA(M,M ) is a noncommu-
tative DG centralA-ring; namely there is a central DG ring homomorphism
(13.1.1) hmM :A→HomA(M,M )
called homothety. When we forget the ring structure,hmM becomes a homomor-
phism in Cstr(A).
Deﬁnition 13.1.2.Given a complexM∈D(A), thederived homothety morphism
hmR
M :A→RHomA(M,M )
is the morphism inD(A) with this formula:hmR
M :=ηR
M,M◦Q(hmM).
In other words, the diagram
A
Q(hmM) //
hmR
M

HomA(M,M )
ηR
M,M // RHomA(M,M )
in D(A) is commutative. The letter “R” in the superscript of the expressionhmR
M
refers to “right derived functor”.
ThismaterialwillbepublishedbyCambridgeUniversityPressas Derived CategoriesbyAmnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works.c© Amnon Yekutieli, 2019.
253
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Exercise 13.1.3. Prove that ifρ: M →I is a K-injective resolution, then the
diagram
A
Q(hmI) //
hmR
M --
HomA(I,I )
ηR
I,I
∼=
// RHomA(I,I )
RHom(Q(ρ),Q(ρ)−1)∼=

RHomA(M,M )
in D(A) is commutative.
Exercise 13.1.4. Formulate and prove a version of the previous exercise with a
K-projective resolution ofM.
Deﬁnition 13.1.5.A complex M ∈D(A) is said to have the derived Morita
property if the derived homothety morphismhmR
M :A→RHomA(M,M ) in D(A)
is an isomorphism.
Proposition 13.1.6. The following conditions are equivalent for a complexM∈
D(A) :
(i) M has the derived Morita property.
(ii) The homothety ring homomorphismA→EndD(A)(M) is a bijective, and
HomD(A)
(
M,M [p]
{
= 0 for allp⁄= 0.
(iii) TheA-module H0(
RHomA(M,M )
{
is free of rank1, with basis the element
idM, and Hp(
RHomA(M,M )
{
= 0 for everyp⁄= 0.
Exercise 13.1.7. Prove Proposition 13.1.6. (Hint: see Corollary 12.2.8 and the
preceding material.)
Remark 13.1.8.In some texts (e.g. in [13]), a complexM with the derived Morita
property is called asemi-dualizing complex. This name is only partly justiﬁed, be-
cause this property occurs in the deﬁnition of a dualizing complex – see Deﬁnition
13.1.9 below. However, there is a whole other class of complexes with the derived
Morita property – these are thetilting complexes. Often these two classes of com-
plexes are disjoint. More on these notions, and their noncommutative variants, can
be found in Sections 14 and 18 of the book.
From here on the commutative ringA is assumed to be noetherian. Recall that
Df(A) is the full subcategory of D(A) on the complexes with ﬁnitely generated
cohomology modules. The subcategoryDf(A) is triangulated.
The next deﬁnition ﬁrst appeared in [62, Section V.2]. The injective dimension
of a complex was deﬁned in Deﬁnition 12.4.8.
Deﬁnition 13.1.9.Let A be a noetherian commutative ring. A complex ofA-
modules R is called adualizing complexif it has the following three properties:
(i) R∈Db
f (A).
(ii) R has ﬁnite injective dimension.
(iii) R has the derived Morita property.
Recall that in the traditional literature (e.g. [105]), a noetherian ringA is called
regular if all its local ringsAp are regular local rings. TheKrull dimension of A
is the dimension of the schemeSpec(A); namely the supremum of the lengths of
strictly ascending chains of prime ideals inA. In practice we never see regular rings
that are not ﬁnite dimensional (there are only pretty exotic examples of them).
The following deﬁnition will simplify matters for us:
Deﬁnition 13.1.10.We shall say that a noetherian commutative ringA is regular
if it has ﬁnite Krull dimension, and all its local ringsAp are regular local rings, in
the sense of [105].
254
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Every ﬁeldK, and the ring of integersZ, are regular rings. IfA is regular, then
so is the polynomial ringA[t1,...,tn] inn< ∞variables, and also the localization
of A at every multiplicatively closed set. See [105, Chapter 7].
As proved by Serre (see [105, Theorem 19.2]) a regular ringA has ﬁnite global
cohomological dimension. This means that there is a numberd∈N such that for
all modulesM,N ∈M(A) and allq > d, the modules Extq
A(M,N ) vanish. This
implies that everyA-module M has injective, projective and ﬂat dimensions≤d.
It follows that every complexM∈Db(A) has ﬁnite injective, projective and ﬂat
dimensions (see Deﬁnitions 12.4.8 and 12.4.18).
Example 13.1.11.LetA be a regular ring. TakingR :=A we see thatR satisﬁes
condition (ii) of Deﬁnition 13.1.9. The other two conditions hold regardless of the
regularity ofA. Thus the complexR =A is a dualizing complex over the ringA.
In Subsection 0.2 of the Introduction we used this fact for the ringA =Z.
Deﬁnition 13.1.12.Given a dualizing complexR∈D(A), the duality functor
associated to it is the triangulated functor
D : D(A)op→D(A), D := RHomA(−,R ).
The notation “D” deliberately keeps the dualizing complexR implicit. Note
that upon applying the functorD to the objectA∈D(A) we getD(A) =R.
Let us choose a K-injective resolutionρ: R→I. There is an isomorphism of
triangulated functors
(13.1.13) presI :D
≃
− →HomA(−,I )
from D(A)op to D(A), that we call a presentation ofD. For everyM∈D(A) the
diagram
(13.1.14) D(M) id //
∼=presI,M

RHomA(M,R )
RHom(idM,Q(ρ))∼=

HomA(M,I )
ηR
M,I
∼=
// RHomA(M,I )
is commutative. (Note that we can chooseI to be a bounded complex of injectives,
by Proposition 12.4.13.)
Let M,I ∈C(A). There is a homomorphism
(13.1.15) evM,I :M→HomA
(
HomA(M,I ),I
{
in Cstr(A), calledHom-evaluation, with formula
evM,N (m)(φ) := (−1)p·q·φ(m)
for m∈Mp and φ∈HomA(M,I )q.
Lemma 13.1.16. Let R be a dualizing complex overA, with associated duality
functor D.
(1) The functorD◦D : D(A)→D(A) is triangulated.
(2) There is a unique morphismevR,R : Id→D◦D of triangulated functors
from D(A) to itself, calledderived Hom-evaluation, such that for every K-
injective resolutionρ:R→I, and every complexM∈D(A), the diagram
M
evR,R
M //
Q(evM,I) ((
D(D(M))
∼=

HomA
(
HomA(M,I ),I
{
255
Derived Categories | Amnon Yekutieli | 14 Apr 2019
is commutative. Here the vertical isomorphism is a double application of
the presentation presI.
(3) ForM =A there is equalityevR,R
A = hmR
R of morphismsA→(D◦D)(A)
in D(A).
Proof. (1) Choose a K-injective resolution ρ: R →I. Let’s write F :=
HomA
(
HomA(−,I ),I
{
. The functor F can be seen as a DG functor fromC(A)
to itself, that is then made into a functor fromD(A) to itself. So by Theorem
5.5.1(1), F is a triangulated functor (i.e. there is a translation isomorphismτF
etc.). Using the presentation (13.1.13) twice we get an isomorphismD◦D∼=F of
functors from D(A) to itself. This makesD◦D triangulated.
(2) With the K-injective resolutionρ: R→I above, we deﬁne the morphismev
so as to make the diagram commutative. According to Theorem 5.5.1(2),ev is a
morphism of triangulated functors. Because the resolutionρ:R→I is unique up
to homotopy, we get the same morphismev regardless of choice of resolution.
(3) This is clear from Exercise 13.1.3. □
Exercise 13.1.17. Suppose that A is a regular ring, and we take the dualizing
complex R := A. Let P be a bounded complex of ﬁnitely generated projective
A-modules. Show that:
(1) There is a canonical isomorphismD(P )∼= HomA(P,A ) in D(A).
(2) There is a canonical isomorphism
(D◦D)(P )∼= HomA
(
HomA(P,A ),A
{
in D(A).
(3) Under the isomorphism in item (2), the morphismevR,R
P goes to Q(evP,A).
(4) The homomorphism evP is a quasi-isomorphism.
Here is the ﬁrst important result regarding dualizing complexes.
Theorem 13.1.18. Suppose R is a dualizing complex over the noetherian com-
mutative ringA, with associated duality functorD. Then for every complexM∈
Df(A) the following hold:
(1) The complexD(M) belongs to Df(A).
(2) The morphism
evR,R
M :M→D(D(M))
in D(A) is an isomorphism.
Proof. (1) Condition (ii) of Deﬁnition 13.1.9 says that the functorD has ﬁnite
cohomological dimension. Condition (i) says thatD(A)∈Df(A). The assertion
follows from Theorem 12.5.7, withN0 := Mf(A).
(2) The compositionD◦D is a triangulated functor with ﬁnite cohomological di-
mension (at most twice the injective dimension ofR). The cohomological dimension
of the identity functorId is 0 (if A⁄= 0). By condition (iii) of Deﬁnition 13.1.9 we
know that evA is an isomorphism. Now we can use Theorem 12.5.2. □
Corollary 13.1.19.Under the assumptions of Theorem13.1.18, let⋆be one of the
boundedness conditionsb, +,−or⟨empty⟩, and let−⋆be the reversed boundedness
condition. Then the functor
D : D⋆
f (A)op→D−⋆
f (A)
is an equivalence of triangulated categories.
Proof. The previous theorem tells us thatD is its own quasi-inverse. The claim
about the boundedness holds becauseD has ﬁnite cohomological dimension. □
256
Derived Categories | Amnon Yekutieli | 14 Apr 2019
We saw that dualizing complexes exist over regular rings. This fact is used for the
very general existence result Theorem 13.1.34. But ﬁrst we need some preparation.
Here are some adjunction properties related to homomorphisms between com-
mutative rings. These are enhancements of the material from Subsection 12.10.
Recall that a ring homomorphismu : A→B gives rise to a forgetful functor
Restu : D(B)→D(A). This functor is going to be implicit in the discussion below.
Lemma 13.1.20. LetA→B be a ring homomorphism.
(1) If I∈C(A) is K-injective, thenJ := HomA(B,I )∈C(B) is K-injective.
(2) GivenM∈D(A), let us deﬁneN := RHomA(B,M )∈D(B). Then there is
an isomorphism RHomB(−,N )∼= RHomA(−,M ) of triangulated functors
D(B)op→D(B).
Proof. (1) This is an adjunction calculation. SupposeL∈C(B) is acyclic. There
are isomorphisms
(13.1.21) HomB(L,J )∼= HomB
(
L, HomA(B,I )
{∼= HomA(L,I )
in C(B). SinceI is K-injective overA, the complexHomA(L,I ) is acyclic.
(2) Choose a K-injective resolutionM→I in C(A). Let J := HomA(B,I ). Then
N→J is a K-injective resolution inC(B). There are isomorphisms of triangulated
functors
(13.1.22) RHomA(−,M )∼= HomA(−,I )
and
(13.1.23) RHomB(−,N )∼= HomB(−,J ),
where the functors (13.1.22) are contravariant functors fromD(A) to itself, and
the functors (13.1.23) are contravariant functors fromD(B) to itself. But given
L∈C(B) we can viewHomA(L,I ) as a complex ofB-modules, and in this way the
functors (13.1.22) become contravariant triangulated functors fromD(B) to itself.
Formula (13.1.21) shows that the functors (13.1.22) and (13.1.23) are isomorphic.
□
Lemma 13.1.24. LetA→B be a ﬂat ring homomorphism, letM∈D−
f (A), and
let N∈D+(A). Then there is an isomorphism
RHomA(M,N )⊗AB∼= RHomB(B⊗AM,B⊗AN)
in D(B). This isomorphism is functorial inM and N.
Proof. Theorem 12.10.14 tells us that
RHomA(M,N )⊗AB∼= RHomA(M,B⊗AN)
in D(B). Then, by forward adjunction (Theorem 12.6.6) we get
RHomA(M,B⊗AN)∼= RHomB(B⊗AM,B⊗AN).
The functoriality is clear. □
Lemma 13.1.25. LetI be anA-module. The following conditions are equivalent:
(i) I is injective.
(ii) For every ﬁnitely generatedA-moduleM the module Ext1
A(M,I ) is zero.
Exercise 13.1.26. Prove Lemma 13.1.25. (Hint: use the Baer criterion, Theorem
2.7.10.)
Lemma 13.1.27. The injective dimension of a complex N ∈D(A) equals the
cohomological dimension of the functor
RHomA(−,N )|Mf(A)op : Mf(A)op→D(A).
257
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. Bydeﬁnitiontheinjectivedimensionof N, sayd, isthecohomologicaldimen-
sion of the functorRHomA(−,N ) : D(A)op→D(A). Let d′be the cohomological
dimension of the functorRHomA(−,N )|Mf(A)op. Obviously the inequalityd≥d′
holds. For the reverse inequality we may assume thatH(N) is nonzero andd′<∞.
This implies that there are integersq1 = q0 +d′such that for everyM∈Mf(A)
there is an inclusion
con
(
H
(
RHomA(M,N )
{{
⊆[q0,q 1].
In particular, forM =A, we getcon(H(N))⊆[q0,q 1]. LetN→J be an injective
resolution in C(A) with inf(J)≥q0. Take I := smt≤q1(J), the smart truncation
from Deﬁnition 7.3.6. The proof of Proposition 12.4.13, plus Lemma 13.1.25, show
that N→I is an injective resolution. But thenRHomA(−,N )∼= HomA(−,I ), so
this functor has cohomological displacement in the interval[q0,q 1], that has length
d′. □
Recall that a ring homomorphismA→B is called ﬁniteif it makesB into a
ﬁnitely generatedA-module.
Proposition 13.1.28. LetA→B be a ﬁnite ring homomorphism, and letRA be
a dualizing complex overA. Then the complex
RB := RHomA(B,RA)∈D(B)
is a dualizing complex overB.
Proof. Consider the duality functors DA := RHom A(−,RA) and DB :=
RHomB(−,RB). As explained in the proof of Lemma 13.1.20(2), they are isomor-
phic as contravariant triangulated functors fromD(B) to itself. SinceRB =DA(B)
and B ∈Db
f (A), by Corollary 13.1.19 we have RB ∈Db
f (A). But then also
RB ∈Db
f (B). Next, because DB(L) ∼= DA(L) for all L ∈D(B), this implies
that the cohomological dimension ofDB is at most that ofDA, which is ﬁnite.
We see that the injective dimension of the complexRB is ﬁnite. Lastly, there is
an isomorphismDB◦DB∼=DA◦DA as functors fromDb
f (B) to itself, and hence
evR,R : Id→DB◦DB is an isomorphism. Applying this to the objectB∈Db
f (B)
we see thathmR
RB = evR,R
B : B→(DB◦DB)(B) is an isomorphism. SoRB has
the derived Morita property. The conclusion is thatRB is a dualizing complex over
B. □
Recall that a ring homomorphismA→B is called alocalizationif B is isomor-
phic, as anA-ring, to the localizationAS ofA with respect to some multiplicatively
closed subsetS.
Proposition 13.1.29. Let A→B be a localization ring homomorphism, and let
RA be a dualizing complex overA. Then the complex
RB :=B⊗ARA∈D(B)
is a dualizing complex overB.
Proof. It is clear thatRB∈Db
f (B). By Lemma 13.1.27, to compute the injective
dimension ofRB it is enough to look atRHomB(M,RB) for M∈Mf(B). We can
ﬁnd a ﬁnitely generatedA-submodule M′⊆M such thatB·M′= M; and then
M∼=B⊗AM′. Lemma 13.1.24 tells us that
RHomB(M,RB)∼= RHomA(M′,RA)⊗AB.
We conclude that the injective dimension ofRB is at most that ofRA, which is
ﬁnite. Lastly, by the same lemma we get an isomorphism
RHomB(RB,RB)∼= RHomA(RA,RA)⊗AB,
258
Derived Categories | Amnon Yekutieli | 14 Apr 2019
and it is compatible with the morphisms fromB. ThusRB has the derived Morita
property. □
Recall that a ring homomorphismA→B is called ﬁnite typeif B is ﬁnitely
generated as anA ring (i.e.B is a quotient of the polynomial ringA[t1,...,tn] for
some n< ∞).
Deﬁnition 13.1.30.A ring homomorphismu :A→B is calledessentially ﬁnite
type (EFT) if it can be factored intou =uloc◦uft, whereuft :A→Bft is a ﬁnite
type ring homomorphism, anduloc :Bft→B is a localization homomorphism.
This is illustrated in the following commutative diagram.
A ﬁnite type
uft //
u

Bft localization
uloc //B
Proposition 13.1.31. Letu :A→B be an EFT ring homomorphism.
(1) Let v :B→C be another EFT ring homomorphism. Thenv◦u :A→C
is an EFT ring homomorphism.
(2) LetA→A′be a ring homomorphism, and deﬁneB′:=A′⊗AB. Then the
induced ring homomorphismu′:A′→B′is EFT.
(3) If the ringA is noetherian, thenB is also noetherian.
Exercise 13.1.32. Prove Proposition 13.1.31.
Example 13.1.33. LetK be a noetherian ring, letX be a ﬁnite typeK-scheme,
and letx∈X be a point. Then the local ringOX,x is an EFTK-ring.
Theorem 13.1.34. LetK be a regular noetherian commutative ring, and letA be
an essentially ﬁnite type commutativeK-ring. ThenA has a dualizing complex.
See Deﬁnition 13.1.10 regarding regular rings.
Proof. The ring homomorphismK→A can be factored asK→Apl→Aft→
A, where Apl = K[t1,...,tn] is a polynomial ring, Apl →Aft is surjective, and
Aft→A is a localization. (The subscripts stand for “polynomial” and “ﬁnite type”
respectively.) According to [105, Theorem 19.5] the ringApl is regular; so, as shown
in Example 13.1.11, the complexRpl :=Apl is a dualizing complex overApl.
DeﬁneRft := RHomApl(Aft,R pl)∈D(Aft). By Proposition 13.1.28 this is a
dualizing complex overAft. Finally deﬁneR :=A⊗AftRft∈Db
f (A). By Proposition
13.1.29 this is dualizing complex overA. □
The proof of Theorem 13.1.34 might give the impression thatA could have a lot
of nonisomorphic dualizing complexes. This is not quite true, as the next theorem
demonstrates.
Theorem 13.1.35. LetA be a noetherian commutative ring with connected spec-
trum, and let R and R′be dualizing complexes overA. Then there is a rank 1
projectiveA-moduleL and an integerd, such thatR′∼=R⊗AL[d] in D(A).
We need some lemmas before proving the theorem.
Lemma 13.1.36 (Künneth Trick). Let M,M′∈D−(A), and leti,i′∈Z be such
that sup(H(M))≤i and sup(H(M′))≤i′. Then
Hi+i′
(M⊗L
AM′)∼= Hi(M)⊗A Hi′
(M′)
as A-modules.
Exercise 13.1.37. Prove Lemma 13.1.36.
259
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Lemma 13.1.38 (Projective Truncation Trick). Let M ∈D−(A), with i1 :=
sup(H(M))∈Z. Assume the A-module P := Hi1(M) is projective. Then there
is an isomorphismM∼= smt≤i1−1(M)⊕P [−i1] in D(A).
Exercise 13.1.39. Prove Lemma 13.1.38. (Hint: ﬁrst replaceM with its trunca-
tion smt≤i1(M). Then prove thatP is a direct summand ofMi1.)
By a principal open setin the aﬃne scheme inSpec(A) we mean a set of the
form Spec(As), whereAs is the localization ofA at an elements∈A. Thus
Spec(As) ={p∈Spec(A)|s /∈p}.
Lemma 13.1.40. LetM,M′∈Mf(A), and letp⊆A be a prime ideal.
(1) If Mp⁄= 0 and M′
p⁄= 0 then Mp⊗ApM′
p⁄= 0.
(2) If Mp⊗ApM′
p∼=Ap then Mp∼=M′
p∼=Ap.
(3) If Mp∼= Ap, then there is a principal open neighborhoodSpec(As) of p in
Spec(A) such thatMs∼=As as As-modules.
Exercise 13.1.41. Prove Lemma 13.1.40. (Hint: use the Nakayama Lemma.)
Here is a pretty diﬃcult technical lemma.
Lemma 13.1.42. In the situation of the theorem, let M,M′∈D−
f (A) satisfy
M⊗L
A M′∼= A in D(A). Then M ∼= L[d] in D(A) for some rank 1 projective
A-moduleL and an integerd.
Proof. For each primep⊆A let Mp :=Ap⊗AM, and deﬁneep := sup(H(Mp)) in
Z∪{−∞}. Deﬁne the generalized integere′
p similarly.
Fix one prime p. The associativity and symmetry of the left derived tensor
product imply the existence of these isomorphisms
(13.1.43)
Mp⊗L
ApM′
p = (Ap⊗L
AM)⊗L
Ap (Ap⊗L
AM′)
∼=Ap⊗L
A (M⊗L
AM′)∼=Ap⊗L
AA∼=Ap
in D(Ap). SinceAp⁄= 0, it follows thatH(Mp)⁄= 0 and H(M′
p)⁄= 0. Soep,e′
p∈Z,
and Hep(Mp), He′
p(M′
p) are nonzero ﬁnitely generatedAp-modules. By Lemma
13.1.40(1) we know that
Hep(Mp)⊗Ap He′
p(M′
p)⁄= 0.
According to Lemma 13.1.36 we have
Hep(Mp)⊗Ap He′
p(M′
p)∼= H(ep+e′
p)(Mp⊗L
ApM′
p)∼= H(ep+e′
p)(Ap).
But Ap is concentrated in degree0; this forcesep +e′
p = 0 and
Hep(Mp)⊗Ap He′
p(M′
p)∼=Ap
in D(Ap). By Lemma 13.1.40(2) we now see that Hep(Mp)∼= He′
p(M′
p)∼= Ap.
According to Lemma 13.1.38 there are isomorphisms
(13.1.44) Mp∼=Ap[−ep]⊕smt≤ep−1(Mp)
and
M′
p∼=Ap[−e′
p]⊕smt≤e′
p−1(M′
p)
in D(Ap). These, with (13.1.43), give an isomorphism
(13.1.45)
(
Ap[−ep]⊕smt≤ep−1(Mp)
{
⊗L
Ap
(
Ap[−e′
p]⊕smt≤e′
p−1(M′
p)
{∼=Ap.
Theleftsideof(13.1.45)isthedirectsumoffourobjects. Passingtothecohomology
of (13.1.45) we see thatN := H
(
smt≤ep−1(Mp)[−e′
p]
{
is a direct summand ofAp.
260
Derived Categories | Amnon Yekutieli | 14 Apr 2019
But, sincee′
p +ep = 0, the graded moduleN is concentrated in the degree interval
[∞,−1]. It follows thatN = 0. Therefore, by (13.1.44), we deduce that
(13.1.46) Mp∼=Ap[−ep].
The calculation above works for every primep. From (13.1.46) we get
(13.1.47) Ap⊗A Hi(M)∼= Hi(Mp)∼=
{
Ap if i =ep,
0 otherwise.
We now use Lemma 13.1.40(3) to deduce that for every primep there is an open
neighborhood Up of p in Spec(A) such that Hep(Mq)∼= Aq for all q∈Up. This
implies, by equation (13.1.47), thateq =ep. Therefore p↦→ep is a locally constant
function Spec(A)→Z. We assumed that Spec(A) is connected, and this implies
that this is a constant function, sayep =−d for some integerd.
DeﬁneL := H−d(M)∈Mf(A). Using truncation we see thatM∼=L[d] in D(A).
We know thatLp∼= Ap for all primes p. Finally, Lemma 13.1.24 says that the
A-module L is projective. □
Remark 13.1.48. Lemma 13.1.42 is actually true in much greater generality: the
ring A does not have to be noetherian, and we do not have to assume that the
complexes M and M′have bounded above or ﬁnite cohomology. The proof is
harder (see the proof of Theorem 14.5.17).
Proof of Theorem13.1.35. Deﬁne the duality functorsD := RHom A(−,R ) and
D′:= RHomA(−,R′); these are ﬁnite dimensional contravariant triangulated func-
tors from Df(A) to itself. And deﬁneF :=D′◦D andF′:=D◦D′, that are ﬁnite
dimensional (covariant) triangulated functors fromDf(A) to itself. Let
(13.1.49) M :=F (A) =D′(D(A)) = RHomA(R,R′)
and
M′:=F′(A) =D(D′(A)) = RHomA(R′,R ).
These are objects ofDb
f (A).
For every objectN∈D(A) there is a morphism
ψN :N⊗L
A RHomA(R,R′)→RHomA
(
RHomA(N,R ),R′{
deﬁned as follows: we choose a K-projective resolutionP→N and a K-injective
resolution R′→I′. Then ψN is represented by the obvious homomorphism of
complexes
P⊗A HomA(R,I′)→HomA
(
HomA(P,R ),I′{
.
As N changes, ψN is a morphism of triangulated functorsψ: (−)⊗L
AM→D′◦
D = F. For N = A the morphismψA is an isomorphism, by equation (13.1.49).
The functorF has ﬁnite cohomological dimension, and the functor(−)⊗L
AM has
bounded above cohomological displacement. According to Theorem 12.5.2, the
morphism ψN is an isomorphism for everyN∈D−
f (A). In particular this is true
for N :=M′. So, using Theorem 13.1.18, we obtain
M′⊗L
AM∼= (D′◦D)(M′)∼= (D′◦D◦D◦D′)(A)∼=A.
According to Lemma 13.1.42 there is an isomorphismM∼=L[d]. Finally, using the
isomorphism ψR, we get
R⊗AL[d]∼=F (R) =D′(D(R))∼=D′(A) =R′. □
What if Spec(A) has more than one connected component?
Deﬁnition 13.1.50.Let A be a ring.
261
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(1) We say thatA has aﬁnite connected component decompositionif
Spec(A) =
m∐
i=1
Spec(Ai),
a ﬁnite disjoint union of nonempty connected closed subschemes.
(2) IfAhasaﬁniteconnectedcomponentdecompositionasabove, thenthe con-
nected component decompositionofAis the ring isomorphismA∼=∏m
i=1 Ai.
Of course, ifA has a ﬁnite connected component decomposition, then this de-
composition is unique, up to renumbering.
Proposition 13.1.51.IfA is noetherian, then it has a ﬁnite connected component
decomposition.
Exercise 13.1.52.
(1) Prove the proposition above.
(2) Find a ringA that does not have a ﬁnite connected component decompo-
sition.
Corollary 13.1.53. Let R and R′be dualizing complexes overA, and let A =∏m
i=1Ai be the connected component decomposition ofA. Then there is an isomor-
phism
R′∼=R⊗A
(
L1[d1]⊕···⊕Lm[dm]
{
in D(A), where eachLi is a rank1 projectiveAi-module, and eachdi is an integer.
Furthermore, the modulesLi are unique up to isomorphism, and the integersdi are
unique.
Exercise 13.1.54. Prove Corollary 13.1.53.
Remark 13.1.55. A rank 1 projective A-module L is also called an invertible
A-module. This is becauseL is invertible for the tensor product. Recall that the
group of isomorphism classes of invertibleA-modules is the commutative Picard
group PicA(A).
The commutative derived Picard groupDPicA(A) is the abelian groupPicA(A)×
Zm that classiﬁes dualizing complexes overA, as in Corollary 13.1.53.
Now assume thatA is noncommutative, and ﬂat central over a commutative ring
K. There are noncommutative versions of dualizing complexes and of “invertible”
complexes, that are calledtilting complexes. The latter form the nonabelian group
DPicK(A), and it classiﬁes noncommutative dualizing complexes. See [126], [127],
[79], [165] and [132]. We shall study this material in Sections 14 and 18 of the book.
Remark 13.1.56. The lack of uniqueness of dualizing complexes has always been
a source of diﬃculty. A certain uniqueness or functoriality is needed, already for
proving existence of dualizing complexes on schemes.
In [62] Grothendieck utilized local and global duality in order to formulate a
suitable uniqueness of dualizing complexes. This approach was very cumbersome
(even without providing details!).
Since then there have been a few approaches in the literature to attack this
diﬃculty. Generally speaking, these approaches came in two ﬂavors:
•Representability. This started with P. Deligne’s Appendix to [62], and
continued most notably in the work of A. Neeman, J. Lipman and their
coauthors. See [114], [98] and their references.
•Explicit Constructions. Mostly in the early work of Lipman et al., including
[97] and [96], and in the work of A. Yekutieli [162], and [164] and [168].
In Subsection 13.5 of the book we will presentrigid residue complexes, for which
there is a built-in uniqueness, and even functoriality (see Remark 13.5.17).
262
Derived Categories | Amnon Yekutieli | 14 Apr 2019
13.2. Interlude: The Matlis Classiﬁcation of Injective Modules.We start
with a few facts about injective modules over rings that are neither commutative
nor noetherian. Sources for this material are [129] and [93].
Deﬁnition 13.2.1.
(1) Let M be anA-module. A submodule N⊆M is called anessential sub-
module if for every nonzero submoduleL⊆M, the intersectionN∩L is
nonzero. In this case we also say thatM is anessential extensionof N.
(2) An essential monomorphismis a monomorphismφ:N↣M whose image
is an essential submodule ofM.
(3) Let M be anA-module. An injective hull (or injective envelope) ofM is
an injective moduleI, together with an essential monomorphismM↣I.
Proposition 13.2.2. Every A-moduleM admits an injective hull.
Proof. See [129, Theorem 3.30] or [93, Section 3.D]. □
There is a weak uniqueness result for injective hulls.
Proposition 13.2.3. Let M be anA-module, and supposeφ: M ↣ I and φ′:
M↣I′are monomorphisms into injective modules.
(1) If φis essential, then there is a monomorphism ψ: I ↣ I′such that
ψ◦φ=φ′.
(2) If φ′is also essential, thenψabove is an isomorphism.
Exercise 13.2.4. Prove Proposition 13.2.3.
In classical homological algebra we talk about the minimal injective resolution
of a moduleM. Let us recall it. We start by taking the injective hullφ:M↣I0.
This gives an exact sequence
0→M
φ
− →I0→M1→0,
where M1 is the cokernel ofφ. Then we take the injective hullM1↣I1, and this
gives a longer exact sequence
0→M→I0→I1→M2→0,
and so on. We want to generalize this idea to complexes.
Deﬁnition 13.2.5.
(1) A minimal complex of injectiveA-modules is a bounded below complex of
injective modulesI, such that for every integerq the submodule of cocycles
Zq(I)⊆Iq is essential.
(2) Let M ∈D+(A). A minimal injective resolution of M is a quasi-iso-
morphism M→I into a minimal complex of injectivesI.
Proposition 13.2.6. LetM∈D+(A).
(1) There exists a minimal injective resolutionφ:M→I.
(2) If φ′: M →I′is another minimal injective resolution, then there is an
isomorphism ψ:I→I′in Cstr(A) such thatφ′=ψ◦φ.
(3) IfM has ﬁnite injective dimension, then it has a bounded minimal injective
resolutionI.
Proof. (1) We know that there is a quasi-isomorphismM→J whereJ is a bounded
below complex of injective modules. For every q let Eq be an injective hull of
Zq(J). By Proposition 13.2.3(1) we can assume thatEq sits inside Jq like this:
Zq(J)⊆Eq⊆Jq. Since Eq is injective, we can decomposeJq into a direct sum:
Jq∼= Eq⊕Kq. The homomorphism dq
J : Kq→Jq+1 is a monomorphism since
263
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Kq∩Zq(J) = 0. And the image dq
J(Kq) is contained inEq+1. Thus dq
J(Kq) is a
direct summand ofEq+1, and this shows that the quotient
Iq+1 :=Eq+1/dq
J(Kq)∼=Jq+1/(Kq+1⊕dq
J(Kq))
is an injective module. The canonical surjection of graded modulesπ:J→I is a
homomorphism of complexes, with kernel the acyclic complex
⨁
q∈Z
(
Kq[−q]
dq
J
− − →dq
J(Kq)[−q−1]
{
.
Therefore πis a quasi-isomorphism. A short calculation shows thatI is a minimal
complex of injectives, i.e.Zq(I)⊆Iq is essential.
(2) See next exercise. (We will not need this fact.)
(3) According to Proposition 12.4.13, the complexJ that appears in item (1) can
be chosen to be bounded. □
Exercise 13.2.7. Prove Proposition 13.2.6(2).
Remark 13.2.8.Important: the isomorphismsψin Propositions 13.2.3 and 13.2.6
are not unique (see next exercise). We will see below (in Subsection 13.5) that a
rigid residue complex is a minimal complex of injectives that has no nontrivial rigid
automorphisms.
Exercise 13.2.9. Take A := K[[t]], the power series ring over a ﬁeldK. Let
M :=A/(t), the trivial module (the residue ﬁeld viewed as anA-module).
(1) Find a minimal injective resolutionM→I.
(2) Find a nontrivial automorphism of the complexI in Cstr(A) that ﬁxes the
submodule M⊆I0.
Now we add the noetherian condition.
Proposition 13.2.10. Assume A is a left noetherian ring. Let{Iz}z∈Z be a col-
lection of injectiveA-modules. ThenI :=⨁
z∈ZIz is an injectiveA-module.
Exercise 13.2.11. Prove Proposition 13.2.10. (Hint: use the Baer criterion.)
From here on in this subsection all rings are noetherian commutative. For them
much more can be said.
Recall that a moduleM is called indecomposableif it is not the direct sum of
two nonzero modules.
Deﬁnition 13.2.12.Let a⊆A be an ideal.
(1) Let M be anA-module. The a-torsion submoduleof M is the submodule
Γ a(M) consisting of the elements that are annihilated by powers ofa. Thus
Γ a(M) = lim
i→
HomA(A/ai,M )⊆M.
(2) If Γ a(M) =M then M is called ana-torsion module.
(3) The functor Γ a : M(A)→M(A) is called thea-torsion functor.
Here are some important properties of the torsion functor.
Proposition 13.2.13. Let a be an ideal inA.
(1) The functor Γ a is left exact.
(2) The functor Γ a commutes with inﬁnite direct sums.
Exercise 13.2.14. Prove the proposition above.
264
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Perhaps the most important theorem about injective modules over noetherian
commutative rings is the following structural result due to E. Matlis [104] from
1958. See also [148, Section V.4], [93, Sections 3.F and 3.I], [105, Section 18] and
[30].
For a prime idealp⊆A we writek(p) :=Ap/pp, the residue ﬁeld ofp.
Theorem 13.2.15(Matlis). LetA be a noetherian commutative ring.
(1) Let p⊆A be a prime ideal, and letJ(p) be the injective hull of theAp-
modulek(p). Then, as anA-module,J(p) is injective, indecomposable and
p-torsion.
(2) Suppose I is an indecomposable injectiveA-module. Then I∼= J(p) for a
unique prime idealp⊆A.
(3) Every injectiveA module I is a direct sum of indecomposable injectiveA-
modules.
Theorem 13.2.15 tells us that every injectiveA-module I can be written as a
direct sum
(13.2.16) I∼=
⨁
p∈Spec(A)
J(p)⊕µp
foracollectionofcardinalnumbers {µp}p∈Spec(A), calledtheBass numbers. General
counting tricks can show that the multiplicityµp is an invariant ofI. But we can
be more precise:
Proposition 13.2.17. Let I be an injectiveA-module, with direct sum decompo-
sition (13.2.16). Then for everyp there is equality
µp = rankk(p)
(
HomAp
(
k(p),A p⊗AI
{{
.
Proof. Consider another primeq. If q⊈ p then there is an elementa∈q−p, and
then a is both invertible and locally nilpotent onAp⊗AJ(q). This implies that
Ap⊗AJ(q) = 0. On the other hand, ifq⊆p, thenAp⊗AJ(q)∼=J(q). Therefore
Ap⊗AI∼=⨁
q⊆pJ(p)⊕µp.
Next, if q⊊ p, then there is an elementb∈p−q, and it is both invertible and
zero on the moduleHomAp
(
k(p),J (q)
{
. The implication is that this module is zero.
Finally, ifq = p then we have
HomAp
(
k(p),J (p)
{∼= HomAp
(
k(p),k(p)
{∼=k(p),
because the inclusionk(p)⊆J(p) is essential.
Sincek(p) is a ﬁnitely generatedAp-module, the functorHomAp(k(p),−) com-
mutes with inﬁnite direct sums. Therefore, putting all these cases together, we see
that
HomAp
(
k(p),A p⊗AI
{{∼=k(p)⊕µp
ask(p)-modules. □
