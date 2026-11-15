---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-012-36-indexing-expressions-and-their-semantic-rules
section_title: "Indexing Expressions and Their Semantic Rules"
section_number: 3.6
pages: 11-11
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.973
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:indexing expressions}
For an $n$-dimensional automatic word $W$, an indexing expression is
$W[e_1][e_2]\cdots[e_n]$ where the $e_i$ are either arithmetic
expressions or predicates with one free variable.

An indexing expression on its own is not a valid predicate, and it is
not meaningful to talk about automata accepting indexing expressions.
Smallest predicates involving indexing expressions are defined in
Section \ref{sec:relative expressions} and they involve comparison
operators.

We use indexing expressions to refer to positions indicated by $e_i$.
The semantic of predicates involving indexing expressions can be
derived from the following rule:

\begin{DEFN}[semantic rule regarding indexing]
Suppose automatic word $W$, expressions $e_1,e_2,\ldots,e_n$ where 
the $e_i$ are either arithmetic expressions or predicates with one free variable, free variables $x_1,x_2,\ldots,x_m$ occurring in the $e_i$, and an alphabetic constant $\alpha$ are given. Predicate $W[e_1][e_2]\cdots[e_n]=@\alpha$ is satisfied by substitutions $x_k=v_k$ for all $k$, if all of the following hold:
\begin{itemize}
\item If $e_i$ is an arithmetic expression, then $a_i$ is the value of the
$e_i$ when evaluated at $x_k=v_k$ for all $k$.
\item If $e_i$ is a predicate with one free variable, then it is satisfied by substitutions $x_k=v_k$ for all $k$. Let $a_i$ equals $v_k$ when $x_k$ is the free variable in $e_i$.
\item The symbol $W[a_1][a_2]\ldots[a_n]$ equals $\alpha$.
\end{itemize}
\end{DEFN}

Having this rule, coming up with similar rules for other comparison
operators, e.g., $W[e_1][e_2]\cdots[e_n]<@\alpha$, and even predicates
involving comparison of two automatic words, e.g.,
$W_1[e_1][e_2]\cdots[e_m]\text{>=}W_2[e'_1][e'_2]\cdots[e'_n]$, should
be straightforward. Recall that alphabetic constants are ordered just
like integers.
