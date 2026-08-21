---
doc_id: arxiv-1208.1663v2
doc_title: "The 3D index of an ideal triangulation and angle structures"
section_id: sec-021-appendix-b-the-tetrahedron-index-and-the-quantum
section_title: "Appendix B. The tetrahedron index and the quantum dilogarithm"
section_number: null
pages: 27-28
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
doc_brief: "The 3D index of an ideal triangulation and angle structures — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
Gukov-Gaiotto-Dimofte came up with the beautiful formula (1.2)for the tetrahedron in-
dex from a Fourier transform of the quantum dilogarithm. For completeness, we include
this relation here, taken from [5]. The quantum dilogarithm of Faddeev and Kashaev is a
fundamental building block of quantum topology [8, 14, 13]. The q-series version of this
analytic function is given by
(B.1) L(m,x,q ) = (q−m
2 +1x−1)∞
(q−m
2x)∞
∈ Z((x))[[q1/2]]
We claim that
(B.2)
∑
e
I(m,e )(q)xe =L(m,x,q ).
To prove this, use the deﬁnition of I(m,e ), shift e toe−n and use the ﬁrst two identities of
Lemma A.1. We get
∑
e
I(m,e )(q)xe =
∑
n,e
(−1)nq
1
2n(n+1)−(n+ 1
2e)mxe
(q)n(q)n+e
=
∑
n,e
(−1)nq
1
2n(n+1)(
q−m
2x−1)n(
q−m
2x
)e
(q)n(q)e
= (q−m
2 +1x−1)∞
(q−m
2x)∞
.
Each of the recursion relations (3.1a), (3.1b), (3.3a) and (3.3b) is equivalent to the corre-
sponding relation (B.3a)-(B.3d) for the generating series L(m,x,q )
(B.3a) ( −1 +q−m
2x−1)L(m,x,q ) +L(m + 1,q
m
2x,q ) = 0
(B.3b) (1 −q−m
2x−1)L(m,x,q ) +L(m− 1,q
m
2x,q ) = 0
28 STA VROS GAROUF ALIDIS
(B.3c) (1 + x2− (q
m
2 +q−m
2 ))L(m,x,q ) +xq
m
2L(m,qx,q ) = 0
(B.3d)
L(m−2,x,q )−(L(m−1,q
1
2x,q )+L(m−1,q− 1
2x,q )−q1−mL(m−1,q− 1
2x,q ))+L(m,x,q ) = 0
Equations (B.3a)-(B.3d) are easy to verify using the fact that L(m,q,x ) is a proper hyper-
geometric function of (m,q ). This gives an alternative proof of part (a) of Theorem 3.7.
Observe ﬁnally that the recursions (3.1a) and (3.1b) have a solution space of rank 2. On
the other hand, the recursions (B.3a) and (B.3b) have a solution space of rank 1.
