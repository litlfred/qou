---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-015-38-relative-expressions
section_title: "Relative Expressions"
section_number: 3.8
pages: 11-12
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
Comparison operators are =,!=,<,>,<=, and >=. A relative expression is any of the following:
• An expression e1 <e2 where e1 and e2 are arithmetic expressions and < is any comparison operator.
• An expression e1 <e2 where e1 and e2 are indexing expressions and/or alphabetic constants and < is any comparison
operator.
• A calling expression is a relative expression.
We stress that W [a] = b +2 is not a relative expression based on the deﬁnition above, since W [a] is an indexing expression
and b +2 is an arithmetic expression. We will see shortly that any relative expression is a predicate. Section 4.4 explains how
to construct automata accepting relative expressions.
11
3.9
Predicates
A predicate is an expression formed from relative expressions and logical operators:
• Every relative expression is a predicate.
• For every predicate P all of (P), ∼(P) and `(P) are predicates.
• For every predicate P1 and P2 all of P1 &P2, P1 | P2, P1 ∧P2, P1 => P2, P1 <=> P2 are predicates.
• For every predicate P and free variables x1,x2,...,xn both of Ex1,x2,...,xn P and Ax1,x2,...,xn P are predicates.
The semantic rules with which we assign true and false values to predicates deﬁned here can be obtained by adding the
semantic rules for indexing and calling to the well-known semantics of ﬁrst-order logic and Presburger arithmetic.
Walnut provides two commands for converting predicates to automata accepting them: eval and def; see Sections 7.1
and 7.2, respectively.
4
Decision Procedure: Walnut’s Implementation
In this section, we learn about a procedure that takes a predicate and constructs an automaton accepting that predicate. The
procedure explained here is what implemented in Walnut, and we shall call it the decision procedure.
For every deﬁned number system, Walnut knows the automata for valid representations, addition, equality, and less-than
predicates/relations. Every predicate is ultimately built out of these four predicates using logical operators. So we only
need to explain the construction of automata for complex predicates from automata for simpler subpredicates. We start by
