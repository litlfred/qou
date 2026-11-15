---
doc_id: m4-24
doc_title: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface"
section_id: sec-003-11-the-jones-polynomial
section_title: "The Jones polynomial"
section_number: 1.1
pages: 8-9
source_pdf: m4-24.pdf
source_sha256: cf7c5e29b818e647
toc_source: inferred
---
The Kauﬀman bracket of unoriented link diagrams is deﬁned by the following
recursive relations,
D
E
= A
D
E
+ A−1D
E
,

D

= (−A2 −A−2)⟨D⟩
for any diagram D,
⟨the empty diagram ∅⟩= 1,
where three pictures in the ﬁrst formula imply three links diagrams, which are
identical except for a ball, where they diﬀer as shown in the pictures. The Jones
polynomial VL(t) of an oriented link L is deﬁned by
VL(t) = (−A2 −A−2)−1(−A3)−w(D)⟨D⟩

A2=t−1/2 ∈Z[t1/2, t−1/2],
where D is a diagram of L, w(D) is the writhe of D, and ⟨D⟩is the Kauﬀman
bracket of D with its orientation forgotten. The Jones polynomial is an isotopy
invariant of oriented links uniquely characterized by
t−1VL+(t) −tVL−(t) = (t1/2 −t−1/2)VL0(t),
(1)
VO(t) = 1,
where O denotes the trivial knot, and L+, L−, and L0 are three oriented links,
which are identical except for a ball, where they diﬀer as shown in Figure 1. It
is shown, by (1), that for any knot K, its Jones polynomial VK(t) belongs to
Z[t, t−1].
L+
L−
L0
Figure 1: Three links L+, L−, L0
Geometry & Topology Monographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds
381
1.1.1
