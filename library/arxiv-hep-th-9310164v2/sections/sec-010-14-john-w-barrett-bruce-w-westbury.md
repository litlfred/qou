---
doc_id: arxiv-hep-th-9310164v2
doc_title: "SPHERICAL CATEGORIES"
section_id: sec-010-14-john-w-barrett-bruce-w-westbury
section_title: "JOHN W. BARRETT & BRUCE W. WESTBURY"
section_number: 14
pages: 14-15
source_pdf: 9310164v2.pdf
source_sha256: e0972e04667ccc47
doc_brief: "SPHERICAL CATEGORIES — This paper is a study of monoidal categories with duals where th e ten- sor product need not be commutative."
---
Proposition 3.7. Let A be a spherical Hopf algebra. Let x be a left A-module.
Then End(x), the endomorphism algebra in the non-degenerate quotient, is semi-
simple.
Proof. Let End A(x) be the endomorphism algebra of x in the category of left A-
modules. Then we show that the kernel of the map End A(x) → End(x) contains
the nilpotent radical of End A(x). Since the nilpotent radical is a two-sided ideal it
is suﬃcient to show that if θ ∈ EndA(x) is nilpotent then tr L(θ) = 0. However θ
and ω commute and so θω is also nilpotent. This shows that tr L(θ) is the matrix
trace of a nilpotent endomorphism of a ﬁnite dimensional vec tor space over F and
so tr L(θ) = 0.
Proposition 3.8. Let A be a spherical Hopf algebra. Take the non-degenerate
quotient of the spherical category of left A-modules. Take J to be a set of objects
such that, if End(x) ∼
= F then there is a unique a ∈ J such that x ∼
= a. Then, for
each object x in the non-degenerate quotient, there is a natural isomorph ism
x ∼
=
⨁
a∈J
Hom(x, a) ⊗ a.
Proof. First we deﬁne, for each idempotent π ∈ End(x), an object πx in the non-
degenerate quotient. Let π′ ∈ EndA(x) be a lifting of π. Then π′x is a left A-module
and so also gives an object, πx, in the non-degenerate quotient. This object is
independent of the choice of lifting since πx is characterised by the property that,
for any w and y,
Hom(w, πx) = Hom( w, x).π and Hom( πx, y) = π. Hom(x, y).
Next we show that if π is primitive then End( πx) ∼
= F. More generally, if π1 and
π2 are primitive idempotents then
Hom(π1x, π2x) ∼
=
{ F if π1 and π2 are isomorphic
0 otherwise
If π is primitive then so is π′ and so End A(π′x) is a local algebra. Hence End( πx)
is a non-trivial semisimple quotient of a local algebra and s o is F. Alternatively,
End(πx) is π. End(x).π which is F since π is primitive.
Now write 1 ∈ End(x) as a sum of orthogonal primitive idempotents. This
decomposition is not canonical. However, for each a ∈ J, deﬁne Ea to be the sum
of the idempotents, {π}, in the decomposition that satisfy πx ∼
= a. Then each
non-zero Ea is a central idempotent in End( x) and the decomposition
x ∼
=
⨁
a∈J
Eax
is canonical. Furthermore it follows from this discussion t hat, for each a ∈ J,
Eax can be naturally identiﬁed with V (x, a) ⊗ a for some V (x, a). Hence x ∼
=⨁
a∈J V (x, a) ⊗ a.
SPHERICAL CATEGORIES 15
Each V (x, a) can be identiﬁed with Hom( x, a) since Hom( a, b) = 0 if a and b
are distinct elements of J. This follows from the non-degeneracy condition which
implies that if Hom( a, b) = 0 then Hom( b, a) = 0.
This shows that the non-degenerate quotient is semisimple a nd that the set J is a
complete set of inequivalent simple objects. If the Hopf alg ebra is ﬁnite dimensional
and semisimple then it is clear that this set is ﬁnite. If the H opf algebra is ﬁnite
dimensional but not semisimple then the set J is typically inﬁnite.
There are two 3-manifold invariants constructed from the qu antised enveloping
algebra of SL(2). One is the construction of a invariant of a framed 3-mani fold
given a surgery presentation of the 3-manifold given in [Res hetikhin and Turaev
1991]. The other is a state sum model invariant constructed i n [Turaev and Viro
1992] using a triangulation. The formalism for extending th e deﬁnitions from SL(2)
to other ﬁnite dimensional simple algebras is given in [Tura ev 1992] and [Barrett
and Westbury 1996]. Each of these approaches encounters the same diﬃculty which
is that the set J is required to be ﬁnite. A quantised enveloping algebra at a r oot
of unity is not semisimple and the set J for the category of all modules may be
inﬁnite. In order to deﬁne 3-manifold invariants it is suﬃci ent to ﬁnd a spherical
subcategory with J ﬁnite. This problem was solved for SL(2) in [Reshetikhin and
Turaev 1991].
Let A be the quantised enveloping algebra of a ﬁnite dimensional s emisimple Lie
algebra at a root of unity. Assume that the order, k, of the quantum parameter q is
at least the Coxeter number of the Lie algebra. Then it is show n in [Andersen and
Paradowski 1995] that the category of tilting modules is the smallest category which
contains the irreducibles with highest weight in the interi or of the fundamental
alcove and which is closed under taking tensor products and d irect summands.
Furthermore this category is spherical and the isomorphism classes of objects in
the semisimple quotient are indexed by the dominant weights in the interior of the
fundamental alcove, and in particular, is a ﬁnite set.
Remark 3.9. Let A be a ﬁnite dimensional spherical Hopf algebra. Then the cate -
gory of projective left A-modules is a spherical category. This constructs a spheric al
subcategory with J ﬁnite but we know of no applications. If A is semisimple this
result is superﬂuous and in the example of the quantised enve loping algebra of
SL(2) given in [Reshetikhin and Turaev 1991] every indecompos able projective has
quantum dimension 0 so that J is empty.
The category of projective left A-modules is a subcategory of the spherical cat-
egory of left A-modules. Hence to show it is spherical it is suﬃcient to show it is
closed under the operations of tensor product and taking dua ls. The tensor product
of a projective module with any module is projective and so th e category of projec-
tive modules is closed under tensor products. It is shown in [ Larson and Sweedler
1969] that a ﬁnite dimensional Hopf algebra is Frobenius and therefore the dual of
a projective module is projective.
