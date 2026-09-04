---
doc_id: black-samson-phd2010sp
doc_title: "REPRESENTATIONS OF HECKE"
section_id: sec-007-11-historical-background
section_title: "Historical Background"
section_number: 1.1
pages: 9-11
source_pdf: Black_Samson_phd2010sp.pdf
source_sha256: c16799b0bd54ff29
doc_brief: "REPRESENTATIONS OF HECKE — 19 sections: Acknowledgments; INTRODUCTION 1; SCHUR-WEYL DUALITY AND QUOTIENTS O"
---
The Alexander polynomial has a history dating back to the early days of algebraic topology.
The original definition ([1]) came from analyzing the group of deck transformations on the infinite
cyclic cover of the complement of a knot. In the same paper, Alexander reduced the calculation of
the invariant to a combinatorial procedure using knot diagrams. Decades later, Conway introduced
a special normalization of the invariant ([9]) extended to links, denoted \7(L), that was recursively
computable using a skein relation on the diagrams (see Figure 1.1).
x x ) (
Lo
Figure 1.1: The Conway skein relation:
Following the discovery by Jones of a new invariant ([23] and also [10, Chapter 9] for
an interesting account of the discovery), there was an explosion of interest in the industry of
producing link invariants using skein theories. \Vithin a year, a two-variable polynomial invariant
was simultaneously introduced by several independent groups of authors, all of whose names are
celebrated in the acronym: HOMFLYPT ([14] and [34]). Using the skein theoretic approach, we
first pass to a diagram of the link, which involves the choice of a generic projection onto a plane.
The verification that a function on these diagrams is well-defined as a function of the original link
reduces to the formal task of checking invariance under the Reidemeister moves. Much of the
geometry of three dimensional space is lost in the passage to a diagram, but the trade-off is that
many of the tools of representation theory which have no obvious connection to the original link
2
can be brought to bear. The menagerie of quantum invariants that exists today comes about in
this manner.
In the seminal work of Reshetikhin and Turaev ([36]), they construct quantum link in­
variants as tensor functors from the tensor category of colored tangles to the category of modules
over the quantum group Uv(g), for 9 a simple complex Lie algebra, using the quasi-triangular Hopf
algebra structure on Uv(g) and choosing representations to label components. Specifically, a (d, d')­
tangle connecting d' points on the bottom to d points on the top produces a Uv(g)-homomorphism
VVP1 ® ... ® W"d' --'I vV)\] ® ... ®W'\d' where the modules Wllj and W,\., are determined by the colors
on the strands. In this context, links appear as (O,O)-tangles, as they have no endpoints, and so
link invariants are Uv (g)-module endomorphisms of the ground field C(v). A family of polynomial
invariants Pn (n :.:-: 2) arises from the choice of 9 = E[(n) and the coloring of each component of the
link by the standard n-dimensional representation. Each of the invariants Pn are specializations
of the HOMFLYPT polynomial at x = vn (see 11.1), and they satisfy the skein relation:
(1.1)
At n = 1 the specialization is trivial, but the n = 0 case is evidently the Alexander polynomial
(z = v - V-I in Conway's normalization \l(L)). However, to construct the Alexander polynomial
as a quantum invariant, a suitable substitute for the meaningless £1[(0) is required.
One approach is to use the restricted UdE[(2)), where ( = p, labeling each component
with the entire family of 2-dimensional modules W,\, A E C, and recovering the invariant in terms
of A. Another approach is to use the superalgebra Uv (g[(111)) with a generic v, taking W to
be its (111)-dimensional standard module. In either case, the quantized deformation admits a
quasi-triangular Hopf (super-)algebra structure and hence a link invariant (see [40], [28], or [37]).
However, there are some subtleties to these two alternative constructions, the main problem being
that the quantum invariant evaluates to zero on any link. This is reflection of the fact that the
quantum dimension vanishes on W for either algebra. The solution is to cut open the link to form
a (1, I)-tangle, so that the Reshetikhin-Turaev functor produces an endomorphism of W, which
by Schur's Lemma is a scalar.
3
w
1
w
(1.2)
Figure 1.2: A (1, I)-tangle and its associated endomorphism of W.
