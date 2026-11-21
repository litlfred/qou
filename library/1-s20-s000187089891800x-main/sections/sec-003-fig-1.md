---
doc_id: 1-s20-s000187089891800x-main
doc_title: "Spherical Categories"
section_id: sec-003-fig-1
section_title: "FIG. 1"
section_number: null
pages: 10-14
source_pdf: 1-s2.0-S000187089891800X-main.pdf
source_sha256: 9844f124dcbc7f36
toc_source: outline
doc_brief: "Spherical Categories — 7 sections: Front matter; INTRODUCTION; MONOIDAL CATEGORIES WITH DUALS"
---
to the left. This isotopy moves the loop in Fig. 1 past the point at infinity.
Taken together with planar isotopies, such an operation on planar graphs
generates all the isotopies on the sphere. It follows that the evaluation in
a spherical category of a closed graph with labelled edges and with a dis-
tinguished edge at each vertex is invariant under isotopies of the sphere S 2.
Definition 2.1.
A pivotal category is a category with duals together
with a morphism =(c): e  cc* for each object c # C.
The conditions on the components of = are the following:
(1)
For all morphisms, f : a  b, the following diagram commutes
=(b)
f1
e
ww
=(a)
aa*
bb* ww
1f * ba*
(2)
For all objects a, the following composite is the identity map
of a*:
a* ww
*&1(a*) ea* www
=(a*)1
(a*a**)a* wwww
:(a*, a**, a*) a* (a**a*)
wwww
1#(a*, a)
a* (aa*)* www
1=(a)* a*e* ww
1 &&1 a*e ww
\(a*)
a*
(3)
For all objects a and b the following composite is required to be
=(ab):
e ww
=(a)
aa* wwww
1*&1(a*)
a (ea*)
wwww
1 (=(b)1) a ((bb*)a*) wwwww
1 :(b, b*, a*)
a(b (b*a*))
wwwwww
:&1(a, b, b*a*)
(ab) (b*a*) www
1 #(b, a) (ab) (ab)*
FIGURE 1
These conditions imply that the strict extension is a pivotal category in
the sense of [3]. This is clear once it has been shown that = is well- defined
on the strict extension.
The functor V and the maps = are not independent. The maps = deter-
mine V. This observation is in [5] where the maps = are taken as more
fundamental than V. In [12] it is noted that the maps = also determine #.
Lemma 2.2.
In any pivotal category, for any morphism f: a  b the
following composite is f*:
b* www
\&1(b*)
b*e www
1=(a)
b* (aa*) wwww
1 ( f1)
b* (ba*)
wwwww
:&1(b*, b, a*)
(b*b)a* wwwww
({(b*) {(b))1 (b***b**)a
wwww
#(b**, b*)1 (b*b**)*a*wwww
=*(b*)1
e*a* ww
&&11 ea* ww
*(a*) a*
Proof.
This follows directly from conditions (1) and (2) of the preced-
ing definition.
Remark 2.3.
Note also that a pivotal category is closed, in the sense
that there are natural isomorphisms, for all a, b, and c;
Hom(ab, c)$Hom(b, a*c),
Hom(a, bc)$Hom(ac*, b)
Hom(ab, c)$Hom(a, cb*),
Hom(a, bc)$Hom(b*a, c).
Definition 2.4.
Let a be any object in a pivotal category. Then the
monoid End(a) has two trace maps, trL, trR: End(a)  End(e). In a pivotal
category trL( f ) is defined to be the composite
e ww
=(a*)
a*a** wwww
1 {&1(a)
a*a ww
1f
a*a wwww
{(a*) {(a)
a***a** wwww
#(a**, a*)
(a*a**)* www
=*(a*)
e* w
&
e
and trR( f ) is defined to be the composite
e ww
=(a)
aa* ww
f1
aa* www
{(a)1
a**a* www
#(a*, a)
(aa*)* ww
=*(a)
e* w
&
e.
In a strict pivotal category these definitions simplify to
trL( f )==(a*)(1f ) =(a*)*
trR( f )==(a)( f1) =(a)*
These are called trace maps because they satisfy trL( fg)=trL(g f ) and
trR( fg)=trR(g f ).
Definition 2.5.
A pivotal category is spherical if, for all objects a and
all morphisms f: a  a,
trL( f )=trR( f ).
An equivalent condition is that trL( f )=trL( f *), for all f : a  a. Also, in
a spherical category, trL( fg)=trL( f ) } trL(g) (where the product is in
End(e)) for all f : a  a and all g: b b.
In the rest of this paper we study additive spherical categories. This
means that each Hom set is a finitely generated abelian group; and that the
data defining the spherical structure is compatible with the additive
structure. This means that  is Z-bilinear, that V is Z-linear, and all com-
ponents of all the natural transformations in the pivotal data are multi-
linear over Z.
In any additive monoidal category End(e) is a commutative ring (see
[5]) and we denote this ring by F. In particular the trace map, trL, takes
values in this ring. It follows that an additive monoidal category is F-linear,
by using the structure maps of * and \, and that if the category is pivotal
then the data defining the pivotal structure is F-linear.
The main examples of additive spherical categories arise as the category
of representations of a Hopf algebra with some additional structure. This
is discussed in detail in the next section.
Example 2.6.
An example of an additive spherical category which can-
not be regarded as a category whose objects are finitely generated free
modules is given by taking the free Z[q, q&1, z]-linear category on the
category of
oriented tangles
and then taking the
quotient by the
well-known skein relation for the HOMFLY polynomial. This is an
additive spherical category and for each pair of objects a and b, Hom(a, b)
is a finitely generated free Z[q, q&1, z]-module. However, the objects can-
not be taken to be finitely generated modules unless z is a quantum integer.
Definition 2.7.
For any two objects a and b there is a bilinear pairing
3: Hom(a, b)_Hom(b, a)  F
defined by 3( f, g)=trL( fg)=trL(g f ).
Definition 2.8.
A spherical category is non-degenerate if, for all
objects a and b, the pairing 3 is non-degenerate.
The next theorem shows that every additive spherical category has a
natural quotient which is a non-degenerate spherical category. This con-
struction is mentioned in [12].
Theorem 2.9.
Let C be an additive spherical category. Define the sub-
category J to have the same set of objects and morphisms defined by
HomJ(c1, c2)=[ f # HomC(c1, c2) : trL( fg)=0 for all g # HomC(c2, c1)].
Then CJ is a non-degenerate additive spherical category.
Proof.
It is clear that J is closed under composition on either side by
arbitrary morphisms in C. Hence the quotient is an additive category. It is
also clear that f # J if and only if f * # J and so the functor V is well
defined on the quotient. The functor  is well -defined on the quotient
since f # J implies fg1 # J and g2 f # J for arbitrary morphisms in C.
This follows from the observation that trL(( fg)h) can always be written
as trL( f h$) for a morphism h$, which can be constructed from g and h.1
The structure maps of the natural transformations :, *, \, #, &, { and the
morphisms =(a) are taken to be the images in the quotient of the given
morphisms in C. The conditions on this structure which imply that this
quotient is spherical follow from the same conditions in C.
Each pairing 3 is non-degenerate by construction.
1 We thank Marco Mackaay for pointing out that this argument was given incorrectly in
[13].
