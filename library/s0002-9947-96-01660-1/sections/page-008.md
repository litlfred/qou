---
doc_id: s0002-9947-96-01660-1
doc_title: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS"
section_id: page-008
section_title: "Page 8"
section_number: null
pages: 8-8
source_pdf: S0002-9947-96-01660-1.pdf
source_sha256: aa63e62b78aa5045
toc_source: undetermined
doc_brief: "Invariants of piecewise-linear 3-manifolds — This paper presents an algebraic framework for constructing in- variants of closed oriented 3-manifolds by taking a state sum model on a tri- angulation."
---
4004
JOHN W. BARRETT AND BRUCE W. WESTBURY
Proof. In the formula
M
a∈J
Hom(x, a) ⊗Hom(a, x) ∼= End(x)
ﬁrst consider x to be an element of J. Then by counting dimensions, one has that
End(x) ∼= F.
Now consider the same formula with x any simple object. Again by counting di-
mensions, only one of the terms on the left is non-zero. For this a ∈J, Hom(x, a) ∼=
Hom(a, x) ∼= F. Thus there are elements f ∈Hom(x, a), g ∈Hom(a, x) such that
fg = idx. From this it follows that gf ∈End(a) is an idempotent and is not zero.
But End(a) ∼= F, and so gf = ida. This shows that x is isomorphic to a ∈J.
Deﬁnition 2.12. A semisimple spherical category is called ﬁnite if the set of iso-
morphism classes of simple objects is ﬁnite.
Deﬁnition 2.13. The dimension K of a ﬁnite semisimple spherical category is
deﬁned by the formula
K =
X
a∈J
dim2
q(a)
for some choice J of one object in each isomorphism class of simple objects. The
dimension is independent of this choice.
Lemma 2.14. For each pair of objects (a, b) in a semisimple spherical category,
dimq(a) dimq(b) =
X
c∈J
dimq(c) dim Hom(c, a ⊗b).
Proof. The left-hand side is equal to tr 1a⊗b. The lemma follows from the applica-
tion of the semisimple condition of Deﬁnition 2.10 with x = y = a ⊗b, and some
linear algebra.
3. Symmetries of simplicial invariants
In this section, we deﬁne the data for a state sum model given a strict non-
degenerate spherical category C.
Then we show that the simplicial invariant of
labelled manifolds has the property that it depends only on the isomorphism class
of the labelling of each edge. Then it is shown that the invariant depends only on
the underlying combinatorial structure of the simplicial complex.
The data for a state sum model is constructed as follows. The label set I is the
set of simple objects in the category. For each ordered triple (a, b, c) of labels, the
vector space H(a, b, c) is deﬁned to be Hom(b, a ⊗c) (see Figure 2).
For the partition function of the tetrahedron A labelled by e01 = a, e02 = b,
e12 = c, e23 = d, e13 = e, e03 = f, ﬁrst deﬁne a linear functional on the space
Hom(d ⊗c, e) ⊗Hom(f, d ⊗b) ⊗Hom(e ⊗a, f) ⊗Hom(b, c ⊗a).
The linear functional is deﬁned to be
α ⊗β ⊗γ ⊗δ 7→trL(β(1 ⊗δ)(α ⊗1)γ)
(Figure 3). This linear functional determines a unique linear map
a
b
c
d
e
f

+
: Hom(f, d ⊗b) ⊗Hom(b, c ⊗a) →Hom(e, d ⊗c) ⊗Hom(f, e ⊗a)
