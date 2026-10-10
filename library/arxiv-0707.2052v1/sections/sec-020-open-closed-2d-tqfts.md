---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-020-open-closed-2d-tqfts
section_title: "Open-closed 2d TQFTs."
section_number: null
pages: 26-27
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasiz ing the importance of a pairing which generalizes Mukai’s pairi ng on the cohomology of K3"
---
Consider the open and closed 2-cobordism category 2Coboc whose objects
are oriented, compact one-manifolds — in other words, disjo int unions of
circles and intervals — and whose morphisms are (diﬀeomorph ism classes
of) cobordisms-with-corners between the source and target one-manifolds.
A morphism can be drawn as a vertical cobordism, from the sour ce at the
bottom to the target at the top. As well as parts of the boundar y being
at the top and the bottom, there will be parts of the boundary i n between,
corresponding to the fact that this is a cobordism with corne rs. An example
is shown below.
Disjoint union makes 2Coboc into a symmetric monoidal category and an
open-closed two-dimensional topological quantum ﬁeld the ory (2d TQFT) is
deﬁned to be a symmetric monoidal functor from 2Coboc to some appropriate
symmetric monoidal target category, which we will take to be the category of
vector spaces or the category of graded vector spaces. The ca tegory 2Coboc
has a simple description in terms of generators and relation s which means
that there is a reasonably straight forward classiﬁcation o f open-closed 2d
TQFTs up to equivalence. This is what we will now describe. Th e following
morphisms generate 2Coboc as a symmetric monoidal category.
We will come back to the relations below.
To specify an open-closed 2d TQFT up to equivalence on object s it suf-
ﬁces to specify the image C of the circle and the image O of the interval. The
former is called the space of closed string states and the lat ter is called the
space of open-string states. Using the four planar generating morphisms pic-
tured above, together with the relations between them, it tr anspires that O,
the space of open-string states is precisely a symmetric, bu t not-necessarily
commutative Frobenius algebra. This means that it is a unita l algebra with
a non-degenerate, symmetric, invariant inner-product. It is useful to note
here that the inner product is symmetric because the two surf aces pictured
below are diﬀeomorphic, however these surfaces are not ambient isotopic
— so one cannot be deformed to the other in three-space while t he bottom
boundary is ﬁxed.
diﬀeo=
On the other hand, the ﬁrst four generating morphisms, along with their
relations, mean that C, the space of closed string states, is a commuta-
26
tive Frobenius algebra. The last two morphisms mean that there ar e maps
i∗ : C→ O and i∗ : O→ C, and by the relations these are adjoint with respect
to the pairings on these spaces. Moreover, i∗ is an algebra map, such that
its image lies in the centre of O. The ﬁnal relation that these must satisfy is
the Cardy Condition . In terms of the generators pictured above this is the
following relation:
= .
Note again that these surfaces are diﬀeomorphic but not isot opic in three-
space. In terms of maps, writing µ : O ⊗ O→ O and δ : O→ O ⊗ O for the
product and coproduct of the open string state space and writ ing τ : O⊗O→
O ⊗ O for the symmetry in the target category, the Cardy Condition is the
equality of maps from O to O:
µ ◦ τ ◦ δ = i∗ ◦ i∗.
We will have reason to use an equivalent condition below.
To summarize, having an open-closed 2d TQFT is equivalent to having
the data of a commutative Frobenius algebra C, a symmetric Frobenius
algebra O, and an algebra map i∗ : C→ O with central image, such that the
Cardy Condition is satisﬁed.
