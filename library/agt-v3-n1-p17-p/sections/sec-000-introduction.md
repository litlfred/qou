---
doc_id: agt-v3-n1-p17-p
doc_title: "Skein-theoretical derivation of some formulas of Habiro"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: agt-v3-n1-p17-p.pdf
source_sha256: df196f0a732ad6b9
toc_source: inferred
doc_brief: "Skein-theoretical derivation of some formulas of Habiro — We use skein theory to compute the coeﬃcients of certain power series considered by Habiro in his theory of sl2 invariants of integral homol"
---
In a talk at the Mittag-Leﬄer Institute in May 1999, K. Habiro announced a
new approach to computing the colored Jones polynomial of knots and quantum
sl2 invariants of integral homology 3-spheres. For an exposition, see his paper
[H2] (some results are already announced in [H1]). His invariant for homology
spheres recovers both the sl2 Reshetikhin-Turaev invariants at roots of unity,
and Ohtsuki’s power series invariants. Later, Habiro and T.Q.T. Le generalized
this to all quantum invariants associated to simple Lie algebras.
In the sl2 case, quantum invariants can be expressed in terms of skein theory,
using the Jones polynomial or the Kauﬀman bracket. Habiro’s invariant for
homology spheres can be constructed using certain skein elements ω = ω+ and
ω−1 = ω−such that circling an even number of strands with ω+ (resp. ω−)
induces a positive (resp. negative) full twist:
xeven
ω+
=
xeven
(1)
More precisely, ω+ and ω−are not skein elements, but inﬁnite sums (i.e. power
series) of such. But as long as they encircle an even number of strands (cor-
responding to a strand colored by an integer-spin representation of sl2), the
c⃝Geometry & Topology Publications
538
Gregor Masbaum
result is well-deﬁned. Also, it makes sense to consider powers of ω = ω+, and
circling an even number of strands with ωp induces p positive full twists, where
p ∈Z.
The main purpose of this paper is to give skein-theoretical proofs of Habiro’s
formulas for ω+ and ω−(they are stated already in [H1]) and for ωp (this
formula will appear in [H3]). Habiro’s original proofs of these formulas use the
quantum group Uqsl2.
This paper is organized as follows. After stating Habiro’s formula for ω+ and
ω−in Section 1, we give a proof using orthogonal polynomials along the lines
of [BHMV1] in Section 2. This proof is quite straightforward, although the
computations are a little bit more involved than in [BHMV1]. Unfortunately,
it seems diﬃcult to use this approach to compute the coeﬃcients of ωp for
|p| ≥2. Therefore, in Section 3 we start afresh using the Kauﬀman bracket
graphical calculus. A ﬁrst expression for ωp in Theorem 3.2 is easily obtained,
but it is not quite good enough, as an important divisibility property of the
coeﬃcients of ωp is not clear from this formula. This property is then shown in
Section 4 by some more skein theory. The ﬁnal expression for ωp obtained in
Theorem 4.5 is equivalent to Habiro’s one from [H3]. (The results of Section 2
are not used here, so that this gives an independent proof in the p = ±1 case
as well.)
To illustrate one use of ωp, we conclude the paper in Section 5 by giving a for-
mula for the colored Jones polynomial of twist knots. This generalizes formulas
of Habiro [H1] (see also Le [L1, L2]) for the trefoil and the ﬁgure eight knot.
(For those two knots, one only needs Habiro’s original ω+ and ω−.)
Habiro has proved (again using quantum groups) that formulas of this type exist
for all knots, but the computation of the coeﬃcients is not easy in general. For-
mulas of this kind are important for at least two reasons: computing quantities
related to the Kashaev-Murakami-Murakami volume conjecture [Ka, MM], and
computing Habiro’s invariant of the homology sphere obtained by ±1 surgery
on the knot. For more about this, see Habiro’s survey article [H2].
Acknowledgements I got the idea for this work while talking to T.Q.T. Le
during his visit to the University of Paris 7 in July 2002. I would like to thank
both him and K. Habiro for helpful discussions, and for sending me parts of
their forthcoming papers [L2] and [H3].
Algebraic & Geometric Topology, Volume 3 (2003)
Skein-theoretical derivation of some formulas of Habiro
539
