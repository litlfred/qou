---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-010-3-basic-differential-geometry-of-flag-manifolds
section_title: "Basic differential geometry of flag manifolds"
section_number: 3
pages: 7-9
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.993
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
[]{#sec:flag label="sec:flag"}

We will now define flags and flag manifolds formally and discuss some basic properties. Let $n$ be a positive integer and $\mathbb{V}$ be an $n$-dimensional vector space over $\mathbb{R}$. We write $\mathop{\mathrm{V}}(k, \mathbb{V})$ for the Stiefel manifold [@Stiefel1935] of $k$-frames in $\mathbb{V}$ and $\mathop{\mathrm{Gr}}(k, \mathbb{V})$ for the Grassmannian [@Grass] of $k$-dimensional subspaces in $\mathbb{V}$. If the choice of $\mathbb{V}$ is unimportant or if $\mathbb{V} = \mathbb{R}^n$, then we will just write $\mathop{\mathrm{V}}(k,n)$ and $\mathop{\mathrm{Gr}}(k,n)$.

::: definition
Let $0 < n_1 < \dots < n_d < n$ be an increasing sequence of $d$ positive integers and $\mathbb{V}$ be an $n$-dimensional vector space over $\mathbb{R}$. A flag of type $(n_1,\dots, n_d)$ in $\mathbb{V}$ is a sequence of subspaces $$\mathbb{V}_1 \subsetneq  \mathbb{V}_2 \subsetneq \dots \subsetneq \mathbb{V}_d, \quad \dim \mathbb{V}_i = n_i,\quad i=1,\dots,d.$$ We denote the set of such flags by $\mathop{\mathrm{Flag}}(n_1,\dots,n_d;\mathbb{V})$ and call it the *flag manifold* of type $(n_1,\dots, n_d)$. If $\mathbb{V}$ is unimportant or if $\mathbb{V} = \mathbb{R}^n$, then we will just write $\mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$.
:::

For notational convenience we will adopt the following convention throughout: $$n_0 \coloneqq 0, \qquad n_{d+1} \coloneqq n, \qquad \mathbb{V}_0 \coloneqq \{0 \}, \qquad \mathbb{V}_{d+1} \coloneqq \mathbb{V}.$$

We will see in Proposition [\[prop:geometric structure\]](#prop:geometric structure){reference-type="ref" reference="prop:geometric structure"} that flag manifolds are indeed manifolds. When $d=1$, $\mathop{\mathrm{Flag}}(k; \mathbb{V})$ is the set of all $k$-dimensional subspaces of $\mathbb{V}$, which is the Grassmannian $\mathop{\mathrm{Gr}}(k,\mathbb{V})$. The other extreme case is when $d= n-1$ and $n_i = i$, $i =1,\dots, n-1$, and in which case $\mathop{\mathrm{Flag}}(1,\dots, n-1;\mathbb{V})$ comprises all *complete flags* of $\mathbb{V}$, i.e., $$\mathbb{V}_1 \subsetneq  \mathbb{V}_2 \subsetneq \dots \subsetneq \mathbb{V}_{n-1}, \quad \dim \mathbb{V}_i = i,\quad i=1,\dots,n-1.$$

Like the Grassmannian, the flag manifold is not merely a set but has rich geometric structures. We will start with the most basic ones and defer other useful characterizations to Sections [\[sec:homo\]](#sec:homo){reference-type="ref" reference="sec:homo"} and [\[sec:mfld\]](#sec:mfld){reference-type="ref" reference="sec:mfld"}.

::: proposition
[]{#prop:geometric structure label="prop:geometric structure"} Let $0 < n_1< \dots < n_d < n$ be integers and $\mathbb{V}$ be an $n$-dimensional real vector space. The flag manifold $\mathop{\mathrm{Flag}}(n_1,\dots, n_d;\mathbb{V})$ is

1.  []{#it:mfld label="it:mfld"} a connected compact smooth manifold;

2.  []{#it:var1 label="it:var1"} an irreducible affine variety;

3.  []{#it:cls1 label="it:cls1"} a closed submanifold of $\mathop{\mathrm{Gr}}(n_1,\mathbb{V})\times \mathop{\mathrm{Gr}}(n_2,\mathbb{V}) \times \dots \times \mathop{\mathrm{Gr}}(n_d,\mathbb{V})$;

4.  []{#it:cls2 label="it:cls2"} a closed submanifold of $\mathop{\mathrm{Gr}}(n_1,\mathbb{V})\times \mathop{\mathrm{Gr}}(n_2-n_1,\mathbb{V}) \times \dots \times \mathop{\mathrm{Gr}}(n_d-n_{d-1},\mathbb{V})$;

5.  []{#it:fiber label="it:fiber"} a fiber bundle on $\mathop{\mathrm{Gr}}(n_d,\mathbb{V})$ whose fiber over $\mathbb{W}\in \mathop{\mathrm{Gr}}(n_d,\mathbb{V})$ is $\mathop{\mathrm{Flag}}(n_1,\dots, n_{d-1};\mathbb{W})$;

6.  []{#it:var2 label="it:var2"} a smooth projective variety.
:::

::: proof
*Proof.* Property [\[it:mfld\]](#it:mfld){reference-type="eqref" reference="it:mfld"} is well-known [@Monk1959; @Borel1991] but also follows from the characterization in Proposition [\[prop:equivalent definition of flag manifold\]](#prop:equivalent definition of flag manifold){reference-type="ref" reference="prop:equivalent definition of flag manifold"} as a quotient of a compact connected Lie group by a closed subgroup. Property [\[it:var1\]](#it:var1){reference-type="eqref" reference="it:var1"} is a consequence of Propositions [\[prop:representation of flags\]](#prop:representation of flags){reference-type="ref" reference="prop:representation of flags"} and [\[prop:reduced coord\]](#prop:reduced coord){reference-type="ref" reference="prop:reduced coord"}, where we give two different ways of representing $\mathop{\mathrm{Flag}}(n_1,\dots,n_d;\mathbb{V})$ as an affine variety in $\mathbb{R}^m$, $m = (nd)^2$. Property [\[it:var2\]](#it:var2){reference-type="eqref" reference="it:var2"} is a consequence of [\[it:cls1\]](#it:cls1){reference-type="eqref" reference="it:cls1"} or [\[it:cls2\]](#it:cls2){reference-type="eqref" reference="it:cls2"}, given that the Grassmannian is a projective variety.

In the following, let $\{\mathbb{V}_i\}_{i=1}^d \in \mathop{\mathrm{Flag}}(n_1,\dots,n_d;\mathbb{V})$, i.e., $\dim \mathbb{V}_i = n_i$, $i=1,\dots, d$. For [\[it:cls1\]](#it:cls1){reference-type="eqref" reference="it:cls1"}, the map $$\label{eq:j}
\varepsilon : \mathop{\mathrm{Flag}}(n_1,\dots,n_d;\mathbb{V}) \to \mathop{\mathrm{Gr}}(n_1,\mathbb{V})\times \dots \times \mathop{\mathrm{Gr}}(n_d,\mathbb{V}), \quad \{\mathbb{V}_i\}_{i=1}^d \mapsto (\mathbb{V}_1, \mathbb{V}_2, \dots, \mathbb{V}_d)$$ is clearly an embedding. Its image is closed since if $(\mathbb{V}_1 , \dots, \mathbb{V}_d) \not\in \varepsilon \bigl(\mathop{\mathrm{Flag}}(n_1,\dots,n_d;\mathbb{V})\bigr)$, then there exists some $i \in \{ 1,\dots, d-1\}$ such that $\mathbb{V}_i \not\subseteq \mathbb{V}_{i+1}$; so if $\mathbb{V}'_i\in \mathop{\mathrm{Gr}}(n_i,\mathbb{V})$ and $\mathbb{V}'_{i+1} \in \mathop{\mathrm{Gr}}(n_{i+1},\mathbb{V})$ are in some small neighborhood of $\mathbb{V}_i$ and $\mathbb{V}_{i+1}$ respectively, then $\mathbb{V}'_i \not\subseteq \mathbb{V}'_{i+1}$.

For [\[it:cls2\]](#it:cls2){reference-type="eqref" reference="it:cls2"}, choose and fix an inner product on $\mathbb{V}$. Let $\mathbb{V}_i^{\perp}$ denote the orthogonal complement of $\mathbb{V}_i$ in $\mathbb{V}_{i+1}$, $i=1,\dots, d-1$. The map $$\label{eq:j2}
\begin{aligned}
\varepsilon ': \mathop{\mathrm{Flag}}(n_1,\dots, n_d;\mathbb{V}) &\to \mathop{\mathrm{Gr}}(n_1,\mathbb{V})\times \mathop{\mathrm{Gr}}(n_2-n_1,\mathbb{V}) \times \dots \times \mathop{\mathrm{Gr}}(n_d-n_{d-1},\mathbb{V}),\\
\{\mathbb{V}_i\}_{i=1}^d &\mapsto (\mathbb{V}_1, \mathbb{V}_1^{\perp}, \dots, \mathbb{V}_{d-1}^{\perp})
\end{aligned}$$ is clearly an embedding. That the image of $\varepsilon '$ is closed follows from the same argument used for $\varepsilon$.

For [\[it:fiber\]](#it:fiber){reference-type="eqref" reference="it:fiber"}, consider the map $$\rho: \mathop{\mathrm{Flag}}(n_1,\dots,n_d;\mathbb{V}) \to \mathop{\mathrm{Gr}}(n_d,\mathbb{V}), \quad \{\mathbb{V}_i\}_{i=1}^d \mapsto \mathbb{V}_d,$$ that is clearly surjective and smooth. For any $\mathbb{W} \in  \mathop{\mathrm{Gr}}(n_d,\mathbb{V})$, $\rho^{-1}(\mathbb{W})$ consists of flags of the form $$\mathbb{V}'_1 \subseteq \mathbb{V}'_2 \subseteq \dots \subseteq \mathbb{V}'_{d-1} \subseteq \mathbb{W},\quad \dim \mathbb{V}'_i = n_i,\quad i=1,\dots, d-1.$$ In other words, the fiber $\rho^{-1}(\mathbb{W}) \cong  \mathop{\mathrm{Flag}}(n_1,\dots, n_{d-1};\mathbb{W})$. ◻
:::

The fiber bundle structure in Proposition [\[prop:geometric structure\]](#prop:geometric structure){reference-type="ref" reference="prop:geometric structure"}[\[it:fiber\]](#it:fiber){reference-type="eqref" reference="it:fiber"} may be recursively applied to get $$\begin{gathered}
\mathop{\mathrm{Flag}}(n_1,\dots, n_{d-1};n_d) \to \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n) \to \mathop{\mathrm{Gr}}(n_d,n),\\
\mathop{\mathrm{Flag}}(n_1,\dots, n_{d-2};n_{d-1}) \to \mathop{\mathrm{Flag}}(n_1,\dots, n_{d-1};n_d) \to \mathop{\mathrm{Gr}}(n_{d-1},n),
\end{gathered}$$ and so on, ending in the well-known characterization of the Stiefel manifold as a principal bundle over the Grassmannian $$\mathop{\mathrm{O}}(n) \to \mathop{\mathrm{V}}(k,n) \to \mathop{\mathrm{Gr}}(k,n).$$

In the next two sections, we will see how the flag manifold may be equipped with extrinsic matrix coordinates and be represented as either homogeneous spaces of matrices (Section [\[sec:homo\]](#sec:homo){reference-type="ref" reference="sec:homo"}) or manifolds of matrices (Section [\[sec:mfld\]](#sec:mfld){reference-type="ref" reference="sec:mfld"}) that in turn give closed-form analytic expressions for various differential geometric objects and operations needed for optimization algorithms.
