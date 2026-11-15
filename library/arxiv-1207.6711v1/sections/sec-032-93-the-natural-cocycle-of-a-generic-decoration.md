---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-032-93-the-natural-cocycle-of-a-generic-decoration
section_title: "The natural cocycle of a generic decoration"
section_number: 9.3
pages: 29-31
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
decorations naturally give rise to cocycles on M.
Deﬁnition 9.8. A pair (g0N, g1N) of N-cosets in SL(n, C) is suﬃciently generic if there
exists a (necessarily unique) g ∈SL(n, C) such that
(9.3)
(g0N, g1N) = g(N, qN), with q counter-diagonal.
A tuple is suﬃciently generic if it is pairwise suﬃciently generic.
Let N −denote the lower triangular matrices in SL(n, C) with 1’s on the diagonal.
30
STAVROS GAROUFALIDIS, MATTHIAS GOERNER, AND CHRISTIAN K. ZICKERT
Deﬁnition 9.9. An element n ∈B is normalized if the last column vector consists of 1’s.
An element n−∈N −in normalized if the ﬁrst column vector consists of 1’s.
Deﬁnition 9.10. A triple (g0B, g1B, g2B) of B-cosets in PGL(n, C) is suﬃciently generic
if there exists a (necessarily unique) g ∈PGL(n, C) such that
(9.4)
(g0B, g1B, g2B) = g(B, q1B, n−B), with n−∈N −normalized.
A tuple is suﬃciently generic if each triple is suﬃciently generic.
Remark 9.11. A simple exercise in linear algebra shows that generic (as in Deﬁnition 8.6)
implies suﬃciently generic.
Deﬁnition 9.12. Let (g0N, g1N, g2N, g3N) be a generic SL(n, C)/N-decoration on ∆3
n. The
natural (SL(n, C), N)-cocycle on ∆3
n is the coboundary of the unique 0-cochain τ satisfying
(9.5)
(gv0N, gv1N) = τ v0v1(N, qN) with q counter diagonal.
This deﬁnes the map Lαβ in (1.5). It follows immediately from the deﬁnition that the
natural cocycle labels short edges by elements in N and long edges by counter diagonal
elements. Let q1 denote the counter diagonal matrix whose non-zero entries are all 1. Note
that q1 = q−1
1 .
Deﬁnition 9.13. Let (g0B, g1B, g2B, g3B) be a generic decoration on a simplex. The natural
(PGL(n, C), B, H)-cocycle on ∆3
n is the coboundary of the unique 0-cochain τ satisfying
(9.6)
(gv0B, gv1B, gv2B) = τ v0v1v2(B, q1B, n−B) with n−∈N −normalized.
This deﬁnes the map Lαβγ in (1.5).
Remark 9.14. Note that a (G, H)-cocycle σ on ∆determines a G/H-decoration D on ∆.
We say that D is compatible with σ. To see this note that σ is the coboundary of a 0-cochain
τ on ∆, which is unique up to left multiplication by an element in G. The value of τ at the
vertices near a vertex of ∆are all in the same H-coset. Hence, we have a decoration on ∆.
Similarly, a (G, B, H)-cocycle on ∆determines a G/B-decoration on ∆. It follows that the
maps Lαβ and Lαβγ are bijective with explicit inverses.
Lemma 9.15. Let D = (g0B, g1B, g2B, g3B) be a generic decoration on a simplex. The
natural (PGL(n, C), B, H)-cocycle is the unique cocycle, which is compatible with the dec-
oration and satisﬁes
(i) Short edges are labeled by elements in H.
(ii) Middle edges are labeled by normalized elements in B.
(iii) Long edges are labeled by q1.
Proof. We ﬁrst show that the natural cocycle satisﬁes the three conditions. It is enough to
prove this for a single edge of each type. We may assume that D = (B, q1, B, n−B, m−B)
where n−, m−∈N −and n−is normalized.
Then τ 012 = 1, so for each edge starting
at 012, we only need to compute the value of τ at the end point. Since (q1B, B, n−B) =
q1(B, q1B, q1n−B), and the ﬁrst column vector of q1n−consists of 1’s, it follows that τ 102 = q1,
proving the result for the long edges. Since the stabilizer of B is B, it follows that τ 021 ∈B,
GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS
31
proving the result for the middle edges. Finally, τ 013 is the unique element in H such that
hm−h−1 is normalized, proving the result for the short edges.
Let σ1 and σ2 be two cocycles satisfying the required conditions. Since any two cocycles
diﬀer by the coboundary action, σ2 = ησ1 for some coboundary η. Since long edges are
labeled by q1 and since the cocycles determine the same decoration, we may assume that
η takes values in H. It is now elementary to check that if η is not the identity, either (ii)
or (iii) fails.
□
Remark 9.16. Note that for a generic decoration on a triangulation of M, the natural
cocycles on each simplex ﬁt together to form a natural cocycle on M.
