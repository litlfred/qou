---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-002-2-the-tetrahedral-index
section_title: "The tetrahedral index"
section_number: 2
pages: 4-5
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
The index for a triangulation is built up from thetetrahedron index I∆ : Z2→ Z[[q
1
2 ]],
deﬁned form,e∈ Z by
I∆(m,e )(q) =
∞∑
n=max{0,−e}
(−1)nq
1
2n(n+1)−(n+ 1
2e)m
(q)n(q)n+e
(1)
where (q)n = Πn
i=1(1−qi) is theq-Pochhammer symbol (by convention(q)0 = 1). The index
coincides with the coeﬃcients ofze in the generating function
I(m,q,z ) =
∑
e∈Z
I∆(m,e )(q)ze = (q− m
2 +1z−1;q)∞
(q− m
2 z;q)∞
(2)
where
(z;q)∞ =
∞∏
n=0
(1−zqn). (3)
(see [Gar15]). It follows that for any ﬁxedq∈ C with 0<|q|< 1, the product forI(m,q,z )
converges for allz∈ C with z⁄= 0, and deﬁnes a holomorphic function ofz in the annulus
0<|z|< 1 with Laurent series given by∑
e∈ZI∆(m,e )(q)ze.
A more symmetric version of the tetrahedral index was deﬁned in [GHRS15] fora,b,c ∈ Z
by
J∆(a,b,c ) = (−q
1
2 )−bI∆(b−c,a−b) = (−q
1
2 )−cI∆(c−a,b−c) = (−q
1
2 )−aI∆(a−b,c−a). (4)
Then J∆(a,b,c ) is invariant under all permutations of its argumentsa,b,c and satisﬁes
J∆(a,b,c ) = (−q
1
2 )sJ∆(a +s,b +s,c +s) for alls∈ Z. (5)
In particular, ifa,b≥ 0 then (1) gives
J∆(a,b, 0) =I∆(−a,b ) =q
1
2ab + higher order terms, (6)
and (5) shows that, in general, the lowest degree term inJ∆(a,b,c ) has q-degree
degJ∆(a,b,c ) = 1
2 ((a−m)(b−m) + (b−m)(c−m) + (c−m)(a−m)−m) (7)
and coeﬃcient(−1)m, wherem = min{a,b,c}.
The tetrahedral index also satisﬁes many other interesting algebraic identities including
the quadratic identity ∑
e∈Z
I∆(m,e )I∆(m,e +c)qe =δc,0, (8)
the pentagon identity
∑
e0∈Z
qe0I∆(m1,x 1 +e0)I∆(m2,x 2 +e0)I∆(m1 +m2,x 3 +e0) (9)
=q−x3I∆(m1−x2 +x3,x 1−x3)I∆(m2−x1 +x3,x 2−x3),
and some importantrecurrence relations. (See [Gar15] for the details.)
THE 3D-INDEX AND NORMAL SURF ACES 5
