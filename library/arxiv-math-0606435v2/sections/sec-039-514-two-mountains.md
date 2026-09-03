---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-039-514-two-mountains
section_title: "Two mountains"
section_number: 5.1.4
pages: 29-31
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
(2,n)-torus connected component, or a reducible braid and can work by induction on the number of strands. Similarly
at least one valley has depth 1, otherwise σ1 in β′ remains reducible in β.
The following operation will be somewhat important, and we will call it “ﬁlling the valley”.
Lemma 5.3 (“ﬁlling the valley”) Any valley can be removed from the maxi mal subword in the positive resolution
tree.
Proof. Same as for lemma 5.2. ✷
Lemma 5.4 If a mountain M is not of maximal height (i.e. n − 1), then MW F(β) ≥ 4.
Proof. Let k < n − 1 be the height of M. We assumed there are at least two mountains of maximal heigh t. So
now w.l.o.g. assume some, say the left, of the neighbored mou ntains of M has height k′ > k. Fill the two valleys
around M starting with σk−1. Then the maximal subword has a syllable index sequence k + 1,k,k − 1,k,k − 1,k.
Make the second and third syllable trivial (if not already), and apply YB relations, moving the fourth syllable to the
left: k + 1,k − 1,k,k − 1(,k − 1),k. The result is a summit reduced word, in which a new syllable o f index k − 1
(the underlined one) was removed and it became non-maximal. Hence the non-maximal subword has exponent sum
[β′]k−1 > 1, and so MW F ≥ 4. ✷
Lemma 5.5 If β has > 2 valleys of depth at most n − 3, then MW F(β) ≥ 4.
Proof. It sufﬁces to check for 3 mountains (as one can ﬁll separate va lleys) and 4-braids (as one can ﬁll valleys by
levels as in the proof of lemma 5.2 and the remark after theore m 5.3). This is just the word [1232112321121321],
which is easily checked (to have MW F = 4). ✷
5.1.4. Two mountains
We assume in §5.1.4 and §5.1.5 that n ≥ 5. The case of 4-braids is considered later in §5.1.6. We refer to §2.4 for the
use of notation we will employ.
We assume ﬁrst β has two mountains. By the previous remarks they are both of height n − 1.
So now consider words with syllable index sequence
1,2, . . . ,n − 2,n − 1, p1@, . . . ,pk@, n − 2,n − 3, . . .,g + 1,g!,
g + 1, . . . ,n − 2,n − 1, q1@, . . . ,ql@, n − 2,n − 3, . . .,2,1(33)
such that l + k = n − 3 and {p1, . . . ,pk,q1, . . . ,ql} = {1, . . . ,n − 3}. We will distinguish only between non-trivial and
trivial syllables (in former case exponent is immaterial). For non-trivial syllables we write an exclamation mark after
the index, for trivial ones an ‘at’ (@) sign. If none of ! and @ is speciﬁed, we do not exclude explicitly any of either
types. We write β1, . . . ,β6 for the subwords separated by space in (33).
Assume w.l.o.g. (up to reversing the braid’s orientation) that some pi is 1, and let up to commutativity the p1, . . . ,pk
subword be written as h,h − 1, . . .,1,p′
1, . . . ,p′
k−h (the p′
i contain the indices above h occurring as pi).
Assume the maximal syllable of σh+1 in β1 is non-trivial. Then one can write β as word with a subword of index
sequence
1, . . . ,h + 1!,h@, . . . ,1@ .(34)
30 5 Positivity of 3-braid links
If now h < n − 3, we can make in (34) all syllables trivial except h + 1, which we make of exponent 2, then split a
loop (component of a link in a node of a positive resolution tr ee) by removing all the syllables in (34) together with
the terminating ‘1’ in (33). We obtain
h + 2, . . .,n − 2,n − 1, p′
1@, . . . ,p′
k−h@, n − 2,n − 3, . . .,g + 1,g!,
g + 1, . . .,n − 2,n − 1, q1@, . . . ,ql@, n − 2,n − 3, . . .,2.
(Here no syllables of index 1 occur, and the split loop is the i solated leftmost strand.) Then we ﬁll the valley starting
with the index-n − 1-summits, splitting another loop (the rightmost strand),
h + 2, . . . ,n − 3,n − 2, p′
1@, . . . ,p′
k−h@, q1@, . . . ,ql@, n − 2,n − 3, . . .,2,
and are left with a word that has at least two σn−2. So MW F ≥ 4.
Case 1. Assume the smaller valley has depth g > 1. The β has two index-1 syllables, a trivial (non-summit) and a
non-trivial (summit) one. By a ﬂype one can exchange them, an d so have a non-summit reduced word. Then one can
change β to a word of smaller index sum, and so we are done by induction.
Case 2. Now g = 1. We write β1, . . . ,β6 for the 6 subwords separated by spacing in (33). By a similar a rgument as
after (34) we can argue that if one can reorder the syllables in β2,5 so that β has a subword with an index sequence
k,k + 1, . . . ,h − 1,h!,h − 1, . . .,k ,(35)
with the ﬁrst or last h − k syllables belonging to β2,5 and the others to β1,3,4,6, and h < n − 2, then MW F ≥ 4.
W.l.o.g. assume 1 ∈ β5 (which is meant to abbreviate that β5 contains an index-1 syllable).
Case 2.1. Now if 2 ⁄∈β5 (so 2 ∈ β2) then the 2-index syllables in β4,6 are trivial (because we have otherwise (35) with
k = 1, h = 2).
We distinguish several cases by the subwords of (non-summit ) syllables of index 1 ,2 and 3 in β2,5. We separate the
subwords between β2 and β5 by a vertical line ‘|’. (We assume here that n ≥ 6. The case n = 5 must be handled by a
separate, but simpliﬁed, argument.) Note that by symmetrie s we can exchange the words of 1 ,2 and 3 left and right
from ‘|’ and also (simultaneously) reverse both, and can also use the commutativity of 1 and 3. Then we are left with
the following cases.
Case 2.1.1. 2|31. If 3 ∈ β5, then both 3 in β1,3 are trivial. (Otherwise, we would have (35) fork = 2 and h = 3.) Below
we give pairs of words, the ﬁrst obtained by extending all adm issible syllables to be non-trivial, and the second one
by extending the ﬁrst word to one with knot closure, which was then checked to reduce (by at least one strand, not
necessarily to a 3 braid).
[11223442556655443221112334455344166554433211],
[112223442555665544432211123344553441666554433211] reduces.
Case 2.1.2. If 3 ∈ β2, then one of both 3-index syllables in β1,3 must be trivial. (It is the syllable in β3 if ‘3’ occurs
before ‘2’ inβ2, or the syllable in β1 otherwise.)
Case 2.1.2.1. 23|1.
[112234423556655443322111233445544166554433211],
[112234423556665554443322111233445544166554433211] reduces.
Case 2.1.2.2. 32|1
[112233443255665544322111233445544166554433211],
[112233444325556665544322111233445544166554433211] reduces.
Case 2.2. Now assume 2 ∈ β5. Since 1 ∈ β5, now the exclusion of (35) shows that only one of the 2-index s yllables
in β4,6 is trivial, but we will show that also one in β1,3 is. Namely, by making the proper index-1 (summit) syllable to
exponent 2, and one of the 2-index syllables ofβ1,3 trivial, one can slide by braid relations the 1-index syllable σ1 = X
from β5 to β2. By applying the previous argument, both 2-index syllables in (the now modiﬁed) β1,3 are trivial. One
of them was previously made trivial to slide X in, but the condition on the other one persists for the original braid.
In all situations, make all the other syllables in β1,3,4,6 non-trivial and check using KnotScape that the braid reduces.
