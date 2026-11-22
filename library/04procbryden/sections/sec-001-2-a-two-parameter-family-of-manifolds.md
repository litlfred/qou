---
doc_id: 04procbryden
doc_title: "Some computations of Ohtsuki series"
section_id: sec-001-2-a-two-parameter-family-of-manifolds
section_title: "A two-parameter family of manifolds"
section_number: 2
pages: 4-9
source_pdf: 04procbryden.pdf
source_sha256: 8baffbc6542c34a5
toc_source: inferred
doc_brief: "Some computations of Ohtsuki series — We present some computational data on Ohtsuki series for a two pa- rameter family of integer homology spheres obtained by surgery around what we call ‘2–strand"
---
A two-parameter family of manifolds
2.1. Definition of the manifolds
Let K(( S
T )) be the knot obtained by connecting two tangles each of
which consists of two strands simply braided, with S and T crossings
respectively, the two tangles being connected as shown in Figure 1.
Negative S and/or T result in crossings of opposite orientation. Here,
K(( S
T )) will be a knot (and not a link) when S and T are not both odd.
Note that for diﬀerent parities of S and T, the relative orientations
of the diﬀerent parts of K(( S
T )) will be diﬀerent. Replacing (S, T) by
(−T, −S) doesn’t change the knot, while reversing the signs of both S
and T (or interchanging S and T) changes the knot to its mirror image.
Some special cases are, S = 0 (unknot), S = ±1 ((2, T ∓1) torus knot)
along with the examples in the table in table below, where the knots
have been given with their Conway names.
Table .
S
2
3
4
5
6
7
8
4
6
4
5
6
T
2
2
2
2
2
2
2
3
3
4
4
4
K(( S
T ))
41
52
61
72
81
92
101
73
93
83
94
103
In this paper we consider the manifolds M(( S
T )) obtained from S3 by
surgery on the framed knot K(( S
T )) of Figure 1. The number of twists
U in K(( S
T )) is chosen so that the resulting blackboard framed knot will
56
Some computations of Ohtsuki series
T
crossing
u
curls
S
crossings
Figure 1. Knot family K(( S
T ))
have framing ±1, that is, so that M(( S
T )) will be an integer homology
sphere. This requires U = (−1)T S−(−1)ST ±1, where the signs depend
on the parities of S and T (since the relative orientations of diﬀerent
sections of the knot depend upon the parities of S and T), so in fact
for each S and T we obtain two manifolds M±
(( S
T )).
2.2. Calculation of ZK
The Kauﬀman-Lins state sum formulation (see (KL)) of the WRT
invariant ZK(M±
(( S
T ))) uses a sum over states which are colorings of
the one component of K(( S
T )) and of the regions into which the knot
diagram of K(( S
T )) in Figure 1 cuts the plane, by colors from the set
{0, 1, . . . , K −2}. The only admissible colorings are those which sat-
isfy the constraint that for each edge of the knot diagram, the triple
57
N. Jacoby & R. Lawrence
Figure 2. Allowed states for K(( S
T ))
of colors coming from the component and the two regions on either
side of the edge, satisﬁes the Clebsch-Gordan constraint. The possible
colorings in our case are shown in Figure 2. This would give a formula
for ZK(M±
(( S
T ))) as a sum over S + 1 indices in which the summand
contains S −1 nontrivial quantum 6j symbols.
Using recombination, each crossing can be written as a sum over the
label on the internal edge, of the evaluation of an ‘H’ type graph with
two trivalent vertices (Figure 3(1)). This leads to the conﬁguration in
Figure 3(2) which can be simpliﬁed using Figure 3(3) to a network
whose size is independent of S and T, although with a non-standard
weighting. It has just four trivalent vertices (that is, it is a tetrahedral
A triple {a, b, c} is said to satify the Clebsch-Gordan constraint if they satisfy
the triangle inequality |a −b| ≤c ≤a + b while a + b + c is even and at most 2K −4.
58
Some computations of Ohtsuki series
Figure 3. Recombination
network) and the resulting formula for the WRT invariant is
ZK(M±
(( S
T ))) = G−1
±

a,x,y
∆x∆y(λ
a a
x )S(λa a
y
)T (λa a
0
)U
	 a
x
a
a
y
a

(3)
where the sum is over colors a, x and y for which {a, a, x} and {a, a, y
}
are admissible triples, while G± are the Gauss sums 
a ∆2
a(λa a
0
)±
1
obtained by evaluation on the unknot with framing ±1. We have used
notation,
∆n = (−1)n A2(n+1)−q−2(n+1)
q2−q−2
λa b
c
= (−1)(a+b+c)/2A(a(a+2)+b(b+2)−c(c+2))/2
where A is a fourth root of q.
59
N. Jacoby & R. Lawrence
2.3. Properties of Ohtsuki series
The Ohtsuki series ∞
m=0 λm(q −1)m will depend on S and T (and U,
or equivalently on the sign of the surgery). To include this dependence
clearly in the notation, we will denote the coeﬃcients by λ±
m(S, T).
Theorem
For ﬁxed parity and signs for S and T, λm is a polyno-
mial in S and T of degree 2m with rational coeﬃcients.
Proof.
It is known that M −→λm(M) is a ﬁnite type invariant
of manifolds of order m. On the other hand, the map K −→λm(S3
K)
(doing +1 surgery on the knot) gives a Vassiliev invariant of order 2m.
(This follows for example from the Melvin-Morton-Rozansky conjecture
(B-NG) and Le (Le).)
However if |S|+|T| > 2m, then let us pick any 2m+1 of the crossings
in the knot diagram of K(( S
T )) in Figure 1, say s of these crossings will be
from the ones that were counted by S and t from the crossings that were
counted by T, where s+t = 2m+1. One can consider the 22m+1 knots
obtained by variously altering the orientations of these crossings in all
possible ways. Since λm is Vassiliev of order 2m, the alternating sum
of the values of λm on these knots vanishes. When the orientation of a
crossing (say of type S) in K(( S
T )) is ﬂipped, the resulting knot is of the
same type, by with S changed to S−2signS. Without loss of generality,
S and T are positive. Then the result of changing the orientations of i
crossings of type S and j crossings of type T, is K(( S−2i
T −2j )). There are
 s
i
  t
j

ways in which to pick the subsets of crossings to ﬂip, so that
s

i=0
t

j=0
(−1)i+j
 s
i
  t
j

λ±
m(S −2i, T −2j) = 0 ,
(4)
for all S and T positive and all s, t with s + t = 2m + 1. The left
hand side of (4) is the order s + t ﬁnite diﬀerence partial derivative of
λ±
m, s times in the S direction and t times in the T direction. Observe
also that all the terms in (4) involve S and T of ﬁxed parities. This
condition is suﬃcient to guarantee that (for ﬁxed parities) λ±
m(S, T) is
expressible as a polynomial in S and T of order at most 2m, as required.
Since λm ∈Z, these polynomials must have rational coeﬃcients, in fact
22m((2m)!!)2λm(S, T) ∈Z[S, T] where n!! ≡n
r=1 r!.
60
Some computations of Ohtsuki series
