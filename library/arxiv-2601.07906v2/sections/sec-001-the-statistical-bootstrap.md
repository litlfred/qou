---
doc_id: arxiv-2601.07906v2
doc_title: "March 2026 A universal sum over topologies in 3d gravity"
section_id: sec-001-the-statistical-bootstrap
section_title: "The statistical bootstrap"
section_number: null
pages: 9-11
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
doc_brief: "March 2026 A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS 3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
In fact, it seems perfectly consistent to take any on-shell and acylindrical ‘seed’,
consider its orbit under the action of the machine, and decide to add this orbit to
the sum over topologies or not. This gives an infinite number of choices, signaling
a large redundancy in the possible consistent statistical descriptions for 3d gravity.
This seems contrary to our expectation that pure 3d gravity would, in some sense,
be the simplest theory satisfying the statistical bootstrap.
We could turn this question around and instead ask: What are the minimal
properties imposed on a statistical ensemble of CFT 2 data that uniquely select 3d
gravity, including the full sum over topologies? It is logically possible that adding
conditionsbeyondthose we have imposed (such as a version of the moment problem
[49], the existence of a matrix-tensor model [7, 8], or the presence of random matrix
universality in the CFT spectrum [50]) requires more topologies for these additional
conditions to be satisfied. We come back to this important open question in the
discussion.
Plan of the paper.In section 2, we will define the conditions that any statistical
theory of CFT 2 data dual to pure 3d gravity must satisfy. Then, in section 3 we
show that the condition of crossing symmetry (at all genera) is solved by summing
– 9 –
over handlebodies, explaining in particular the relation to non-Gaussianities in the
statistics of OPE coefficients. Although this is mainly a review, it sets up a lot of the
formalism that will be needed in the following sections. In section 4, we show how the
condition of typicality, combined with crossing and consistency conditions between
higher and lower moments, leads to non-handlebodies in the bulk. The gravitational
machine is introduced as a way to systematize these non-handlebody contributions,
and its main properties are proven. In section 5, we apply the machine to produce a
variety of examples of non-handlebodies, and compute their partition functions. We
end with a discussion and an outlook for future work. Finally, in the appendices we
have collected many technical results about 3-manifolds, their fundamental groups,
and Virasoro TQFT that are needed in the main text.
2 The statistical bootstrap
The goal of this section is to define a statistical theory that models compact irrational
CFT2’s with a pure Einstein gravity dual at large central chargec[51]. Such CFT 2’s
have no extended chiral algebra beyond Virasoro symmetry, so we will organize the
spectrum of (L0, ¯L0) into Virasoro primaries and descendants. The descendant states
are fixed by symmetry, so they should not be treated as random variables. On the
other hand, the conformal primaries will be treated statistically.
Let us imagine there exists a probability distributionµ({h i, ¯hi,Cijk}) that we
can use as a statistical model for the dynamical CFT 2 data, which consist of the
infinite list of primary conformal dimensions ∆ i =h i + ¯hi, integer spinsJ i =h i− ¯hi
and primary OPE coefficientsC ijk≡C hihjhk. We package the spectral data in terms
of the density of primary states,
ρ(h, ¯h) =
X
i
δ(hi−h)δ( ¯hi− ¯h),(2.1)
where the sum is over the primary spectrum, with a similar formula for the density
of OPE coefficients (as in [52]). The average of any function of OPE coefficients and
conformal weights is then defined by integrating it against the measureµ:
F({hi, ¯hi,Cijk}) =
Z
dL0d¯L0dCµ({h i, ¯hi,Cijk})F({hi, ¯hi,Cijk}).(2.2)
Here dCis a volume element on the space of rank-3 tensors.
Crucially, we will impose a number of conditions on the moments of this prob-
ability distributionµ, such that the statistical model is a good approximation of a
holographic CFT 2 in the large-climit. 6 The goal of this section is to specify these
6In particular, we do not assume that the average is taken over an ensemble of ‘true’ CFT’s.
For an exploration of probability distributions on the space of 2d CFT’s, see the recent work [53].
Also, for a more in-depth discussion about the notion of an ‘approximate CFT’ we refer the reader
to section 2 of [7].
– 10 –
conditions, which we will refer to as the “statistical bootstrap”. We will mostly as-
sume that the spectrum of (L 0, ¯L0) has a twist gap all the way up to the black hole
threshold, meaning thath i, ¯hi is either zero (the vacuum, denoted by1) or bigger
than c−1
24 . However, the material presented in this section can also be extended to
incorporate states below the threshold in the conical defect regime [26], as will be
discussed in section 3.
Let us emphasize that although we take the conditions considered in this section
to benecessary, they need not be sufficient: we have not exhausted all constraints
on the distributionµthat one may want to impose. In the discussion, we comment
on the possibility of imposing additional constraints on the moments, that arise (for
example) from positivity ofµand the Stieltjes/Hamburger moment problem.
