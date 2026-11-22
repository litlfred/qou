---
doc_id: s40879-023-00706-0
doc_title: "Bring’s curve: old and new"
section_id: sec-007-3-geometric-points
section_title: "Geometric points"
section_number: 3
pages: 17-19
source_pdf: s40879-023-00706-0.pdf
source_sha256: 4c5af312d2e5d6a7
toc_source: outline
doc_brief: "Bring’s curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
---
We now have a good understanding of how the automorphism group acts on the curve,
and so before looking at quotient Riemann surfaces in Sect.4 we want to ﬁrst consider
orbits of points that have geometric signiﬁcance on the curve. These points will have
important connections to the function theory of the curve; they are also related to
physical aspects of Euclidean realisations (i.e. can be immersed in Euclidean 3-space)
of the curve. Such orbits are characterised by the following result from Wiman.
Proposition 3.1 ([67]) There are only three orbits orbits of points of size less than 120
on B and these have sizes 24, 30, and 60 respectively.
Proof By [27, III.7.7] we know the stabilizer of a point must be a cyclic group. The
cyclic subgroups of S5 are C2, C3, C4, C5, C6; the corresponding orbits would thus
be of (respective) sizes 60, 40, 30, 24 or 20. To obtain Wiman’s result we must show
that C3 does not ﬁx a point on Bring’s curve. Using Riemann–Hurwitz we have
3 = 120(g −1) + 30a60 + 40a40 + 45a30 + 48a24 + 50a20
where ak ⩾0 is the number of S5 orbits of size k. There are no solutions to this for
g ⩾1. For g = 0 we have the unique solution 1 = a60 = a30 = a24. This shows there
can be no points with C3 stabilizer.
These points and corresponding geometric structures are important when relating
Clebsch’s diagonal surface to Hilbert modular surfaces [5, 38]. We identify these orbits
as the geometric points on the curve deﬁned in [60].13 Explicitly they are the vertices,
face-centres, and edge-centres of the the universal map {5, 4}6—the Petrie polygon (as
deﬁned in [14, Section 8.6]) of degree 6 coming from the tiling of the hyperbolic disk
by pentagons, where four meet at a vertex [59]. It is noted in [66] that this tessellation
has a Euclidean realisation as a dodecadodecahedron (Fig.1a). This has 30 vertices,
60 edges, and 24 faces, giving genus
g = 1 −V −E + F
2
= 4,
13 Being a geometric point on a curve is a priori not an interesting statement unless we know the corre-
sponding map is regular, as we have in this case.
3
Page 18 of 46
H.W. Braden, L. Disney-Hogg
(a) Dodecadodecahedron
(b) Small Stellated Dodecahedron
Fig. 1 Geometric realisations, generated in Sagemath
(a) {5, 4} tessellation
(b) {5, 5} tessellation
Fig. 2 Hyperbolic tilings, generated in Sagemath
as we expect. In a recent paper, this connection to the dodecadodecahedron was used
to identify Bring’s curve as the moduli space of equilateral plane pentagons up to the
action of the conformal group [53]. The (small) stellated dodecahedron (Fig.1b) also
has genus 4 (having V = 12 = F, E = 30), coming from the tessellation {5/2, 5} ∼=
{5, 5 | 3}, which can be interpreted as adding three ‘holes’ to the {5, 5} tessellation [14,
Section 8.5]. This {5, 5 | 3} tessellation has automorphism group C2 × A5, which is an
index-2 subgroup of C2 × S5, the automorphism group of {5, 4}6. This is due to the
map D1 deﬁned in [34, Section 3.1], which maps the dodecadodecahedron to the small
stellated dodecahedron. We include both these tessellations in Fig.2. Klein connects
thesmallstellateddodecahedrontoBring’scurvethroughadegree-3coveringB →P1
constructed from the hyperbolic triangles giving the tessellation [66], and we will see
this map later in Sect.5 in a different context.
Bring’s curve: old and new
Page 19 of 46
