---
doc_id: amc-2730
doc_title: "Braid representatives minimizing the number of simple walks *"
section_id: sec-006-simple-walks-on-3n-torus-braids
section_title: "Simple walks on (3,n) torus braids"
section_number: null
pages: 18-21
source_pdf: amc_2730.pdf
source_sha256: 65730074a2925c6e
toc_source: outline
doc_brief: "Braid representatives minimizing the number of simple walks * — Given a knot, we develop methods for finding a braid representative that minimizes the number of simple walks."
---
In this section, we show that the number of simple walks on the braid γn with closure the
p3, nq torus link is given by the n-th term of the sequence 0, 1, 4, 5, 10, 19, 34, 63, 116, 213,
392, 721, 1326, . . . We will find a closed form solution for the number of simple walks and
use it to show they grow exponentially in n.
For n ě 1, let γn “ pσ´1
1 σ´1
2 qn.
The closure of γn is the p3, nq torus knot if
n ı 0 pmod 3q and the p3, nq torus link if n ” 0 pmod 3q. For that reason, we refer
to γn as the (negative) p3, nq torus braid.
Proposition 7.1. Let gpnq be the number of simple walks on the p3, nq torus braid γn.
Then
gpnq “ c1αn ` c2βn ` c3γn,
where α, β, γ are the roots of t3 ´ t2 ´ t ´ 1 (see Equation (7) for explicit formulas for the
roots) and where
c1 “
1 ` 3α´1
´α2 ` 4α ´ 1,
c2 “
1 ` 3β´1
´β2 ` 4β ´ 1,
c3 “
1 ` 3γ´1
´γ2 ` 4γ ´ 1.
Proof. We claim that gpnq satisfies the tribonacci recurrence relation:
gpnq “ gpn ´ 1q ` gpn ´ 2q ` gpn ´ 3q.
(6)
The proof of the claim is long, so we first show how to solve the recurrence relation to get
the formula for gpnq.
The tribonacci numbers Tpnq are the sequence 0, 1, 1, 2, 4, 7, 13, . . . for n ě 0, and
they also satisfy (6). We will use the closed form solution for Tpnq to find a closed form
solution for gpnq. The recurrence Relation (6) has characteristic polynomial pptq “ tn ´
tn´1´tn´2´tn´3 “ tn´3pt3´t2´t´1q. It has one nonzero real root α and two complex
roots β and γ given by
α “ 1
3p1 `
3b
19 ` 3
?
33 `
3b
19 ´ 3
?
33q,
β “ 1
2p1 ´ α `
a
´3α2 ` 2α ` 5q,
γ “ 1
2p1 ´ α ´
a
´3α2 ` 2α ` 5q.
(7)
The closed form solution for Tpnq is a linear combination of powers of the roots of the
characteristic polynomial:
Tpnq “
αn
´α2 ` 4α ´ 1 `
βn
´β2 ` 4β ´ 1 `
γn
´γ2 ` 4γ ´ 1.
The sequence gpnq is related to the tribonacci sequence by the equation
gpnq “ Tpnq ` 3Tpn ´ 1q.
From this we can write gpnq “ c1αn`c2βn`c3γn and use the values gp1q “ 0, gp2q “
1, gp3q “ 4 to solve for the coefficients c1, c2, c3:
c1 “
1 ` 3α´1
´α2 ` 4α ´ 1,
c2 “
1 ` 3β´1
´β2 ` 4β ´ 1,
c3 “
1 ` 3γ´1
´γ2 ` 4γ ´ 1.
It remains to prove the claim, namely to show that the simple walks on γn satisfy the
recurrence Relation (6) for all n ě 4. To do this, we establish a bijective correspondence
between the simple walks on γn and the union of the sets of simple walks on γn´1, γn´2
and γn´3. In general, for braids on three strands, the simple walks will have J “ t2u,
J “ t3u or J “ t2, 3u. For the pn, 3q torus braids, all three occur.
We claim that every simple walk on γn´1, γn´2 and γn´3 can be extended to a simple
walk along γn. We prove this by considering the three cases separately. As before, we will
identify simple walks with their weights, which we write as monomials in tai, bi, ci | i “
1, . . . , 2nu.
Suppose w1 is a simple walk on γn´1. If J “ t2u, then it is on the understrand at the
p2n ´ 2q-nd crossing, and so w1 “ w2b2n´2. We set w “ w2a2n´2b2n and note that w is a
simple walk on γn with J “ t2u. If J “ t3u, then we set w “ w1a2n. If J “ t2, 3u, then
we set w “ w1b2n ¨ a2n´1c2n. Note that in this last case, the paths become inverted, but
this is allowable for the walks with J “ t2, 3u. Figure 8 shows how the simple walks are
extended. In all three cases it is clear that w is a simple walk on γn.
J = {2}
J = {3}
J = {2, 3}
 
