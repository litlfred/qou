---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-011-41-simplex-coordinates
section_title: "Simplex coordinates"
section_number: 4.1
pages: 9-9
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.774
latex_coverage_ratio: 1.0
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
We identify each simplex of a concrete triangulation $\T$ with the ordered simplex 
\begin{equation}
\Delta^3_n = \left\{(x_0,x_1,x_2,x_3) \in \R^4\bigm\vert 0\leq x_i \leq n, x_0 + x_1 + x_2 + x_3 = n\right\}.
\end{equation}
By removing the four vertices, we obtain the ideal standard simplex
$\dot{\Delta}^3_n$.
Consider the sets
$$\Delta^3_n(\Z)=\Delta^3_n\cap \Z^4,\qquad \dot{\Delta}^3_n(\Z)=\dot{\Delta}^3_n\cap\Z^4,\quad\mbox{and}\quad \Delta^3_n(\Z_+)=\Delta^3_n\cap\Z_+^4$$
of integral points, non-vertex integral points, and integral points lying entirely inside the simplex. A simple counting argument shows that 
\begin{equation}\label{eq:Counting}
\left|\Delta^3_n(\Z)\right| = \binom{n+3}{3},\quad \big|\dot{\Delta}^3_n(\Z)\big| = \binom{n+3}{3}-4,\quad\mbox{and}\quad \left|\Delta^3_n(\Z_+)\right| = \binom{n-1}{3}.
\end{equation}
Note that $\dot{\Delta}^3_2(\Z)$ consists of the edge midpoints of $\Delta^3_2$ and thus naturally parametrize the undirected edges.

When convenient, we abbreviate tuples by dropping the parenthesis and the commas, e.g., we write 1010 instead of $(1,0,1,0)$. Note that the indices of an edge and its opposite edge add up to $1111$. 

\begin{figure}
\begin{center}
\includegraphics{figures_gen/SubSimplices_included}
\end{center}
\caption{Subsimplices and shape parameters for $n=8$.}
\end{figure}
