---
doc_id: angled-survey
doc_title: "Contemporary Mathematics From angled triangulations to hyperbolic structures"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: angled-survey.pdf
source_sha256: 8b49e682a39848bc
toc_source: inferred
---
Around 1980, William Thurston showed that “almost every” 3–manifold M,
whether closed or bounded, admits a complete hyperbolic metric [31]. When the
boundary of M consists of tori, this metric is unique up to isometry [20, 24].
Thurston introduced a method for ﬁnding this unique metric. The idea was to
subdivide the interior of M into ideal tetrahedra (tetrahedra whose vertices are
removed), and then give those tetrahedra hyperbolic shapes that glue up coherently
in M. The shape of a hyperbolic ideal tetrahedron can be completely described by
a single complex number, namely the cross–ratio of its four vertices on the sphere
at inﬁnity. Thurston wrote down a system of gluing equations in those complex
parameters, whose solution corresponds to the complete hyperbolic metric on the
interior of M [30].
The diﬃculty with Thurston’s approach is that this non-linear system of equa-
tions is very diﬃcult to solve in practice. Even proving the existence of a positively
oriented solution, for a given triangulation, often turns out to be a daunting task.
In the 1990s, Andrew Casson and Igor Rivin discovered a powerful technique
for solving Thurston’s gluing equations. Their main idea (which builds on a result
of Colin de Verdi`ere [3]) was to separate the system into a linear part and a non-
linear part. The linear part of the equations corresponds geometrically to a study
2010 Mathematics Subject Classiﬁcation. 57M50.
Futer is supported in part by NSF Grant No. DMS–1007221.
Gu´eritaud is supported in part by the ANR program ETTT (ANR-09-BLAN-0116-01).
c
⃝0000 (copyright holder)
1
Contemporary Mathematics
Volume 541, 2011
c
⃝2011 The Authors
159
http://dx.doi.org/10.1090/conm/541/10683
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
2
DAVID FUTER AND FRANC¸ OIS GU´ERITAUD
of dihedral angles of the individual tetrahedra. In order for the tetrahedra to ﬁt
together in M, the dihedral angles at each edge of M must sum to 2π; in order
for the tetrahedra to be positively oriented, all the angles must be positive. For
a given triangulation τ, the space of solutions to this linear system of equations
and inequalities is a convex polytope A(τ), with compact closure A(τ). A point of
A(τ), corresponding to an assignment of tetrahedron shapes that satisﬁes the angle
conditions, is called an angle structure on τ. See Deﬁnition 3.1 for details.
An angle structure on τ is weaker than a hyperbolic metric, because the linear
equations that deﬁne A(τ) impose a strictly weaker condition on tetrahedra than
do Thurston’s gluing equations. Nevertheless, Casson proved
Theorem 1.1. Let M be an orientable 3–manifold with boundary consisting
of tori, and let τ be an ideal triangulation of M. If A(τ)̸ = ∅, then M admits a
complete hyperbolic metric.
In other words, the existence of an angle structure implies the existence of a
hyperbolic structure. Finding this hyperbolic structure requires solving the non-
linear part of the gluing equations. To do this, Casson and Rivin introduced a
volume functional V : A(τ) →R, which assigns to every angle structure on τ the
sum of the hyperbolic volumes of the tetrahedra in this structure. See Deﬁnition 5.2
for a precise deﬁnition. As we shall see in Section 5, the function V has a number of
pleasant properties: it is smooth and strictly concave down on A(τ), and extends
continuously to A(τ). Casson and Rivin independently proved
Theorem 1.2. Let M be an orientable 3–manifold with boundary consisting of
tori, and let τ be an ideal triangulation of M. Then a point p ∈A(τ) corresponds
to a complete hyperbolic metric on the interior of M if and only if p is a critical
point of the functional V : A(τ) →R.
All told, the Casson–Rivin program can be summarized as follows. Solving
the linear part of Thurston’s gluing equations produces the convex polytope A(τ).
Solving this linear system is straightforward and algorithmic; by Theorem 1.1,
the existence of a solution implies that a hyperbolic structure also exists.
By
Theorem 1.2, solving the non-linear part of the gluing equations amounts to ﬁnding
a critical point (necessarily a global maximum) of the functional V : A(τ) →R. In
practice, the search for this maximum point can be accomplished by gradient–ﬂow
algorithms. It is worth emphasizing that a critical point of V does not always exist:
the maximum of V over the compact closure A(τ) will occur at a critical point in
A(τ) if and only all the tetrahedra of τ are positively oriented in the hyperbolic
metric on M.
1.1. Where to ﬁnd proofs. Proofs of Theorem 1.1 are readily available in
the literature. A nice account appears in Lackenby [13, Corollary 4.6], and a slightly
more general result appears in Futer and Gu´eritaud [5, Theorem 1.1]. Here is a
brief summary of the argument. By Thurston’s hyperbolization theorem [31], the
existence of a hyperbolic structure is equivalent to the non-existence of essential
spheres, disks, tori, and annuli in M. Any such essential surface S can be moved
into a normal form relative to the triangulation τ; this means that every component
of intersection between S and a tetrahedron is a disk in one of several combinato-
rial types. The dihedral angles that come with an angle structure permit a natural
160
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
FROM ANGLED TRIANGULATIONS TO HYPERBOLIC STRUCTURES
3
measure of complexity for normal disks, which mimics the area of hyperbolic poly-
gons.
As a result, one can show that every surface S with non-negative Euler
characteristic must have non-positive area, which means it is inessential. Hence M
is hyperbolic.
By contrast, direct proofs of Theorem 1.2 are harder to ﬁnd. The standard
reference for this result is Rivin [26]. However, the focus of Rivin’s paper is some-
what diﬀerent: he mainly studies the situation where M is an ideal polyhedron,
subdivided into ideal tetrahedra that meet at a single vertex. The notion of an
angle space A(τ) and a volume functional V still makes sense in this context, and
Rivin’s proof of the analogous result [26, Lemma 6.12 and Theorem 6.16] extends
(with some eﬀort by the reader) to manifolds with torus boundary.
One reference that contains the above formulation of Theorem 1.2, together
with a direct proof, is Chan’s undergraduate honors thesis [1, Theorem 5.1]. How-
ever, this thesis is not widely available. In addition, Chan’s argument relies on
a certain symplectic pairing introduced by Neumann and Zagier [22], a layer of
complexity that is not actually necessary.
The central goal of this paper is to write down an elementary, self-contained
proof of Theorem 1.2.
The argument is organized as follows.
In Section 2, we
