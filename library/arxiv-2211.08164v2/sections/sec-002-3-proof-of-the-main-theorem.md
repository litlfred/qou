---
doc_id: arxiv-2211.08164v2
doc_title: "INFINITELY MANY RIEMANN SURF ACES WITH A TRANSITIVE ACTION ON THE WEIERSTRASS POINTS"
section_id: sec-002-3-proof-of-the-main-theorem
section_title: "Proof of the main theorem"
section_number: 3
pages: 3-6
source_pdf: 2211.08164v2.pdf
source_sha256: aff9ff3ef5ac28be
doc_brief: "INFINITELY MANY RIEMANN SURFACES WITH A TRANSITIVE ACTION ON THE WEIERSTRASS POINTS — In this short note, we prove the existence of inﬁnitely many pairwise non-isomorphic, non-hyperelliptic Riemann"
---
The proof of the main theorem will be a consequence of the following f our facts.
Fact 1. Let X be a non-hyperelliptic compact Riemann surface of genus g = 3. If the
automorphism group of X acts transitively on the Weierstrass points then X ∈ K3.
Proof. Assume that the automorphism group G of X acts transitively on the Weier-
strass points. By [16, Theorem 1], the weight of each of these point s is either equal
to 1 or 2. Since the sum of the weights of all the points of X is equal to 24, the
Riemann surface X has either 12 or 24 Weierstrass points. In particular, the order
of G must satisfy
|G| = 12|GP | or |G| = 24|GP |
where GP stands for the stabiliser subgroup of a Weierstrass point P of X. It follows
that the order of G must be divisible by 12 and consequently, by [1, Theorem 16],
the Riemann surface either belongs to K3 or is isomorphic to the Picard curve
Q : x4 + y4 + z3x = 0.
This latter curve is the unique non-hyperelliptic Riemann surface of g enus g = 3
with exactly 48 automorphisms (see, for instance, [6] and [26]).
To prove the fact it suﬃces to verify that X is not isomorphic to Q. Let
Q = [0 : 0 : 1] ∈ Q
4 SEBASTI ´AN REYES-CAROCCA AND PIETRO SPEZIALI
and denote by C(x, y) the function ﬁeld of Q. A straightforward computation shows
that 1 /x has a pole of order 4 at Q while it is regular elsewhere, and that y/x has a
pole of order 3 at Q while it is regular elsewhere. In other words, Q is a Weierstrass
point of Q, its gap sequence is {1, 2, 5} and its weight is 2. Now, the transitivity
implies that all the Weierstrass points of Q have weight equal to 2, which is the
maximal possible weight in genus three. However, following [18, Theo rem 1.2], there
are exactly two Riemann surfaces of genus three on which all Weiers trass points are of
maximal weight; these surfaces being C0 and C3. Clearly, none of them is isomorphic
to Q and the proof of the fact is done. □
Although the following fact is known (see, for instance, [11]), we inc lude a proof
for the sake of completeness.
Fact 2. Assume that X is isomorphic to Ct with t ⁄= 0 , −1, ±2, t0 and let G denote
its automorphism group. Then the signature of the action of G on X is (0; 2, 2, 2, 3).
In other words, the quotient X/G is rational, the associated regular covering map
X → X/G ∼= P1
ramiﬁes over exactly four values, and the corresponding ﬁbe rs consist of ramiﬁcation
points with stabilisers of orders 2, 2, 2 and 3 respectively.
Proof. We recall that the signature of the action of a group isomorphic to S4 on a
compact Riemann surface of genus g = 3 is either (0; 2 , 2, 2, 3) or (0; 3 , 4, 4). Consider
the automorphism of P2 given by
Φ([ x : y : z]) = [ −y : x : z]
and observe that Φ has only two ﬁxed points
P1 = [−i : 1 : 0] and P2 = [1 : −i : 0].
Note that Φ restricts to an automorphism of order 4 of Ct for each t. A straightforward
computation shows that P1, P2 belong to Ct if and only if t = 2, and therefore
G /greaterorequalslant⟨Φ ⟩ ∼
= C4
is a group of automorphisms of X acting without ﬁxed points. This, coupled with
the fact that S4 possesses a single conjugacy class of cyclic subgroups of order 4,
shows that there is no point of X with G-stabiliser of order divisible by 4. Hence,
the signature cannot be (0; 3 , 4, 4) and the claim follows. □
Fact 3. If X is isomorphic to Ct with t ⁄= 0 , −1, ±2, t0 and there is a Weierstrass
point of X ﬁxed by an involution of X then the action of the automorphism group G
of X is transitive on the Weierstrass points.
Proof. We recall that the group S4 has two conjugacy classes of cyclic subgroups of
order two (a standard reference for permutation groups is [5]; a n ice and concise list
RIEMANN SURF ACES WITH TRANSITIVE ACTION ON WEIERSTRASS POI NTS 5
of properties of S4, including presentations, can be also found at [7]). In terms of the
presentation
G ∼= S4 = ⟨a, b, c, d : a2, b2, (ab)2, c3, cac−1ab, cbc−1a, d2, dadab, [d, b], (dc)2⟩,
these conjugacy classes are represented by ⟨d⟩ (of length 6) and by ⟨b⟩ (of length 3).
A computation shows that the action of G on X is topologically equivalent to the
one represented by the generating vector
(b, db, dc, c−1)
(see [3] for a precise deﬁnition of generating vector) and consequ ently, each involution
ι of G acts with ﬁxed points. More precisely, if ι is conjugate to d then ι has 4 ﬁxed
points, and such points belong to two distinct orbits. By contrast, if ι is conjugate to
b then ι has 4 ﬁxed points, and such points belong to the same orbit (see Mac beath’s
formula [25]).
Now, assume that there exists a Weierstrass point P ﬁxed by an involution. The
weight of points ﬁxed by involutions was investigated by Towse. In fa ct, following
his main results in [37], the expected weight of a point ﬁxed by an involut ion ﬁxing
4 points is equal to 0, that is, these points are not Weierstrass poin ts unless the
image points in the quotient curve are Weierstrass points, either fo r the canonical or
another linear series. In addition, the parity of the actual weight o f such a point must
agree with the parity of the expected weight. It follows that the we ight of P is even;
hence it is equal to 2. If P is ﬁxed by an involution conjugate to d then X has 24
Weierstrass points of weight 2; a contradiction. Thus, one sees th at P must be ﬁxed
by an involution conjugate to b. Thereby, the orbit of P consists of 12 Weierstrass
points of weight 2, and the action is transitive, as claimed. □
Fact 4. If X ∈ K3 then the automorphism group G of X acts transitively on the
Weierstrass points.
Proof. Since Klein’s quartic and Fermat’s quartic are known to have a transit ive
action on the Weierstrass points [24], we only need to consider the r emaining cases,
namely, when X is isomorphic to Ct where t ⁄= 0, −1, ±2, t0. As proved in Fact 2, in
such a case the G-stabiliser subgroup of each point of X is trivial, of order two or of
order three.
Assume that there exists a Weierstrass point P with trivial stabiliser. Then each
point in the G-orbit of P is a Weierstrass point. In particular, we have 24 Weierstrass
points of weight 1, and the action is transitive.
Now, suppose that there exists a Weierstrass point P ﬁxed by an automorphism
of order three. In such a case, X has 8 Weierstrass points. It follows from the fact
that X is non-hyperelliptic that there exists a Weierstrass point R which does not
belong to the G-orbit of P . If the stabiliser of R were trivial, then X would have 32
Weierstrass points; a contradiction. It then follows from the prec eding discussion that
6 SEBASTI ´AN REYES-CAROCCA AND PIETRO SPEZIALI
R must be ﬁxed by an involution conjugate to b and therefore the surface possesses,
in addition to P and its whole G-orbit, 12 Weierstrass points of weight 2. This
is impossible and therefore there is no Weierstrass point among the ﬁ xed points of
automorphisms of order three.
Finally, in the remaining case (namely, if there is a Weierstrass point ﬁx ed by
an involution) the transitivity has been already proved. The proof o f the fact then
follows. □
The previous four facts can be summarised in the following theorem.
Theorem 1. A non-hyperelliptic compact Riemann surface X of genus three has
automorphism group acting transitively on the Weierstrass points if and only if X
belongs to the family K3.
The proof of the main theorem follows directly from the result above .
