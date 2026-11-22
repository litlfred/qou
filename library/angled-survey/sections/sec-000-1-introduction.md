---
doc_id: angled-survey
doc_title: "From angled triangulations to hyperbolic structures"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: angled-survey.pdf
source_sha256: 8b49e682a39848bc
toc_source: inferred
doc_brief: "From angled triangulations to hyperbolic structures — This survey paper contains an elementary exposition of Casson and Rivin’s technique for ﬁnding the hyperbolic metric on a 3–manifold M with"
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
recall the deﬁnition of Thurston’s gluing equations. In Section 3, we give a rigorous
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
