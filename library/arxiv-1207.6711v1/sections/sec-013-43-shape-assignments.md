---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-013-43-shape-assignments
section_title: "Shape assignments"
section_number: 4.3
pages: 9-10
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.903
latex_coverage_ratio: 0.873
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
We now introduce the generalized shape parameters. We will need to replace the traditional labeling of the shape parameters $z^\prime$ and $z^{\prime\prime}$ by a notation, which better exhibits the symmetry and naturally allows for a unified treatment of the gluing equations for all $n\geq 2$. 


\begin{definition}\label{def:Subsimplex}
A \emph{subsimplex} of $\Delta^3_n$ is a subset $S$ of $\Delta^3_n$ obtained by translating $\Delta^3_2\subset\R^4$ by an element $s$ in $\Delta^3_{n-2}(\Z)\subset\Z^4$, i.e.~$S=s+\Delta^3_2$.
\end{definition}

Fix $n\geq 2$. 
We wish to assign shape parameters to each edge of each subsimplex. Note that the set of all these edges is naturally parameterized by the set $\Delta^3_{n-2}(\Z)\times\dot{\Delta}^3_2(\Z)$, the first coordinate being the subsimplex, and the second coordinate the edge. 


\begin{definition}\label{shapeassignment}
A shape assignment on $\Delta^3_n$ is an assignment 
\begin{equation}
z\colon\Delta^3_{n-2}(\Z)\times \dot{\Delta}^3_2(\Z)\to\C\setminus\{0,1\}, \qquad (s,e)\mapsto z^e_s
\end{equation}
satisfying the \emph{shape parameter relations}
\begin{subequations}
\label{eqn:shapeparamrel}
\begin{align}
z^{0011}_s&=z^{1100}_s=\frac{1}{1-z^{0101}_s}\label{shapepar1}\\
z^{0110}_s&=z^{1001}_s=\frac{1}{1-z^{0011}_s}\label{shapepar2}\\
z^{0101}_s&=z^{1010}_s=\frac{1}{1-z^{0110}_s}\label{shapepar3}.
\end{align}
\end{subequations}

\end{definition}





\begin{remark}When $n=2$, there is only a single subsimplex indexed by $s=0000$, so $\Delta^3_{n-2}(\Z)\times\dot{\Delta}^3_2(\Z)\cong \dot{\Delta}^3_2(\Z)$ parametrizes the edges of a simplex. Since the shape parameters in \eqref{eqn:shapeParms} satisfy $$z=\frac{1}{1-z''},\qquad z'=\frac{1}{1-z},\qquad z''=\frac{1}{1-z'},$$  Definition \ref{shapeassignment} generalizes Thurston's shape assignments. The new notation relates to that of Thurston as follows:
$$z=z_s^{0011}=z_s^{1100},\qquad z^\prime=z_s^{0110}=z_s^{1001}, \qquad z''=z_s^{0101}=z_s^{1010}.$$
\end{remark}
