---
doc_id: arxiv-math-9907032v1
doc_title: "Combinatorial optimization in geometry"
section_id: sec-013-8-computational-complexity
section_title: "COMPUTATIONAL COMPLEXITY"
section_number: 8
pages: 21-22
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
Consider the following two decision problems:
Problem 1. Let T be a simplicial complex, homeomorphic to a surface S (possibly
with boundary), and let α :V (T ) → R+ be an assignment of cone angles to the ver-
tices of T . Does there exist a Euclidean structure E onS with the prescribed cone
angles, such that the Delaunay triangulation of ( S,E ) is combinatorially equivalent
to T ?
Problem 2. Let T be a simplicial complex, homeomorphic to a surface S (possibly
with boundary), and let ∆ : E(T ) → (0,π ] be an assignment of dihedral angles to
the edges of T . Does there exist a singular Euclidean structure E on S, such that
the Delaunay triangulation of ( S,E ) is combinatorially equivalent to T , and whose
dihedral angles are given by ∆.
By Theorem 1.6, there are eﬃcient algorithms for both problems, sin ce they
reduce to the linear program L of section 1. If the angles (cone angles in problem 1,
dihedral angles in problem 2) are rational multiples of π, such that the numerator
and denominator are both bounded by C, then (by now) standard interior point
methods allow us to solve the linear program L using O(n4(1 + logC)) arithmetic
operation, each involving arithmetic using precision O(n(1 + logC)). In the case
where all of the prescribed cone angles are equal to 2 π, the log C can be disposed
with, and we wind up with an algorithm of bit-complexity O(n5 log2n).
Remark. In practice, the simplex algorithm appears much more eﬃcient, and t his
has been used by M. B. Dillencourt to analyze all planar triangulations of up to 14
vertices, and to determine which of them are combinatorially equivale nt to planar
Delaunay tessellations ([4; 3]).
For problem 2, the network ﬂow formulation of section 5 turns out t o give a
markedly superior complexity. Indeed, it has been shown in [1] that f or a network
withn nodes, m arcs, and the (integer) capacity of each arc bounded by U , we can
determine the maximal ﬂow in time bounded by O(nm log((n/m)(logU )1/ 2 + 2)).
For the network N1 of section 5, assuming the genus of the surface is ﬁxed,
the number of arcs and nodes in the network are both bounded by c onstant mul-
· 22
tiples of the number F of faces in the complex T . If all of the dihedral an-
gles are rational multiples of π, with numerators and denominators all bounded
in absolute value by C, the quantity U is bounded by CO(F ) (since we need to
compute the least common multiple of the denominators), giving a run ning time
bound of O(F 5/ 2). For the program N2, the bound is the same, since the only
diﬃculty consists of picking the right value of ǫ, and this can be made to be
1/least common denominator of the dihedral angles.
