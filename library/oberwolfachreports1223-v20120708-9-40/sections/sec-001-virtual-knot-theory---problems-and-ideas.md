---
doc_id: oberwolfachreports1223-v20120708-9-40
doc_title: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by"
section_id: sec-001-virtual-knot-theory---problems-and-ideas
section_title: "Virtual Knot Theory - Problems and Ideas"
section_number: null
pages: 9-12
source_pdf: OberwolfachReports1223_v20120708_9_40.pdf
source_sha256: 94f82cfc185955ba
toc_source: inferred
doc_brief: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by — This meeting concentrated on topological invariants in low di"
---
Louis H. Kauffman
1. Introduction
Virtual knot theory [3, 2] is a generalization of classical knot theory that can be
described in a number of ways. One way to describe it is to say that virtual knot
theory uses diagrams just like the diagrams for classical knot theory except that
there is a new type of crossing, called virtual, that is neither an under-crossing
nor an overcrossing. The virtual crossing behaves in the following way: any arc
in the diagram with a consecutive sequence of virtual crossings can be excised
from the diagram and another arc can be placed transversely to the remaining
part of the diagram so that all the crossings introduced in the new arc are also
taken to be virtual. Otherwise, one applies the usual Reidemister moves to the
classical crossings in the diagram. This diagrammatic deﬁnition of virtual knot
theory is equivalent to saying that virtual knot theory is the set of equivalence
classes of oriented Gauss codes modulo the abstract Reidemeister moves on these
codes. Since not all codes are realizable in the plane, a diagram for a virtual knot
or link may contain virtual crossings in the same way that an attempt to embed a
non-planar graph into the plane leads to extra crossings of the edges of the graph
with itself. In this view, the virtual crossings are artifacts of the attempt to embed
a non-planar code into the plane.
Another equivalent deﬁnition of virtual knot theory is that a virtual knot is
represented by an embedding of a circle (or circles) into a thickened oriented surface
of some genus g. Two such embeddings are equivalent if there is an orientation
preserving homeomorphism of the surface that carries one embedding to the other,
or if one can perform a 1-handle surgery in the complement of the knot in the
thickened surface, retaining connectiviity and changing the genus. We say that
virtual knots are knots in thickened surfaces taken up to handle stabilization.
From this point of view, one would like to ﬁnd the least genus surface in which
such a knot could be represented. Kuperberg [4] proved that the embedding type
of the knot in its minimal genus surface is uniquely determined and so there is a
deﬁnite topological interpretation for the virual knot as its least genus embedding.
It follows from this Theorem of Kuperberg that virtual knot theory embeds in
classical knot theory (this was proved earlier by a more algebraic argument [3, 2]).
In this talk we describe a polynomial invariant of virtual knots and links that
has the advantage of being quite easy to calculate, and it can detect features that
the Jones polynomial cannot see.
10
Oberwolfach Report 28/2012
a
b
d=a-1
c= b+1
W    = a - c
W    = b - d 
+
-
a
b
a
b
No change at a 
virtual crossing.
A
B
C
A
B
C
0
-1
0
0
1
1
2
2
1
1
0
A
B
C
W
W
+
-
sgn(A) = sgn(B) = +1
sgn(C) = -1
wr(K) = 1
P   (t) =  t   + t    - 2
-2   +2
+2   -2
0     0
-2
2
K
K
Figure 1. Labeled Flat Crossing and Example 1
2. The Polynomial Invariant
We deﬁne a polynomial invariant of of virtual knots by ﬁrst describing how to
calculate the polynomial. We then justify that this deﬁnition is invariant under
virtual isotopy. Calculation begins with a ﬂat oriented virtual knot diagram (the
classical crossings in a ﬂat diagram do not have choices made for over or under).
An arc of a ﬂat diagram is an edge of the 4-regualar graph that it represents. That
is, an edge extends from one classical node to the next in orientation order. An
arc may have many virtual crossings, but it begins at a classical node and ends at
another classical node. We label each arc c in the diagram with an integer λ(c) so
that an arc that meets a classical node and crosses to the left increases the label
by one, while an arc that meets a classical node and crosses to the right decreases
the label by one. See Figure 1 for an illustration of this rule. We prove that such
integer labelling can always be done for any virtual or classical link diagram. In
a virtual diagram the labeling is unchanged at a virtual crossing, as indicated in
Figure 1. One can start by choosing some arc to have an arbitrary integer label,
and then proceed along the diagram labelling all the arcs via this crossing rule.
We call such an integer labelling of a diagram a Cheng coloring of the diagram.
The invariant described herein is a generalization the the invariant described by
Cheng in [1].
Given a labeled ﬂat diagram we deﬁne two numbers at each classical node c:
W−(c) and W+(c) as shown in Figure 1. If we have a labeled classical node with
left incoming arc a and right incoming arc b then the right outgoing arc is labeled
Invariants in Low-Dimensional Topology and Knot Theory
11
a −1 and the left outgoing arc is labeled b + 1 as shown in Figure 1. We then
deﬁne
W+(c) = a −(b + 1)
and
W−(c) = b −(a + 1).
Note that
W−(c) = −W+(c)
in all cases.
Given a crossing c in a diagram K, we let sgn(c) denote the sign of the crossing.
The sign of the crossing is plus or minus one according to the standard convention.
The writhe, wr(K), of the diagram K is the sum of the signs of all its crossings.
For a virtual link diagram, labeled in the integers according to the scheme above,
and a crossing c in the diagram, deﬁne W(c) by the equation
W(c) = Wsgn(c)(c)
so that W(c) is W±(c) according as the sign of the crossing is plus or minus.
Let K be a virtual knot diagram. Deﬁne
PK =
!
c
sgn(c)tW(c) −wr(K).
We shall prove that the Laurent polynomial PK is a highly non-trivial invariant
of virtual knots.
In Figure 1 we show the computation of the weights for a given ﬂat diagram
and the computation of the polynomial for a virtual knot K with this underlying
diagram. The knot K is an example of a virtual knot with unit Jones polynomial.
The polynomial PK for this knot has the value
PK = t−2 + t2 −2,
showing that this knot is not isotopic to a classical knot.
References
[1] Zhiyun Cheng, A polynomial invariant of virtual knots, arXiv:1202.3850.
[2] M. Goussarov, M. Polyak and O. Viro, Finite type invariants of classical and virtual knots,
Topology 39 (2000), 1045–1068.
[3] L. H. Kauﬀman, Virtual Knot Theory, European J. Comb. 20 (1999), 663–690.
[4] G. Kuperberg, What is a virtual link?, Algebraic and Geometric Topology 3 (2003), 587–
591.
12
Oberwolfach Report 28/2012
