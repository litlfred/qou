---
doc_id: 0309214v3
doc_title: "The colored Jones function is q –holonomic"
section_id: sec-003-13-plan-of-the-proof
section_title: "Plan of the proof"
section_number: 1.3
pages: 5-5
source_pdf: 0309214v3.pdf
source_sha256: 53967ef30b0aedb9
toc_source: outline
doc_brief: "The colored Jones function is q –holonomic — A function of several variables is called holonomic if, roughly speaking, it is determined from ﬁnitely many of its values via ﬁnitely many linear"
---
Plan of the proof
In Section 2, we discuss in detail the notion of a q–holonomic function. We give
examples of q–holonomic functions (our building blocks), together with rules
that create q–holonomic functions from known ones.
In Section 3, we discuss the colored Jones function of a link in 3–space, using
state sums associated to a planar projection of the link. The colored Jones
function is built out of local building blocks (namely, R–matrices) associated
to the crossings, which are assembled together in a way dictated by the planar
projection. The main observation is that the R–matrix is q–holonomic in all
variables, and that the assembly preserves q–holonomicity. Theorem 1 follows.
As a bonus, we present the colored Jones function as a multisum of a q–proper
hypergeometric function.
In Section 4 we show that the cyclotomic function of a knot (a reparametriza-
tion of the colored Jones function, introduced by Habiro, with good integrality
properties) is q–holonomic, too. We achieve this by studying explicitly a change
of basis for representations of sl2.
In Section 5 we give a theoretical review about complexity and computability of
recursion relations of q–holonomic functions, following Zeilberger. These ideas
solve the problem of ﬁnding recursion relations of q–holonomic functions which
are given by multisums of q proper hypergeometric functions. It is a fortunate
coincidence (?) that the colored Jones function can be presented by such a
multisum, thus we can compute its recursion relations. Theorem 2 follows.
Section 6 is a computer implementation of the previous section, where we use
Mathematica packages developed by A Riese.
In Section 7 we discuss the g–colored Jones function of a knot, associated to a
simple Lie algebra g. Our goal is to prove that the g–colored Jones function is
q–holonomic in all variables (see Theorem 6). In analogy with the g = sl2 case,
we need to show that the local building block, the R–matrix, is q–holonomic in
all variables. This is a trip to the world of quantum groups, which takes up the
rest of the section, and ends with an appendix which computes (by brute-force)
structure constants of quantized enveloping Lie algebras in the rank 2 case.
