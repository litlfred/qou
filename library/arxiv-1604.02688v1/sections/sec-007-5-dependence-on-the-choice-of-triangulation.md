---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-007-5-dependence-on-the-choice-of-triangulation
section_title: "Dependence on the choice of triangulation"
section_number: 5
pages: 8-11
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
Physics predicts that the 3D-index as deﬁned above should give atopological invariantof
the underlying manifoldM, but this is not known in general.
The ﬁrst diﬃculty is that the summation in (16) need not even converge (as a formal
power series) for all ideal triangulationsT. But the good triangulations can be characterised
using normal surface theory.
Given a triangulation T of a 3-manifoldM, an embedded surfaceS ⊂ M is a normal
surfaceif it intersects each tetrahedron in a ﬁnite collection of disjoint normal quadrilaterals
(‘quads’) and triangles as shown in Figure 3. In each tetrahedron there are 4 types of normal
triangles and 3 types of normal quads.
THE 3D-INDEX AND NORMAL SURF ACES 9
Figure 3. The four types of triangular disks (left) and one of the three types
of quadrilateral disks (right).
Embedded normal surfaces were introduced by Kneser [Kne29] and developed by Haken
[Hak61b, Hak61a] to create a normal surface theory which has played a key role in the devel-
opment of algorithmic 3-manifold topology. Haken observed that (not necessarily embedded)
closed normal surfaces are parametrised by vectors of quad numbers and triangle numbers
in Z7n satisfying linearmatching equations. Tollefson [Tol98] showed that the quad numbers
are enough to determine a closed normal surface up to multiples of the boundary tori. These
give vectors inZ3n satisfying linearQ-matching equations.
Deﬁnition 5.1.[JR03, KR05] An ideal triangulationT is 1-eﬃcient if
(0) it contains no embedded normal 2-spheres or projective planes, and
(1) the only embedded normal tori or Klein bottles are vertex-linking.
Theorem 5.2. [GHRS15, Theorem 1.2] The sum deﬁningIT([γ]) converges for all [γ]∈
H1(∂M ; Z) if and only if the sumIT(0) converges if and only if the ideal triangulationT is
1-eﬃcient.
We will outline a new, more direct proof of this result in Section 8 below, by rewriting the
index as a sum of contributions from normal surfaces.
It is shown in [GHRS15] that 1-eﬃcient triangulations exist for many important classes
of cusped 3-manifolds including all hyperbolic manifolds and small Seifert ﬁbre spaces. But
they cannot exist for 3-manifolds containing (embedded) essential spheres, projective planes,
tori or Klein bottles which are not boundary parallel.
It is known by the work of Matveev and Piergallini (see [Mat87, Mat03, Pie88]) that any
two triangulations T, T′ (with at least 2 tetrahedra) of a given closed 3-manifoldM can be
connected by a sequence of 2-3 and 3-2 Pachner moves. We can also consider 0-2 and 2-0
moves on triangulations as shown in Figure 4.
The pentagon identity for the tetrahedral index gives the following key property of the
3D-index:
Theorem 5.3([Gar15, §6],[GHRS15, Theorem 1.1]). If T and T′ are related by a 2-3 move
and both are 1-eﬃcient, thenIT =IT′.
The quadratic identity for the tetrahedral index gives:
10 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
2-3
3-2
(a) The 2-3 and 3-2 moves.
0-2
2-0
(b) The 0-2 and 2-0 moves.
Figure 4. Moves on (topological) triangulations.
Theorem 5.4.[GHRS15, Theorem 5.1]If T and T′ are ideal triangulations related by a 0-2
move and both are 1-eﬃcient, thenIT =IT′.
It is currently unknown whether any two 1-eﬃcient triangulations of a given cusped man-
ifold are connected by 2-3/3-2 and 0-2/2-0 moves preserving 1-eﬃciency. See Section 12 for
a discussion of some experimental results on this question.
However, using the previous results, we can obtain atopological invariantIM of any cusped
hyperbolic 3-manifoldM as follows (see [GHRS] for the details).
• Consider thecanonicalor Epstein-Penner decomposition ofM into convex ideal hy-
perbolic polyhedra (using horoball cusp neighbourhoods of equal volume ifM has
more than one cusp).
• If the Epstein-Penner decomposition is a triangulationT, then we deﬁneIM =IT.
• In general, we can deﬁneIM =IT where T is any triangulation in a classEPconsisting
of all regular triangulations of the Epstein-Penner cells, with all possible layered
triangulations of the bridge regions between any incompatible triangulations of the
faces.
• A regular triangulationof a set of pointsA ={ai} in Rn, is obtained by lifting the
points vertically to points(ai,ti) in Rn+1, taking the bottom faces of their convex
hull in Rn+1, and then projecting back toRn. (Use the projective model to extend
this deﬁnition toHn.)
• All triangulations in classEP admit semi-angle structures, hence are 1-eﬃcient.
• Results of Gelfand, Kapranov and Zelevinsky on regular triangulations imply that
EP is connected by sequences of 2-3, 3-2, 0-2 and 2-0 moves, staying within 1-eﬃcient
triangulations. But the index is invariant under such moves, soI(T) is the same for
all T in EP.
• Hence we obtain a well-deﬁned invariant for any cusped hyperbolic 3-manifold.
6. Some Q-normal surf ace theory
In this section we discuss surfaces in general position with respect to an ideal triangulation.
This discussion is similar to the one of Haken who studied and encoded normal surfaces in
general position with respect to a triangulation of a closed 3-manifold. A major diﬀerence is
THE 3D-INDEX AND NORMAL SURF ACES 11
that amongst surfaces in general position with respect to an ideal triangulation is the class of
embedded spun normal surfaces (a concept introduced by Thurston, [Thu77, Wal11]), which
intersect each tetrahedron in a ﬁnite number of quadrilaterals, and a possibly inﬁnite number
of triangles. Also, just as in the closed case, a spun normal surface can be reconstructed
from its quadrilateral data and the quadrilaterals satisfy theQ-matching equations.
Let M be an orientable 3-manifold with boundary consisting ofr tori, and let T be an
oriented ideal triangulation withn tetrahedra. Let E denote the set of edges ofT, and recall
that □ denotes the set of quad types in the tetrahedra ofT. Of course,|E| =n and|□| = 3n.
Recall that theQ-normal surface solution spaceQ(T; R) for T is a subset of R□∼= R3n
consisting of real quad coordinates assigned to the quad types inT satisfying theQ-matching
equations of Tollefson. After choosing a cyclic ordering of quad types in each tetrahedron,
compatible with the orientation onT, we can write the quad coordinates ofS∈Q(T; R) as
a vector
S = (a1,b 1,c 1,a 2,b 2,c 2,...,a n,bn,cn)∈ (R3)n = R3n
where (aj,bj,cj) are the quad coordinates ofS in tetrahedronj.
Let Q(T; Z) = Q(T; R)∩ Z3n be the sublattice ofQ(T; R) of integer solutions, and let
Q(T; Z+) = Q(T; Z)∩ R3n
+ denote the set of integer solutions with non-negative quad co-
ordinates. Then each elementx of Q(T; Z+) determines a (possibly singular)spun normal
surface in T obtained by takingxA disjoint copies of the quadqA together with additional
normal triangles. The resulting surface is a (possibly singular)closed normal surfaceif only
ﬁnitely many triangles are added, and isembedded if there is at most one non-zero quad
coordinate in each tetrahedron. (See Kang [Kan05], Tillmann [Til08].)
