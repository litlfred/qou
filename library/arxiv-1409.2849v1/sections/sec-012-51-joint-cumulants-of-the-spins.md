---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-012-51-joint-cumulants-of-the-spins
section_title: "Joint cumulants of the spins"
section_number: 5.1
pages: 32-41
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
choosing σ(1) according to a Bernoulli random variable of parameter 1
2, and then each
sign Xi = σ(i)σ(i + 1) according to independent Bernoulli random variables with
P[Xi = 1] = 1− P[Xi =−1] = eβ
2 cosh β.
In particular, one recovers immediately the value of the partition functionZn(I, 0, β) =
2n(cosh β)n−1. We then want to compute the joint cumulants of the magnetizationMn;
by parity, the odd cumulants and moments vanish. By multilinearity, one can expand
κ(2r)(Mn) =
n
∑
i1,...,i2r=1
κ(σ(i1), . . . ,σ(i2r)),
so the problem reduces to the computation of the joint cumulants of the individual
spins, and to the gathering of these quantities. Notice that the joint moments of the
spins can be computed easily. Indeed, ﬁx i1 ≤ i2 ≤ ··· ≤i2r, and let us calculate
E[σ(i1)··· σ(i2r)]. If i2r−1 = i2r, then the two last terms cancel and one is reduced to
the computation of a joint moment of smaller order. Otherwise, notice that
E[σ(i1)··· σ(i2r−2)σ(i2r−1)σ(i2r)] = E[σ(i1)··· σ(i2r−2)Xi2r−1Xi2r−1+1··· Xi2r−1]
= E[σ(i1)··· σ(i2r−2)] xi2r−i2r−1 where x = tanh β.
By induction, we thus get
E[σ(i1)··· σ(i2r)] = x(i2−i1)+(i4−i3)+···+(i2r−i2r−1).
Let us then go to the joint cumulants. We ﬁx i1≤ i2≤···≤ i2r, and to simplify a bit
the notations, we denote i1 = 1, i2 = 2, etc. We recall that the joint cumulants write as
κ(σ(1), . . . ,σ(2r)) = ∑
Π∈Q2r
µ(Π) ∏
A∈Π
E
[
∏
a∈A
σ(a)
]
,
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS33
where the sum runs over set partitions of [ [1, 2r] ]. By parity, the set partitions with
odd parts do not contribute to the sum, so one can restrict oneself to the set Q2r,even
of even set partitions. If A ={a1 <··· < a2s} is an even part of [ [1, 2r] ], we write
xp(A) = x(a2−a1)+···+(a2s−a2s−1). Thus,
κ(σ(1), . . . ,σ(2r)) = ∑
Π∈Q2r,even
µ(Π) ∏
A∈Π
xp(A).
In this polynomial in x, several set partitions give the same power of x; for instance,
with 2 r = 4, the set partitions {1, 2, 3, 4} and{1, 2}⊔{ 3, 4} both give x(2−1)+(3+4).
Denote P2r the set of set partitions of [ [1, 2r] ]whose parts are all of cardinality 2 (pair
set partitions, or pairings). To every even set partition Π, one can associate a pairing
p(Π) by cutting all the even parts{a1 < a2 <··· < a2s−1 < a2s} into the pairs{a1 <
a2}, . . . ,{a2s−1 < a2s}. For instance, the even set partitionΠ ={1, 3, 4, 5}⊔{ 2, 6} gives
the pairing (1, 3)(4, 5)(2, 6). Then, with obvious notations,
κ(σ(1), . . . ,σ(2r)) = ∑
Π∈Q2r,even
µ(Π) xp(Π). (12)
In Equation (12), two important simpliﬁcations can be made:
(1) One can gather the even set partitions Π according to the pairing ρ = p(Π)∈
P2r that they produce. It turns out that the corresponding sum of Möbius func-
tions F(ρ) has a simple expression in terms of the pairing, see §5.1.3.
(2) Some pairings ρ yield the same monomial xρ and the same functional F(ρ). By
gathering these contributions, one can reduce further the complexity of the sum,
see §5.1.2.
In the end, we shall obtain an exact formula for κ(σ(1), . . . ,σ(2r)) that writes as a sum
over Dyck paths of length 2r− 2, with simple coefﬁcients; see Theorem 21.
5.1.1. Pairings, labelled Dyck paths and labelled planar trees. Before we start the reduction
of Formula (12), it is convenient to recall some facts about the combinatorial class of
pairings. We have deﬁned a pairing ρ of size 2r to be a set partition of [ [1, 2r] ]in r pairs
(a1, b1), . . . ,(ar, br). There are
card P2r = (2r− 1)!! = (2r− 1)(2r− 3)··· 3 1
pairings of size 2r, and it is convenient to represent them by diagrams:
123456789 1 0
2
FIGURE 6. The diagram of a pairing of size 2 r = 10.
On the other hand, a labelled Dyck path of size 2 r is a path δ : [ [0, 2r] ]→ N with 2r
steps either ascending or descending, such that:
• the path δ starts from 0, ends at 0 and stays non-negative;
34 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
1
13
2
1
3
FIGURE 7. The labelled Dyck path corresponding to the pairing of Figure 6.
• each descending step δ(k) > δ(k + 1) is labelled by an integer i∈ [ [1, δ(k)] ].
From a labelled Dyck path of size 2 r, one constructs a pairing on 2 r points as follows:
one reads the diagram from left to right, opening a bond when the path is ascending,
and closing the i-th opened bond available from right to left when the path is descend-
ing with label i. For instance, if one starts from the Dyck path of Figure 7, one obtains
the pairing of Figure 6. This provides a ﬁrst bijection between pairings ρ and labelled
Dyck paths δ.
By considering a Dyck path as the code of the depth-ﬁrst traversal of a rooted tree,
one obtains a second bijection betwen pairings of size 2 r and labelled planar rooted
trees with r edges. Here, by labelled planar rooted tree, we mean a planar rooted tree
with a label i on each edge e that is between 1 and the height h(e) of the edge (with
respect to the root). For instance, the following labelled treeT corresponds to the Dyck
path of Figure 7 and to the pairing of Figure 6:
1
12
13
4
FIGURE 8. The labelled planar rooted tree corresponding to the pairing
of Figure 6.
We shall denote Tr the set of planar rooted trees with r edges (without label), and
D2r the corresponding set of Dyck paths (again without label); they have cardinality
card Tr = card D2r = Cr = 1
r + 1
(2r
r
)
.
They correspond to the subset N2r of P2r that consists in non-crossing pair partitions
of [ [1, 2r] ]; a bijection is obtained by labelling each edge or descending step by 1, and
by using the previous constructions. For instance, the non-crossing pairing, the Dyck
path and the planar rooted tree of Figure 9 do correspond.
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS35
123456789 1 0
5
FIGURE 9. Bijection between non-crossing pairings, Dyck paths and pla-
nar rooted trees.
In what follows, we shall always use the letters ν, δ and T respectively for non-
crossing pairings, for Dyck paths and for planar rooted trees. We shall then use con-
stantly the bijections described above, and denote for instance ν(T) for the non-cros-
sing pairing associated to a tree T, or δ(ν) for the Dyck path associated to a non-cros-
sing pairing ν. We shall also use the exponent + to indicate the following operations
on these combinatorial objects:
• transforming a non-crossing pairing ν of size 2 r− 2 in a non-crossing pairing
ν+ of size 2r by adding the bond{1, 2r} "over" the bonds of ν.
• transforming a Dyck path δ of length 2r− 2 in a Dyck path δ+ of length 2r by
adding an ascending step before δ and a descending step after δ.
• transforming a rooted tree T with r− 1 edges in a rooted tree T+ with r edges
by adding an edge "below" the root.
All these operations are compatible with the aforementioned bijections, so for instance
ν(T+) = ( ν(T))+ and δ(ν+) = ( δ(ν))+.
5.1.2. Uncrossing pairings and the associated poset. Let us now see how the combinatorics
of pairings, Dyck paths and planar rooted trees intervene in Formula (12). We start by
gathering the set partitions Π with the same associated pairing ρ = p(Π). Thus, let us
write
κ(σ(1), . . . ,σ(2r)) = ∑
ρ∈P2r
xρ

 ∑
