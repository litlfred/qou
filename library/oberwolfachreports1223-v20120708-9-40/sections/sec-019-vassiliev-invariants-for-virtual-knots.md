---
doc_id: oberwolfachreports1223-v20120708-9-40
doc_title: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by"
section_id: sec-019-vassiliev-invariants-for-virtual-knots
section_title: "Vassiliev invariants for virtual knots"
section_number: null
pages: 39-42
source_pdf: OberwolfachReports1223_v20120708_9_40.pdf
source_sha256: 94f82cfc185955ba
toc_source: inferred
doc_brief: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by — This meeting concentrated on topological invariants in low di"
---
Heather A. Dye
I construct degree one, ﬁnite type invariants for virtual knots. This method
focuses on the idea of partitioning the crossings in a virtual knot diagram into
sets. The sets of crossings are not invariant under the Reidemeister moves, but
the sum of the signs of the crossings in the set (the signed cardinality of the set)
is an invariant of the knot.
Let K+ denote a knot diagram with a positive crossing c. Correspondingly,
let K−denote a knot diagram identical to K+ except at a crossing c – where
the over passing edge is switched to form a negative crossing. Let K• denote a
40
Oberwolfach Report 28/2012
knot diagram identical to K+ except that the crossing c is singular. A ﬁnite type
invariant V [4] [2] has the property that
V(K•) = V(K+) −V(K−).
More generally, let X be a tuple of k singular crossings in the knot diagram K.
Let σ(X) denote a resolution of each crossing as a positively or negatively signed
crossing and let |σ| denote the sum of negative crossings in σ(X). Summing over
all possible resolutions:
V(KX) =
!
σ
(−1)|σ|V(Kσ(X)).
The invariant V is said to have ﬁnite type ≤n if V(KX) = 0 for all tuples of length
n + 1 or greater.
Henrich introduced a degree one, ﬁnite type invariant called the gluing invariant
in [5]. Let K be a virtual knot diagram. Let Kc denote the virtual knot diagram
obtained from K by gluing the crossing c (making the crossing a singularity) and
let KcO denote the diagram obtained by attaching a small unknot near c with
a singularity. Let F(K) denote the ﬂat projection of the knot K. The gluing
invariant is a formal sum of equivalence classes of ﬂat virtual knots with one
singular crossing.
G(K) =
!
c∈K
[F(Kc) −F(KcO)]
(Note that if the crossing c is involved in a Reidemeister I move, then [F(Kc) −
F(KcO)] is the empty diagram.) By extending the ﬂat classical and virtual Rei-
demeister moves to include one singular crossing, the formal sum G(K) becomes
an invariant of virtual knots and a universal, degree one, ﬁnite type invariant.
We compute the weight of a chord in a Gauss diagram. The weights partition
the chords into sets which can be used to deﬁne ﬁnite type invariants of the Gauss
diagrams. A Gauss diagram G is a clockwise oriented circle with a collection, C,
of oriented, signed chords. Equivalence classes of Gauss diagrams are determined
by three types of moves: 1) the introduction or deletion of a single isolated chord,
2) the introduction of two adjacent (feet and head), oppositely signed chords, and
3) the (2,1) and (3,0) triangle moves with appropriately selected signs. (Although
my orientation conventions are slightly diﬀerent, the set of chord diagram moves
is introduced in [8]. In this paper, Turaev determines the minimum set of moves
required to generate the equivalence classes of Gauss diagrams.) We construct a
map P : C →Z. Let c denote a chord and let Nc be the set of chords that intersect
c. The oriented intersection number of the chord c with the chord x is denoted
intc(x). Then
p(c) =
!
x∈Nc
intc(x)sgn(x).
The value of p(c) is the weight of the chord. For each integer i, we deﬁne Ai(G) =
{c | p(c) = i}, the set of chords with weight i. For a positive integer, we deﬁne
Vj(G) = {c | |p(c)| = j}, the set of chords with weight j or −j.
The signed
Invariants in Low-Dimensional Topology and Knot Theory
41
cardinality of these sets are integers that are denoted as |Ai(G)| and as |Vj(G)|
respectively.
|Ai(G)| =
!
c∈Ai(G)
sgn(c) and |Vj(G)| =
!
c∈Vj(G)
sgn(c).
We prove that for any non-zero integer i and any positive integer j, |Ai(G)| and
|Vj(G)| are invariant under the Gauss diagram moves. The proof can be brieﬂy
sketched as follows. Chords involved in a single chord move have weight zero.
Chords involved in a two chord move have the same weight, but have opposite
signs. Their net contribution to the signed cardinality of a set is zero. The weight
of chords is not changed by the triangle moves.
Virtual knots are equivalence classes of virtual knot diagrams that are in one
to one correspondence with equivalence classes of Gauss diagrams [6]. Let K be a
virtual knot diagram and let GK be the corresponding Gauss diagram. We deﬁne
Vj(K) (Ai(K)) to be the set of crossings that correspond to chords in Vj(GK) that
have parity j or −j (respectively i). We deﬁne the gluing invariant Gj(K) to be
a formal sum of ﬂat virtual knot diagrams with one singular crossing. However,
instead of gluing all crossings, we restrict our attention to crossings with particular
weights.
Gj(K) =
!
c∈Vj(K)
sgn(c)[F(Kc) −F(KcO)].
This formal sum of ﬂat diagrams with one singular crossing Gj(K) (modulo the
slightly expanded Reidmeister move set) is a degree one Vassiliev invariant.
We can obtain a numerical invariant equivalent to |Vj(K)| by mapping the
formal sum to the integers and each non-empty diagram class, [F(Kc)−F(KcO)],
is mapped to 1. (The value |Ai(GK)| is an invariant of virtual knots, but it is not
a ﬁnite type invariant.) We remark that
G(K) =
∞
!
i=1
Gi(K).
Taking products of the Gi(K) produces ﬁnite type invariants of higher degree.
(The weights can also be extracted from the polynomial invariant introduced by
Henrich in [5].)
Finite type invariants can be obtained from the Jones polynomial (FK(A)) of
the virtual knot K [6]. We expand FK(ex) as a Taylor series centered at 0. The
coeﬃcient of xk is a ﬁnite type invariant of degree k.
We illustrate this with
the following calculation. Let K+ (K−) denote a knot diagram with a positive
(respectively negative) crossing. Let KV and KH denote a knot diagram with a
vertical and horizontal smoothing respectively. Now ⟨K+⟩= A⟨KH⟩+ A−1⟨KV ⟩.
After normalization:
FK+(A) = −A−2FKV −A−4FKH,
FK−(A) = −A2FKV −A4FKH.
42
Oberwolfach Report 28/2012
Hence
FK•(A) = (−A−2 + A2)(FKV −(−A2 + A−2)FKH).
We see that the expansion of FK••(ex) has the form x2g(x) and and the coeﬃcient
of x is zero. Thus the coeﬃcient of xk is a Vassilliev invariant of degree k [6].
The normalized arrow polynomial, WK(A, Ki), [3] is an enhanced version of the
Jones polynomial that tracks the planarity of a knot diagram using the variables
Ki. The normalized arrow polynomial WK• factors in a similar fashion to FK(A)
and the planarity variables Ki are invariant under Reidemeister moves. As a result,
if we form the Taylor series of WK(ex, Ki) at centered at zero, we can obtain
Vassiliev invariants of degree 1 and higher.
The coeﬃcients of the monomials
with the form xiKj in the arrow polynomial WK(ex) expanded as a Taylor series
at 0 are Vassiliev invariants of degree i. Computations suggest that there is a
relationship between the coeﬃcients of WK(A, Ki) and |Vi(K)|.
References
[1] Dror Bar-Natan, On the Vassiliev knot invariants, Topology 34 (1995), no. 2, 423–472.
[2] S. Chmutov, S. Duzhin, J. Mostovoy Introduction to Vassiliev Invariants, Cambridge Uni-
versity Press, 2012.
[3] H. A. Dye, Louis H. Kauﬀman, Virtual crossing number and the arrow polynomial, J. Knot
Theory Ramiﬁcations 18 (2009), no. 10, 1335–1357.
[4] Mikhail Goussarov, Michael Polyak, Oleg Viro, Finite-type invariants of classical and virtual
knots, Topology 39 (2000), no. 5, 1045–1068.
[5] Allison Henrich, A sequence of degree one Vassiliev invariants for virtual knots, J. Knot
Theory Ramiﬁcations 19 (2010), no. 4, 461–487.
[6] Louis H. Kauﬀman, Virtual knot theory, European J. Combin. 20 (1999), no. 7, 663–690.
[7] V. O. Manturov, Parity in knot theory (Russian), Mat. Sb. 201 (2010), no. 5, 65–110;
translation in Sb. Math. 201 (2010), no. 5-6, 693–733 (Reviewer: Jonathan A. Hillman),
57M25.
[8] Vladimir Turaev, Virtual strings, Ann. Inst. Fourier (Grenoble) 54 (2004), no. 7, 2455–2525.
