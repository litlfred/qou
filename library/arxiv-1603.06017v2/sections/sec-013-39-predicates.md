---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-013-39-predicates
section_title: "Predicates"
section_number: 3.9
pages: 11-11
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
---
An indexing expression on its own is not a valid predicate, and it is not meaningful to talk about automata accepting
indexing expressions. Smallest predicates involving indexing expressions are deﬁned in Section 3.8 and they involve
comparison operators.
We use indexing expressions to refer to positions indicated by ei. The semantic of predicates involving indexing
expressions can be derived from the following rule:
Deﬁnition 4 (semantic rule regarding indexing). Suppose automatic word W , expressions e1,e2,...,en where the ei are
either arithmetic expressions or predicates with one free variable, free variables x1,x2,...,xm occurring in the ei, and an
alphabetic constant α are given. Predicate W [e1][e2]···[en] = @α is satisﬁed by substitutions xk = vk for all k, if all of the
following hold:
• If ei is an arithmetic expression, then ai is the value of the ei when evaluated at xk = vk for all k.
• If ei is a predicate with one free variable, then it is satisﬁed by substitutions xk = vk for all k. Let ai equals vk when xk
is the free variable in ei.
• The symbol W [a1][a2]...[an] equals α.
Having this rule, coming up with similar rules for other comparison operators, e.g., W [e1][e2]···[en] < @α, and even pred-
icates involving comparison of two automatic words, e.g., W1[e1][e2]···[em]>=W2[e′
1][e′
2]···[e′
n], should be straightforward.
Recall that alphabetic constants are ordered just like integers.
