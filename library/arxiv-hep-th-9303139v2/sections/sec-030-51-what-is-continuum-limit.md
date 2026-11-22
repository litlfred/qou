---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-030-51-what-is-continuum-limit
section_title: "What is continuum limit"
section_number: 5.1
pages: 121-124
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 1.0
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
Continuum limit of matrix models is, of course, the crucial issue for their
physical applications whenever these models are interpreted as discrete
(lattice) approximations to continuum theory. The very first thing to be kept
in mind is that it is $not$ the only possible view on matrix models. Another
approach considers them as describing $topological$ (and thus also in a
certain sense "discrete") properties of the theory. Such models, when appearing
in the field of, say, quantum gravity (which after all is a sort of a pure
topological theory) do $not$ require any continuum limit to be taken: their
discrete nature (occurence of {\it integer}-valued matrix indices)
reflects $not$ the discrete
approximation to the space-time (which does not really exist in quantum
gravity), but rather the essential discreteness of the underlying structures:
topology of the module spaces of geometries. Example of matrix models which
allow for this kind of interpretation - in terms of topology of module spaces
of bundles over Riemann surfaces - is provided by Kontsevich models, and this
is why they usually do not require any continuum limit and why we once called
them "continuous matrix models" in the Introduction to these notes. The models
which are usually interpreted in more traditional way - as lattice theories -
are represented by our "discrete" models, the 1-matrix, conventional and
"conformal" multimatrix models being included into this class. More
sophisticated examples are provided by "$c=1$"-theories, Kazakov-Migdal model
and, say, Wilson's QCD (and infinetely many other lattice theories). It is not
a surprise that continuum limits of some discrete models provide the theories
of Kontsevich type: this happens whenever continuum theory is supposed to have
a kind of topological nature. This is usually the case for quantum gravity
(which, as we said, is conceptually a topological theory in the "module space
of geometries" - the notion which is already made more or less explicit in the
$2d$ case), but in principle this can be also true for many other theories,
including exhaustive quantum theory of Yang-Mills fields (again there is
already considerable progress in this direction, as soon as $2d$ Yang-Mills
model is concerned). There should not be confusion about the presence of gauge
particles in dimensions greater than 2 (for Yang-Mills) and 3 (for gravity):
there is no reason to prevent generic topological theory from possessing
continuum spectrum of excitations, though explicit analogue of Kontsevich-like
description of such situations is not yet found (as we mentioned many times,
it should probably rely upon non-eigenvalue models).

We shall not discuss the non-trivial history of invention and understanding of
all these notions (the crucial steps being discovery of the "multiscaling
continuum limits" \cite{Kmamo},\cite{mamo}, which preserve integrable
structure of discrete models in continuum case; hypothesis of equivalence of
quantum and topological $2d$ gravities \cite{WitTG} and its proof
\cite{Witko},\cite{MMM}, provided by discovery of Kontsevich models \cite{Ko}
as a peculiar and powerful tool
for description of topology of the module spaces). Instead,
following the mean line of these notes,  we
shall concentrate on intrinsic relation between (multiscaling) continuum
limits and integrability: the notion of continuum limits is in fact built into
the theory of integrable hierarchies and the underlying representation theory
of Kac-Moody algebras.

In the case of the eigenvalue models the central issue here is the
interrelation between Toda-lattice and KP hierarchies, even its more narrow
aspect: elimination of the zero-time $N$, present in the Toda-lattice case.
{}From representation theory (or conformal field theory, what is essentially
the
same) point of view the thing is that the zero-time (which labels the filling
level
of Dirac sea in the fermionic picture) is associated with the zero-modes of
$scalar$ field and its elimination is just the change of boundary conditions
which eliminates zero-modes. The simplest example of this "twisting" procedure
is just transformation from periodic to antiperiodic scalars - it still
preserves possibility to have fermionic description (where it looks like a
switch from Ramond to Neveu-Schwarz sector), and thus does not take us out of
the field of conventional integrable hierarchies. In representation theory one
can interpret the same operation just as a switch from the
homogeneous to principal representation, which are associated with
the Toda-lattice and KP hierarchies respectively.

This remarkably simple description is of course far from obvious, if one
investigates continuum limit in naive way, without taking integrable structure
into account explicitly, but just sending the number of degrees of freedom in
discrete theory (i.e. the matrix size $N$) to infinity (together with the
inverse lattice spacing, if any). We refer to the classical review
\cite{Migrev}  for discussion of what are the naive continuum limits in
lattice gauge theories, i.e. what are the conditions for getting the
second-order phase transitions, which allow for a continuum-like scaling
behavious in the vicinity of the critical point, with critical exponents
defining all the continuum physics, from quantum dimesnion of the space-time
to spectrum of particles. The problem with naive continuum limits is that they
can easily destroy integrable structure of the theory (the underlying
hidden symmetries), unless special precaution is taken: the critical
point (which is in fact a low-codimensional hypersurface in the
infinite-dimensional space of parameters) should be approached from the
certain directions, so that Ward identities are not explicitly broken.

As soon as this word - Ward -dentities - is pronounced, we already get into
the field of integrable systems and the issue can be discussed inside this
field. The above-mentioned switch from periodic to antiperiodic fields is of
course apparent if the discrete and continuos Virasoro constraints
(represented by formulas

(1.2)
and

(1.3)
in the Introduction) are compared, but this is {\it a posteriori} information,
because so far we interpreted "continuous Virasoro constraints" as the
Ward-identities for the $V=X^3$-Kontsevich model, and it still remains to be
explained why Kontsevich model is indeed what arises after continuum limit is
taken. The simplest approach to {\it this} problem
is to make use of the identity
between discrete 1-matrix model and Gaussian Kontsevich model \cite{ChMa},
established in
section 3.8 above. Then the $X^3$-model arises in the large-$N$ limit just
when the matrix integral is evaluated by the steepest descent method
\cite{Toda}. We shall present this simple calculation in the last subsection
below, but before we take a somewhat more direct (and complicated)
approach in order to reveal at least some of ideas, underlying the entire
theory of continuum limits.
