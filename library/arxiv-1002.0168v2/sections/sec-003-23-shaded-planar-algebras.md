---
doc_id: arxiv-1002.0168v2
doc_title: "Non-cyclotomic fusion categories Scott Morrison Noah Snyder"
section_id: sec-003-23-shaded-planar-algebras
section_title: "Shaded planar algebras"
section_number: 2.3
pages: 6-9
source_pdf: 1002.0168v2.pdf
source_sha256: c95d5d193d57b097
doc_brief: "Non-cyclotomic fusion categories Scott Morrison Noah Snyder — Etingof, Nikshych and Ostrik ask in [ 7,§2] if every fusion category can be completely deﬁned over a cyclotomic ﬁeld."
---
One of the main tools for understanding monoidal categories (and more generally
2-categories) is the diagram calculus (pioneered by Penrose [ 21], Joyal-Street [16],
Reshetikhin-Turaev [24], etc.) of string diagrams. Planar algebras are a version
of this diagram calculus which allows you to study monoidal categories from the
point of view of a particular object, where you only consider strings labelled by that
object.
In particular, given a subfactor the resulting string diagrams have regions which
are checkerboard shaded (corresponding to A and B) and unoriented unlabelled
strings (depending on the shading this string represents either ABB or BBA). The
structure here is a called a “shaded planar algebra.”
We sketch the deﬁnition here. For further details, see [14, §2], [13,§0], or [4].
Deﬁnition 2.2 A (shaded) planar tangle has an outer disk, a ﬁnite number of
inner disks, and a ﬁnite number of non-intersecting strings. A string can be either a
closed loop or an edge with endpoints on boundary circles. We require that there be
an even number of endpoints on each boundary circle, and a checkerboard shading of
the regions in the complement of the interior disks. We further require that there be
a marked point on the boundary of each disk, and that the inner disks are ordered.
Two planar tangles are considered equal if they are isotopic (not necessarily rel
boundary).
Here is an example of a planar tangle.
2
1
⋆
⋆
3
⋆ ⋆
Planar tangles can be composed by placing one planar tangle inside an interior
disk of another, lining up the marked points, and connecting endpoints of strands.
The numbers of endpoints and the shadings must match up appropriately. This
composition turns the collection of planar tangles into a colored operad.
Deﬁnition 2.3 A (shaded) planar algebra over a ﬁeld k consists of
• A family of vector spaces {V(n,±,)}n∈N over k, called the positive and negative
n-box spaces.
• For each planar tangle, a multilinear map Vn1,±1⊗...⊗Vnj,±j→Vn0,±0 where
ni is half the number of endpoints on the ith interior boundary circle, n0 is
half the number of endpoints on the outer boundary circle, and the signs ± are
positive (respectively negative) when the marked point on the corresponding
boundary circle is in an unshaded (respectively shaded) region.
6
For example, the planar tangle above gives a map
V1,+⊗V2,+⊗V2,−→V3,+.
The linear map associated to a ‘radial’ tangle (with one inner disc, radial strings, and
matching marked points) must be the identity. We require that the action of planar
tangles be compatible with composition of planar tangles. In other words, composition
of planar tangles must correspond to the obvious composition of multilinear maps.
We will refer to an element of Vn,± (and speciﬁcally Vn,+, unless otherwise stated)
as an “n-box.”
We make frequent use of three families of planar tangles called multiplication,
trace, and tensor product, which are shown in Figure 1. “Multiplication” gives
an associative product Vn,±⊗Vn,±→ Vn,±. “Trace” gives a map Vn,±→ V0,±.
“Tensor product” gives an associative product Vm,±⊗Vn,±→Vm+n,± if m is even,
or Vm,±⊗Vn,∓→Vm+n,± if m is odd.
...
...
...
1
2
⋆
⋆
⋆
, ⋆ ··· ,
...
...
...
...
21 ⋆⋆⋆
Figure 1: The multiplication, trace, and tensor product tangles.
The (shaded or unshaded) empty diagrams can be thought of as elements of V0,±,
since the ‘empty tangle’ induces a map from the empty tensor product C to the
space V0,±. If the space V0,± is one dimensional then we can identify it with C by
sending the empty diagram to one.
Deﬁnition 2.4 A planar algebra is calledirreducible if dimV0,± = 1 and dimV1,± =
1.
Deﬁnition 2.5 An n-box S is uncappable if ϵi(S) = 0 for all i = 1,··· , 2n where
ϵ1 = ⋆⋆ ··
· , ϵ 2 = ⋆⋆ ··
· , ..., ϵ 2n = ⋆
⋆
··
· .
7
We say S is a rotational eigenvector with eigenvalue ω if ρ(S) =ωS where
ρ = ⋆
⋆
··
· .
Note that ω must be a nth root of unity.
Given a shaded planar algebra we can recover two tensor categories called its even
parts. However to describe this we need to deal with an annoying technical point.
Recall that the planar algebra only captures maps between tensor products of a
ﬁxed generating object. If every object of a semisimple tensor category appears as a
summand of some tensor power of a ﬁxed object, then the tensor category can be
recovered from the full subcategory of these tensor powers by taking the idempotent
completion.
Deﬁnition 2.6 The idempotent completion of a tensor category ˇC is a tensor
categoryC which contains ˇC as a full sub-category. The objects of C are pairs (o,p ),
where o is an object of ˇC and p :o→o is an idempotent in ˇC. We deﬁne
HomC
(
(o,p ), (o′,p′)
)
=
{
f∈ Hom ˇC
(
o,o′)⏐⏐ fp =f =p′f
}
and inherit composition and tensor product. (When we say ˇC is a full sub-category
ofC we are implicitly identifying o with (o, 1o).)
Deﬁnition 2.7 IfP is a shaded planar algebra, let ˇPp be the category whose
objects are even integers and whose morphisms are given by
Hom ˇP p (2m, 2n) =Vm+n,+.
LetPp, called the principal even part of P be the idempotent completion of the
additive completion of ˇPp.
Similarly deﬁne ˇPd whose objects are even integers and whose morphisms are given
by
Hom ˇP d (2m, 2n) =Vm+n,−,
and the dual even partPd to be the idempotent completion of the additive completion
of ˇPd.
A planar algebra is called unitary if there is an antilinear adjoint operation∗ on each
Vn,±, compatible with the adjoint operation on planar tangles given by reﬂection
such that the sesquilinear form ⟨x,y⟩ = tr (xy∗) is positive deﬁnite. The even parts
of a unitary planar algebra are semisimple because all the endomorphism algebras are
ﬁnite dimensional C∗ algebras which are necessarily semisimple. Often in order to
construct a unitary planar algebra from a non-unitary planar algebra we quotient out
by the radical of ⟨x,y⟩ = tr (xy∗), which is called the ideal of negligible morphisms.
Suppose that k<K is an inclusion of ﬁelds and suppose that P is a planar algebra
over K . A rational form ofP over k is a planar algebra Pk over k such that
Pk⊗kK is isomorphic to P . If Pk is a rational form for P then the corresponding
8
fusion categoriesPp
k andPd
k are rational forms for Pp andPd. The rational form
Pp
k is a complete rational form for Pp if every isomorphism class of projection in
Vm+n,+(P) has a representative coming from Vm+n,+(Pp) (and similarly for the dual
even part).
