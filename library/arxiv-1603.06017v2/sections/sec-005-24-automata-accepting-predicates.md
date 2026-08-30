---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-005-24-automata-accepting-predicates
section_title: "Automata accepting Predicates"
section_number: 2.4
pages: 7-8
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
In Walnut, we are interested in automaton M accepting same-length representations in number systems S1,S2,...,Sn of
integers x1,x2,...,xn satisfying some predicate P. When this is the case we say that automaton M accepts the predicate P
(or equivalentlyM accepts relation R of tuples satisfying P). We already saw a few examples of such automata in Figures
2.1–2.6. From [1], also see [8], and as it will be proved again in Section 4, for predicate P in Presburger arithmetic such
an automaton always exists. Presburger arithmetic is the ﬁrst-order theory of natural numbers, in which predicates are
consisted of constants (natural numbers), variables over natural numbers, existential quantiﬁers, universal quantiﬁers,
logical operators (conjunction, disjunction, negation, exclusive disjunction, implication, equivalence), arithmetic operators
(addition, subtraction, multiplication and division by constants), and comparison operators (equality, less than, greater than,
less than or equal, greater than or equal)4.
You can ﬁnd the list of all operators in table 3.1. This list has three operators, namely, reverse ` ,indexing [], and calling $,
that are not allowed in Presburger arithmetic. By indexing we mean indexing into an automatic word, e.g., writing things
like W [i + j] = W [i +n + j]; see Section 3.6 for more details. In [9],[4],[8], and also in Section 4.6 we learn that extending
Presburger arithmetic to include indexing is still decidable. In Section 3.7 we learn about calling and in Section 4.5 we learn
that it is just a syntactic sugar and does not add to the power of the extended Presburger arithmetic (one that includes
indexing into automatic words). We learn about reverse operation in Section 4.3. From here on, by “predicate” we mean a
predicate over this extended Presburger arithmetic (extended to include indexing into automatic words) and until we see the
proof in Section 4, we accept the fact that there exist automata accepting such predicates.
In Section 3 we formally deﬁne what constitutes a predicate, but ﬁrst let us see a few examples:
• P1 := a = 4&b = 5
• P2 := a = b +c
4Presburger arithmetic in its formal deﬁnition recognizes only a minimal subset of constants and operators: 0,1,+,=,<,∀, but it is not difﬁcult to show
that all the other objects and operators we mentioned, e.g., multiplication by constants, does not add to the power of Presburger arithmetic and can be
derived from that minimal set of objects. See Section 3.2 for more details. One thing to note here is that subtraction a −b exists only when there exists a
non-negative number c for which b +c = a.
7
• P3 := Ax Ey x = 2∗y | x = 2∗y +1
• P4 := T [i + j] = T [i +n + j]
