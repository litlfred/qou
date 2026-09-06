---
doc_id: arxiv-2108.09349v2
doc_title: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS BARBARA NIMERSHIEM"
section_id: sec-013-41-the-triangulations-are-veering
section_title: "The triangulations are veering"
section_number: 4.1
pages: 16-17
source_pdf: 2108.09349v2.pdf
source_sha256: 4c732bfcbf3dfb16
---
Pachner moves eliminated the obstructions and
Proposition 4.1. Each triangulation τp is veering.
Proof. With the exception of s, the tetrahedra in τp have an upward orientation induced by the
product region containing the 6-braid, which is how the non- s tetrahedra of τp are ﬂattened in
Figure 8. Flatten s as indicated in the same ﬁgure. In each tetrahedron, assign an angle of π to
the diagonal edges and an angle of 0 to the others. Use red to color the 01 and 25 edges of each
wi and w′
i; the edges s(bc) and s(ad); and the top diagonal of w′
0 along with the bottom diagonal
of wp. (These are exactly the edges colored red in Figure 8.) Color the remaining edges blue. We
claim this coloring forms a veering angle structure on τp, which is also transverse taut.
By Observation 1, the edges in the equivalence class [ w′
0(01)] are exactly the edges colored red.
Thus, the blue edges compose the remaining equivalence classes, and the colorings are consistent
with the face pairings that form M.
GEOMETRIC TRIANGULATIONS OF A F AMILY OF HYPERBOLIC 3-BRAIDS 17
Next we show that the assignment of angles forms a taut angle structure. The angle assignments
themselves guarantee Conditions (1) and (2) of Deﬁnition 3.1 as well as the requirement that taut
angle structures have angles in {0,π}. Only diagonals are assigned an angle of π, so, if there are
exactly two diagonals in each equivalence class, Condition (3) will also be met (the angle sum around
each edge is 2π).
The class [ w′
0(01)], whose members are listed in Observation 1, contains exactly two diago-
nals, w′
0(02) and wp(02). The degree 5 edges of Xp are completely described in Observation 2.
The edges [w′
0(05)] and [w′
0(12)] each contain exactly two diagonals: The top diagonal w1(15) is
matched with the bottom diagonal w′
p−1(51) and similarly for w′
1(02) and wp−1(20) (or s(db) and
s(ac) when p = 1, which completes this case).
To check the remaining 2p− 2 edges of Xp forp> 1, i.e., those of degree 4, we examine wi−1(02)
and w′
i−1(15), the bottom diagonals of wi−1 and w′
i−1 in the braid complement in Figure 8. The
edge wi−1(02) bounds both wi−1(012) and wi−1(025). After passing through the σ1 half-twist, the
ﬁrst of these faces is rotated to the back and identiﬁed with w′
i(102), whereas the second stays in
front and is identiﬁed withwi(125). These faces share the edge 12, which, after another σ1 is twisted
to the back and identiﬁed to w′
i+1(02). A similar argument applies to w′
i−1(15). Symbolically,
wi−1(02)∼wi(12) =w′
i(12)∼w′
i+1(02) for i = 2,...p − 2.
w′
i−1(15)∼wi(05) =w′
i(05)∼wi+1(15) for i = 1,...p − 1. (2)
The only diagonals are the 02 and 15 edges, so the edge classes, [wi(12)] and [wi(05)], contain exactly
twoπ angles as required. The remaining degree-4 edges contain the diagonals of s,s(ac) and s(bd).
The identiﬁcations in Table 5 show that their equivalence classes contain exactly one other diagonal:
s(ac)∼w′
1(21) =w1(21)∼w′
2(20)
s(bd)∼w′
p−1(21) =wp−1(21)∼wp−2(20). (3)
With exactly two diagonals in each equivalence class, the angle structure is taut. Each tetrahedron
appears as in Figure 9, and the gluings of Table 5 identify bottom faces to top faces, so the “upward”
orientations are consistent, forming a transverse taut angle structure, which is also layered. □
Corollary 4.2. The triangulation τp admits a positive angle structure.
Proof. In their main result, [12, Theorem 1.5], Hodgson, Rubinstein, Segerman, and Tillmann prove
that veering triangulations admit positive angle structures (which they call strict angle structures).
A constructive proof showing how to deform a veering angle structure to a positive angle structure
has also been given by Futer and Gu´ eritaud [6, Theorem 1.3]. □
