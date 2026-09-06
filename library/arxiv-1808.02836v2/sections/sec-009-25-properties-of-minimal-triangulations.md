---
doc_id: arxiv-1808.02836v2
doc_title: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds"
section_id: sec-009-25-properties-of-minimal-triangulations
section_title: "Properties of minimal triangulations"
section_number: 2.5
pages: 6-7
source_pdf: 1808.02836v2.pdf
source_sha256: 0224a296253122a2
---
An ideal triangulation of a topologically ﬁnite 3–manifold M is minimal if it uses the smallest number of
simplices in an ideal triangulation of M. The number of ideal simplices in a minimal ideal triangulation of M
is denoted c(M) and termed the complexity of M.
We assume that the reader is familiar with normal surface theory. We refer to [36] for a thorough introduction,
but remark that we only need to study closed normal surfaces in ideal triangulations.
An ideal triangulation of M is 0–efﬁcient if no normal surface is a 2–sphere. An ideal triangulation of M
is ∂ –efﬁcient if it has the property that any closed normal surface that is isotopic to a vertex linking surface
is normally isotopic to that vertex-linking surface. A normal isotopy is an isotopy of M that preserves each
simplex of each dimension.
Theorem 4 Suppose M is the interior of a compact, irreducible, ∂ –irreducible anannular 3–manifold. Then
each minimal ideal triangulation of M is 0–efﬁcient and ∂ –efﬁcient.
Proof It is shown in [17, Corollary 7.3] that each minimal triangulation of M is 0–efﬁcient. In [19, Theorem
4.7], the existence of a ∂ –efﬁcient triangulation is proven by a crushing method. Since crushing reduces the
number of tetrahedra, this means that a triangulation that fails to be ∂ –efﬁcient is not minimal.
We now give a deﬁnition of what we mean by an ideal edge to be homotopic or isotopic into the boundary .
The key is that intermediate paths in the homotopy are not allowed to pass through the ideal vertices, except for
their endpoints. The reader is reminded than an ideal edge of M is an edge of ˆM. An expanded discussion of
the following material can be found in [14].
A path homotopy (resp. isotopy) 1 H : [0,1]× [0,1]→ ˆM between two edge paths is admissible if H( (0,1)×
[0,1] )⊂ M, where the ﬁrst factor parametrises the paths. The edge path γ is admissibly null-homotopic
(resp. null-isotopic) if there is a path homotopy (resp. isotopy) H : [0,1]× [0,1]→ ˆM with H(x,0) = γ(x),
H(x,1) = γ(0) for all x∈ [0,1] and H( (0,1)× [0,1) )⊂ M.
We say that an ideal edge e of M is homotopic (resp. isotopic) into the boundary if it is admissibly null-
homotopic (resp. null-isotopic) in ˆM.
Corollary 5 Suppose M is the interior of a compact, irreducible, ∂ –irreducible anannular 3–manifold other
than a 3–ball, and T is a minimal ideal triangulation of M. Then no ideal edge is isotopic into the boundary.
In particular, no edge in ˆM bounds an embedded disc in ˆM.
Proof Suppose the edge e is isotopic into the boundary. Choose a compact core Mc of M with the property
that each boundary component of Mc is a vertex linking surface. There exists an embedded disc D in Mc
whose boundary consists of e∩ Mc and a subarc on a boundary component B of Mc. The boundary of a
regular neighbourhood of B∪ D has two components; one is a vertex linking surface normally isotopic to B
and the other is a surface S isotopic to B and disjoint from e. Since S is incompressible and not a 2–sphere
and M is irreducible, it follows that there is a normal surface isotopic but not normally isotopic to B. Since
the triangulation is ∂ –efﬁcient according to Theorem 4, it follows that M is homeomorphic with S× (0,1).
However, this contradicts our topological hypotheses on M.
1i.e. a homotopy (resp. isotopy) keeping endpoints ﬁxed
6
Note that the above result does not apply to the unique minimal ideal triangulation T of the 3–ball. This is
the 1–tetrahedron, 1–vertex triangulation of S3 with the vertex removed. The triangulation of S3 has precisely
two edges; one is a trefoil knot in S3 and the other the unknot in S3. The former gives an ideal edge in T that
is only homotopic into the boundary, whilst the latter is isotopic into the boundary. The above proofs breaks
down for the 3–ball because the surface S in the proof shrinks to a sphere contained in a tetrahedron.
We now specialise to the class of manifolds of interest, namely cusped hyperbolic 3–manifolds, where more
speciﬁc results can be shown about their minimal triangulations. In order to limit the cases to consider, we not
only assume that all vertex links are of Euler characteristic zero, but also that the manifolds are orientable.
