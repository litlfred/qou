---
doc_id: arxiv-2108.09349v2
doc_title: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS BARBARA NIMERSHIEM"
section_id: sec-008-3-angle-structures-and-the-casson-rivin-program
section_title: "Angle structures and the Casson-Rivin program"
section_number: 3
pages: 11-13
source_pdf: 2108.09349v2.pdf
source_sha256: 4c732bfcbf3dfb16
---
We will prove that the triangulation τp ofXp deﬁned in 2.4 is geometric by applying the Casson-
Rivin program. This section provides some deﬁnitions, useful results, and a basic outline of the
program. For more details and a beautiful exposition, including an elementary proof of the Casson-
Rivin Theorem, the reader is encouraged to read Futer and Gu´ eritaud’s paper [5].
3.1. Angle structures. To move from a topological triangulation to a geometric one, we need a
way to impose a hyperbolic structure on each tetrahedron where the face pairings are hyperbolic
isometries. A start is to assign angles to the edges of the triangulation.
Deﬁnition 3.1. An angle structure on an ideal triangulation τ of a 3-manifold is an assignment of
angles to the edges of the tetrahedra in τ satisfying the following conditions:
(1) Angles assigned to opposite edges of a tetrahedron are equal, meaning it is enough to specify
three angles θ3i−2, θ3i−1, and θ3i, for each tetrahedron Ti∈τ;
12 BARBARA NIMERSHIEM
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
w′
0
w1 w′
1
w2 w′
2 s
wp−1 w′
p−1
wp
0 5
1 2
1 2 0 5
0 5 1 2
1 2 0 5 d c
0 5 1 2 a b
1 2 0 5
0 5 1 2
1 2
0 5
Figure 8. The tetradedra of τp with [w′
0(01)] colored red. All but s are shown in
the braid complement on the left. The dashed arrows on the right indicate that a
bottom face of the originating tetrahedron is identiﬁed through a half-twist to a top
face of the target tetrahedron. Among faces unpaired by half-twists, the top faces
of w′
0 are identiﬁed to the bottom faces of wp and s is glued to the top faces of w1
and w′
1 and the bottom faces of wp−1 and w′
p−1 as in Table 5.
(2) θ3i−2 +θ3i−1 +θ3i =π for all i; and
(3) The sum of the angles surrounding an edge of the 3-manifold equals 2 π.
This paper utilizes both taut angle structures , where θk ∈{ 0,π} for all k, and positive angle
structures, where θk > 0 for all k. Note that Condition (2) of the deﬁnition implies that a positive
angle structure must have all angles strictly between 0 and π. In this case, the three angles that
sum to π specify a positively oriented ideal hyperbolic tetrahedron. The tetrahedron is isometric to
one whose vertices are at 0, 1, ∞, and a complex number z with Im(z) > 0, where 0, 1, and z
form a Euclidean triangle having the assigned angles. If Im( z) = 0, the tetrahedron is said to be
degenerate, and, if Im(z)< 0, negatively oriented. If an angle structure θ assigns the same angles to
two tetrahedra,T1 andT2, then we will say they are isometric with respect to θ and write T1∼=θ T2.
We useA(τ) to denote the space of all positive angle structures on a triangulation τ and note
that, if τ hasn tetrahedra,A(τ)⊂ (0,π )3n is a convex polytope with compact closure. As such, the
GEOMETRIC TRIANGULATIONS OF A F AMILY OF HYPERBOLIC 3-BRAIDS 13
points obtained through coordinate-by-coordinate averaging of elements of A(τ) are again in A(τ).
Also, real-valued functions deﬁned on A(τ) attain their extreme values. See [5, Proposition 3.2] for
more details about the space of angle structures.
As will be described in 3.3, the initial step in the Casson-Rivin program is to argue that A(τ) is
nonempty, i.e., that the triangulation admits a positive angle structure. We accomplish this in our
case by ﬁrst showing (in 4.1) that τp admits a special type of taut angle structure — a veering angle
structure. The notion of “veering,” ﬁrst introduced by Agol [1], has several equivalent formulations.
The simplest to apply to our triangulations is from [12].
Deﬁnition 3.2. A veering angle structure on an ideal triangulation τ of an oriented 3-manifold M
is a taut angle structure meeting an additional condition: The edges of M can be colored red and
blue in such a way that within each tetrahedron
• two of the edges with angle 0 are red and two are blue (the color on an angle π edge can be
either red or blue)
• when viewed from any of the four ideal vertices, the π-angled edge is followed in the coun-
terclockwise direction by a blue edge and then a red edge.
Each tetrahedron in a veering triangulation appears as the one in Figure 9, where theπ-angled edges
on the diagonal can be red or blue. If there is also a consistent “upward” orientation on the four faces
(for example out of the page in Figure 9), the angle structure is transverse taut. A triangulation
that admits a veering angle structure is said to be veering.
Figure 9. A tetrahedron in a veering triangulation.
Positive angle structures give geometric structures on the tetrahedra in a triangulation. In turn,
these structures determine the face-pairing isometries. Condition (3) of Deﬁnition 3.1 guarantees
that, under these isometries, the tetrahedra ﬁt together to ﬁll the space around the edges of the
manifold, because the sum of dihedral angles around any edge is 2π. However, there is no guarantee
that the result is metrically complete. In fact, if a 3-manifold has a complete hyperbolic structure
of ﬁnite volume, Mostow-Prasad rigidity ensures that the structure is unique up to isometry [14]
[16], so one should not expect completeness for an arbitrary point in A(τ). It turns out that the
independent work of Casson and Rivin [17], which forms the basis of the Casson-Rivin program
in [5] and outlined in 3.3, connects the question of completeness to the volume associated to an
angle structure inA(τ), i.e., the sum of the volumes of the corresponding hyperbolic tetrahedra.
