---
doc_id: arxiv-1011.6483v3
doc_title: "DERIVED HIGHER HOCHSCHILD HOMOLOGY, TOPOLOGICAL CHIRAL HOMOLOGY AND FACTORIZATION ALGEBRAS"
section_id: sec-002-21-simplicial-sets
section_title: "Simplicial sets"
section_number: 2.1
pages: 7-8
source_pdf: 1011.6483v3.pdf
source_sha256: 7a425e51860c37a4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.934
doc_brief: "DERIVED HIGHER HOCHSCHILD HOMOLOGY, TOPOLOGICAL CHIRAL HOMOLOGY AND FACTORIZATION ALGEBRAS — We study the higher Hochschild chain functor, factorization alge- bras and their relationship with"
---
[]{#S:Delta label="S:Delta"} Denote by $\Delta$ the category whose objects are the ordered sets $[k]=\{0,1,\dots,k\}$, and morphisms $f:[k]\to [l]$ are non-decreasing maps $f(i)\geq f(j)$ for $i>j$. In particular, we have the morphisms $\delta_i:[k-1]\to[k], i=0,\dots, k$, which are injections that miss $i$ and we have surjections $\sigma_j:[k+1]\to [k], i=0,\dots,k$, which send $j$ and $j+1$ to $j$.

A *simplicial set* is by definition a contravariant functor from $\Delta$ to the category of sets $\mathcal Sets$ or written as a formula, $Y_{\scriptstyle\bullet}:\Delta^{op}\to\mathcal Sets$. Denote by $Y_k=Y_{\scriptstyle\bullet}([k])$, and call its elements simplicies. The image of $\delta_i$ under $Y_{\scriptstyle\bullet}$ is denoted by $d_i:=Y_{\scriptstyle\bullet}(\delta_i):Y_{k}\to Y_{k-1}$, for $i=0,\dots,k$, and is called the $i$th face. Similarly, $s_i:=Y_{\scriptstyle\bullet}(\sigma_i):Y_{k}\to Y_{k+1}$, for $i=0,\dots,k$, is called the $i$th degeneracy. An element in $Y_k$ is called a degenerate simplex, if it is in the image of some $s_i$, otherwise it is called non-degenerate.

A simplicial set is said to be *finite* if $Y_k$ is finite for every object $[k]\in \Delta$. A *pointed* simplicial set is a contravariant functor into the category $\mathcal Sets_*$ of pointed finite sets, $Y_{\scriptstyle\bullet}:\Delta^{op}\to \mathcal Sets_*$. In particular, each $Y_k=Y_{\scriptstyle\bullet}([k])$ has a preferred element called the base point, and all differentials $d_i$ and degeneracies $s_i$ preserve this base point.

A morphism of (finite or not, pointed or not) simplicial sets is a natural transformation of functors $f_{\scriptstyle\bullet}:X_{\scriptstyle\bullet}\to Y_{\scriptstyle\bullet}$. Thus $f_{\scriptstyle\bullet}$ is given by a sequence of maps $f_k:X_k\to Y_k$ (preserving the base point in the pointed case), which commute with the faces $f_k d_i = d_i f_{k+1}$, and degeneracies $f_{k+1} s_i=s_i f_{k}$ for all $k\geq 0$ and $i=0,\dots, k$.

One of the most important construction for us is the pushout.

::: definition
[]{#D:wedge label="D:wedge"} Let $X_{\scriptstyle\bullet}, Y_{\scriptstyle\bullet}$, and $Z_{\scriptstyle\bullet}$ be simplicial sets, and let $f_{\scriptstyle\bullet}:Z_{\scriptstyle\bullet}\to X_{\scriptstyle\bullet}$ and $g_{\scriptstyle\bullet}:Z_{\scriptstyle\bullet}\to Y_{\scriptstyle\bullet}$ be maps of simplicial sets. We define the wedge $W_{\scriptstyle\bullet}=X_{\scriptstyle\bullet}\cup_{Z_{\scriptstyle\bullet}} Y_{\scriptstyle\bullet}$ of $X_{\scriptstyle\bullet}$ and $Y_{\scriptstyle\bullet}$ along $Z_{\scriptstyle\bullet}$ as the simplicial space given by $W_k= (X_k \cup Y_k)/\sim$, where $\sim$ identifies $f_k(z)=g_k(z)$ for all $z\in Z_k$. The face maps are defined as $d^{W_{\scriptstyle\bullet}}_i(x)=d^{X_{\scriptstyle\bullet}}_i(x), d^{W_{\scriptstyle\bullet}}_i(y)=d^{Y_{\scriptstyle\bullet}}_i(y)$ and the degeneracies are $s^{W_{\scriptstyle\bullet}}_i(x)=s^{X_{\scriptstyle\bullet}}_i(x), s^{W_{\scriptstyle\bullet}}_i(y)=s^{Y_{\scriptstyle\bullet}}_i(y)$ for any $x\in X_k \hookrightarrow W_k$ and $y\in Y_k \hookrightarrow W_k$. It is clear that $W_{\scriptstyle\bullet}$ is well-defined and there are simplicial maps $X_{\scriptstyle\bullet}\stackrel{i_{\scriptstyle\bullet}}\to W_{\scriptstyle\bullet}$ and $Y_{\scriptstyle\bullet}\stackrel{j_{\scriptstyle\bullet}}\to W_{\scriptstyle\bullet}$.

If $X_{\scriptstyle\bullet}$ is a pointed simplicial set, then we can make $W_{\scriptstyle\bullet}$ into a pointed simplicial set by declaring the base point to be the one induced from the inclusion $X_{\scriptstyle\bullet}\to W_{\scriptstyle\bullet}$. (Note that this is in particular the case, when $X_{\scriptstyle\bullet}, Y_{\scriptstyle\bullet}, Z_{\scriptstyle\bullet}, f_{\scriptstyle\bullet}$ and $g_{\scriptstyle\bullet}$ are in the pointed setting.)
:::
