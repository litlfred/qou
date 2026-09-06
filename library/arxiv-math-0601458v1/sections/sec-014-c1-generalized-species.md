---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS JEFFREY MORTON"
section_id: sec-014-c1-generalized-species
section_title: "C.1. Generalized Species"
section_number: null
pages: 66-68
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS JEFFREY MORTON — Interest in combinatorial interpretations of mathematica l entities stems from the convenience of the concrete models they provi de."
---
Fiore, Gambino, and Hyland [7] sheds some light on the choice of categ ories we
have made in deﬁning structure types. In that paper, convention al structure types
are referred to as species, and a generalization is developed to ( /BZ , /C0 )-species for
arbitrary small groupoids /BZ and /C0 , which provides, for ﬁnite sequences of /BZ -
objects, an /C0 -variable set of structures over them. Structure types are then ( 1, 1)-
species, where 1 is the groupoid with one object and identity morphism.
To explain this generalization, we need some terminology.
Deﬁnition 39. Suppose /BZ is a small groupoid. Then !/BZ , the free symmetric
monoidal completion of /BZ , is the smallest symmetric monoidal groupoid con-
taining /BZ . We deﬁne ˆ
/BZ , the free cocompletion of /BZ is the smallest cocomplete
category containing /BZ .
Now, we can make an analogy between the creation of a 2-rig from a c ategory
using these constructions and the creation of a rig from a set using the operation
of taking a free abelian group on a set, and the operation of taking t he free monoid
on a set. If we start with a set of generators S, and then take the free Abelian
group on S, /CI [S], and then take the free monoid on /CI [S], we get a rig, and this
is isomorphic to the rig we get if we take these freely generated stru ctures in the
reverse order. In particular, if S = φ, the rig we get is /C6 , if S ={x}, we get
/C6 [x], the free rig on one generator, and so on. A similar construction is p ossible
for groupoids (and indeed categories).
To see how this applies to species, we ﬁrst note that the free symme tric monoidal
completion of a groupoid consists of “families” of /BZ -objects, whose objects are
tuples of objects from /BZ and whose morphisms are braids between tuples, with
strands labelled by morphisms of /BZ . So in particular, if /BZ is the groupoid 1, with
one object and only the identity morphism, we ﬁnd that ! /BZ
∼= FinSet0. Moreover,
the free cocompletion of /BZ is equivalent to the functor category hom( /BZ
op, Set) of
presheaves on /BZ (see, for instance, MacLane & Moerdijk [14], I.5, Prop 1). So
in particular, since /BZ is a groupoid, and equivalent to its opposite, we have that
ˆ!/BZ
∼= hom(!/BZ , Set).
In the case where /BZ = 1, we have ˆ!/BZ
∼= hom(FinSet0, Set) = Set[Z]. So the
2-rig of structure types can be seen as the freely generated 2-r ig on one generator.
We may think of this generator as being the basic “object”, or “one -element set”.
The ﬁrst natural extension to consider is when /BZ = n, the groupoid with n objects
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 67
having only the identity morphisms. The 2-rig ˆ!n is also called Set[Z1, . . . ,Zn],
and gives what are called multisort species . These can be described as 2-rigs of
structures which can be put on sets of elements of n diﬀerent sorts. For other
groupoids /BZ , we get diﬀerent notions of species, many of which appear in various
contexts in the literature, for instance ([3]).
The generalization of species considered by Fiore, Gambino, and Hyla nd [7] is
the 2-rig hom(! /BZ ,ˆ
/C0 ), for /BZ and /C0 some small groupoids. The various examples of
/BZ -species mentioned above are all seen as functors into Set = ˆ1, so /C0 = 1. The
2-rig hom(! /BZ ,ˆ
/C0 ) is, in particular, the category of functors from ! /BZ , the category
of families of /BZ -objects to ˆ
/C0 , the category of /C0 -variable sets - presheaves over /C0 .
Indeed, it is possible to deﬁne a 2-category of species between gro upoids. In
this setting, the category of functors from families of /BZ -objects into /C0 -variable sets
plays the role of hom( /BZ , /C0 ), and the objects in the 2-category are small groupoids.
68 JEFFREY MORTON
