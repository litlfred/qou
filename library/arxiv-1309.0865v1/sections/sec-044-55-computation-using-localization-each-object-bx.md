---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-044-55-computation-using-localization-each-object-bx
section_title: "Computation using localization. Each object Bx in D splits in Kar (DQ) as the"
section_number: 5.5
pages: 53-55
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnati on of the Hecke category , a fundamental object in representation the ory ."
---
sum of Qe over all subsequences e of x. Here, Qe denotes the object which is the
tensor product of Qxk when ek = 1 and /BD when ek = 0 . Given a graph expressing
a morphism from a sequence Bx of length d to a sequence Bx′ of length d′, we can
localize to obtain a 2d′
× 2d matrix of maps between reﬂection sequences. Since Hom
spaces between standard bimodules are always either rank 1 o r 0, this matrix is ac-
tually populated with polynomials in Q, and is fairly sparse (because many Hom
spaces are zero a priori). Computing any term in this matrix c onsists of applying the
appropriate projection and inclusion maps to the top and bot tom of the graph, and
using the diagrammatics of Kar (DQ) to reduce the graph to a dashed graph with the
desired polynomial on the left. That is, given (x, e) and (x′, e′), the coefﬁcient of the
mapQe →Qe′ of a map φ is given by reducing the following diagram φe′
e .
1
αr
1
αr
1
αg
1
αb
1
αb
There is no sign issue in this convention, even though a mixed graph represents a
morphism only up to sign. For any Soergel graph φ we start with, we can choose a
representative of the isotopy class, and add idempotents as above to obtain a speciﬁc
representative of the mixed graph. Different representati ves of φ will give different
mixed graphs, but they differ only by isotopy of the solid par t of the graph, and
therefore have the same sign when viewed as morphisms in Kar (DQ).
Note that by (5.28), the coefﬁcient associated to e = (1, 1,..., 1) and e′ = (1, 1,..., 1)
of a 2m-valent vertex is precisely 1. Therefore, for any rex move, this “highest” coef-
ﬁcient will be 1.
54 BEN ELIAS AND GEORDIE WILLIAMSON
One can check if two maps in D are equal by computing these two matrices and
comparing the terms. More combinatorially , one can compute once and for all the
“basic” matrices attached to the generating morphisms. For instance, the dot gives a
2 × 1 matrix, the trivalent vertex a 4 × 2 matrix, and the 2m-valent vertex a 2m × 2m
matrix. Computing a more general map consists merely of mult iplying these basic
matrices and annoying bookkeeping. Computers excel at such tasks.
We have not yet proven it, but the passage D → D Q is faithful. Not knowing this,
the equality of two matrices only implies that the original m aps are equal moduloR-
torsion. However, location is injective in the bimodule wor ld, because Hom spaces
are free leftR-modules. In other words, all R-torsion is in the kernel of the functor F .
Therefore we can calculate whether two Soergel graphs have t he same image under
F by localizing D → Kar(DQ) and computing the matrices above. This is a powerful
tool.
For instance, we want to know whether both sides of the B3 relation (5.11) corre-
spond to the same map between Bott-Samelson bimodules. One n eed only compute
by hand the matrices associated to the 4-valent, 6-valent, a nd 8-valent vertices, and
then plug in two appropriate formulae into a computer. Check ing that two sparse
matrices of size 28 × 28 are equal is trivial. If we knew what the H3 relation (5.12)
should be, then checking it would require calculating the 10 -valent vertex (which
is easy), and then computation of a pair of 215 × 215 matrices (which is quite time-
consuming). Unfortunately , backsolving for the coefﬁcien ts in the H3 relation would
require doing linear algebra with a large number N of unknowns (at least 70). There
is an equation for each nonzero term in a sparse 215 × 215 matrix, and the coefﬁ-
cients come fromN different such matrices which need to be computed. Neither t he
author’s computers nor their brains appear to be up to the tas k.
Finally , we provide the alternative proof of faithfulness.
Proposition 5.25. Std is faithful.
Proof. In fact, the techniques we have developed allow us to construct a quasi-inverse
for Std. We construct a functor G from Kar(DQ) to Dstd
Q as follows. Let G send reﬂec-
tion sequences to themselves, and normal sequences to the co rresponding formal
direct sum of reﬂection sequences. On morphisms, G will send standard graphs to
themselves. The generating morphisms which are not standar d graphs are sent as
follows: a bivalent vertex is sent to the appropriate inclus ion or projection; a dot or
trivalent vertex or 2m-valent vertex is sent to the appropriate matrix of standard dia-
grams. It is trivial to check that all the relations hold, so t his functor is well-deﬁned,
and is obviously a quasi-inverse to Std. □
Remember that diagrams and their linear combinations are on ly useful for dis-
playing morphisms between tensor products of generators, n ot for direct sums of
those. To talk about a morphism between direct sums, we need t o use matrices of di-
agrams. Thus we do not expect there to be an actual diagram in Dstd
Q corresponding
to a solid graph.
SOERGEL CALCULUS 55
This proof that Kar (DQ) ∼= Dstd
Q was entirely diagrammatic, and no mention of
bimodules was required.
