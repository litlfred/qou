---
doc_id: arxiv-1208.1663v2
doc_title: "The 3D index of an ideal triangulation and angle structures"
section_id: sec-017-65-an-ideal-triangulation-with-no-index-structur
section_title: "An ideal triangulation with no index structure"
section_number: 6.5
pages: 22-23
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
doc_brief: "The 3D index of an ideal triangulation and angle structures — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
T which contains an edge e and a tetrahedron ∆ 1 such that goes around e ﬁve times with
shapes Z, Z′, Z′, Z′′ and Z′′. Suppose that no other tetrahedron touches e. Then the
equation for a generalized angle structure around e reads
α + 2β + 2γ = 2, α +β +γ = 1
This forces α = 0 so no generalized angle structure has α> 0. Note that the corresponding
gluing equations around the edge e reads
z(z′)2(z′′)2 = 1, zz ′z′′ =−1, z ′ = (1−z)−1
which forces z = 1. Thus the gluing equations have no non-degenerate solution, i.e., no
solution with shapes in C\{ 0, 1}.
More complicated examples can be arranged using special conﬁgurations of two or more
edges and tetrahedra. In all examples that we could generate with no index structure, the
triangulation is degenerate.
Of course, the arguments of a shape solution to the gluing equations is a generalized angle
structure. The latter, however, need not be an index structure if some of the shapes are real,
or have negative imaginary part; see for instance the triangulation of m064 in Section 6.4.
6.6. Invariance under the 2↔ 0 move. The next lemma implies the invariance of the
index of an ideal triangulation under a 2 ↔ 0 move. Such a move is also known as a
pillowcase move, described in detail in [9, Sec.6].
Lemma 6.3. For integersm,e,c we have
∑
e
I∆(m,e )I∆(m,e +c)qe =δc,0.
Proof. Equations (B.1) and (B.2) imply that
∑
e
I∆(m,e )xe = (q−m
2 +1x−1)∞
(q−m
2x)∞
.
THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES 23
Since
(q−m
2 +1x−1)∞
(q−m
2x)∞
· (q−m
2 +1(qx−1)−1)∞
(q−m
2 (qx−1))∞
= 1,
it follows that ∑
e,e′
I∆(m,e )xeI∆(m,e′)qe′
x−e′
= 1.
Therefore, ∑
e,e′:e−e′=c
I∆(m,e )I∆(m,e′)qe′
=δc,0.
This implies that ∑
e′
I∆(m,e′ +c)I∆(m,e′)qe′
=δc,0.
The result follows. □
