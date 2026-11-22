---
doc_id: arxiv-1206.5522v6
doc_title: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS"
section_id: sec-009-33-homology-theories
section_title: "Homology theories"
section_number: 3.3
pages: 18-19
source_pdf: 1206.5522v6.pdf
source_sha256: 6e992242435b5e9f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.966
doc_brief: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS — Factorization homology theories of topological manifolds, after Beilinson, Drinfeld and Lurie, are homology-type theories for topological n-manifolds"
---
We now give our second main definition of this paper, that of a homology theory. First, note that taking products of manifolds defines a functor $\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_{n-1}^B\times\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_1^{\sf or} \rightarrow\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B$, where $\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_1^{\sf or}$ is oriented 1-manifolds and $$\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_{n-1}^B : = \mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_{n-1}\underset{\mathop{\mathrm{\mathsf{Spaces}}}_{/{\sf BTop(n)}}}\times\mathop{\mathrm{\mathsf{Spaces}}}_{/B}$$ is the $\mathop{\mathrm{\infty}}$-category of $(n-1)$-manifolds with a $B$-framing on the product of their tangent bundle product with a trivial line bundle. Consequently, any $B$-framed $n$-manifold of the form $M_0\times\mathbb R$, where $M_0$ is an $(n-1)$-manifold, can be given the structure of a $\mathop{\mathrm{{\mathcal D}\sf isk}}_1^{\sf or}$-algebra in $\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B$, since $\mathbb R$ has the structure of a $\mathop{\mathrm{{\mathcal D}\sf isk}}_1^{\sf or}$-algebra in $\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_1^{\sf or}$.

::: definition
[]{#def.collar-gluing label="def.collar-gluing"} A *collar-gluing among $B$-framed $n$-manifolds* is a continuous map $$f\colon M \to [-1,1]$$ to the closed interval for which the restriction $f_|\colon M_{|(-1,1)}\to (-1,1)$ is a manifold bundle. We will often denote a collar-gluing $M\xrightarrow{f}[-1,1]$ simply as the open cover $$M' \underset{M_0\times \mathbb R}\bigcup M''~\cong~M$$ where $M'= f^{-1}[-1,1)$ and $M''=f^{-1}(-1,1]$ and $M_0 = f^{-1}\{0\}$.
:::

::: remark
We find it useful to think of a collar-gluing as the data of a manifold $M$ together with a codimension-1 properly embedded submanifold $M_0\subset M$ that splits the manifold $M$ into two disconnected parts, $M'$ and $M''$. Such data is afforded by gluing two manifolds with boundary along a common boundary. The actual data of a collar-gluing specifies that named just above, in addition to a bi-collaring $M_0\times \mathbb R\hookrightarrow M$ of $M_0\subset M$.
:::

Construction [\[def.f-inverse\]](#def.f-inverse){reference-type="ref" reference="def.f-inverse"} offers, for each collar-gluing $M\xrightarrow{f} [-1,1]$ among $B$-framed $n$-manifolds, a monoidal functor $$f^{-1}\colon \mathop{\mathrm{{\mathcal D}\sf isk}}^{\partial,\sf or}_{1/[-1,1]} \longrightarrow \mathop{\mathrm{{\mathcal M}\mathsf{fld}}}^B_{n/M}~.$$ In particular, for each symmetric monoidal functor $\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}^B_n \xrightarrow{\mathcal F} \mathcal V$ with $\otimes$-presentable codomain, there is a canonical morphism in $\mathcal V$: $$\label{pre-excision}
\mathcal F(M')\underset{\mathcal F(M_0\times\mathbb R)}\bigotimes\mathcal F(M'')~\underset{\rm Cor~\ref{interval}}\simeq~\int_{[-1,1]} \mathcal F\circ f^{-1}~\longrightarrow~ \mathcal F(M)~.$$

::: definition
[]{#exc label="exc"} A symmetric monoidal functor $\mathcal F:\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^{B}\rightarrow\mathcal V$ satisfies *$\otimes$-excision* if, for each collar-gluing $M' \underset{M_0\times \mathbb R}\bigcup M''\cong M$ among $B$-framed $n$-manifolds, the canonical morphism ([\[pre-excision\]](#pre-excision){reference-type="ref" reference="pre-excision"}) $$\mathcal F(M')\underset{\mathcal F(M_0\times\mathbb R)}\bigotimes\mathcal F(M'')\xrightarrow{~\simeq~}\mathcal F(M)$$ is an equivalence in $\mathcal V$. The $\mathop{\mathrm{\infty}}$-category of *homology theories* for $B$-framed $n$-manifolds valued in $\mathcal V$ is the full $\mathop{\mathrm{\infty}}$-subcategory $$\mathbf H(\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^{B},\mathcal V)~\subset~\mathop{\mathrm{\sf Fun}}^\otimes(\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}^B_n, \mathcal V)$$ consisting of those symmetric monoidal functors that satisfy $\otimes$-excision.
:::

::: remark
The behavior of a homology theory with coefficients in $\mathcal V$ depends critically on the symmetric monoidal structure chosen on $\mathcal V$. For instance, for the symmetric monoidal $\infty$-category $(\mathop{\mathrm{\sf Mod}}_k,\oplus)$ of $k$-modules over a fixed field $k$ with direct sum, a homology theory is forced to be ordinary homology with coefficients in $k$; while for $(\mathop{\mathrm{\sf Mod}}_k,\otimes)$, a homology theories is typically *not* a homotopy invariant of manifolds.
:::

::: remark
One can complete the $\mathop{\mathrm{\infty}}$-category $\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n$ as follows: first, formally adjoin, for every collar-gluing $M'\underset{M_0\times\mathbb R}\bigcup M''\cong M$, the colimit of the simplicial object ${\sf Bar}_\bullet(M',M_0\times\mathbb R,M'')$; second, Dwyer-Kan localize by forcing the natural map from this new object $|{\sf Bar}_\bullet(M',M_0\times\mathbb R,M'')| \rightarrow M$ to be an equivalence. Denote this completion of the $\mathop{\mathrm{\infty}}$-category of manifolds as $\widehat{\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}}_n$. The completion functor $\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n \rightarrow\widehat{\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}}_n$ is the universal homology theory: that is, we now have the suggestive equivalence $$\int_M \mathbb R^n~ \simeq ~M$$ as objects of $\widehat\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n$ (the lefthand side is not defined in $\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n$). By this universal property, a $\otimes$-excisive functor $\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n\rightarrow\mathcal V$ is equivalent to a symmetric monoidal functor $\widehat{\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}}_n \rightarrow\mathcal V$ that preserves geometric realizations of simplicial objects.
:::
