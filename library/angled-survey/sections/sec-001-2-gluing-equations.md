---
doc_id: angled-survey
doc_title: "Contemporary Mathematics From angled triangulations to hyperbolic structures"
section_id: sec-001-2-gluing-equations
section_title: "Gluing equations"
section_number: 2
pages: 3-7
source_pdf: angled-survey.pdf
source_sha256: 8b49e682a39848bc
toc_source: inferred
---
deﬁnition of the polytope of angle structures A(τ) and compute its dimension. In
Section 4, we introduce a natural set of tangent vectors, called leading–trailing
deformations, which span the tangent space TpA(τ). In Section 5, we focus on the
volume functional V : A(τ) →R. We will show that the gluing equations for τ
are in 1–1 correspondence with the leading–trailing deformations; in particular, the
non-linear part of a gluing equation is satisﬁed if and only if the derivative of V
vanishes along the corresponding deformation. It will follow that the full system of
gluing equations is satisﬁed at p ∈A(τ) if and only p is a critical point of V.
1.2. Extending and applying the method. Section 6, at the end of the
paper, surveys some of the ways in which the Casson–Rivin program has been
generalized and applied. Among the generalizations are versions of Theorem 1.2
for manifolds with polyhedral boundary (Theorem 6.2) and Dehn ﬁllings of cusped
manifolds (Theorem 6.1). Another generalization of the method considers angles
modulo 2π: we discuss this brieﬂy while referring to Luo’s paper in this volume
[14] for a much more thorough treatment.
Among the applications are explicit constructions of the hyperbolic metric on
several families of 3–manifolds, including punctured torus bundles [11], certain link
complements [9], and “generic” Dehn ﬁllings of multi-cusped manifolds [12]. For
each of these families of manifolds, the volume associated to any angle structure
gives useful lower bounds on the hyperbolic volume of the manifold: see Theorem
6.3. For each of these families of manifolds, certain angle inequalities obtained while
proving that V : A(τ) →R has a critical point also imply that the combinatorially
natural triangulation τ is in fact the geometrically canonical way to subdivide M.
See Section 6.5 for details.
Finally, the behavior of the volume functional V : A(τ) →R gives a surprising
and short proof of Weil’s local rigidity theorem for hyperbolic metrics [32]. Because
V is strictly concave down (Lemma 5.3), any critical point of V on A(τ) must be
unique.
As a result, there is only one complete metric on M in which all the
161
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
4
DAVID FUTER AND FRANC¸ OIS GU´ERITAUD
tetrahedra of τ are positively oriented. This turns out to imply Weil’s local rigidity
theorem, as we shall show in Theorem 6.4.
1.3. A reader’s guide. For a relative novice to this subject, we recommend
the following strategy. Skim over Section 2, as needed, to recall the crucial deﬁni-
tions of gluing equations and holonomy. Read carefully the deﬁnitions and opening
discussion of Sections 3 and 4, but skip the proofs in those sections entirely. Then,
proceed directly to Section 5, where the computation of Proposition 5.4 is par-
ticularly important.
This computation almost immediately implies the forward
direction of Theorem 1.2. On the other hand, the linear–algebra results in Sections
3 and 4 involve completely diﬀerent ideas compared to the rest of the paper, and
are only needed for the reverse direction of Theorem 1.2 (complete metric implies
critical point of V) and for various applications in Section 6.
For a practical example of the method, the reader may also study the proof of
[11, Lemma 6.2], which proves Theorem 1.2 in the special case of punctured–torus
bundles.
1.4. Acknowledgements. The proof of Theorem 1.2 was developed while
the two authors were preparing to give a mini-course at Osaka University in Jan-
uary 2006. This argument was then tested and reﬁned in front of three workshop
audiences containing many graduate students: at Osaka University in 2006, at Zhe-
jiang University in 2007, and at Columbia University in 2009. We thank all the
participants of those workshops for their suggestions. We are also grateful to the
organizers of the Columbia workshop, “Interactions Between Hyperbolic Geometry,
Quantum Topology and Number Theory,” for their encouragement to write up this
material for the workshop proceedings. Finally, this paper beneﬁted from a num-
ber of conversations with Marc Culler, Feng Luo, Igor Rivin, Makoto Sakuma, and
Louis Theran.
2. Gluing equations
For the length of this paper, M will typically denote a compact, connected,
orientable 3–manifold whose boundary consists of tori. For example, such a mani-
fold can be obtained from S3 by removing an open tubular neighborhood of a knot
or link. An ideal triangulation τ is a subdivision of M∖∂M into ideal tetrahedra,
glued in pairs along their faces. One way to recover the compact manifold M is
to truncate all the vertices of the tetrahedra: then, the triangles created by the
truncation will ﬁt together to tile ∂M.
As discussed in the Introduction, our eventual goal is to ﬁnd a complete hy-
perbolic metric on M by gluing together metric tetrahedra. The metric models for
the tetrahedra in M come from ideal tetrahedra in H3:
Definition 2.1. A hyperbolic ideal tetrahedron T is the convex hull in H3 of
four distinct points on ∂H3. The four points on ∂H3 are called ideal vertices of T,
and are not part of the tetrahedron. The tetrahedron T is called degenerate if it
lies in a single plane, and non-degenerate otherwise.
Recall that an isometry of H3 is completely determined by its action on three
points on ∂H3. Thus we may assume, for concreteness, that three vertices of T
lie at 0, 1, ∞in the upper half-space model. If T is non-degenerate, we may also
162
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
FROM ANGLED TRIANGULATIONS TO HYPERBOLIC STRUCTURES
5
α
α
γ
γ
β
β
0
1
∞
z
Figure 1. Left: the shape of an ideal tetrahedron is deﬁned by
three dihedral angles. Right: the gluing of tetrahedra, seen from
an ideal vertex.
assume that the fourth vertex lies at z ∈C, with Im(z) > 0. This number z ∈C
determines T up to isometry.
Suppose we move T by an orientation–preserving isometry of H3, so that three
vertices again lie at 0, 1, ∞, the fourth vertex again lies in the upper half-plane,
and edge e is mapped to the edge 0∞. Then the fourth vertex of T will be sent to
one of
(2.1)
z,
z′ = z −1
z
or
z′′ =
1
1 −z .
The corresponding number z, z′, or z′′ is called the shape parameter of e. Notice
that opposite edges of T have the same shape parameter, and that zz′z′′ = −1.
The arguments
arg z > 0,
arg z′ > 0,
arg z′′ > 0
represent the dihedral angles of T, or equivalently the angles of the Euclidean
triangle with vertices 0, 1, z. If one of the vertices of T is truncated by a horosphere,
the intersection will be a Euclidean triangle in precisely this similarity class. This
Euclidean triangle of intersection between T and a horosphere is called a boundary
triangle of T. See Figure 1, left.
The tiling of ∂M by boundary triangles of the tetrahedra provides a way to
understand what conditions are required to glue the tetrahedra coherently.
Definition 2.2. Let C be an oriented surface with a speciﬁed triangulation
(for example, a boundary torus of M with the tessellation by boundary triangles).
A segment in C is an embedded arc in one triangle, which is disjoint from the
vertices of C, and whose endpoints lie in distinct edges of C. A normal closed
curve σ ⊂C is an immersed closed curve that is transverse to the edges of C, such
that the intersection between σ and a triangle is a union of segments.
Definition 2.3. Let τ be an ideal triangulation of M, and let C be one torus
component of ∂M. Then τ induces a tessellation of C by boundary triangles. If
each tetrahedron of τ is assigned a hyperbolic shape, then every corner of each
boundary triangle can be labeled with the corresponding shape parameter.
Let σ be an oriented normal closed curve in C. Then every segment of σ in
a triangle of C cuts oﬀa single vertex of a triangle, labeled with a single shape
163
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
6
DAVID FUTER AND FRANC¸ OIS GU´ERITAUD
z1
z2
z3
z4 z5
z6
z7
z8
Figure 2. A normal path σ passing through the tessellation of a
torus by boundary triangles.
parameter (see Figure 2). Let z1, . . . , zk be the sequence of shape parameters cor-
responding to the segments of σ. Then the holonomy of σ is deﬁned to be
(2.2)
H(σ) =
k

