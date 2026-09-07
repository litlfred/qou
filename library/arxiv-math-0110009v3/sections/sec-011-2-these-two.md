---
doc_id: arxiv-math-0110009v3
doc_title: "New upper bounds on sphere packings I"
section_id: sec-011-2-these-two
section_title: "These two"
section_number: 2
pages: 3-4
source_pdf: 0110009v3.pdf
source_sha256: bb0c97f2de33b0dd
doc_brief: "New upper bounds on sphere packings I — We develop an analogue for sphere packing of the linear progr amming bounds for error-correcting codes, and use it to prove upper bounds for the density of"
---
lattices have many remarkable properties and connections w ith other branches
of mathematics, but so far these properties have not led to a p roof that they are
optimal sphere packings. We conjecture that our linear prog ramming bounds
can be used to prove optimality.
If linear programming bounds can indeed be used to prove the o ptimality
of these lattices, it would not come as a complete surprise, b ecause other pack-
ing problems in these dimensions can be solved similarly. Th e most famous
example is the kissing problem: how many nonoverlapping uni t balls can be
arranged tangent to a given one? If we regard the points of tan gency as a spher-
ical code, the question becomes how many points can be placed on a sphere
with no angles less than π/ 3. Odlyzko and Sloane [OS] and Levenshtein [Lev]
independently used linear programming bounds to solve the k issing problem in
692 HENRY COHN AND NOAM ELKIES
4 8 12 16 20 24 28 32
0
1
2
3
4
−1
−2
−3
upper curve: Rogers’ upper bound
lower curve: New upper bound
bottom line: Best packing known
Figure 1. Plot of log 2 δ + n(24 − n)/ 96 vs. dimension n.
8 and 24 dimensions. (The solutions in dimensions 8 and 24 are obtained from
the minimal nonzero vectors in the E8 and Leech lattices.) Because we know
a priori that the answer must be an integer, any upper bound within les s than 1
of the truth would suﬃce. Remarkably, the linear programmin g bound gives
the exact answer, with no need to take into account its integr ality. By contrast,
in most dimensions it gives a noninteger. The remarkable exa ctness seems to
occur only in dimensions 1, 2, 8, and 24. We observe the same nu merically in
our case, but can prove it only for dimension 1.
Figure 1 compares our results with the best packings known as of Decem-
ber, 2002 (see Tables I.1(a) and I.1(b) of [CS, pp. xix, xx]), and the best upper
bounds previously known in these dimensions (due to Rogers [ Ro]). The graph
was normalized for comparison with Figure 15 from [CS, p. 14] .
