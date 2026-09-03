---
doc_id: s0002-9947-96-01660-1
doc_title: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS"
section_id: sec-010-4-a-map-from-vertices-to-morphisms
section_title: "A map from vertices to morphisms,"
section_number: 4
pages: 6-8
source_pdf: S0002-9947-96-01660-1.pdf
source_sha256: aa63e62b78aa5045
doc_brief: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS — This paper presents an algebraic framework for constructing in- variants of closed oriented 3-manifolds by taking a state"
---
then this graph can be evaluated to give a morphism. The relations for a pivotal
category imply that this evaluation depends only on the isotopy class of the graph,
where the attached data is carried along with the isotopy.
The sphere S2 can be regarded as the plane with the point at inﬁnity attached,
and so a planar graph can also be thought of as a graph embedded in S2. Spherical
categories are pivotal categories which satisfy an extra condition, the equality of
left and right trace. This condition implies that the spherical category determines
an invariant of isotopy classes of closed graphs on the sphere. There is an isotopy of
the sphere which takes a closed graph of the form of Figure 1 to the graph obtained
by closing M in a loop to the left. This isotopy moves the loop in Figure 1 past
the point at inﬁnity. Taken together with planar isotopies, such an operation on
planar graphs generates all the isotopies on the sphere.
Deﬁnition 2.7. For any two objects a andb there is a bilinear pairing
Θ: Hom( a,b )× Hom(b,a )→F
deﬁned by Θ(f,g )=t rL(fg )=t rL(gf ).
Deﬁnition 2.8. An additive spherical category is non-degenerate if, for all objects
a and b, the pairing Θ is non-degenerate.
The next theorem shows that every additive spherical category has a natural
quotient which is a non-degenerate spherical category.
INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS 4003
=MM
Figure 1
Theorem 2.9. LetC be an additive spherical category. Deﬁne the additive subcat-
egoryJ to have the same set of objects and morphisms deﬁned by
HomJ (c1,c 2)= {f∈ HomC(c1,c 2):t rL(fg )=0 for all g∈ HomC(c2,c 1)}.
ThenC/J is a non-degenerate additive spherical category.
Proof. It is clear that J is closed under composition on either side by arbitrary
morphisms inC. Hence the quotient is an additive category. It is also clear that
ˆf∈J if and only if f∈J , and so the functor ˆ is well-deﬁned on the quotient.
The functor⊗ is well-deﬁned on the quotient, since f∈J impliesf⊗g1∈J and
g2⊗f∈J for arbitrary morphisms in C. This follows from the observation that
trL(f⊗g)=t rL(f). trL(g), which uses the spherical condition.
The morphisms ϵ(a) are taken to be the images in the quotient of the given
morphisms inC. The conditions on this structure which imply that this quotient
is spherical follow from the same conditions in C.
Each pairing Θ is non-degenerate by construction.
An extra condition on the spherical category is required for the piecewise-linear
invariance of the partition function of a natural simplicial ﬁeld theory. Similar
conditions have been considered by [17], [27], [26], [23] and [28]. An object a is
called non-zero if the ring End(a)⁄=0 .
Deﬁnition 2.10. A semisimple spherical category is an additive, non-degenerate,
spherical category such that there exists a set of inequivalent non-zero objects, J,
such that for any two objects x andy, the natural map given by composition,
⨁
a∈J
Hom(x,a )⊗ Hom(a,y )→ Hom(x,y ),
is an isomorphism.
An object a is called simple if End(a)∼=F.
The following lemma shows that the set J is essentially ﬁxed by the category.
Lemma 2.11. Every simple object is isomorphic to a unique element of J,a n d
every element of J is simple.
4004 JOHN W. BARRETT AND BRUCE W. WESTBURY
Proof. In the formula
⨁
a∈J
Hom(x,a )⊗ Hom(a,x )∼= End(x)
ﬁrst consider x to be an element of J. Then by counting dimensions, one has that
End(x)∼=F.
Now consider the same formula withx any simple object. Again by counting di-
mensions, only one of the terms on the left is non-zero. For thisa∈J,H o m (x,a )∼=
Hom(a,x )∼=F. Thus there are elements f∈ Hom(x,a ), g∈ Hom(a,x ) such that
fg =idx. From this it follows that gf∈ End(a) is an idempotent and is not zero.
But End(a)∼=F,a n ds ogf =ida. This shows that x is isomorphic to a∈J.
Deﬁnition 2.12. A semisimple spherical category is called ﬁnite if the set of iso-
morphism classes of simple objects is ﬁnite.
Deﬁnition 2.13. The dimension K of a ﬁnite semisimple spherical category is
deﬁned by the formula
K =
∑
a∈J
dim2
q(a)
for some choice J of one object in each isomorphism class of simple objects. The
dimension is independent of this choice.
Lemma 2.14. For each pair of objects (a,b ) in a semisimple spherical category,
dimq(a)d i mq(b)=
∑
c∈J
dimq(c)d i mH o m (c,a⊗b).
Proof. The left-hand side is equal to tr 1a⊗b. The lemma follows from the applica-
tion of the semisimple condition of Deﬁnition 2.10 with x = y = a⊗b,a n ds o m e
linear algebra.
