---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-034-511-the-morton-williams-franks-bound
section_title: "The Morton-Williams-Franks bound"
section_number: 5.1.1
pages: 26-27
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
For the proof of theorem 1.3 we will need to study the behaviou r of the bound (11) in the Morton-Williams-Franks
inequality (we abbreviate as MWF) on positive braids. This w as begun by Nakamura [Na], who settled the case
MW F = 2 in the suggestive way: such braids represent only the (2,n)-torus links. (The case MW F = 1 is trivial.) We
will introduce a method that considerably simpliﬁes his pro of (but still makes use of some of his ideas), and then go
on to deal with MW F = 3. The example of non-sharp MWF inequality, 13 9365 in [HT] (the connected 2-cable of the
trefoil), given in [MS], is in fact only among a small family of exceptional cases.
Theorem 5.1 If b(ˆβ) > MW F(ˆβ) = 3, then β reduces to a 4-braid, and is given by one of the following form s (as-
suming that 3∗ denotes a sequence of at least one letter 3, and 11∗ resp. 22∗ sequences of at least two letters 1 or 2):
[22 ∗ 3 ∗ 122 ∗ 11 ∗ 23211∗], and [22 ∗ 3122 ∗ 11 ∗ 23 ∗ 211∗].
We will reduce the proof to a ﬁnite number of words to check, which is done by calculation using the program of [MS].
Since a direct computation is more reliable than an increasingly difﬁcult mathematical argument, we have not tried to
minimize the calculation by all means. However, we point out that for the sake of theorem 1.3 alone (rather than its
reﬁnement, theorem 5.1), the following weaker statement is sufﬁcient, for which a considerable part of the case-by-
case calculations can be dropped. This corollary requires t he notion of semiadequacy [LT], and can be deduced from
theorem 5.1 by direct check of the exceptional words. (We will sometimes write MWF (β) for MW F(ˆβ).)
Corollary 5.1 If β is a positive braid word, andMW F(β) = 3, then β reduces (up to Markov equivalence) to a positive
4-braid word β′, and the diagram ˆβ′ is not B-adequate.
Here the notions of A-adequate and B-adequate for diagrams and braids are as explained in §2.2 and §2.5. We note, as
a consequence of [Th], that a braid is (A/B-)adequate if and only if some, or equivalently any, minimallength word of
a braid in its conjugacy class it is so.
We will thus prove theorem 1.3 only using corollary 5.1, and indicate in the proof of theorem 5.1 the point where the
corollary follows (and the rest of the argument is not needed). The argument that elegantly replaces the remaining case-
by-case checks requires theorem 4.5. Since (by taking again the full extent of our proof) theorem 4.5 is nonetheless
not indispensable, we permit ourselves to defer its proof to a separate paper [St4].
Proof of theorem 1.3. If MWF (β) ≤ 2, then we are done. So assumeMW F(β) = 3. Assume ﬁrst L has an A-adequate
3-braid. Since A-adequate diagrams minimize the number of negative crossings, and L has a positive (braid) diagram,
the A-adequate 3-braid diagram is positive, and we are done. So le t L have a B-adequate 3-braid diagram ˆβ′. Now by
corollary 5.1, we ﬁnd that L reduces to a positive 4-braid β with c+(β) positive crossings, and β is not B-adequate.
Since β′ is B-adequate and B-adequate diagrams minimize the number of positive crossings, c+(β′) < c+(β). On the
other hand, MW F(L) = 3 and the inequalities of MWF for the v-degree of P show that β′ must have exponent sum
[β′] = c+(β) − 1. Since [β′] ≤ c+(β′), we must have equality, so β′ is positive. ✷
Note the following easy and useful consequence of theorem 1.3:
Corollary 5.2 A link which is a closure of a positive braid of at most 4 string s, has a minimal crossing diagram as a
closed positive braid, and a minimal string positive braid representation.
Proof. The case of the braid representation is straightforward, and it implies the minimal crossing diagram statement
by looking at maxdeg z P and using Morton’s inequalities. ✷
The examples in [St3], mentioned after theorem 1.3, show tha t the corollary is not true in case of positive 5-braids at
least for the positive minimal braid representation. So far no examples are known where no minimal crossing positive
