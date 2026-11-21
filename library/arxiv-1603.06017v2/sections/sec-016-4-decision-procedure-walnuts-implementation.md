---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-016-4-decision-procedure-walnuts-implementation
section_title: "Decision Procedure: Walnut's Implementation"
section_number: 4
pages: 12-12
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.685
latex_coverage_ratio: 1.0
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:decision procedure}
In this section, we learn about a procedure that takes a predicate and
constructs an automaton accepting that predicate. The procedure
explained here is what implemented in Walnut, and we shall call it the
decision procedure.

For every defined number system, Walnut knows the automata for valid
representations, addition, equality, and less-than
predicates/relations. Every predicate is ultimately built out of these
four predicates using logical operators. So we only need to explain the
construction of automata for complex predicates from automata for
simpler subpredicates. We start by explaining cross product in Section
\ref{sec:cross product}, which is the core object when constructing
automata for predicates formed from binary logical operators, i.e.,
$\&$,$\mid$,$\wedge$,=>,<=>. Then we move on to quantification in
Section \ref{sec:quantification}, explaining the construction of
automata for predicates formed from E and A operators. In Section
\ref{sec:complement and reverse}, we discuss construction of automata
for the complement $\sim$ and reverse \ReverseBlack operators. With
these tools at our disposal, we are on the right track to construct
automata for complex predicates formed from comparison and arithmetic
operators, e.g., $*$,$/$,$>$,<=,etc. which we explain in Section
\ref{sec:arithmetic and comparison}.
