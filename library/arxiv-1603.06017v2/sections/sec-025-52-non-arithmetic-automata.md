---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-025-52-non-arithmetic-automata
section_title: "Non-arithmetic Automata"
section_number: 5.2
pages: 19-20
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:non-arithmetic automata}
There is a need for automata in which inputs (or some of them) do not
represent numbers in a specific number system. These automata might
accept patterns, or they might be relying on some non-arithmetic
instructions.

For example, the pattern $0^*10^*$ represents powers of $2$ in
$\MSD[2]$. However, the same pattern represents powers of $2$ in
$\LSD[2]$. Therefore, by not assigning a number system to the automaton
$M$ accepting the pattern $0^*10^*$, we are allowed to call $M$ both in
predicates in $\MSD[2]$ and in predicates in $\LSD[2]$. Assigning
number systems to automata accepting patterns usually does not make
much sense. See more examples in Section \ref{sec:reg}.

Allowing non-arithmetic automata is specially helpful when working with
the class of paperfolding words. These words are defined with an
automaton that takes two inputs. One input is a number that represents
a position in the paperfolding word and the other input is folding
instruction that does not represent numbers. To see how Walnut can be
used to prove properties of paperfolding words see
\cite{paperfolding}.
