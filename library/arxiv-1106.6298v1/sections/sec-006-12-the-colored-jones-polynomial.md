---
doc_id: arxiv-1106.6298v1
doc_title: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS"
section_id: sec-006-12-the-colored-jones-polynomial
section_title: "The colored Jones polynomial"
section_number: 1.2
pages: 6-6
source_pdf: 1106.6298v1.pdf
source_sha256: 23b0754067873a04
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 1.0
doc_brief: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS — In 2006 Habiro initiated a construction of generating functions for Witten– Reshetikhin–Turaev (WRT) invariants known as uniﬁed WRT invariants."
---
\newcommand{\RR} {\mathbf R}

Suppose L is a framed oriented link with $m$ ordered components and $V_1,\dots,V_m$ are finite-dimensional modules
over a ribbon Hopf algebra. Then one can define the quantum invariant $J_L(V_1,\dots,V_m)$ through the machinery of quantum link invariant theory, see  \cite{Tu}.
The quantized enveloping algebra $U_h(sl_2)$ of $sl_2$ is a ribbon algebra, and
 for each positive integer $n$ there is
a unique $U_h(sl_2)$-module of dimension $n$. The quantum link invariant $J_L(n_1,\dots,n_m)$, where $n_j$ stands for the $n_j$-dimensional $U_h(sl_2)$-module, is usually called
the colored Jones polynomial, with the $n_j$'s being the colors. When all the colors are 2, $J_L(2,\dots,2)$ is the usual Jones polynomial, which can be defined using
skein relation.

One can construct the colored Jones polynomial without the quantum group theory  by first defining the Jones polynomial through the skein relation, and then
defining the colored Jones polynomial by using cablings, see e.g. \cite{KM, Lic}.



Let us recall here a few well--known formulas.
For the unknot $U$ with 0 framing one has
\begin{equation} J_U(n) = [n] \label{unknot}
\end{equation}
Moreover, $J_L$ is multiplicative with respect to the disjoint union.
 If $L_1$ is obtained from $L$
by increasing the framing of the $i$th component by 1, then
\begin{equation}\label{framing}
J_{L_1}(n_1,\dots,n_m) = q^{(n_i^2-1)/4} J_{L}(n_1,\dots,n_m).
\end{equation}
If all the colors $n_i$ are odd, then $J_{L}(n_1,\dots,n_m) \in \Z[q^{\pm 1}]$.
