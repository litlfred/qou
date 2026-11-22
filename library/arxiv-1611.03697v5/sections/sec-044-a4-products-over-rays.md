---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-044-a4-products-over-rays
section_title: "A.4. Products over rays"
section_number: null
pages: 39-40
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.918
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
Let  $(\Gamma, Z, \Omega)$ be a BPS structure.  Recall the notion of the height of a ray from Section \ref{raydiagram}. Let us now also fix an acute sector $\Delta\subset \bC$.
The support property ensures that for any ray $\ell\subset \Delta$ the expression
\[\DT(\ell)=-\hspace{-.8em}\sum_{\gamma\in \Gamma: Z(\gamma)\in \ell} \DT(\gamma) \cdot x_\gamma\in \bC_\Delta[[\bT]]\]
defines an element of the Lie algebra $\Hat{\fg}_\Delta$. By definition, its height is equal to $\height(\ell)$. We denote the corresponding group element by
\[\bS(\ell)^*=\exp \DT(\ell)\in \Hat{G}_\Delta.\]

Given $N>0$, we can  consider the  truncation
\[\bS(\ell)^*_{<N}=\exp \DT(\ell)_{<N} \in \Hat{G}_{\Delta,<N}.\]
This element is non-trivial only for the finitely many rays of height $<N$. Therefore, we can form the finite clockwise product
\begin{equation}
\label{fin}\bS(\Delta)^*_{<N}=\prod_{\ell\subset \Delta} \;\bS(\ell)_{<N} \in \Hat{G}_{\Delta,<N}.\end{equation}
Taking the limit  $N\to \infty$ then gives a well-defined element 
\begin{equation}
\label{late}\bS(\Delta)^*=\prod_{\ell\subset \Delta} \;\bS(\ell)^* \in \Hat{G}_{\Delta}.\end{equation}
The product on the right hand side will usually be infinite.