i=1
ϵi log(zi),
where ϵi = 1 for corners of triangles to the left of σ and ϵi = −1 for corners
of triangles to the right of σ.
We always choose the branch of the log where
0 < arg(zi) < π for Im(zi) > 0.
Definition 2.4. Thurston’s gluing equations for a triangulation τ require, in
brief, that the holonomy of every curve σ ⊂∂M should be trivial.
More pre-
cisely, the system consists of edge equations and completeness equations. The edge
equation for an edge e of τ requires that all the shape parameters adjacent to e
satisfy
(2.3)
k

i=1
log(zi) = 2πi.
The completeness equations require that, if ∂M consists of k tori, there should be a
collection of simple closed normal curves σ1, . . . , σ2k spanning H1(∂M), such that
(2.4)
H(σj) = 0
∀j.
As the name suggests, the completeness equations ensure we obtain a complete
metric.
Proposition 2.5. Let τ be an ideal triangulation of M. Suppose that each
ideal tetrahedron of τ is assigned a non-degenerate hyperbolic shape with positive
imaginary part, as above. If the shape parameters of the tetrahedra satisfy the edge
gluing equations, these metric tetrahedra can be glued together to obtain a (possibly
incomplete) hyperbolic metric on M∖∂M. This metric will be complete if and only
if the completeness equations are satisﬁed.
Proof. Because all hyperbolic ideal triangles are isometric, there is no ob-
struction to gluing the tetrahedra isometrically along the interiors of their faces.
If the edge equation is satisﬁed for every edge of τ, then this isometric gluing
along faces of τ extends continuously across the edges. Thus we obtain a (possibly
incomplete) hyperbolic metric on M∖∂M and a developing map D : 
M →H3.
If the metric on M is complete, then D : 
M →H3 is an isometry. It is well-
known that the deck transformations corresponding to a component of ∂M must be
parabolic isometries of H3. In particular, if a cusp of M is lifted to ∞in the upper
164
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
FROM ANGLED TRIANGULATIONS TO HYPERBOLIC STRUCTURES
7
half-space model of H3, the parabolic isometries preserving that cusp are Euclidean
translations of C. But a simple closed curve σ ⊂∂M realizes a translation of C
precisely when its holonomy is H(σ) = 0. Thus equation (2.4) holds for all cusps
of M.
Conversely, suppose that the completeness equations (2.4) are satisﬁed for a
basis of H1(∂M). Then, for every cusp torus C ⊂∂M, the boundary triangles of C
can be developed to tile a horosphere in H3. In other words, the developing image
of a collar neighborhood of C is a horoball in H3, which is complete. But if we
remove the collar neighborhoods of every boundary torus in M, the remaining set
is compact, hence also complete. Thus the metric on M is complete.
□
