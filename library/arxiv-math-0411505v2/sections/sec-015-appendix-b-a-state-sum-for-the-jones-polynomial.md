---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUT A TIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-015-appendix-b-a-state-sum-for-the-jones-polynomial
section_title: "Appendix B. A state sum for the Jones polynomial"
section_number: null
pages: 16-19
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent p olynomials that encodes the Jones polynomial of a knot and its parallels."
---
In this section we review the proof of Theorem 5. The Jones polynom ial V of a link is determined by the
skein theory:
q2V
( )
− q−2V
( )
= (q− q−1)V
( )
together with the initial condition V (unknot)(q) = q + q−1. We will be using a normalized version of the
Jones polynomial deﬁned by
J(K)(t) = V (K)(t1/2)/V (unknot)(t1/2).
We review a state sum deﬁnition of the Jones polynomial V discussed by Turaev [Tu] (see also [J1]) and
further studied by Lin and Wang [L W]. We recall the details of Turaev’s general state sum construction,
adapted to our special case.
Deﬁnition B.1. Fix a planar projection K of a knot.
(a) Let PK denote the planar digraph obtained from K by turning each crossing into a vertex. We call the
edges of PK partarcs ofK.
(b) A state s ofK is the assignment of 0 or 1 to each partarc of K, such that at each crossing, the multiset
of labels of the incoming edges equals to the multiset of labels of outgo ing edges. In other words, at each
crossing (positive or negative) a state looks like one of the following p ictures,
where edges colored by 0 or 1 are depicted as dashed or solid respec tively.
(c) The local weight Π v(s) of a vertex v of PK of a state s is given by
c d
ba
−→ (R+)cd
ab
c d
ba
−→ (R−)cd
ab
16
where R+ and R− = (R+)−1 is the R-matrix of the quantum group Uq(sl2) given by:
(R+)0,0
0,0 = (R+)1,1
1,1 =−q (R+)1,0
0,1 = (R+)0,1
1,0 = 1 ( R+)0,1
0,1 = ¯q− q
(R−)0,0
0,0 = (R−)1,1
1,1 =−¯q (R−)1,0
0,1 = (R−)0,1
1,0 = 1 ( R−)1,0
1,0 = q− ¯q
where ¯q = q−1 and all other entries of the R matrix are zero.
(d) The weight Π( s) of a state s is deﬁned by
Π( s) =
∏
v
Π v(s).
Note that ( R−)0,1
0,1 = (R+)1,0
1,0 = 0.
(e) A state s is admissible iﬀ Π( s)⁄= 0.
There is an involution s→ sc of states of K, obtained by interchanging 0 by 1’s.
Lemma B.2. (a) There is a 1-1 correspondence
{ states of K}←→{ even subgraphs of PK}.
(b) There is a 1-1 correspondence
{ admissible states of K}←→{ collections of vertex-disjoint cycles of GK}.
Proof. A state s gives rise to an even subgraph of the PK (whose edges are the ones colored by 1 in s), also
denoted by s. Part (a) follows.
Since every vertex of PK has outdegree 2, it follows that the involution of states correspon ds to the
operation of taking the complement of an even subgraph in PK.
For part (b), observe that an admissible even subgraph s of PK gives rise to an even subgraph of the
arc-graph GK with each indegree at most one: this follows since as mentioned above , (R+)0,1
0,1 = (R−)1,0
1,0 = 0,
and so if we walk on s along the orientation of K, we never ’jump down’; hence whenever we get to an arc
ofK, we traverse it (along its orientation) until its end. Hence we can ge t to each arc at most once and s
corresponds to an even subgraph of GK where each indegree is at most one.
Conversely, an even subgraph of GK gives rise to a ﬂow on PK. This ﬂow will be an admissible even
subgraph of PK if each indegree is at most one. The following ﬁgure illustrates the exc luded possibilities,
where the value of the ﬂow is shown on the partarcs:
a i+1
a j
a i a i+1
a j
a i1
2 1
□
Deﬁnition B.3. An even subgraph G of GK is admissible if each indegree is at most one. In other words,
G is a vertex-disjoint collection of directed cycles. Let S(GK) denote the collection of admissible subgraphs
of the arc-graph GK.
Next we deﬁne rotation and excess numbers of states.
Deﬁnition B.4. (a) The rotation number rot(s) of a state s is the number of counterclockwise circles
colored by 1 minus the number of clockwise circles colored by 1, obtain ed from smoothening of s, i.e., by the
replacement:
at all crossings of s.
(b) The excess number exc(s) of a state s is the sum of the signs of the crossings where all four edges are
colored by 1 in s.
17
With these preliminaries, the Jones polynomial is given by the state su m
V (K)(q) = (−q2)−ω(K) ∑
s admissible
qrot(sc)−rot(s)Π( s).
It was observed by Lin and Wang that the local weights of the R-matrix are proportional, up to a power
of q to the weights of a random walk on K. This is formalized in the following Lemma:
Lemma B.5. [L W, Lemma 2.3] For an admissible state s ofK, we have:
Π( s) = (−q)ω(K)q2exc(s)β(s)|t→q2 .
Proof. First note that β(s) is well deﬁned since by Lemma B.2 there is a 1-1 correspondence bet ween
admissible states of K and even admissible subgraphs of GK, and each even subgraph is naturally a ﬂow on
GK.
Consider the following table of a state around a positive crossing:
R −q ¯q− q 1 1 0 −q
−¯qR 1 1− ¯q2 −¯q −¯q 0 1
β 1 1− ¯q2 ¯q2 1 0 ¯q2
qexc 1 1 1 1 1 q2
qerr 1 1 −q −¯q 1 1
and around a negative crossing:
R −¯q 0 1 1 q− ¯q −¯q
−qR 1 0 −q −q 1− q2 1
β 1 0 1 q2 1− q2 q2
qexc 1 1 1 1 1 ¯q2
qerr 1 1 −q −¯q 1 1
Here, β(s) of a state s equals to the weight of the 1-part of s.
Inspection of these tables reveals that given a state s and a crossing of sign ǫ = ±1, we have R =
(−q)ǫq2exc+errβ. Taking a product over all vertices, we obtain that
Π( s) = (−q)ω(K)q2exc(s)+err(s)β(s)|t→q2 .
It remains to show that qerr(s) = 1. err( s) is computed from a smoothening smooth( s) of s, which consists of
a number of transversely intersecting circles colored by 0 or 1. Any two transverse planar circles intersect on
an even number of points, which can be paired up by paths on each cir cle. A case by case argument shows
that err( s) = 1. Some cases of the local contributions to ′err′ and their pairwise canceling is shown by:
−q
−q
−q
−q
−q
−q
−q
−q
This concludes the proof of the lemma. □
The involution on the set of states of K has further consequences discovered by Lin and Wang. Fix a
partarc of K that borders the unbounded region of the planar projection and m ark it by ⋆. Let F ′(K− ⋆)
denote the set of all admissible states of K where ⋆ is colored by 0.
18
We will show ﬁrst that
(8) J(K)(t) = tδ(K) ∑
s∈F ′(K−⋆)
tδ(s)β(s).
We recall that δ(K) = 1 /2(−ω(K) + rot(K)) and δ(s) = exc( s)− rot(s).
Consider a long knot K long depicted as a box and the two ways of closing it to obtain a knot K as follows:
Let ai denote V (K long) with boundary conditions i, for i = 0, 1. Then, the two ways of closing K long give:
V (K)(q) = qa0 + q−1a1 = q−1a0 + qa1
from which follows that a0 = a1 and thus V (K)(q) = ( q + q−1)a0 = V (unknot)a0. Thus, (8) follows.
Next we introduce the rotation and excess numbers of a collection o f vertex disjoint cycles of GK, using
Lemma B.2.
