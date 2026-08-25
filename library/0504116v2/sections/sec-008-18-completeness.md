---
doc_id: 0504116v2
doc_title: "On deformations of hyperbolic 3-manifolds with geodesic boundary"
section_id: sec-008-18-completeness
section_title: "Completeness"
section_number: 1.8
pages: 11-12
source_pdf: 0504116v2.pdf
source_sha256: 24a8c998e40aed5d
doc_brief: "On deformations of hyperbolic 3-manifolds with geodesic boundary (Frigerio, AGT 6 (2006) 435–457) — the solution variety of consistency equations for a geometric partially truncated triangulation…"
---
Let T1,..., Tk be the boundary tori of ¯N . From now on we denote by µi,λ i a ﬁxed
basis of H1(Ti; Z)∼= π1(Ti), i = 1,..., k. Any point in Ω(T ) naturally deﬁnes an
Aff(C)–structure on Ti (see eg, [1, 5]). For x∈ Ω(T ), we denote by ai(x)∈ C (resp. by
bi(x)∈ C) the linear component of the holonomy ofµi (resp. ofλi) corresponding to
the Aff(C)–structure deﬁned by x on Ti. It is well-known that the hyperbolic structure
deﬁned by x on N induces a complete metric on the ith cusp of N if and only if
ai(x) = bi(x) = 1. Moreover, one can explicitly compute ai and bi in terms of the
dihedral angles as follows.
Let ∆ be a tetrahedron inT , let v be an ideal vertex of ∆ and Lx(v) be the (similarity
class of the) Euclidean triangle obtained by intersecting the geometric realization of
∆ parameterized by x with a small horosphere centred at v. The tetrahedron being
oriented, this triangle is also oriented, so, once a vertex p of Lx(v) is ﬁxed, we can
associate to the similarity structure of Lx(v) the unique complex number zx(L(v), p)
such that Lx(v) is carried to the Euclidean triangle with vertices 0 , 1, zx(L(v), p) by
an orientation-preserving similarity sending p to 0. Suppose that e1, e2, e3 are the
internal edges emanating form v, and that they are positively arranged around v. If
p = L(v123)∩ e1, then
zx(L(v123), p) = (sinθ2/sinθ3)· eiθ1.
If γ is an oriented simplicial loop on Ti and q is a vertex of γ , then the set of all
triangles touchingγ in q and lying on the right ofγ is well-deﬁned and will be denoted
by R(γ, q). Moreover, we shall denote by V(γ) the set of vertices of γ . Let ˆµi, ˆλi be
simplicial loops on Ti representingµi,λ i. The following result is proved in [15, 1].
Algebraic &GeometricTopology 6 (2006)
446 Roberto Frigerio
Proposition 1.13 We have
ai(x) = (−1)#V( ˆµi)·∏
q∈V( ˆµi)
∏
T∈R( ˆµi,q) zx(T, q),
bi(x) = (−1)#V( ˆλi)·∏
q∈V( ˆλi)
∏
T∈R( ˆλi,q) zx(T, q).
As a consequence of Mostow–Prasad’s rigidity Theorem for hyperbolic manifolds with
geodesic boundary [7, 4] we get the following:
Theorem 1.14 There exists at most one point in Ω(T ) that deﬁnes on N a complete
hyperbolic structure with geodesic boundary.
Proof See [7].
