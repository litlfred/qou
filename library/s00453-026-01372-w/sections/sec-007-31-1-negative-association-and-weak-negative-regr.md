---
doc_id: s00453-026-01372-w
doc_title: "Concentration of Submodular Functions and Read-k Families Under Negative Dependence"
section_id: sec-007-31-1-negative-association-and-weak-negative-regr
section_title: "1-Negative Association and Weak Negative Regression"
section_number: 3.1
pages: 7-7
source_pdf: s00453-026-01372-w.pdf
source_sha256: 98b569eff84fb489
toc_source: outline
doc_brief: "Concentration of Submodular Functions and Read-k Families Under Negative Dependence — We study the question of whether submodular functions of random variables satisfying various notions of negative"
---
We ﬁrst deﬁne the weaker notion of negative dependence which we work with, called
1-negative association, and prove some simple properties about it. We also deﬁne a
related notion of weak negative regression, which is the analogue of 1-negative asso-
ciation for the notion of negative regression, and we show the equivalence between
the two for binary random variables and show that weak negative regression is strictly
stronger in general. After an initial draft, we discovered that [1] had already intro-
duced the notion of weak negative regression for binary random variables in a context
complementary to ours. Using their work, we can immediately show nice properties
about 1-negative association.
Deﬁnition 2 A collection of random variables X1, . . . , Xn is said to satisfy 1-negative
association if for any two monotone functions f and g, where g depends on a single
random variable Xi and f depends on the remaining random variables {X j} j∈[n]\{i},
we have E[ f g] ≤E[ f ]E[g].
Deﬁnition 3 A collection of random variables X1, . . . , Xn is said to satisfy weak
negative regression if for any index i and any monotone function f depending on the
remaining random variables {X j} j∈[n]\{i}, we have E[ f |Xi = b] ≤E[ f |Xi = a] for
all a ≤b.
The remainder of the discussion, including proofs and examples illustrating the rela-
tionship between these deﬁnitions, is deferred to Appendix A.
