---
doc_id: arxiv-math-0110119v1
doc_title: "Idempotents of the Hecke algebra become Schur functions in the skein of the annulus"
section_id: sec-004-5-the-variant-skein-c-of-the-annulus
section_title: "The variant skein C′ of the annulus"
section_number: 5
pages: 6-8
source_pdf: 0110119v1.pdf
source_sha256: 4904a86e8a340f59
toc_source: inferred
doc_brief: "Idempotents of the Hecke algebra become Schur functions in the skein of the annulus — The Hecke algebra Hn contains well known idempotents Eλ which are indexed by Young diagrams with n cells."
---
The variant skein C′ of the annulus
The skein of the annulus C′ with two boundary points has been considered e.g.
in [6] and [4]. We are using the version introduced by Morton in [10] where the
two boundary points lie on diﬀerent boundary components of the annulus. This
version has the beneﬁt of a commutative multiplication.
We equip the annulus with two distinguished boundary points. An output
point on the inner circle, and an input point on the outer circle. The resulting
skein C′ becomes an algebra by deﬁning the product A · B of diagrams A and B
as putting the outward circle of B next to the inward circle of A so that the two
involved distinguished boundary points become a single point in the interior of
the new annulus. An example for the multiplication is depicted in ﬁgure 5. The
single straight arc e connecting the two marked points is the identity element, as
shown in ﬁgure 6.
Any arc which connects the two marked points without crossings is regularly
isotopic to a power of the diagram a which is depicted in ﬁgure 7.
For any integer n ≥1 we have a linear map ∆′
n : Rn
n →C′ as shown in ﬁgure
8. We abbreviate ∆′
n by ∆′ if the index n is obvious from the context. With this
notation, the diagram a from ﬁgure 7 is the image of the identity braid 12 of R2
2
under the map ∆′
2.
We denote the image of Rn
n under the map ∆′
n by Cn. We deﬁne C′+ to be the
submodule of C′ spanned by all submodules C′0, C′1, . . ..
6
·
=
Figure 5: The multiplication in C′.
Figure 6: The identity e in C′.
Figure 7: The arc a (at the left) and its
inverse a−1 (at the right).
D
D
Figure 8: Map ∆′
n from Rn
n to C′.
7
Figure 9: The additional arc for the closure.
The diagrams A · B and B · A are not regularly isotopic in general but they
are equal modulo the skein relations as will be shown in lemma 5.1.
We note that C′ can be turned into an algebra over C in two ways. Let A be a
diagram in C′ and γ be a diagram in C. Then γ · A is deﬁned as putting γ above
A, and A · γ is deﬁned as putting γ below A. Morton uses in [10] the notation
l(γ, A) resp. r(A, γ) for the operation of C on C′ on the left resp. right (up to a
turn over of the annulus).
Lemma 5.1 ([10]) C′ is commutative.
Proof Let D be a diagram in C′. By induction on the number of crossings of D,
we can write D as a scalar linear combination of diagrams, D = α1D1+· · ·+αkDk,
such that the single arc of any diagram Di is totally descending and that it lies
completely below any other component of Di. Hence, D = γ1ai1 + · · · + γkaik for
elements γ1, . . . , γk of C and ij ∈Z.
The commutativity of C′ now follows from the observation that terms of the
kind γai for γ ∈C and i ∈Z commute with each other.
⋄
Remark The above proof suggests that C′+ is the polynomial ring in a with
coeﬃcients in C+. This turns out to be true. One has to check that the powers
of a are linearly independent over the scalars C+ (see [4] and [7]).
We deﬁne a closing operation r 7→ˆr from C′ to C which means adding the arc
in ﬁgure 9 from above to a diagram r. In order that this is possible, the annulus
for C has to be slightly larger than C′. The framing of the diagram ˆr is deﬁned
to be its blackboard framing. We remark that this closing operation is not an
algebra homomorphism.
