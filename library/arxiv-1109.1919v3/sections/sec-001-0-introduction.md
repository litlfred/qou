---
doc_id: arxiv-1109.1919v3
doc_title: "COMBINATORIAL DESCENT DATA FOR GERBES"
section_id: sec-001-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-5
source_pdf: 1109.1919v3.pdf
source_sha256: 2b634edddf232047
toc_source: outline
doc_brief: "COMBINATORIAL DESCENT DATA FOR GERBES — We consider descent data in cosimplicial crossed groupoids. This is a combinatorial abstraction of the descent data for gerbes in algebraic geom- etry."
---
For a cosimplicial crossed groupoid G = {Gp}p∈N we denote by Desc(G) the set
of gauge equivalence classes of descent data. The purpose of this note is to prove:
Theorem 0.1 (Equivalence). Let Φ : G →H be a weak equivalence between cosim-
plicial crossed groupoids. Then the function
Desc(Φ) : Desc(G) →Desc(H)
is bijective.
The various notions involved are recalled or deﬁned in Section 1. The theorem
is repeated as Theorem 2.4 in Section 2, and proved there. Connections with other
papers, and several remarks, are in Section 3.
Theorem 0.1 plays a crucial role in the new version of our paper [Ye1] on twisted
deformation quantization of algebraic varieties. This is explained in Remark 3.2.
Acknowledgments. I wish to thank Matan Prezma, Ronald Brown, Sharon Hol-
lander, Vladimir Hinich, Behrang Noohi and Lawrence Breen for useful discussions.
1. Combinatorial Descent Data
We begin with a quick review of cosimplicial theory. Let ∆denote the simplex
category. The set of objects of ∆is the set N of natural numbers. Given p, q ∈N,
the morphisms α : p →q in ∆are order preserving functions
α : {0, . . . , p} →{0, . . . , q}.
We denote this set of morphisms by ∆q
p. An element of ∆q
p may be thought of
as a sequence i = (i0, . . . , ip) of integers with 0 ≤i0 ≤· · · ≤ip ≤q. We call
∆q := {∆q
p}p∈N the q-dimensional combinatorial simplex, and an element i ∈∆q
p
is a p-dimensional face of ∆q.
Let C be some category. A cosimplicial object in C is a functor C : ∆→C.
We shall usually write Cp := C(p) ∈Ob(C), and leave the morphisms C(α) :
C(p) →C(q), for α ∈∆q
p, implicit. Thus we shall refer to the cosimplicial object
C as {Cp}p∈N. The category of cosimplicial objects in C, where the morphisms are
natural transformations of functors ∆→C, is denoted by ∆(C).
Date: 01 May 2014.
Key words and phrases. Cosimplicial crossed groupoids, descent, gerbes.
Mathematics Subject Classiﬁcation 2000. Primary: 18G50; Secondary: 18G30, 20L05.
This research was supported by the Israel Science Foundation.
1
arXiv:1109.1919v3  [math.KT]  1 May 2014
2
AMNON YEKUTIELI
If C is a category of sets with structure, then an object C ∈Ob(C) has elements
c ∈C. Let {Cp}p∈N be a cosimplicial object of C. Given a face i ∈∆q
p and an
element c ∈Cp, it will be convenient to write
(1.1)
ci := C(i)(c) ∈Cq.
The picture to keep in mind is of “the element c pushed to the face i of the simplex
∆q”. See Figure 1 for an illustration.
Let G be a groupoid. For objects x, y ∈Ob(G) we write G(x, y) := HomG(x, y),
the set of morphisms g : x →y. We also denote by G(x) := G(x, x) the automor-
phism group of x.
Suppose G1 and G2 are groupoids, such that Ob(G1) = Ob(G2). An action Ψ of
G1 on G2 is a collection of group isomorphisms Ψ(g) : G2(x)
≃
−→G2(y) for all x, y ∈
Ob(G1) and g ∈G1(x, y), such that Ψ(h ◦g) = Ψ(h) ◦Ψ(g) whenever g and h are
composable, and Ψ(1x) = 1G2(x). Here 1x ∈G1(x) is the the identity automorphism
of the object x in the groupoid G1, and 1G2(x) is the identity automorphism of the
group G2(x). The prototypical example is the adjoint action AdG1 of the groupoid
G1 on itself, namely
AdG1(g)(h) := g ◦h ◦g−1.
Deﬁnition 1.2. A crossed groupoid is a structure
G = (G1, G2, AdG1↷G2, D)
consisting of:
• Groupoids G1 and G2, such that G2 is totally disconnected, and Ob(G1) =
Ob(G2). We write Ob(G) := Ob(G1).
• An action AdG1↷G2 of G1 on G2, called the twisting.
• A morphism of groupoids (i.e. a functor) D : G2 →G1 called the feedback,
which is the identity on objects.
These are the conditions:
(i) The morphism D is G1-equivariant with respect to the actions AdG1↷G2
and AdG1. Namely
D(AdG1↷G2(g)(a)) = AdG1(g)(D(a))
in the group G1(y), for any x, y ∈Ob(G), g ∈G1(x, y) and a ∈G2(x).
(ii) For any x ∈Ob(G) and a ∈G2(x) there is equality
AdG1↷G2(D(a)) = AdG2(x)(a),
as automorphisms of the group G2(x).
We sometimes refer to the morphisms in the groupoid G1 as 1-morphisms, and
to the morphisms in G2 as 2-morphisms.
Remark 1.3. A crossed groupoid is better known as a strict 2-groupoid, or a
crossed module over a groupoid, or a 2-truncated crossed complex; see [Bw]. When
Ob(G) is a singleton then G is just a crossed module (or a crossed group). More
on this in Remark 3.3.
Deﬁnition 1.4. Suppose H = (H1, H2, AdH1↷H2, D) is another crossed groupoid.
A morphism of crossed groupoids Φ : G →H is a pair of morphisms of groupoids
Φi : Gi →Hi, i = 1, 2, that are equal on objects, and respect the twistings and the
feedbacks.
We denote by CrGrpd the category consisting of crossed groupoids and morphisms
between them.
COMBINATORIAL DESCENT DATA
3
We shall be interested in cosimplicial crossed groupoids, i.e. in objects of the
category ∆(CrGrpd). A cosimplicial crossed groupoid G = {Gp}p∈N has a crossed
groupoid Gp in each simplicial dimension p. The morphisms of crossed groupoids
G(i) : Gp →Gq, for i ∈∆q
p, are implicit, and we use notation (1.1) for objects,
1-morphisms and 2-morphisms.
Let us ﬁx p ∈N. Then for any x ∈Ob(Gp) there is a group homomorphism (the
feedback)
D : Gp
2(x) →Gp
1(x).
And for every morphism g : x →y in Gp
1 there is a group isomorphism (the twisting)
Ad(g) = AdGp
1↷Gp
2(g) : Gp
2(x) →Gp
2(y).
Note that we are using the expression Ad(g) to mean both AdGp
1↷Gp
2(g) and
AdGp
1(g); hopefully that will not cause confusion.
Deﬁnition 1.5. Let G = {Gp}p∈N be a cosimplicial crossed groupoid. A combina-
torial descent datum in G is a triple (x, g, a) of elements of the following sorts:
(0) x ∈Ob(G0).
(1) g ∈G1
1(x(0), x(1)), where x(0), x(1) ∈Ob(G1) are the objects corresponding
to the vertices (0) and (1) of ∆1.
(2) a ∈G2
2(x(0)), where x(0) ∈Ob(G2) is the object corresponding to the vertex
(0) of ∆2.
The conditions are as follows:
(i) (Failure of 1-cocycle)
g−1
(0,2) ◦g(1,2) ◦g(0,1) = D(a)
in the group G2
1(x(0)). Here x(i) ∈Ob(G2) and g(i,j) ∈G2
1(x(i), x(j)) corre-
spond to the faces (i) and (i, j) respectively of ∆2.
(ii) (Twisted 2-cocycle)
a−1
(0,1,3) ◦a(0,2,3) ◦a(0,1,2) = Ad(g−1
(0,1))(a(1,2,3))
in the group G3
2(x(0)).
Here x(i) ∈Ob(G3), g(i,j) ∈G3
1(x(i), x(j)) and
a(i,j,k) ∈G3
2(x(i)) correspond to the faces (i), (i, j) and (i, j, k) respectively
of ∆3.
We denote by Desc(G) the set of all descent data in G.
See Figure 1 for an illustration.
Deﬁnition 1.6. Let (x, g, a) and (x′, g′, a′) be descent data in the cosimplicial
crossed groupoid G. A gauge transformation (x, g, a) →(x′, g′, a′) is a pair (f, c)
of elements of the following sorts:
(0) f ∈G0
1(x, x′).
(1) c ∈G1
2(x(0)), where x(0) ∈Ob(G1) is the object corresponding to the vertex
(0) of ∆1.
These two conditions must hold:
(i)
g′ = f(1) ◦g ◦D(c) ◦f −1
(0)
in the set G1
1(x′
(0), x′
(1)).
(ii)
a′ = Ad(f(0))

