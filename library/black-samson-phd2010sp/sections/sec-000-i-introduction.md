---
doc_id: black-samson-phd2010sp
doc_title: "REPRESENTATIONS OF HECKE"
section_id: sec-000-i-introduction
section_title: "INTRODUCTION"
section_number: I
pages: 9-14
source_pdf: Black_Samson_phd2010sp.pdf
source_sha256: c16799b0bd54ff29
toc_source: inferred
doc_brief: "REPRESENTATIONS OF HECKE — 16 sections: Front matter; INTRODUCTION; ILL Links and Braids"
---
1.1.
Historical Background
The Alexander polynomial has a history dating back to the early days of algebraic topology.
The original definition ([1]) came from analyzing the group of deck transformations on the infinite
cyclic cover of the complement of a knot. In the same paper, Alexander reduced the calculation of
the invariant to a combinatorial procedure using knot diagrams. Decades later, Conway introduced
a special normalization of the invariant ([9]) extended to links, denoted \7(L), that was recursively
computable using a skein relation on the diagrams (see Figure 1.1).
x x
) (
Lo
Figure 1.1: The Conway skein relation:
Following the discovery by Jones of a new invariant ([23] and also [10, Chapter 9] for
an interesting account of the discovery), there was an explosion of interest in the industry of
producing link invariants using skein theories. \Vithin a year, a two-variable polynomial invariant
was simultaneously introduced by several independent groups of authors, all of whose names are
celebrated in the acronym: HOMFLYPT ([14] and [34]). Using the skein theoretic approach, we
first pass to a diagram of the link, which involves the choice of a generic projection onto a plane.
The verification that a function on these diagrams is well-defined as a function of the original link
reduces to the formal task of checking invariance under the Reidemeister moves.
Much of the
geometry of three dimensional space is lost in the passage to a diagram, but the trade-off is that
many of the tools of representation theory which have no obvious connection to the original link
2
can be brought to bear. The menagerie of quantum invariants that exists today comes about in
this manner.
In the seminal work of Reshetikhin and Turaev ([36]), they construct quantum link in-
variants as tensor functors from the tensor category of colored tangles to the category of modules
over the quantum group Uv(g), for 9 a simple complex Lie algebra, using the quasi-triangular Hopf
algebra structure on Uv(g) and choosing representations to label components. Specifically, a (d, d')-
tangle connecting d' points on the bottom to d points on the top produces a Uv(g)-homomorphism
VVP1 ® ... ® W"d'
--'I vV)\] ® ... ®W'\d' where the modules Wllj and W,\., are determined by the colors
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
of A.
Another approach is to use the superalgebra Uv (g[(111)) with a generic v, taking W to
be its (111 )-dimensional standard module.
In either case, the quantized deformation admits a
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
1.2.
Summary of Thesis
In this dissertation, we consider a third alternative, indirectly related to the g[(111)-
approach, but we work only with braids, which is Jones' approach via Markov traces ([24]). There
is essentially no loss of generality, as any link has a diagram presenting it as the closure of a braid.
In Chapter II, we recall some of the basics regarding links, braids, and invariants. The
HOMFLYPT polynomial is constructed from representations of the braid group, factoring through
the Iwahori-Hecke algebra Hd (as in [24], although our notations are substantially different). Also,
a converse is presented:
an invariant of links defined on braids that satisfies a skein relation
necessarily factors through the Hecke algebra. This latter perspective, namely that skein relations
determine certain algebras, is a motivation for the results in Chapter III. The remainder of the
chapter is devoted to a particular example: the Jones polynomial. We introduce the Temperley-
Lieb algebra T Ld, both as an explicit quotient of the Hecke algebra and as a diagrammatic algebra
carrying a particularly elegant trace. There are no new results here beyond the considerable task
of gathering this wealth of constructions and formulae into one consistent notational framework.
The groundwork is laid for the following chapters where certain analogous results are derived for
the Alexander polynomial.
In Chapter III, we look at special cases of Schur-Weyl duality between H d and Uv(g[(mln))
on tensor space.
In particular, the representations of the Heeke algebra from Chapter II are
explicitly connected to the Reshetikhin-Turaev intertwiners. The Temperley-Lieb algebra appears
here as the centralizer algebra ofUv(g) in End(VI8J·· 'I8JV) for g[(210) = g[(2), or equivalently .5[(2).
Hence, using results of Jimbo ([21] and [22]), building on the classical work of Schur ([38]) and
Weyl ([41, Chapter III]), TL d is presented as a product of matrix algebras indexed by partitions
of at most two rows. As the Wedderburn components for Young diagrams of more than two rows
form a cellular ideal in Hd' the quotient T Ld inherits the cellular structure from Hd. In fact, T Ld
has a natural diagram basis that is easy to express in terms of the standard basis for Hd; hence,
4
the Markov trace on nd that produces the Jones polynomial can be calculated diagrammatically.
The Kauffman state-sum for the Jones polynomial comes directly from this formalism for TLd .
One of the goals of this work, only partially realized, is to find an analogous formalism for the
Alexander polynomial.
Alas, the story for the Alexander polynomial is not so simple. The Super Temperley-Lieb
algebra STLd is defined as the intertwiner algebra for the quantum group associated to g[(111).
Hence, the Markov trace on nd giving the Alexander polynomial on braids factors through STLd.
This algebra has Wedderburn components indexed by hook partitions.
However, the ideal that
consists of components that are not hooks is not cellular in the dominance order on partitions, and
so STLd does not inherit the cellular structure from nd and the map nd --» STLd is quite subtle.
\Ve can obtain a basis for STLd' but it has no clear connection to the standard basis for nd, and so
it is not obvious how to calculate the Markov trace directly. In fact, because the transition matrix
from the standard basis for nd to our basis for STLd is only defined upon extending scalars to iQl(v),
it is no longer clear that the Alexander invariant is a Laurent polynomial in Z[v, V-I]. The main
result in this section is a presentation of the relations for STLd using some of the combinatorics
of the symmetric group adapted to nd.
This is why in Chapter IV we start again using Young's seminormal form for nd.
To
begin, STL d is presented as a diagram algebra in the basis of matrix units of its Wedderburn
components. As a result, a lot of complicated information is packaged in the idempotents in nd
that project onto STLd. Using character formulas of Geck and Jacon ([16], [17]) for the irreducible
representations of nd and building upon the work of Jones ([24]), a combinatorial procedure is
deduced for calculating the trace, and hence the Alexander polynomial, from a braid diagram
directly. This state-sum has the appeal of being computable in terms of certain labeled diagrams
(the basis for STLd) that come from resolving crossings in the original braid. The trade-off for
changing basis so drastically is the aforementioned difficulty that the formula gives the Alexander
polynomial as a sum of rational functions involving quantum integers, obscuring the fact that the
invariant is actually a Laurent polynomial.
In Chapter V, we reprove the main theorem combinatorially. By analyzing possible states
in the expansion of a braid diagram, we are able to check invariance under the Markov moves
directly. Moreover, agreement with the Alexander polynomial is verified. This "naive" proof has
an unexpected advantage: it may be possible to extend the state-sum formula to the multivariable
5
Alexander polynomial using colored braids, as in the work of Murakami ([33]), using the combi-
natorics directly. In a different direction, we hope to recover the Alexander invariant for virtual
links ([27]) as a state-sum in an analogous fashion.
6
CHAPTER II
BRAIDS, LINKS, AND THE JONES POLYNOMIAL
