---
doc_id: arxiv-2501.03424v1
doc_title: "Soergel bimodules and Kazhdan-Lusztig polynomials"
section_id: sec-000-coxeter-systems-hecke-algebras-and-kazhdan-luszt
section_title: "Coxeter Systems, Hecke algebras, and Kazhdan-Lusztig preliminaries"
section_number: null
pages: 4-4
source_pdf: 2501.03424v1.pdf
source_sha256: 53e00a30fd850a5b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.881
doc_brief: "Soergel bimodules and Kazhdan-Lusztig polynomials — This paper presents an exposition of Soergel bimodules, the categoriﬁcation of Hecke alge- bras, and their applications to various topics in"
---
\end{center}

\subsection{Coxeter Systems}

Suppose $W$ is a group, and $S \subset W$ is a finite subset consisting of generators of $W.$ Let $(m_{st})_{s,t \in S}$ be a matrix satisfying 
$$m_{st} = m_{ts} \in \{1,2,\ldots\} \cup \{\infty\} $$ with $m_{ss} = 1$ for every $s \in S$. We say that the pair $(W,S)$ is a \textit{Coxeter system}, and $W$ a \textit{Coxeter group}, if $W$ admits the presentation 
$$W = \langle s \in S \st (st)^{m_{st}} = e \text{ for any } s,t \in S, m_{st} < \infty\rangle,$$
where $e$ denotes the identity element in $W$. It turns out that the value $m_{st}$ is the order of the element $st \in W$, and, if $m_{st}$ is not finite, no correlation exists between $s$ and $t$. One will often see generators $s \in S$ submitted to the condition that it is involutive, i.e. $s^2 = e$. These generators are sometimes called reflections, and so it may not be a surprise that
