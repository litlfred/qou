---
doc_id: amc-2730
doc_title: "Braid representatives minimizing the number of simple walks *"
section_id: sec-005-simple-walks-on-2n-torus-braids
section_title: "Simple walks on (2,n) torus braids"
section_number: null
pages: 17-18
source_pdf: amc_2730.pdf
source_sha256: 65730074a2925c6e
toc_source: outline
doc_brief: "Braid representatives minimizing the number of simple walks * — Given a knot, we develop methods for finding a braid representative that minimizes the number of simple walks."
---
In this section, we show that the number of simple walks on the braid βn with closure
the p2, nq torus link is given by the n-th term in the Fibonacci sequence 1, 2, 3, 5, 8, 13,
21, 34, 55, 89, 144, . . . We will find a closed form solution for the number of simple walks
and use it to show they grow exponentially in n.
For n ě 1 let βn “ σ´n
1 . The closure of βn is the p2, nq torus knot if n is odd and the
p2, nq torus link if n is even. For that reason, we refer to βn as the (negative) p2, nq torus
braid.
Proposition 6.1. Let fpnq be the number of simple walks on the p2, nq torus braid βn.
Then
fpnq “
ˆ 5 `
?
5
10
˙ ˆ 1 `
?
5
2
˙n
`
ˆ 5 ´
?
5
10
˙ ˆ 1 ´
?
5
2
˙n
.
Proof. The first step is to show that the simple walks on βn satisfy the Fibonacci recurrence
relation
fpnq “ fpn ´ 1q ` fpn ´ 2q.
(5)
To do this, we establish a bijective correspondence between the set of simple walks on
βn and the union of the sets of simple walks on βn´1 and βn´2. This is accomplished by
extending simple walks on βn´1 and βn´2 to simple walks on βn.
In the following, we identify simple walks with their weights, which we write as mono-
mials in tai, bi, ci | i “ 1, . . . , nu. Notice that all simple walks under consideration will
have J “ t2u.
Given a simple walk w1 on βn´1, set w “ w1an. Then w is a simple walk on βn. See
Figure 7 (left). Since J “ t2u, this is actually the only way to extend w1 to a simple walk
on βn .
Similarly, given a simple walk w1 on βn´2, set w “ w1bn´1cn. Then w is again a
simple walk on βn. See Figure 7 (right). This is the only way to extend w1 to a simple walk
on βn which avoids simple walks extended from βn´1.
 
Figure 7: Extending simple walks from βn´1 and βn´2 to βn.
The two sets of simple walks are disjoint. This can be verified by noting that they
traverse different strands between the pn ´ 1q-st and n-th crossings. Equivalently, one can
see this by comparing their weights at the n-th crossing. The simple walks extended from
βn´1 have weight an, whereas those extended from βn´2 have weight cn.
Every simple walk on βn is an extension of one on βn´1 or βn´2. To that end, let w be
a simple walk on βn. Since J “ t2u, at the n-th crossing, either the walk jumps down and
has weight an, or it stays on the overstrand and has weight cn. In the first case, w “ w1an
for a simple walk w1 on βn´1. In the second, w “ w1bn´1cn for some simple walk w1 on
βn´2. This establishes the bijective correspondence, and Equation (5) follows directly.
The second step is to solve the recurrence Relation (5). It is a homogeneous linear
recurrence relation with constant coefficients and characteristic polynomial
pptq “ tn ´ tn´1 ´ tn´2 “ tn´2pt2 ´ t ´ 1q.
This polynomial has two non-zero roots:
t “ 1 ˘
?
5
2
.
Therefore, its general solution is given by fpnq “ c1p 1`
?
5
2
qn ` c2p 1´
?
5
2
qn. Using the
values fp1q “ 1 an fp2q “ 2, it follows that
1 “ c1
ˆ1 `
?
5
2
˙
` c2
ˆ1 ´
?
5
2
˙
,
2 “ c1
ˆ1 `
?
5
2
˙2
` c2
ˆ1 ´
?
5
2
˙2
.
Solving for c1, c2, we find that
c1 “ 5 `
?
5
10
and
c2 “ 5 ´
?
5
10
.
The formula for fpnq follows, and this completes the proof.
7
