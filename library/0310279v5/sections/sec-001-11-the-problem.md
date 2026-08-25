---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS"
section_id: sec-001-11-the-problem
section_title: "The problem"
section_number: 1.1
pages: 1-5
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
doc_brief: "Stabilization in the braid groups I: MTWS — 30 sections: Introduction; The problem; Block-strand diagrams and template"
---
LetX be an oriented link type in the oriented 3–sphere S3 or R3 = S3\{∞}. A
representative X∈X is said to be a closed braid if there is an unknotted curve
A⊂ (S3\ X) (the axis) and a choice of ﬁbration H of the open solid torus S3\ A
by meridian discs {Hθ; θ∈ [0, 2π]}, such that whenever X meets a ﬁber Hθ the
intersection is transverse. We call the pair ( A, H) a braid structure The fact that X
is a closed braid with respect to H implies that the number of points in X∩ Hθ is
independent ofθ. We call this number the braid index of X, and denote it by the symbol
b(X). The braid index ofX , denoted b(X ), is the minimum value of b(X) over all
closed braid representatives X∈X .
Closed braid representations ofX are not unique, and Markov’s well-known theorem
(see the book by Birman [3], and the papers by Birman and Menasco [12], Lambropoulou
Published: 27 April 2006 DOI: 10.2140/gt.2006.10.413
414 Joan S Birman and William W Menasco
and Rourke [22], Markov [23], Morton [28] and Traczyk [31]) asserts that any two are
related by a ﬁnite sequence of elementary moves. One of the moves is braid isotopy
by which we mean an isotopy of the pair ( X, R3\ A) which preserves the condition
that X is transverse to the ﬁbers of H. The other two moves are mutually inverse, and
are illustrated in Figure 1. Both take closed braids to closed braids. We call them
destabilization and stabilization where the former decreases braid index by one and the
latter increases it by one. The ‘weight’w denotes w parallel strands, relative to the given
projection. The braid inside the box which is labeled P is an arbitrary (w + 1)–braid.
Later, it will be necessary to distinguish between positive and negative destabilizations,
so we illustrate both now.
P
+
A
w
1
destabilize
stabilize
P
A
w
1
P
A
w
1
−
destabilize
stabilize
P
A
w
1
Figure 1: The two destabilization moves
Theorem 1 (Markov’s Theorem (MT) [23]) Let X+, X− be closed braid representa-
tives of the same oriented link typeX in oriented 3–space, with the same braid axis A.
Then there exists a sequence
(1–1) X+ = X1→ X2→···→ Xr = X−
of closed braid representatives ofX such that, up to braid isotopy, eachXi+1 is obtained
from Xi by a single stabilization or destabilization.
It is easy to ﬁnd examples of subsequences Xj→···→ Xj+k of (1–1) in Theorem 1
such that b(Xj) = b(Xj+k), but Xj and Xj+k are not braid isotopic. Call such a
sequence a Markov tower . The stabilization and destabilization moves are very
simple, but sequences of stabilizations, braid isotopies and destabilizations can have
unexpected consequences. In the braid groups these moves are ‘site dependent’, unlike
the stabilization–destabilization move in the Reidemeister–Singer Theorem. (For an
example the reader should refer ahead to the speciﬁed site of the stabilization in the
sequence in Figure 5.) Until now these moves have been predominately used to develop
link invariants, but the Markov towers themselves have been ‘black boxes’. One of
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 415
the main motivating ideas of this work is to open up the black box and codify Markov
towers.
Markov’s Theorem is typical of an entire class of theorems in topology where some
form of stabilization and destabilization play a central role. Other examples are:
(1) The Reidemeister–Singer Theorem [30] relates any two Heegaard diagrams of
the same 3–manifold, by a ﬁnite sequence of very simple elementary changes
on Heegaard diagrams. The stabilization–destabilization move adds or deletes a
pair of simple closed curves a, b in the deﬁning Heegaard diagram, where a∩ b
= 1 point and neither a nor b intersects any other curve ai, bj in the Heegaard
diagram.
(2) The Kirby Calculus [21] gives a ﬁnite number of moves which, when applied
repeatedly, sufﬁce to change any surgery presentation of a given 3–manifold into
any other, at the same time keeping control of the topological type of a 4–manifold
which the given 3–manifold bounds. The stabilization–destabilization move is
the addition-deletion of an unknotted component with framing±1 to the deﬁning
framed link.
(3) Reidemeister’s Theorem (see Burde–Zieschang [15]) relates any two diagrams
of the same knot or link, by a ﬁnite sequence of elementary moves which are
known as RI, RII, RIII. The stabilization–destabilization move is RI. It is easy to
see that Markov’s Theorem implies Reidemeister’s Theorem.
These theorems are all like Markov’s Theorem in the sense that while the stabilization
and destabilization moves are very simple, a sequence of these moves, combined with the
appropriate isotopy, can have very non-trivial consequences. Here are other examples
in which the stabilization move is not used, at the expense of restricting attention to a
special example:
(4) W Haken proved that any Heegaard diagram for a non-prime 3–manifold is
equivalent to a Heegaard diagram which is the union of two separate Heegaard
diagrams, one for each summand, supported on disjoint subsets of the given
Heegaard surface. See Scharlemann–Thompson [29] for a very pleasant proof.
(5) Waldhausen [32] proved that any two Heegaard diagrams of arbitrary but ﬁxed
genus g for the 3–sphere S3 are equivalent.
In the course of an effort which we began in 1990 to discover the theorem which will be
the main result of this paper (see Theorem 2 below) the authors made several related
contributions to the theory of closed braid representatives of knots and links:
(4′) A split (resp. composite) closed n–braid is an n–braid which factorizes as a
product XY where the sub-braid X involves only strands 1,..., k and the sub-
braid Y involves only strands k + 1,..., n (resp. k,..., n). In the manuscript
Geometry &Topology 10 (2006)
416 Joan S Birman and William W Menasco
[7] the authors proved that if X is a closed n–braid representative of a split or
composite link, then up to (braid-index preserving) isotopy and exchange moves,
as in Figure 2, X may be assumed to be a split or composite closed braid.
w
1
P Q
w
1
P Q
Figure 2: The exchange move
(5′) In the manuscript [9] the authors proved that if X is a closed braid representative
of theµ–component unlinkX , then a ﬁnite sequence of braid isotopies, exchange
moves and destabilization can be found which change X to the closure of the
identity braid in the braid group Bµ.
(6) In the manuscript [ 11] the authors discovered that there is another move, the
3–braid ﬂype (see Figure 3) with the property that if X is a closed 3–braid
representative of a knot or link typeX which cannot be represented by a 1–braid
or 2–braid, then either X has a unique conjugacy class or X has exactly two
conjugacy classes, and these two classes are related by a 3–braid ﬂype. They
also showed that the exchange move can be replaced by braid isotopy for prime
links of braid index 3.
P
Q
R
A +
P
Q
R
A+
P
Q
R
A
−
P
Q
R
A−
positive
ﬂype
negative
ﬂype
Figure 3: The two ﬂype moves
The authors also established two fundamental facts which gave strong evidence that a
more general result might be true:
(7) In [8] the authors introduced a complexity function on closed braid representatives
ofX and proved that, up to exchange moves, there are at most ﬁnitely many
conjugacy classes of representatives of minimum complexity.
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 417
(8) In [10] the authors proved that if a link typeX has inﬁnitely many conjugacy
classes of closed braid representatives of the same braid index, then, up to
exchange moves, they fall into ﬁnitely many equivalence classes.
The goal of this paper is to generalize examples (4′), (5′) and (6), taking into account
(7) and (8), to arbitrary closed braid representatives of arbitrary oriented knots and links.
We call our main theoremMarkov’s Theorem Without Stabilization(MTWS), because it
is a direct modiﬁcation of Markov’s Theorem, but with his stabilization move replaced
by other moves which allow one to jump from one isotopy class in the complement of
A to another, while keeping the braid index constant or decreasing it.
