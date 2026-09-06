---
doc_id: arxiv-1206.5522v6
doc_title: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS"
section_id: sec-004-23-manifolds-with-boundary
section_title: "Manifolds with boundary"
section_number: 2.3
pages: 11-12
source_pdf: 1206.5522v6.pdf
source_sha256: 6e992242435b5e9f
doc_brief: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS — Factorization homology theories of topological manifolds , after Beilinson, Drinfeld and Lurie, are homology-type theories for topological"
---
boundary.
Deﬁnition 2.14. Mﬂd∂
n is the symmetric monoidal topological category of topological n-manifolds,
possibly with boundary, which have ﬁnite good covers by Euclidean sp aces Rn and upper half spaces
R≥0× Rn−1. Morphisms are open embeddings which map boundary to boundary. Disk∂
n is the full
symmetric monoidal topological subcategory of Mﬂd∂
n consisting of ﬁnite disjoint unions of Rn and
R≥0× Rn−1.
Remark 2.15. The category Disk∂
n is designed to be minimal with respect to the condition that any
ﬁnite subset of an n-manifold with boundary has an open neighborhood homeomorphic to an object
of Disk∂
n. In particular, the closed n-disk Dn is consequently not an object of Disk∂
n.
The following property is essential.
Proposition 2.16. The functor
R≥0×− : Mﬂdn−1−→ Mﬂd∂
n
is homotopically fully faithful. That is, for every pair of (n− 1)-manifolds M and N , the map
Emb(M, N )−→ Emb
(
R≥0× M, R≥0× N
)
is a homotopy equivalence.
Proof. This follows by the standard method of pushing oﬀ to inﬁnity in the R≥0 direction (as in
the Alexander trick or the contractibility of foliations on Rn up to integrable homotopy). That is,
deﬁne a deformation retraction onto the subspace Emb(M, N ) by deﬁning for each t∈ [0, 1] the map
ht : Emb
(
R≥0× M, R≥0× N
)
−→ Emb
(
R≥0× M, R≥0× N
)
by
ht(g)(s, x) =
{ (s, g0(x)) for s < (1− t)−1− 1
g(s + 1− (1− t)−1, x) for s≥ (1− t)−1− 1
where g0 :֒→N is the restriction of g at the value s = 0.
□
11
Remark 2.17. Together with the Kister–Mazur Theorem [Ki], the previous propos ition implies that
the map
Top(n− 1)֒→Emb(R≥0× Rn−1, R≥0× Rn−1)
is a homotopy equivalence. Likewise, Disk∂
n is an unoriented variant of the Swiss cheese operad of
Voronov [Vo]. Namely, the framed variant Disk∂,fr
n is homotopy equivalent to the PROP associated
to the Swiss cheese operad.
