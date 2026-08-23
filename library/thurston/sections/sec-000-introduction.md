---
doc_id: thurston
doc_title: "The Geometry and Topology of Three-Manifolds"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 3-9
source_pdf: Thurston.pdf
source_sha256: 6010919ed83edd81
doc_brief: "The Geometry and Topology of Three-Manifolds — 22 sections: Introduction; GEOMETRY AND THREE-MANIFOLDS; Start with the three sphereS3, whi"
---
These notes (through p. 9.80) are based on my course at Princeton in 1978–
79. Large portions were written by Bill Floyd and Steve Kerckho↵. Chapter 7, by
John Milnor, is based on a lecture he gave in my course; the ghostwriter was Steve
Kerckho↵. The notes are projected to continue at least through the next academic
year. The intent is to describe the very strong connection between geometry and low-
dimensional topology in a way which will be useful and accessible (with some e↵ort)
to graduate students and mathematicians working in related ﬁelds, particularly 3-
manifolds and Kleinian groups.
Much of the material or technique is new, and more of it was new to me. As
a consequence, I did not always know where I was going, and the discussion often
tends to wanter. The countryside is scenic, however, and it is fun to tramp around if
you keep your eyes alert and don’t get lost. The tendency to meander rather than to
follow the quickest linear route is especially pronounced in chapters 8 and 9, where
I only gradually saw the usefulness of “train tracks” and the value of mapping out
some global information about the structure of the set of simple geodesic on surfaces.
I would be grateful to hear any suggestions or corrections from readers, since
changes are fairly easy to make at this stage. In particular, bibliographical informa-
tion is missing in many places, and I would like to solicit references (perhaps in the
form of preprints) and historical information.
Thurston — The Geometry and Topology of 3-Manifolds iii
Contents
Introduction iii
Chapter 1. Geometry and three-manifolds 1
Chapter 2. Elliptic and hyperbolic geometry 9
2.1. The Poincar´ e disk model. 10
2.2. The southern hemisphere. 11
2.3. The upper half-space model. 12
2.4. The projective model. 13
2.5. The sphere of imaginary radius. 16
2.6. Trigonometry. 17
Chapter 3. Geometric structures on manifolds 27
3.1. A hyperbolic structure on the ﬁgure-eight knot complement. 29
3.2. A hyperbolic manifold with geodesic boundary. 31
3.3. The Whitehead link complement. 32
3.4. The Borromean rings complement. 33
3.5. The developing map. 34
3.8. Horospheres. 38
3.9. Hyperbolic surfaces obtained from ideal triangles. 40
3.10. Hyperbolic manifolds obtained by gluing ideal polyhedra. 42
Chapter 4. Hyperbolic Dehn surgery 45
4.1. Ideal tetrahedra in H3.4 5
4.2. Gluing consistency conditions. 48
4.3. Hyperbolic structure on the ﬁgure-eight knot complement. 50
4.4. The completion of hyperbolic three-manifolds obtained from ideal
polyhedra. 54
4.5. The generalized Dehn surgery invariant. 56
4.6. Dehn surgery on the ﬁgure-eight knot. 58
4.8. Degeneration of hyperbolic structures. 61
4.10. Incompressible surfaces in the ﬁgure-eight knot complement. 71
Thurston — The Geometry and Topology of 3-Manifolds v
CONTENTS
Chapter 5. Flexibility and rigidity of geometric structures 85
5.2. 86
5.3. 88
5.4. Special algebraic properties of groups of isometries of H3. 92
5.5. The dimension of the deformation space of a hyperbolic three-manifold. 96
5.7. 101
5.8. Generalized Dehn surgery and hyperbolic structures. 102
5.9. A Proof of Mostow’s Theorem. 106
5.10. A decomposition of complete hyperbolic manifolds. 112
5.11. Complete hyperbolic manifolds with bounded volume. 116
5.12. Jørgensen’s Theorem. 119
Chapter 6. Gromov’s invariant and the volume of a hyperbolic manifold 123
6.1. Gromov’s invariant 123
6.3. Gromov’s proof of Mostow’s Theorem 129
6.5. Manifolds with Boundary 134
6.6. Ordinals 138
6.7. Commensurability 140
6.8. Some Examples 144
Chapter 7. Computation of volume 157
7.1. The Lobachevsky function l(✓). 157
7.2. 160
7.3. 165
7.4. 167
References 170
Chapter 8. Kleinian groups 171
8.1. The limit set 171
8.2. The domain of discontinuity 174
8.3. Convex hyperbolic manifolds 176
8.4. Geometrically ﬁnite groups 180
8.5. The geometry of the boundary of the convex hull 185
8.6. Measuring laminations 189
8.7. Quasi-Fuchsian groups 191
8.8. Uncrumpled surfaces 199
8.9. The structure of geodesic laminations: train tracks 204
8.10. Realizing laminations in three-manifolds 208
8.11. The structure of cusps 216
8.12. Harmonic functions and ergodicity 219
vi Thurston — The Geometry and Topology of 3-Manifolds
CONTENTS
Chapter 9. Algebraic convergence 225
9.1. Limits of discrete groups 225
9.3. The ending of an end 233
9.4. Taming the topology of an end 240
9.5. Interpolating negatively curved surfaces 242
9.6. Strong convergence from algebraic convergence 257
9.7. Realizations of geodesic laminations for surface groups with extra cusps,
with a digression on stereographic coordinates 261
9.9. Ergodicity of the geodesic ﬂow 277
NOTE 283
Chapter 11. Deforming Kleinian manifolds by homeomorphisms of the sphere
at inﬁnity 285
11.1. Extensions of vector ﬁelds 285
Chapter 13. Orbifolds 297
13.1. Some examples of quotient spaces. 297
13.2. Basic deﬁnitions. 300
13.3. Two-dimensional orbifolds. 308
13.4. Fibrations. 318
13.5. Tetrahedral orbifolds. 323
13.6. Andreev’s theorem and generalizations. 330
13.7. Constructing patterns of circles. 337
13.8. A geometric compactiﬁcation for the Teichm¨ uller spaces of polygonal
orbifolds 346
13.9. A geometric compactiﬁcation for the deformation spaces of certain
Kleinian groups. 350
Index 357
Thurston — The Geometry and Topology of 3-Manifolds vii
CHAPTER 1
