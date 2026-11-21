---
doc_id: arxiv-2507.19896v1
doc_title: "Generalized Markov traces and Jucys-Murphy elements"
section_id: sec-004-iwahori-hecke-algebras
section_title: "Iwahori-Hecke algebras."
section_number: null
pages: 3-3
source_pdf: 2507.19896v1.pdf
source_sha256: a3f23d5a08b397ee
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.96
doc_brief: "Generalized Markov traces and Jucys-Murphy elements — We give a simple construction of Markov traces for Iwahori-Hecke algebras associated with infinite series of crystallographic Coxeter groups."
---
Let $\mathcal{A} = \mathbb{Q}(v)$. The Iwahori-Hecke algebra $\He_v(W,S) = \He(W,S)$ associated to a Coxeter system $(W,S)$ is a unital $\mathcal{A}$-algebra with generators $t_s, s \in S,$ subject to the relations
\begin{enumerate}[label=(\roman*).,ref=(\roman*)]
\item $\langle t_{s_i},t_{s_j}\rangle_{m_{ij}} = \langle t_{s_j},t_{s_i}\rangle_{m_{ij}}$, where $\langle x,y \rangle_{m}$ is an alternating product $xyx\dots$ of $x$ and $y$ with $m$ factors.
\item \label{item:1} $(t_s - v)(t_s + v^{-1}) = 0.$
\end{enumerate}
When $(W,S)$ is of type $B_n$ we will also be interested in the Iwahori-Hecke algebra $\He_{v,v_0}(W,S)$ with unequal parameters $v, v_0 \in \mathcal{A}$. This is a unital algebra over the ring $\mathcal{A}$, with the relation \ref{item:1} replaced by the relations
\begin{enumerate}[]
\item[(ii\textquotesingle).] $(t_{s_i} - v)(t_{s_i} + v^{-1}) = 0$ for $i > 1$,
\item[(ii\textquotesingle\textquotesingle).] $(t_{s_i} - v_0)(t_{s_i} + v_{0}^{-1}) = 0$.
\end{enumerate}


When $(W,S)$ is of type $X_n$ with $X \in \{A, B=C, D\}$, we will write $W(X_n)$ and $\He(X_n)$ for $W$ and $\He(W,S)$, or $\He_{v,v_0}(B_n)$ if we need to emphasize that we use unequal parameters. In each of these cases, we will write $t_i$ for $t_{s_i}$.

Let $w = s_{i_1}\dots s_{i_r}, w \in W, s_{i_k} \in S$ be a reduced expression. Then the element $t_w = t_{s_{i_1}}\dots t_{s_{i_r}}$ in $\He(W,S)$ is independent of the choice of a reduced expression, and $\He(W,S)$ is a free $\mathcal{A}$-module with a basis $t_w, w \in W$. The elements $t_w$ are invertible, and the collection $t_{w}^{-1}, w \in W,$ gives another basis of $\He(W,S)$ over $\mathcal{A}$.
