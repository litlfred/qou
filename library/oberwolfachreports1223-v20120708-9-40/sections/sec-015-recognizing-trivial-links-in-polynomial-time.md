---
doc_id: oberwolfachreports1223-v20120708-9-40
doc_title: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by"
section_id: sec-015-recognizing-trivial-links-in-polynomial-time
section_title: "Recognizing trivial links in polynomial time"
section_number: null
pages: 31-33
source_pdf: OberwolfachReports1223_v20120708_9_40.pdf
source_sha256: 94f82cfc185955ba
toc_source: inferred
doc_brief: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by — This meeting concentrated on topological invariants in low di"
---
Chad Musick
We let a link be a family of circles disjointly embedded in R3∪{∞}. Trivial links
are those links embedded such that the 3-dimensional space may be continuously
deformed so that the resultant link is embedded as a subset of R2. We give a
method to decide, for any link L, whether or not L is trivial. This method is
polynomial in complexity.
We proceed by developing two new measures of complexity, the crumple and
the sentence length. To deﬁne these, we restrict our attention to links embedded
in a restricted fashion as described below.
Let L be a link. If we may ﬁnd a ﬁnite set S of concentric spheres of positive
integer radius such that the closure of the portion of L lying in (R3 −S) ∪{∞} is
a set of disjoint line segments each lying along a line through the common center
of the members of S, we say that the link is a tar link.
Given a tar link L with a set S of spheres as described above, we let the crumple
of L be the sum of the lengths of the portions of L lying in the complement of S.
By choosing a tar link in which all of the members of the intersection of L and
the complement of S lie in the plane R2, we may write a descriptive sentence of
the embedding of L. The length of this sentence will depend upon the number of
line segments in the complement of S and on the number of mutual intersections
between S, L, and R2.
32
Oberwolfach Report 28/2012
We give a method to construct a sentence from any link diagram. The initial
length of this sentence will be a linear multiple of the number of crossings in the
diagram. By its construction, the crumple of the resulting link will be at worst
quadratic on the number of crossings. As well, the number of crossings in any
diagram of a sentence will be at most quadratic on the length of the sentence.
This gives us an upper bound on the complexity of the diagrams as a function of
the length of the descriptive sentence.
As a Lemma, we show that given a trivial link and a descriptive sentence for
a tar link equivalent to this link – and so also trivial – there is a simple isotopy
occurring entirely within one of the spheres associated to the link such that the
resultant link has a strictly smaller crumple. This gives an immediate algorithm
to determine whether or not a link is trivial.
Knowing this Lemma, we then prove that there is a strictly monotonic sequence
on a 5-tuple describing a link.
Each of the measures of this tuple is at worst
quadratic on the number of crossings of the diagram used to generate the initial
sentence, and so on the number of crossings of the original diagram. We show that
there are a polynomial number of attempts needed before a move may be found
that results in a strictly lower tuple from a trivial link. Taken together, these
moves constitute an algorithm to decide whether or not a link is trivial. Those
links that are trivial will produce a sequence of diagrams proceeding stepwise to a
trivial diagram. Those links that are not trivial will terminate when none of the
polynomial number of possible moves produces an improvement in the complexity
tuple.
We demonstrate the use of the algorithm on two trivial knot diagrams and give
a complete description of the construction of the sentence and of the algorithm.
References
[1] J. Birman and W. Menasco, Special positions for essential tori in link complements, Topol-
ogy 33 (1994), no. 3, 525–556.
[2] Peter R. Cromwell, Embedding knots and links in an open book I: Basic properties, Topology
Appl. 64 (1995), no. 1, 37–58.
[3] Ivan Dynnikov, Arc-presentation of links. monotonic simpliﬁcation, Fund. Math. 190
(2006), 29–76.
[4] Louis H. Kauﬀman and Soﬁa Lambropoulou, Unknots and molecular biology, Milan J. Math.
74 (2006), 227–263.
[5] Kunio Murasugi, Knot theory & its applications, Birkh¨auser, 1996, English edition.
[6] Mitsuyuki Ochiai, Non-trivial projections of the trivial knot, Ast`erisque 192 (1987), 7–10.
[7] Herbert Seifert, ¨Uber das Geschlecht von Knoten, Math. Ann. 110 (1935), no. 1, 571–592.
How to Fold a Manifold
J. Scott Carter
A classical result of J.W. Alexander states that any k + 2 dimensional oriented
compact connected manifold can be obtained as a simple branched cover of the (k+
2)-sphere with branch set an embedded k-dimensional manifold. Other important
results include those of Hilden and Montesinos which indicate that a 3-dimensional
Invariants in Low-Dimensional Topology and Knot Theory
33
manifold is a simple 3-fold branched cover of the 3-sphere, and that of Iori and
Piergallini that states that a 4-dimensional manifold can be obtained as a simple
5-fold branched cover of the 4-sphere branched along am embedded surface in the
4-sphere.
Our result (Carter and S. Kamada) is that we can embedded 2-fold simple
branched covers of the 2,3, and 4-sphere branched along a linked oriented manifold
in the sphere times a 2-disk in such a way that the projection to the sphere is the
covering map. Similarly, we can immerse the 3-fold branched covers in the same
space. Covers with higher branching indices can often be embedded. In this way,
we are initiating a theory of braids for knotted 3-manifolds in 5-space and knotted
4-manifolds in 6-space.
