---
doc_id: arxiv-0704.1313v1
doc_title: "Mutant knots and intersection graphs"
section_id: sec-007-the-sl2-weight-system
section_title: "The sl(2) weight system"
section_number: null
pages: 9-11
source_pdf: 0704.1313v1.pdf
source_sha256: a75bb39c60ec9b15
toc_source: outline
doc_brief: "Mutant knots and intersection graphs — We prove that if a ﬁnite order knot invariant does not disting uish mutant knots, then the corresponding weight system depends on the interse ction graph of a"
---
Our treatment of the universal weight system associated with the Lie algebra sl(2)
is based on the recurrence formula for computing the value of this w eight system on
chord diagrams due to Chmutov and Varchenko [7]. The recurrence states that if a
chord diagram contains a leaf, that is, a chord intersecting only one other chord, then
the value of the sl(2) universal weight system on the diagram is ( c − 1/ 2) times its
value on the result of deleting the leaf, and, in addition,
− − + = 2 − 2
meaning that the value of the weight system on the chord diagram on the left-hand
side coincides with the linear combinations of its values on the chord dia grams indi-
cated on the right.
Now, in order to prove Theorem 3 for the universal sl(2) weight system, we must
prove that mutations of a chord diagram preserve the values of th is weight system.
9
Take a chord diagram and a share in it. Apply the above reccurence f ormula to a
chord and two its neighbors belonging to the chosen share. The rec urrence relation
does not aﬀect the complementary share, while all the instances of the modiﬁed ﬁrst
share are simpler than the initial one (each of them contains either f ewer chords or
the same number of chords but with fewer intersections). Repeat ing this process, we
can replace the original share by a linear combination of the simplest s hares, chains,
which are symmetric meaning that they remain unchanged under rot ations. The sl(2)
case of Theorem 3 is proved. □
Now let us turn to the proof of Theorem 4. For elementary notions o f matroid
theory we refer the reader to any standard reference, say to [1 9]. Recall that a matroid
can be associated to any graph. It is easy to check that the matro id associated to the
disjoint union of two graphs coincides with that for the graph obtain ed by identifying
a vertex in the ﬁrst graph with a vertex in the second one. We call th e result of
gluing a vertex in a graph G1 to a vertex in a graph G2 a 1 -product of G1 and G2.
The converse operation is 1 -deletion. Of course, the 1-product depends on the choice
of the vertices in each of the factors, but the corresponding mat roid is independent
of this choice.
Similarly, let G1, G2 be two graphs, and pick vertices u1, v 1 in G1 and u2, v 2 in G2.
Then the matroid associated to the graph obtained by identifying u1 with u2 and v1
with v2 coincides with the one associated to the graph obtained by identifyin g u1 with
v2 and u2 with v1. The operation taking the result of the ﬁrst identiﬁcation to that
of the second one is called the Whitney twist on graphs.
Both the 1-product and the Whitney twist have chord diagram analo gs. For two
chord diagrams with a distinguished chord in each of them, we deﬁne t heir 1-product
as a chord diagram obtained by replacing the distinguished chords in t he ordinary
product of chord diagrams chosen so as to make them neighbors by a single chord
connecting their other ends. The Whitney twist also is well deﬁned be cause of the
following statement.
Lemma 1 Suppose the intersection graph of a chord diagram is the resu lt of identi-
fying two pairs of vertices in two graphs G1 and G2. Then both graphs G1 and G2 are
intersection graphs, as well as the Whitney twist of the orig inal graph.
The assertion concerning the graphs G1 and G2 is obvious. In order to prove that
the result of the Whitney twist also is an intersection graph, let c1, c 2 denote the
two chords in a chord diagram C such that deleting these chords makes C into an
ordinary product of two chord diagrams C1, C 2. By reﬂecting the diagram C2 and
restoring the chords c1 and c2 we obtain a chord diagram whose intersection graph is
the result of the desired Whitney twist. The lemma is proved.
According to the Whitney theorem, two graphs have the same matr oid iﬀ they
can be obtained from one another by a sequence of 1-products/d eletions and Whitney
twists. Therefore, Theorem 4 follows from
Lemma 2 (i) The value of the universal sl(2) weight system on the 1-product of chord
diagrams coincides with the product of its values on the fact ors divided by c. (ii) The
10
value of the universal sl(2) weight system remains unchanged under the Whitney twist
of the chord diagram.
Statement (i) is proved in [7]. The proof of statement (ii) is similar to th at of
Theorem 3. Consider the part C2 participating in the Whitney twist and apply to
it the recurrence relations. Note that the relations do not aﬀect t he complementary
diagram C1. Simplifying the part C2 we reduce it to a linear combination of the
simplest possible diagrams, chains, which are symmetric under reﬂec tion. Reﬂecting
a chain preserves the chord diagram, whence the value of the sl(2) weight system.
Theorem 4 is proved. □
