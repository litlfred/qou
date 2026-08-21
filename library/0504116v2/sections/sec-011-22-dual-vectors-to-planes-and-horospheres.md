---
doc_id: 0504116v2
doc_title: "On deformations of hyperbolic 3-manifolds with geodesic boundary"
section_id: sec-011-22-dual-vectors-to-planes-and-horospheres
section_title: "Dual vectors to planes and horospheres"
section_number: 2.2
pages: 14-15
source_pdf: 0504116v2.pdf
source_sha256: 24a8c998e40aed5d
doc_brief: "On deformations of hyperbolic 3-manifolds with geodesic boundary (Frigerio, AGT 6 (2006) 435–457) — the solution variety of consistency equations for a geometric partially truncated triangulation…"
---
If S∈S gd, by construction the image of S under the developing map Dt is contained in
a totally geodesic immersed surface in H3. It is easily seen that such a surface must in
turn be contained in a geodesic plane ˆS(t) of H3. We now need to associate to each ˆS(t)
a suitable ultra-ideal point bS(t), which will be called the dual point of ˆS(t). Such point
naturally lies in 4–dimensional Minkowsky space, so we ﬁx some notation about this
space.
We denote by M 3+1 the space R4 with coordinates x0, x1, x2, x3 endowed with the
Lorentzian inner product⟨x, y⟩ =−x0y0 + x1y1 + x2y2 + x3y3. We set
H3
− = {x∈ M 3+1 : ⟨x, x⟩ =−1, x0> 0},
H3
+ = {x∈ M 3+1 : ⟨x, x⟩ = 1},
L3
+ = {x∈ M 3+1 : ⟨x, x⟩ = 0, x0> 0}.
We recall thatH3
− is the upper sheet of the two-sheeted hyperboloid, and that⟨· ,·⟩
restricts to a Riemannian metric on H3
−. With this metric, H3
− is the so-called
hyperboloid model H3
hyp of hyperbolic space. The one-sheeted hyperboloid H3
+
turns out to have a bijective correspondence with the set of hyperbolic half-spaces in
H3
hyp. Given b∈H 3
+, the corresponding half-space, called the dual of b, is given by
{v∈H 3
− : ⟨v, b⟩ ⩽ 0}. Similarly, the cone L3
+ of future-oriented light-like vectors of
M 3+1 corresponds to the set of horospheres in H3
hyp. The horosphere dual to u∈ L3
+
is given by{v∈H 3
− : ⟨v, u⟩ =−1}.
Note now that for any S∈S gd the set Dt(~N) locally lies on a deﬁnite side of ˆS(t), so
we can deﬁne bS(t) to be the dual vector to the half-space that locally contains Dt(~N)
and is bounded by ˆS(t).
When S belongs toSpar a vector bS(t)∈ L3
+ can also be deﬁned as follows: take an
oriented edge ~f of ~T ending in S and set bS(t) to be the unique point in L3
+ with
Algebraic &GeometricTopology 6 (2006)
Deforming hyperbolic 3–manifolds with boundary 449
x0(bS(t)) = 1 which projects to the endpoint of Dt(~f ) in ∂H3. Such an endpoint exists
because Dt(~f ) is a geodesic, and is clearly independent of the choice of~f , so bS(t) is
indeed well-deﬁned. Since developing maps vary smoothly with respect to t we have
the following:
Lemma 2.5 For any S∈S gd∪S par the map t↦→ bS(t) is smooth with respect to t.
