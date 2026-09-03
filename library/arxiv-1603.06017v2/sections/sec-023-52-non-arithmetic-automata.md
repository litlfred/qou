---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-023-52-non-arithmetic-automata
section_title: "Non-arithmetic Automata"
section_number: 5.2
pages: 19-20
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
There is a need for automata in which inputs (or some of them) do not represent numbers in a speciﬁc number system.
These automata might accept patterns, or they might be relying on some non-arithmetic instructions.
For example, the pattern 0∗10∗represents powers of 2 in msd_2. However, the same pattern represents powers of 2 in
lsd_2. Therefore, by not assigning a number system to the automaton M accepting the pattern 0∗10∗, we are allowed to call
M both in predicates in msd_2 and in predicates in lsd_2. Assigning number systems to automata accepting patterns usually
does not make much sense. See more examples in Section 7.5.
Allowing non-arithmetic automata is specially helpful when working with the class of paperfolding words. These words
are deﬁned with an automaton that takes two inputs. One input is a number that represents a position in the paperfolding
word and the other input is folding instruction that does not represent numbers. To see how Walnut can be used to prove
properties of paperfolding words see [10].
19
6
