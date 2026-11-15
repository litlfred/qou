---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-023-112-trefoil-complement
section_title: "Trefoil complement"
section_number: 11.2
pages: 35-36
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.879
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
\label{trefoil_ex}

The right-handed trefoil complement (`L103001' in SnapPy) has a 
2-tetrahedron triangulation $\T$ with gluing equation/holonomy coefficients 
given by:
$$
\begin{bmatrix} 1 & 2 & 2 & 2 & 1 & 2 \\ 1 & 0 & 0 & 0&1&0\\
0 & 0 & -1 & 1 & 0 & 0\\ 1 & 0 & -4 & 4 & -1 & 0
\end{bmatrix}
$$

Hence, summing over edge 2, the 3D-index is
\begin{align*}
I_\T(x \mu + y \lambda) &= \sum_{k \in \Z} \JD(k+y,0,-x-4y)\JD(x+4y,k-y,0) \\
&=\sum_k q^k \ID(x+4y,k+y)(-q^{1/2})^{-x-4y}\ID(x+4y,k-x-5y) \\
&= \sum_{k'} q^{k'} (-q^{1/2})^{-x-6y} \ID(m,k') \ID(m,k'-x-6y) \\
&= \sum (-q^{1/2})^{-x-6y} \delta_{0,-x-6y} = \delta_{0,x+6y}.
\end{align*}
where we put $k'=k+y$ and $m=x+4y$ and used the quadratic identity.

Note that $I_\T(\gamma)$ is non-trivial exactly when $\gamma$ is a multiple of
the boundary curve $-6\mu+\lambda$ of the essential annulus 
(and M\"obius strip) in the trefoil knot exterior.


\subsection{$\bf{T^2 \times I}$}  
\label{t2xI_ex}

There is a unique triangulation of $T^2 \times I$ with 3 tetrahedra. 
Regina's isomorphism signature of the triangulation is `dLQacccbjkg'. This 
triangulation turns out to be 1-efficient and has the following 
gluing equation/holonomy coefficients (from SnapPy):

$$
\begin{bmatrix} 
1 &   2 &   2 &   1 &   1 &   1 &   1 &   1 &   1\\
1 &   0 &   0 &   0 &   0 &   0 &   0 &   0 &   0\\
 0 &   0 &   0 &   1 &   1 &   1 &   1 &   1 &   1\\
0 &   0 &   0 &   0 &   0 &   1 &   1 &   0 &   0\\
-1 &   0 &   0 &   0 &   1 &   0 &   0 &   0 &   1\\
0 &   0 &   0 &   1 &   0 &   0 &   0 &  -1 &   0\\
 0 &   0 &   0 &   0 &   0 &   1 &  -1 &   0 &   0
\end{bmatrix}
$$

Because both this triangulation and the solid torus triangulation have a 
degree one edge, the computation is very similar to that of 
Example \ref{solid_torus_ex}.

Let $\omega = (x_1 \mu_1+ y_1 \lambda_1, x_2 \mu_2+ y_2 \lambda_2)$. Then
\begin{align*}
I_{\CT}({\omega})(q) &= \sum_{k_2 \in \Z} 
q^{k_2} \JD(k_2-y_1,0,0) \JD(x_2, y_1,x_1+y_2) \JD(x_1-y_2,-x_2,y_1)\\
&=\JD(k_2-y_1,0,0) \JD(x_2, y_1,x_1+y_2) q^{y_1} 
\sum_{k_2 \in \Z} q^{k_2-y_1} \JD(k_2-y_1,0,0)=0,
\end{align*}
since
$$
\sum_{\ell\in\Z} q^\ell \JD(\ell,0,0) = 
\sum_{\ell\in\Z} \ID(-\ell,0) q^\ell= \sum_{\ell\in\Z} \ID(0,\ell) q^\ell
= I(0,q,q)= \frac{(q q^{-1};q)_\infty}{(q)_\infty;q}=0.
$$
