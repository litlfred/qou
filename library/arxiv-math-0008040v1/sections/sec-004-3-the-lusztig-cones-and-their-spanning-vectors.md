---
doc_id: arxiv-math-0008040v1
doc_title: "Rectangle diagrams for the Lusztig cones of quantized envel oping algebras of type A Robert Marsh"
section_id: sec-004-3-the-lusztig-cones-and-their-spanning-vectors
section_title: "The Lusztig cones and their spanning vectors"
section_number: 3
pages: 5-8
source_pdf: 0008040v1.pdf
source_sha256: a72319b55dbaf20b
doc_brief: "Rectangle diagrams for the Lusztig cones of quantized envel oping algebras of type A Robert Marsh — Let U be the quantum group associated to a Lie algebra g of type An."
---
Lusztig [12] introduced certain regions which, in low rank, give rise to canonical basis elements of
a particularly simple form. The Lusztig cone , Ci, corresponding to i ∈χ n, is deﬁned to be the set
of points a ∈ Nk satisfying the following inequalities:
(*) For every pair s,s ′ ∈ [1,k ] with s<s ′, is =is′ =i and ip ⁄=i whenevers<p<s ′, we have
(
∑
p
ap) −as −as′ ≥ 0,
where the sum is over all p with s < p < s′ such that ip is joined to i in the Dynkin diagram (we
call such a pair s,s ′ a minimal pair).
It was shown by Lusztig [12] that if a ∈ Ci then the monomial F (a1)
i1 F (a2)
i2 · · ·F (ak)
ik lies in the
canonical basis B, provided n = 1, 2, 3. The author [14] showed that this remains true if n = 4.
Counter-examples of Xi [21] and Reineke [18] show that this i s not true in general.
Remark: It can be shown that, for any i ∈χ n, we have Ci ⊆Yi, i.e., the Lusztig cone is contained
in the Kashiwara cone. The methods of this paper could be used to do this in type An, but the
author has recently learnt that A. Premat [16] has a more succ inct proof for all simply-laced cases.
The reduced expression i deﬁnes an ordering on the set Φ + of positive roots of the root system
associated to W . We write α j =si1si2 · · ·sij−1(α ij ) for j = 1, 2,... ,k . Then Φ + = {α 1,α 2,...α k}.
For a = (a1,a 2,... ,a k) ∈ Zk, write aα j =aj. If α =α ij :=α i +α i+1 + · · · +α j−1 with i<j , we
also write aij for aα ij .
We shall need the chamber diagram (chamber ansatz) for i deﬁned in [2, §§1.4, 2.3]. We take
n + 1 strings, numbered from top to bottom, and write i from left to right along the bottom of the
diagram. Above a letter ij in i, the ijth and (ij + 1)st strings from the top above ij cross. Thus,
for example, in the case n = 3 with i = (1, 3, 2, 1, 3, 2), the chamber diagram is shown in Figure 1.
We denote the chamber diagram of i by CD( i). A chamber will be deﬁned as a pair ( c, i), where
c is a bounded component of the complement of CD( i). Each chamber ( c, i) can be labelled with
5
the numbers of the strings passing below it, denoted l(c, i). Following [2], we call such a label a
chamber set. For example, the chamber sets corresponding to the 3 bounded chambers in Figure 1
are 134, 3, 13. Note that the set of chamber sets of i is independent of its commutation class (so we
can talk also of the chamber sets of such a commutation class) . Every subset of [1 ,n + 1] can arise
as a chamber set for some i, except for subsets of the form [1 ,j ] and [ j,n + 1] for 1 ≤j ≤ n + 1;
this is observed in the proof of [2, Theorem 2.7.1].
We now recall some of the results from [13] that we shall need. We have by [13, §4] that there is a
matrix Pi ∈GLk(Z) such that Ci = {a ∈ Zk : Pia ≥ 0}, where, for z ∈ Zk, z ≥ 0 means that each
entry in z is nonnegative. It follows that Ci is the set of nonnegative linear combinations of the
columns of Qi =P −1
i . These columns were described in [13], using the concept of a partial quiver .
A partial quiver P of type An is a quiver of type An which has some (or none) of its arrows replaced
by undirected edges, in such a way that the subgraph obtained by deleting undirected edges and
any vertex incident only with undirected edges is connected . We number the edges of a partial
quiver from 2 to n, starting at the right hand end. We write P as a sequence of n − 1 symbols, L,
R or −, where L denotes a leftward arrow, R a rightward arrow, and − an undirected edge. Thus
any partial quiver will be of form − − − ∗ ∗ ∗ − − − , where the ∗’s denoteL’s orR’s.
If P,P ′ are partial quivers we write P ′ ≥ P (or P ≤ P ′) if every edge which is directed in P is
directed in P ′ and is oriented in the same way, and say that P is a sub partial quiver of P ′. For
example, − − −LRLL− ≤ RLRLRLLL.
It is known that if i is compatible with a quiver Q (in the sense of [9, §4.7]) then the set of reduced
expressions for w0 compatible with Q is precisely the commutation class of χ n containing i. We
say that this commutation class is compatible with Q. Berenstein, Fomin and Zelevinsky (see [2,
§4.4]) describe a method for constructing i ∈χ n compatible with any given quiver Q, as follows.
Suppose Q is a quiver of type An. Let Λ ⊆ [2,n ] be the set of all edges of Q pointing to the
left. Berenstein, Fomin and Zelevinsky construct an arrang ement Arr(Λ). Consider a square in the
plane, with horizontal and vertical sides. Put n + 1 points onto the left-hand edge of the square,
equally spaced, numbered 1 to n + 1 from top to bottom, and do the same for the right-hand edge,
but number the points from bottom to top. Line h joins point h on the left with point h on the
right. For h = 1,n + 1, Line h is a diagonal of the square. For h ∈ [2,n ], Line h is a union of two
line segments of slopes π/ 4 and −π/ 4. There are precisely two possibilities for Line h. If h ∈ Λ,
the left segment has slope −π/ 4, while the right one has slope π/ 4; for h ∈ [2,n ] \ Λ, it goes the
other way round. Berenstein, Fomin and Zelevinsky give the e xample of the arrangement for n = 5
and Λ = {2, 4}, which we show in Figure 2 (points corresponding to elements of Λ are indicated by
ﬁlled circles). They show that i ∈ χ n is compatible with the quiver Q if and only if the chamber
diagram CD( i) is isotopic to Arr(Λ).
If P is a partial quiver, let l(P ) be the subset of [1 ,n + 1] deﬁned in the following way. Put
l1(P ) = {j ∈ [2,n ] : edge j of P is an L}. If the rightmost directed edge of P is an R, and this is
in position i, then let l2(P ) = [1,i − 1], otherwise the empty set. If the leftmost directed edge of P
is an R, and this is in position j, then let l3(P ) = [j + 1,n + 1], otherwise the empty set. Then put
l(P ) = l1(P ) ∪l2(P ) ∪l3(P ). We know from [13, §5.4] that l sets up a one-to-one correspondence
between chamber sets and partial quivers; for a chamber ( c, i), we denote by P (c, i) the partial
quiver corresponding to l(c, i). Also, if i is compatible with a quiver Q, then the partial quivers
6
◦
◦
◦
◦
◦
◦
◦
◦
◦
◦
◦
◦
•
•
•
•
1
2
3
4
5
6
6
5
4
3
2
1
...................................................................................................................................................................................................................................................................................................................................................................................................................
.................................................................................................................................................................................................................................................................................................................................. .................................................................................
................................................................................................................................................................. ................................................................................................................................................................................................................................................................................................................................................................................................................... ..................................................................................................................................................................................................................................................
.................................................................................................................................................................................................................................................................................................................................. .................................................................................
...................................................................................................................................................................................................................................................................................................................................................................................................................
Figure 2: The arrangement Arr {2, 4}.
corresponding to its chambers are precisely those P ≤Q.
Each minimal pair in i corresponds naturally to a chamber ( c, i). Thus, given a chamber ( c, i),
there is a corresponding row of Pi and therefore a corresponding column of Qi, that is, a spanning
vector of Ci. We denote this spanning vector by a(c, i). Similarly, the other n rows ofPi correspond
to inequalities of the form aα j ≥ 0 for α j a simple root, 1 ≤j ≤n. We denote the corresponding
spanning vectors by a(j, i).
We consider a(c, i) = ( a1,a 2,... ,a k) as a multiset M (c, i) of positive roots, where each positive
root α ij occurs with multiplicity, aij. Similarly we write M (j, i) for the multiset corresponding to
a(j, i), for j = 1, 2,... ,k . These multisets have been described in [13].
Theorem 3.1 (See [13, §5.12]).
(a) The multiset spanning vector M (c, i) depends only upon P (c, i). For a partial quiver P we
choose a chamber (c, i) such that P (c, i) = P and write M (P ) = M (c, i).
(b) The multiset spanning vector M (j, i) depends only upon j; we denote it by M (j).
(c) For a partial quiver P , M (P ) is given by the following construction. We say that a sub part ial
quiverY ofP is a component ofP if all of its edges are oriented in the same way and it is maxima l
in length with this property. We say Y has typeL if its edges are oriented to the left, and type R if its
edges are oriented to the right. For such a component Y ofP , let a(Y ) be the number of the leftmost
edge to the right of the component, and let b(Y ) be the number of the rightmost edge to the left of the
component. Let M (Y ) be the set of positive roots α ij satisfying 1 ≤i ≤a(Y ) ≤b(Y ) ≤j ≤n + 1.
Then M (P ) is the multiset union (i.e. adding multiplicities) of the M (Y ), where Y varies over
all components of P , with the multiplicity mij of α ij replaced by nij = ⌈ 1
2mij⌉. Furthermore, for
j = 1, 2,...n , M (j) is the set of positive roots α pq satisfying 1 ≤p ≤j ≤j + 1 ≤q ≤n + 1.
7
