---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-013-45-the-pullback-of-a-shape-assignment-under-a-sy
section_title: "The pullback of a shape assignment under a symmetry"
section_number: 4.5
pages: 13-14
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
the symmetry group of ∆n with S4.
Deﬁnition 4.8. Letσ∈S4 and letz : ∆3
n−2(Z)× ˙∆3
2(Z)→ C\{0, 1} be a map. The pullback
of z under σ is the map given by
(4.8) σ∗z : ∆3
n−2(Z)× ˙∆3
2(Z)→ C\{ 0, 1}, (s,e )↦→ (zσ(e)
σ(s))sgn(σ).
The pullback obviously satisﬁes the standard properties τ∗σ∗ = (στ )∗ and id∗ = id.
Lemma 4.9. The pullback preserves shape assignments.
Proof. Let z be a shape assignment. One easily checks that (4.5) is preserved under the A4
action on the indices, so the result follows for σ∈ A4. Hence, all that remains is to prove
the result for the permutation σ01 switching 0 and 1. The equation
(4.9) ( σ∗
01z)0011
s = (σ∗
01z)1100
s = 1
1− (σ∗
01z)0101
s
is equivalent to
(4.10) ( z0011
σ01(s))−1 = (z1100
σ01(s))−1 = 1
1− (z1001
σ01(s))−1,
which follows from (4.5a) and (4.5b). The other equations are similarly veriﬁed. □
Note that if σ∈A4 is a rotation, the pullback σ∗z is the shape assignment obtained from
z by rotating the simplex by σ. If σ is orientation reversing, one must also replace all the
shape parameters by their inverses.
Remark 4.10. We view the pullback of a shape assignment on an ordered simplex ∆ as
the natural induced shape assignment on the simplex ∆′ obtained from ∆ by reordering the
vertices such that the ith vertex of ∆′ is the σ(i)th vertex of ∆.
0
1
3
20
3
2
1
z0110
0021(σ∗z)0101
0210
0
1
3
20
1
3
2 z0110
0021
(σ∗z)0101
0210
Figure 8. Reordering byσ = (123). Figure 9. Pullback by σ = (123).
14 STA VROS GAROUF ALIDIS, MATTHIAS GOERNER, AND CHRISTIAN K. ZICKERT
