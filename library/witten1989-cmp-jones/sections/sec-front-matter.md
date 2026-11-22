---
doc_id: witten1989-cmp-jones
doc_title: "Commun. Math. Phys. 121, 351-399 (1989) Mathematical Physics © Springer-Verlag 1989 Quantum Field Theory and the Jones Polynomial Edward Witten **"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-3
source_pdf: witten1989-cmp-jones.pdf
source_sha256: 32f98ed8f7b23588
toc_source: inferred
doc_brief: "Quantum field theory and the Jones polynomial (Witten, Commun. Math. Phys. 121 (1989) 351–399) — Chern–Simons gauge theory gives the Jones polynomial; framing dependence of Wilson loops"
---
Communications in
Commun. Math. Phys. 121, 351-399 (1989) 
Mathematical
Physics
© Springer-Verlag 1989
Quantum Field Theory and the Jones Polynomial
Edward Witten **
School of Natural Sciences, Institute for Advanced Study, Olden Lane, Princeton,
NJ 08540, USA
Abstract. It is shown that 2+1 dimensional quantum Yang-Mills theory, with
an action consisting purely of the Chern-Simons term, is exactly soluble and
gives a natural framework for understanding the Jones polynomial of knot
theory in three dimensional terms. In this version, the Jones polynomial can be
generalized from S3 to arbitrary three manifolds, giving invariants of three
manifolds that are computable from a surgery presentation. These results shed
a surprising new light on conformal field theory in 1 -f-1 dimensions.
In a lecture at the Hermann Weyl Symposium last year [1], Michael Atiyah
proposed two problems for quantum field theorists. The first problem was to give
a physical interpretation to Donaldson theory. The second problem was to find an
intrinsically three dimensional definition of the Jones polynomial of knot theory.
These two problems might roughly be described as follows.
Donaldson theory is a key to understanding geometry in four dimensions.
Four is the physical dimension at least macroscopically, so one may take a slight
liberty and say that Donaldson theory is a key to understanding the geometry of
space-time. Geometers have long known that (via de Rham theory) the self-dual
and anti-self-dual Maxwell equations are related to natural topological invariants
of a four manifold, namely the second homology group and its intersection form.
For a simply connected four manifold, these are essentially the only classical
invariants, but they leave many basic questions out of reach. Donaldson's great
insight [2] was to realize that moduli spaces of solutions of the self-dual Yang-
Mills equations can be powerful tools for addressing these questions.
Donaldson theory has always been an intrinsically four dimensional theory,
and it has always been clear that it was connected with mathematical physics at
least at the level of classical nonlinear equations. The puzzle about Donaldson
theory was whether this theory was tied to more central ideas in physics, whether it
could be interpreted in terms of quantum field theory. The most important
* An expanded version of a lecture at the IAMP Congress, Swansea, July,
** Research supported in part by NSF Grant No. 86-20266, and NSF Waterman Grant 88-17521
352 
E.Witten
Fig. 1. A knot in three dimensional space
evidence for the existence of such a connection had to do with Floer's work on
three manifolds [3] and the nature of the relation between Donaldson theory and
Floer theory. Also, the "Donaldson polynomials" had an interesting formal
analogy with quantum field theory correlation functions. It has turned out that
Donaldson theory can indeed be given a physical interpretation [4].
As for the Jones polynomial and its generalizations [5-11], these deal with the
mysteries of knots in three dimensional space (Fig. 1). The puzzle on the
mathematical side was that these objects are invariants of a three dimensional
situation, but one did not have an intrinsically three dimensional definition. There
were many elegant definitions of the knot polynomials, but they all involved
looking in some way at a two dimensional projection or slicing of the knot, giving
a two dimensional algorithm for computation, and proving that the result is
independent of the chosen projection. This is analogous to studying a physical
theory that is in fact relativistic but in which one does not know of a manifestly
relativistic formulation - like quantum electrodynamics in the 1930's.
On the physical side, the puzzle about the knot polynomials was the following.
Unlike the Donaldson theory, where a connection with quantum field theory was
not obvious, the knot polynomials have been intimately connected almost from
the beginning with two dimensional many body physics. In fact, constructions of
the knot polynomials have related them to two dimensional (or 1 + 1 dimensional)
many-body physics in a bewildering variety of ways, mainly involving soluble
lattice models [7], solutions of the Yang-Baxter equation [8], and monodromies of
conformal field theory [11]. In the latter interpretation, the knot polynomials are
related to aspects of conformal field theory that have been particularly fruitful
recently [12-16]. On the statistical mechanical side, studies of the knot poly-
nomials have related them to Temperley-Lieb algebras and their generalizations,
and to other aspects of soluble statistical mechanics models in 1 -f 1 dimensions.
For physicists the challenge of the knot polynomials has been to bring order to this
diversity, find the unifying themes, and learn what it is that is three dimensional
about two dimensional conformal field theory.
Now, the Donaldson and Jones (and Floer and Gromov [17]) theories deal
with topological invariants, and understanding these theories as quantum field
theories involves constructing theories in which all of the observables are
topological invariants. Some physicists might consider this to be a little bit
strange, so let us pause to explain the physical meaning of "topological
invariance". The physical meaning is really "general covariance". Something that
can be computed from a manifold M as a topological space (perhaps with a
Quantum Field Theory and the Jones Polynomial 
353
smooth structure) without a choice of metric is called a "topological invariant" (or
a "smooth invariant") by mathematicians. To a physicist, a quantum field theory
defined on a manifold M without any a priori choice of a metric on Mis said to be
generally covariant. Obviously, any quantity computed in a generally covariant
quantum field theory will be a topological invariant. Conversely, a quantum field
theory in which all observables are topological invariants can naturally be seen as
a generally covariant quantum field theory. Indeed, the Donaldson, Floer, Jones,
and Gromov theories can be seen as generally covariant quantum field theories in
four, three, and two space-time dimensions. The surprise, for physicists, perhaps
comes in how general covariance is achieved. General relativity gives us a
prototype for how to construct a quantum field theory with no a priori choice of
metric - we introduce a metric, and then integrate over all metrics. This example is
so influential in our thinking that we tend to think of a generally covariant theory
as being, by definition, a theory in which the metric is a dynamical variable. The
lesson from the Donaldson, Floer, Jones, and Gromov theories is precisely that
there are highly non-trivial quantum field theories in which general covariance is
realized in other ways. In particular, in this paper we will describe an exactly
soluble generally covariant quantum field theory in which general covariance is
achieved not by integrating over metrics but because we begin with a gauge
invariant Lagrangian that does not contain a metric.
