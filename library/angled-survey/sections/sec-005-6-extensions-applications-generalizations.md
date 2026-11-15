---
doc_id: angled-survey
doc_title: "From angled triangulations to hyperbolic structures"
section_id: sec-005-6-extensions-applications-generalizations
section_title: "Extensions, applications, generalizations"
section_number: 6
pages: 19-23
source_pdf: angled-survey.pdf
source_sha256: 8b49e682a39848bc
toc_source: inferred
doc_brief: "From angled triangulations to hyperbolic structures — This survey paper contains an elementary exposition of Casson and Rivin’s technique for ﬁnding the hyperbolic metric on a 3–manifold M with"
---
This ﬁnal section of the paper surveys several ways in which the Casson–Rivin
program has been generalized and extended, as well as several inﬁnite families of
manifolds to which the program has been successfully applied.
Theorem 1.2 concerns manifolds with non-empty boundary that consists of tori.
It is natural to ask whether similar methods can be applied to treat manifolds with
more general boundary, or closed manifolds that have no boundary at all. Indeed,
there has been considerable progress in these areas.
6.1. Closed manifolds via Dehn ﬁlling. The most straightforward way to
extend Theorem 1.2 to closed manifolds is via Dehn surgery. If C is a boundary
torus of M, and μ, λ are simple closed normal curves that form a basis for H1(C),
then M(p/q) is the manifold obtained by attaching a solid torus to C, such that
the boundary of the meridian disk is mapped to pμ + qλ. In terms of the gluing
equations of Deﬁnition 2.4, attaching a disk to the closed curve pμ+qλ is equivalent
to solving the holonomy equation
(6.1)
p H(μ) + q H(λ) = 2πi.
Just as above, the imaginary part of equation (6.1) is linear in the angles of τ.
Imposing this linear equation corresponds to taking a codimension–1 linear slice of
the angle space A(τ).
Theorem 6.1. Let M be a manifold with boundary a single torus C, and let
τ be an ideal triangulation of M. Choose a pair (p, q) of relatively prime integers,
and let Ap/q(τ) ⊂A(τ) be the set of all angle structures that satisfy the imaginary
177
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
20
DAVID FUTER AND FRANC¸ OIS GU´ERITAUD
part of equation (6.1). Then a critical point of the volume functional V on Ap/q(τ)
yields a complete hyperbolic structure on M(p/q), the p/q Dehn ﬁlling of M.
The analogous statement holds for ﬁllings along multiple boundary tori.
The proof follows the same outline as Theorem 1.2; see [1, Theorem 6.2] for
more details.
6.2. Manifolds with polyhedral boundary. There is also an analogue of
Theorem 1.2 for ideal triangulations where not every face of the tetrahedra is glued
to another face. Given such a partial gluing of tetrahedra, one obtains a 3–manifold
N whose boundary is subdivided into ideal triangles. If the tetrahedra carry di-
hedral angles, then every edge along ∂N will also carry a prescribed angle. The
simplest case of this is when N is an ideal polyhedron, but one may also consider
cases where N has more complicated topology.
It is worth asking exactly when a 3–manifold N with polyhedral boundary, and
with a ﬁxed assignment of convex dihedral angles, carries a complete hyperbolic
metric with ideal vertices that realizes those angles. The following combinatorial
condition was suggested by Rivin [25]:
(∗) For every simple closed normal curve σ ⊂∂N that bounds a disk in N, the
sum of exterior angles along σ is at least 2π, with equality iﬀσ encircles
an ideal vertex.
Theorem 6.2. Let N be a 3–manifold with polyhedral boundary and prescribed
(convex) dihedral angles along every edge of ∂N. Suppose that N is irreducible and
atoroidal, and furthermore that N is a 3–ball, or a solid torus, or has incompressible
boundary.
Then N carries a complete hyperbolic metric realizing the prescribed
angles if and only if condition (∗) holds. Furthermore, any hyperbolic realization is
unique up to isometry.
The case when N is a polyhedron is due to Rivin [27, 28]; the case of solid tori,
to Gu´eritaud [8]. In both cases, the argument works by ﬁrst proving that N has
an ideal triangulation with a non-empty angle space A(τ), and then proving that
the volume functional V has a critical point in A(τ). This critical point gives the
hyperbolic realization of N. In the preprint [29], Schlenker gives a more analytic
and general argument in the case of incompressible boundary. Conjecturally, the
special hypotheses of all these papers are not needed: all that should be necessary
is that N is irreducible and contains no incompressible tori, and that the angle
assignments satisfy (∗). See [5, Conjecture 2.4].
6.3. Generalized angle structures. All of the angle structures discussed so
far have involved strictly positive dihedral angles. One natural generalization of
the deﬁnitions in Section 3 would be to allow negative angles, or more generally, to
consider angles mod 2π.
A generalized angle structure is an assignment of a real number to every pair
of opposite edges in a tetrahedron, so that equations (2) and (3) of Deﬁnition 3.1
are satisﬁed, but the inequalities are discarded. The set of all such assignments
is denoted GA(τ). Luo and Tillmann showed that for any ideal triangulation τ of
a manifold with torus boundary, GA(τ) is always non-empty [18]; in other words,
there is no analogue of Theorem 1.1. Furthermore, they establish a linear–algebraic
duality between angle structures and normal surfaces (see also Rivin [28]). For
178
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
FROM ANGLED TRIANGULATIONS TO HYPERBOLIC STRUCTURES
21
example, the obstruction to ﬁnding a non-empty positive polytope A(τ) ⊂GA(τ)
is a certain branched normal surface with non-negative Euler characteristic.
Generalizing further, an S1–valued angle structure on a triangulation τ is an
assignment of a real number (mod 2π) to every pair of opposite edges in a tetrahe-
dron, such that
(1) Around each ideal vertex of a tetrahedron, the dihedral angles sum to π
(mod 2π),
(2) Around each edge of M, the dihedral angles sum to 0 (mod 2π).
The set of all S1–valued angle structures on τ is denoted SA(τ).
Just as with real–valued solutions in GA(τ), Luo showed that the existence
of S1–valued solutions is extremely general. For any triangulated closed pseudo–
manifold (i.e., any cell complex obtained by gluing tetrahedra in pairs along all of
their faces, whatever the link of a vertex), he showed that SA(τ)̸ = ∅, and is a
closed smooth manifold [15, Proposition 2.6].
Even though the existence of S1–valued angle structures does not distinguish
the class of hyperbolic manifolds, studying the volume of such a structure can still
yield geometric information. Recall from Lemma 5.1 that the Lobachevsky function
L is π–periodic; as a result, Deﬁnition 5.2 of the volume functional V extends in a
natural way to SA(τ). Because SA(τ)̸ = ∅is a compact manifold, V must achieve
a maximum. The work of Luo [15] and Luo–Tillmann [17] uses this maximum
point to either solve a generalized version of the gluing equations (which yields a
representation from a double branched cover of M into PSL(2, C)), or ﬁnd certain
highly restrictive normal surfaces in M. See Luo’s survey paper in this volume [14]
for more details.
6.4. Volume estimates. Recall that, by Lemma 5.3, the volume functional
V is concave down on A(τ). As a result, any critical point of V must actually be
the global maximum of the function over the compact closure A(τ). Thus Theorem
1.2 has the following corollary.
Theorem 6.3. Let M be an orientable 3–manifold with boundary consisting of
tori, and let τ be an ideal triangulation of M. Suppose that V : A(τ) →R has a
critical point at p ∈A(τ). Then, for any point q ∈A(τ),
V(q) ≤vol(M),
with equality iﬀq = p (i.e., iﬀq gives the complete hyperbolic metric on M).
In fact, the analogous statement also holds in the settings of Section 6.1 (Dehn
ﬁlling) or Section 6.2 (polyhedral boundary). The uniqueness of a critical point
of V turns out to be the key idea in Rivin’s proof of the uniqueness statement of
Theorem 6.2.
Theorem 6.3 allows to compute eﬀective, combinatorial volume estimates for
hyperbolic 3–manifolds. In certain settings, the combinatorics of a 3–manifold nat-
urally guides a choice of triangulation τ, and the same combinatorial data provide
a convenient point q ∈A(τ). Then, Theorem 6.3 says that V(q) is a lower bound
on the volume of M. This approach is illustrated by the ﬁrst family of manifolds
to which the Casson–Rivin method was successfully applied [11].
A decade after Colin de Verdi`ere, Casson, and Rivin developed the theory of
volume maximization in the early 1990s, it was Gu´eritaud who ﬁrst applied the
method to ﬁnd the hyperbolic metrics on an inﬁnite family of manifolds, namely
179
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
22
DAVID FUTER AND FRANC¸ OIS GU´ERITAUD
punctured torus bundles [11]. In an appendix to the same paper, Futer extended
the method to two–bridge links [11, Appendix].
For both of these families of
manifolds, the existence of hyperbolic metrics was well-known, but the volume
estimates coming from Theorem 6.3 were both new and sharp. Combined with Dehn
surgery techniques, the volume estimates from [11] also give explicit, combinatorial
bounds for the volume of several families of knot and link complements [6, 7], as
well as of a number of closed manifolds [23].
It is worth asking whether the existence of a critical point of V in A(τ) is actu-
ally necessary for the volume inequality of Theorem 6.3. Casson conjectured that
this inequality holds for any angled triangulation τ, whether or not the tetrahedra
of this triangulation can be given positively oriented shapes in the hyperbolic met-
ric on M. (Note that, by Theorem 1.1, the hyperbolic metric must exist.) If proved
true, this conjecture would provide a practical tool for ﬁnding volume estimates on
many more families of 3–manifolds.
6.5. Canonical triangulations. Nearly everything discussed thus far in this
paper has depended on the choice of triangulation. As it turns out, many of the
methods already discussed can show that a particular triangulation is geometrically
canonical for M.
Given a hyperbolic 3–manifold M with k cusps, let H1, . . . , Hk be disjoint
horospherical neighborhoods of the cusps. Then the Ford–Voronoi domain F is the
set of all points in M that have a unique shortest path to the union of the Hi. This
is an open set in M, whose complement L = M∖F is a compact 2–complex, called
the cut locus. The dual to L is an ideal polyhedral decomposition P of M; the n–
cells of P are in bijective correspondence with the (3 −n)–cells of L. This is called
the canonical polyhedral decomposition of M, relative to the cusp neighborhoods
Hi.
The combinatorics of L —and therefore, of P— depends only on the relative
volumes of the Hi. In particular, if M has only one cusp, there are no choices what-
soever, and P is completely determined by the hyperbolic metric. If the horoballs
in H3 obtained by lifting the cusp neighborhoods Hi are in “general position,” ev-
ery vertex of 	L will have exactly four closest horoballs. Thus each vertex of L will
meet four edges, and the dual polyhedral decomposition P will generically be a
triangulation.
If τ is a given triangulation (or, more generally, a given polyhedral decompo-
sition), proving that τ is canonical amounts to verifying ﬁnitely many inequalities
about nearest horoballs. Epstein and Penner found a way to translate these inequal-
ities into convexity statements in the Minkowski space R3+1, where H3 is modeled
by a hyperboloid [4]. More recently, Gu´eritaud discovered that the convexity in-
equalities that imply canonicity (once translated to inequalities involving dihedral
angles of the polyhedra) can be veriﬁed using information obtained in the course
of showing that V : A(τ) →R has a critical point [9].
To date, the method of angled triangulations has found both the hyperbolic
metric and the canonical polyhedral decomposition of several families of 3–manifolds:
punctured–torus bundles [9, Theorem 1.11.1], two-bridge links [9, Theorem 2.1.7],
and certain special arborescent links [9, Theorem 2.3.1].
Gu´eritaud used the
same ideas to ﬁnd the canonical triangulations for convex cores of quasi-Fuchsian
punctured–torus groups [10]. All of these families of manifolds actually have closely
180
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
FROM ANGLED TRIANGULATIONS TO HYPERBOLIC STRUCTURES
23
related combinatorial features, with the structure of the triangulation eﬀectively de-
termined by the combinatorics of SL(2, Z) and continued fractions.
There is a recent result that brings together several themes from this section.
Suppose that M is a hyperbolic 3–manifold with k cusps, and the canonical de-
composition of M is indeed a triangulation. If we perform Dehn ﬁlling along one
of these cusps, the result will (generically) be another hyperbolic manifold M(p/q),
with a new geometry. In [12], Gu´eritaud and Schleimer use the canonical triangu-
lation of M to completely describe the canonical triangulation of its generic Dehn
ﬁllings. Their argument uses Theorems 6.1 and 6.2 to construct a triangulated solid
torus with the right shape and glue it into M(p/q).
6.6. Weil rigidity. We close this paper with an application whose statement
has nothing to do with triangulations. The following rigidity theorem, due to Weil
[32], precedes Mostow–Prasad rigidity by a dozen years.
Theorem 6.4. Let M be a 3–manifold with boundary consisting of tori. Then
any complete hyperbolic metric on the interior of M is locally rigid: there is no
local deformation of the metric through other complete hyperbolic metrics.
We thank Marc Culler and Feng Luo for a fruitful discussion that produced the
following extremely short proof.
Proof. Suppose that M admits a complete hyperbolic metric. Choose horoball
neighborhoods H1, . . . , Hk about the cusps of M. Then, as in Section 6.5, this
choice of cusp neighborhoods determines a decomposition P of M into ideal poly-
hedra. Luo, Schleimer, and Tillmann showed that M has a ﬁnite–sheeted cover N,
in which the lift of P decomposes into positively oriented ideal tetrahedra [16]. Let
τ be this positively oriented ideal triangulation of N.
By Theorem 1.2, the complete hyperbolic metric on N (which was obtained by
lifting the metric on M) represents a critical point of V : A(τ) →R. By Lemma
5.3, this critical point is unique. But any local deformation of the complete metric
on M would lift to a deformation of the metric on N, which would violate Lemma
5.3.
□
