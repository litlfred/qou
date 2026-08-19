---
doc_id: 0307092v2
doc_title: "Published: 14 February 2004"
section_id: sec-005-6-the-cycle-relation
section_title: "The cycle relation"
section_number: 6
pages: 23-30
source_pdf: 0307092v2.pdf
source_sha256: de2f7ddec49b2ce6
doc_brief: "Extended Bloch group and the Cheeger–Chern–Simons class Walter D Neumann — We deﬁne an extended Bloch group and show it is naturally isom orphic to H3(PSL(2, C)δ; Z)."
---
In this section we prove a general relation called the “cycle relation,” that holds
in ˆP(C). We will use it repeatedly later. It is, in fact, a consequen ce of the
ﬁve-term relation (2) alone and does not involve the transfe r relation (3).
Let K be a simplicial complex obtained by gluing 3–simplices ∆ 1, . . . ,∆ n to-
gether in sequence around a common 1–simplex E . Thus, for each index j
modulo n, ∆ j is glued to each of ∆ j−1 and ∆ j+1 along one of the two faces of
∆ j incident to E . Suppose, moreover, that the vertices of each ∆ j are ordered
such that orderings agree on the common 2–faces of adjacent 3 –simplices.
There is then a sequence ǫ1 = ±1, . . ., ǫn = ±1 such that the 2–faces used for
gluing all cancel in the boundary of the 3–chain ∑ n
j=1 ǫj∆ j . (Proof: choose
ǫ1 = 1 and then for i = 2, . . . , n choose ǫi so the common face of ∆ i−1 and ∆ i
cancels. The common face of ∆ n and ∆ 1 must then cancel since otherwise that
face occurs with coeﬃcient ±2 in ∂ ∑ n
j=1 ǫj∆ j , and E occurs with coeﬃcient
±2 in ∂∂ ∑ n
j=1 ǫj∆ j .)
Geometry & Topology, Volume 8 (2004)
436 Walter D Neumann
PSfrag replacements
E
Figure 4: Conﬁguration for the cycle relation
Suppose now further that a combinatorial ﬂattening wi has been chosen for
each ∆ j such that the “signed sum” of log parameters around the 1–sim plex
E vanishes and the same for parity parameters:
n∑
j=1
ǫjlE(∆ j, wj) = 0 ,
n∑
j=1
ǫjδE(∆ j, wj) = 0 . (6)
We think of the 1–simplex E as being vertical, so that we can label the two
1–simplices other than E of the common triangle of ∆ j and ∆ j+1 as Tj and
Bj (for “top” and “bottom”). Let w′
j be the ﬂattening obtained from wj
by adding ǫjπi to the log parameter at Tj and its opposite edge in ∆ j and
subtracting ǫjπi from the log parameter at Bj and its opposite edge in ∆ j . If
we do this for each j then the total log parameter (and, by Corollary 5.4, also
parity parameter) around any 1–simplex of the complex K is not changed (we
sum log-parameters with the appropriate sign ǫj ): — at E no log-parameter
has changed while at every other 1–simplex πi has been added at one of the
two adjacent 3–simplices and subtracted at the other.
Lemma 6.1 (Cycle relation about E ) With the above notation,
n∑
j=1
ǫj[wj] =
n∑
j=1
ǫj[w′
j] ∈ ˆP(C),
where we are using [w] as a shorthand for [ℓ−1w] (ie, [w] means [z; p, q] where
ℓ(z; p, q) = w; see Lemma 3.2).
Proof Each of the 3–simplices ∆ i has an associated ideal hyperbolic struc-
ture compatible with the combinatorial ﬂattenings wj . This ideal hyperbolic
structure is also compatible with the ﬂattening w′
j . Choose a realization of ∆ 1
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class 437
as an ideal simplex in H
3
. We think of this as a mapping of ∆ 1 to H
3
. We can
extend this to a mapping of K to H
3
which maps each ∆ j to an ideal simplex
with shape appropriate to its combinatorial ﬂattening. Adj acent simplices will
map to the same side of their common face in H
3
if either their orientations
or the signs ǫj do not match and will be on opposite sides otherwise. The fact
that the signed sums of log and parity parameters around the 1 –simplex E are
zero guarantees that the identiﬁcations match up as we go onc e around E .
Note that K has n + 2 vertices. We ﬁrst consider the special case that n = 3
and there is an ordering v0, . . . , v4 of the ﬁve vertices of K that restricts to the
given vertex ordering for each simplex. We also assume the ﬁv e vertices of K
map to distinct points z0, . . . , z4 of ∂H3 .
Each 3–simplex ∆ j for j = 1 , 2, 3 has vertices obtained by omitting one of
the ﬁve vertices v0, . . . , v4 . Denote by ∆ 4 and ∆ 5 the 3–simplices obtained
by omitting each of the other two vertices. The fact that the c ommon 2–
faces of the ∆ j cancel when taking boundary of the chain ǫ1∆ 1 + ǫ2∆ 2 + ǫ3∆ 3
means that, up to sign this sum corresponds to three summands of the chain
∂⟨v0, . . . , v4⟩ = ∑ (−1)i⟨vo, . . . , ˆvi, . . . , v4⟩. Choose ǫ4 and ǫ5 so that ∑ 5
j=1 ǫj∆ j
is ±∂⟨v0, . . . , v4⟩.
By Lemma 3.5, we can choose unique combinatorial ﬂattenings w4 and w5 of
∆ 4 and ∆ 5 so that the signed sum of log parameters and parity parameter s
around any 1–simplex of K ∪ ∆ 4 ∪ ∆ 5 is zero. Note that w4 and w5 do not
change if we replace w1, . . . ,w3 by w′
1, . . . ,w′
3 . By Lemma 3.4 we then have
ǫ1w1 + ǫ2w2 + ǫ3w3 = −(ǫ4w4 + ǫ5w5)
ǫ1w′
1 + ǫ2w′
2 + ǫ3w′
3 = −(ǫ4w4 + ǫ5w5),
proving this case.
We next consider the case that for some index j modulo n the images of ∆ j and
∆ j+1 in
H
3
do not coincide, so their union has ﬁve distinct vertices. By cycling
our indices we may assume j = 1. Since the orderings of the vertices of ∆ 1 and
of ∆ 2 agree on the three vertices they have in common, there is an or dering
of all ﬁve vertices compatible with both ∆ 1 and ∆ 2 . Let ∆ 0 be the simplex
determined by the common 1–simplex E and the two vertices that ∆ 1 and ∆ 2
do not have in common. Then there is an ǫ0 = ±1 such that the common faces of
∆ 0 , ∆ 1 , and ∆ 2 cancel in the boundary of the chain ǫ0∆ 0+ǫ1∆ 1+ǫ2∆ 2 . Choose
a ﬂattening w0 of ∆ 0 such that ǫ0lE(∆ 0, w0)+ǫ1lE(∆ 1, w1)+ǫ2lE(∆ 2, w2) = 0.
Then the relation of the lemma has already been proved for w0 , w1 , w2 , and
by subtracting this relation from the relation to be proved f or w1, . . . ,wn we
Geometry & Topology, Volume 8 (2004)
438 Walter D Neumann
obtain a case of the lemma with one fewer simplices. Thus, if w e assume the
lemma proved for n − 1 simplices then this case is also proved.
The above induction argument fails only for the case that the re are 2 m simplices
that alternately “fold back on each other” so that their imag es in H
3
all have
the same four vertices. The above induction eventually redu ces us to this case
(usually with m = 1). We must therefore deal with this situation to complete
the proof. We ﬁrst consider the case that m = 1 so n = 2. We then have
four vertices z0, . . . , z3 in ∂H
3
. We assume the 1–simplex E is z0z1 . Then the
ordering of the vertices of the faces z0z1z2 and z0z1z3 is the same in each of ∆ 1
and ∆ 2 . Choose a new point z4 in ∂H
3
distinct from z0, . . . , z3 and consider
the ordered simplex with vertices z0, z1, z2 ordered as above followed by z4 .
Call this ∆ 3 . Similarly make ∆ 4 using z0, z1, z3 ordered as above followed by
z4 . Choose ﬂattenings of ∆ 3 and ∆ 4 so that the signed sum of log parameters
for ∆ 1, ∆ 3, ∆ 4 around E is zero. Then we obtain a three simplex relation of
the type already proved for ∆ 1, ∆ 3, ∆ 4 and another for ∆ 2, ∆ 3, ∆ 4 , and the
diﬀerence of these two relations gives the desired two-simpl ex relation.
More generally, if we are in the above “folded” case with m > 1 we can use an
instance of the three-simplex relation to replace one of the 2m simplices by two.
We then use the induction step to replace one of these new simp lices together
with an adjacent old simplex by one simplex and then repeat fo r the other
new simplex. In this way we reduce to a relation involving 2 m − 1 simplices,
completing the proof.
7 Computation of ˆB(C)
In this section we work out the relationship of the extended B loch group with
the usual one. The result is Theorem 7.5.
We consider the case n = 3 of the cycle relation (Lemma 6.1). Denote the
ﬁve vertices involved v0 . . . , v4 and assume the three 3–simplices meet along
the edge E = v3v4 . If we order v0, . . . , v4 in this order and give the simplices
the inherited vertex orders then the cycle relation can be wr itten (with the
appropriate relationship among p0, p1, p2 ):
[x; p0, q0] − [y; p1, q1] + [y/x; p2, q2] =
[x; p0, q0 − 1] − [y; p1, q1 − 1] + [y/x; p2, q2 − 1]. (7)
This is true for any choice of q0, q1, q2 so long as p0, p1, p2 satisfy the appropriate
relation. Thus if we just change q0 and subtract the resulting equation from
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class 439
the above we get
[x; p0, q0] − [x; p0, q′
0] = [ x; p0, q0 − 1] − [x; p0, q′
0 − 1].
From the versions of the three-simplex cycle relation with d iﬀerent orderings of
the vertices v0, . . . , v4 we can similarly derive three versions of this relation:
[x; p, q] − [x; p, q′] = [ x; p, q − 1] − [x; p, q′ − 1]
[x; p, q] − [x; p′, q] = [ x; p − 1, q] − [x; p′ − 1, q]
[x; p, q] − [x; p + s, q − s] = [ x; p + 1, q − 1] − [x; p + s + 1, q − s − 1]
(8)
From these we obtain:
Lemma 7.1 [x; p, q] = pq[x; 1, 1] − (pq − p)[x; 1, 0] − (pq − q)[x; 0, 1] + ( pq −
p − q + 1)[x; 0, 0].
Proof The ﬁrst of the relations (8) implies [ x; p, q] = [ x; p, q − 1] + [x; p, 1] −
[x; p, 0] and applying this repeatedly shows
[x; p, q] = q[x; p, 1] − (q − 1)[x; p, 0]. (9)
The second equation of (8) implies similarly that [ x; p, q] = p[x; 1, q] − (p −
1)[x; 0, q] and using this to expand each of the terms on the right of (9) g ives
the desired equation.
Up to this point we have only used consequences of the ﬁve-ter m relation and
not used the transfer relation (3). We digress brieﬂy to show that the transfer
relation almost follows from the ﬁve term relation.
Proposition 7.2 If ˆP ′(C) and ˆB′(C) are deﬁned like ˆP(C) and ˆB(C) but
without the transfer relation, then in ˆP ′(C) the element κ := [x; 1, 1]+[ x; 0, 0]−
[x; 1, 0] − [x; 0, 1] is independent of x and has order 2. Moreover, ˆP ′(C) =
ˆP(C) × C2 and ˆB′(C) = ˆB(C) × C2 , where C2 is the cyclic group of order 2
generated by κ.
Proof If we subtract equation (7) with p0 = p1 = q0 = q1 = q2 = 1 from the
same equation with p0 = p1 = 0, q0 = q1 = q2 = 1 we obtain [ x; 1, 1]−[y; 1, 1]−
[x; 0, 1] + [ y; 0, 1] = [ x; 1, 0] − [y; 1, 0] − [x; 0, 0] + [ y; 0, 0], which rearranges to
show that κ is independent of x. The last of the equations (8) with p = q = 0
and s = −1 gives 2[ x; 0, 0] = [ x; 1, −1] + [ x; −1, 1] and expanding the right
side of this using Lemma 7.1 gives 2[ x; 0, 0] = −2[x; 1, 1] + 2[x; 1, 0] + 2[x; 0, 1],
showing that κ has order dividing 2.
Geometry & Topology, Volume 8 (2004)
440 Walter D Neumann
To show κ has order exactly 2 we note that there is a homomorphism ǫ : ˆP ′(C)
→ Z/2 deﬁned on generators by [ z; p, q] ↦→(pq mod 2). Indeed, it is easy to
check that this vanishes on the lifted ﬁve-term relation, an d is thus well deﬁned
on ˆP ′(C). Since ǫ(κ) = 1 we see κ is non-trivial. Finally, Lemma 7.1 implies
that the eﬀect of the transfer relation is simply to kill the el ement κ, so the
ﬁnal sentence of the proposition follows.
Lemma 7.3 For any [x; p, q] ∈ ˆP(C) one has [x; p, q] + [1 − x; −q, −p] =
2[1/2; 0, 0].
Proof Assume ﬁrst that 0 < y < x < 1. Then, as remarked in the proof of
Proposition 2.5,
[x; p0, q0] − [y, p1, q1] + [ y
x ; p1 − p0, q2] − [ 1 − x−1
1 − y−1 ; p1 − p0 + q1 − q0, q2 − q1] +
[ 1 − x
1 − y ; q1 − q0, q2 − q1 − p0] = 0
is an instance of the lifted ﬁve term relation. Replacing y by 1 − x, x by 1 − y ,
p0 by −q1 , q1 by −q0 , q0 by −p1 , q1 by −p0 , and q2 by q2 − q1 − p0 replaces
this relation by exactly the same relation except that the ﬁr st two terms are
replaced by [1 − y; −q1, −p1] − [1 − x; −q0, −p0]. Thus subtracting the two
relations gives:
[x; p0, q0] − [y; p1, q1] − [1 − y; −q1, −p1] + [1 − x; −q0, −p0] = 0 .
Putting [ y; p1, q1] = [1 /2; 0, 0] now proves the lemma for 1 /2 < x < 1. But
since we have shown this as a consequence of the lifted ﬁve ter m relation, we
can analytically continue it over the whole of ˆC.
Proposition 7.4 The following sequence is exact:
0 → C∗ χ
− → ˆP(C) → P (C) → 0
where ˆP(C) → P (C) is the natural map and χ(z) := [ z; 0, 1] − [z; 0, 0] for
z ∈ C∗ .
Proof Denote {z, p} := [z; p, q] − [z; p, q − 1] which is independent of q by the
ﬁrst equation of (8). By Lemma 7.3 we have [ z; p, q]−[z; p−1, q] = −{1−z, −q}.
It follows that elements of the form {z, p} generate Ker
( ˆP(C) → P (C)
)
. Com-
puting {z, p} using Lemma 7.1 and the transfer relation, one ﬁnds {z, p} =
{z, 0} which only depends on z . Thus the elements {z, 0} = χ(z) generate
Ker
( ˆP(C) → P (C)
)
. If we take equation (7) with even pi and subtract the
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class 441
same equation with the qi reduced by 1 we get an equation that says that
χ : C∗ → Ker
( ˆP(C) → P (C)
)
is a homomorphism. We have just shown that it
is surjective, and it is injective because R ◦ χ is the map C∗ → C/π2 deﬁned
by z ↦→πi
2 log z .
We can now describe the relationship of our extended groups w ith the “classical”
ones.
Theorem 7.5 There is a commutative diagram with exact rows and columns
0 0 0

