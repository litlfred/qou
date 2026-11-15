---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-017-appendix-b-a-state-sum-for-the-jones-polynomial
section_title: "Appendix B. A state sum for the Jones polynomial"
section_number: null
pages: 16-19
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
toc_source: outline
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent polynomials that encodes the Jones polynomial of a knot and its parallels."
---
In this section we review the proof of Theorem] The Jones polynomial V of a link is determined by the

skein theory:
wOeerO)ew-or 9)

together with the initial condition V(unknot)(g) = q + q~!. We will be using a normalized version of the
Jones polynomial defined by
J(K)(t) = V(K)(#!/?)/V (unknot)(#"/?).

We review a state sum definition of the Jones polynomial V discussed by Turaev (see also [Ji]) and
further studied by Lin and Wang [LW]. We recall the details of Turaev’s general state sum construction,
adapted to our special case.

Definition B.1. Fix a planar projection K of a knot.

(a) Let Px denote the planar digraph obtained from K by turning each crossing into a vertex. We call the
edges of Px partarcs of K.

(b) A state s of K is the assignment of 0 or 1 to each partarc of K, such that at each crossing, the multiset
of labels of the incoming edges equals to the multiset of labels of outgoing edges. In other words, at each
crossing (positive or negative) a state looks like one of the following pictures,

a A a A vv. ft

where edges colored by 0 or 1 are depicted as dashed or solid respectively.
(c) The local weight I,(s) of a vertex v of Px of a state s is given by

c d c d
Ni (Re x — (Rd
a*rNnb a b

6

16
where R+ and R~ = (R+)~1 is the R-matrix of the quantum group U,(sl2) given by:
=-4 (R*)
=-4 (R’)

where g = q~! and all other entries of the R matrix are zero.

(d) The weight II(s) of a state s is defined by
II(s) = Il II,(s).
v

Note that (R~)q°; = (R*)19 =0.
(e) A state s is admissible iff II(s) 4 0.

There is an involution s > s® of states of K, obtained by interchanging 0 by 1’s.
\ ging \
Lemma B.2. (a) There is a 1-1 correspondence
{states of K}<—> {even subgraphs of Px}.
(b) There is a 1-1 correspondence
admissible states of K}<—> {collections of vertex-disjoint cycles of Gx}.
) A

Proof. A state s gives rise to an even subgraph of the Px (whose edges are the ones colored by 1 in s), also
denoted by s. Part (a) follows.

Since every vertex of Px has outdegree 2, it follows that the involution of states corresponds to the
operation of taking the complement of an even subgraph in Px.

For part (b), observe that an admissible even subgraph s of Px gives rise to an even subgraph of the
arc-graph Gx with each indegree at most one: this follows since as mentioned above, (R+)0"; = (R-Yro =0,
and so if we walk on s along the orientation of K, we never ’jump down’; hence whenever we get to an arc
of K, we traverse it (along its orientation) until its end. Hence we can get to each arc at most once and s
corresponds to an even subgraph of Gc where each indegree is at most one.

Conversely, an even subgraph of Gx gives rise to a flow on Px. This flow will be an admissible even
subgraph of Pic if each indegree is at most one. The following figure illustrates the excluded possibilities,
where the value of the flow is shown on the partarcs:

Oo

Definition B.3. An even subgraph G of Gx is admissible if each indegree is at most one. In other words,
G is a vertex-disjoint collection of directed cycles. Let S(Gx_) denote the collection of admissible subgraphs
of the arc-graph Gx.

Next we define rotation and excess numbers of states.

Definition B.4. (a) The rotation number rot(s) of a state s is the number of counterclockwise circles
colored by 1 minus the number of clockwise circles colored by 1, obtained from smoothening of s, i.e., by the

replacement:
x ad ; \ Y
XA IO Mal =)
at all crossings of s.

(b) The excess number exc(s) of a state s is the sum of the signs of the crossings where all four edges are
colored by 1 in s.

17
With these preliminaries, the Jones polynomial is given by the state sum
V (K)(q) = (−q2)−ω(K)
X
s admissible
qrot(sc)−rot(s)Π(s).
It was observed by Lin and Wang that the local weights of the R-matrix are proportional, up to a power
of q to the weights of a random walk on K. This is formalized in the following Lemma:
Lemma B.5. [LW, Lemma 2.3] For an admissible state s of K, we have:
Π(s) = (−q)ω(K)q2exc(s)β(s)|t→q2.
Proof. First note that β(s) is well deﬁned since by Lemma B.2 there is a 1-1 correspondence between
admissible states of K and even admissible subgraphs of GK, and each even subgraph is naturally a ﬂow on
GK.
Consider the following table of a state around a positive crossing:
R
−q
¯q −q
1
1
0
−q
−¯qR
1
1 −¯q2
−¯q
−¯q
0
1
β
1
1 −¯q2
¯q2
1
0
¯q2
qexc
1
1
1
1
1
q2
qerr
1
1
−q
−¯q
1
1
and around a negative crossing:
R
−¯q
0
1
1
q −¯q
−¯q
−qR
1
0
−q
−q
1 −q2
1
β
1
0
1
q2
1 −q2
q2
qexc
1
1
1
1
1
¯q2
qerr
1
1
−q
−¯q
1
1
Here, β(s) of a state s equals to the weight of the 1-part of s.
Inspection of these tables reveals that given a state s and a crossing of sign ǫ = ±1, we have R =
(−q)ǫq2exc+errβ. Taking a product over all vertices, we obtain that
Π(s) = (−q)ω(K)q2exc(s)+err(s)β(s)|t→q2.
It remains to show that qerr(s) = 1. err(s) is computed from a smoothening smooth(s) of s, which consists of
a number of transversely intersecting circles colored by 0 or 1. Any two transverse planar circles intersect on
an even number of points, which can be paired up by paths on each circle. A case by case argument shows
that err(s) = 1. Some cases of the local contributions to ′err′ and their pairwise canceling is shown by:
−q
−q
−q
−q
−q
−q
−q
−q
This concludes the proof of the lemma.
□
The involution on the set of states of K has further consequences discovered by Lin and Wang. Fix a
partarc of K that borders the unbounded region of the planar projection and mark it by ⋆. Let F′(K −⋆)
denote the set of all admissible states of K where ⋆is colored by 0.
18
We will show first that
(8) JK) = SX) G(s).
seF/(K—x)

We recall that 6(K) = 1/2(—w(K) + rot(K.)) and 6(s) = exc(s) — rot(s).
Consider a long knot 1°" depicted as a box and the two ways of closing it to obtain a knot K as follows:

Let a; denote V(K'?8) with boundary conditions i, for i = 0,1. Then, the two ways of closing K!°"8 give:

V(K)(q) = qa0 + q7'a1 = q" ‘a0 + gar

from which follows that a9 = a; and thus V(K)(q) = (¢+q7!)ao = V(unknot)ag. Thus, §) follows.
Next we introduce the rotation and excess numbers of a collection of vertex disjoint cycles of Gx, using

Lemma
