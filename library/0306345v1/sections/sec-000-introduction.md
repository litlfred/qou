---
doc_id: 0306345v1
doc_title: "Published: 16 June 2003 Skein-theoretical derivation of some formulas of Habiro Gregor Masbaum"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 0306345v1.pdf
source_sha256: 936aa08026b2683b
doc_brief: "Skein-theoretical derivation of some formulas of Habiro — We use skein theory to compute the coecients of certain power series considered by Habiro in his theory ofsl2 invariants of integral homol"
duplicate_of: "agt-v3-n1-p17-p"
---
In a talk at the Mittag-Leﬄer Institute in May 1999, K. Habiro announced a
new approach to computing the colored Jones polynomial of kn ots and quantum
sl2 invariants of integral homology 3-spheres. For an expositi on, see his paper
[H2] (some results are already announced in [H1]). His invar iant for homology
spheres recovers both the sl2 Reshetikhin-Turaev invariants at roots of unity,
and Ohtsuki’s power series invariants. Later, Habiro and T. Q.T. Le generalized
this to all quantum invariants associated to simple Lie alge bras.
In the sl2 case, quantum invariants can be expressed in terms of skein t heory,
using the Jones polynomial or the Kauﬀman bracket. Habiro’s i nvariant for
homology spheres can be constructed using certain skein ele ments ω = ω + and
ω −1 = ω − such that circling an even number of strands with ω + (resp. ω − )
induces a positive (resp. negative) full twist:
xeven
ω + =
xeven
(1)
More precisely, ω + and ω − are not skein elements, but inﬁnite sums ( i.e. power
series) of such. But as long as they encircle an even number of strands (cor-
responding to a strand colored by an integer-spin represent ation of sl2 ), the
c© G eometry & Topology Publications
538 Gregor Masbaum
result is well-deﬁned. Also, it makes sense to consider powe rs of ω = ω + , and
circling an even number of strands with ω p induces p positive full twists, where
p ∈ Z.
The main purpose of this paper is to give skein-theoretical p roofs of Habiro’s
formulas for ω + and ω − (they are stated already in [H1]) and for ω p (this
formula will appear in [H3]). Habiro’s original proofs of th ese formulas use the
quantum group Uqsl2 .
This paper is organized as follows. After stating Habiro’s f ormula for ω + and
ω − in Section 1, we give a proof using orthogonal polynomials al ong the lines
of [BHMV1] in Section 2. This proof is quite straightforward , although the
computations are a little bit more involved than in [BHMV1]. Unfortunately,
it seems diﬃcult to use this approach to compute the coeﬃcien ts of ω p for
|p| ≥ 2. Therefore, in Section 3 we start afresh using the Kauﬀman br acket
graphical calculus. A ﬁrst expression for ω p in Theorem 3.2 is easily obtained,
but it is not quite good enough, as an important divisibility property of the
coeﬃcients of ω p is not clear from this formula. This property is then shown in
Section 4 by some more skein theory. The ﬁnal expression for ω p obtained in
Theorem 4.5 is equivalent to Habiro’s one from [H3]. (The res ults of Section 2
are not used here, so that this gives an independent proof in t he p = ±1 case
as well.)
To illustrate one use of ω p , we conclude the paper in Section 5 by giving a for-
mula for the colored Jones polynomial of twist knots. This ge neralizes formulas
of Habiro [H1] (see also Le [L1, L2]) for the trefoil and the ﬁg ure eight knot.
(For those two knots, one only needs Habiro’s original ω + and ω − .)
Habiro has proved (again using quantum groups) that formula s of this type exist
for all knots, but the computation of the coeﬃcients is not ea sy in general. For-
mulas of this kind are important for at least two reasons: com puting quantities
related to the Kashaev-Murakami-Murakami volume conjectu re [Ka, MM], and
computing Habiro’s invariant of the homology sphere obtain ed by ±1 surgery
on the knot. For more about this, see Habiro’s survey article [H2].
Acknowledgements I got the idea for this work while talking to T.Q.T. Le
during his visit to the University of Paris 7 in July 2002. I wo uld like to thank
both him and K. Habiro for helpful discussions, and for sendi ng me parts of
their forthcoming papers [L2] and [H3].
Algebraic & Geometric Topology, Volume 3 (2003)
Skein-theoretical derivation of some formulas of Habiro 539
