---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-008-41-the-tetrahedron-index-and-its-properties
section_title: "The tetrahedron index and its properties"
section_number: 4.1
pages: 16-17
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
toc_source: outline
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
nition
and the identities satis
ed by the tetrahedron index of [DGG13]. For a detailed discussion,
see [Garb].
The building block of the index IT of an ideal triangulation T is the tetrahedron index
I∆(m, e)(q) ∈Z[[q1/2]] de
ned by
(5)
I∆(m, e) =
∞
X
n=(−e)+
(−1)nq
1
2 n(n+1)−(n+ 1
2 e)m
(q)n(q)n+e
where
e+ = max{0, e}
and (q)n = Qn
i=1(1 −qi). If we wish, we can sum in the above equation over the integers,
with the understanding that 1/(q)n = 0 for n < 0.
The tetrahedron index satis
es the following linear recursion relations
(6a)
q
e
2I∆(m + 1, e) + q−m
2 I∆(m, e + 1) −I∆(m, e) = 0
(6b)
q
e
2I∆(m −1, e) + q−m
2 I∆(m, e −1) −I∆(m, e) = 0
and
(7a)
I∆(m, e + 1) + (qe+ m
2 −q−m
2 −q
m
2 )I∆(m, e) + I∆(m, e −1) = 0
(7b)
I∆(m + 1, e) + (q−e
2 −m −q−e
2 −q
e
2)I∆(m, e) + I∆(m −1, e) = 0
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD
17
and the duality identity
(8)
I∆(m, e)(q) = I∆(−e, −m)
and the triality identity
(9)
I∆(m, e)(q) = (−q
1
2)−eI∆(e, −e −m)(q) = (−q
1
2)mI∆(−e −m, m)(q)
and the pentagon identity
(10) I∆(m1 −e2, e1)I∆(m2 −e1, e2) =
X
e3∈Z
qe3I∆(m1, e1 +e3)I∆(m2, e2 +e3)I∆(m1 +m2, e3) ,
and the quadratic identity
(11)
X
e∈Z
I∆(m, e)I∆(m, e + c)qe = δc,0 =

1 if c = 0
0 if c̸ = 0
The above relations are valid for all integers m, e, mi, ei, c.
