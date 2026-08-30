---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-022-51-true-and-false-automata
section_title: "True and False Automata"
section_number: 5.1
pages: 19-19
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
In Section 2.4 we saw an example of a predicate with no free variables:
Ax Ey x = 2∗y | x = 2∗y +1
This predicate evaluates to true (it is a tautology). Here is an example of a predicate with no free variable that evaluates to
false (contradiction):
Ex x > x +1
Walnut assigns a special automaton called true (false) automaton to predicates with no free variable that evaluate to true
(false). However there could be predicates with free variables that are converted to true or false automata. See the following
conventions implemented in Walnut:
• Conjunction (disjunction) of true automaton with automaton M yields M (true automaton, respectively).
• Conjunction (disjunction) of false automaton with automaton M yields false automaton (M, respectively).
• Negation of true automaton is false automaton and vice versa.
• Conventions for other logical operators follow from the above.
These conventions are reﬂecting the following facts from mathematical logic (for a predicate P):
• P &true and P | true are equivalent to P and true respectively.
• P &false and P | false are equivalent to false and P respectively.
• ∼true = false and ∼false = true.
As an example, the automaton (y) : (Ax x < x +1)& y = 2 is exactly the same as automaton (y) : y = 2. As another example, the
automaton (y) : (Ex x < 0)& y = 2 is the false automaton. As in our last example, note that ∼(Ex x < 0) is the true automaton.
Figures 5.1 and 5.2 show the special way Walnut represents true and false automata.
Figure 5.1: True automaton
Figure 5.2: False automaton
5.2
