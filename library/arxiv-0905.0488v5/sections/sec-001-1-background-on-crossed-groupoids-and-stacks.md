---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI"
section_id: sec-001-1-background-on-crossed-groupoids-and-stacks
section_title: "Background on Crossed Groupoids and Stacks"
section_number: 1
pages: 11-15
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI — Let X be a smooth algebraic variety over a ﬁeldK containing the real numbers."
---
Inthispaperweworkalotwithstacksontopologicalspaces. Thereadercancon-
sult our earlier paper [Ye4], that contains a pretty detailed account of2-categories,
stacks and gerbes, with the same notation (Sections 1-2 of that paper).
Regarding set theoretic considerations, we employ Grothendieck universes. We
consider a universe U, that we call the small universe. Elements ofU are called
small sets. By default all groups, rings etc. are small, i.e. their underlying sets
are small. And by default all categoriesC are U-categories, i.e. Ob(C)⊂U, and
HomC(i,j )∈Ufor alli,j ∈Ob(C). Thus Set, Grpetc. denote the categories of small
sets, small groups etc., and they areU-categories. However some of the categories
will be small categories; a categoryC is small ifOb(C) is a small set. There is also
a universe V, that we call the big universe, andU is an element of V. Elements
of V will be called big sets. The2-category Cat of all U-categories is aV-category
(namely Ob(Cat)⊂V).
Recall that agroupoidis a category in which all morphisms are invertible. Given
a groupoidG and objectsi,j ∈Ob(G) we usually writeG(i,j ) := HomG(i,j ), the
set of morphisms fromi to j; andG(i) := G(i,i ), the automorphism group of the
object i.
Deﬁnition 1.1.Let G be a groupoid.
12 AMNON YEKUTIELI
(1) Let i,j ∈Ob(G) and g∈G(i,j ). We deﬁne an isomorphism of groups
AdG(g) :G(i)
≃
− →G(j)
by the formulaAdG(g)(h) :=g◦h◦g−1 for h∈G(i).
(2) The functor AutG : G→Grp is deﬁned as follows: on objectsAutG(i) :=
G(i), and on morphismsAutG(g) := AdG(g).
(3) Let H be another groupoid, and letΦ : G→H be a functor. Deﬁne the
natural transformation
AutΦ : AutG⇒AutH◦Φ
of functorsG→Grp to be the group homomorphismAutΦ := Φ : G(i)→
H(Φ(i)), fori∈Ob(G).
Suppose G and N are groupoids, such that Ob(N) = Ob( G). An action Ψ
of G on N is a collection of group isomorphisms Ψ(g) : N(i)
≃
− →N(j) for all
i,j ∈Ob(G) and g∈G(i,j ), such thatΨ(h◦g) = Ψ(h)◦Ψ(g) whenever g and h
are composable, and Ψ(1i) is the identity automorphism of the groupN(i). The
prototypical example is the actionAdG of G on itself.
Deﬁnition 1.2.A crossed groupoidis a structure
G = (G1,G 2, AdG1↷G2, D)
consisting of:
•Groupoids G1 andG2, such thatG2 is totally disconnected, andOb(G1) =
Ob(G2). We writeOb(G) := Ob(G1).
•An action AdG1↷G2 of G1 on G2, called thetwisting.
•A morphism of groupoids (i.e. a functor)D :G2→G1 called thefeedback,
which is the identity on objects.
These are the conditions:
(i) The morphism D is G1-equivariant with respect to the actionsAdG1↷G2
and AdG1. Namely
D(AdG1↷G2(g)(a)) = AdG1(g)(D(a))
in the groupG1(j), for anyi,j ∈Ob(G), g∈G1(i,j ) and a∈G2(i).
(ii) For anyi∈Ob(G) and a∈G2(i) there is equality
AdG1↷G2(D(a)) = AdG2(i)(a),
as automorphisms of the groupG2(i).
We sometimes refer to morphisms in the groupoidG1 as 1-morphisms, and to
the morphisms inG2 as 2-morphisms.
For later use we record the next facts (that are almost immediate from the
deﬁnitions).
Proposition 1.3. LetG = (G1,G 2, AdG1↷G2, D) be a crossed groupoid.
(1) For i ∈Ob(G) let IG(i) := G2(i), and for g ∈G1(i,j ) let IG(g) :=
AdG1↷G2(g). Then IG :G1→Grp is a functor.
(2) For i∈Ob(G) and a∈IG(i) let ig(a) := D(a)∈G1(i). Then ig : IG ⇒
AutG1 is a natural transformation of functorsG1→Grp.
(3) The data (G1,G 2, AdG1↷G2, D) can be recovered from the groupoidG1, the
functor IG :G1→Grp and the natural transformationig : IG⇒AutG1.
Proposition 1.3 suggests an alternative way to view the crossed groupoidG =
(G1,G 2, AdG1↷G2, D). We call IG(i) = G2(i) the inner gauge groupof the object
i, and its elements are also calledinner gauge transformations. The group homo-
morphism ig = D : IG(i)→G1(i) is called theinner action. The morphisms inG1
TWISTED DEFORMATION QUANTIZATION 13
are also calledgauge transformations. See Remark 1.7 regarding this point of view.
Warning: the group homomorphismig = D is usually not injective.
Here are some examples of crossed groupoids.
Example 1.4. Consider any groupoidG1, and letG2 be the totally disconnected
groupoid gotten from G1 by removing all morphisms between distinct objects.
(More generally one can take any normal subgroupoidN⊂G1, in the sense of [Ye4,
Deﬁnition 3.1], and deﬁneG2 := N.) Deﬁne the twistingAdG1↷G2 := AdG1|G2,
and the feedbackD :G2→G1 is the inclusion. This is easily seen to be a crossed
groupoid.
For a categoryC we denote byC×the subcategory having all the objects ofC,
and its morphisms are the isomorphisms ofC. We callC×the groupoid of invertible
morphisms of C. Note that if G is a groupoid, then any functorG→C factors
through C×.
Example 1.5. Take the categoryGrp of small groups. We will makeGrp×into a
crossed groupoid by introducing inner gauge groups. For a groupG let IG(G) :=G.
For a group isomorphismφ:G→G′(i.e. for a morphismφ∈Grp×(G,G′)) we let
IG(φ) := φ. And for an elementg∈G we let ig(g) := AdG(g), i.e. conjugation.
Here the kernel of the homomorphism
ig : IG(G) =G = Grp×
2 (G)→Grp×
1 (G) = AutGrp(G)
is the center of the groupG.
Example 1.6. Let R be a commutative ring. Take the category Assoc(R) of
associative unitalR-algebras. Then Assoc×(R) is a crossed groupoid. The group of
innergaugetransformationsofanassociative R-algebraAisthegroup IG(A) :=A×
of invertible elements. It is functorial, since a ring isomorphismg :A→A′sends
invertible elements to invertible elements. The inner actionig(a), fora∈IG(A), is
conjugation by this invertible element, namelyig(a)(a′) = a⋆a′⋆a−1, where⋆is
the multiplication inA. The conditions are very easy to verify.
Remark1.7. Acrossedgroupoidisbetterknownasa strict 2-groupoid, oracrossed
module over a groupoid, or as a2-truncated crossed complex; see [Bw]. WhenOb(G)
is a singleton thenG is just a crossed module. In earlier versions of this paper, and
in [Ye10], we used the namecategory with inner gauge groups. A trace of this name
remains in the inner gauge groupsIG.
We use diﬀerent notation (fonts) for groupoids and crossed groupoids in this
paper, depending usually on their size. ThusG will most likely be a small groupoid,
whereas G will be a big groupoid (i.e. aU-category).
Traditionally papers used2-groupoid language to discuss descent (cf. [BGNT1]).
In this paper we realized that the crossed groupoid language is more eﬀective:
geometric descent data comes naturally in terms of a cosimplicial crossed groupoid
(seeDeﬁnition6.3), andalsotheDeligneconstruction(seeDeﬁnition3.5)appearsas
a crossed groupoid, so it is more natural to talk about theDeligne crossed groupoid.
Deﬁnition 1.8.Suppose H = (H1,H 2, AdH1↷H2, D) is another crossed groupoid.
A morphism of crossed groupoidsΦ : G→H is a pair of morphisms of groupoids
Φp : Gp→Hp, p = 1, 2, that are equal on objects, and respect the twistings and
the feedbacks. We denote byCrGrpd the category consisting of crossed groupoids
and morphisms between them.
Deﬁnition 1.9.A morphism of crossed groupoidsΦ : G→H is called anequiva-
lence if Φ 1 :G1→H1 is an equivalence of groupoids, and for everyi∈Ob(G) the
group homomorphism Φ 2 :G2(i)→H2(Φ 2(i)) is bijective.
14 AMNON YEKUTIELI
Let G be a crossed groupoid. We deﬁne the homotopy setπ0(G) := π0(G1),
namely the set of isomorphism classes of objects ofG1. The homotopy groups ofG
are
π1(G,i ) := Coker
(
D :G2(i)→G1(i)
{
and
π2(G,i ) := Ker
(
D :G2(i)→G1(i)
{
for i∈Ob(G). The setπ0(G) and the groupsπp(G,i ) are functorial inG.
Deﬁnition 1.10.A morphism of crossed groupoidsΦ : G→H is called aweak
equivalence if the functionπ0(Φ) : π0(G)→π0(H) is bijective, and the group
homomorphisms πp(Φ,i ) : πp(G,i )→πp(H, Φ(i)) are bijective for alli∈Ob(G)
and p∈{1, 2}.
Of course ifΦ is an equivalence then it is a weak equivalence.
Deﬁnition 1.11.Let X be a topological space. Astack of crossed groupoids
P = (P1, P2, AdP1↷P2, D)
on X consists of a crossed groupoid
P(U) =
(
P1(U), P2(U), AdP1(U)↷P2(U), D
{
for every open setU⊂X, with a morphism of crossed groupoids
restV/U : P(U)→P(V ),
called restriction, for every inclusionV ⊂U of open sets. The three conditions
below have to hold:
(i) The restriction morphisms satisfyrestW/V◦restV/U = restW/U for a double
inclusion W⊂V ⊂U of open sets ofX.
(ii) The prestack of groupoidsP1 :U↦→P1(U) on X is a stack.
(iii) For every open setU and objectA∈Ob(P(U)), the presheaf of groups
P2(A) :V ↦→P2(V )(restV/U (A))
on U is a sheaf.
Condition (i) says that the stackP1 is split, i.e. it is a catégorie ﬁbrée scindée,
in the sense of [Gi].
Deﬁnition 1.12.Let P be a stack of crossed groupoids onX.
(1) An objectA∈Ob(P(U)), for some open setU, is called alocal objectof P.
(2) LetA∈Ob(P(U)), and letV ⊂U. We writeA|V := restV/U (A).
(3) LetA ∈Ob(P(U)) andA′∈Ob(P(U′)) be local objects of P, and let
V ⊂U∩U′. An elementg∈P1(V )(A|V,A′|V ) is called alocal 1-morphism
of P; and an elementa∈P2(V )(A|V ) is called alocal 2-morphism of P.
(4) Foralocalobject Aof Pwedenoteby IG(A)thesheafofgroups P2(A)from
condition (iii) in Deﬁnition 1.11; and we denote byig : IG(A)→P1(A) the
homomorphism of sheaves of groups induces by the feedbacksD.
We denote by Grp(X) the stack of sheaves of groupson X. It is the stack of
categories that assigns to each open setU the category Grp(X)(U) := Grp(U) of
sheaves of small groups onU. The restriction morphisms here are restrictions of
sheaves.
For any stack of groupoids P on X there is a functor of stacks AutP : P→
Grp(X), which is the geometrization of Deﬁnition 1.1(2). Like Proposition 1.3 we
have:
Proposition 1.13. Let P be a stack of crossed groupoids onX.
TWISTED DEFORMATION QUANTIZATION 15
(1) IG : P1→Grp(X) is a functor of stacks onX.
(2) ig : IG ⇒AutP1 is a natural transformation between functors of stacks
P1→Grp(X).
(3) The data (P1, P2, AdP1↷P2, D) can be recovered from the stack of groupoids
P1, the functor of stacksIG : P1→Grp(X) and the natural transformation
ig : IG⇒AutP1.
Proof. Again this is immediate from the deﬁnitions, but here the details are of
course much more complicated than in Proposition 1.3. It is good to look up [Ye4,
Section 2] for detailed deﬁnitions and notation. □
Example 1.14. This is the geometric version of Example 1.4. Suppose G is a
gerbe onX, and N is a normal subgroupoid onG, in the sense of [Ye4, Deﬁnition
3.6]. Then there is a stack of crossed groupoidsP on X, with P1 := G, P2 := N,
AdP1↷P2 := AdG|N, and D : P1→P2 is the inclusion.
Example 1.15. This is the geometric version of Example 1.5. On any open set
U⊂X we have the crossed groupoidGrp×(U), in which the objects are the sheaves
of groupsG onU; the1-morphisms are the isomorphisms of sheaves of groups; and
the 2-morphisms are the elements ofΓ(U,G). The twisting and feedback are as in
Example 1.5. AsU varies we obtain a stack of crossed groupoidsGrp×(X).
Example 1.16.This is the geometric version of Example 1.6. Take a commutative
ring R. For an open setU⊂X denote by Assoc(R,U ) the category of sheaves of
associativeR-algebras onU. AsU varies we getAssoc(R,X ), thestack of sheaves
of associativeR-algebras onX. Inside Assoc(R,X ) we have the stack of groupoids
Assoc×(R,U ), in which we take only the invertible morphisms. The latter can
be made into a stack of crossed groupoids by takingIG(A) := A×, the sheaf of
invertible elements.
