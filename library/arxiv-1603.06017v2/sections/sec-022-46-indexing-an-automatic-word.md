---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-022-46-indexing-an-automatic-word
section_title: "Indexing an Automatic Word"
section_number: 4.6
pages: 18-19
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:indexing to an automatic word}

Suppose $W$ is an $n$-dimensional automatic word and
$M\big(Q,q_0,O,\delta,\Sigma,\mathbf{S_1},\mathbf{S_2},\ldots,\mathbf{S_n}\big)$
is its corresponding automaton with output. Also let $\alpha$ be an
alphabetic constant. We note that $(x_1,x_2,\ldots,x_n):
W[x_1][x_2]\cdots[x_n]=@\alpha$ is the automaton
$$\big(Q,q_0,F,\delta,\mathbf{S_1},\mathbf{S_2},\ldots,\mathbf{S_n}\big)$$
when minimized, where $F=\big\{q:O(q)=\alpha\big\}$. Similar arguments
can be made for other comparison operators.

Suppose $W_1$ and $W_2$ are $m$- and $n$-dimensional automatic words, respectively, and let $M_1$ and $M_2$ be their corresponding automata with output. We note that $(x_1,x_2,\ldots,x_m,y_1,y_2,\ldots,y_n): W_1[x_1][x_2]\cdots[x_m]=W_2[y_1][y_2]\cdots[y_n]$
is  $(M_1\times M_2)(F)$ when minimized, where $F$ contains all $(q_1,q_2)$ where $q_1$ and $q_2$ are states of $M_1$ and $M_2$, respectively, and they have the same output. Similar arguments can be made for other comparison operators.

The above statements can be proved easily using the semantic rule
explained in Section \ref{sec:indexing expressions}. Now what if
indices are arithmetic expressions and/or predicates with one free
variable? The construction is based on substitutions similar to the
ones mentioned for calling expressions in Section \ref{sec:calling an
automaton}.
