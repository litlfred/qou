---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-014-38-relative-expressions
section_title: "Relative Expressions"
section_number: 3.8
pages: 11-12
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 1.0
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:relative expressions}
Comparison operators are $=$,!=,$<$,$>$,<=, and >=. A relative expression is any of the following:
\begin{itemize}
\item An expression $e_1 \olessthan e_2$ where $e_1$ and $e_2$ are arithmetic expressions and $\olessthan$ is any comparison operator.
\item An expression $e_1 \olessthan e_2$ where $e_1$ and $e_2$ are indexing expressions and/or alphabetic constants and $\olessthan$ is any comparison operator.
\item A calling expression is a relative expression.
\end{itemize}
We stress that $W[a]=b+2$ is not a relative expression based on the definition above, since $W[a]$ is an indexing expression and $b+2$ is an arithmetic expression. 
We will see shortly that any relative expression is a predicate.
Section \ref{sec:arithmetic and comparison} explains how to construct
automata accepting relative expressions.
