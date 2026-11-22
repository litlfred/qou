---
doc_id: arxiv-1508.07379v2
doc_title: "Convergence of Mayer and Virial expansions and the Penrose tree-graph identity"
section_id: sec-004-31-general-penrose-identity
section_title: "General Penrose identity"
section_number: 3.1
pages: 7-8
source_pdf: 1508.07379v2.pdf
source_sha256: c3dbf93d1cac198e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.922
latex_coverage_ratio: 0.983
doc_brief: "Convergence of Mayer and Virial expansions and the Penrose tree-graph identity — We establish new lower bounds for the convergence radius of the Mayer series and the Virial series of a continuous"
---
Penrose identity is a rewriting of the Ursell functions $$\Phi^T(x_1,\dots,x_n)~=~\sum\limits_{g\in {\mathcal G}_{n}}~
\prod\limits_{\{i,j\}\in E_g}\left[  e^{ -\b V(x_i -x_j)} -1\right]$$ based on the existence of a map (*partition scheme*) from the set ${\mathcal T}_n$ of the trees with vertex set $[n]$ to the set ${\mathcal G}_n$ of the connected graphs with vertex set $[n]$.

::: defi
[]{#partschem label="partschem"} A map $\bm{M}: {\mathcal T}_n\to {\mathcal G}_n$ is called a partition scheme in the set of the connected graphs ${\mathcal G}_n$ if, for all $\tau\in {\mathcal T}_n$, $\tau\subset \bm{M}(\t)$ (i.e. $\t$ is subgraph of $\bm{M}(\t)$) and ${\mathcal G}_n=\biguplus_{\tau\in {\mathcal T}_n}[\tau,\bm M(\tau)]$ where $\biguplus$ means disjoint union and $[\tau,\bm M(\tau)]=\{g\in {\mathcal G}_n: \tau\subset g\subset \bm M(\tau)\}$ is an interval in ${\mathcal G}_n$ (with respect to the set-inclusion).
:::

\
Once a partition scheme in ${\mathcal G}_n$ has been given, we have the following identity

::: teorema
[]{#Penid label="Penid"} Let $V(x)$ be a pair potential. Let $n\ge 2$. Let $\bm{M}: {\mathcal T}_n\to {\mathcal G}_n$ be a partition scheme in ${\mathcal G}_n$. Then, for any $(x_1,\dots,x_n)\in \mathbb{R}^{dn}$ the following identity holds []{#penide label="penide"} \_g\_n \_{i,j}E_g =  \_͡\_ne\^-̱\_{i,j}E\_()͡\\E\_͡V(x_i-x_j)
:::

\
**Proof** . Let us pose shortly $V_{ij}=\b V(x_i-x_j)$. Since ${\mathcal G}_n$ is the disjoint union ${\mathcal G}_n=\biguplus_{\tau\in {\mathcal T}_n}[\tau,\bm{M}(\tau)]$ we can write $$\sum_{g\in {\mathcal G}_n} \prod_{\{i,j\}\in E_g}\left(e^{- V_{ij}}-1\right)~=~\sum_{\t\in {\mathcal T}_n} \sum_{g\in  [\tau,\bm{M}(\tau)]}
\prod_{\{i,j\}\in E_g}\left(e^{- V_{ij}}-1\right)~=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$$ $$~~~~~~~~~~~~~~~~~~~~~~=~
\sum_{\t\in {\mathcal T}_n} \prod_{\{i,j\}\in E_\t}\left(e^{- V_{ij}}-1\right)\sum_{g\in G_n\atop E_\t\subset E_g\subset E_{\bm{M}(\t)}}
 \prod_{\{i,j\}\in E_g\setminus E_\t}\left(e^{- V_{ij}}-1\right) =$$ $$~~~~~~~~~~~~~~~~~~~=~ \sum_{\t\in {\mathcal T}_n} \prod_{\{i,j\}\in E_\t}\left(e^{- V_{ij}}-1\right)\sum_{E\subset E_{\bm{M}(\t)}\setminus E_\t}
 \prod_{\{i,j\}\in E}\left(e^{- V_{ij}}-1\right)~=~$$ $$~~~~~~~~~~~~~~~~\,\,\,\,\;~~~~\,=~ \sum_{\t\in {\mathcal T}_n} \left[\prod_{\{i,j\}\in E_\t}\left(e^{- V_{ij}}-1\right)\right]
 \prod_{\{i,j\}\in E_{\bm{M}(\t)}\setminus E_\t}\left[\left(e^{- V_{ij}}-1\right)+1\right]~=~$$ $$~~~~\;\;\;\,~~\:~~~~=
 ~ \sum_{\t\in {\mathcal T}_n} \left[\prod_{\{i,j\}\in E_\t}\left(e^{- V_{ij}}-1\right)\right]
 \prod_{\{i,j\}\in E_{\bm{M}(\t)}\setminus E_\t} e^{- V_{ij}}~~~~~~~~~~~\Box$$

\
From Theorem [\[Penid\]](#Penid){reference-type="ref" reference="Penid"} the corollary below easily follows.

::: cor
[]{#cor1 label="cor1"} Let $V(x)$ be a pair potential. Let $n\ge 2$. Let $\bm{M}: {\mathcal T}_n\to {\mathcal G}_n$ be a partition scheme in ${\mathcal G}_n$. Then, for any $(x_1,\dots,x_n)\in \mathbb{R}^{dn}$ the following inequality holds []{#tre label="tre"} \|\_gG\_n  \_{i,j}E_g\|    \_͡T_n e\^-̱\_{i,j}E\_()͡\\E\^+\_͡V(x_i-x_j) \_{i,j}E\_͡(1-e\^- \|̱V(x_i-x_j)\|) where $E_\tau^+$ denotes the set of edges of the tree $\tau$ with non-negative energy. That is, []{#t+ label="t+"} E\_\^+={{i,j}E\_:͡ V(x_i-x_j)}
:::

\
**Proof**. Let us pose once again $V_{ij}=\b V(x_i-x_j)$. By Theorem [\[Penid\]](#Penid){reference-type="ref" reference="Penid"} we have that []{#uno label="uno"} \|\_g_n \_{i,j}E_g(e\^- V\_ij-1)\|   \_͡\_n \_{i,j}E\_͡\|e\^- V\_ij-1\| e\^- \_{i,j}E\_()͡E\_͡V\_ij Using now the trick proposed in [@errata] we observe that, for any $\t\in \mathcal T_n$ $$\prod_{\{i,j\} \in E_\tau} |e^{-V_{ij}}-1|=\Big[ \prod_{\{i,j\} \in E_\tau} (1-e^{- |V_{ij}|}) \Big] \
 e^{- \sum_{\{i,j\}\in E_\t\setminus E^+_\t}V_{ij}}$$ so that []{#due label="due"} e\^- \_{i,j}E\_()͡E\_͡V\_ij =  e\^- \_{i,j} E\_M() E\^+\_V\_ij Inserting now ([\[due\]](#due){reference-type="ref" reference="due"}) into ([\[uno\]](#uno){reference-type="ref" reference="uno"}) we get ([\[tre\]](#tre){reference-type="ref" reference="tre"}). $\Box$
