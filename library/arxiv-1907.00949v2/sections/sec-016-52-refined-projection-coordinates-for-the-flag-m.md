---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-016-52-refined-projection-coordinates-for-the-flag-m
section_title: "Refined projection coordinates for the flag manifold"
section_number: 5.2
pages: 18-19
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.927
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
[]{#sec:rproj label="sec:rproj"}

We discuss a variation of projection coordinates on flag manifolds based on Proposition [\[prop:geometric structure\]](#prop:geometric structure){reference-type="ref" reference="prop:geometric structure"}[\[it:cls2\]](#it:cls2){reference-type="eqref" reference="it:cls2"}. As in Section [\[sec:proj\]](#sec:proj){reference-type="ref" reference="sec:proj"}, if we identify the Grassmannians as sets of projection matrices as in [\[eq:P\]](#eq:P){reference-type="eqref" reference="eq:P"}, then the map in [\[eq:j2\]](#eq:j2){reference-type="eqref" reference="eq:j2"} becomes $$\label{eq:embedding of flag}
\varepsilon': \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n) \to \mathbb{R}^{nd \times nd},\quad \{\mathbb{V}_i\}_{i=1}^d \mapsto \mathop{\mathrm{diag}}(W_1W_1^{\scriptscriptstyle\mathsf{T}},\dots, W_dW_d^{\scriptscriptstyle\mathsf{T}}),$$ where column vectors of $W_i\in \mathbb{R}^{n\times (n_i - n_{i-1})}$ form an orthonormal basis of $\mathbb{V}_{i-1}^{\perp}$, the orthogonal complement of $\mathbb{V}_{i-1}$ in $\mathbb{V}_i$, $i =1,\dots,d$. This gives us another description of $\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ as a matrix manifold, an analogue of Proposition [\[prop:representation of flags\]](#prop:representation of flags){reference-type="ref" reference="prop:representation of flags"}.

::: proposition
[]{#prop:reduced coord label="prop:reduced coord"} The flag manifold $\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ is diffeomorphic to $$\label{eq:Rflag}
\lbrace
R = \mathop{\mathrm{diag}}(R_1,\dots, R_d)\in \mathbb{R}^{nd \times nd}: R_i^2 = R_i = R_i^{\scriptscriptstyle\mathsf{T}},\; \mathop{\mathrm{tr}}(R_i) = n_i - n_{i-1},\; R_i  R_j = 0,\;  i < j
\rbrace.$$
:::

We call the representation in Proposition [\[prop:reduced coord\]](#prop:reduced coord){reference-type="ref" reference="prop:reduced coord"} *reduced projection coordinates* on the flag manifold $\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$. Again, it is straightforward to translate between the other three coordinates systems and reduced projection coordinates. This readily yields expressions for metric, tangent space, geodesic, and parallel transport in reduced projection coordinates as before. We will state those for tangent space and metric as examples.

::: proposition
[]{#prop:tangent3 label="prop:tangent3"} Let $R = \mathop{\mathrm{diag}}(R_1,\dots,R_d) \in \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ be as represented in [\[eq:Rflag\]](#eq:Rflag){reference-type="eqref" reference="eq:Rflag"}. Then the tangent space is given by $$\begin{gathered}
\label{eq:tangent3}
T_R\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n) = \lbrace  Z =\mathop{\mathrm{diag}}(Z_1,\dots,Z_d) \in \mathbb{R}^{nd\times nd} :
R_i Z_i + Z_i R_i = Z_i = Z_i^{\scriptscriptstyle\mathsf{T}},\\ \mathop{\mathrm{tr}}(Z_i) = 0, \; Z_i R_j + R_i Z_j =0,\;1\le i < j \le d. \rbrace
\end{gathered}$$
:::

Propositions [\[prop:reduced coord\]](#prop:reduced coord){reference-type="ref" reference="prop:reduced coord"} and [\[prop:tangent3\]](#prop:tangent3){reference-type="ref" reference="prop:tangent3"} give an alternative way to obtain the metric $g$ in Proposition [\[prop:metric\]](#prop:metric){reference-type="ref" reference="prop:metric"}. Let $g_i$ be the standard metric on $\mathop{\mathrm{Gr}}(n_i-n_{i-1},n)$, $i=1,\dots,d$. Then it is straightforward to verify that $g$ is the pull-back of $\sum_{i=1}^d g_i$ via the embedding [\[eq:j2\]](#eq:j2){reference-type="eqref" reference="eq:j2"} in Proposition [\[prop:geometric structure\]](#prop:geometric structure){reference-type="ref" reference="prop:geometric structure"}[\[it:cls2\]](#it:cls2){reference-type="eqref" reference="it:cls2"}. This also gives us an expression for the metric in terms of reduced projection coordinates.

::: proposition
[]{#prop:metric3 label="prop:metric3"} Let $R = \mathop{\mathrm{diag}}(R_1,\dots, R_d) \in \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ be as in [\[eq:Rflag\]](#eq:Rflag){reference-type="eqref" reference="eq:Rflag"}. Let $W= \mathop{\mathrm{diag}}(W_1,\dots,W_d),Z =\mathop{\mathrm{diag}}(Z_1,\dots,Z_d)\in T_R \mathop{\mathrm{Flag}}(n_1,\dots, n_d;n)$ be as in [\[eq:tangent3\]](#eq:tangent3){reference-type="eqref" reference="eq:tangent3"}. Then there exist $V_i, A_i, B_i\in \mathbb{R}^{n\times (n_i - n_{i-1})}$ such that $$\label{eq:VAB}
V_i V_i^{\scriptscriptstyle\mathsf{T}}= R_i,\; V_i^{\scriptscriptstyle\mathsf{T}}V_i = I_{n_i - n_{i-1}}, \;
V_i A_i^{\scriptscriptstyle\mathsf{T}}+ A_i V_i^{\scriptscriptstyle\mathsf{T}}= W_i,\;
V_i^{\scriptscriptstyle\mathsf{T}}A_i = 0,\;
V_i B_i^{\scriptscriptstyle\mathsf{T}}+ B_i V_i^{\scriptscriptstyle\mathsf{T}}= Z_i,\;
V_i^{\scriptscriptstyle\mathsf{T}}B_i = 0,$$ and the metric $g$ is given by $$g_R(W,Z) =  \sum_{i=1}^d   \mathop{\mathrm{tr}}(A_i^{\scriptscriptstyle\mathsf{T}}B_i).$$
:::

::: proof
*Proof.* As the Grassmannian is just a flag manifold with $d=1$, all our earlier discussions about Stiefel and projection coordinates also apply to it. So for $W_i,Z_i \in T_{R_i} \mathop{\mathrm{Gr}}(n_i-n_{i-1},n)$ in projection coordinates, there exist $V_i, A_i, B_i\in \mathbb{R}^{n\times (n_i - n_{i-1})}$ satisfying [\[eq:VAB\]](#eq:VAB){reference-type="eqref" reference="eq:VAB"}. The standard Riemannian metric $g_i$ on $\mathop{\mathrm{Gr}}(n_i-n_{i-1},n)$ at $R_i$ is then given by $g_i (W_i,Z_i) =  \mathop{\mathrm{tr}}( A_i^{\scriptscriptstyle\mathsf{T}}B_i)$ and thus we have $$g_R(W,Z) = \sum_{i=1}^d g_i (W_i,Z_i) = \sum_{i=1}^d   \mathop{\mathrm{tr}}(A_i^{\scriptscriptstyle\mathsf{T}}B_i). \qedhere$$ ◻
:::
