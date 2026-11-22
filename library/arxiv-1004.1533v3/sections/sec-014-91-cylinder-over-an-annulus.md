---
doc_id: arxiv-1004.1533v3
doc_title: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT"
section_id: sec-014-91-cylinder-over-an-annulus
section_title: "Cylinder over an annulus"
section_number: 9.1
pages: 34-36
source_pdf: 1004.1533v3.pdf
source_sha256: 95c1544431e6bf37
toc_source: outline
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 0.75
doc_brief: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT — In this paper we show how one can extend Turaev-Viro invariants, deﬁned for an arbitrary spherical fusion category C, to 3-manifolds with cor- ners."
---
\label{s:computations1}


Let $F=S^1\times I\times I$ be the cylinder over an annulus, as shown
below. 

\tzCylinderI
 
Then 
$$
\del F=C_a\cup C_b \cup C_{in}\cup C_{out} \cup C\cup \ov{C}
$$
where $C_a, C_b$ are the left and right annuli, $C_{in}$ and $C_{out}$ are
the inner and outer cylinders, and $C$ is the internal cell:
\begin{align*}
&C_a=\tzCL
\qquad
C_b=\tzCR\\
&C_{in}=\tzCin
\qquad
C_{out}=\tzCout
\qquad
C=\tzC
\end{align*}


The pullback of the cell decomposition of $\del F\simeq S^2$ to the sphere
is homeomorphic to the cube shown below:
$$
\tzCube
$$

Drawing the dual graph, we see that given a collection 
\begin{align*}
 &\psi_L\in H(\ov{C_a})=\<A,X_k, (A')^*, X_k^*\>,\qquad 
 \psi_R\in H(\ov{C_b})=\<B_1^*,X_l, B', X_l^*\>\\
 &\psi_{in} \in H(\ov{C_{in}})=\<A^*,X_i, B, X_i^*\>,\qquad 
 \psi_{out}\in H(\ov{C_{out}})=\<A',X_j, (B')^*, X_j^*\>\\
 &\ph\in H(C)=\<X_l,X_j^*,X_k^*,X_j\>,\qquad 
 \ph'\in H(\ov{C})=\<X_j^*,X_k,X_j,X_l^*\>,
\end{align*}
the value $(Z(F),\psi_L\otimes \psi_R\otimes
\psi_{in}\otimes\psi_{out}\otimes\ph\otimes\ph')$ is given by
the following graph:
$$
\tzDualGraphCylII
$$
