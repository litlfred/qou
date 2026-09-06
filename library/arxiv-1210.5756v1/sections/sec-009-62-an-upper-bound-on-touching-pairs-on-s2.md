---
doc_id: arxiv-1210.5756v1
doc_title: "Contact Graphs of Unit Sphere Packings Revisited ∗"
section_id: sec-009-62-an-upper-bound-on-touching-pairs-on-s2
section_title: "An upper bound on touching pairs on S2"
section_number: 6.2
pages: 16-16
source_pdf: 1210.5756v1.pdf
source_sha256: c7546a79a85b8dd5
doc_brief: "Contact Graphs of Unit Sphere Packings Revisited ∗ — The contact graph of an arbitrary ﬁnite packing of unit balls in Euclidean 3-space is the (simple) graph whose vertices correspond to the packing"
---
Our goal is to show that the number of touching pairs in an arbitrary packing of spherical caps of angular
radius π/6 on S2 is at most 25. The proof presented here is indirect and it is based on the previous section.
The details are as follows.
Let X ={x1,..., xN} be a point set on S2 with N≤ 12 and minimum spherical distance π/3 between
any two points in X. Taking the Delaunay triangulation DX of X on S2, we let f be the number of faces,
e be the number of edges, and N be the number of vertices. Since DX is a triangulation of X on S2, every
face is a triangle, and so e = 3
2f. Moreover, just as in the previous section, Euler’s formula implies that
f = 2N− 4.
Now, assume to the contrary that there exist at least 26 touching pairs in a packing of N spherical caps
of angular radius π/6 on S2 with the center points forming X and with N≤ 12. Then e = 3(N− 2)≥ 26
implies that either N = 12 or N = 11.
If N = 12, then f = 20 and e = 30. Hence, the indirect assumption implies that the number of edges
of length > π
3 ofDX is at most 4 and so, there are at most 8 irregular triangles in DX. (Here an irregular
triangle ofDX means a triangle of S2 diﬀerent from the one having side lengths equal to π
3 .) Thus, one can
repeat the proof of the previous section under the case N = 12 leading to a contradiction.
Finally, if N = 11, then f = 18 and e = 27. Hence, the indirect assumption implies that the number of
edges of length > π
3 ofDX is at most 1 and so, there are at most 2 irregular triangles in DX. (Here again
an irregular triangle of DX means a triangle of S2 diﬀerent from the one having side lengths equal to π
3 .)
Thus, one can repeat the proof of the previous section under the case N = 11 leading to a contradiction.
This ﬁnishes our indirect proof on the number of touching pairs in Theorem 3.
