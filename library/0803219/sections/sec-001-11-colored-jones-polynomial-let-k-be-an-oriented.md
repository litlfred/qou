---
doc_id: 0803219
doc_title: "ACTA MATHEMATICA VIETNAMICA 219 AN INTRODUCTION TO THE VOLUME CONJECTURE AND ITS GENERALIZATIONS"
section_id: sec-001-11-colored-jones-polynomial-let-k-be-an-oriented
section_title: "Colored Jones polynomial. Let K be an oriented knot in the three-sphere"
section_number: 1.1
pages: 2-4
source_pdf: 0803219.pdf
source_sha256: 8e37e11b8c8953c8
---
S3, and D its diagram. We assume that D is the image of a projection R3 ∼=
S3 \ {∞} → R2 of a circle S1 together with a ﬁnite number of double point
singularities as in Figure 1.
Figure 1. A crossing of a knot diagram
We call these double points with over/under data crossings.
Now we associate to the knot diagram a Laurent polynomial in A following
L. Kauﬀman [28].
First of all we forget the orientation of D.
Then replace a crossing with a linear combination of two pair s of parallel arcs
as in the right hand side of the following equality:
= A + A−1 .
THE VOLUME CONJECTURE AND ITS GENERALIZATIONS 221
Now we have a linear combination of two new diagrams, which ma y not be knot
diagrams but link diagrams.
We choose another crossing and replace it with a linear combi nation of two
new diagrams. Now we have a linear combination of four diagra ms.
Continue these processes until we get a linear combination o f diagrams with
no crossings, whose coeﬃcients are some powers of A.
If we replace each resulting diagram with ( − A2 − A−2)ν −1 where ν is the num-
ber of components of the diagram, we get a Laurent polynomial ⟨D⟩ ∈ Z[A, A −1],
which is called the Kauﬀman bracket.
Now we recall the orientation of D. Let w(D) be the sum of the signs of the
crossings in D, where the sign is deﬁned as in Figure 2.
:+1 , :− 1
Figure 2. A positive crossing (left) and a negative crossing (right)
Lastly we deﬁne V (K; t) :=
(
− A3)−w(D) ⟨D⟩
⏐⏐⏐
A:=t− 1/ 4
. It is known that this
coincides with (a version of) the Jones polynomial [22] sinc e
t−1V
(
; t
)
− tV
(
; t
)
=t−1 ×
(
− t−3/ 4
)−w( )⟨ ⟩
− t ×
(
− t−3/ 4
)−w( )⟨ ⟩
=t−1 ×
(
− t−3/ 4
)−w( )−1{
t−1/ 4
⟨ ⟩
+ t1/ 4
⟨ ⟩}
− t ×
(
− t−3/ 4
)−w( )+1{
t−1/ 4
⟨ ⟩
+ t1/ 4
⟨ ⟩}
=
(
− t−3/ 4
)−w( )(
t1/ 2 − t−1/ 2
)⟨ ⟩
=
(
t1/ 2 − t−1/ 2
)
V
(
; t
)
.
In this paper we use another version J2(K; q) that satisﬁes
qJ2
(
; q
)
− q−1J2
(
; q
)
=
(
q1/ 2 − q−1/ 2
)
J2
(
; q
)
with the normalization J2(unknot; q) = 1. Note that
J2(L; q) = ( − 1)♯(L)−1V
(
L; q−1)
for a link with ♯(L) components.
222 HITOSHI MURAKAMI
It is well known that J2 corresponds to the two-dimensional irreducible rep-
resentation of the Lie algebra sl(2; C). The invariant corresponding to the N -
dimensional irreducible representation is called the N -colored Jones polynomial
and denoted by JN (K; q). It can be also deﬁned as a linear combination of the
(2-colored) Jones polynomials of ( N − 1)-parallels or less of the original knot.
For example, K. Habiro [14] and T. Lˆ e [38] calculated the N -colored Jones
polynomial for the trefoil knot T (Figure 3) and for the ﬁgure-eight knot E
(Figure 4) as follows:
JN (T ; q) = q1−N
N −1∑
k=0
q−kN
k∏
j=1
(
1 − qj−N)
and
JN (E; q) =
N −1∑
k=0
k∏
j=1
(
q(N −j)/ 2 − q−(N −j)/ 2
)(
q(N +j)/ 2 − q−(N +j)/ 2
)
.
For other formulas of JN (T ; q), see [42, 40].
Figure 3. Trefoil
