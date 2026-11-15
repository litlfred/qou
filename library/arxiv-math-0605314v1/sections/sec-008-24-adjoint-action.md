---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-008-24-adjoint-action
section_title: "Adjoint action"
section_number: 2.4
pages: 9-9
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.957
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:adjoint-action label="sec:adjoint-action"} Let $\trr\zzzcolon U_h\ho U_h \rightarrow U_h$ denote the (left) adjoint action defined by $$\trr(x\otimes y)=x \trr y = \sum x_{(1)} y S(x_{(2)})$$ for $x,y\in U_h$. We regard $U_h$ as a left $U_h$-module via the adjoint action. Since we have $\Uq\trr\Uq\subset \Uq$, we may regard $\Uq$ as a left $\Uq$-module.

For each homogeneous element $x\in U_h$, we have $$\begin{gathered}
  \label{e17}
  K^i\trr x = q^{i|x|} x\quad \text{for $i\in \modZ $},\\
  \label{e24}
  e^n\trr x =
  \sum_{j=0}^n (-1)^j q^{\hf j(j-1)+j|x|} {\bb nj}_q e^{n-j}x e^j
  \quad \text{for $n\ge 0$},\\
  \label{e64}
  \tF^{(n)}\trr x =
  \sum_{j=0}^n (-1)^j q^{-\hf j(j-1)+j|x|}\tF^{(n-j)}x\tF^{(j)}
  \quad \text{for $n\ge 0$}.
\end{gathered}$$

::: proposition
[]{#thm:19 label="thm:19"} $\Uqv$ is a left $\Uq$-submodule of $\Uq$.
:::

::: proof
*Proof.* It follows from [\[e17\]](#e17){reference-type="eqref" reference="e17"}--[\[e64\]](#e64){reference-type="eqref" reference="e64"} that if $x$ is a homogeneous element of $\Uqv$, then we have $y\trr x\in \Uqv$ for $y=K^i,e^n,\tF^{(n)}$ with $i\in \modZ$, $n\ge 0$. Since these elements generate $\Uq$, we have the assertion. ◻
:::
