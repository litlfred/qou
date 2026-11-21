---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-011-35-arithmetic-expressions
section_title: "Arithmetic Expressions"
section_number: 3.5
pages: 10-11
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 1.0
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:arithmetic expressions}
The permissible arithmetic operators are $+,-,*,/$. Equality $=$ is {\it not\/}
an arithmetic operator. A constant expression is an expression
involving only constants and arithmetic operators that evaluates to a
natural number, e.g., $4,3+2,6/4,2*3$ but not $-3$ nor $2-3$.  An
arithmetic expression is defined recursively in the usual way:

\begin{itemize}
\item A constant expression is an arithmetic expression, e.g., $2$,$10$,$7-4$, but not $-1$.
\item A variable is an arithmetic expression, e.g., $x,y,z$,etc.
\item For arithmetic expression $e$, the expression $(e)$ is also arithmetic.
\item For arithmetic expression $e_1$ and $e_2$ both of $e_1+e_2$ and $e_1-e_2$ are arithmetic expressions.
\item For variable $x$ and constant expression $c$ all of $x*c$,$c*x$, and $x/c$ are arithmetic expressions.
\item For arithmetic expression $e$ and constant expression $c$ all of $(e)*c$, $c*(e)$, and $(e)/c$ are arithmetic expressions. 
\end{itemize}
An arithmetic expression on its own is not a predicate, and it is not
meaningful to talk about an automaton accepting an arithmetic
expression. For example, talking about an automaton accepting $x+y+z=0$
makes sense, while talking about an automaton accepting $x+y+z$ is not
meaningful.  Walnut reports an error if the user tries to construct an
automaton for an arithmetic expression.

See Section \ref{sec:arithmetic and comparison} to see how Walnut
constructs automaton for valid predicates like $$(y_1 \otimes y_2
\otimes \cdots \otimes y_m) \olessthan (x_1 \otimes x_2 \otimes \cdots
\otimes x_n),$$ where the $x_i$ and $y_j$ are variables or arithmetic
constants, $\otimes$ are arithmetic operators, and $\olessthan$ is a
comparison operator.
