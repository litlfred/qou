---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-11
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI — Let X be a smooth algebraic variety over a ﬁeldK containing the real numbers."
---
1. Background on Crossed Groupoids and Stacks 11
2. Deformations of Sheaves of Rings 15
3. DG Lie Algebras and Deformations of Aﬃne Varieties 19
4. Twisted Objects in a Stack of Crossed Groupoids 21
5. Combinatorial Descent Data 25
6. Geometric Descent Data and Decomposition 28
7. Total Trivialization of Twisted Deformations 33
8. Lie Descent Data 36
9. From Lie Descent to Geometric Descent 39
10. Cosimplicial Formality 42
11. Twisted Quantization 45
References 48
0. Introduction
0.1. Deformation Quantization. Let K be a ﬁeld of characteristic0, and letX
be a smooth algebraic variety overK, with structure sheafOX. Suppose R is a
parameter algebraover K; namely R is a complete local noetherian commutative
K-algebra, with maximal idealm and residue ﬁeldR/m = K. The main example
is R = K[[ℏ]], the formal power series ring in the variableℏ. An associative R-
deformation ofOX is a sheafA of ﬂatm-adically complete associativeR-algebras
onX, withanisomorphism ψ: K⊗RA
≃
− →OX, calledanaugmentation. Similarly, a
Date: 5 September 2014.
Key words and phrases.Deformation quantization, algebraic varieties, stacks, gerbes, DG Lie
algebras.
Mathematics Subject Classiﬁcation2000. Primary: 53D55; Secondary: 14B10, 16S80, 17B40,
18D05.
This research was supported by the US-Israel Binational Science Foundation and by the Israel
Science Foundation.
1
arXiv:0905.0488v5  [math.AG]  5 Sep 2014
2 AMNON YEKUTIELI
PoissonR-deformation ofOX is a sheafA of ﬂatm-adically complete commutative
PoissonR-algebras onX, with an augmentation toOX.
Such deformations could be sheaf-theoretically trivial, meaning that A ∼=
Rˆ⊗OX, endowed with either an associative multiplication (called a star prod-
uct), or a Poisson bracket. This is what happens in the diﬀerentiable setup (i.e.
when X is a C∞manifold and K = R). But in the algebro-geometric setup the
sheafA could be very complicated – indeed, all classical commutative deformations
ofOX are special cases of both associative and Poisson deformations.
SupposeA andA′are twoR-deformations (of the same kind, namely both are
Poisson or associative). Agauge transformationg :A→A′is an isomorphism of
sheaves ofR-algebras (Poisson or associative) that commutes with the augmenta-
tions toOX. If such a gauge transformation exists, thenA andA′are said to be
gauge equivalent.
An R-deformationA ofOX determines a ﬁrst order bracket{−,−}A onOX.
When R = K[[ℏ]] this is the usual induced Poisson bracket, cf. [Ye1]. For general
R see Deﬁnition 2.20. It is important to note that the ﬁrst order bracket{−,−}A
is gauge invariant.
Example 0.1.1. Suppose{−,−}is a Poisson bracket onOX. Consider the com-
mutative K[[ℏ]]-algebraA :=OX[[ℏ]] = K[[ℏ]]ˆ⊗OX, endowed with the Poisson
bracket ℏ{−,−}and the obvious augmentation toOX. We get a Poisson K[[ℏ]]-
deformation ofOX, and the ﬁrst order bracket is{−,−}A ={−,−}.
LetA be a PoissonR-deformation ofOX. A deformation quantization ofA is
an associativeR-deformationB = quant(A), such that{−,−}B ={−,−}A.
In the fundamental paper [Ko1], M. Kontsevich proved that in theC∞setup, and
for R = R[[ℏ]], every Poisson R[[ℏ]]-deformationA can be quantized. Moreover,
Kontsevich proved that his quantization is canonical, and it induces a bijection
between the set of gauge equivalence classes of Poisson deformations, and the set
of gauge equivalence classes of associative deformations.
We proved an analogous result foraﬃne smooth algebraic varietiesover a ﬁeldK
containing R. The method used in our paper [Ye1] was an adaptation of the ideas
of Kontsevich from [Ko1] to the algebro-geometric setup. There were cohomological
obstructions, indicating that the same result (namely [Ye1, Theorem 0.1]) would
not hold for more complicated smooth algebraic varieties.
0.2. Twisted Quantization: Overview. In the paper [Ko2], Kontsevich sug-
gested that onany smooth algebraic varietyX, every PoissonR-deformationA of
OX can be quantized to astack ofR-algebroids B on X.
The purpose of the present paper is more than just to provide a proof of that
assertion of Konstevich. We introduce the notions oftwisted PoissonR-deformation
and twisted associativeR-deformation ofOX. These are stacky versions of theR-
deformations discussed above. A twisted associative R-deformation is a reﬁned
variant of thestack of R-linear algebroidsfrom [Ko2], and is very similar to the
notion of DQ algebroid from [KS2]. The concept of twisted Poisson deformation
appears to be totally new (in algebraic geometry, as well as in real diﬀerential and
complex analytic geometry).
Our main result (the Twisted Quantization Theorem, number 0.10.1 below) es-
tablishes a twisted quantizationoperation, which is a canonical bijection between
the set of twisted gauge equivalence classes of twisted PoissonR-deformations of
OX, and the set of twisted gauge equivalence classes of twisted associative R-
deformations. The proof of Theorem 0.10.1 requires many intermediate results (in
ring theory, algebraic geometry, cosimplicial groupoids andL∞morphisms), some
TWISTED DEFORMATION QUANTIZATION 3
of them of independent interest. We present a few of these intermediate results be-
low in the Introduction. The Twisted Quantization Theorem raises a few questions
that we ﬁnd intriguing; see end of Section 11.
We should mention that the ﬁrst occurrence of twisted quantization was in the
paper [Ka] of M. Kashiwara from 1996, that concerned contact manifolds. We
discuss this work, and several other papers related to twisted deformations, in
Subsection 0.11.
0.3. Twisted Deformations.Let us now explain what are twisted deformations.
We shall start with the concept ofcrossed groupoid(also known as a crossed
module over a groupoid, or a strict2-groupoid, cf. [Ye7, Bw]). This is a structure
P = (P1, P2, AdP1↷P2, D) consisting of groupoids P1 and P2, such thatOb(P1) =
Ob(P2) and P2 is totally disconnected; an actionAdP1↷P2 of P1 on P2 called the
twisting; and a morphism of groupoids (i.e. a functor) D : P2 →P1 called the
feedback. There are conditions relating the twisting and the feedback; see Deﬁnition
1.2 for more details. We refer to the morphisms in the groupoidP1 as 1-morphisms
of P, or asgauge transformations. The morphisms in P2 are called 2-morphisms,
or inner gauge transformations. There is an obvious notion of morphism between
crossed groupoids.
Now letX be a topological space. Astack of crossed groupoidsP on X is the
geometrization of a crossed groupoid. Thus for every open setU ⊂X we have
a crossed groupoid P(U); and for every inclusion V ⊂U of open sets there is
a morphism of crossed groupoids restV/U : P(U)→P(V ). We assume that the
restriction morphisms satisfy restW/V ◦restV/U = restW/U for a double inclusion
W⊂V ⊂U of open sets ofX. We also assume thatP1 is a stack of groupoids (in
the usual sense), and for every local objectA of P the presheaf of groupsP2(A) is
a sheaf. See Deﬁnition 1.11 for details.
For us there are two important stacks of crossed groupoids. LetK be a ﬁeld of
characteristic 0,X an algebraic variety overK, and(R, m) some parameter algebra
over K (these are the default assumptions for the rest of the Introduction). First
there is the stackP := AssDef(R,OX) of associativeR-deformations ofOX, which
assigns to each open setU⊂X the set P(U) := AssDef(R,OU) of associativeR-
deformations ofOU. The 1-morphisms inP(U) are the gauge transformations. The
inner gauge groupP2(U)(A) of an objectA∈Ob(P(U)) is the multiplicative group
of elements ofΓ(U,A) that are congruent to1 modulo m. The feedback D(a), for
an elementa∈P2(U)(A), is the conjugation action ofa onA|U.
The second stack of crossed groupoids is the stackP := PoisDef(R,OX) of Pois-
son R-deformations ofOX. It assigns to each open setU ⊂X the set P(U) :=
PoisDef(R,OU) of Poisson R-deformations of OU. Again the 1-morphisms are
the gauge transformations. The inner gauge group P2(U)(A) of an objectA∈
Ob(P(U)) is Γ(U, Exp(mA)), where mA is viewed as a sheaf of pronilpotent Lie
algebras with the Poisson bracket. The action of P2(U)(A) onA is by formal
hamiltonian ﬂows.
Given a stack of crossed groupoidsP on X, we can talk abouttwisted objects
of P. Such a twisted object is a triple(G, A, cp), consisting of a gerbeG on X,
called the gauge gerbe, with a morphism of stacks of groupoids A : G →P1,
called the representation. This means that to every local objecti of G we assign
a local object A(i) of P; and to every local isomorphismg :i→j in G we assign
a local 1-isomorphism (i.e. a gauge transformation) A(g) : A(i)→A(j) in P1.
There is also an isomorphism of sheaves of groupscp : G(i)→P2(A(i)) for every
local objecti of G, called thecoupling isomorphism. All these data have to satisfy
certain compatibilities – see Deﬁnitions 4.1 and 4.6 for full details. By slight abuse
4 AMNON YEKUTIELI
of language, we usually refer to the twisted objectA and its gauge gerbeG. An
object A(i), for some local objecti of G, is called alocal objectof A.
In Examples 4.7 and 4.8 we explain how gerbes and stacks ofR-algebroids can
be viewed as twisted objects, of the stacks of crossed groupoids Grp×(X) and
Assoc×(R,X ) respectively.
By deﬁnition atwisted associative R-deformation of OX is a twisted object
A of the stack of crossed groupoids AssDef(R,OX). Likewise, a twisted Pois-
son R-deformation ofOX is a twisted objectA of the stack of crossed groupoids
PoisDef(R,OX).
The distinction between twisted associativeR-deformations and DQ-algebroids
(in the sense of [KS2]) is explained in Remark 4.13. As we said before, the concept
of twisted Poisson deformation appears to be completely new – there does not seem
to be any similar deﬁnition in the literature.
0.4. Gauge Gerbes. There is a beneﬁt in working with gauge gerbes: it is easier
to study the combinatorial structure of a twisted deformation. Indeed, letA be
a twistedR-deformation ofOX, with gauge gerbe G. The coupling isomorphism
endows G with the m-adic ﬁltration, making it into a pronilpotent gerbe (in the
sense of [Ye4]). Using the results from [Ye4] on pronilpotent gerbes we obtain the
next theorem (repeated in a more general form as Theorem 7.2 in the body of the
paper):
Theorem 0.4.1 (Total Trivialization). Let K be a ﬁeld of characteristic0, X
an algebraic variety overK, A a twisted associative or PoissonR-deformation of
OX, with gauge gerbe G, and U an open set in X that satisﬁesH1(U,OX) =
H2(U,OX) = 0 (for instance an aﬃne open set). Then the groupoid G(U) is
nonempty and connected.
0.5. Combinatorial Descent. In this subsection we leave the geometry aside,
to talk about combinatorial descent data. We shall return to the geometry in
Subsection 0.7.
We are interested incosimplicial crossed groupoids. A cosimplicial crossed group-
oidG ={Gp}p∈N is made up of a crossed groupoidGp = (Gp
1,Gp
2, Ad, D)for everyp,
and a morphism of crossed groupoidsG(α) :Gp→Gq for every arrowα:p→q in
the simplex category∆ . The morphismsG(α) must satisfy the simplicial relations.
Let G ={Gp}p∈N be a cosimplicial crossed groupoid. Acombinatorial descent
datum in G is a triple(ω,g,a) consisting of elements of these sorts:ω∈Ob(G0),
g ∈G1
1(ω(0),ω(1)) and a ∈G2
2(ω(0),ω(0)). These elements have to satisfy two
conditions: “failure of1-cocycle” and “twisted2-cocycle”; see Deﬁnition 5.2. Here
ω(i) is the object of the crossed groupoidGp corresponding to the vertex(i) of the
simplex ∆ p, andGp
p(ω(i),ω(j)) is the set of morphismsω(i)→ω(j) in the groupoid
Gp
p.
As we shall see in Subsection 0.7 below, combinatorial descent data is an ab-
straction of the familiar descent data for gerbes.
Let us denote by Desc(G) the set of combinatorial descent data. There is an
equivalence relation on this set, called gauge equivalence (see Deﬁnition 5.3), and
we denote by Desc(G) the quotient set. A morphism Φ : G→H of cosimplicial
crossed groupoids induces a functionDesc(Φ) : Desc(G)→Desc(H). The notion of
weak equivalencebetween cosimplicial crossed groupoids is introduced in Deﬁnition
5.5. The next result is proved in the companion paper [Ye8]. See [Pr] for an
alternative proof.
TWISTED DEFORMATION QUANTIZATION 5
Theorem 0.5.1(Combinatorial Equivalence, [Ye8, Theorem 0.1]). Let Φ : G→H
be a weak equivalence between cosimplicial crossed groupoids. Then the function
Desc(Φ) : Desc(G)→Desc(H)
is bijective.
0.6. Lie Descent. Let g = ⨁
i∈Z gi be a quantum type DG Lie algebra overK,
namely gi = 0 for alli< −1. There is an induced pronilpotent DG LieR-algebra
mˆ⊗g = ⨁
i∈Z mˆ⊗gi. Following [De] and [Ge1] we consider theDeligne crossed
groupoid Del(g,R ) (better known as the Deligne2-groupoid). Recall that the set
of objects of Del(g,R ) is the set MC(mˆ⊗g) of solutions of the Maurer-Cartan
equation. The 1-morphisms in Del(g,R ) are the elements of the gauge group
Exp(mˆ⊗g0), and the 2-morphisms in Del(g,R ) are the elements of the groups
Exp(mˆ⊗g−1)ω, forω∈MC(mˆ⊗g). See Sections 3 and 8 for details.
Now suppose g ={gp}p∈N is a cosimplicial quantum type DG Lie algebra. So
in each simplicial dimension p there is a quantum type DG Lie algebra gp =⨁
i≥−1 gp,i. Since the Deligne crossed groupoid is functorial, we get a cosimplicial
crossed groupoid Del(g,R ) =
{
Del(gp,R )
}
p∈N. The combinatorial descent con-
struction from Subsection 0.5 gives rise to the set of Lie descent data
Desc
(
Del(g,R )
{
, and its quotient set (modulo gauge equivalence)Desc
(
Del(g,R )
{
.
Suppose h ={hp}p∈N is another cosimplicial quantum type DG Lie algebra. A
cosimplicial L∞morphism Ψ : g→h is a collectionΨp : gp→hp of L∞morphisms,
that respect the cosimplicial structures. We say thatΨ is a cosimplicialL∞quasi-
isomorphism if each Ψp : gp→hp is an L∞quasi-isomorphism.
Theorem 0.6.1(Equivalence for Lie Descent). Let Ψ : g→h be a cosimplicialL∞
morphism between cosimplicial quantum type DG Lie algebras, and letν: R→S
be a homomorphism between parameter algebras, all over a ﬁeldK of characteristic
0. Then there is a function
Desc(Del)(Ψ,ν) : Desc(Del(g,R ))→Desc(Del(h,S )),
which is functorial in Ψ and ν. Furthermore, if Ψ is a cosimplicial L∞quasi-
isomorphism andνis an isomorphism, thenDesc(Del)(Ψ,ν) is bijective.
This is repeated with more details as Theorem 8.8 in the body of the paper. The
proof uses Theorem 0.5.1, and results from [Ye7] on the Deligne crossed groupoid
and on thebar-cobar constructionfor DG Lie algebras.
0.7. Geometric Descent.Let P = (P1, P2, AdP1↷P2, D) be some stack of crossed
groupoids on a topological spaceX. We denote the set of twisted objects of P
by TwOb(P). There is an intrinsic notion of twisted gauge equivalence between
twisted objects (see Deﬁnition 4.10), and we denote the resulting set of equivalence
classes by TwOb(P).
Let U ={Uk}k∈K be an open covering of the spaceX. For k0,...,km∈K
we write Uk0,...,km := Uk0∩···∩Ukm. A geometric descent datum for twisted
objects of P, relative to this covering, consists of a collection{Ak0}k0∈K of objects
Ak0∈Ob(P(Uk0)), a collection{gk0,k1}of 1-morphisms
gk0,k1 :Ak0|Uk0,k1
≃
− →Ak1|Uk0,k1
in P1(Uk0,k1), and a collection{ak0,k1,k2}of 2-morphisms
ak0,k1,k2∈P2(Uk0,k1,k2)(Ak0|Uk0,k1,k2 ).
The conditions are:
g−1
k0,k2
◦gk1,k2◦gk0,k1 = D(ak0,k1,k2)
6 AMNON YEKUTIELI
as automorphisms ofAk0|Uk0,k1,k2 in P1(Uk0,k1,k2), and
a−1
k0,k1,k3
·ak0,k2,k3·ak0,k1,k2 = AdP1↷P2(g−1
k0,k1
)(ak1,k2,k3)
in the groupP2(Uk0,...,k3)(Ak0|Uk0,...,k3 ).
The above can be stated in terms of combinatorial descent (see Subsection 0.5).
For any open setU⊂X we have a crossed groupoidP(U). Thus, given an open
covering U, the Čech construction gives rise to a cosimplicial crossed groupoid
C(U, P). A geometric descent datum is precisely an element ofDesc(C(U, P)).
A consequence of Theorem 0.4.1 is this result (it is a combination of Corollary
7.4, Theorem 6.22, Proposition 6.19 and Proposition 2.15 in the body of the paper):
Theorem 0.7.1(Decomposition). Let K be a ﬁeld of characteristic0, X a smooth
algebraic variety overK,R a parameter algebra overK, andU an aﬃne open cover-
ing of X. Denote by P(R,X ) either of the stacks of crossed groupoids
AssDef(R,OX) or PoisDef(R,OX). Then there is a bijection
dec : TwOb
(
P(R,X )
{≃
− →Desc
(
C(U, P(R,X ))
{
called decomposition, which is functorial with respect to reﬁnementsU′→U of
aﬃne open coverings, and with respect to homomorphismsR→R′of parameter
algebras.
The ideas of geometric descent data and decomposition are not new; they appear
in most texts about gerbes (cf. [Gi, Section IV.3.5], and also [Br, Ko2, BGNT1,
DP1]). However, a result such as Theorem 0.4.1 is usually not available, and the
authors usually impose something like Theorem 0.4.1 as a condition (explicitly or
implicitly), or else they are forced to deal with hypercoverings.
WhatTheorem0.7.1saysisthatwecanreplacethestudyoftwisteddeformations
with that of geometric descent data.
0.8. DG Lie Algebras and Deformations.On the smooth algebraic varietyX
there are two important sheaves of DG Lie algebras: the sheafTpoly,X of poly-
derivations, and the sheafDpoly,X of polydiﬀerential operators. Within Dpoly,X
there is the subalgebraDnor
poly,X ofnormalized polydiﬀerential operators. The sheaves
Tpoly,X,Dpoly,X andDnor
poly,X are quasi-coherent gradedOX-modules, and the in-
clusionDnor
poly,X→Dpoly,X is a quasi-isomorphism.
Theorem 0.8.1 (Geometrization, [Ye9, Theorem 0.1]). Let K be a ﬁeld of char-
acteristic 0, X a smooth algebraic variety overK, R a parameter algebra overK,
and U an aﬃne open set inX. There are equivalences of crossed groupoids
geo : Del
(
Γ(U,Dnor
poly,X),R
{
→AssDef(R,OU)
and
geo : Del
(
Γ(U,Tpoly,X),R
{
→PoisDef(R,OU)
which we callgeometrization. The equivalencesgeo commute with homomorphisms
R→R′of parameter algebras, and with inclusions of aﬃne open setsU′→U.
See Deﬁnition 1.9 regarding equivalences of crossed groupoids.
In earlier versions of this paper the proof of Theorem 0.8.1 was part of the
material. However the paper got to be extremely long, and hence we extracted all
the material leading to Theorem 0.8.1, and made it into the new paper [Ye9]. In
terms of content, everything involving stacks remained in this paper, and the rest
was moved to [Ye9].
The proof of Theorem 0.8.1, in [Ye9], has several diﬃcult components. First
there is the issue ofm-adically complete ﬂat sheaves ofR-modules on the variety
X, that required a lot of basic work (some of it in [Ye5]). Regarding associative
TWISTED DEFORMATION QUANTIZATION 7
deformations, the geometrization required a delicate analysis of sheaves of noncom-
mutative rings on an algebraic variety, usingOre localization. The fact that the DG
Lie algebraDnor
poly,X controls associative deformations (without any diﬀerentiality
restriction on these deformations!) is a new result. In our earlier paper [Ye1] we
had to put a local diﬀerentiality condition on associative deformations (that we
now know is redundant). It is important to note that the corresponding statement
for complex analytic manifolds is an open problem; see [KS2, Remark 2.2.7].
Consider a ﬁnite aﬃne open coveringU of X. The Čech construction gives rise
to the cosimplicial quantum type DG Lie algebrasC(U,Tpoly,X)and C(U,Dnor
poly,X).
The combination of Theorems 0.8.1 and 0.5.1 yields:
Corollary 0.8.2(Geometrization of Descent Data). Let K be a ﬁeld of character-
istic 0, X a smooth algebraic variety overK, R a parameter algebra overK, and
U a ﬁnite aﬃne open covering ofX. There are bijections
geo : Desc
(
Del
(
C(U,Dnor
poly,X),R
{{≃
− →Desc
(
C
(
AssDef(R,OX),U
{{
and
geo : Desc
(
Del
(
C(U,Tpoly,X),R
{{≃
− →Desc
(
C
(
PoisDef(R,OX),U
{{
.
The functions geo respect homomorphisms R →R′of parameter algebras, and
reﬁnements of coveringsU′→U.
This is Theorem 9.5 in the body of the paper.
We know thatTpoly,X andDnor
poly,X are sheaves in the étale topology ofX. This,
with Corollary 0.8.2 and Theorem 0.7.1, imply thatTwOb
(
P(R,X )
{
is contravari-
ant with respect to étale morphismsX′→X. The set TwOb
(
P(R,X )
{
is also
covariant with respect to homomorphismsR →R′of parameter algebras. See
Theorem 9.9 for the precise statement.
0.9. The Formality Morphism. Given a ﬁnite aﬃne open coveringU of X,
we can form themixed resolutionMixU(M) of any quasi-coherent sheafM. This
resolutionisfunctorial, andmoreoverthecomplex MixU(M)isacyclicfortheglobal
sections functorΓ(X,−). Resolving the sheavesTpoly,X andDpoly,X we get sheaves
of DG Lie algebrasMixU(Tpoly,X) and MixU(Dpoly,X). See [Ye1, Proposition 6.3]
for details.
Assume dimX = n. An étale coordinate systemon an open setU ⊂X is an
étale morphism s : U →An
K. By open covering with étale coordinatesof X we
mean a pair (U,s), consisting of an open coveringU ={Uk}, together with a
familys ={sk}of étale coordinate systemssk :Uk→An
K.
One of the main results of [Ye1] is that there is anL∞quasi-isomorphism
Ψ s ={Ψ s;i}i≥1 : MixU(Tpoly,X)→MixU(Dpoly,X)
between sheaves of DG Lie algebras onX. This is [Ye1, Theorem 0.2], and it relies
on the universal formality morphism of Kontsevich from [Ko1]. See [VdB, Theorem
1.1] for another proof. In Theorem 10.3 in the body of the paper we expand [Ye1,
Theorem 0.2]. As a consequence we obtain the next theorem, which is repeated,
with more details, as Theorem 10.6.
Theorem 0.9.1(Cosimplicial Formality). Assume the ﬁeldK contains R. LetX
be a smooth algebraic variety overK, and let(U,s) be a ﬁnite aﬃne open covering
8 AMNON YEKUTIELI
with étale coordinates ofX. Then there is a diagram
C(U,Tpoly,X)

C(U,Dnor
poly,X)

C
(
U, MixU(Tpoly,X)
{ C(U,Ψ s) // C
(
U, MixU(Dpoly,X)
{
,
where the objects are cosimplicial quantum type DG Lie algebras, the vertical arrows
are cosimplicial DG Lie quasi-isomorphisms, and the horizontal arrow is a cosim-
plicial L∞quasi-isomorphism. This diagram is independent (up to cosimplicial
quasi-isomorphism) of the covering(U,s), and respects étale morphismsX′→X.
The reason for the conditionR⊂K is because in [Ye1] we used the original uni-
versal quantization morphism of Konstevich [Ko1]. See Remark 11.6 for a discussion
on how to relax this condition.
0.10. The Twisted Quantization Theorem.There is a notion oftwisted gauge
equivalence between twisted associativeR-deformation ofOX; this is the same as
the twisted gauge equivalence inTwOb(P) for P := AssDef(R,OX). Likewise for
twisted Poisson deformations.
A twisted deformation A induces a ﬁrst order bracket{−,−}A onOX. See
Deﬁnition 4.15, or the text preceding Example 0.1.1 above.
Here is the main result of our paper:
Theorem 0.10.1 (Twisted Quantization). Let K be a ﬁeld containing the real
numbers, letR be a parameterK-algebra, and letX be a smooth algebraic variety
over K. Then there is a bijection of sets
tw.quant :{twisted PoissonR-deformations ofOX}
twisted gauge equivalence
∼=−−→{twisted associativeR-deformations ofOX}
twisted gauge equivalence
called twisted quantization. The bijection tw.quant preserves ﬁrst order brackets,
and commutes with homomorphisms of parameter algebrasR→R′, and with étale
morphisms of varietiesX′→X.
This theorem is repeated in greater detail as Theorem 11.1. It is proved by
assembling Theorem 0.7.1, Corollary 0.8.2, Theorem 0.9.1 and Theorem 0.6.1. The
roles of these results can be seen in the diagram in Figure 1. Speciﬁcally, the
bijections dec in the diagram are from Theorem 0.7.1; the bijectionsgeo are from
Corollary 0.8.2; and the bijections mix and Ψ s are gotten by applying Theorem
0.6.1 to the diagram of cosimplicialL∞quasi-isomorphisms in Theorem 0.9.1.
In Corollaries 11.2 and 11.3 we explain what happens when some or all of the
cohomology groups H1(X,OX), H2(X,OX), H1(X,TX) and H1(X,DX) vanish.
A twistedR-deformation A ofOX is said to bereally twistedif it has no global
objects, namely if the groupoidG(X) is empty (whereG is the gauge gerbe ofA).
Any deformationA generates a twisted deformationA, andA is a global object
of A. See Example 6.23. Any twisted deformationA that is not really twisted is
of this form.
One consequence of Theorem 7.2 is that in the diﬀerentiable setup (andK = R)
there are no really twistedR-deformations. However, whenX is a complex analytic
manifold (and K = C), there do exist really twistedR-deformations. Presumably
our methods (with minor adjustments) should work also for complex analytic man-
ifolds, and a result similar to Theorem 0.10.1 should hold.
Here is a question that we ﬁnd intriguing.
TWISTED DEFORMATION QUANTIZATION 9
TwOb
(
PoisDef(R,OX)
{
dec

tw.quant // TwOb
(
AssDef(R,OX)
{
dec

Desc
(
C(U, PoisDef(R,OX))
{
Desc
(
C(U, AssDef(R,OX))
{
Desc
(
Del
(
C(U,Tpoly,X),R
{{
geo
OO
mix

Desc
(
Del
(
C(U,Dnor
poly,X),R
{{
geo
OO
mix

Desc
(
Del
(
C(U, MixU(Tpoly,X)),R
{{ Ψ s // Desc
(
Del
(
C(U, MixU(Dpoly,X)),R
{{
Figure 1. Diagram of bijections in the proof of Theorem 0.10.1.
Question 0.10.2.LetX be a Calabi-Yau surface, with symplectic Poisson bracket
{−,−}. Consider the Poisson K[[ℏ]]-deformationA ofOX that we get from Ex-
ample 0.1.1, and the twisted Poisson deformationA generated byA. Let B :=
tw.quant(A), which is a twisted associativeK[[ℏ]]-deformation ofOX, well-deﬁned
up to twisted gauge equivalence. IsB really twisted?
This question is repeated (with a few more details) at the end of Section 11,
along with a some other questions.
0.11. Discussion of Related Work.We ﬁnish the introduction with a discussion
ofseveralrelatedpapers. Thisisnotaneasytask, sincethesepaperswerewrittenby
people working in several mathematical branches – diﬀerential geometry, complex
analytic geometry, algebraic geometry and mathematical physics – and the style of
writing varies accordingly.
The impetus for our work was trying to understand the ideas proposed by Kont-
sevich in [Ko2]. In that paper Kontsevich considered a smooth algebraic varietyX
over a ﬁeld of characteristic0. He claimed that any formal Poisson deformation
ofOX can be quantized to a stack of algebroids. However there was only a hint
of a proof in [Ko2], and there was no statement regarding classiﬁcation. We found
this new idea of Kontsevich extremely interesting, and wanted to prove it, and to
expand it to a precise classiﬁcation statement (generalizing the aﬃne case). We
had several conversations with Kontsevich, in which he oﬀered some valuable sug-
gestions, that eventually led us to the concept of twisted Poisson deformation (see
Subsection 0.3). The precise statement about twisted deformation quantization of
an algebraic variety appears for the ﬁrst time in this paper (this is Theorem 0.10.1);
and ours is the only paper that gives a complete proof of this result.
As we already mentioned, Kashiwara [Ka] was the ﬁrst to consider stacky quan-
tizations. The situation in [Ka] was this:X is a complex contact manifold, so there
is an open coveringX =⋃Ui, where eachUi is isomorphic to an open submanifold
of a projective cotangent bundle. Thus onUi there is a sheafEi of microdiﬀerential
operators. Kashiwara proved that even if theEi cannot be glued into a sheaf of
rings, they can always be glued into a twisted sheaf (i.e. a stack of algebroids)E.
The paper [KS2] by Kashiwara and P. Schapira discusses a variant of the stack
of microdiﬀerential operators, that is called aDQ algebroid. The description of a
DQ algebroid A as a twisted object is explained in Remark 4.13. There is some
overlap regarding technical points between our paper and [KS2] (see Remark 3.8,
and the Introduction of [Ye9]). The main thrust of [KS2] is the study of the
Hochschild homology sheaf associated to a symplectic DQ algebroidA, and related
10 AMNON YEKUTIELI
characteristic classes. It does not contain any sort of twisted quantization statement
similar to our Theorem 0.10.1.
P. Polesello and A. D’Agnolo [Po, DP1, DP2] studied twisted associative defor-
mations of complex manifolds, and quantizations of contact manifolds, in the spirit
of [Ka, KS2]. The relationship between [DP2] and our paper is mostly that in both
papers heavy use is made of stacks of crossed groupoids as a means of classify-
ing twisted forms of stacks (as in Theorem 0.7.1 above). The paper [Po] classi-
ﬁes twisted associative deformations corresponding to a ﬁxed symplectic structure;
there is nothing in it resembling our Theorem 0.10.1. One should also note (this
was pointed to us by Polesello) that the deformations in [Po] and [KS2] are not
augmented (see Remark 4.13).
E. Getzler wrote two papers [Ge1, Ge2] on higher Deligne groupoids. The rele-
vant results in [Ge2], and a certain diﬃculty in that paper, are explained in Remark
8.11. For some time we had hoped to rely on Getzler’s results for a proof of Theorem
0.6.1 (at least for artinian parameter algebras), but we could not ﬁnd a satisfac-
tory way to overcome the diﬃculty mentioned in Remark 8.11. This is why we
eventually provided our own proof, that does not rely on Getzler’s work.
P. Bressler, A. Gorokhovsky, R. Nest and B. Tsygan wrote a series of papers
on deformations of real and complex manifolds. In the paper [BGNT1] there is a
discussionofcosimplicialDGLiealgebras, withresultssimilartoourTheorem0.6.1,
but only for DG Lie homomorphismsg→h between cosimplicial DG Lie algebras
(not L∞morphisms), and only for artinian parameter algebras. Nonetheless several
resultsin[BGNT1]inspireduswhenwediscoveredTheorems0.5.1and0.6.1. Stacks
– in the true geometric sense – do not actually occur in [BGNT1]; the authors only
look at what we refer to in Subsection 0.7 as geometric descent data. Also there
is no twisted quantization result similar to our Theorem 0.10.1; in a large part of
the paper they only consider a particular symplectic Poisson bracket and study its
twisted associative quantizations.
The paper [BGNT2] considers twisted associative deformations of twistedOX-
algebroids on a real or complex manifoldX. If we understand correctly, the as-
sociative deformations considered in [BGNT2] are by deﬁnition locally diﬀerential,
so the authors avoid touching the hard technical issues lying behind our Theorem
0.8.1 (see discussion in Subsection 0.8). The paper [BGNT2] does not contain a
twisted quantization result similar to our Theorem 0.10.1. As far as we can tell
one of the main results there, namely [BGNT2, Theorem 5.22], is analogous to our
Corollary 0.8.2 in the associative case.
The third paper by this team of authors is [BGNT3]. They consider several kinds
of nerves (simplicial sets) associated with2-groupoids, and prove these are homo-
topy equivalent. One of the methods used in [BGNT3] is nonabelian multiplicative
integration of surfaces, as in our paper [Ye6]; indeed, they reproduce some of our
results (with shorter proofs in special cases). Among other things, it is claimed in
[BGNT3] that the diﬃculty in [Ge2] mentioned above can be settled (more on this
in Remark 8.11). It should be interesting to compare the results of [BGNT3] to our
Theorems 0.5.1 and 0.6.1.
The fourth paper in this series is [BGNT4]. Here they look at aC∞manifold
X over K = R, with structure sheafOX. They start with a twist B0 ofOX,
namely a stack of R-algebroids B0 on X that is locally equivalent toOX. Such
twists are classiﬁed by cohomology classes[φ]∈H3
dR(X). Let R be an artinian
parameter R-algebra with maximal ideal m. Theorem 1.1 of [BGNT4] says that
associative R-deformations B of B0 are classiﬁed by the Deligne crossed groupoid
of an L∞algebra, whose underlying graded R-module is Γ(X,Tpoly,X)⊗m. The
binary operation is the usual one, but there is a ternary operation coming from a
TWISTED DEFORMATION QUANTIZATION 11
closed 3-formφonX that represents the de Rham class[φ] of B0. This means that
stacky associativeR-deformations B correspond toR-linearφ-Poisson structures on
X, in the sense of Severa and Weinstein (cf. [Se]). In this way [BGNT4, Theorem
1.1] can be viewed as describing a twisted quantization operation. However, the
stackyness of anR-deformation B is the same as that ofB0 = R⊗R B. Thus this
result is “perpendicular” to our twisted quantization from Theorem 0.10.1: for us
the algebroid B0 is always trivial (i.e.B0 =OX), and the stackyness is only in the
R-linear deformation B.
Thelastpapertobediscussedis[CH]. Theaimofthatpaperistoproveatwisted
deformation quantization like our Theorem 0.10.1. However in [CH] the authors
do not consider actual geometric twisted deformations, but only the corresponding
Lie descent data. Thus they do not have any kind of geometrization result like
our Corollary 0.8.2, nor a decomposition result like our Theorem 0.7.1. Their main
result, [CH, Theorem 3.5], seems to assert (in our notation, and whenX is a smooth
algebraic variety) that there is a bijection
Desc
(
Del
(
C(U,Tpoly,X), K[[ℏ]]
{{∼= Desc
(
Del
(
C(U,Dnor
poly,X), K[[ℏ]]
{{
.
Thus it is only a part of our Theorem 0.10.1 (the bottom half of the diagram
in Figure 1). We have some reservations regarding the validity of the proofs in
[CH], for these reasons: the proofs in [CH] are not all clear; delicate issues about
pronilpotent groupoids (such as those dealt with in the paper [Ye7]) are ignored;
and there are some speciﬁc problems in homotopy theory (cf. Remarks 5.7 and
8.11).
Acknowledgments. Work on this paper began together with Fredrick Leitner,
and I wish to thank him for his contributions. Many of the ideas in this paper
are inﬂuenced by the work of Maxim Kontsevich, and I am grateful to him for
discussing this material with me. Thanks also to Michael Artin, Pavel Etingof,
Damien Calaque, Michel Van den Bergh, Pierre Deligne, Lawrence Breen, Pierre
Schapira, Assaf Hasson, George Bergman, James Stasheﬀ, Vladimir Hinich, Pietro
Polesello, Francois Petit and Matan Prasma for their assistance on various aspects
of this project. Finally I wish to thank the anonymous referee for reading the paper
carefully and suggesting some further references.
