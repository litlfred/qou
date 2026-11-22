---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-043-a3-lie-algebra-and-associated-group
section_title: "A.3. Lie algebra and associated group"
section_number: null
pages: 38-39
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.927
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
Continue with the notation from the last subsection. For each $N>0$, 
the Poisson bracket induces the structure of a nilpotent  Lie algebra  on the Poisson ideal
\[\fg_{\Delta,\leq N} \subset \bC_{\Delta}[\bT]_{\leq N}\]
consisting of elements of positive height. The Baker-Campbell-Hausdorff formula then gives rise to a unipotent algebraic group $G_{\Delta,\leq N}$ with a bijective exponential map
\[\exp\colon \fg_{\Delta,\leq N} \to G_{\Delta,\leq N}.\]
Taking the limit as $N\to \infty$ we obtain a pro-nilpotent Lie algebra and a pro-unipotent group
related by a bijective exponential map
\[\exp\colon \Hat{\fg}_{\Delta}\to \Hat{G}_{\Delta}.\]

More concretely, the Lie algebra $\Hat{\fg}_\Delta$ consists of formal sums \eqref{lon} of positive height, viewed as a Lie algebra via the Poisson bracket. The group \[\Hat{G}_\Delta=\{\exp(x):x\in \Hat{\fg}_\Delta\},\]
consists of formal symbols $\exp(x)$ for elements $x$ of the Lie algebra. The group structure is  defined using the Baker-Campbell-Hausdorff formula:
\[\exp(x)\cdot \exp(y) = \exp \Big( (x+y)+\frac{1}{2}[x,y]+\cdots \Big).\]
Note that if $\Delta_1\subset \Delta_2$ are nested acute sectors then there is an obvious embedding of Lie algebras ${\fg}_{\Delta_1}\subset {\fg}_{\Delta_2}$, which induces an injective homomorphism $\Hat{G}_{\Delta_1}\into \Hat{G}_{\Delta_2}$ of the corresponding groups. 
We happily confuse elements of $\Hat{G}_{\Delta_1}$ with the corresponding elements of $\Hat{G}_{\Delta_1}$.


 \begin{remark}The Lie algebra $\Hat{\fg}_\Delta$ acts on the algebra $\bC_{\Delta}[[\bT]]$ via Poisson derivations: 
\[x\cdot y = \{x,y\}, \quad x\in \Hat{\fg}_\Delta, \quad y\in \bC_{\Delta}[[\bT]].\]
This exponentiates to give an action of $\Hat{G}_\Delta$ by Poisson automorphisms:
\begin{equation}
\label{rats}\exp(x)\cdot y = \exp \{x, - \} (y), \quad x\in \Hat{\fg}_\Delta, \quad y\in \bC_{\Delta}[[\bT]].\end{equation}
On the left-hand side of \eqref{rats} the symbol $\exp$ is purely formal as discussed above, whereas on the right-hand side it denotes the exponential of the Poisson derivation $\{x,-\}$, viewed as an endomorphism of the vector space $\bC_{\Delta}[[\bT]]$.\end{remark}
