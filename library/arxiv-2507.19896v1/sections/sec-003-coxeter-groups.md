---
doc_id: arxiv-2507.19896v1
doc_title: "Generalized Markov traces and Jucys-Murphy elements"
section_id: sec-003-coxeter-groups
section_title: "Coxeter groups."
section_number: null
pages: 2-3
source_pdf: 2507.19896v1.pdf
source_sha256: a3f23d5a08b397ee
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.985
doc_brief: "Generalized Markov traces and Jucys-Murphy elements — We give a simple construction of Markov traces for Iwahori-Hecke algebras associated with infinite series of crystallographic Coxeter groups."
---
Let $(W, S), S = \{s_1, \dots, s_n\},$ be a Coxeter system. Thus, $W$ is a group with a presentation $(s_0, \dots, s_n | (s_is_j)^{m_{ij}} = e)$, where $m_{ij} \in \mathbb{Z}^+ \cup \{\infty\}$, with $m_{ii} = 1, m_{ji} = m_{ij} \geq 2$ if $i \neq j$, and $m_{ij} = \infty$ means that there is no relation included for the pair $s_i, s_j$. Such a presentation is read off the Coxeter diagram of $(W,S)$ in a standard way: such a diagram is a non-oriented graph with $S$ as a set of vertices, and $m_{ij} - 2$ edges between the vertices $s_i$ and $s_j$. Let $l: W \to \mathbb{Z}_{\geq 0}$ be the Bruhat length function with respect to $S$.

We will be primarily interested in Coxeter groups that are Weyl groups of classical types $A, B = C, D$. To fix the numeration of the generators, their Coxeter diagrams are presented below, with a vertex corresponding to $s_i \in S$ marked by $i$. The Coxeter diagram of type $A_n$ is \[\dynkin[arrows=false, edge length=0.6cm, backwards, labels={n,n-1,2,1}]A{},\] of type $B_n = C_n$ is
\[
  \dynkin[arrows=false, edge length=0.6cm, backwards, labels={n-1,,,1,0}]B{},
\]
and of type $D_n$ is 
\[
\dynkin[arrows=false, edge length=0.6cm, backwards, labels={n-1,,,2,1,1'}]D{}.
\]
When $n$ is small, these are interpreted in a standard way as follows: the Coxeter system $A_1 = B_1 = D_1$ has a single vertex, $D_2 = A_1 \times A_1$, $D_3 = A_3$. We also adopt the convention $A_0 = B_0 = D_0$ corresponding to the empty Coxeter graph and the trivial Coxeter group.

Many of the results and definitions in this paper are valid in types all types $A, B, D$, with definitions for type $A_{n-1}$ naturally fitting with definitions in types $B_n, D_n$. In this case, we will write ``type $X_n$, where $X$ is $A_{-1}$, $B$ or $D$'' (or something in a similar vein).
