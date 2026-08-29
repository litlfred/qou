---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-036-512-maximal-subwords
section_title: "Maximal subwords"
section_number: 5.1.2
pages: 27-28
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Here we start the technical considerations needed to prove theorem 5.1. We consider the form (9), now with allli > 0.
Deﬁnition 5.1 We deﬁne summit syllables in (9):
a) All σli
n−1 are summit syllables, and
b) if α = σli
k and α′ = σ
l j
k are summit syllables, with no σl′
k′ for k′ ≥ k occurring between α and α′, then all σl′
k−1
occurring between α and α′ are summit syllables.
Note that, according to deﬁnition 2.1, we consider syllable s in cyclic order. The relation “between” in the above
deﬁnition should also be understood in that sense: a syllabl e occurring after the last index i syllable α and/or before
the ﬁrst index i syllable α′ is considered to be between α and α′.
For the following considerations it is (not necessary but) helpful to visualize β by the braid scheme explained in [St6].
Separate β in (9) into subwords α1 . . .αn, such that αi contains only syllables of odd or even index, and this parity
changes between αi and αi+1. Then for a syllable σl
k occurring in αi, put the integer l at the point (k,i) ∈ N × N ⊂ R2
in the plane. Here (k,i) is the point in the i-th row and k-th column, with rows numbered (as in Cartesian coordinates)
from bottom to top and columns from left to right.
One obtains a certain checkerboard pattern of integers we ca ll braid scheme of β. (If we do not put any integer on a
point (k,i), we assume its “content” is zero, or it is “empty”. So for all non-empty points (k,i) in the scheme, i + k is
always even or always odd.)
One can reduce the scheme by moving an integer l at (k,i) to (k,i − 2) if i > 2 and the points (k ± 1,i − 1) are empty.
We call the scheme reduced if it does not admit any such move. T hen in a reduced scheme, summit syllables of β
are those, whose entries in the scheme are “on top” when viewing the scheme from the left. From this viewangle the
following “geographic” choice of terminology becomes moreplausible.
Deﬁnition 5.2 Summit syllables still have a cyclic order from (9). We call the subword β′ of β in (9) made of summit
syllables the maximal subword. The subword made of non-summit syllables (i.e. the subword obtained by deleting in
β all syllables in β′) is called non-maximal subword.
Note that neighbored summit syllables have indiceski differing by ±1. We say that a summit syllable isminimal resp.
maximal if its both neighbors have higher resp. lower index.
We call β summit reduced if all its minimal summit syllables are non-trivial. We call β index reduced if it is non-
singular and its index sum ∑ n
i=1 ki · li cannot be reduced by a Yang-Baxter relation, i.e. β contains no σi+1σiσi+1 as
subword.
Lemma 5.1 Index reduced =⇒ summit reduced. In particular a summit reduced form always exists. ✷
Recall that a positive resolution tree is a rooted tree with directed edges, whose vertices (nodes) contain positive braid
words, the root labelled by β. Every vertex has exactly one incoming edge, except the root that has none, and zero
or two outoutgoing edges. In former case it is labelled by an u nlink (terminal node). In latter case it is labelled by a
word of the form ασ2
i α′, with α,α′ positive words, and the two vertices connected by the outgoing edges are labelled
by ασiα′ and αα′, or positive words obtained therefrom by Markov equivalence (isotopy of the closure link).
In [Na] the following fact was observed, and used decisively, and we shall do the same here.
28 5 Positivity of 3-braid links
Theorem 5.2 (Nakamura [Na]) MW F(β) is the maximal number of components of a (link in a) node in a po sitive
resolution tree for β.
In particular, MW F is monotonous (does not decrease) under word extension, anddoes not depend on the exponent of
non-trivial syllables.
Lemma 5.2 If β is summit reduced, and β′ is obtained from β by removing all summit syllables, then there is a positive
resolution tree for β that contains β′ as a node.
Proof. Since minimal syllables are non-trivial, one can delete the m in the resolution tree. The two neighbors in the
maximal subword join to a non-trivial new minimal syllable, and so one iterates the procedure. ✷
Since all σl′
n−1, σl′
n−2 in (9) occur as summit syllables, β′ has split last two strands, and so we have a quick proof of
Nakamura’s main result.
Corollary 5.3 (Nakamura [Na]) Any summit reduced positive word on n ≥ 3 strands has MW F ≥ 3. ✷
In particular any positive braid representation of a (2,n)-torus link can be reduced to the standard one by index-
decreasing YB relations and removals of nugatory crossings.
