---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-006-33-variables
section_title: "Variables"
section_number: 3.3
pages: 8-8
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
---
(quantiﬁed). For example P3 has no free variables, and can be regarded as a constant, in this case it is always true.
We have seen that, given a predicate P, for any ordering x1,x2,...,xn of free variables and for every assignment of number
systems S1,S2,...,Sn to those variables, there exists an automaton M accepting such a predicate, i.e., a tuple of same length
words t = (w1,w2,...,wn) is accepted by M if and only if the substitutions xi = [wi]Si satisfy P.
For example, consider the predicate P1. The automaton in Figure 2.1 accepts P1. Furthermore there exists automaton M
accepting tuples (x, y) for which |x| = |y| and substitutions a = [y]msd_2, and b = [x]msd_2 are satisfying P1. There also exists
an automaton N accepting tuples (x, y) for which |x| = |y| and substitutions a = [x]msd_ﬁb and b = [y]lsd_2 are satisfying P1.
By deﬁnition, both M and N also accept the predicate P1.
We would like to annotate predicates so that they contain information on number systems without ambiguity (we will
see how shortly). For such an annotated predicate P and the ordering x1,x2,...,xn on free variables, there exists a unique
minimized automaton accepting the predicate. We denote this unique automaton by
(x1,x2,...,xn) : P.
The ordering we ﬁx on variables, in Walnut and throughout this article, is the lexicographic ordering on the variables’
name.
The following are examples of annotated predicates5:
• P′
1 := ?msd_2 a = 4&b = 5
• P′
2 := ?msd_ﬁb a = b +c
From the annotated predicate P′
1 we understand that a,b,4,5 should all be interpreted in msd_2 and = should be interpreted
as =msd_2. Hence (a,b) : P′
1 is the automaton accepting msd_2 representations of 4 and 5 as its ﬁrst and second inputs
respectively. Also from annotation ?msd_ﬁb in P′
2 it is clear what to expect from automaton (a,b,c) : P′
2.
We can annotate a predicate with multiple number systems, e.g., see Figure 2.9. Here are the rules with which we assign
