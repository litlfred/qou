---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-002-12-flags-in-statistics
section_title: "Flags in statistics"
section_number: 1.2
pages: 3-4
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.947
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
Although not usually viewed in this manner, classical multivariate data analysis techniques [@MKB] may be cast as nested subspace-searching problems, i.e., constrained or unconstrained optimization problems on the flag manifold.

We let $\text{\usefont{U}{bbm}{m}{n}1}$ denote a vector of all ones (of appropriate dimension). We assume that our data set is given in the form of a sample-by-variables design matrix $X \in \mathbb{R}^{n \times p}$, $n \ge p$, which we call a data matrix for short. Let $\overline{x}=\frac{1}{n}X^{\scriptscriptstyle\mathsf{T}}\text{\usefont{U}{bbm}{m}{n}1}\in\mathbb{R}^{p}$ be its sample mean and $S_X = (X-\text{\usefont{U}{bbm}{m}{n}1}\overline{x}^{\scriptscriptstyle\mathsf{T}})^{\scriptscriptstyle\mathsf{T}}(X-\text{\usefont{U}{bbm}{m}{n}1}\overline{x}^{\scriptscriptstyle\mathsf{T}}) \in \mathbb{R}^{p \times p}$ be its sample covariance. For another data matrix $Y \in \mathbb{R}^{n \times q}$, $S_{XY} = (X-\text{\usefont{U}{bbm}{m}{n}1}\overline{x}^{\scriptscriptstyle\mathsf{T}})^{\scriptscriptstyle\mathsf{T}}(Y-\text{\usefont{U}{bbm}{m}{n}1}\overline{y}^{\scriptscriptstyle\mathsf{T}}) = S_{YX}^{\scriptscriptstyle\mathsf{T}}\in \mathbb{R}^{p \times q}$ denotes sample cross-covariance.

