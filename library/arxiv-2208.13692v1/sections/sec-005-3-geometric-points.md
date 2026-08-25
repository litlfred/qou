---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-005-3-geometric-points
section_title: "Geometric Points"
section_number: 3
pages: 12-13
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
doc_brief: "Bring's curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
We now have a good understanding of how the automorphism group acts on the curve,
and so before looking at quotient Riemann surfaces in §4 we want to ﬁrst consider orbits
of points that have geometric signiﬁcance on the curve. These points will have important
connections to the function theory of the curve; they are also related to physical aspects of
Euclidean realisations (i.e. can be immersed in Euclidean 3-space) of the curve. Such orbits
are characterised by the following result from Wiman.
BRING’S CUR VE: OLD AND NEW 13
Proposition 3.1 ([Wim95]). There are only 3 orbits orbits of points of size less than 120
onB and these have sizes 24, 30, and 60 respectively.
Proof. By [FK92, III.7.7] we know the stabilizer of a point must be a cyclic group. The
cyclic subgroups of S5 are C2, C3, C4, C5, C6; the corresponding orbits would thus be of
(respective) sizes 60, 40, 30, 24 or 20. To obtain Wiman’s result we must show that C3 does
not ﬁx a point on Bring’s curve. Using Riemann-Hurwitz we have
3 = 120(g− 1) + 30a60 + 40a40 + 45a30 + 48a24 + 50a20
whereak≥ 0 are the number of S5 orbits of size k. There are no solutions to this for g≥ 1.
Forg = 0 we have the unique solution 1 = a60 = a30 = a24. This shows there can be no
points with C3 stabilizer. □
These points and corresponding geometric structures are important when relating Cleb-
sch’s diagonal surface to Hilbert modular surfaces [Hir76, Bel04]. We identify these orbits as
the geometric points on the curve deﬁned in [SW97].10 Explicitly they are the vertices, face-
centres, and edge-centres of the the universal map{5, 4}6 - the Petrie polygon (as deﬁned in
[CM80, §8.6]) of degree 6 coming from the tiling of the hyperbolic disk by pentagons, where
4 meet at a vertex [Sin88]. It is noted in [Web05] that this tessellation has a Euclidean
realisation as a dodecadodecahedron (Figure 1a). This has 30 vertices, 60 edges, and 24
faces, giving genus
g = 1− V−E +F
2 = 4,
as we expect. In a recent paper, this connection to the dodecadodecahedron was used to
identify Bring’s curve as the moduli space of equilateral plane pentagons up to the action of
the conformal group [Ram22]. The (small) stellated dodecahedron (Figure 1b) also has genus
4 (having V = 12 = F , E = 30), coming from the tessellation {5/2, 5}∼={5, 5|3}, which
can be interpreted as adding 3 ‘holes’ to the {5, 5} tessellation [CM80, §8.5]. This {5, 5|3}
tessellation has automorphism group C2×A5, which is an index-2 subgroup of C2×S5, the
automorphism group of {5, 4}6. This is due to the map D1 deﬁned in [Hen13, §3.1], which
maps the dodecadodecahedron to the small sellated dodecahedron. We include both these
tessellations in Figure 2 below. Klein connects the small stellated dodecahedron to Bring’s
curve through a degree-3 coveringB→ P1 constructed from the hyperbolic triangles giving
the tessellation [Web05], and we will see this map later in §5 in a diﬀerent context.
