---
doc_id: arxiv-0902.0350v1
doc_title: "A REVISION OF THE PROOFOF THE KEPLER CONJECTURE"
section_id: sec-002-2-blueprint-edition-of-the-kepler-conjecture
section_title: "Blueprint edition of the Kepler conjecture"
section_number: 2
pages: 5-7
source_pdf: 0902.0350v1.pdf
source_sha256: 4591687132c93973
doc_brief: "A REVISION OF THE PROOFOF THE KEPLER CONJECTURE — The Kepler conjecture asserts that no packing of congruent balls in three-dimensional Euclidean space has density greater than that of the"
---
The blueprint edition of the proof of the Kepler conjecture is a second-
generation proof that contains far more explicit detail than the original
proof. The blueprint edition is available at [18], [19]. Many proofs have been
significantly simplified and systematized. It has been written in a manner
to permit easy formalization. As its name might suggest, this version is
intended as a blueprint for the construction of a formal proof. This section
compares the blueprint edition with the original.
2.1. Lemmas in elementary geometry . A collection of about 200 lem-
mas that can be expressed in elementary terms has been extracted from
the original proof and placed in a separate collection [19]. This has several
advantages. First of all, these lemmas, although elementary, are precisely
the parts of the original proof that put the greatest burden on the reader’s
geometrical intuition. (Many of these lemmas deal with the existence or
non-existence of configurations of several points in R3 subject to various
metric constraints.) Also, the lemmas can be stated without reference to
the Kepler conjecture and all of the machinery that has been introduced to
give a proof. Finally, the proofs of these lemmas rely on similar methods
and are best considered together [16]. Section 3 onEnhanced Automation
gives an approach to proving the lemmas in this collection.
These lemmas can be expressed in the first-order language of the real num-
bers; that is, they can be expressed in the syntax of first-order logic with
equality (allowing quantifiers∀x,∃x with variables running over the real
numbers), the real constants0, 1, and ring operations(+), (−), (·) on R.
In fact, L. Fejes Tóth’s statement of the Kepler conjecture as an optimiza-
tion problem in a finite number of variables can itself be expressed in the
first-order language of the real numbers [45]. (For this, the truncation used
by L. Fejes Tóth must be modified slightly so that the truncated Voronoi
cells are polyhedra.) Thus, it should come as no surprise that many of the
intermediate lemmas in the proof can also be expressed in this manner.
Forexample, considerthestatementassertingtheexistenceofacircumcenter
of a triangle: if three points in the plane are not collinear, then there exists
a point in the plane that is equidistant from all three. This can be expressed
in elementary terms as follows: for every(x1,y 1), (x2,y 2), (x3,y 3), if there
do not existt1,t 2, andt3 for whicht1(x1,y 1) +t2(x2,y 2) +t3(x3,y 3) = (0, 0)
6 HALES, HARRISON, MCLAUGHLIN, NIPKOW, OBUA, AND ZUMKELLER
and t1 +t2 +t3 = 1, then there exists(x,y ) such that
(x−x1)2 + (y−y1)2 = (x−x2)2 + (y−y2)2 = (x−x3)2 + (y−y3)2.
2.2. Background material. There is now a close match between what the
blueprint edition assumes as background and what the proof assistantHOL
Light provides, as described in Section 3. The blueprint edition develops
substantial background material in trigonometry, measure and integration,
hypermaps, and fans (a geometric realization of a hypermap). It turns out
that only a small number ofprimitive volumes need to be computed for the
proof of the Kepler conjecture. These primitives include the volume of a
ball, a tetrahedron, and right circular cone. No line or surface integrals are
required.
A hypermap consists of three permutationse,n,f (on a finite setD) that
compose to the identitye◦n◦f = I. A hypermap is the combinatorial
structure used by Gonthier in his formal proof of the four color theorem. In
2005, the proof of the Kepler conjecture was rewritten in terms of hyper-
maps, because it is better suited for formal proofs than planar graphs.
The Jordan curve theorem (JCT) has been formalized as a step in the Fly-
speck project [20]. In fact, something weaker than the JCT suffices. The
project only uses the JCT for curves on the surface of a unit sphere consist-
ing of a finite number of arcs of great circles; that is, a spherical polygonal
version of the JCT. In the proof of the Kepler conjecture, the combinatorial
structure of a cluster of spheres is encoded as a hypermap. An Euler char-
acteristic calculation, based on the JCT, shows that these hypermaps are
planar. The planarity of these hypermaps is a crucial property that is used
in the enumeration of tame graphs (Section 6). The background chapter in
the blueprint edition contains detailed proofs of these facts.
The blueprint edition contains several introductory essays that introduce
the main concepts in the proof, including the algorithms implemented by
the computer code.
The formalization of the blueprint text started in 2008 with work of J. Rute
(CMU) and the Hanoi Flyspeck group. The current members of this group
are Trần Nam Trung, Nguyễn Tất Thắng, Hoàng Lê Trường, Nguyễn Quang
Trưởng, Vũ Khắc Kỷ, Nguyễn Anh Tâm, Nguyễn Tuyên Hoàng, Nguyễn Đức
Phương, Vương Anh Quyền, Phan Hoàng Chơn, and managed by Tạ Thị
Hoài An. The blueprint formalization is still at an early stage.
A REVISION OF THE PROOF OF THE KEPLER CONJECTURE 7
