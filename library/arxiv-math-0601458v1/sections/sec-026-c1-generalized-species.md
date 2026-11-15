---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS"
section_id: sec-026-c1-generalized-species
section_title: "C.1. Generalized Species"
section_number: null
pages: 66-68
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
toc_source: outline
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS — Interest in combinatorial interpretations of mathematical entities stems from the convenience of the concrete models they provide."
---
Fiore, Gambino, and Hyland [7] sheds some light on the choice of categories we
have made in deﬁning structure types. In that paper, conventional structure types
are referred to as species, and a generalization is developed to (G,
H)-species for
arbitrary small groupoids
G and
H, which provides, for ﬁnite sequences of
G-
objects, an
H-variable set of structures over them. Structure types are then (1, 1)-
species, where 1 is the groupoid with one object and identity morphism.
To explain this generalization, we need some terminology.
Deﬁnition 39. Suppose
G is a small groupoid. Then !G, the free symmetric
monoidal completion of
G, is the smallest symmetric monoidal groupoid con-
taining
G. We deﬁne b
G, the free cocompletion of
G is the smallest cocomplete
category containing
G.
Now, we can make an analogy between the creation of a 2-rig from a category
using these constructions and the creation of a rig from a set using the operation
of taking a free abelian group on a set, and the operation of taking the free monoid
on a set. If we start with a set of generators S, and then take the free Abelian
group on S,
Z[S], and then take the free monoid on
Z[S], we get a rig, and this
is isomorphic to the rig we get if we take these freely generated structures in the
reverse order. In particular, if S = φ, the rig we get is
N, if S = {x}, we get
N[x], the free rig on one generator, and so on. A similar construction is possible
for groupoids (and indeed categories).
To see how this applies to species, we ﬁrst note that the free symmetric monoidal
completion of a groupoid consists of “families” of
G-objects, whose objects are
tuples of objects from
G and whose morphisms are braids between tuples, with
strands labelled by morphisms of
G. So in particular, if
G is the groupoid 1, with
one object and only the identity morphism, we ﬁnd that !G ∼= FinSet0. Moreover,
the free cocompletion of
G is equivalent to the functor category hom(Gop, Set) of
presheaves on
G (see, for instance, MacLane & Moerdijk [14], I.5, Prop 1). So
in particular, since
G is a groupoid, and equivalent to its opposite, we have that
c
!G ∼= hom(!G, Set).
In the case where
G = 1, we have c
!G ∼= hom(FinSet0, Set) = Set[Z]. So the
2-rig of structure types can be seen as the freely generated 2-rig on one generator.
We may think of this generator as being the basic “object”, or “one-element set”.
The ﬁrst natural extension to consider is when
G = n, the groupoid with n objects
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS
67
having only the identity morphisms. The 2-rig b!n is also called Set[Z1, . . . , Zn],
and gives what are called multisort species. These can be described as 2-rigs of
structures which can be put on sets of elements of n diﬀerent sorts.
For other
groupoids
G, we get diﬀerent notions of species, many of which appear in various
contexts in the literature, for instance ([3]).
The generalization of species considered by Fiore, Gambino, and Hyland [7] is
the 2-rig hom(!G, b
H), for
Gand
H some small groupoids. The various examples of
G-species mentioned above are all seen as functors into Set = ˆ1, so
H = 1. The
2-rig hom(!G, b
H) is, in particular, the category of functors from !G, the category
of families of
G-objects to ˆ
H, the category of
H-variable sets - presheaves over
H.
Indeed, it is possible to deﬁne a 2-category of species between groupoids. In
this setting, the category of functors from families of
G-objects into
H-variable sets
plays the role of hom(G,
H), and the objects in the 2-category are small groupoids.
68
JEFFREY MORTON
