---
doc_id: arxiv-1208.1663v2
doc_title: "The 3D index of an ideal triangulation and angle structures"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
doc_brief: "The 3D index of an ideal triangulation and angle structures — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
2. Index structures, angle structures and the 3D index 3
2.1. Index structures 3
2.2. Angle structures 5
2.3. The Neumann-Zagier matrices 5
2.4. On the topological invariance of the index 7
3. Axioms for the tetrahedron index 8
4. Properties of a tetrahedron index 10
4.1. Part (d) of Theorem 3.2 10
4.2. The rank of V : part (a) of Theorem 3.2 10
4.3. The rank of V+: part (b) of Theorem 3.2 11
4.4. Proof of triality: part (c) of Theorem 3.2 12
4.5. I∆ is a tetrahedron index 13
4.6. The degree of I∆ 13
4.7. Proof of Theorem 3.7 13
5. Convergence of the 3D index 14
5.1. Proof of Theorem 2.4 14
5.2. An independent proof of convergence for strict index structures 16
Date: October 6, 2015.
Supported in part by NSF grant DMS-11-05678.
1991 Mathematics Classiﬁcation. Primary 57N10. Secondary 57M25.
Key words and phrases: 3D index, tetrahedron index, quantum dilogarithm, gluing equations, Neumann-
Zagier equations, hyperbolic geometry, ideal triangulations, 2-3 moves, pentagon, angle structures, index
structures, q-holonomic sequences.
1
arXiv:1208.1663v2  [math.GT]  7 Oct 2015
2 STA VROS GAROUF ALIDIS
6. Invariance of the 3D index under 2 ↔ 3 moves and 2↔ 0 moves 18
6.1. Invariance under the 3 → 2 move 18
6.2. Invariance under the 2 → 3 move 20
6.3. An ideal triangulation of m136 21
6.4. An ideal triangulation of m064 21
6.5. An ideal triangulation with no index structure 22
6.6. Invariance under the 2 ↔ 0 move 22
6.7. Acknowledgment 23
Appendix A. I∆ satisﬁes the pentagon identity 23
A.1. A generating series proof of the pentagon identity 23
A.2. A second proof of the pentagon identity 26
Appendix B. The tetrahedron index and the quantum dilogarithm 27
References 28
1. Introduction
In a series of papers [6, 5], Dimofte-Gaiotto-Gukov studied topological gauge theories using
as input an ideal triangulationT of a 3-manifoldM. These gauge theories play an important
role in
• Chern-Simons perturbation theory (that ﬁts well with the earlier work on quantum
Riemann surfaces of [4] and the later work on the perturbative invariants of [7]),
• categoriﬁcation and Khovanov Homology, that ﬁts with the earlier work [28].
Although the gauge theory depends on the ideal triangulationT , and the 3D index in general
may not converge, physics predicts that the gauge theory ought to be a topological invariant
of the underlying 3-manifold M. When ∂M consists of r torii, the low energy description of
these gauge theories gives rise to a partially deﬁned function
(1.1)
I :{ideal triangulations}−→ Z((q1/2))Zr×Zr
, T ↦→IT (m1,...,m r,e 1,...,e r)∈ Z((q1/2))
for integers mi and ei, which is invariant under some partial 2-3 moves. The building block
of the 3D index IT is the tetrahedron indexI∆(m,e )(q)∈ Z[[q1/2]] deﬁned by 1
(1.2) I∆(m,e ) =
∞∑
n=(−e)+
(−1)nq
1
2n(n+1)−(n+ 1
2e)m
(q)n(q)n+e
where
e+ = max{0,e}
and (q)n =∏n
i=1(1−qi). If we wish, we can sum in the above equation over the integers,
with the understanding that 1/(q)n = 0 for n< 0.
Roughly, the 3D index IT of an ideal triangulation T is a sum over tuples of integers
of a ﬁnite product of tetrahedron indices evaluated at some linear forms in the summation
1The variables (m,e ) are named after the magnetic and electric charges of [5].
THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES 3
variables. Convergence of such sums is not obvious, and not always expected on physics
grounds. For instance, the following sum
∑
e∈Z
I∆(0,e )qve
converges in Z((q1/2)) if and only if v >0. This follows easily from the fact that the degree
δ(e) of the summand is given by
δ(e) =e +
{
0 if e≥ 0
e2
2− e
2 if e≤ 0
Our goal is to
(a) prove that the 3D index IT exists if and only if T admits an index structure (a
generalization of a strict angle structure); see Theorem 2.12 below.
(b) give a complete axiomatic deﬁnition of the tetrahedron index I∆ focusing on the
combinatorial and q-holonomic aspects; see Section 3.
(c) to show that the 3D index is invariant under 3 → 2 moves, but not in general under
2→ 3 moves, and give a necessary and suﬃcient criterion for invariance under 2↔ 3
moves; see Section 6.
