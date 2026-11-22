---
doc_id: arxiv-alg-geom-9408004v1
doc_title: "Cubics, Integrable Systems, and Calabi-Yau Threefolds"
section_id: sec-001-front-matter-page-2
section_title: "Front matter (page 2)"
section_number: null
pages: 2-2
source_pdf: 9408004v1.pdf
source_sha256: d3bc00265294aa02
toc_source: inferred
doc_brief: "Cubics, Integrable Systems, and Calabi-Yau Threefolds — 28 sections: Front matter (page 1); Front matter (page 2); Front matter (page 3)"
---
The last section is entirely speculative. We muse on the role which the
CY integrable system might play in the mirror conjecture: we would like to
separate the conjecture into a formal part, which deals with a ‘mirror trans-
form’ for objects consisting of an integrable system together with certain La-
grangian multisections and other lists of data, and a geometric, Torelli-like
part, saying that a CY family can be recovered from its integrable system.
The attempt to read oﬀall relevant data (= the partition functions for the
A and B models) directly from the system leads to some Hodge theoretic
questions which we cannot solve, concerning the information encoded in a
normal function and especially in its inﬁnitesimal invariant.
It is our pleasure to acknowledge beneﬁcial and pleasant conversations
with R. Bryant, I. Dolgachev, M. Green, P. Griﬃths, S. Katz, L. Katzarkov,
D. Morrison, T. Pantev and E. Witten.
§1. The cubic condition.
Our goal in this section is to describe the conditions on a given family
π : X →U of abelian varieties (or complex tori) for there to exist, locally
over U, an algebraic (or analytic) symplectic structure σ on X such that π
is a Lagrangian ﬁbration with respect to σ. (In this situation we say that
the family admits a Lagrangian structure.) What we want is a closed, non-
degenerate holomorphic 2-form σ on X such that the ﬁbers Xu := π−1(u)
are Lagrangian (= maximal isotropic) subvarieties with respect to σ.
By way of motivation, let us review the corresponding questions for C∞
objects. Any C∞family π : X →U of real tori is locally trivial, i.e. locally
(over U) isomorphic to U × (S1)n. In particular, a Lagrangian structure
exists whenever dim U = n = dim (ﬁbers). Given a C∞symplectic mani-
fold (X , σ) with Lagrangian ﬁbration π : X →U, there is a natural aﬃne
structure on the ﬁbers Xu [AG,2.42]; so if these ﬁbers are compact, they
must be tori. In this case the base U also acquires a natural integral-aﬃne
structure, i.e. an atlas of coordinate systems which diﬀer on intersections
by a combination of arbitrary translations and Z-linear transformations. To
get these coordinates, we choose a basis γ1(u), · · ·, γn(u) for the integral ho-
mology H1(Xu, Z), varying smoothly with u in an open subset U0 of U, as
well as a 1-form τ on π−1(U0) satisfying dτ = σ. (These always exist.) We
then let
(1)
ti(u) :=
Z
γi(u) τ,
i = 1, · · ·, n.
The freedom of changing τ (by a closed 1-form) and the γi (by the action
of GLn(Z)) then allows the ti to change by a translation and Z-linear trans-
formation, respectively. These ti are called action variables. They deﬁne
2