↓


↓


↓
0 − − − − →µ∗ − − − − →C∗ − − − − →C∗/µ∗ − − − − →0
χ|µ∗


↓ χ


↓ β


↓


↓
0 − − − − →ˆB(C) − − − − →ˆP(C) ν− − − − →C ∧ C − − − − →K2(C) − − − − →0

↓


↓ ǫ


↓ =


↓
0 − − − − → B(C) − − − − → P(C) ν′
− − − − →C∗ ∧ C∗ − − − − →K2(C) − − − − →0

↓


↓


↓


↓
0 0 0 0
Here µ∗ is the group of roots of unity and the labeled maps deﬁned as fo llows:
χ(z) = [ z; 0, 1] − [z; 0, 0] ∈ ˆP(C);
ν[z; p, q] = (log z + pπi) ∧ (− log(1 − z) + qπi);
ν′[z] = 2
(
z ∧ (1 − z)
)
;
β[z] = log z ∧ πi;
ǫ(w1 ∧ w2) = −2(ew1 ∧ ew2);
and the unlabeled maps are the obvious ones.
Proof The top horizontal sequence is trivially exact while the oth er two are
exact at their ﬁrst two non-trivial groups by deﬁnition of ˆB and B . The bottom
row is exact also at its other two places by Milnor’s deﬁnitio n of K2 . The
exactness of the third vertical sequence is elementary and t he second one has
just been proved. The commutativity of all but the top left sq uare is elementary.
A diagram chase conﬁrms that χ maps µ∗ to ˆB(C) and that the left vertical
sequence is also exact. Another conﬁrms exactness of the mid dle row.
Geometry & Topology, Volume 8 (2004)
442 Walter D Neumann
