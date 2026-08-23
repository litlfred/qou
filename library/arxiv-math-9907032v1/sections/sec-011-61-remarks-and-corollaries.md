---
doc_id: arxiv-math-9907032v1
doc_title: "Combinatorial optimization in geometry"
section_id: sec-011-61-remarks-and-corollaries
section_title: "Remarks and Corollaries"
section_number: 6.1
pages: 19-20
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
Let us assume that the complex T has no boundary, and that the function ∆ is such
that all of the cone angles (computed using Lemma 1.2) are equal to 2π, so that
any realization is Euclidean (and hence can be developed into the plane ). Then,
we can combine theorems 6.1 and 4.11 to get
Corollary 6.6. Let T be an inﬁnite locally ﬁnite triangulation, and let ∆ :
E(T ) → (0,π ] be an assignment of dihedral angles to the edges of T , let Then there
exists a ﬂat surface S, and a collection of points p1,...,p n,... inS whose Delaunay
triangulation is combinatorially equivalent to T and which has dihedral angles given
by ∆ if and only if:
—If v is an interior vertex of T , then
∑
e ∈E(T ) incident to v
(π − ∆( e)) = 2π. (27)
—If E is a non-coterminous minimal cutset, then
∑
e∈E
(π − ∆( e))> 2π. (28)
The above Corollary can be viewed as an extension of Theorem 0.1 of [2 0] to
the case of ideal polyhedra with inﬁnitely vertices (and hence also of Andre’ev’s
theorem for ideal polyhedra [2]), but not without certain caveats: even when T is
topologically a disk, it is not at all obvious whether the metric on the su rfaceS (or,
even, any surface S) is geodesically complete. If it is complete, it follows that S is
the Euclidean plane, and that the developing map is a global isometry, but otherwise
the developing map is, only an immersion. Checking if the given simply-co nnected
Euclidean surface S is the Euclidean plane is nothing other than the type problem
– that is, we want to know whether a Riemann surface is parabolic, hy perbolic, or
elliptic. If we know the shapes of all the triangles, this can be shown t o be equivalent
to the recurrence of a random walk on the 1-skeleton of the comple x T , where an
edgeAB, incident to triangles ABC andABD has weight 1/(cotC + cotD) ([21]).
Using this, it can be shown without too much diﬃculty that in the case w here all
of the dihedral angles are rational multiples of π, bounded away from 0 and π, then
this is equivalent to the recurrence of the symmetric random walk on the 1-skeleton
of T .
In the special case of all dihedral angles being equal to π or π/2, corollary 6.6
reduces to an existence theorem for inﬁnite locally ﬁnite circle packin gs. In this
case, the type problem, and a number of others, has been studied at great length
by a number of authors, starting with Koebe, but more recently by A. Marden (in
the context of Schottky groups), W. Thurston, B. Rodin and D. S ullivan, Z.-X. He,
O. Schramm, and others.
It should be noted the Theorem 6.1 says nothing about uniqueness, and the proof
certainly does not show any form of uniqueness. In view of Theorem 1.4 one might
suspect that perhaps this could be shown with more work. In fact, it is quite clear
from the above-mentioned work on circle packing that uniqueness f ails, though in
a controlled manner described in the conjecture below:
· 20
Conjecture 6.7. LetT be a inﬁnite locally ﬁnite complex, ∆ a system of dihe-
dral angles satisfying the hypotheses of Theorem 6.1. If the re is a realization of T
supported on a simply-connected domain Ω 0 ⊂ C, then there is one supported on ev-
ery simply-connected domain Ω ⊂ C. Furthermore, such a realization is determined
uniquely by Ω (up to the group of M¨ obius transformations ﬁxing Ω ).
