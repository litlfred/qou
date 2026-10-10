---
doc_id: arxiv-1001.2933v4
doc_title: "Analytic Continuation Of Chern-Simons Theory"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: "1"
pages: 4-7
source_pdf: 1001.2933v4.pdf.txt
source_sha256: b02636c86d593c02
toc_source: inferred
doc_brief: "Analytic Continuation Of Chern-Simons Theory — The title of this article refers to analytic continuation of three-dimensional ChernSimons gauge theory away from integer values of the usual coupling"
---
1 Introduction
This paper is devoted to the analytic continuation of three-dimensional Chern-Simons gauge
theory as a function of its coupling parameters. One motivation for this study concerns
three-dimensional quantum gravity, which plausibly has at least some sort of relationship
to three-dimensional Chern-Simons theory with gauge group SL(2, C). In that context,
Euclidean quantum gravity is obtained by analytic continuation to imaginary values of the
coupling parameter s that is introduced in section 2.1 However, for imaginary s, the ChernSimons path integral, like the Euclidean quantum gravity path integral in any dimension,
does not appear to be convergent. Our analysis in this paper will explain how to make sense
of this sort of path integral, at least in the Chern-Simons case.
Another motivation is to understand aspects of the Jones polynomial of knots2and its
generalizations that have not yet been explained from the point of view of three-dimensional
gauge theory. The Jones polynomial of a knot was originally defined as a Laurent polynomial
in a complex variable q – a rational function of q with poles only at q = 0 and q = ∞. ChernSimons gauge theory with gauge group SU(2) (or another compact Lie group) reproduces
the Jones polynomial, and its generalizations, at values of q of the form exp(2πi/(k + h)),
where k is a positive integer, and h (which is 2 for SU(2)) is the dual Coxeter number of the
gauge group. The Jones polynomial and related invariants are determined by their values
for these special values of q, but it would be desirable to have a gauge theory explanation
of the existence of a natural analytic continuation. It has generally been expected that
1And the singularity at s = ±iℓ that we will discuss in section 2.4 is at least a cousin of the “chiral point”
of three-dimensional gravity, which has been much studied recently [1].
2The usual mathematical terminology is that a knot is an embedded circle in a three-manifold (usually a
three-sphere) while a union of disjoint embedded circles is called a link. Except in section 4.2.7, all statements
about knots in this paper have rather immediate analogs for links, but for brevity we will refer to knots.
4

the explanation has something to do with the relation between Chern-Simons theories with
gauge groups SU(2) or SL(2, C), but a really clear picture has not been available. A better
understanding appears to require analytic continuation of Chern-Simons theory beyond the
values of the parameters at which the path integral can be most simply understood.
Finally, in the last decade or more, striking new results have been obtained [2–21] about
the analytic continuation of invariants related to the Jones polynomial. (A useful review
is [17]; partial physics-based explanations with some relevance to the present paper are
[6,18,19]. While it is impractical to give complete references on Chern-Simons theory, some
contributions comparing the asymptotic or in some cases exact behavior of the Chern-Simons
partition function to geometry, but not focusing on analytic continuation, are [22–34].) The
colored Jones polynomial Jn(q) of a knot is interpreted in Chern-Simons gauge theory in
terms of the expectation value of a Wilson loop operator associated to the n-dimensional
representation of SU(2). Let q
n = exp(2πiγ), and consider the behavior of Jn(q) in a scaling
limit with n tending to infinity for fixed γ. The behavior of this limit for certain values
of γ can be naturally understood in SU(2) Chern-Simons theory, but many of the more
recent results certainly appear to be more directly related to the theory with gauge group
SL(2, C). For example, for γ near 1, and at least for some knots, the large n behavior
appears to be dominated by an SL(2, C)-valued flat connection that does not take values in
SU(2). Although there has not been a completely clear picture of how and why the scaling
limit of Jn(q) should be related to SL(2, C) Chern-Simons theory, the idea that there is
such a relationship has been a fruitful source of new ideas and generalizations [6]. Again,
it has been clear that a fuller picture will require a better understanding of the analytic
continuation of Chern-Simons theory.
In this paper, we will definitely not obtain complete answers to all of the above questions,
and among other things we do not have a general answer concerning the volume conjecture.
(It is true, as will become clear, if a certain integer-valued coefficient is always nonzero, but
we do not know why this would always be so.) But we do hope to make some things clearer.
We show that critical points of the analytically continued Chern-Simons functional should
be used to determine – by steepest descent – suitable integration cycles for the quantum
path integral. For a given value of the coupling parameters, not all critical points should
be included; doing so would lead to immediate contradiction with known facts about the
knot polynomials. Instead, one should start with a real integration cycle for real coupling
and then, as one varies the coupling into the complex plane, one varies the integration
cycle so that the integral remains convergent. In the process, one encounters subtle Stokes
phenomena that govern the appearance and disappearance of critical points. The Stokes
phenomena can be described, in principle, by solving steepest descent equations that in the
context of Chern-Simons theory amount to four-dimensional elliptic differential equations
that generalize the instanton equation. This gives a suitable framework for analytically
continuing the SL(2, C) Chern-Simons theory as a function of its coupling parameter, and
for better understanding its relation to the SU(2) theory.
5

Section 2 of the paper is devoted to a more complete overview of some of these matters.
In section 3, we describe the analytic continuation of oscillatory integrals in finite dimensions and their analysis by steepest descent. This is an application of the framework
of [35–40], which is reviewed here for convenience. Various aspects of this framework have
been applied to quantum field theory from different points of view [41–45]. Floer theory (for
reviews see for instance [46,47]) is a prototype for the application of Morse theory to middledimensional cohomology of function spaces, which appears in our approach to Chern-Simons
gauge theory.
In section 4, we apply what we have learned to the analytic continuation of ChernSimons gauge theory on a generic three-manifold. A striking result emerges: the gradient
flow equations relevant to analytic continuation of three-dimensional Chern-Simons theory
actually have four-dimensional symmetry.
In section 5, we consider the special case of knot invariants in S
3
, where stronger conclusions are possible because, in the absence of the knot, there are no non-trivial flat connections.
The main examples considered in section 5 are the trefoil knot and the figure-eight knot.
In each case, we consider the semi-classical limit of the colored Jones polynomial, keeping
fixed the conjugacy class of the monodromy of a flat connection around the knot. (In other
words, we consider the limit mentioned above of n → ∞ with fixed γ.) The technique that
we use to describe the Stokes phenomena relies on analyzing the singularities of the moduli
space of flat connections – that is, the special values of the monodromy at which flat connections that are generically distinct become coincident. The semiclassical behavior near
such a special value is interesting in itself; it can be modeled by a finite-dimensional integral
associated to the relevant singularity. We analyze several examples of such singularities and
compare the results to what has been found in the mathematical literature in studies of
the semiclassical limit of the colored Jones polynomial. For the trefoil knot, though many
interesting questions remain, the Stokes phenomena that we analyze suffice to determine the
integration cycle of the analytically continued Chern-Simons path integral for all values of
γ. For the figure-eight knot, we primarily determine what happens close to the real γ axis.
In both cases, our analysis of the Stokes phenomena suffices to explain the validity of the
volume conjecture.
Finally, in section 6, we make a few remarks on a four or five-dimensional interpretation of
what we have learned, with the possible goal of a new understanding of Khovanov homology.
6
