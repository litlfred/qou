---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-019-45-calling-an-automaton
section_title: "Calling an Automaton"
section_number: 4.5
pages: 17-18
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
In Section 3.7, we learned about the syntax and semantic of calling an automaton. A calling expression is a kind of syntactic
sugar to save some space when writing long and complicated predicates. Suppose we already have computed the automaton
(x1,x2,...,xn) : P and given it the name M. We can refer to P in a predicate P′ without writing P all over again, by just
17
writing $M(e1,e2,...,en), where $ symbol is to signify that M is an automaton, and the ei are either arithmetic expressions or
predicates with exactly one free variable. In such case, we say, predicate P′ is calling M (or is calling predicate P).
To construct automaton for $M(e1,e2,...,en), Walnut constructs the equivalent automaton:
Ex1,x2,...,xn P &(x1 = e′
1)&(x2 = e′
2)&···&(xn = e′
n)&(e j1)&(e j2)&...&(e jk )
where x1,x2,...,xn are the free variables in P, k is the number of predicates in e1,e2,...,en, j1, j2,..., jk are indices of
predicates among e1,e2,...,en, and if e j is an arithmetic expression, then e′
j = e j , otherwise e j is a predicate, and e′
j is the
free variable occurring in e j .
The fact that this predicate is equivalent to $M(e1,e2,...,en) could be obtained easily using the semantic rule explained
in Section 3.7. Walnut’s implementation includes some considerations to improve efﬁciency. For example, obviously when
e j is a variable, we do not need to introduce a new variable x j .
Calling an automaton inside a predicate P′ is also more efﬁcient than copying P over and over again in P′. This is
because Walnut does not need to construct M every time we write $M in P′.
The commands def and eval in Walnut are responsible for constructing the automaton M from predicate P. Unlike eval,
the command def saves the automaton M so it can be called later from other predicates like P′. See Section 7.2 for more
information on def command.
To see an example, let M be the automaton (a,b) : a +b = 10, and let Q be the predicate $M(x, y)& y = 8. The automaton
in Figure 4.14 accepts Q.
Figure 4.14: Automaton accepting Q
Please refer to Section 7.2, which is devoted to examples of calling automata.
When calling an automaton M, one has to make sure that the j’th argument is in the same number system as j’th input
in M for all j.
4.6
