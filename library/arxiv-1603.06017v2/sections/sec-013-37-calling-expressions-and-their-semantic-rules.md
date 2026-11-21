---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-013-37-calling-expressions-and-their-semantic-rules
section_title: "Calling Expressions and Their Semantic Rules"
section_number: 3.7
pages: 11-11
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.905
latex_coverage_ratio: 0.925
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:calling expressions}
For an automaton $M$ with $n$ inputs a calling expression is
$\$M(e_1,e_2,\ldots,e_n)$ where the $e_i$ are either arithmetic
expressions or predicates with one free variable. For such an
expression, we say that $M$ is called with arguments
$e_1,e_2,\ldots,e_n$. A calling expression on its own is a valid
predicate, as we will see in Section \ref{sec:relative expressions}.

\begin{DEFN}[semantic rule regarding calling]
Suppose $M$ is the automaton $y_1,y_2,\ldots,y_n: P$ for some predicate
$P$. Suppose expressions $e_1,e_2,\ldots,e_n$ where the $e_i$ are
either arithmetic expressions or predicates with one free variable, and
free variables $x_1,x_2,\ldots,x_m$ occurring in the $e_i$ are given.
Predicate $\$M(e_1,e_2,\cdots,e_n)$ is
satisfied by substitutions $x_k=v_k$ for all $k$, if all of the
following hold:
	\begin{itemize}
		\item If $e_i$ is an arithmetic expression, then $a_i$ is the
		value of $e_i$ when evaluated at $x_k=v_k$ for all $k$.
		\item If $e_i$ is a predicate with one free variable, then it is satisfied by substitutions $x_k=v_k$ for all $k$. Let $a_i$ equals $v_k$ when $x_k$ is the free variable in $e_i$.
		\item $P$ is satisfied by substitutions $y_i=a_i$ for all $i$. 
	\end{itemize}
\end{DEFN}
