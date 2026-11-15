---
doc_id: arxiv-2601.07906v2
doc_title: "A universal sum over topologies in 3d gravity"
section_id: sec-024-tricolorability-and-handlebodyness
section_title: "Tricolorability and handlebodyness"
section_number: null
pages: 85-87
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
toc_source: outline
doc_brief: "A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
Tricolorability and handlebodyness
Computing the fundamental group and applying the Whitehead algorithm is a sys-
tematic way to check whether two handlebody-knots are equivalent, as long as the
fundamental group only has one relation. There is another simpler test to distinguish
handlebody-knots. In the main text, we used the fundamental group as an invariant
as discussed in appendix A.2 for the handlebody-knot 52. The goal of this section is
to present a much simpler criterion for detecting non-trivial handlebody-knots. This
test is a generalization of tricolorability for classical knots.
Tricolorability for knots.
Let us first review tricolorability for regular knots. A
knot is called tricolorable if each segment of the knot when projected onto the plane
can be colored using the following set of rules:
1. All three colors must be used.
2. At every crossing all three colors are used, or only one color is used.
If any two knots are related to each other via Reidemeister moves, then either both
knots are tricolorable, or neither is. In particular, the unknot is not tricolorable.
The classic example of a tricolorable knot is the trefoil,
.
(A.18)
– 85 –
Tricolorability for handlebody-knots.
For handlebody-knots, a very similar
test applies with a few modifications. First, we need to pick a link component of the
diagram. We call this component the enhanced constituent link of the handlebody-
knot. Examples of enhanced constituent links are given below in (A.19); they cor-
respond to the edges with double lines in the diagrams. Note that the enhanced
constituent link may have more than one component. We say that an edge is thick,
if it is part of an enhanced constituent link; we refer to the rest of the edges as thin.
A handlebody-knot diagram with an enhanced constituent link is tricolorable if
we can color it following the rules:
1. All three colors must be used.
2. At every trivalent vertex, the colors of each edge must be the same.
3. At every crossing:
a) If the over-edge is thick, then either all colors are used, or only one color
is used.
b) If the over-edge is thin, then the under-edges do not change color.
Below are a few examples of tricolorable handlebody-knots:
(A.19)
Note that depending on the choice of enhanced constituent link, the diagram may or
may not be colorable. For a handlebody-knot to be tricolorable, we simply require
that an enhanced constituent link exists such that the diagram can be colored.
Importantly, the trivial handlebody-knot is not tricolorable, as it can be seen
from the diagram below; regardless of the choice of enhanced constituent link, only
the trivial coloring is possible:
.
(A.20)
The tricolorability criterion was introduced in [135], where it was demonstrated
that if two handlebody-knots are related to each other by a sequence of moves which
include the F and B transforms, and all the Reidemeister moves, then they are
both tricolorable or neither is. This shows that no tricolorable handlebody-knot, in
particular those in (A.19), can be a handlebody.
– 86 –
