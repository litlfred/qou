---
doc_id: 0406242v4
doc_title: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements FRANC¸ OIS GUÉRITAUD APPENDIX BY DA VIDFUTER"
section_id: sec-008-63-behavior-of-the-volume-functional
section_title: "Behavior of the volume functional"
section_number: 6.3
pages: 17-19
source_pdf: 0406242v4.pdf
source_sha256: 27e48b483007b824
---
As a consequence of Lemma 6.2, to prove Theorem 1.1 we only need to ﬁnd a critical
point of the volume functionalV in the open polyhedron P of cyclic sequences (wi)
satisfying the conditions (3). A few more facts about the volume of ideal hyperbolic
tetrahedra will be needed.
By Proposition 6.1, the volume functionalV continuously extends to the (compact)
closure ¯P of the polyhedron P (the space ¯P is deﬁned by turning the conditions
(3) to weak inequalities, or taking the limits in Rm of sequences of P). Then V has
well-deﬁned extrema on ¯P, which are automatically critical if they belong toP. Because
Geometry &Topology 10 (2006)
1256 Franc ¸ois Gu´eritaud and David Futer
of the following proposition, the only possibility for a critical point is to be an absolute
maximum.
Proposition 6.6 The volume of an ideal tetrahedron is a concave function of its dihedral
angles.
Proof This follows from Proposition 6.1, whose notations we use again: xt, yt, zt are
the dihedral angles. By symmetry we may assume x0, y0≤π/2. Assume further that
xt, yt, zt are afﬁne functions of t with ﬁrst-degree coefﬁcients X, Y, Z. Proposition 6.1
implies−dV/dt = X log sinxt + Y log sinyt + Z log sinzt , and by differentiating we
obtain
−d2V/dt2|t=0 = X2 cot x0 + Y2 cot y0 + Z2 cot z0
= X2 cot x0 + Y2 cot y0 + (X + Y)2 1− cot x0 cot y0
cot x0 + cot y0
= (X + Y)2 + (X cot x0− Y cot y0)2
cot x0 + cot y0
≥ 0.
As a consequence, the volume functional V is also concave on ¯P and Theorem 1.1
holds if the maximum ofV is interior. Next we explore the behavior of V near the
boundary of ¯P.
Proposition 6.7 (Simple degeneracy) If (Qt)t≥0 is a smooth family of ideal tetrahedra
with dihedral angles xt, yt, zt such that x0, y0∈ (0,π ); z0 = 0 and dzt
dt|t=0 > 0, then
dV
dt|t=0 = +∞.
Proof Simply check that the right hand side of (5) goes to 0 as t goes to 0. We call
this situation simple degeneracy because the limiting triangle has only one vanishing
angle (two of its vertices are therefore collapsed).
Proposition 6.8 (Double degeneracy) If (Qt)t≥0 is a smooth family of ideal tetrahedra
satisfying (x0, y0, z0) = (0, 0,π ) and d
dt|t=0(xt, yt, zt) = (1 + λ, 1− λ,−2) with
λ∈ (−1, 1), then
exp−dV
dt
⏐⏐⏐
t=0
= 1−λ2
4
(1 +λ
1−λ
)λ
.
Proof As t goes to 0, one has sin xt∼ (1 +λ)t and sin yt∼ (1−λ)t and sin zt∼ 2t.
The right hand side of (5) is thus equivalent to
(
(1 +λ)t
)1+λ(
(1−λ)t
)1−λ(2t)−2 = 1−λ2
4
(1 +λ
1−λ
)λ
.
Geometry &Topology 10 (2006)
Canonical triangulations 1257
We call this situationdouble degeneracy because the limiting triangle has two vanishing
angles (its vertices are distinct, but collinear). At a double degeneracy, the volume has
directional derivatives, but no well-deﬁned differential.
