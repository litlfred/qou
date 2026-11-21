---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-010-34-operators
section_title: "Operators"
section_number: 3.4
pages: 9-10
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 1.0
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:operators}
The full list of operators allowed in predicates can be found in Table
\ref{tab:operators}\footnote{we prefer this notation to those familiar
from mathematical logic, because we want to liken our notation to those
of programming languages, as Walnut is ultimately a programming
language.}. This list has operator precedences. The lower this number
is, the higher the precedence is. For example, multiplication by constant
has the highest precedence. Parentheses override all precedences. All
operators are associative from left to right, except for complement
$\sim$, reverse \ReverseBlack, quantifiers E and A, calling \$, and
indexing $[]$ which are all associative from right to left.

\begin{table}[h]
	\centering
	\begin{tabular}{ | m{1.7cm} | m{1.4cm}| m{4cm} | m{5cm}|} 
		\hline
		precedence & operator & explanation & examples\\
		\hline
		1 & $*$ & multiplication by a constant & $2*x$ and $x*2$ \\ 
		\hline
		1 & $/$ & division by a constant & $x/2$ but not $2/x$\\ 
		\hline
		2 & $+$& addition & \\ 
		\hline
		2 & $-$& subtraction & \\
		\hline
		3 &   $=$ & equality& \\
		\hline
		3 &  !=  & inequality& \\
		\hline
		3 &  $<$ & less than& \\
		\hline
		3 &  $>$  & greater than& \\
		\hline
		3 & <= & less than or equal& \\
		\hline
		3 &  >= & greater than or equal& \\
		\hline
		4 &  $\sim$  & complement&\\
		\hline
		4 &   \ReverseBlack  & reverse&\\
		\hline
		5 &  $\&$ & conjunction&\\
		\hline
		5 &  $\mid$  & disjunction&\\
		\hline
		5 &  $\wedge$ & exclusive disjunction&\\
		\hline
		6 &  => & implication&\\
		\hline
		7 & <=> & equivalence&\\
		\hline
		8 &   E  & existential quantifier & $\text{E}x,y,z$ or $\text{E}x\text{ E}y\text{ E}z$\\
		\hline
		8 &   A & universal quantifier & $\text{A}x,y,z$ or $\text{A}x\text{ A}y\text{ A}z$\\
		\hline
		9 & $\$$ & calling &$\$\text{M}(x,y)$ \\
		\hline
		9 & $[]$ & indexing & $T[i+j]$\\
		\hline
	\end{tabular}
	\caption{List of operators in Walnut}
	\label{tab:operators}
\end{table}