c−1
(0,2) ◦a ◦Ad(g−1
(0,1))(c(1,2)) ◦c(0,1)

in the group G2
2(x′
(0)).
4
AMNON YEKUTIELI
Figure 1. Illustration of a combinatorial descent datum (x, g, a)
in the cosimplicial crossed groupoid G = {Gp}p∈N.
Figure
2. Illustration
of
a
gauge
transformation
(f, c)
:
(x, g, a) →(x′, g′, a′) between descent data.
This is illustrated in Figure 2.
Proposition 1.7. Let G be a cosimplicial crossed groupoid. The gauge transfor-
mations form an equivalence relation on the set Desc(G).
We call this relation gauge equivalence. Actually Desc(G) has a lot more struc-
ture; see Remark 3.5.
Proof. Given a descent datum (x, g, a), the pair (1x, 1x(0)), where 1x ∈G0
1(x) and
1x(0) ∈G1
2(x(0)) are the identity elements of these groups, is a gauge transformation
from (x, g, a) to itself. Next let
(f, c) : (x, g, a) →(x′, g′, a′)
and
(f ′, c′) : (x′, g′, a′) →(x′′, g′′, a′′)
COMBINATORIAL DESCENT DATA
5
be gauge transformations between descent data. Then
 f ′ ◦f , c ◦f −1
(0) (c′)

: (x, g, a) →(x′′, g′′, a′′)
is a gauge transformation. And
 f −1, f(0)(c−1)

: (x′, g′, a′) →(x, g, a)
is a gauge transformation.
□
Let Φ : G →H be a morphism of cosimplicial crossed groupoids. Given a descent
datum (x, g, a) ∈Desc(G), the triple
Φ(x, g, a) := (Φ(x), Φ(g), Φ(a))
is a descent datum in H. The resulting function
Desc(Φ) : Desc(G) →Desc(H)
respects the gauge equivalence relations.
Deﬁnition 1.8. For a cosimplicial crossed groupoid G we write
Desc(G) :=
Desc(G)
gauge equivalence.
For a morphism Φ : G →H of cosimplicial crossed groupoids, we denote by
Desc(Φ) : Desc(G) →Desc(H)
the induced function.
