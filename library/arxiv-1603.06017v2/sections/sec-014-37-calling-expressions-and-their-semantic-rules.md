---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-014-37-calling-expressions-and-their-semantic-rules
section_title: "Calling Expressions and Their Semantic Rules"
section_number: 3.7
pages: 11-11
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
For an automaton M with n inputs a calling expression is $M(e1,e2,...,en) where the ei are either arithmetic expressions
or predicates with one free variable. For such an expression, we say that M is called with arguments e1,e2,...,en. A calling
expression on its own is a valid predicate, as we will see in Section 3.8.
Deﬁnition 5 (semantic rule regarding calling). Suppose M is the automaton y1, y2,..., yn : P for some predicate P. Suppose
expressions e1,e2,...,en where the ei are either arithmetic expressions or predicates with one free variable, and free variables
x1,x2,...,xm occurring in the ei are given. Predicate $M(e1,e2,··· ,en) is satisﬁed by substitutions xk = vk for all k, if all of
the following hold:
• If ei is an arithmetic expression, then ai is the value of ei when evaluated at xk = vk for all k.
• If ei is a predicate with one free variable, then it is satisﬁed by substitutions xk = vk for all k. Let ai equals vk when xk
is the free variable in ei.
• P is satisﬁed by substitutions yi = ai for all i.
3.8
