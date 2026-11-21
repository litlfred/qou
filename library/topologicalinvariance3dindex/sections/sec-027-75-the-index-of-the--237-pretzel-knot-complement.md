---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-027-75-the-index-of-the--237-pretzel-knot-complement
section_title: "The index of the (-2,3,7) pretzel knot complement"
section_number: 7.5
pages: 47-48
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
toc_source: outline
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
is the 12 crossing knot 12n242 in the census. The default SnapPy triangulation T of the
12n242 complement uses 3 ideal tetrahedra. The Epstein-Penner decomposition TEP uses 3
ideal tetrahedra. However, the two triangulations T and TEP are combinatorially dierent; for
instance have edge-valencies 5, 6, 7 and 5, 5, 8 respectively. Nevertheless, both triangulations
48 STAVROS GAROUFALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
are geometric with canonical strict angle structure and are related by geometric 23 moves,
which preserve the index. The angle structure equations of T are given by:
A =


1
0
0
0
1
1
1
1
1


B =


0
1
0
1
1
0
1
0
2


C =


1
1
2
1
0
0
0
1
0

.
Apply the following operations on (A|B|C):
• Permute the rows according to (123) 7→(312).
• Permute the second and third columns of A and simultaneously, of B and C.
• If ¯a1, ¯b1, ¯c1 are the 
rst columns of A, B and C, then permute (¯a1|¯b1|¯c1) 7→(¯b1|¯c1|¯a1).
After the above permutations, the matrix (A|B|C) of the (−2, 3, 7) pretzel knot becomes
the corresponding matrix of the 52 knot. Since the above permutations do not change the
index, it follows that I(−2,3,7)(0) = I52(0).
Exercise 7.2. Using the matrix (A|B|C) above, it follows that the index of T is given by
(35)
I(−2,3,7)(0)(q) =
X
(k1,k2)∈Z2
(−1)k2q
1
2 (k1−2k2)I∆(k1, −k2)I∆(−k1 +k2, k1)I∆(−2k1 +2k2, k1 −2k2).
On the other hand, the index of 52 is given by Equation (33). Using the identities of the
tetrahedron index from Section 4, show that
X
(k1,k2)∈Z2
I∆(−k1, k1 −k2)2I∆(2k1 −2k2, −k1) =
X
(k1,k2)∈Z2
(−1)k2q
1
2 (k1−2k2)I∆(k1, −k2)I∆(−k1 + k2, k1)I∆(−2k1 + 2k2, k1 −2k2).
