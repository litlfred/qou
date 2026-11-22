---
doc_id: arxiv-quant-ph-0606114v3
doc_title: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation"
section_id: sec-016-5-quantum-topology-cobordism-categories-temperle
section_title: "Quantum Topology, Cobordism Categories, Temperley-Lieb Algebra and Topological Quantum Field Theory"
section_number: 5
pages: 29-33
source_pdf: 0606114v3.pdf
source_sha256: a8e08c457b65c728
toc_source: inferred
doc_brief: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation — We review the q-deformed spin network approach to Topological Quantum Field Theory and apply these methods"
---
Temperley-Lieb Algebra and Topological Quan-
tum Field Theory
The purpose of this section is to discuss the general idea behind topological
quantum ﬁeld theory, and to illustrate its application to basic quantum me-
chanics and quantum mechanical formalism. It is useful in this regard to have
available the concept of category, and we shall begin the section by discussing
this far-reaching mathematical concept.
Deﬁnition. A category Cat consists in two related collections:
1. Obj(Cat), the objects of Cat, and
2. Morph(Cat), the morphisms of Cat.
satisfying the following axioms:
1. Each morphism f is associated to two objects of Cat, the domain of f
and the codomain of f. Letting A denote the domain of f and B denote
the codomain of f, it is customary to denote the morphism f by the
arrow notation f : A −→B.
2. Given f : A −→B and g : B −→C where A, B and C are objects of
Cat, then there exists an associated morphism g ◦f : A −→C called the
composition of f and g.
3. To each object A of Cat there is a unique identity morphism 1A : A −→A
such that 1A◦f = f for any morphism f with codomain A, and g◦1A = g
for any morphism g with domain A.
4. Given three morphisms f : A −→B, g : B −→C and h : C −→D, then
composition is associative. That is
(h ◦g) ◦f = h ◦(g ◦f).
If Cat1 and Cat2 are two categories, then a functor F : Cat1 −→Cat2 consists
in functions FO : Obj(Cat1) −→Obj(Cat2) and FM : Morph(Cat1) −→
Morph(Cat2) such that identity morphisms and composition of morphisms
are preserved under these mappings. That is (writing just F for FO and FM),
1. F(1A) = 1F (A),
2. F(f : A −→B) = F(f) : F(A) −→F(B),
3. F(g ◦f) = F(g) ◦F(f).
A functor F : Cat1 −→Cat2 is a structure preserving mapping from one
category to another. It is often convenient to think of the image of the functor
F as an interpretation of the ﬁrst category in terms of the second. We shall
use this terminology below and sometimes refer to an interpretation without
specifying all the details of the functor that describes it.
The notion of category is a broad mathematical concept, encompassing
many ﬁelds of mathematics.
Thus one has the category of sets where the
objects are sets (collections) and the morphisms are mappings between sets.
One has the category of topological spaces where the objects are spaces and
the morphisms are continuous mappings of topological spaces. One has the
category of groups where the objects are groups and the morphisms are homo-
morphisms of groups. Functors are structure preserving mappings from one
category to another. For example, the fundamental group is a functor from
the category of topological spaces with base point, to the category of groups.
In all the examples mentioned so far, the morphisms in the category are re-
strictions of mappings in the category of sets, but this is not necessarily the
case. For example, any group G can be regarded as a category, Cat(G), with
one object ∗. The morphisms from ∗to itself are the elements of the group
and composition is group multiplication. In this example, the object has no
internal structure and all the complexity of the category is in the morphisms.
The Artin braid group Bn can be regarded as a category whose single
object is an ordered row of points [n] = {1, 2, 3, ..., n}. The morphisms are the
braids themselves and composition is the multiplication of the braids. The
ordered row of points is interpreted as the starting and ending row of points
at the bottom and the top of the braid. In the case of the braid category,
the morphisms have both external and internal structure.
Each morphism
produces a permutation of the ordered row of points (corresponding to the
begiinning and ending points of the individual braid strands), and weaving of
the braid is extra structure beyond the object that is its domain and codomain.
Finally, for this example, we can take all the braid groups Bn (n a positive
integer) under the wing of a single category, Cat(B), whose objects are all
ordered rows of points [n], and whose morphisms are of the form b : [n] −→[n]
where b is a braid in Bn. The reader may wish to have morphisms between
objects with diﬀerent n.
We will have this shortly in the Temperley-Lieb
category and in the category of tangles.
The n-Cobordism Category, Cob[n], has as its objects smooth manifolds of
dimension n, and as its morphisms, smooth manifolds Mn+1 of dimension n+1
with a partition of the boundary, ∂Mn+1, into two collections of n-manifolds
that we denote by L(Mn+1) and R(Mn+1). We regard Mn+1 as a morphism
from L(Mn+1) to R(Mn+1)
Mn+1 : L(Mn+1) −→R(Mn+1).
As we shall see, these cobordism categories are highly signiﬁcant for quantum
mechanics, and the simplest one, Cob[0] is directly related to the Dirac notation
of bras and kets and to the Temperley-Lieb algebara. We shall concentrate
in this section on these cobordism categories, and their relationships with
quantum mechanics.
One can choose to consider either oriented or non-oriented manifolds, and
within unoriented manifolds there are those that are orientable and those that
are not orientable. In this section we will implicitly discuss only orientable
manifolds, but we shall not specify an orientation. In the next section, with
the standard deﬁnition of topological quantum ﬁeld theory, the manifolds will
be oriented. The deﬁnitions of the cobordism categories for oriented manifolds
go over mutatis mutandis.
Lets begin with Cob[0]. Zero dimensional manifolds are just collections
of points. The simplest zero dimensional manifold is a single point p. We
take p to be an object of this category and also ∗, where ∗denotes the empty
manifold (i.e. the empty set in the category of manifolds). The object ∗occurs
in Cob[n] for every n, since it is possible that either the left set or the right set
of a morphism is empty. A line segment S with boundary points p and q is a
morphism from p to q.
S : p −→q
See Figure 10. In this ﬁgure we have illustrated the morphism from p to p.
The simplest convention for this category is to take this morphism to be the
identity. Thus if we look at the subcategory of Cob[0] whose only object is p,
then the only morphism is the identity morphism. Two points occur as the
boundary of an interval. The reader will note that Cob[0] and the usual arrow
notation for morphisms are very closely related. This is a place where notation
and mathematical structure share common elements. In general the objects of
Cob[0] consist in the empty object ∗and non-empty rows of points, symbolized
by
p ⊗p ⊗· · · ⊗p ⊗p.
Figure 10 also contains a morphism
p ⊗p −→∗
and the morphism
∗−→p ⊗p.
The ﬁrst represents a cobordism of two points to the empty set (via the bound-
ing curved interval). The second represents a cobordism from the empty set
to two points.
