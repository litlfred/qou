---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-019-31-example-41-continued
section_title: "Example: 41 continued"
section_number: 3.1
pages: 16-16
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.85
latex_coverage_ratio: 1.0
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sub.torexample label="sub.torexample"}

To illustrate the Definition [\[torintro\]](#torintro){reference-type="ref" reference="torintro"}, consider the figure-eight knot complement again. From Section [\[sec.41triang\]](#sec.41triang){reference-type="ref" reference="sec.41triang"}, we already have one possible choice for the Neumann-Zagier matrices [\[NZ41\]](#NZ41){reference-type="eqref" reference="NZ41"} and a generic flattening [\[flat41\]](#flat41){reference-type="eqref" reference="flat41"}. We use them to obtain

$$\begin{aligned}
\pm\tau_{\mathbf{4_1}} &= \frac12 \det\left[\begin{pmatrix} 2 & 2 \\ 1 & 1 
\end{pmatrix}\begin{pmatrix} z'' & 0 \\ 0 & w'' \end{pmatrix} 
+ \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} z^{-1} & 0 
\\ 0 & w^{-1} \end{pmatrix}\right] w''{}^{-1} \notag \\
&= \frac1{2w''}\det\begin{pmatrix} 2z''+z^{-1} & 2w''+w^{-1}
\\ z''+z^{-1} & w'' \end{pmatrix} \notag \\
&= \frac1{2w''}\det\begin{pmatrix} z''+1 & w''+1\\ 1 & w'' 
\end{pmatrix} \notag\\ 
&=\frac12(z''-w''{}^{-1}) = \frac12{\sqrt{-3}}\,, \label{tor41}
\end{aligned}$$

where at intermediate steps we used $z''+z^{-1}-1=w''+w^{-1}-1=0$, and at the end we substituted the discrete faithful solution $z=z''=w=w''=e^{i\pi/3}$.

The invariant $\tau_{\mathbf{4_1}}$ belongs to the invariant trace field $E_{\mathbf{4_1}} = \mathbb{Q}(\sqrt{-3})$, and agrees with the torsion of the figure-eight knot complement [@DFJ].
