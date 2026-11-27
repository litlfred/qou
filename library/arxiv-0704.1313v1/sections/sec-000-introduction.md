---
doc_id: arxiv-0704.1313v1
doc_title: "Mutant knots and intersection graphs"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 0704.1313v1.pdf
source_sha256: a75bb39c60ec9b15
toc_source: outline
doc_brief: "Mutant knots and intersection graphs — We prove that if a ﬁnite order knot invariant does not disting uish mutant knots, then the corresponding weight system depends on the interse ction graph of a"
---
Below, we use standard notions of the theory of ﬁnite order, or Va ssiliev, invariants
of knots in 3-space; their deﬁnitions can be found, for example, in [ 6] or [14]. All
knots are assumed to be oriented.
Two knots are said to be mutant if they diﬀer by a rotation/reﬂection of a tangle
with four endpoints; if necessary, the orientation inside the tangle may be replaced
by the opposite one. Here is a famous example of mutant knots, the Conway (11n34)
knot C of genus 3, and Kinoshita–Terasaka (11 n42) knot KT of genus 2 (see [1]).
C = KT =
Note that the change of the orientation of a knot can be achieved b y a mutation in
the complement to a trivial tangle.
Most known knot invariants cannot distinguish mutant knots. Neith er the (col-
ored) Jones polynomial, nor the HOMFLY polynomial, nor the Kauﬀman two variable
polynomial distinguish mutants. All Vassiliev invariants up to order 10 do not dis-
tinguish mutants as well [17] (up to order 8 this fact was established by a direct
computation [5, 6]). However, there is a Vassiliev invariant of order 1 1 distinguishing
C and KT [16, 17]. It comes from the colored HOMFLY polynomial.
∗ The Ohio State University, Mansﬁeld.
†Institute for System Research RAS and the Poncelet Laboratory , Independent University of
Moscow, partly supported by the grant ACI-NIM-2004-243 (Noe uds et tresses), RFBR 05-01-01012-
a, NWO-RFBR 047.011.2004.026 (RFBR 05-02-89000-NWOa), GIMP A NR-05-BLAN-0029-01.
1
The main combinatorial objects of the Vassiliev theory of knot invar iants are
chord diagrams. To a chord diagram, its intersection graph (also called circle graph)
is associated. The vertices of the graph correspond to chords of the diagram, and two
vertices are connected by an edge if and only if the corresponding c hords intersect.
The value of a Vassiliev invariant of order n on a singular knot with n double
points depends only on the chord diagram of the singular knot. Henc e any such
invariant determines a function, a weight system , on chord diagrams with n chords.
Conversely, any weight system induces, in composition with the Kont sevich integral,
which is the universal ﬁnite order invariant, a ﬁnite order invariant o f knots. Such
knot invariants are called canonical. Canonical invariants span the whole space of
Vassiliev invariants.
Direct calculations for small n show that the values of these functions are uniquely
determined by the intersection graphs of the chord diagrams. This fact motivated
the intersection graph conjecture in [5] (see also [6]) which states that any weight
system depends on the intersection graph only. This conjecture h appened to be false,
because of the existence of a ﬁnite order invariant that distinguish es two mutant knots
mentioned above and the following fact.
The knot invariant induced by a weight system whose values de pend only on the
intersection graph of the chord diagrams cannot distinguis h mutants.
A justiﬁcation of this statement, due to T. Le (unpublished), looks like follows
(see details in [6]). If we have a knot (in general position) with a disting uished two-
string tangle, then all the terms in the Kontsevich integral of the k not having chords
connecting the tangle with its exterior vanish.
Our goal is to prove the converse statement thus establishing an e quivalence be-
tween ﬁnite order knot invariants nondistinguishing mutants and we ight systems de-
pending on the intersection graphs of chord diagrams only.
Theorem 1 If a ﬁnite order knot invariant does not distinguish mutants , then the
corresponding weight system depends only on the intersecti on graphs of chord dia-
grams.
Together, the two statements can be combined as follows.
A canonical knot invariant does not distinguish mutants if a nd only if its weight
system depends on the intersection graphs of chord diagrams only.
Recently, B. Mellor [15] extended the concept of intersection grap h to string links.
We do not know whether our Theorem 1 admits an appropriate gener alization.
Section 2 is devoted to the proof of Theorem 1. In Sec. 3, we discus s relationship
between intersection graphs and the weight systems associated t o the Lie algebra sl(2)
and the Lie algebra gl(1|1).
The paper was written during the second author’s visit to the Mathe matical De-
partment of the Ohio State University. He expresses his gratitude to this institution
for warm hospitality and excellent working conditions. The authors a re grateful to
S. Duzhin, K. J. Supowit, and A. Vaintrob for useful discussions.
2
