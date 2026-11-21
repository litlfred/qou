---
doc_id: arxiv-q-alg-9702017v2
doc_title: "Idempotents of Hecke algebras of type A"
section_id: sec-004-5-framing-and-the-murphy-operators
section_title: "Framing and the Murphy operators"
section_number: 5
pages: 14-25
source_pdf: 9702017v2.pdf
source_sha256: 282c911abb2a54e9
toc_source: outline
doc_brief: "Idempotents of Hecke algebras of type A — We use a skein-theoretic version of the Hecke algebras of type A to present three-dimensional diagrammatic views of Gyoja’s idempotent el- ements, based"
---
Framing and the Murphy operators
In this section we return to the 3-dimensional views of the skein S(B, P) for a
ball B ∼= B3 with a set P of 2n distinguished points on its boundary, introduced
in Sect. 4.
Idempotents of the Hecke algebra.
15
T
Q
Q
Q
Q
-1
β
β
/
/
Figure 11: The wiring of (D2 × I, P ′) into (D2 × I, P)
We noted earlier that this skein is linearly isomorphic to Hn. In order to
translate the results about Hn from the previous section into a 3-dimensional
setting we shall use some explicit choices of isomorphism in a couple of standard
cases.
We start with the case when B = D2 × I and the set P = PI ∪PO of input
and output points consists of PI = Q × {1} and PO = Q × {0} for some Q ⊂D2
with |Q| = n. Write S(B, P) = HQ in this case, which will be identiﬁed with
Hn when the points of Q lie in a straight line across D2. We can compare HQ′
and HQ by choosing an n-string braid β in D2 × I with end points Q × {0}
and Q′ × {1}, or equivalently a homeomorphism from (D2, Q) to (D2, Q′). Now
construct a wiring as shown in Fig. 11, where the strings meet the level disks in
Q or Q′ as indicated and are connected by β or β−1. This induces a linear map
S(β) : HQ′ →HQ, where the image of a tangle T in HQ′ is the extended tangle
in HQ shown in Fig. 11.
Note that β is a braid in D2 × I in the sense that its strings are monotone in
the last coordinate. It should properly be regarded as an element of the ‘braid
groupoid’ of D2.
The skein HQ is clearly an algebra under the obvious stacking operation, and
S(β) is an algebra homomorphism. Indeed it is an algebra isomorphism with
inverse S(β−1). Thus HQ ∼= Hn for each Q with |Q| = n.
In the previous section we constructed an element Eλ ∈HQ where the points
Q lie in the cells of the Young diagram λ. The element eλ ∈Hn has the form
eλ = S(β)(Eλ) where the braid β lines up the cells of λ according to the tableau
T(λ). Then Eλ is itself a quasi-idempotent in HQ. Now Eλ is constructed as the
composite Eλ = EI
λEO
λ of two elements of HQ, with EI
λ made from the row boxes
with elements aj and EO
λ made from the column boxes with bj. In the notation
of the last chapter we have S(β)(EI
λ) = Eλ(a) and S(β)(EO
λ ) = ωπλEλ∨(b)ω−1
πλ .
To understand the behaviour of eλ further, by considering Eλ and other elements
of the skeins HQ, we shall show the following.
Lemma 5.1 Let Q ⊂D2 with |Q| = n. There is a unique element aQ in the
Idempotents of the Hecke algebra.
16
algebra HQ which corresponds to an ∈Hn under every choice of isomorphism
S(β).
Proof.
The element an ∈Hn is central, by Lemma 4.3. Given Q select any
braid β to connect Q to the straight line of n points, and deﬁne aQ = S(β)(an).
Let γ be another such braid.
Then γ−1β represents an element of Hn which
commutes with an. Hence S(γ−1β)(an) = an, and S(γ)(an) = S(β)(an).
A similar element bQ can be constructed from bn.
✷
For every subdisk D′ ⊂D2 with R = Q ∩D′ there is an induced inclusion of
algebras HR ⊂HQ, where a tangle in D′ × I is extended by the trivial strings
on Q −R. The discussion following Lemma 4.3 shows that aQaR is a non-zero
multiple of aQ, and similarly bQbR is a non-zero multiple of bQ.
We now look at some consequences of the work in Sect. 4 within the context
of the general skein S(B, P). Take B = B3 and P = PO ∪PI ⊂S2. Deﬁne a
geometric partition ω of P to be a family of disjoint discs {Dα} in S2 containing
the points of P, such that no disc Dα contains both output and input points.
The geometric partition ω determines two partitions λ(ω) and µ(ω) of n,
where λ1 ≥λ2 ≥· · · ≥λk are the numbers of points of PI in the individual disks
Dα of the partitioning family, and µ is determined similarly by the output points
PO.
Given a geometric partition ω construct a wiring in S2 × I as follows. For
each disk Dα containing a subset Pα ⊂P insert the skein element aPα or bPα into
Dα ×I ⊂S2 ×I, choosing aPα if Pα ⊂PO and bPα if Pα ⊂PI. The union of these
gives a skein element in S2 × I, which induces a linear map
S(ω) : S(B, P) →S(B, P)
by attaching S2 × I as a ‘shell’ around B3.
In many cases the nature of the map S(ω) depends only on the partitions
λ(ω) and µ(ω), as described in the following lemma, which is an immediate
consequence of Lemmas 4.4 and 4.6.
Lemma 5.2 Let S(ω) : S(B, P) →S(B, P) be the linear map induced from a
geometric partition ω of P.
(a)
If λ(ω) and µ(ω) are inseparable then S(ω) = 0.
(b)
If λ(ω) is just separable from µ(ω) (when µ(ω) = λ(ω)∨) then S(ω)
has rank 1. Its image is spanned by S(ω)(T), where T is any tangle whose arcs
separate λ(ω) from µ(ω).
Proof.
Choose a homeomorphism from B to D2×I which carries the disks
Dα containing PO to D2 × {0} and those containing PI to D2 × {1}, arranged
in partition order along a straight line with the input or output points lined up
inside each disk. This induces a linear isomorphism, φ say, from S(B, P) to Hn.
Idempotents of the Hecke algebra.
17
The homeomorphism also extends to a map of S2 × I which carries the wiring
determined by ω to the element Eλ(ω)(a) at the top of D2 ×I along with Eµ(ω)(b)
at the bottom. Then φ ◦S(ω) ◦φ−1 : Hn →Hn is the linear map given by
T 7→Eλ(ω)(a) T Eµ(ω)(b).
In case (a) this map is zero by Lemma 4.4, and so S(ω) = 0.
In case (b) its image has dimension 1, spanned by the image of any T which
separates λ(ω) from µ(ω), by Lemmas 3.3 and 4.6. The isomorphism φ gives
the corresponding result for S(ω) using tangles in S(B, P) which correspond to
separating tangles T under the homeomorphism.
✷
Even where ω is separable we can deduce easily that S(ω)(T) = 0 for certain
tangles T.
Lemma 5.3 Let ω′ be a subpartition of ω, in the sense that every disk of ω′ is
contained in a disk of ω. Then S(ω) (S(ω′)(T)) is a non-zero multiple of S(ω)(T)
for every T.
Proof.
This follows at once from the construction of S(ω) and the prop-
erties of the elements aQ and bQ, when the shell for ω′ is viewed as lying inside
the shell for ω.
✷
Hence if S(ω′)(T) = 0 then S(ω)(T) = 0 also.
Lemma 5.4 Suppose that some of the strings of a tangle T can be enclosed in a
ball B′ ⊂B which does not meet the remaining strings of T. A given geometric
partition ω of P = T ∩∂B determines a partition ω′ of P ′ = P ∩B′, using disks
Dα ∩B′. If λ(ω′) and µ(ω′) are inseparable then S(ω)(T) = 0.
Proof.
Extend ω′ to a partition of P by choosing the trivial partition on
the points of P −P ′. Then S(ω′)(T) = 0, by Lemma 5.2 applied to B′. Now ω′
is a subpartition of ω, so S(ω)(T) = 0, by Lemma 5.3.
✷
The simplest case occurs when B′ contains just two strings whose inputs
and outputs each lie in a disk in B′ contained in one of the disks of ω. Then
λ(ω′) = µ(ω′) = (2) are inseparable partitions.
We return now to the study of eλ ∈Hn by means of Eλ = EI
λEO
λ in the skein
HQ based on the Young diagram λ. Write ω for the geometric partition grouping
the input points by the rows of λ and the output points by its columns. Then
λ(ω) = λ and µ(ω) = λ∨are just separable, and S(ω)(T) = EI
λTEO
λ for any
T ∈HQ. By Lemma 5.2(b) we can then write EI
λTEO
λ = ϕTEI
λEO
λ = ϕTEλ for
some scalar ϕT. In particular, if T is central then TEλ = ϕTEλ, and consequently
S(β)(T)eλ = ϕTeλ in Hn, for the appropriate β.
Thus any central element c ∈Hn satisﬁes ceλ = cλeλ for some scalar cλ.
The eigenvalue cλ may be found as ϕT when we choose T = S(β−1)(c) in the
Idempotents of the Hecke algebra.
18
Fn
=
...
...
...
Figure 12: The full curl Fn on n strings
. . .
. . .
Figure 13: The braid Ti
appropriate skein HQ. We will now calculate these eigenvalues for two important
central elements of Hn.
The ﬁrst of these is the full curl Fn ∈Hn, which is closely involved with
changes of framing. In the skein HQ we can describe the full curl FQ as follows.
Take the trivial framed braid Q × I ⊂D2 × I and rotate D2 × {1} through 2π
anticlockwise while keeping D2×{0} ﬁxed. The resulting framed braid represents
FQ. Note that the framing of each string in FQ is 1. It is clear that S(β)FQ′ = FQ
for any β. The full curl Fn can be drawn, with blackboard framing, as in Fig. 12.
We can describe FQ recursively by selecting a subdisk containing n −1 of the
points, R say. Then FQ is the composite of FR with the braid which takes the
remaining string once around all the others in the subdisk.
Using tensor product to denote the juxtaposition of oriented tangles in Hn,
the recursive deﬁnition gives
Fn = Tn(Fn−1 ⊗1) =
n
Y
i=1
Ti ⊗1n−i ,
where Ti is the i-string tangle in Fig. 13 (all strings have blackboard framing
except the ith which has its framing indicated by the dotted line in the ﬁgure).
Theorem 5.5 Let λ be a Young diagram with n cells. Then Fneλ = fλeλ, where
fλ = x|λ|2v−|λ|snλ and nλ =
X
(i,j)∈λ
2(j −i).
Proof.
By induction on the number of strings.
When n = 1 we have
λ = ✷. Then eλ is the single string, and fλ = xv−1 by the skein relations.
Assume now that the result holds for all Young diagrams with fewer than n
cells. Let λ be a Young diagram with n cells and let µ denote the Young diagram
obtained from λ by deleting a ﬁxed choice of extreme cell, with coordinates (p, r).
Idempotents of the Hecke algebra.
19
. . .
...
Figure 14: The element EI
λTEO
λ = S(ω)(T)
We shall work in the skein HQ based on λ, and show that FQEλ = fλEλ by
calculating S(ω)(FQ). Take R ⊂Q to be deﬁned by the subdiagram µ. We can
include the algebra HR in HQ by adjoining an extra trivial string to the skein.
Then FQ = FRT, where T is a version of Fig. 13 in which the extreme string
winds once around the strings from R. It is geometrically clear that T commutes
with the subalgebra HR.
Now since µ is a subdiagram of λ we have EI
λEI
µ = kEI
λ and EO
µ EO
λ = lEO
λ for
some non-zero k, l. Then FQEλ = EI
λFQEO
λ since FQ is central and
S(ω)(FQ) = EI
λFQEO
λ
=
(lk)−1EI
λEI
µFRTEO
µ EO
λ
=
(lk)−1EI
λ(EI
µFREO
µ )TEO
λ
=
fµ(lk)−1EI
λ(EI
µEO
µ )TEO
λ
=
fµEI
λTEO
λ = fµS(ω)(T).
It is enough to prove that
EI
λTEO
λ = x2|µ|+1v−1s2(r−p) Eλ ,
(1)
since then FQEλ = fµx2|µ|+1v−1s2(r−p) Eλ. Rewriting fµ by the induction hypoth-
esis we obtain
fλ = x|µ|2+2|µ|+1v−1−|µ|s2(r−p)+nµ = x|λ|2v−|λ|snλ .
The picture of EI
λTEO
λ = S(ω)(T) is given in Fig. 14.
We now represent some simple braids B in the skein HQ by schematic pictures
looking down on B from above. The points of Q are points on the grid. Any
string not explicitly shown is assumed to pass straight down, while a path with an
arrow indicates the projection of a string descending from the top to the bottom
in D2 × I. When all strings pass straight down we have the identity braid Id,
with S(ω)(Id) = Eλ.
Idempotents of the Hecke algebra.
20
T
=
.
.
...
. . .
....... . . . . . . ...
.
..
.... ..
.... . . . . .
..
✕
,
T ′′
=
..
.
.
. . .
....... . . . . . . ....
.. .... ..
.... . . . . .
...
✕
Figure 15: Reduction to the extreme rectangle
.. . .
✕
...
✕
Figure 16: Smoothed braids arising from crossings outside the extreme rectangle
The schematic picture for T is shown in Fig. 15. There is one string in this
braid starting and ﬁnishing from the chosen extreme position, marked ×, which
encircles the vertical strings based on µ. We now alter T systematically through
a sequence of braids which retain the vertical strings while taking the encircling
string round successively fewer verticals. When we pass from one such braid T ′ to
another T ′′ by crossing through one vertical string, noted on the accompanying
diagrams by •, the skein relation gives T ′ = x2T ′′ + x(s −s−1)L, where the braid
L arises by smoothing at the crossing of the vertical and encircling strings. Thus
the diagram for L has two non-vertical arcs, one from × to • and one from •
to ×. The braids L which arise in this way will be shown, using Lemma 5.4, to
satisfy S(ω)(L) = 0, giving S(ω)(T ′) = x2S(ω)(T ′′), when the string • does not
lie on the edge of the extreme rectangle determined by ×, in the sense of Sect. 3.
Starting then with T, pull the encircling string successively through the ver-
tical strings outside the extreme rectangle for ×, working leftward through the
columns and upwards through the rows until it encircles the extreme rectangle.
The diagram of a typical smoothed braid L is shown in Fig. 16.
Each L has a subbraid made up of an L-shaped array of vertical strings taken
from the row and column containing × and •, along with a single string joining ×
and •. This subbraid can be enclosed in a ball B′ for which the induced geometric
partition ω′ determines an inseparable pair of partitions λ(ω′) and µ(ω′). Thus
S(ω)(L) = 0 in each case, by Lemma 5.4. A typical example is shown in Fig. 17.
The encircling string in T can then be pulled through |λ| −rp strings to
give the braid T ′′ in which it encircles the extreme rectangle, as in Fig. 15, with
S(ω)(T) = x2(|λ|−rp)S(ω)(T ′′).
Idempotents of the Hecke algebra.
21
Figure 17:
C1 =
.
..
. . .
....... . . . . . . ....
.
. .
.
.. ..
....
..
. . .
....
✕
,
S =
.
. . .
....... . . . . . . ......
..
.
. ..
.... . . . . .
..... .
✕
,
C2 =
. . .
..
.. ..
.
...
.
.
..... . . . . .
.
.....
.
.
.. .
.. .
.... .
✕
Figure 18:
Now write T ′′ = C1SC2, where C1, S and C2 are shown in Fig. 18. A similar
systematic move of the encircling string in S through the vertical strings inside
the extreme rectangle, working through the columns from the left and from the
top down, will replace S by a braid with all strings vertical, at the expense of
a factor x2(r−1)(p−1). A typical smoothed braid L arising from the skein relation
at an intermediate crossing change is shown in Fig. 19, again with an L-shaped
subdiagram which ensures that S(ω)(L) = 0.
The framing of the eventual vertical string through × is still +1; when this is
returned to 0 we get S(ω)(S) = x2(r−1)(p−1)xv−1Eλ. The calculations for Eq. (1)
are completed by noting that EI
λC1 = (xs)2(r−1)EI
λ and C2EO
λ = (−xs−1)2(p−1)EO
λ ,
by Lemma 4.3.
Then S(ω)(T ′′) = x2(r+p−2)s2(r−p)S(ω)(S), giving
S(ω)(T) = x2|λ|−1s2(r−p)v−1Eλ
as claimed.
✷
..
...
✕
Figure 19: A smoothed braid arising from a crossing inside the extreme rectangle
Idempotents of the Hecke algebra.
22
Note that
X
(i,j)∈λ
2j =
k
X
i=1
λi
X
j=1
2j =
k
X
i=1
λi(λi + 1) =
k
X
i=1
λ2
i + |λ|.
Similarly,
X
(i,j)∈λ
2i =
m
X
j=1
(λ∨
j )2 + |λ|. Thus, by Theorem 5.5, nλ =
X
i
λ2
i −
X
j
(λ∨
j )2.
As we discuss in Sect. 6, Theorem 5.5 is a skein theoretic calculation of the
framing factors for the irreducible representations of SU(N)q. There are various
other well-known formulae, in terms of the weights of the representation or the
length of either the columns or rows of the Young diagram. In [14] Morton gives
the 3-variable formula for fλ, with nλ deﬁned recursively in terms of smaller
Young diagrams. Alternatively, the fact that a Young diagram with exactly N
cells in the ﬁrst column indexes the same representation as the Young diagram
obtained by removing this column gives an inductive proof of a formula in terms
of the column length. For a given N, the framing factor becomes a function of
s alone. Reshetikhin [] proved that fλ(N) = s∆λ where ∆λ is the value of the
Casimir operator on the irreducible representation associated to λ. An expression
for ∆λ in terms of the weights of the representation, was described to the authors
by Kohno, from which a form of nλ in terms of row length alone can be derived,
namely, nλ = P λ2
i + |λ| −P 2iλi.
However, this lacks the simplistic charm of stating that nλ is twice the sum
of the contents.
The other central element of Hn which we consider is the sum M of the
Murphy operators. These are discussed in [5] and are most easily described in the
version Hn(1, z) of the Hecke algebras, converting by the appropriate isomorphism
as needed. In Hn(1, z) the jth Murphy operator M(j) =
j−1
X
i=1
ω(i j) is the sum of all
the positive transposition braids involving the string j and strings of smaller label.
Then write M = Pn
j=1 M(j) = P ωτ, where the sum is over all transpositions
τ ∈Sn, to give an element which can readily be shown by skein theory to be
central in Hn. We know from our work above that eigenvalues mλ can be found
such that Meλ = mλeλ.
As above we shall calculate mλ from the equation
EI
λS(β)(M)EO
λ = mλEλ in HQ, with Q deﬁned by the diagram λ. We again use
schematic diagrams to consider the constituent braids S(β)(ω(i j)) = β−1ω(i j)β
inside HQ.
This allows an easy calculation of the scalar m(j)
λ
which satisﬁes
EI
λS(β)(M(j))EO
λ
= m(j)
λ Eλ and hence gives mλ = P
j m(j)
λ .
It provides an
alternative to the original algebraic proof of Theorem 5.7 by Dipper and James
[5].
One of the advantages of the central element M over, say, the full curl is
demonstrated in [12]. There are many examples of distinct Young diagrams with
the same framing factor, which is the eigenvalue of the full curl. The smallest
example occurs with six cells, where the partitions (4, 1, 1) and (3, 3) both have
framing factor x36v−6s6. Any pair of Young diagrams with the same number of
Idempotents of the Hecke algebra.
23
ω(i j)
=
. . .
. . .
...
...
Figure 20:
cells, which are self conjugate will have the same framing factor, for example
(4, 2, 1, 1) and (3, 3, 2). In contrast, the scalar mλ uniquely determines λ, given
the number of cells.
Recall that the Young tableau T(λ) was deﬁned by labelling the cells of λ
from 1 to |λ| along the rows. For the three-dimensional picture, we use this to
indicate the ordering of the strings within the Young diagram, and to determine
the conversion braid β used in the isomorphism S(β) with the Hecke algebra.
As we saw in the case of the framing coeﬃcient, the power of x really only
keeps track of the number of strings. We shall set x = 1 in what follows. This
gives one of the presentations of the Hecke algebra, Hn(1, z), described in Sect. 2.
The result for Hn follows directly from an application of the isomorphism with
Hn(1, z).
We can write M(j) as the sum of positive transposition braids
M(j) =
j
X
i=1
ω(i j) ,
where ω(i j) is the positive permutation braid in Fig. 20.
Lemma 5.6 Suppose that the jth cell of λ has coordinates (k, l). Then
EI
λS(β)(M(j))EO
λ = sl−k[l −k] Eλ .
Proof.
Work as above in the algebra HQ based on the diagram λ. Write
j@i for the braid drawn schematically in Fig. 21. If we pull the string j through
j@i =
.
.
. . .
....... . . . . . . .....
.
.
...
.
.
.... .
. . .
..... .
.
●
●
j
i
,
S(β)(ω(i j))) =
.
.
. . .
....... . . . . . . .....
.
.
...
.
.
.... .
. . .
..... .
.
j
i
●
●
Figure 21:
the vertical string i we get the braid j@(i + 1), while smoothing at the crossing
of these strings gives the braid S(β)(ω(i j)), shown also in Fig. 21. Then
j@i = (s −s−1)S(β)(ω(i j)) + j@(i + 1),
Idempotents of the Hecke algebra.
24
by the skein relation (with x = 1). Summing over all i < j gives
j@1 −j@j = (s −s−1)S(β)(M(j)).
From the calculation in Theorem 5.5 we have
S(ω)(j@1) = EI
λ(j@i)EO
λ = s2(l−k)Eλ
while S(ω)(j@j) = Eλ, where ω is the geometric partition determined, as before,
by the diagram λ. Therefore
EI
λS(β)(M(j))EO
λ = S(ω)(j@1 −j@j) = (s2(l−k) −1)
(s −s−1)
Eλ .
✷
We can thus prove the result of Dipper and James [5] directly using skein
theory. For completeness, we also include the proof that the eigenvalues of the
sum of Murphy operators uniquely determines the Young diagrams, which is due
to Katriel, Abdesselam and Chakrabarti [12]
Theorem 5.7 Let λ be a Young diagram with n cells. Set M =
Pn
j=1 M(j).
Then M is central in Hn and Meλ = mλeλ where
mλ =
X
(k,l)∈λ
s(l−k)[l −k] =
X
(k,l)∈λ
s2(l−k) −1
s −s−1
.
The Young diagram λ is determined by mλ and n.
Proof.
First we show that M is central.
It is enough to show that σi
commutes with M, for i = 1, . . . , n −1. We know that M =
X
k<l
ω(k l) is the sum
of all the positive transposition braids, working as above in Hn(1, z). If neither
k nor l is equal to i or i + 1 then σi commutes with ω(k l). It also commutes with
ω(i i+1) = σi.
The remaining elements in M can be written as
Ai =
X
k<i

