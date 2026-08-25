---
doc_id: sigma12-065
doc_title: ""
section_id: sec-003-31-special-points-of-the-hulekcraig-representati
section_title: "Special points of the Hulek–Craig representation and desingularisation"
section_number: 3.1
pages: 4-4
source_pdf: sigma12-065.pdf
source_sha256: a6e0e0da5cc5ff9b
doc_brief: "Bring’s Curve: its Period Matrix and the Vector of Riemann Constants ⋆ — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
---
The points at infinity for the HC curve (2.1) are given by (the real points) [0 , 1, 0] and [1, 0, 0],
but the latter is singular. In fact the singularities of the HC curve are [1 , 0, 0] and [ζk,ζ 2k, 1]
for k∈{ 0,..., 4} so we must work out expansions nearby in order to form a properly compact
curve.
First the infinite singularity: consider the structure near [1 , 0, 0], say at points [1 ,y,z ] for
small y, z. The curve reduces to
y5 +z5 +y2z2−yz− 2y3z3 = 0,
so in the usual Puiseux construction we suppose z = Ayα +··· . Equating lowest order terms
we get one of
• A5y5α−Ayα+1 = 0 which implies z =y1/4 +··· , that is z≈y1/4 near this point,
• y5−Ayα+1 = 0 which implies z =y4 +··· or z≈y4.
The second of these gives a single z for each y near 0, the first gives four different values for z.
Together these make up the expected five sheets and so expansions after this point are unique.
Thus in the vicinity of [1, 0, 0] solutions [1,y,z ] of the first equation behave as [1,t 4,t ] wheret is
a local parameter for the curve. Similarly the second equation has solutions behaving as [1 ,t,t 4]
in terms of a local parameter. Thus the point [1 , 0, 0] desingularises into precisely two points on
the nonsingular curve:
[1, 0, 0]1∼
[
1,t 4,t
]
, [1, 0, 0]2∼
[
1,t,t 4]
, (3.1)
where∼ here indicates behaviour of a local coordinate in the vicinity of a specified point.
For the remaining singular points we only need to investigate explicitly one and then note
that the automorphism [x,y,z ]↦→ [ζx,ζ 2y,z ] will tell us how the other singularities behave. So
we look at [1 , 1, 1]. At first sight, two of the sheets come together here. Consider [1 + ϵ,y, 1]
near to [1, 1, 1]. To first order
y5− 2y3 +y2−y + 1 = 0.
This quintic has four distinct roots: two are complex, corresponding to nonsingular points and
will play no role in future developments. There is a real negative root α∼− 1.7549 which also
corresponds to a nonsingular point and will occur later. Finally, 1 is a root, which gives us the
expected singularity at [1, 1, 1].
Expanding about this singular point, at the next order we discover
y = 1 +ϵ−1 +
√
5
2 +··· , y = 1 +ϵ−1−
√
5
2 +··· .
These are clearly distinct solutions and together with the nonsingular expansions exhaust the
five possible nonsingular preimages near x = 1, so [1 , 1, 1] once again desingularises to two
distinct points.
