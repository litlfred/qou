---
doc_id: arxiv-2501.03424v1
doc_title: "Soergel bimodules and Kazhdan-Lusztig polynomials ethan eugene wynner"
section_id: sec-014-theorem
section_title: "Theorem"
section_number: null
pages: 12-13
source_pdf: 2501.03424v1.pdf
source_sha256: 53e00a30fd850a5b
doc_brief: "Soergel bimodules and Kazhdan-Lusztig polynomials ethan eugene wynner — This paper presents an exposition of Soergel bimodules, the categ oriﬁcation of Hecke alge- bras, and their applications to"
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.959
---
\textit{If $\Hom(M_\mu, M_\eta) = 1,$ then there exists a dominant weight $\lambda \in \h^*$ and $x,y \in W$ such that}
$$\mu = x \cdot \lambda, \eta = y \cdot \lambda,$$
with $x \ge y$ in Bruhat order. This brings us our seminal conjecture, stated as follows.



\subsubsection{The Kazhdan-Lusztig conjecture}

\textit{ For every $x,y \in W,$ the following holds:}
$$[M_{(y\cdot 0)} : L_{(x \cdot 0)}] = h_{y,x}(1).$$

This conjecture is the focal application of Soergel bimodules. In the near future, we will cover this in more depth. Kazhdan and Lusztig also proved the following formula, the 


\subsubsection{Kazhdan-Lusztig Inversion Formula}
Let $w_0 \in W$ be the longest eleemnt. For every $x,y \in W,$ we have the identity
$$\sum_{z \in W}(-1)^{l(y) + l(x)}h_{z,x}(v)h_{zw_0, yw_0}(v) = \begin{cases}
    1 \text{ if } x = y \\
    0 \text{ else}
\end{cases}$$

Along with the previous conjecture, this implies a similar identity in the Grothendieck group of $\mathcal{O}$:

$$[L_{(y\cdot 0)}] = \sum_{y \le x}(-1)^{l(y) + l(x)}h_{xw_0, yw_0}(1)[M_{(x\cdot 0)}].$$

At this point, we might find ourselves asking some questions about what exactly Kazhdan-Lusztig polynomials are. To try shedding some light, we turn to the following theorem of of Polo \ref{ref11}, stating roughly that any polynomial with positive coefficients is a Kazhdan-Lusztig polynomial in some symmetric group.
