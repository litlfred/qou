---
doc_id: arxiv-2503.08846v1
doc_title: "A Tutorial on Knots and Quantum Mechanics"
section_id: sec-002-topological-invariants-from-matrix-traces
section_title: "Topological invariants from matrix traces"
section_number: null
pages: 6-7
source_pdf: A_Tutorial_on_Knots_and_Quantum_Mechanics.pdf
source_sha256: 18321b615ffc968b
toc_source: outline
doc_brief: "A Tutorial on Knots and Quantum Mechanics — These notes review a description of quantum mechanics in terms of the topology of spaces, basing on the axioms of Topological Quantum Field Theory and path"
---
Topological invariants from matrix traces
It will be useful to review a few important steps explaining the origin of the Jones polynomial, as they
will also be helpful for later applications.
An important object is the (Artin) braid group.
This group is a generalization of the group of
permutations of n elements and can be defined in terms of n −1 generators:
Bn := {bk, k = 1, . . . , n −1| bibi+1bi = bi+1bibi+1, i = 1, . . . , n −2; bibj = bjbi, |i −j| > 1} .
(10)
In other words, group Bn consists of all words constructed of n −1 letters bk, satisfying the above
relations. The relations are the same as for the generators of the permutation group, with the exception
of the requirement that the generators square to identity. Relaxing this condition makes the braid group
infinite, unlike the permutation group.
Braid group has a diagrammatic presentation as an evolution of n points on a line. For example, the
generators of the group are represented by
b1 =
· · ·
,
b2 =
· · ·
,
b3 =
· · ·
. . .
(11)
The inverse generators have the opposite order of line crossing (left twists, as opposed to right twists):
b−1
1
=
· · ·
,
b−1
2
=
· · ·
,
. . .
b−1
n−1 =
· · ·
.
(12)
Group multiplication is organized by stacking the diagrams of the group elements on top of each other:
b2b1 =
· · ·
· · ·
,
b2b−1
2
=
· · ·
· · ·
.
(13)
The diagrams give a faithful representation of the group elements and have an obvious relation with knot
diagrams. In particular, it is easy to see that the II and the III Reidemeister moves of knot diagrams
guarantee the braid group relations.
A theorem, proven by Alexander, states that any knot or link diagram can be obtained as a tracelike
closure of some braid. By a tracelike closure one understands the pairwise connection of all top and
bottom points of the same order with nonintersecting lines. Here are two examples, how the simplest
nontrivial trefoil knot can be obtained from two tracelike closures:
∼
∼
.
(14)
6
In the above examples the braids were oriented horizontally to optimize space.
Since braid diagrams respect two of the three Reidemeister moves and the tracelike closures of braids
form knot diagrams, one may wonder if traces of matrix representation of braids can yield topological
invariants. In fact, naive trace will not do the job. Andrei Markov proved a theorem explaining what kind
of traces gives an invariant. The so-called Markov trace TrM should satisfy the following two properties:
• (cyclicity) for two braids α and β
TrM(α · β) = TrM(β · α)
(15)
• (Markov property) for braid βn ∈Bn and its embedding βn · bn in Bn+1,
TrM(βn) = TrM(βn · b±1
n )
(16)
Markov property can be expressed diagrammatically as
βn
∼
βn
,
(17)
which is a particular expression of the I Reidemeister move. Therefore, Markov traces of braids should be
invariant under all the Reidemester moves, or, in other words, they should compute topological invariants
of knots and links.
