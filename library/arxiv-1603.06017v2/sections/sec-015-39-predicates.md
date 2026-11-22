---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-015-39-predicates
section_title: "Predicates"
section_number: 3.9
pages: 12-12
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 1.0
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:predicates}
A predicate is an expression formed from relative expressions and logical operators:
\begin{itemize}
\item Every relative expression is a predicate.
\item For every predicate $P$ all of $(P)$, ${\sim (P)}$ and ${\text{\textasciigrave}(P)}$ are predicates. 
\item For every predicate $P_1$ and $P_2$ all of $P_1 \mathbin{\&} P_2$, $P_1 \mid P_2$, $P_1 \wedge P_2$, $P_1 \mathbin{\text{ => }} P_2$, $P_1 \mathbin{\text{ <=> }} P_2$ are predicates.
\item For every predicate $P$ and free variables $x_1,x_2,\ldots,x_n$ both of $\text{E}x_1,x_2,\ldots,x_n\text{ }P$ and $\text{A}x_1,x_2,\ldots,x_n\text{ }P$ are predicates.
\end{itemize}
The semantic rules with which we assign true and false values to
predicates defined here can be obtained by adding the semantic rules
for indexing and calling to the well-known semantics of first-order
logic and Presburger arithmetic.

Walnut provides two commands for converting predicates to automata
accepting them: eval and def; see Sections \ref{sec:eval} and
\ref{sec:def}, respectively.
