---
doc_id: 1-s20-s000187089891800x-main
doc_title: "Spherical Categories"
section_id: sec-001-1-monoidal-categories-with-duals
section_title: "MONOIDAL CATEGORIES WITH DUALS"
section_number: 1
pages: 2-9
source_pdf: 1-s2.0-S000187089891800X-main.pdf
source_sha256: 9844f124dcbc7f36
toc_source: outline
doc_brief: "Spherical Categories — 7 sections: Front matter; INTRODUCTION; MONOIDAL CATEGORIES WITH DUALS"
---
In this section we study monoidal categories with duals. Examples are
finitely generated free modules over a commutative ring. In these examples
the tensor product is commutative, but we do not require this. The
motivating examples of monoidal categories with duals are the categories
of representations of Hopf algebras. These categories have a contravariant
functor given by the contragradient dual but are not categories with duals,
in general, as we require that each object be reflexive.
The only result in this section is a coherence theorem. The proof follows
the coherence theorem for monoidal categories in [7]. The definition of
coherence involves an infinite set of diagrams. A coherence theorem gives
a finite set of conditions for coherence to hold.
In the following definition it is convenient to regard the distinguished
object e as a functor from the category with one morphism to C. Then *
and \ can be defined to be natural transformations.
Definition 1.1.
A monoidal category is a category, C, together with a
functor  : C_C C, an object e, and natural transformations
:: ( _1)  (1_ )
*: e1
 1
\: 1e
 1