Π∈Q2r,even
p(Π)=ρ
µ(Π)

 = ∑
ρ∈P2r
xρ F(ρ),
where F(ρ) stands for the sum in parentheses. Notice thatxρ is invariant if one replaces
in a pairing two crossing pairs{a1, a3},{a2, a4} with a1 < a2 < a3 < a4 by two nested
pairs (but non-crossing){a1, a4},{a2, a3}; indeed,
(a3− a1) + (a4− a2) = ( a4− a1) + (a3− a1).
We call uncrossing the operation on pairings which consists in replacing two crossing
pairs by two nested pairs as described above, and we denote ρ1 ≽ ρ2 if there is a
36 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
sequence of uncrossings from the pairing ρ1 to the pairing ρ2; this is a partial order on
the set P2r.
6
FIGURE 10. The operation of uncrossing on a pairing.
Proposition 18. The poset (P2r,≼) is a disjoint union of lattices, and each lattice contains a
unique non-crossing set partition ν, which is the minimum of this connected component of the
Hasse diagram of (P2r,≼). Moreover:
1. On the lattice L (ν) associated to ν∈ N2r, the monomial x ρ and the functional F (ρ) are
constant (equal to xν and F(ν)).
2. The cardinality card L(ν) = N(ν) is given by:
N(ν) = ∏
e∈E(T(ν))
h(e, T(ν)),
where h(e, T) is the height of the edge e in the (planar) rooted tree T, and E (T) is the set of
edges of a tree T.
Proof. First, notice that if ρ1≼ ρ2 in P2r, then there is a sequence of pairings going from
ρ1 to ρ2 such that every two consecutive terms µ and ρ of the sequence differ only by
the replacement of a simple nesting by a simple crossing. By that we mean that we do
not need to do replacements such as the one on Figure 11, which creates 3 crossings at
once.
7
FIGURE 11. The crossing of a nesting that is not simple.
Indeed, denoting (i, j) the crossing of the i-th bond with the j-th bond, bonds being
numeroted from their starting point, one has (1, 3) = ( 1, 2)◦ (2, 3)◦ (1, 2), which is a
composition of simple operations of crossing; and the same idea works for nestings of
higher depth. Thus, the Hasse diagram of the poset (P2r,≼) has edges that consist in
replacements of simple nestings by simple crossings.
This being clariﬁed, it sufﬁces now to notice that via the bijection between pairings
and labelled Dyck paths explained in §5.1.1, the replacing a simple nesting by a simple
crossing corresponds to the raising of a label by 1:
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS37
1
1
2
1
8
FIGURE 12. The operation of uncrossing is a change of labels on Dyck paths.
In particular, ifρ1 and ρ2 are two comparable pairings in(P2r,≼), then the correspond-
ing labelled Dyck paths have the same shape; and for a given shape δ∈ D2r, there is
exactly one corresponding non-crossing pair partition ν = ν(δ), which is minimal in
its connected component in the Hasse diagram of (P2r,≼). Endowed with ≼, this
connected component L(ν) is isomorphic as a poset to the product of intervals
∏
e∈T(ν)
[ [1, h(e, T(ν))] ].
Indeed, the order on the set of labelled trees of shapeT(ν) induced by (L(ν),≼) and by
the bijection between pairings and labelled trees is simply the product of the orders of
the intervals of labels. This proves all of the Proposition but the invariance of F(·) on
L(ν) (the invariance of x(·) was shown at the beginning of this paragraph); we devote
§5.1.3 to this last point and to the actual computation of the functional F(·). □
Assuming the invariance of F(·) on each lattice L(ν), we thus get:
κ(σ(1), . . . ,σ(2r)) = ∑
ρ∈P2r
xρ F(ρ) = ∑
ν∈N2r
xν N(ν) F(ν), (13)
where N(ν) is explicit. Hence, it remains to compute the functional F(ρ).
5.1.3. Computation of the functional F. The main result of this paragraph is:
Proposition 19. The functional F (·) is constant on L (ν), and if ν is a non-crossing pairing,
then
F(ν) = (−1)r−1
∏
e∈T(ν)
h(e,T(ν))⁄=1
(h(e, T(ν))− 1)
if T(ν) has a single edge of height 1, and 0 otherwise.
Lemma 20. The functional F vanishes on pairings associated to labelled rooted trees with more
than one edge of height 1.
Proof. Suppose that Π is an even set partition with p(Π) = ρ; ρ being a pairing of size
2r associated to a labelled Dyck path that reaches 0 after 2 a steps, with 2r = 2a + 2b,
a > 0 and b > 0 (this is equivalent to the statement "having more than one edge of
height 1"). We denote ρ1 and ρ2 the pairings associated to the two parts of the Dyck
path. There are several possibilities:
38 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
• either Π can be split as two even set partitionsΠ1 of [ [1, 2a] ]and Π2 of [ [2a + 1, 2r] ],
with respectively k and l parts, and with p(Π1) = ρ1 and p(Π2) = ρ2;
• or, Π is one of the k× l possible ways to unite two such even set partitions Π1
and Π2 by joining one part of Π1 with one part of Π2;
• or, Π is one of the (k
2)× (l
2)× 2! possible ways to unite two such even set parti-
tions Π1 and Π2 by joining two parts of Π1 with two parts of Π2;
• or, Π is one of the (k
3)× (l
3)× 3! possible ways to unite two such even set parti-
tions Π1 and Π2 by joining three parts of Π1 with three parts of Π2;
• etc.
So, F(ρ) can be rewritten as
∑
p(Π1)=ρ1
p(Π2)=ρ2
(−1)t−1
(
(t− 1)!− kl (t− 2)! +
(k
2
)( l
2
)
2! (t− 3)!−
(k
3
)( l
3
)
3! (t− 4)! +···
)
,
where t = k + l. However, for every possible value of k≥ 1 and l≥ 1, the term in
parentheses vanishes. Indeed, assuming for instance k≤ l, we look at
(k + l− 1)!
k
∑
x=0
(−1)x
(k
x
)( l
x
)( k + l− 1
x
)−1
= k! (l− 1)!
k
∑
x=0
(−1)x
( l
x
)( k + l− 1− x
k− x
)
= k! (l− 1)!
(k− 1
k
)
= 0
by using Riordan’s array rule for the second identity. □
Thus, F vanishes on pairings ρ associated to labelled trees with more than one edge
of height 1. In other words, if F(ρ)⁄= 0, then{1, 2r} is a pair in ρ, and we can look at
the restricted pairing ˜ρ = ρ|[ [2,2r−1] ], which is of size 2r− 2; and we can consider F as a
functional on P2r−2. To avoid any ambiguity, we denote this new functional
G(ρ∈ P2r) = ∑
p(Π)=ρ
(−1)𝓁(Π) (𝓁(Π))!
We then expect the formula G(ρ) = (−1)r ∏e∈E(T(ρ)) h(e). We proceed by induction
on labelled rooted planar trees, and we look at the action of adding a leave of label 1
to the tree, and of increasing a label of an edge by 1. To ﬁx the ideas, it is convenient to
consider the following example of pairing ρ, and the associated set of set partitions Π
with p(Π) = ρ. The pairing ρ of Figure 13 is associated to the labelled planar rooted
tree on Figure 14, and it has functional G(ρ) = ( −1)3 3! + 2× (−1)2 2! = −2. We
denote N(l, ρ) the number of set partitions such that p(Π) = ρ and 𝓁(Π) = l. Hence,
G(ρ) =
r
∑
l=1
N(l, ρ) (−1)l l!
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS39
ℓ =3
ℓ =2
9
FIGURE 13. A pairing of size 2 r = 6 (the upper diagram) and the associ-
ated set of set partitions, which contains 3 elements.
11
2
10
FIGURE 14. The labelled planar rooted tree associated to the pairing of
Figure 13.
(1) Adding an edge . Suppose that one adds an edge with label 1, to obtain for in-
stance:
11
21
11
FIGURE 15. Addition of an new edge of label 1 to the planar rooted tree.
Set ρ′ for the new pairing; notice that it is obtained from ρ by inserting a simple
bond
14 . The set partitions Π′ with p(Π′) = ρ′ are of two kinds:
(a) those where the new bond is left alone. They all come from a set partition
Π with p(Π) = ρ by simply inserting the new bond:
ℓ =4
ℓ =3
12
FIGURE 16. Set partitions where the new bond is left alone.
These terms give the following contribution to G(ρ′):
G(a)(ρ′) =−
r
∑
l=1
N(l, ρ) (−1)l (l + 1)!.
40 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
(b) those where the new bond is linked to another part of a set partition Π
with p(Π) = ρ. Starting from a set partition Π with p(Π) = ρ, the number
of parts of Π that can actually receive the new bond is 𝓁(Π)− (h(e)− 1),
because the new bond cannot be linked to the h(e)− 1 parts that go above
him. In our example:
ℓ =3
ℓ =2
13
FIGURE 17. Set partitions where the new bound is integrated in another part.
These other terms give the following contribution to G(ρ′):
G(b)(ρ′) =
r
∑
l=1
N(l, ρ) (−1)l l! (l + 1− h(e)).
We conclude that G(ρ′) = G(a)(ρ′) + G(b)(ρ′) =−h(e) G(ρ), so the formula for
G stays true when one adds an edge of label 1.
(2) Raising a label . As explained before, raising a label corresponds to adding a
simple crossing to the pairing ρ, which is done by exchanging two ends b and
d of two simply nested pairs {a < b} and{c < d} of ρ. This does not change
the structure of the set of even set partitions Π with p(Π) = ρ; that is, N(l, ρ) =
N(l, ρ′) for every l. So, the formula for G also stays true when one raises a label.
Since every labelled rooted tree is obtained inductively from the empty tree by adding
edges and raising labels, the proof of Proposition 19 is done.
5.1.4. Expansion of the joint cumulants as sums over Dyck paths. Recall that xν stands for
x(a2−a1)+···+(a2r−a2r−1) if ν is the pairing {a1 < a2}, . . . ,{a2r−1 < a2r}. We adopt the
same notations with Dyck paths and planar rooted trees, so xδ or xT stands for xν if
δ = δ(ν) or if T = T(ν). We also denote D∗
2r the image of D2r−2 in D2r by the operation
δ↦→ δ+. Notice that if ∆ = ( δ(T))+ with T tree with r− 1 edges, then
∏
e∈E(T)
h(e) (h(e) + 1) =
2r−1
∏
i=1
∆i,
∆i denoting the value of the Dyck path ∆ after i steps. Starting from Equation (13) and
using the explicit formulas that we have obtained for N(ν) and F(ν), we therefore get:
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS41
Theorem 21. For every indices 1≤···≤ 2r,
κ(σ(1), . . . ,σ(2r)) = (−1)r−1
∑
δ∈D∗
2r
(
2r−1
∏
i=1
δi
)
xδ.
Example. The two non-crossing pairings of size 4 are
15 and
15 ,
the associated powers of x are
x(6−1)+(5−4)+(3−2) and x(6−1)+(5−2)+(4−3),
and the associated quantities G(ν) are 4 and 12, so, with r = 3,
κ(σ(1), . . . ,σ(6)) = 4 x6+5+3−4−2−1 + 12 x6+5+4−3−2−1.
Theorem 21 has several easy corollaries. First of all, we see immediately from it that
the sign of a joint cumulant of spins is prescribed, which was a priori non-obvious. On
the other hand, applying Theorem 21 to the case r = 1 yields
κ(σ(i), σ(j)) = x|j−i|,
that is, the correlation between two spins decreases exponentially with the distance
between the spins. More generally, one can use Theorem 21 to get a useful bound on
cumulants. Notice that the minimal exponent of x that appears in the right-hand side
of the formula is
x(2r)+((2r−1)−(2r−2))+((2r−3)−(2r−4))+···+(3−2)−1.
Indeed, it is easily seen that the exponent of x in xT increases when one makes a rota-
tion of a leaf of T in the sense of Tamari (cf. [Tam62]). Since all trees are generated by
leaf rotations from the tree with all edges of height 1 ( cf. [Knu04]), the previous claim
is shown. It follows that
|κ(σ(1), . . . ,σ(2r))|≤

 ∑
δ∈D∗
2r
2r−1
∏
i=1
δi

 x(2r)+((2r−1)−(2r−2))+···+(3−2)−1.
The quantity
Q(r) = ∑
δ∈D∗
2r
(
2r−1
∏
i=1
δi
)
= ∑
T∈Tr−1

 ∏
e∈E(T)
h(e) (h(e) + 1)


has for ﬁrst values 1, 2, 16, 272, 7936, . . . , and a simple bound on Q(r) is (2r− 2)!, see
Proposition 26 hereafter. Hence, a generalization of the exponential decay of covari-
ances is given by:
Proposition 22. For any positions of spins i1≤ i2≤···≤ i2r,
|κ(σ(i1), . . . ,σ(i2r))|≤ (2r− 2)! xi2r+(i2r−1−i2r−2)+···+(i3−i2)−i1.