Figure 8: Extending simple walks from γn´1 to γn.
J = {2}
J = {3}
J = {2, 3}
 
Figure 9: Extending simple walks from γn´2 to γn.
In a similar way, we can extend simple walks on γn´2. Let w1 be a simple walk on
γn´2. If J “ t2u, then we set w “ w1a2n´3c2n´2b2n. If J “ t3u, then we set w “
w1b2n´2a2n´1c2n. If J “ t2, 3u, then we set w “ w1a2n´2b2n ¨ b2n´3c2n´1c2n. In this
last case, notice that the paths become inverted. Figure 9 shows how the simple walks are
extended. In all three cases, it is clear that w is a simple walk on γn.
Lastly, let w1 be a simple walk on γn´3. Then since γn “ γn´3pσ´1
1 σ´1
2 q3 with
pσ´1
1 σ´1
2 q3 inducing the identity permutation, we can extend w1 to a simple walk on γn
by remaining on the same strands. If J “ t2u, then we set w “ w1b2n´5c2n´3c2n´2b2n.
If J “ t3u, then we set w “ w1b2n´4b2n´3c2n´1c2n. If J “ t2, 3u, then we set w “
w1b2n´5c2n´3c2n´2b2n ¨ b2n´4b2n´3c2n´1c2n. Figure 10 shows how the simple walks are
extended. In all three cases, it is clear that w is a simple walk on γn.
It is not difficult to see that the sets of extended simple walks from γn´1, γn´2, and
γn´3 are all disjoint. For instance, this follows by comparing their weights, and noting
they are pairwise unequal.
The last step is to show that this accounts for all simple walks on γn. We will see that
every simple walk on γn is an extension of a simple walk on γn´1, γn´2 or γn´3.
Suppose w is a simple walk on γn. If J “ t2u, then it must traverse the understrand
at the 2n-th crossing and is on the overstrand just below the p2n ´ 2q-nd crossing. If it
jumps down at the p2n ´ 2q-nd crossing, then w “ w2a2n´2b2n, and w is the extension of
the simple walk w1 “ w2n2n´2 on γn´1. Otherwise, if it remains on the overstrand at the
p2n ´ 2q-nd crossing, then either w “ w1a2n´3c2n´2b2n for w1 a simple walk on γn´2, or
w “ w1b2n´5c2n´3c2n´2b2n for w1 a simple walk on γn´3.
J = {2}
J = {3}
J = {2, 3}
 
Figure 10: Extending simple walks from γn´3 to γn.
If instead J “ t3u, then it is on the overstrand just below the p2nq-th crossing. If it
jumps down at the p2nq-th crossing, then w “ w1a2n for w1 a simple walk on γn´1. Other-
wise, if it remains on the overstrand at the p2nq-th crossing, then either w
“
w1b2n´2a2n´1c2n for w1 a simple walk on γn´2, or w “ w1b2n´4b2n´3c2n´1c2n for w1 a
simple walk on γn´3.
Lastly, suppose J “ t2, 3u. Then w consists of two paths, ends with b2nc2n, and is on
the overstrand below the p2n ´ 1q-st crossing. If it jumps down at the p2n ´ 1q-st crossing,
then w “ w1b2n ¨ a2n´1c2n for w1 a simple walk on γn´1. If it remains on the overstrand
at the p2n ´ 1q-st crossing, then it is also on the overstrand at the p2n ´ 2q-nd crossing. If
it jumps down at the p2n ´ 2q-nd crossing, then w “ w1a2n´2b2n ¨ b2n´3c2n´1c2n for w1
a simple walk on γn´2. If it remains on the overstrand at the p2n ´ 2q-nd crossing, then it
approaches the p2n ´ 4q-th and p2n ´ 5q-th crossings on understrands, and it follows that
w “ w1b2n´5c2n´3c2n´2b2n ¨ b2n´4b2n´3c2n´1c2n for w1 a simple walk on γn´3.
This shows that every simple walk on γn is obtained by extending a simple walk on
γn´1, γn´2 or γn´3. It follows that there is a bijection correspondence between the set
of simple walks on γn and the union of the simple walks on γn´1, γn´2 and γn´3. The
bijective correspondence implies that the sequence gpnq of simple walks on γn satisfy the
recurrence Relation (6).
