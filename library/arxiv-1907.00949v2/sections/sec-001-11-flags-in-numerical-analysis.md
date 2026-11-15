---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-001-11-flags-in-numerical-analysis
section_title: "Flags in numerical analysis"
section_number: 1.1
pages: 2-3
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.981
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
In numerical analysis, flags naturally arise in finite elements, multigrid, spectral and pseudospectral methods, wavelets, iterative matrix computations, etc, in several ways.

::: example
In multigrid, algebraic multigrid, finite element methods, we often consider a sequence of increasingly finer *grids* or *meshes* $G_1 \subseteq G_2
\subseteq G_3 \subseteq \cdots$ on the domain of interest $\Omega$. The vector space of real-valued functions $$\mathbb{V}_k \coloneqq \{ f : G_k \to \mathbb{R} \}$$ gives us a flag $\mathbb{V}_1 \subseteq \mathbb{V}_2 \subseteq  \mathbb{V}_3 \subseteq \cdots$ of finite-dimensional vector spaces where $\dim \mathbb{V}_k = \# G_k$. The aforementioned numerical methods are essentially different ways of extracting approximate solutions of increasing accuracy from the flag.
:::

::: example
In spectral and pseudospectral methods, we consider a class of functions of increasing complexity determined by an *order* $d$, e.g., polynomial or trigonometric polynomial functions of degree $d$, on the domain of interest $\Omega$. The vector space $$\mathbb{V}_d \coloneqq \{ f : \Omega \to \mathbb{R} : \mathop{\mathrm{deg}}(f) \le d \}$$ gives us a flag $\mathbb{V}_1 \subseteq \mathbb{V}_2 \subseteq  \mathbb{V}_3 \subseteq \cdots$ as $d$ is increased. Again, these methods operate by extracting approximate solutions of increasing accuracy from the flag.
:::

::: example
Given $A \in \mathbb{R}^{n \times n}$ and $b \in \mathbb{R}^n$, the subspace $$K_{k}(A,b) \coloneqq \operatorname{span}\{b,Ab,\dots,A^{k-1} b\}$$ is called the $k$th *Krylov subspace*. The gist behind Krylov subspace methods in numerical linear algebra, whether for computing solutions to linear systems, least squares problems, eigenvalue problems, matrix functions, etc, are all based on finding a sequence of increasingly better approximations from the flag $K_0(A,b) \subseteq K_1(A,b) \subseteq \dots \subseteq K_k(A,b)$.
:::

::: example
A standard way to construct wavelets is to define a *multiresolution analysis*, i.e., a sequence of subspaces $\mathbb{V}_{k+1} \subseteq \mathbb{V}_k$ defined by $$f(t) \in \mathbb{V}_k \quad \Leftrightarrow \quad f(t/2) \in \mathbb{V}_{k+1}.$$ The convention in wavelet literature has the indexing in reverse order but this is a minor matter --- a nested of sequence of subspaces is a flag regardless of how the subspaces in the sequence are labeled. So a multiresolution analysis is also a flag.
:::

This is not an exhaustive list, flags also arise in numerical analysis in other ways, e.g., analysis of eigenvalue methods [@GM1986; @JH2002].
