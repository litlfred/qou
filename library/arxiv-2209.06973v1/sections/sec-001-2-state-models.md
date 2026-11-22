---
doc_id: arxiv-2209.06973v1
doc_title: "On the geometry of two state models for the colored Jones polynomial"
section_id: sec-001-2-state-models
section_title: "State models"
section_number: 2
pages: 3-5
source_pdf: 2209.06973v1.pdf
source_sha256: cc3393a17c48b9df
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.694
doc_brief: "On the geometry of two state models for the colored Jones polynomial — Using the ﬂow property of the R-matrix deﬁning the colored Jones polynomial, we establish a natural bijection between the set of"
---
We will consider *vertex models* as defined in [@J], see also [@T].

::: defn
Let $\mathfrak{G}$ be a set of (possibly in some way decorated) finite graphs and let $\mathcal{R}$ be an integral domain (usually $\mathcal{R}=\mathbb{Z}[t^{\pm \frac{1}{D}}]$ for some natural number $D$). A *state model* on $\mathfrak{G}$ assigns to each graph $G=(V,E)\in \mathfrak{G}$ ($V$ is the vertex set, $E$ is the edge set) a *state-sum* $$Z(G)=\sum_{f\in \textrm{St}(G)}Z(f)=\sum_{f\in \textrm{st}(G)}Z(f)\in \mathcal{R}$$ with $Z(f)=\Delta \cdot \beta (f)\in \mathcal{R}$. The factor $\Delta \neq 0$ is a *global* contribution defined from the *geometry* and possible decorations of the graph but does not depend on the coloring. The set $\textrm{St}(G)\subset \{f: E\rightarrow \mathbb{Z}\}$ ($\mathbb{Z}$ could be replaced by any countable set) is a set of *edge-colorings*, the states of the state model. The factors $\beta (f):=\prod_{v\in V}\beta_v(f)\in \mathcal{R}$, are defined *locally*. This means that $\beta_v(f)$ depends only on edge-colorings of edges incident with $v$ or with adjacent vertices. The set of *contributing states* or *admissible states* (see [@T]) $\textrm{st}(G):=\{f\in \textrm{St}|\beta (f)\neq 0\}\subset \textrm{St}(G)$ is always finite so that $Z(G)$ is defined. The condition $f\in \textrm{st}(G)$ is determined by local conditions on $f$, conditions on the colorings at vertices. Note that $\beta (f)\neq 0 \Longleftrightarrow \beta_v(f)\neq 0 \ \textrm{for all}\  v$.
:::

::: rem
\(a\) Decoration on a graph includes direction, signs or numbers attached to vertices and/or edges. Those decorations are not to be confused with the edge-colorings.

\(b\) The above definition focuses on vertex contributions and is adapted to state sums on braid projections. In the link projection case, additionally colorings at extrema are included in the definition of $\beta (f)$. This is necessary so that the state sums define isotopy invariants.
:::

::: defn
[]{#defn: equivalency label="defn: equivalency"} Let $\mathfrak{G}_1,\mathfrak{G}_2$ be two sets of finite decorated graphs and corresponding state models $Z_1,Z_2$. Let $\Phi: \mathfrak{G}_1\rightarrow \mathfrak{G}_2$. Suppose that for each $G\in \mathfrak{G}_1$ there is a surjective map of corresponding state sets $\phi_G: \textrm{St}_1(G)\rightarrow \textrm{St}_2(\Phi (G))$ such that for each $f\in \textrm{St}_2(\Phi(G))$ we have $$Z_2(f)=\sum_{g\in \textrm{st}_1(G): \phi _G(g)=f}Z_1(g)$$ Then we will say that the state model $Z_1$ *dominates* the state model $Z_2$ *over* $(\Phi ,\phi =(\phi_G))$. If all maps $\phi_G$ are all bijections (so in particular restrict to bijections $\textrm{st}_1(G)\rightarrow \textrm{st}_2(\Phi (G))$ then we call the two state models *equivalent over* $\Phi$.
:::

::: rem
Equivalence of the state-sum models can be stronger than equality of the state-sums in $\mathcal{R}$. Note that it follows that the sets of admissible states for a graph $G$ and its image $\Phi (G)$ correspond to each other under the bijection $\phi _G$.
:::

::: defn
[]{#defn:edge coloring label="defn:edge coloring"} An edge-coloring on a digraph $G$ is a $\mathbb{Z}$-*flow* if $$\sum_{e\ \textrm{ingoing}\ v}f(e)=\sum_{e\ \textrm{outgoing}\ v}f(e)=:f(v).$$ Let $\mathcal{F}(G)$ denote the set of all $\mathbb{Z}$-flows on $G$. It is called a *flow* if the image of $f$ is in $\mathbb{N}_0:=\{0,1,2,,\ldots \}$. An $n$-*flow* is a flow with $f(v)\leq n$ for all vertices $v$, i. e. $f(v)\in \{0,1,\ldots ,n\}=:\underline{n}$. The set of flows respectively $n$-flows on a digraph $G$ is denoted by $\mathcal{F}(G)$ respectively $\mathcal{F}_n(G)$. Let $\mathcal{F}^n(G)$ denote the set of flows $f$ on $G$ with $f(e)\in \underline{n}$ for all $n$, the $n$-*bounded* flows. Note: $\mathcal{F}(G)\supset \mathcal{F}^n(G)\supset \mathcal{F}_n(G)$.
:::

::: exmp
The flow set $\mathcal{F}_1(G)$ is in bijective correspondence with the set of unions of vertex-disjoint directed cycles of $G$.
:::
