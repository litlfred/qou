---
doc_id: 0504116v2
doc_title: "On deformations of hyperbolic 3–manifolds with geodesic boundary ROBERTO FRIGERIO Let M be a complete ﬁnite-volume hyperbolic 3–manifold with compact non-empty geodesic boundary an"
section_id: sec-005-15-exceptional-hexagons
section_title: "Exceptional hexagons"
section_number: 1.5
pages: 7-9
source_pdf: 0504116v2.pdf
source_sha256: 24a8c998e40aed5d
doc_brief: "On deformations of hyperbolic 3-manifolds with geodesic boundary (Frigerio, AGT 6 (2006) 435–457) — the solution variety of consistency equations for a geometric partially truncated triangulation…"
---
It is easily seen that gluings match ideal vertices to each other, because these notions
are part of the initial topological information about a triangulation. When a pairing
glues two compact lateral hexagons, to be sure that the gluing is an isometric one we
may equivalently require the lengths of the internal edges or those of the boundary
edges to match under the gluing. On the other hand, sinceT is a good triangulation, a
non-compact lateral hexagon F is actually a pentagon with four right angles and an ideal
vertex: we shall say in this case that F is an exceptional lateral hexagon. By Lemma 1.4,
the isometry class of an exceptional lateral hexagon is determined by the lengths of its
boundary edges. However, in order to end up with a non-redundant set of consistency
equations, it is convenient to ﬁnd an alternative approach to moduli for exceptional
hexagons. To this aim we need now to be slightly more careful about orientation than
we have been so far. Namely, we choose on the tetrahedra an orientation compatible
with a global orientation of the manifold. As a result also the lateral hexagons have a
ﬁxed orientation, and the gluing maps reverse the orientation of the hexagons.
So, let us consider an exceptional hexagon F∗
126 as in Figure 4, and recall that the
hexagon is oriented and embedded in H3 byθ. We consider the horospheres O1 and
Algebraic &GeometricTopology 6 (2006)
442 Roberto Frigerio
R RR1 R2
α1 α2
e16
e6
e26
Figure 5: Notation for the proof of Proposition 1.8
O2 centred at e12 and passing through the non-ideal ends of e1 and e2 respectively. We
deﬁne σθ(F126) to be±dist(O1, O2), the sign being positive if e2, e12, e1 are arranged
positively on∂F∗
126 and O1 is contained in the horoball bounded by O2, or if e2, e12, e1
are arranged negatively on∂F∗
126 and O2 is contained in the horoball bounded by O1,
and negative otherwise. Together with equation 1, the following proposition allows to
computeσ in terms of the dihedral angles.
Proposition 1.8 We have
(3) σθ(F126) = ln(sinh Lθ(e16)/ sinh Lθ(e26)).
Proof Letα1,α 2 and R, R1, R2 be the angles and lengths shown in Figure 5. An easy
computation in the upper half-plane model of H2 shows that Lθ(ei6) = ln cot(αi/2)
for i = 1, 2. Moreover we have R = R1· tanα1 = R2· tanα2, so expσθ(F126) =
R1/R2 = tanα2/ tanα1. Now for i = 1, 2 we have tanαi = 2 cot(αi/2)/(cot2(αi/2)−
1) = 2 exp Lθ(ei6)/(exp(2Lθ(ei6))− 1). Combining these equations we ﬁnally get
expσθ(F126) = sinh Lθ(e16)/ sinh Lθ(e26).
We now deﬁne 𝓁θ(F126) to be the length of e6. The next proposition shows that
the functions σ and 𝓁 provide a parameterization of isometry classes of exceptional
hexagons.
Algebraic &GeometricTopology 6 (2006)
Deforming hyperbolic 3–manifolds with boundary 443
Proposition 1.9 Let F and F′ be paired exceptional lateral hexagons. Their pairing
can be realized by an isometry if and only ifσθ(F) +σθ(F′) = 0 and𝓁θ(F) =𝓁θ(F′).
Proof We concentrate on the “if” part of the statement, the “only if” part being obvious.
Let f1, f2 and f′
1, f′
2 be the boundary edges of of F and F′ respectively, and assume that
the orientation-reversing pairing between F and F′ glues f1 to f′
2 and f′
1 to f2. Since
𝓁θ(F) =𝓁θ(F′), Lemma 1.4 easily implies that L(f1) ⩽ L(f′
2) if and only if L(f2) > L(f′
1).
Moreover the assumption that σθ(F) =−σθ(F′) and Proposition 1.8 give L(f1) ⩽ L(f′
2)
if and only if L(f2) ⩽ L(f′
1). This forces L(f1) = L(f′
2) and L(f2) = L(f′
1), whence the
conclusion.
Remark 1.10 Let ∆ be a partially truncated tetrahedron and suppose that v is the
unique ideal vertex of ∆. Let F1, F2, F3 be the faces of ∆ incident to v and for
i = 1, 2, 3 let ei be the edge of Fi not containing v. The isometry classes of the
geometric realizations of ∆ are parameterized by the lengths of the ei’s and the values
taken by σ on the Fi’s. More precisely, the map that associates to any geometric
realizationθ of ∆ the point (Lθ(e1), Lθ(e2), Lθ(e3),σθ(F1),σθ(F2),σθ(F3)) deﬁnes a
diffeomorphism between open subsets of two afﬁne hyperplanes of R6.