Each component of each of the natural transformations :, * and \ is
required to be an isomorphism. These data are also required to be coherent
which is equivalent to requiring that : satisfy the pentagon identity and
that \ and * satisfy a triangular identity. Also, \(e)=*(e) : ee  e. These
conditions are given in [8].
If each component of the natural transformations :, *, and \ is the iden-
tity map then the category is called strict monoidal.
If C is a category, then the opposite category C & is the category
obtained
by
reversing
morphisms.
If
F: C D
is
a
functor,
then
F&: C &  D& is the corresponding functor on the opposites. A functor
C&  D is the same as a contravariant functor C D.
Definition 1.2.
Let (C, , e, :, *, \) be a monoidal category. Then the
data needed to make this a category with duals is a functor, V: C&  C,
and natural transformations
(1)
{: 1  VV,
(2)
#: (V_V) b    op b V
and an isomorphism &: e  eV.
Each component of the natural transformations { and # is required to be
an isomorphism. A category with data satisfying these conditions is called
a category with dual data.
Definition 1.3.
A category with dual data is strict if each component
of the natural transformations # and { is the identity map and the map &
is the identity map. In this case the category is called a category with strict
dual data.
In the following definition, if :=(\, \, ..., \) is an n-tuple of signs,
then C: denotes the category C\_C\_ } } } _C\, with C+#C. Also, if 0
is the 0-tuple, then C0 is the category with one morphism, so that
e: C0  C.
It is convenient to regard & as a natural transformation from the functor
e to the functor e& b V.
Definition 1.4.
The set of iterates of the functors , V, and e is the
smallest set of functors F: C: C which satisfies the following conditions:
(1)
The functor e: C0  C is an iterate.
(2)
The identity functor 1: C  C is an iterate.
(3)
If F and G are iterates then the functor FG=F_Gb  is an
iterate.
(4)
If F is an iterate then F*=F & b V is an iterate.
The length of : is called the multiplicity of the iterated functor. There is a
category with objects the set of all iterates of , V, and e and morphisms
all natural transformations.
Definition 1.5.
Let F, G, and H be any three iterated functors. Then
we have natural transformations
:: (FG)H  F (GH)
*: eF  F
\: Fe  F
#: (F*) (G*)  (GF)*
{: F  F**
&: e  e*
Each of these is an isomorphism. Each of these and their inverses are called
instances. More particularly, the first one, for example, is called an instance
of :, and its inverse an instance of the inverse of :.
Definition 1.6.
The set of expansions is the smallest subset of the set
of natural transformations which satisfies the following:
(1)
The identity functor, 1, is an expansion.
(2)
Any instance is an expansion.
(3)
If ; is an expansion then ;1 and 1; are expansions.
(4)
If ; is an expansion then ;* is an expansion.
The smallest set which satisfies all but the last condition is the set of
reduced expansions.
Definition 1.7.
The smallest subcategory which contains instances and
which is closed under  and V is equal to the smallest subcategory which
contains expansions. This is called the category of iterates and any
morphism in this category is called an iterated natural transformation.
The smallest subcategory of the category of iterates which contains
instances and which is closed under  is equal to the smallest subcategory
of the category of iterates which contains reduced expansions. Any mor-
phism in this category is called a reduced iterated natural transformation.
Definition 1.8.
Since every expansion is an isomorphism and the
inverse of any expansion is an expansion it follows that every iterated
natural transformation is an isomorphism and that every inverse of an
iterated natural transformation is an iterated natural transformation. The
category C with dual data is coherent if any two iterated natural transfor-
mations between the same two iterated functors are equal. Equivalently,
the dual data is coherent if any diagram with vertices iterated functors and
arrows expansions commutes.
A category with dual data which is coherent is called a category with
duals.
The following is a coherence theorem, in the sense that this is a finite set
of conditions on the data which are necessary and sufficient for the data to
be coherent.
Theorem 1.9.
A category C with dual data is coherent if, and only if, the
following conditions are satisfied:
(1)
{(e) is the composite
e w
&
e* ww
&*&1
e**.
(2)
For each object c, {(c*) and {(c)* are inverse isomorphisms.
(3)
For any object a, the following diagram commutes
\(a*)
#(a, e)
a*e ww
1 &
a*e*
a*
ww
**(a)
(ea)*
(4)
For any object a, the following diagram commutes
*(a*)
#(e, a)
e}a* ww
v 1
e*a*
a*
ww
\*(a)
(ae)*
(5)
For all objects a, b, and c, the following diagram commutes
:(c*, b*, a*)
:*(a, b, c)
(c*b*)a* www
#(c, b)1
(bc)*a* www
#(bc, a) (a (bc))*
c*(b*a*) wwww
1#(b, a)
c*(ab)* www
#(c, ab) ((ab)c)*
(6)
For all objects a and b the following diagram commutes
{(a) {(b)
#*(b, a)
ab
www
{(ab)
(ab)**
a**b** www
#(a*, b*)
(b*a*)*
Note that the following diagram shows that {(a)**={(a**) for any
object a follows from the condition that { is a natural transformation with
each component an isomorphism.
{(a)
{**(a)
a ww
{(a)
a**
a** ww
{(a**) a****
This is implied by condition (2) but not conversely.
It is trivial that if the natural transformations are coherent then each of
these diagrams commutes. It remains to prove the converse.
Lemma 1.10.
Any iterated natural transformation is equal to a reduced
iterated natural transformation.
Proof.
There are six natural transformations :, *, \, #, { and & and six
conditions above. Furthermore each condition has exactly one instance
which is not reduced and for each natural transformation there is exactly
one condition which contains an instance of that natural transformation
which is not reduced. Hence, by applications of these diagrams and their
images by V, any instance is equal to a reduced iterated natural transforma-
tion and it follows that any iterated natural transformation is equal to a
reduced iterated natural transformation.
This shows that it is sufficient to prove the coherence theorem for
reduced iterated natural transformations. Any reduced iterate of (:, *, \)
and their inverses is called a central iterate. Mac Lane proves the coherence
theorem for central iterates in [7].
Lemma 1.11.
Any expansion of an instance of #, {, or & (but not their
inverses) composed with a central iterate is equal to a central iterate com-
posed with an expansion of an instance of #, {, or &.
Proof.
This follows from the condition that the central iterate is a
natural transformation and that each component of the expansion is a
morphism. The commutative square which contains both of these provides
the proof. An example is provided by the following commutative diagram:
(#(F, G)1H)1J
#(F, G)1HJ
((F*G*)H)J wwwww
:(F*G, H, J)
(F*G*) (HJ)
((GF )*H)J wwwwww
:((GF )*, H, J)
(GF)* (HJ)
Definition 1.12.
The set of standard iterated functors is the smallest
set of iterated functors which satisfies:
(1)
The iterates e, 1, and V are standard.
(2)
If F {e is standard then F 1 and F V are standard.
Definition 1.13.
The set of reduced iterated functors is the smallest set
of iterated functors which satisfies:
(1)
The iterates e, 1, and V are reduced.
(2)
If F and G are reduced then F G is reduced.
Define two iterated functors, F and G, to be equivalent if there is an
iterated natural transformation from F to G. This is obviously an equiv-
alence relation.
Definition 1.14.
The rank r and luminosity, l, of an iterated functor
are defined recursively as follows:
(1)
r(e)=1 and r(1)=1
(2)
r(FG)=r(F)+r(G)+1
(3)
r(F*)=r(F ).
(1)
l(e)=0 and l(1)=0
(2)
l(FG)=l(F)+l(G)
(3)
l(F*)=l(F )+r(F ).
The rank is a modified multiplicity, and the luminosity is a measure of
the number of stars. The luminosity is unaffected by central iterated natural
transformations, but is increased by instances of #, {, and &.
Lemma 1.15.
For any iterated functor F, there is a unique reduced
iterated functor R and a unique natural transformation R  F which is an
iterate of instances of #, {, and &.
Proof.
The proof is by induction on the sum of the luminosity and the
rank of F. Any iterated functor is of the form
(1)
F**,
(2)
(FG)*,
(3)
e*,
(4)
FG,
(5)
1, V, or e;
and the only instances of #, {, and & which have these as range are
(1)
{: F  F**
(2)
#: (G*) (F*)  (FG)*
(3)
&: e  e*
(4)
A1 or 1B
(5)
none.
In the first three cases, the conclusion follows from the induction
hypothesis applied to the domain of the natural transformation, which has
the same rank and lower luminosity. In (4), the induction hypothesis can
be applied to F and G separately, which have lower rank and luminosity
which is no greater. The conclusion follows as the natural transformations
A1 and 1B commute. The functors in (5) are reduced iterated
functors, and F=R.
The proof of the coherence theorem [1.9] now follows. It is only
necessary to consider reduced iterated natural transformations. A reduced
iterated natural transformation is said to be directed if it is the product of
instances which do not include the inverses of (#, {, &). By the preceding
Lemma [1.15], each iterated functor is equivalent to a reduced iterated
functor, and hence to a standard iterated functor, by a directed natural
transformation.
By a standard argument (see [7]), it is sufficient to prove the coherence
result for directed natural transformations between an iterated functor F
and a standard iterated functor S. According to Lemma 1.11, any directed
natural transformation S  F can be written as a central iterate S R
followed by an iterate of instances of (#, {, &): R F. By Lemma 1.15, R
and the second natural transformation are unique, while the first natural
transformation is unique by the coherence of central iterates.
Definition 1.16.
If C is a category with duals then define the category
PC to have objects of the form (F, [a1, ..., an]) where F is a standard
iterated functor of multiplicity n and each ai is an object of C. The set of
morphisms from (F,[a1, ..., an]) to (G, [a1, ..., am]) is the set of morphisms
in C from F(a1, ..., an) to G(a1, ..., am).
There is a functor i: C  PC defined on objects by a [ (1, a). There is
also
a
functor
?: PC C
defined
on
objects
by
(F,[a1, ..., an]) [
F(a1, ..., an). It is trivial that the composite i b ? is the identity functor of C.
It is also clear that there is a canonical natural transformation from ? b i to
the identity functor of PC. Hence the categories PC and C are canonically
equivalent.
The coherence theorem implies that the category PC is a strict monoidal
category with strict duals. The functor i has the universal property that if
D is a strict monoidal category with strict duals and F: C D is a functor
of monoidal
categories with duals
then there is
a unique functor
G: PC  D of strict monoidal categories with strict duals such that
F=i bG.
