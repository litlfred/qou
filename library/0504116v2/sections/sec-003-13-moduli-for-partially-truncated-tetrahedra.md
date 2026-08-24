---
doc_id: 0504116v2
doc_title: "On deformations of hyperbolic 3-manifolds with geodesic boundary"
section_id: sec-003-13-moduli-for-partially-truncated-tetrahedra
section_title: "Moduli for partially truncated tetrahedra"
section_number: 1.3
pages: 4-6
source_pdf: 0504116v2.pdf
source_sha256: 24a8c998e40aed5d
doc_brief: "On deformations of hyperbolic 3-manifolds with geodesic boundary (Frigerio, AGT 6 (2006) 435–457) — the solution variety of consistency equations for a geometric partially truncated triangulation…"
---
The following result implies that the dihedral angles can be used as moduli for geometric
tetrahedra.
Theorem 1.3 Let ∆ be a partially truncated tetrahedron and let ∆(1) be the set of
edges of ∆. The geometric realizations of ∆ are parameterized up to isometry by
the dihedral angle assignmentsθ : ∆(1)→ (0,π ) such that for each vertex v of ∆, if
e1, e2, e3 are the edges that emanate from v, thenθ(e1) +θ(e2) +θ(e3) is equal toπ
for ideal v and less thanπ for non-ideal v.
Having introduced moduli for geometric tetrahedra, our next task is to determine, given
a triangulated manifold, which values of moduli deﬁne a global hyperbolic structure on
the manifold. The following well-known hyperbolic trigonometry formulae will prove
useful later:
Lemma 1.4 With notation as in Figure 2 we have
cosh a1 = (cosα2· cosα3 + cosα1)/(sinα2· sinα3),
cosh b1 = (cosh c2· cosh c3 + cosh c1)/(sinh c2· sinh c3).
Algebraic &GeometricTopology 6 (2006)
Deforming hyperbolic 3–manifolds with boundary 439
α2
b3
a1
a2
a3
b3 b2
b1
c2 c3
c1 = 0c1
b1
b2
c3c2
α3
α1
Figure 2: A triangle, a right-angled hexagon and a pentagon with four right angles and an ideal
vertex
Let now ∆ be a partially truncated tetrahedron with edges e1,..., e6 as in Figure 3.
We ﬁx a geometric realization θ of ∆ determined by the dihedral angles θi = θ(ei)
for i = 1,..., 6 and we denote by Lθ the length with respect to this realization.
The boundary edges of the lateral hexagons of ∆ correspond to the pairs of distinct
non-opposite edges{ei, ej}, and will be denoted by eij. Note that eij disappears towards
inﬁnity, so it has length 0, when the common vertex of ei and ej is ideal. Lemma 1.4
readily implies
(1) cosh Lθ(e12) = (cosθ1· cosθ2 + cosθ3)/(sinθ1· sinθ2).
Note that this result is correct also when the common end of e1 and e2 is ideal.
e6
e1 e5
e3
e2
e4
θ6
θ2
θ3
θ4
θ5
θ1
Figure 3: Notation for edges and dihedral angles of a truncated tetrahedron
Turning to the length of an internal edge, we note that the edge is an inﬁnite half-line or
an inﬁnite line when one or both its ends are ideal, respectively. Otherwise the length
is computed using Lemma 1.4. With notation as in Figure 3, and deﬁning vijk as the
Algebraic &GeometricTopology 6 (2006)
440 Roberto Frigerio
vertex from which the edges ei, ej, ek emanate, we set:
cθ(e1) = cosθ1· (cosθ3· cosθ6 + cosθ2· cosθ5)
+ cosθ2· cosθ6 + cosθ3· cosθ5 + cosθ4· sin2θ1;
dθ(v123) = 2 cosθ1· cosθ2· cosθ3 + cos2θ1 + cos2θ2 + cos2θ3− 1.
Proposition 1.5 dθ(v123) = 0 if and only if the vertex v123 is ideal. If v123 and v156
are both non-ideal then
(2) cosh Lθ(e1) = cθ(e1)
/√
dθ(v123)· dθ(v156).
Remark 1.6 Let ∆ be a partially truncated tetrahedron without ideal vertices. Then
the geometric realizations of ∆ are parameterized by the lengths of the internal edges.
In fact, the map that associates to the dihedral angles of a geometric realization of ∆
the lengths of its internal edges is a diffeomorphism between open subsets of R6.