::: example
[]{#eg:pca label="eg:pca"} The $k$th *principal subspace* of $X$ is $\mathop{\mathrm{im}}(Z_k)$, where $Z_k$ is the $p \times k$ orthonormal matrix given by $$\label{eq:pca}
Z_k = \mathop{\mathrm{argmax}}\{ \mathop{\mathrm{tr}}(Z^{\scriptscriptstyle\mathsf{T}}S_X Z)  : Z \in \mathop{\mathrm{V}}(k,p)\}, \quad k =1,\dots, p.$$ So $\mathop{\mathrm{im}}(Z_k)$ is a $k$-dimensional linear subspace of $\mathbb{R}^p$ spanned by the orthonormal columns of $Z_k$. In an appropriate sense, the $k$th principal subspace captures the greatest variability in the data among all $k$-dimensional subspaces of $\mathbb{R}^p$. In principal component analysis (PCA), the data points, i.e., columns of $X$, are often projected onto $\mathop{\mathrm{im}}(Z_k)$ with $k =2,3$ for visualization or with other small values of $k$ for dimension reduction. Clearly $\mathop{\mathrm{im}}(Z_k)$ is contained in $\mathop{\mathrm{im}}(Z_{k+1})$ and the flag $$\mathop{\mathrm{im}}(Z_1) \subseteq  \mathop{\mathrm{im}}(Z_2) \subseteq \dots \subseteq \mathop{\mathrm{im}}(Z_p)$$ explains an increasing amount of variance in the data.
:::

In [@PX Theorem 9], it is shown how one may directly define PCA as an optimization problem on a flag manifold, a powerful perspective that in turn allows one to generalize and extend PCA in various manners. Nevertheless what is lacking in [@PX] is an algorithm for optimization on flag manifolds, a gap that our article will fill.

::: example
[]{#eg:cca label="eg:cca"} The $k$th pair of *canonical correlation loadings* $(a_k, b_k) \in \mathbb{R}^p \times \mathbb{R}^q$ is defined recursively by $$\begin{gathered}
\label{eq:cca}
(a_k, b_k) = \mathop{\mathrm{argmax}}\{ a^{\scriptscriptstyle\mathsf{T}}S_{XY} b : a^{\scriptscriptstyle\mathsf{T}}S_{X} a = b^{\scriptscriptstyle\mathsf{T}}S_{Y} b = 1, \\
 a^{\scriptscriptstyle\mathsf{T}}S_X a_j = a^{\scriptscriptstyle\mathsf{T}}S_{XY} b_j = b^{\scriptscriptstyle\mathsf{T}}S_{YX} a_j = b^{\scriptscriptstyle\mathsf{T}}S_Y b_j = 0, \; j =1,\dots,k-1 \}.
\end{gathered}$$ Let $A_k = [a_1,\dots,a_k] \in \mathbb{R}^{p \times k}$ and $B_k = [b_1,\dots,b_k] \in \mathbb{R}^{q \times k}$. Then the canonical correlation subspaces of $X$ and $Y$ are given by $$\mathop{\mathrm{im}}(A_1) \subseteq \dots \subseteq \mathop{\mathrm{im}}(A_p) \quad\text{and}\quad \mathop{\mathrm{im}}(B_1) \subseteq \dots \subseteq \mathop{\mathrm{im}}(B_q),$$ which are flags in $\mathbb{R}^p$ and $\mathbb{R}^q$ respectively. Collectively they capture how the shared variance between the two data sets increases with $k$.
:::

::: example
[]{#eg:ca label="eg:ca"} Let $t = \text{\usefont{U}{bbm}{m}{n}1}^{\scriptscriptstyle\mathsf{T}}X\text{\usefont{U}{bbm}{m}{n}1} \in \mathbb{R}$, $r = \frac{1}{t} X\text{\usefont{U}{bbm}{m}{n}1}  \in \mathbb{R}^n$, $c = \frac{1}{t} X^{\scriptscriptstyle\mathsf{T}}\text{\usefont{U}{bbm}{m}{n}1} \in \mathbb{R}^p$ denote the total, row, and column weights of $X$ respectively and set $D_r = \frac{1}{t} \mathop{\mathrm{diag}}(r) \in \mathbb{R}^{n \times n}$, $D_c = \frac{1}{t} \mathop{\mathrm{diag}}(c) \in \mathbb{R}^{p \times p}$. For $k =1,\dots,p$, we seek matrices $U_k \in \mathbb{R}^{k \times n}$ and $V_k \in \mathbb{R}^{k \times p}$ such that $$\label{eq:ca}
(U_k, V_k) = \mathop{\mathrm{argmax}}\{ \mathop{\mathrm{tr}}\bigl( U^{\scriptscriptstyle\mathsf{T}}(\tfrac{1}{t} X - rc^{\scriptscriptstyle\mathsf{T}})  V \bigr) :  U^{\scriptscriptstyle\mathsf{T}}D_r U = I = V^{\scriptscriptstyle\mathsf{T}}D_c V \}.$$ The solution $$\mathop{\mathrm{im}}(U_1) \subseteq \dots \subseteq \mathop{\mathrm{im}}(U_p) \quad\text{and}\quad \mathop{\mathrm{im}}(V_1) \subseteq \dots \subseteq \mathop{\mathrm{im}}(V_p)$$ are flags in $\mathbb{R}^n$ and $\mathbb{R}^p$ respectively and collectively they explain the increasing deviation from the independence of occurrence of two outcomes.
:::

For reasons such as sensitivity of the higher-dimensional subspaces to noise in the data, in practice one relies on the first few subspaces in these flags to make various inference about the data. Nevertheless, we stress that the respective flags that solve [\[eq:pca\]](#eq:pca){reference-type="eqref" reference="eq:pca"}, [\[eq:cca\]](#eq:cca){reference-type="eqref" reference="eq:cca"}, [\[eq:ca\]](#eq:ca){reference-type="eqref" reference="eq:ca"} over all $k$ will paint a complete picture showing the full profile of how variance, shared variance, or deviation from independence vary across dimensions.

Apart from PCA, CCA, and CA, flags arise in other multivariate data analytic techniques [@MKB], e.g., factor analysis (FA), linear discriminant analysis (LDA), multidimensional scaling (MDS), etc, in much the same manner. One notable example is the independent subspace analysis proposed in [@NSP2006; @NAP2008], a generalization of independent component analysis.
