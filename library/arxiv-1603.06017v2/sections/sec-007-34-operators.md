---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-007-34-operators
section_title: "Operators"
section_number: 3.4
pages: 8-9
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
• If ?S appears inside a pair of parentheses or brackets, then the number system S is effective from the place it occurs in
the predicate to the nearest closing parenthesis or bracket6.
• If ?S appears outside all parentheses and brackets, then the number system S is effective from the place it occurs in the
predicate to the end of predicate.
• If none of the rules above applies, the number system is assumed to be msd_2 by default.
• It is assumed that the number systems do not contradict each other, i.e., a single variable cannot have two different
number systems in one predicate, and all operands of an arithmetic or comparison operator must belong to the same
number system.
We saw in Figure 2.1, the unique automaton (a,b) : P′
1. In Figure 2.8, we see the automaton (a,b) : a = 4&b = 13 (recall
that when the number system is not speciﬁed it is assumed to be msd_2):
Figure 2.8: The automaton accepting a = 4&b = 13, does not accept all representations of 4
5Names for variables, words, and automata in Walnut start with a letter and can contain alphanumerics and underscores. So to distinguish number
system annotations in a predicate we use the preﬁx ?.
6Brackets [] only appear in indexing expressions. See Sections 3 and 3.6 for more details.
8
Note how this automaton fails to accept t = (100,w2) for any w2. This is obviously due to the fact that 13 does not have
a representation of length 3 in msd_2. So we stress again that when we say automaton M accepts predicate P, we mean
that M accepts all (tuples of) equal length representations of x1,...,xn satisfying P. Therefore this example conforms to the
deﬁnition.
Let us see an example of an automaton having multiple number systems.
Figure 2.9 depicts the automaton
(a,b) : a = 1&(?lsd_2 b = 1).
Figure 2.9: Automaton accepting a = 1&(?lsd_2 b = 1)
3
