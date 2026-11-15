---
doc_id: arxiv-1010.5321v3
doc_title: "Formulas on hyperbolic volume ∗"
section_id: sec-014-333-the-case-of-dimension-n
section_title: "The case of dimension n"
section_number: 3.3.3
pages: 13-14
source_pdf: 1010.5321v3.pdf
source_sha256: c6bb20926b1f291f
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.987
doc_brief: "Formulas on hyperbolic volume ∗ — This paper collects some important formulas on hyperbolic volume."
---
The following lemma plays an important role in the $n$-dimensional case.

::: lemma
We have two $k$-dimensional affine subspaces $H_k$ and $H'_k$, respectively for which they intersection have dimension $k-1$. Assume that the points $P\in H_k$, $P'\in H'_k$ and $P''\in H_k\cap H'_k$ hold the relations $PP'\bot H'_k$ and $P'P''\bot H_k\cap H'_k$, respectively. Then the angle $$\alpha =\tan ^{-1}\frac{\tanh(PP')}{\sinh P'P''},$$ is independent from the position of $P$ in $H_k$.
:::

Let $P$ and $Q$ be two arbitrary points of $H_k$. Then by the theorem of three perpendiculars we also have that $PP''\bot H_k\cap H'_k$ and $Q'Q''\bot H_k\cap H'_k$ implying that $P''Q''$ orthogonal to the lines $PP',P'P'',QQ'$ and $Q'Q''$, respectively. Thus the angles $PP'P''\angle$, $QQ'Q''\angle$ are equals. This immediately implies the statement. $\Box$

Let now our orthosceme is the convex hull of the vertices $0=A_0, A_1, \ldots , A_{n}$ situated into a hyperbolic orthogonal coordinate system as we did it in the three dimensional case. More precisely, the coordinates of the vertices are $(0,\ldots, 0)^T$, $(0,\ldots, 0,a_n)^T$, $(a_1,0,\ldots, 0,a_n)^T$, $(a_1,a_2,0\ldots, 0,a_n)^T$ $\ldots$ $(a_1,a_2,\ldots,a_n)^T$, respectively. Introduce the function giving the upper boundary of the successive integrals. These are $\phi_0=a_n$, $\phi_1:x_n\mapsto x_1$ for a point $(x_1,0,\ldots,0,x_n)^T$ of the edge $\mbox{ conv }(OA_2)$, $\phi_2:(x_n,x_1)\mapsto x_2$ on the points $(x_1,x_2,0\ldots,x_n)^T$ of the triangle $\mbox{ conv }(OA_2A_3)$. In general $\phi_k:(x_1,\ldots,x_{k-1},0,\ldots, 0,x_n)\mapsto x_k$ if the corresponding point $(x_1,x_2\ldots x_{k-1},x_k,0,\ldots,0,x_n)^T$ is on the $k-1$-face $\mbox{ conv }(OA_2A_3\cdots A_{k+1})$ and so on\... From Lemma 1 we get that $$\frac{ \tanh \phi_{k+1}(x_n,x_1,\ldots ,x_k)}{\sinh x_k}=\frac{ \tanh a_{k+1}}{\sinh a_k},$$ implying that $$\phi_{k+1}(x_n,x_1,\ldots ,x_k)=\tan^{-1}\left(\frac{ \tanh a_{k+1}}{\sinh a_k}\sinh x_k\right).$$ In the case of $k=1$, the volume can be determined by the following $n$-times integral: $v(O)=\int\limits_{0}^{a_n}\int\limits_{0}^{\tan^{-1}\left(\frac{ \tanh a_{1}}{\sinh a_n}\sinh x_n\right)}\cdots  \int\limits_{0}^{\tan^{-1}\left(\frac{ \tanh a_{n-1}}{\sinh a_{n-2}}\sinh x_{n-1}\right)}$

$(\cosh^{n-1}x_{n-1})(\cosh^{n-2}  x_{n-2})\cdots (\cosh  x_{1})
\mathrm{d}x_{n-1}\cdots \mathrm{d}x_{1}\mathrm{d}x_n.$
