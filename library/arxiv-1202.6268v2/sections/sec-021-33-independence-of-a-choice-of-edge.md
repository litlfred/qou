---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-021-33-independence-of-a-choice-of-edge
section_title: "Independence of a choice of edge"
section_number: 3.3
pages: 17-18
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.931
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sec.invglue label="sec.invglue"}

We fix $M,\,\mathcal{T},\,\widehat\beta_\mathcal{T}=(z,\mathbf A,\mathbf B,f)$.

In order to choose matrices $\mathbf A,\,\mathbf B$, we must ignore the redundant gluing equation corresponding to an edge of $\mathcal T$. This was discussed in Section [\[sec.NZ\]](#sec.NZ){reference-type="ref" reference="sec.NZ"}. Suppose, then, that we choose a different edge to ignore. For example, if we choose the $(N-1)^{\text{st}}$ rather than the $N^{\text{th}}$ (and keep the same quad type and meridian path), then we obtain new Neumann-Zagier matrices $\widetilde{\mathbf A},\,\widetilde{\mathbf B}$, which are related to the original ones as

$$\widetilde{\mathbf A} =  P_{(N-1,N)}\,\,\mathbf A\,,\qquad \widetilde{\mathbf B} 
=  P_{(N-1,N)}\,\,\mathbf B\,,$$

where

$$P_{(N-1,N)} := \begin{pmatrix} 1 & 0 & \cdots & 0 & 0 & 0 \\
 0 & 1 & \cdots & 0 & 0 & 0 \\
 && \ddots &&&\\
 0 & 0 &\cdots & 1 & 0 & 0 \\
 -1 & -1 & \cdots & -1 & -1 & -1 \\
 0 & 0 & \cdots & 0 & 0 & 1
\end{pmatrix}\,.$$

Similarly, eliminating the $I^{\text{th}}$ rather than the $N^{\text{th}}$ edge constraint is implemented by multiplying with a matrix $P_{(I,N)}$ whose $I^{\rm th}$ row is filled with $-1$'s. Any such matrix satisfies $\det P_{(I,N)}=- 1$.

In the formula for $\tau_{\mathcal{T}}$, only the determinant part is affected by a change of edge. Then

$$\det\big(\widetilde{\mathbf A}\Delta_{z''}+\widetilde{\mathbf B}\Delta_{z}^{-1}\big)
 = \det\big(P_{(I,N)}({\mathbf A}\Delta_{z''}+{\mathbf B}\Delta_{z}^{-1})\big)
 = - \det\big({\mathbf A}\Delta_{z''}+{\mathbf B}\Delta_{z}^{-1}\big)\,,$$

leading to invariance of $\tau_{\mathcal{T}}$, up to the usual sign.
