---
doc_id: arxiv-1210.5756v1
doc_title: "Contact Graphs of Unit Sphere Packings Revisited ∗"
section_id: sec-005-4-proof-of-i-in-theorem-2-using-theorem-3
section_title: "Proof of (i) in Theorem 2 using Theorem 3"
section_number: 4
pages: 7-8
source_pdf: 1210.5756v1.pdf
source_sha256: c7546a79a85b8dd5
toc_source: outline
doc_brief: "Contact Graphs of Unit Sphere Packings Revisited ∗ — The contact graph of an arbitrary ﬁnite packing of unit balls in Euclidean 3-space is the (simple) graph whose vertices correspond to the packing"
---
Proof of (i) in Theorem 2 using Theorem 3
Let P be an arbitrary packing of n unit balls in E3. Let B stand for the unit ball centered at the origin of
E3 and let P = {c1 +B, ..., cn +B}. Then, we take the contact graph G(P) of P whose vertices are c1, ..., cn
with an edge connected between two vertices if ci + B and cj + B touch each other, i.e., dist(ci, cj) = 2.
Every touching triplet ci + B, cj + B, and ck + B (resp. touching quadruple ci + B, cj + B, ck + B, and
cl + B) of P corresponds to a regular triangle spanned by ci, cj, and ck (resp. regular tetrahedron spanned
by ci, cj, ck, and cl) of edge length 2 in G(P).
Lemma 3. The number of regular triangles (resp., regular tetrahedra) of edge length 2 sharing a vertex in
G(P) is at most 25 (resp., 11).
7
Figure 4: Projecting a spherical cap between two unit balls.
Proof. Let the unit balls ci + B and cj + B of P be touching. Then the central projection of cj + B from ci
onto the boundary of ci +B is a spherical cap of angular radius π/6, as seen in Figure 4. By projecting each
unit ball cj + B of P that touches ci + B onto the boundary of ci + B, we get a packing of spherical caps of
angular radius of π/6 on the boundary of ci + B. Therefore, Theorem 3 ﬁnishes the proof of Lemma 3.
We now prove the desired upper bound on the number of the regular triangles of edge length 2 in G(P).
By Lemma 3, we have that there are at most 25 regular triangles in the contact graph G(P) sharing a vertex,
so we count 25n touching triplets in P. Yet, since each triplet is counted at each of the three vertices of
the regular triangles, we divide by three to avoid over counting, thus leading to the bound of at most 25n
3
touching triplets in P. Finally, using Lemma 3 again, a similar counting argument yields that the number
of regular tetrahedra of edge length 2 in G(P) is at most 11n
4 .
