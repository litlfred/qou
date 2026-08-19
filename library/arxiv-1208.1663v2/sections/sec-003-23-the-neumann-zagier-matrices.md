---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES STAVROS GAROUFALIDIS With an appendix by Sander Zwegers"
section_id: sec-003-23-the-neumann-zagier-matrices
section_title: "The Neumann-Zagier matrices"
section_number: 2.3
pages: 5-7
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES STAVROS GAROUFALIDIS With an appendix by Sander Zwegers — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of"
---
tetrahedra of a 3-manifold M with torii boundary components. Sssign variables Zi,Z′
i,Z′′
i
at the opposite edges of each tetrahedron ∆ i respecting its orientation as in Figure 2.
Then we can read oﬀ matrices N×N matrices ¯A, ¯B and ¯C whose rows are indexed by
the N edges ofT and whose columns are indexed by the Zi,Z′
i,Z′′
i variables. These are the
2The sum of the 3 angles around each vertex is traditionally π.
6 STA VROS GAROUF ALIDIS
Figure 2. Shapes of a tetrahedron.
so-called Neumann-Zagier matrices that encode the exponents of the gluing equations ofT ,
originally introduced by Thurston [20, 25]. In terms of these matrices, a generalized angle
structure is a triple of vectors α,β,γ ∈ RN that satisfy the equations
(2.7) ¯Aα + ¯Bβ + ¯Cγ = (2,..., 2)T, α +β +γ = (1,..., 1)T.
A quadQ forT is a choice of pair of opposite edges at each tetrahedron ∆ i fori = 1,...,N .
Q can be used to eliminate one of the three variables αi,βi,γi at each tetrahedron using the
relation αi +βi +γi = 1. Doing so, Equations (2.7) take the form
Aα + Bγ =ν.
The matrices ( A|B) have some key symplectic properties, discovered by Neumann-Zagier
whenM is a hyperbolic 3-manifold (andT is well-adapted to the hyperbolic structure) [20],
and later generalized to the case of arbitrary 3-manifolds in [19]. Neumann-Zagier show that
the rank of (A|B) isN−r, wherer is the number of boundary components ofM; all assumed
torii. If we choose N−r linearly independent rows of (A|B), then we obtain matrices (A′|B′)
and a vector ν′, which combine to M = (A′|B′|ν′). In addition, the exponents of meridian
and longitude loops at each boundary torus give additional matrices ( aT,bT ) and (cT,dT ) of
size r× 2N.
Deﬁnition 2.11. The 3D index ofT is deﬁned by
(2.8) IT (m,e )(q) =IM(dm−be,−cm +ae)(q)
Implicit in the above deﬁnition is a choice of quad Q and a choice of rows to remove.
However, the index is independent of these choices; see Remark 2.8. Keep in mind the
action of ( Z/3)N given by acting on the ith columns ¯ai, ¯bi and ¯ci of ¯A, ¯B and ¯C by
S(¯ai|¯bi|¯ci) = (¯bi|¯ci|¯ai),
(and ﬁxing all other columns) and on the ith coordinates of an angle structure by
S(αi,βi,γi) = (βi,γi,αi)
(and ﬁxing all other coordinates) and on the ith columns ai and bi of A and B by
S(ai|bi|ν) = (−bi|ai−bi|ν−bi).
(and ﬁxing all other columns). Since the rank of ( A|B) is N−r and A, B are (N−r)×N
matrices, it follows that M admits a strict structure if and only T admits a strict angle
structure. In addition, T admits an index structure if for every choice of quad Q there
THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES 7
exist a solution (α,β,γ ) of Equations (2.7) that satisﬁes the inequalities (2.2). Theorem 2.4
implies the following.
Theorem 2.12. The index IT : Zr× Zr−→ Z((q1/2)) is well-deﬁned if and only if T admits
an index structure. In particular, IT exists ifT admits a strict angle structure.
See Section 6.3 for an example of an ideal triangulation T of the census manifold m136 [3]
which admits a semi-strict angle structure (i.e., angles are nonnegative real numbers), does
not admit a strict angle structure, and which has a solution of the gluing equations that
recover the complete hyperbolic structure. A case-by-case analysis shows that this example
admits an index structure, thus the index IT exists. This example appears in [11, Example
7.7]. We thank H. Segerman for a detailed analysis of this example.