ω(k i) + ω(k i+1)

+
X
i+1<l

ω(i l) + ω(i+1 l)

.
Now σi ω(k i) σi = ω(k i+1), for k < i. Similarly σi ω(i+1 l) σi = ω(i l), for i + 1 < l.
Hence Ai = X + σi X σi, where X =
X
k<i
ω(k i) +
X
i+1<l
ω(i+1 l). Then
σi Ai
=
σi X + σ2
i X σi
=
σi X + z σi X σi + X σi
=
Ai σi,
Idempotents of the Hecke algebra.
25
since σ2
i = z σi + 1 in Hn(1, z). This completes the proof that M is central.
Then S(β)(M) is central in HQ and so S(β)(M)Eλ = EI
λS(β)(M)EO
λ
=
mλEλ. The value of mλ as claimed follows directly from Lemma 5.6 by writing
M = P
j M(j).
To work in the version of the Hecke algebra used by Dipper and James we
need simply apply the isomorphism from Hn(1, z) to Hn(q).
A further small
change is needed to give their exact result, as the Murphy operators in their
paper correspond to s M(j) here, and so their value of mλ is s times our value.
To recover λ from mλ calculate the Laurent polynomial
(s −s−1)mλ + n =
X
(k,l)∈λ
s2(l−k) =
X
cjs2j say.
Then the integer cj gives the number of cells in λ on the diagonal at distance j
to the right of the leading diagonal.
✷
6
