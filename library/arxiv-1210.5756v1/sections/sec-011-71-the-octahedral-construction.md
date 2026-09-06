---
doc_id: arxiv-1210.5756v1
doc_title: "Contact Graphs of Unit Sphere Packings Revisited ∗"
section_id: sec-011-71-the-octahedral-construction
section_title: "The Octahedral Construction"
section_number: 7.1
pages: 16-18
source_pdf: 1210.5756v1.pdf
source_sha256: c7546a79a85b8dd5
doc_brief: "Contact Graphs of Unit Sphere Packings Revisited ∗ — The contact graph of an arbitrary ﬁnite packing of unit balls in Euclidean 3-space is the (simple) graph whose vertices correspond to the packing"
---
We now consider an explicit construction of a unit sphere packing placed over the face-centered cubic lattice
for which we obtain a high number of touching triplets and quadruples of unit balls in E3. For any positive
integerk≥ 2, place n(k) = 2k3+k
3 lattice points of the face-centered cubic lattice such that their convex hull
is a regular octahedron K⊂ E3 of edge length 2(k− 1) having exactlyk lattice points along each of its edges
(see Figure 12 for k = 4).
16
Figure 12: The Octahedral Construction for k = 4.
It is not hard to see via layer by layer cross-sections that the number of regular tetrahedra of edge length
2 spanned by the lattice points in K is equal to
2
k−1∑
i=2
2i(i− 1) = 4(k− 2)(k− 1)k
3 .
This means that we can pack n(k) = 2k3+k
3 unit balls forming an octahedral shape in E3 such that there are
exactly N4(k) = 4(k−2)(k−1)k
3 touching quadruples. We note that 3
2n(k) > k3 implies
( 3
2
)2/3
n2/3(k) > k2,
and observe that n(k)<k 3 implies n1/3(k)<k . With these bounds, we can bound N4(k) in terms of n.
N4(k) = 4(k− 2)(k− 1)k
3 = 2
( 2
3k3 + 1
3k
| {z }
n(k)
)
− 4k2 + 2k> 2n(k)− 4
(3
2
)2/3
n2/3(k) + 2n1/3(k) ,
ﬁnishing the proof of (iii) in Theorem 2 on touching quadruples.
We have seen that the number of regular tetrahedra of edge length 2 in the above mentioned Octahedral
Construction is equal to N4(k); we now consider the number of regular triangles of side length 2 spanned by
the lattice points in K and label it by N3(k). We note that the volume of an octahedron of edge length 2 is
8
√
2
3 moreover, the volume of a tetrahedron of edge length 2 is
√
8
3 . Furthermore, the volume of K is equal
to 8
√
2
3 (k− 1)3. Thus, the number of octahedra of edge length 2 in the Octahedral Construction is equal to,
8
√
2
3 (k− 1)3− 4(k−2)(k−1)k
3
√
8
3
8
√
2
3
= (k− 1)3− (k− 2)(k− 1)k
3
We also note that the number of regular triangles of side length 2 of the regular triangle of side length
2(k− 1), which is the face of K, is equal to ( k− 1)2. Hence, the number of regular triangle faces of side
length 2 (i.e., touching triplets) in the Octahedral Construction is,
N3(k) = 1
2
(
4N4(k) + 8((k− 1)3− (k− 2)(k− 1)k
3 (k)) + 8(k− 1)2)
)
= 4
3(k− 1)k(4k− 5) .
Using the bounds introduced before the preceding remark, we can now bound N3(k) in terms of n.
N3(k) = 4
3(k− 1)k(4k− 5) = 8
( 2
3k3 + 1
3k
| {z }
n(k)
)
− 12k2 + 4k> 8n(k)− 12
(3
2
)2/3
n2/3(k) + 4n1/3(k) ,
ﬁnishing the proof of (iii) in Theorem 2 on touching triplets.
17
