---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-022-515-more-than-two-mountains
section_title: "More than two mountains"
section_number: 5.1.5
pages: 31-33
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
More than two mountains
To deal with the general case, now we make the following modiﬁcations. We call a summit syllable sequence with
indices n −2 and n −1 terminated on both sides by n −1’s a modiﬁed mountain or plateau. We have again by lemma
5.5 only two valleys of depth < n−2, or alternatively only two plateaus (now instead of mountains). The case of more
than two mountains is thus mainly a adaptation of the case of two mountains, replacing mountains by plateaus.
Again we may assume non-maximal subwords have exactly one (and trivial) syllable per index. The elimination of
the maximal subwords can be done similarly.
We distinguish two cases as in the above study of the 2-mountain words, depending on the depth g of the second valley
(the other valley has depth 1 by the same argument as above).
Case 1. g > 1. We use the previous ﬂyping argument.
Case 2. g = 1. In the second case we had restrictions on exponents of syllables with index 2 and 3 occurring in
the maximal subwords from the position of syllables with index 1 and 2 occurring in the non-maximal subwords.
The restrictions on 2-(index) syllables from 1-(index) syllables remain. So do the restrictions on 3-syllables from
2-syllables unless we have ≤5 strands. The argument is the same: one can still pull out two loops and has at least two
letters of σn−2.
Now we check restrictions on 3-index syllables for 5 strands and reducibility. We have up to extensions a ﬁnite number
of special braids to verify. Clearly, extensions are never admissible for non-summit syllables, and always admissible
for summit index-1-syllables (since they are all non-trivial). Also extensions of subwords (n−2 n−2 n−1)k occurring
repeatedly are redundant, since doubling the letter n −1 is the same as deleting the n −2 n −2 for the next k. We will
verify that the property MWF ≥4 resp. reducibility does not depend on the value of k as soon as k > 0. We will thus
deal only with the other extensions.
Case 2.1. The non-summit 2-index syllable is between two valleys of depth n −2 = 3 - this is handled as before:
[1234334123343211234321] has MWF = 4,
[1234334213343211234321] has MWF = 4,
[1234334233432112314321] has MWF = 4.
Case 2.2. The non-summit 2-index syllable is between one depth n −2 = 3 valley and one depth 1 valley. These are
words of the form [123412(334)k3211234(334)l321],
[123421(334)k3211234(334)l321],
[12342(334)k32112341(334)l321]
for k > 0, l ≥0, and their extensions.
Case 2.2.1. [123412(334)k3211234(334)l321] and extensions.
Case 2.2.1.1. l = 0. To display the extendability of syllables, in the following notation the necessarily trivial syllables
are hatted, while a possibly trivial syllable is underlined.
[1ˆ2ˆ3412(334)k3211ˆ2ˆ3ˆ4321].
32
5
Positivity of 3-braid links
When l = 0, then making non-trivial any single of the hatted syllables makes MWF = 4 already for k = 1, while for
any k > 0 making any combination (possibly all) of the underlined syllables non-trivial gives MWF = 3.
Now again check that braids reduce, for example:
[1234123343343211234321] has MWF = 3,
[12341233433433432111234321] reduces to 3 strands,
[1234441233433433221123433221] reduces to 3 strands.
Case 2.2.1.2. When l = 1, the already for k = 1 we have without extensions [1234123343211234334321] and MWF =
4.
Case 2.2.2. [123421(334)k3211234(334)l321] and extensions.
Case 2.2.2.1. When l = 0, we have for all k the extendability
[12ˆ3421(334)k3ˆ2112ˆ3ˆ43ˆ21],
with the same explanation as before.
For example, [122344213343343343321122343321] reduces to 3 strands.
Case 2.2.2.2. When l ≥1, then already for k = 1 and no extensions MWF([1234213343211234334321])= 4.
Case 2.2.3. [12342(334)k32112341(334)l321] and extensions.
Case 2.2.3.1. When l = 0, we have
[12ˆ342(334)k3211ˆ2ˆ3ˆ413ˆ21].
For example, [122344233433433433221123413321] reduces to 3 strands.
Case 2.2.3.2. When l > 0, already for k = 1, l = 1 without extension we have [1234233432112341334321] and
MWF = 4.
Case 2.3. The non-summit 2-index syllable is between two depth 1 valleys. These are (up to symmetry) words of the
form
[1234(334)k321123421321] and
[12341(334)k32112342321],
for k > 0, and their extensions (here necessarily l = 0).
Case 2.3.1. [1234(334)k32112342132] and extensions:
[1234(334)k3ˆ2112ˆ3ˆ421ˆ3ˆ21].
Again for k = 1 making non-trivial all underlined syllables gives MWF = 3, while making non-trivial any of the hatted
syllables gives MWF = 4.
For example, [1234334321123214321] has MWF = 3, and its extensions
[122333443343211223214321] and
[122334433433433433211223421321]
were checked to reduce to 3 strands.
The same is the outcome for k > 1.
Case 2.3.2. [12341(334)k32112342321] and extensions:
[1ˆ2341(334)k3ˆ2112ˆ3ˆ42ˆ321]
The reducibility cases follow analogously. For example, [123344133433433433211223423221] reduces to 3 strands.
5.1
Positive braid links
33
