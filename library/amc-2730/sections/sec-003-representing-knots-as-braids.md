---
doc_id: amc-2730
doc_title: "(Also available at http://amc-journal.eu) Braid representatives minimizing the number of simple walks* Hans U. Boden † , Matthew Shimoda ‡"
section_id: sec-003-representing-knots-as-braids
section_title: "Representing knots as braids"
section_number: null
pages: 10-14
source_pdf: amc_2730.pdf
source_sha256: 65730074a2925c6e
doc_brief: "(Also available at http://amc-journal.eu) Braid representatives minimizing the number of simple walks* Hans U. Boden † , Matthew Shimoda ‡ — Given a knot, we develop methods for finding a braid"
---
One of the objectives in this paper is to find braid representations of knots that minimize
the number of simple walks. To do that, we will apply several different operations that
H. U. Boden and M. Shimoda: Braid representatives minimizing the number of simple walks 11
alter the braid word without changing its representative knot. These operations include
reflection, rotation, and cyclic permutation of the braid word, and each of them can be used
to reduce the number of simple walks. We begin with a review of some standard material
on representing knots as braids (see also [5]).
· · ·
β
· · ·
· · ·
α
β
α−1
· · ·
Conjugation
· · ·
β
· · ·
· · ·
β
· · ·
· · ·
β
· · ·
Stabilization
Figure 4: The Markov moves.
Given a braid β, its closure is denoted pβ and is the knot or link obtained by connect-
ing the strands on top with the corresponding strands on bottom without introducing any
additional crossings.
The next result is called Alexander’s theorem and was first proved in 1923, see [1].
Theorem 4.1. Every oriented knot or link is equivalent to the closure pβ for some braid
βPBm.
Definition 4.2. The Markov moves include conjugation and stabilization (see Figure 4).
Given a braid β P Bm, conjugation involves replacing it with αβα´1 for some αP Bm.
Stabilization involves replacing β with either βσm or βσ´1
m . Note that conjugation pre-
serves the braid width and stabilization increases it by one.
The next result is attributed to Markov. For a proof, see [5, Theorem 2.3].
Theorem 4.3. Two braids have equivalent link closures if and only if they are related by a
sequence of Markov moves.
LetβPBm, and let
SWβ“tW |W is a simple walk onβ withJĎt 2,...,m uu (4)
be the set of simple walks on the braidβ.
Given a knot, we are interested in finding the braid representative that minimizes the
number of simple walks. Of course, the set of simple walks depends on the braid represen-
tative chosen. In fact, it depends on the braid word since it is not preserved under insertion
(or deletion) ofσiσ´1
i orσ´1
i σi into the braid word. This is the analogue, for braids, of the
Reidemeister II move. We explain this important point next.
12 Ars Math. Contemp. 23 (2023) #P1.10
Given a walk on a braid, we say that an arc of the braid is active if it is traversed by a
path of the walk. Similarly, we say that a crossing is active if the walk jumps down from
overcrossing arc to undercrossing arc at that crossing. Thus, the active crossings are the
ones with the local weight ai,˘. In Figures 1, 2, and 3, the active arcs are depicted with
zebra stripes.
Now consider two braid words: γ “ αβ and γ1 “ ασiσ´1
i β. (A similar argument
applies toγ1“ασ´1
i σiβ.) We will show thatSWγĎSWγ1.
SupposeW is a simple walk onγ. If both strands i,i ` 1 are active or if they are both
not active, then W extends in a unique way to a simple walk on γ1. If one of the strands
i,i ` 1 is active and the other is not, then W extends to a simple walk on γ1, but possibly
in more than one way. This proves the claim, and in particular, we see that the number of
simple walks is non-decreasing under an elementary insertion.
Recall that a braid word is said to be reduced if it does not contain an occurrence of
σiσ´1
i orσ´1
i σi. By the above considerations, for any given knot, we can always assume
that its braid representative is given by a reduced word.
In a similar way, one can show that the set of simple walks is invariant under far com-
mutativity and the Yang-Baxter relation. For far commutativity, this is straightforward, and
we leave the details to the reader. For the Yang-Baxter relation, consider the braid words
γ“ασiσi`1σiβ andγ1“ασi`1σiσi`1β and assume the relevant crossings arej,j ` 1,
andj` 2.
We claim that any simple walk on γ extends in a unique way to a simple walk on γ1.
There are several cases, depending on which of the three crossingsj,j` 1,j` 2 are active.
If none of the crossings are active, then it extends to a simple walk on γ1. If one of the
crossings is active, and if we make the corresponding crossing on γ1 active, and then it
extends to a simple walk onγ1. If two of the crossings of γ are active, then they must bej
andj`2, and it extends to a simple walk onγ1 again withj andj`2 active crossings. Note
that it is not possible for all three crossings to be active. This shows that|SWγ|“| SWγ1|
under the Yang-Baxter relation.
One can also apply the Markov moves to a braid and consider their effect on the set of
simple walks. For instance, under conjugation, one would expect that the resulting braid
word will have a larger set of simple walks. A special case is cyclic permutation, which
involves replacingβ “ σε1
i1σε2
i2 ¨¨¨ σεℓ
iℓ withβ1 “ σε2
i2 ¨¨¨ σεℓ
iℓσε1
i1. We will study the effect
of cyclic permutation on the set of simple walks in the next section.
Under stabilization, we will show that the set of simple walks is non-decreasing. Let
β P Bm, β1 “ βσ˘1
m P Bm`1, and suppose W is a simple walk on β. If m R J, then
W extends uniquely to a simple walk on β1. If m P J and β1 “ βσm, then we can
extendW to a simple walk on β1 by either making the extra crossing active or by setting
J1“JYtm` 1u. If mPJ andβ1“βσ´1
m , then we can extendW to a simple walk on
β1 withJ1“JYtm` 1u. Notice that forβ1“βσ´1
m , we have one additional simple walk
that does not come fromβ, namely the one withJ“tm` 1u and the extra crossing made
active. In particular, it follows that|SWβ|ď| SWβ1|.
LetK be a knot and suppose β P Bm`1 is a braid representative for K withmě 1.
Ifβ is conjugate to a braid of the form γσ˘
m for some braid γ P Bm, thenβ is said to be
reducible. The braidβ is said to be irreducible if it is not reducible.
The next result summarizes our discussion.
Proposition 4.4. If K is a knot, then any braid representative for K that minimizes the
number of simple walks can be assumed to be given by a reduced and irreducible braid word.
H. U. Boden and M. Shimoda: Braid representatives minimizing the number of simple walks 13
In addition, one can apply symmetry operations to alter the braid word without chang-
ing its knot or link closure. We will use these operations to find braid representatives that
minimize the number of simple walks. The three operations we will consider are called
reflection, rotation, and reversal, and we introduce them next.
For a given braid β, its reflection is denoted β˚ and is obtained by switching all the
crossings of β. If β represents the knot K, then β˚ represents its mirror image K˚. If
β “ σε1
i1 ¨¨¨ σεℓ
iℓ , then its reflection is the braid word given by β˚ “ σ´ε1
i1 ¨¨¨ σ´εℓ
iℓ (see
Figure 5).
For the purposes of computing the colored Jones polynomial, one can use either β or
β˚, since the invariants are related by the simple formula JN,Kpqq “JN,K˚pq´1q. The
two braids will have completely different sets of simple walks. In fact, as we shall see
in the next section, the simple walks on β andβ˚ are disjoint and complementary to one
another. There is an obvious computational advantage to working with the braid having
fewer simple walks.
In fact, there are other symmetries that can be applied to get a new braid representative
for a knot (or its mirror image). For example, given a braid word β representing a knot, if
one rotates it 1800 in the plane, one obtains a new braid word representing the same knot.
Specifically, ifβ “ σε1
i1 ¨¨¨ σεℓ
iℓ , then the rotated braid word is denoted β: and is given by
β:“σεℓ
m´iℓ¨¨¨ σε1
m´i1 (see Figure 5).
Another example is braid reversal, which is given by reversing the order of the braid
word. Again, the new braid represents the same knot. If β“σε1
i1 ¨¨¨ σεℓ
iℓ , then its reversal
is denotedβr and is given by βr “ σεℓ
iℓ ¨¨¨ σε1
i1 (see Figure 5). Notice that βr is the braid
obtained fromβ by rotating it 1800 around a horizontal line in the plane.
There is a one-to-one correspondence between the sets of simple walks on β andβr.
Under the correspondence, the walks have the same set of active crossings, and the weights
for the over- and undercrossingspbi,˘,ci,˘q are switched. In fact, as we shall see, a simple
walk is completely determined by its set of active crossings, and it follows that |SWβ|“
|SWβr|.
β
β∗
β†
βr
Figure 5: A braidβ representing the knot 52 and its reflectionβ˚, rotationβ:, and reversal
βr.
Given a braid word for a knot, applying reflection, rotation, or cyclic permutation will
alter its set of simple walks. Since the computation of the colored Jones polynomial is
exponential in the number of simple walks, it is advantageous to choose the braid represen-
tative that minimizes the number of simple walks.
14 Ars Math. Contemp. 23 (2023) #P1.10
