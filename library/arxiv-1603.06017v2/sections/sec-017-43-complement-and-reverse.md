---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-017-43-complement-and-reverse
section_title: "Complement and Reverse"
section_number: 4.3
pages: 15-16
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
To obtain (x1,...,xm) :∼(P) from (x1,...,xm) : P, one has to add all transitions to dead state (in Walnut, we call this totalizing
an automaton), and then switching ﬁnal and non-ﬁnal states, but one also has to make sure that the resulting automaton
is intersected with the automaton accepting RS1 ×···×RSm where Si is the number system assigned to xi in (annotated)
predicate P. (Recall that RS is the set of all valid representations in the number system S. Also recall that to deﬁne and use a
number system in Walnut, one has to provide automaton accepting the set of all representations in that number system,
therefore automaton accepting RS1 ×···×RSm could be constructed easily using cross product explained in Section 4.1.)
Take a look at automaton (a) : ?msd_ﬁb a = 1 depicted in Figure 4.8 that accept words representing 1 in msd_ﬁb.
Now to obtain (a) :∼(?msd_ﬁb a = 1), we ﬁrst add the dead state and all the transitions to it:
8This is an automaton with multiple initial states. One can show that for every nondeterministic automaton with multiple initial states, there is an
equivalent automaton with only one initial state.
15
Figure 4.8: Number 1 in Fibonacci
Figure 4.9: Totalized automaton
Switching ﬁnal and non-ﬁnal states we obtain an automaton accepting {0,1}∗\0∗1:
Figure 4.10: Switching ﬁnal and non-ﬁnal states
But then this automaton accepts words that have consecutive 1’s which are not acceptable Fibonacci representations. So
to get the ﬁnal answer we have to intersect this automaton with the one depicted in Figure 2.6. The result is depicted in 4.11.
Figure 4.11: Automata accepting all numbers in Fibonacci except 1
The reverse operator is not a logical operator per se, but we include it because it is useful when working with automata.
The operand of the reverse operator is an automaton 9. The result is an automaton with all its transitions reversed.
4.4
