---
doc_id: amc-2730
doc_title: "Braid representatives minimizing the number of simple walks *"
section_id: sec-004-semi-simple-walks-and-cyclic-permutation
section_title: "Semi-simple walks and cyclic permutation"
section_number: null
pages: 14-21
source_pdf: amc_2730.pdf
source_sha256: 65730074a2925c6e
toc_source: outline
doc_brief: "Braid representatives minimizing the number of simple walks * — Given a knot, we develop methods for finding a braid representative that minimizes the number of simple walks."
---
Semi-simple walks and cyclic permutation
The main result in this section is an invariance property which asserts that under the cyclic
permutation, the total number of simple walks on a braid β and its reflection β˚ does not
change. To see this, we introduce the notion of semi-simple walks and study their behavior
under reflection.
Recall the definition of SWβ in Equation (4). Previously, we identified walks W with
their weights, given by the ordered product of operators tai,˘, bi,˘, ci,˘u for each crossing
traversed. However, it will be more convenient to record W using only the operators ai,˘,
and we can do so with no loss of information. In the following, we write ai instead of ai,˘;
it is notationally more compact and the sign ˘ can be recovered from the braid word. Thus,
there is a one-to-one correspondence between simple walks on β and (certain) monomials
in ta1, . . . , aℓu, as we shall now explain.
Given a simple walk W, recall that the active crossings are where the walk jumps
down from the overcrossing arc to the undercrossing arc. If the i-th crossing is active, we
record this with ai. As usual, the crossings are labeled 1, 2, . . . , ℓfrom top to bottom of
the braid. The collection of active crossings of W determines a monomial in ta1, . . . , aℓu,
and thus we see that a simple walk determines a monomial. Conversely, the monomial in
ta1, . . . , aℓu uniquely determines the simple walk W. We will explain this below, but be-
fore we do, notice that not every monomial corresponds to a simple walk. For example, the
trefoil braid σ3
1 has three crossings and so there are 23 “ 8 possible monomials. However,
it has only one simple walk corresponding to the monomial a2.
Suppose then that ai1 ¨ ¨ ¨ aik is a monomial, indicating that crossings i1, . . . , ik are
active. We perform an oriented smoothing at each active crossing. Since the walk jumps
down there, the crossing type determines which of the arcs are active and which are not.
Specifically, if the crossing is positive, the active arc is the one on the left, and if the
crossing is negative, the active arc is the one on the right (see Figure 6). At each active
crossing, we mark the active arc using some marking scheme. (In all figures, the active
arcs have zebra stripes.) We then extend the marking along the arc through any inactive
crossings and around the back of the braid closure, continuing again through the braid and
around the back as many times as necessary, until reaching another active crossing.
σi
σ−1
i
Figure 6: An active crossing and its oriented smoothing for σi and σ´1
i
. The active arc has
zebra stripes and the inactive arc is solid.
One of two things will happen at this active crossing. Either the extended marking is
on an inactive arc, in which case the monomial does not correspond to a valid simple walk,
or it is on the active arc. If the second case holds for all extended arcs, then this is a valid
simple walk. Notice that, in that case, every arc of the partial smoothing of the braid closure
is connected to either an active or an inactive arc. To see that we argue by contradiction. If
the partial smoothing of pβ contains an arc that is not connected to an active or an inactive
arc, then we can follow it along pβ and it will only pass through inactive crossings before
H. U. Boden and M. Shimoda: Braid representatives minimizing the number of simple walks
15
returning to itself. Therefore, it determines a sublink of the closure of β, which contradicts
the assumption that the closure of β is a knot.
Note that, in the second case, the simple walk is determined by the active or marked
arcs, and once those are specified we can read the full operator by recording all the crossings
it passes through. This explains why the simple walk is determined by its active crossings.
Note that, in order for the marked arcs to be a simple walk, the first strand of the braid at
the top and bottom must be inactive.
This process can alternatively be understood in terms of taking the partial smoothing of
a knot K at a subset of crossings. Given a subset of crossings, we can perform the partial
oriented smoothing of K at the selected crossings. In general, this will produce a link. Our
assumption is that the resulting link can be partitioned into two sublinks, one containing
the active (or marked) arcs the other containing the inactive (or unmarked) arcs.
So, for a given monomial to correspond to a simple walk, it must be the case that the
active and inactive arcs of the braid are contained in different components of the partial
smoothing. Further, it must be the case that the first strand of the braid (at bottom) is
inactive.
We can apply this to understand the behavior of simple walks under taking reflection.
In the mirror image, all the crossings are switched. So, using same monomials to record
simple walk on β and β˚, it follows that taking reflection is equivalent to switching the
active and inactive arcs. That is because each positive crossing of β is negative in β˚ and
vice versa. This is illustrated by switching from left to right or vice versa in Figure 6.
The walks on β and β˚ with the same monomial are dual. We explain this from the
point of view of the full set of weights. Let W be a walk on β with monomial ai1 ¨ ¨ ¨ aik,
and let W ˚ be the corresponding walk on β˚ with monomial ai1 ¨ ¨ ¨ aiℓ. Then W and W ˚
trace out disjoint arcs of the braid obtained from β by smoothing the crossings i1, . . . , ik.
In terms of the weights, the walks W and W ˚ have the same set of active crossings, but
at the inactive crossings, their local weights are opposite. Specifically, if i is an inactive
crossing and the local weight Wpiq “ bi, then W ˚
piq “ ci. If instead Wpiq “ ci, then
W ˚
piq “ bi. Likewise, if Wpiq “ 1, then W ˚
piq “ bici, and if Wpiq “ bici then W ˚
piq “ 1.
Lemma 5.1. The simple walks with J Ď t2, . . . , mu on a braid β and its reflection β˚ are
disjoint. In other words, SWβ X SWβ˚ “ ∅.
Proof. Suppose W is a simple walk on β with monomial ai1 ¨ ¨ ¨ aik. Then the partial
smoothing of β at the crossings i1, . . . , ik can be partitioned into active and inactive arcs.
Here, we mark the active arcs, with the first strand of the braid at the top inactive. For the
same monomial on the mirror image β˚, the active and inactive arcs will be switched. In
particular, the first strand on β˚ will be active at the top and marked as such. Therefore,
the monomial ai1 ¨ ¨ ¨ aik will not correspond to a valid simple walk on β˚. It follows that
SWβ X SWβ˚ “ ∅, and this completes the proof.
Definition 5.2. Given a braid word β, we say that a walk W on β is semi-simple if it
is a simple walk on β or on β˚ with J Ď t2, . . . , mu. We use Sβ to denote the set of
semi-simple walks on β. Therefore, Sβ “ SWβ Y SWβ˚.
Since SWβ and SWβ˚ are disjoint, it follows that |Sβ| “ |SWβ| ` |SWβ˚|, where
|S| denotes the cardinality of the finite set S.
We leave it as an exercise to show that every monomial ai for 1 ď i ď ℓcorresponds
to a simple walk on either β or β˚. Thus |Sβ| ě n.
16
Ars Math. Contemp. 23 (2023) #P1.10
Theorem 5.3. The set of semi-simple walks Sβ is invariant under cyclic permutation of
the braid word.
The theorem is a direct consequence of the next two lemmas. The first lemma implies
that cyclic permutation of β does not alter the set of simple walks unless β starts with σ1
or σ´1
1 .
Lemma 5.4. Suppose β “ σε1
i1 σε2
i2 ¨ ¨ ¨ σεℓ
iℓis a braid word with i1 ‰ 1. Let β1 “
σε2
i2 ¨ ¨ ¨ σεℓ
iℓσε1
i1 be the braid obtained by cyclic permutation. Then SWβ “ SWβ1.
Proof. Suppose W P SWβ is a simple walk on β with J Ď t2, . . . , mu. Let W 1 be the
corresponding simple walk on β1, with underlying set J1. There are three possible cases,
depending on whether i1 and i1 ` 1 lie in J. First, if neither i1 nor i1 ` 1 lie in J, then
cyclic permutation has no effect and W 1 is a simple walk on β1 with J1 “ J. Second, if
exactly one of i1, i1 ` 1 lies in J, then J1 ‰ J, but W 1 is nevertheless a simple walk on β1
with J1 Ď t2, . . . , mu. Third, if both i1 and i1 ` 1 are in J, then J1 “ J and W is a valid
simple walk on β1. This completes the proof of the lemma.
The second lemma studies the effect of cyclic permutation for braids that start with σ1
or σ´1
1 . We will show that cyclic permutation of a braid β has the potential to exchange
simple walks between SWβ and SWβ˚, but it does not alter the set of semi-simple walks.
Lemma 5.5. Suppose β “ σε1
i1 σε2
i2 ¨ ¨ ¨ σεℓ
iℓis a braid word with i1 “ 1. Let β1 “
σε2
i2 ¨ ¨ ¨ σεℓ
iℓσε1
i1 be the braid obtained by cyclic permutation. Then Sβ “ Sβ1.
Proof. Suppose W P SWβ is a simple walk on β with J Ď t2, . . . , mu. Let W 1 be the
corresponding simple walk on β1, with underlying set J1. There are two possible cases,
depending on whether or not J contains 2. If 2 R J, then J1 “ J and so W 1 P SWβ1.
Similarly, if 2 P J and the monomial for W contains a1 (in which case β necessarily begins
with σ´1
1 ), then again J1 “ J and W 1 P SWβ1. However, if 2 P J and the monomial for
W does not contain a1, then 1 P J1 and so W 1 R SWβ1. However, the dual walk pW 1q˚
is simple walk on pβ1q˚ with pJ1q˚ Ď t2, . . . , mu, and hence pW 1q˚ P SWpbe1q˚. In
particular, it follows that the set Sβ “ SWβ Y SWβ˚ of semi-simple walks is unchanged
by cyclic permutation. This completes the proof of the lemma.
The next result states that, up to reordering the crossings, the set of semi-simple walks
on a braid word and its rotation are equal.
Proposition 5.6. Let β “ σε1
i1 ¨ ¨ ¨ σεℓ
iℓbe a braid word on m strands, and let β: “
σε1
m´i1 ¨ ¨ ¨ σεℓ
m´iℓbe its rotation. Then the sets of semi-simple walks of β and β: are equal,
namely Sβ “ Sβ:.
Proof. The braid rotation β: is obtained from β by rotating it 1800 in the plane. In order to
relate the semi-simple walks on β and β:, we index the crossings of β: from top to bottom
using n, . . . , 1, and we identify semi-simple walks on β and β: with the subsets of active
crossings. In this way, every semi-simple walk on β and β: corresponds to a monomial
ai1 . . . aik indicating that i1, . . . , ik are the active crossings.
Given a monomial ai1 . . . aik, the semi-simple walk on β is obtained by taking the
smoothing of β at each crossing i1, . . . , ik and locally marking the active and inactive arcs
using a marking scheme that differentiates them. (We mark the active arcs using zebra
H. U. Boden and M. Shimoda: Braid representatives minimizing the number of simple walks
17
stripes.) Then extend the markings around the braid closure. Since ai1 . . . aik corresponds
to a semi-simple walk, the markings on the active and inactive arcs will not coincide.
The same will be true for β:, provided one follows the same procedures at the corre-
sponding crossings. Since β: is obtained by a 1800 rotation which interchanges the first
and last strands of the braid, this will not preserve SWβ since the new walk may not satisfy
J Ď t2, . . . , mu. Nevertheless, the semi-simple walks of β and β: are preserved. This
completes the proof.
6
Simple walks on p2, nq torus braids
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
18
Ars Math. Contemp. 23 (2023) #P1.10
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
Simple walks on p3, nq torus braids
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
H. U. Boden and M. Shimoda: Braid representatives minimizing the number of simple walks
19
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
20
Ars Math. Contemp. 23 (2023) #P1.10
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
H. U. Boden and M. Shimoda: Braid representatives minimizing the number of simple walks
21
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
