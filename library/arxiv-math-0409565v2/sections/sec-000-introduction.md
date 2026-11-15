---
doc_id: arxiv-math-0409565v2
doc_title: "Unital Gröbner Bases over Arbitrary Commutative Ground Rings"
section_id: sec-000-introduction
section_title: "Introduction."
section_number: null
pages: 1-2
source_pdf: 0409565v2.pdf
source_sha256: 236704063f12c05e
toc_source: outline
doc_brief: "Unital Gröbner Bases over Arbitrary Commutative Ground Rings — Let R be a commutative ring with unity and a let A be a not necessarily commutative R-algebra which is free as an R-module."
---
Introduction.
There have been several generalizations of Gr¨obner basis theory, coming in one
of two ﬂavors: noncommutative theory and theories for working over special
ground rings, e.g. Euclidean domains, PID’s or UFD’s. For an overview of the
theory of such rings see [1]. Over a ﬁeld, one of the main uses of a Gr¨obner
basis is to ﬁnd a basis for the quotient of an algebra A by a (left or two-sided)
ideal I. Let us consider two examples for k a (commutative) ﬁeld (with unity)
whose quotient algebras can be readily described through the known Gr¨obner
basis theory.
Example 1.
1.1. Let A be the polynomial algebra k[x1, · · · , xn] and consider the ideal
m = (x1, · · · , xn).
Taking a graded lexicographic ordering on A with
xi < xj if i < j, m2 has a Gr¨obner basis given by {xixj}. Thus the
quotient A/m2 is an n + 1-dimensional k-vector space with a basis given
by:
A/m2 = k{1, x1, · · · , xn}
∗Both authors were supported under a NSF VIGRE grant.
1
1.2. If g is a lie algebra with lie bracket [ , ]g over k then one forms the
universal enveloping algebra Ug as the quotient of the tensor or free algebra
T g on g by the two sided ideal J:
J = (xy −yx −[x, y]g |x, y ∈g֒ →T g)
If one chooses a total ordering < on the index set I for a k-basis g = k <
xi|i ∈I > then a Gr¨obner basis argument yields the Poincare-Birkhoﬀ-
Witt(PBW) theorem which says that Ug has a basis of non-decreasing
words ([5] [2]).
A consideration of the ﬁrst example shows the fact that k was a ﬁeld was not
important – one would have a similar statement with the integers Z, though not
through Gr¨obner basis techniques. The same holds for the second example if
we replace k by an arbitrary (commutative) ring. However, in this more general
setting, one cannot make use of Gr¨obner basis techniques – one must prove this
by “ad-hoc” methods as in [6]. However, these arguments bear a close relation
to those used in the Gr¨obner basis theory. We view the inability of Gr¨obner
basis techniques to apply to these mild generalizations as an unsatisfactory state
of aﬀairs.
If one regards the above two examples closely, one sees that the ground ﬁeld
k never enters into the picture. Speciﬁcally, one does not need to invert any
constants, and this leads to the notion of a unital Gr¨obner basis. We will prove
the following:
Theorem 2. Let R be a commutative algebra with unity.
Let A be an R-
algebra which is free as an R-module and without quasi-zeros. Let (B, <) be an
admissible system on A and let I be a two-sided ideal of A with a unital Gr¨obner
basis G. Deﬁne ˜O(G) to be the free R-module spanned by the monomials which
do not occur as leading monomials of members of G. Then:
1. There is a k-module isomorphism A/I ≃˜O(G) of free R-modules.
2. A = I ⊕˜O(G)
For the case of a left ideal I, or for the case where A has quasi-zeros, one only
need to combine the techniques in [3] with ours. As a corollary we obtain the
PBW theorem over an arbitrary commutative ring with unity. In particular, if R
is a Q-algebra we have a Gr¨obner basis proof of the equivalence of the category of
(ﬁnite dimensional) lie algebras over R and (ﬁnite dimensional) smooth formal
groups over R.
