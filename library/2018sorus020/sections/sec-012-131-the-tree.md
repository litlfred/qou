---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-012-131-the-tree
section_title: "The tree"
section_number: 1.3.1
pages: 30-31
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
toc_source: inferred
doc_brief: "Reidemeister torsion on character varieties — 52 sections: Front matter; Introduction; Character varieties and Reidemeist"
---
The tree
Let K be an extension of k, we deﬁne a k-discrete valuation as a surjective map
v : K →Z ∪{∞} such that
— v(0) = +∞
— v(x + y) ≥min(v(x), v(y))
— v(xy) = v(x) + v(y)
— ∀z ∈k, v(z) = 0 and k is maximal for this property.
We call Ov = {x ∈K : v(x) ≥0} the valuation ring, and we pick t ∈Ov an element of
valuation 1, that we call a uniformizing parameter. The group of invertible elements
O∗
v is the group of elements whose valuation is zero, (t) is the unique maximal ideal
of Ov, Ov/(t) ≃k is the residual ﬁeld. Remark that every ideal is of the form (tn),
for some n ∈N. The main exemple to have in mind here is the valuation ring C[[t]]
of formal series in t, with the valuation v : C((t))∗→Z, P 7→ordt(P) given by the
vanishing order at t = 0. The uniformizing element is t and the residual ﬁeld is C.
A lattice L in a two dimensional K-vector space V is a free Ov-module of rank two
that spans V as a vector space. The group K∗acts on the set of lattices in V by
homothety . We denote by T the set of equivalence classes, that is L ∼L′ iﬀthere
exists x ∈K∗such that L′ = xL.
We are going to deﬁne an integer-valued distance on T. We ﬁx a lattice L together
with a basis of L, say {e, f}. For any class [L′] ∈T one can express a basis of L′ ∈[L′]
as {ae + bf, ce + df} with a, b, c, d ∈K ; and up to homothety, we can pick in fact
a, b, c, d ∈Ov, that is L′ ⊂L. Assume a has minimal valuation among {a, b, c, d},
then the matrix ( a b
c d ) can be transformed into

a
0
0 d−bc
a

by SL2(Ov) right and left
multiplication that preserves the standard lattice O2
v. Hence L′ ≃aOv⊕(d−bc
a )Ov ≃
tnOv ⊕tmOv for some n, m ∈N. We deﬁne d([L], [L′]) = |n −m|, and one can check
29
that it deﬁnes a distance that does depend only on [L] and [L′].
This distance turns T into a graph whose vertices are classes of lattices [L] such
that vertices at distance 1 are linked by an edge. This graph is connected since
any two vertices admit representatives L, L′ such that L = Ov ⊕Ov and L′ =
Ov ⊕td([L],[L′])Ov, hence a path joining L to L′ can be constructed as Lk = Ov ⊕tkOv
with k = 0, . . . , d([L], [L′]). In fact it can be shown that T is a tree, see [SB77].
