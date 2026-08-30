---
doc_id: arxiv-0802.1072v2
doc_title: "A note on closed 3-braids ∗"
section_id: sec-004-the-conjugacy-problem-for-3-braids
section_title: "The conjugacy problem for 3-braids"
section_number: null
pages: 5-6
source_pdf: 0802.1072v2 (1).pdf
source_sha256: 6f4d93f0b7ba5cd7
doc_brief: "A note on closed 3-braids ∗ — This is a review article about knots and links of braid index 3."
---
The conjugacy problem is close-by. The summit set of W , denoted SS( W ), is the subset of those
elements in the conjugacy class of W which, when represented by words in normal form, have
maximal power. It is, by deﬁnition, invariant under conjuga tion by powers of δ. Even more, it
must be ﬁnite, for the following reasons. The deﬁning relati ons in the band presentation preserve
the algebraic sum of the exponents of an element in B3, and conjugation does too. Therefore
the algebraic sum is a class invariant, and from this it follo ws that every time that the power is
increased by conjugation, the tail goes down in letter lengt h, until we reach the summit set. As
for the summit set, it must be ﬁnite because the letter length of the tail of a word in SS( W ) is
ﬁnite and is an invariant. The summit set is Xu’s basic invari ant of the conjugacy class of W .
This was the invariant in Garside’s algorithm in [13], howev er in the special case of B3, using the
band presentation, Xu was able to determine SS( W ) rapidly, and choose a unique symbol Σ ⋆(W )
with the property that two elements W, W ′ are conjugate if and only if Σ ⋆(W ) = Σ ⋆(W ′). Her
unique symbol is deﬁned as follows. Suppose that X = δmal1
i1al2
i2··· alt
it is in the summit set of
W . She associates to X the array Σ( X) = ( m, (l1, l2, . . . , lt)). The integer m is ﬁxed (and is
minimal for the conjugacy class. Her representative Σ ⋆(W ) is chosen so that t is minimal, and
so that among all sequences with the same t it is lexicographically smallest. Thus, for example,
(5, (2, 2)) < (5, (1, 2, 1)) and (5 , (1, 3)) < (5, (2, 2)). She proves that W, W ′∈ B3 are conjugate if
and only if Σ ⋆(W ) = Σ ⋆(W ′). We illustrate the algorithm via an example.
Step 1: The ﬁrst part of the algorithm is to ﬁnd a single element in SS( W ). Let us suppose that
we are given an element W = δqas1
τ1 . . . ast
τt∈ B3, which is in normal form but may or may not be
in its summit set. To test whether W is in SS( W ), we modify W = δqas1
τ1 . . . ast
τt by ‘twisted cyclic
permutation’ of the tail of W . That is, we push the left-most syllable as1
τ1 in the tail to the left,
past δq, using (4) and then move it to the right end of W . This may be achieved by a special kind
of conjugation that we call a tail move on W :
W = δqas1
τ1 . . . ast
τt→ (δqa−s1
τ1 δ−q)(W )(δqas1
τ1 δ−q) = δqas2
τ2··· ast
τt (δqas1
τ1 δ−q) = X.
Xu proves that W is in its summit set if and only if, after a single tail move, th e power is not
increased and the syllable length is not decreased. To under stand why this is so, observe that the
ﬁnal syllable of X is δqas1
τ1 δ−q = as1
j for some j = 1 , 2, 3 and so there are 3 possibilities, namely
j = τt + 1, τt or τt− 1 (mod 3). Xu proves that if j = τt + 1 or τt, then W and also X are in normal
form as written and are in SS( W ). The ﬁrst part of the algorithm ends. For, if X is modiﬁed again
by another tail move, then the modiﬁed X will have the same power as X and be in normal form,
because W was in normal form, so that τ2 = τ1 + 1 (mod 3), and this property is preserved by the
second tail move.
If X is not in normal form, then the only possibility is that j = τt−1, in which case we obtain a new
5
factor δ at the interface between the ﬁnal letter in W and the initial letter in the syllable that was
permuted, because δ = aτtaτt−1. An example is given by W = δ−3a4
1a2a3
3a2
1a2. After a tail move it
changes to X = δ−3(a2a3
3a2
1a2)(a4
1) = δ−3a2a3
3a2
1δa3
1 = δ−2a3a3
1a2
2a3
1, which has higher power than
W . But in this example X is not in normal form, because when the factor δ that appeared after the
tail move was moved to the left, an additional factor δ popped up at the interface between the ﬁnal
two syllables. Pushing the new factor δ to the left, we obtain Y = δ−2a3a3
1a2δa2
1 = δ−1a1a3
2a3a2
1.
The power has been increased again. Normal form has been achi eved, because the subscript array
is increasing.
We now test whether Y in our example is in SS( W ), by applying a tail move. The answer is ‘yes’.
More generally, the process of repeated applications of tai l moves, and passage to normal form,
continues until we ﬁnd an element whose power is unchanged af ter a tail move. In our example
that element is Y and so Y ∈ SS(W ). In a more general example, another cycling might lead to
additional powers of δ, but in the most general example the following holds: If a tai l move does not
change the power, then we have achieved summit power. Note th at the tail move may, nevertheless,
increase syllable length.
Step 2: Having achieved summit power, Xu’s method for choosing an in variant of the conjugacy
class is the following: If Y = δmal1
µ1 . . . alk
µk belongs to SS( W ), one associates to Y its Xu symbol
Σ( Y ) = ( m; (l1, l2, . . . , lk)). In our example, Σ( Y ) = (−1; (1, 3, 1, 2)).
Note that every element in SS( W ) has the same summit power m, but elements need not have
the same syllable length. In particular, if in step 1 it had ha ppened that, after a tail move on
W , we found ourselves in the case j = τt, then the syllable length would go down, because in
X the permuted syllable as1
j could be amalgamated with the ﬁnal syllable ast
τt of W . Among all
elements Y ∈ SS(W ), her deﬁning symbol Σ ⋆(W ) is the one for which the sequence of exponents
(l1, l2, . . . , lk) is lexicographically smallest. In particular, the syllab le length is minimized among
elements in the summit set. It is now easy to see that if a tail m ove leaves both the power and the
syllable length invariant then we are almost done with step 2 .
We study Σ( Y ) = (−1; (1, 3, 1, 2)) in our example. We seek the unique element in SS( W ) for which
the tail symbol is lexicographically smallest. But now obse rve that the candidates are simply the
4 cyclic permutations of the tail symbol, i.e. (1,3,1,2), (3 ,1,2,1), (1,2,1,3). (2,1,3,1). (In a more
general case the tail symbol will have, say, u entries, and so it will have u cyclic permutations,
all of which occur for some element in SS( W ).) In our example Σ ⋆(Y ) = (−1; (1, 2, 1, 3)) is the
Xu invariant of the conjugacy class. We found it without calc ulating the entire summit set, in
particular we ignored all the elements whose syllable lengt h was bigger than 4, and we did not have
t0 deal with the 3 possible subscript sequences of each eleme nt that has this Xu symbol. Therefore
we are done. ‖
