---
doc_id: amc-2730
doc_title: "Braid representatives minimizing the number of simple walks *"
section_id: sec-004-semi-simple-walks-and-cyclic-permutation
section_title: "Semi-simple walks and cyclic permutation"
section_number: null
pages: 14-17
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
stripes.) Then extend the markings around the braid closure. Since ai1 . . . aik corresponds
to a semi-simple walk, the markings on the active and inactive arcs will not coincide.
The same will be true for β:, provided one follows the same procedures at the corre-
sponding crossings. Since β: is obtained by a 1800 rotation which interchanges the first
and last strands of the braid, this will not preserve SWβ since the new walk may not satisfy
J Ď t2, . . . , mu. Nevertheless, the semi-simple walks of β and β: are preserved. This
completes the proof.
6
