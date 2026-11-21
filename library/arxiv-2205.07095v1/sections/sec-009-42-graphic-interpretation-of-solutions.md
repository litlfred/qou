---
doc_id: arxiv-2205.07095v1
doc_title: "Virial Expansions for Correlation Functions in Canonical Ensemble"
section_id: sec-009-42-graphic-interpretation-of-solutions
section_title: "Graphic interpretation of solutions."
section_number: 4.2
pages: 10-13
source_pdf: 2205.07095v1.pdf
source_sha256: 2ec6916399150e2d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.982
doc_brief: "Virial Expansions for Correlation Functions in Canonical Ensemble — The inﬁnite set of coupled integral nonlinear equations for correlation func- tions in the case of classical canonical ensemble is"
---
As in the case of the Kirkwood-Salzburg equations for a large canonical ensemble (see details in [@Re2021]) the analytical expression of the kernel $T (\eta|\gamma)$ can be given as contributions of forest-graphs. The number $N (m | n), m = |\eta|, n = |\gamma|$ all forest graphs can be calculated by solving the following recurrent equation: $$\label{Numberforests-vir}
N(m|n)=\sum_{k=0}^n {n \choose k}N(m+k-1|n-k)+\sum_{k=1}^n {n \choose k}N(m|n-k)\sum_{l=1}^k {k \choose l}N(l|k-l).$$ If we reject the nonlinear term, the recurrent equation can be solved exactly: $N (m | n) = m (m + n)^{n-1}$ (see [@Re2021]). This formula makes it possible to prove the convergence of the integral [\[SSCA-2\]](#SSCA-2){reference-type="eqref" reference="SSCA-2"} at $j = 1$ and small density values. But the nonlinear term apparently significantly increases the number of forest graphs. But according to the formula [\[final\]](#final){reference-type="eqref" reference="final"}, each contribution of the forest graph, which contains a tree with the contribution of the factor $K (x_1; \xi), \xi \in \gamma$, which appears from the second sum in [\[final\]](#final){reference-type="eqref" reference="final"} is included with a minus sign. So, for example calculating $$\label{T11}
    T(x_1|y)\;=\; \varrho^2\left[ K(x_1;y)\;-\;K(x_1;y)\right]=0.$$ Therefore, it is necessary to analyze this recurrent relationship in more detail. It is easy to get the following proposition.

::: prop
[]{#dens label="dens"} From initial conditions [\[incon0\]](#incon0){reference-type="eqref" reference="incon0"}-[\[incon1\]](#incon1){reference-type="eqref" reference="incon1"} it follows that $$\label{den1}
   T(x_1|\emptyset)\;=\;\varrho,\;\;T(x_1|\gamma)\;=\;0\;\text{for}\;\gamma\neq\emptyset.$$ It gives the needed equality for density $\rho(x_1)\;=\;\varrho$.\
In addition $T(\eta|\emptyset)\;=\;\varrho^{|\eta|}\exp[-\beta U(\eta)]$.
:::

The *proof* follows from [\[final\]](#final){reference-type="eqref" reference="final"} by induction procedure. To obtain the solution of [\[final\]](#final){reference-type="eqref" reference="final"} in the language of graph theory [@Ste64; @Gro67] define the set graphs $\mathcal{D}(\eta; \gamma)$.

::: remark
[]{#graph label="graph"} The set $\mathcal{D}(\eta; \gamma)$ is the set of rooted graph, connected components of which are 2-connected graphs with respect to configuration $\gamma$. Any graph $G\in\mathcal{D}(\eta; \gamma)$ has $m=|\eta|$ vertices of configuration $\eta$ and $n=|\gamma|$ vertices of configuration $\gamma$. Every vertex of $\eta$ can be free of lines or can connect only with vertices $y$ of configuration $\gamma$. Every vertex $y\in\gamma$ connects with vertices $x$ or $y$ by at least two lines. This definitions is very close to definitions of the set of white and black vertices $\mathcal{D}(W; B)$ in [@Ja21], Section 2. The role of the roots of the graph is performed by the configuration $\eta$. A singleton $G\in\mathcal{D}(x_1; \emptyset)$. The contribution of any vertex is $\varrho$. The contribution of line $w(l_{xy})$, which connected two vertices $x$ and $y$ or $y_i$ and $y_j$ is $K(x;y)$.
:::

::: remark
[]{#graph1 label="graph1"} According to [\[SSCA-2\]](#SSCA-2){reference-type="eqref" reference="SSCA-2"}, integration is performed at the points of configuration $\gamma$, and according to equation [\[final\]](#final){reference-type="eqref" reference="final"}, in the kernels $T(\theta; \xi)$, the configuration $\xi\subseteq\gamma$, and the configuration $\theta$ can contain both variables from $\eta$ and $\gamma$. Therefore, the corresponding graphs of sets $\mathcal{D}(\theta; \xi)$ can contain only black vertices.
:::

The main statement of the section is

::: prop
[]{#dens label="dens"} The solution of the recurrence relation [\[final\]](#final){reference-type="eqref" reference="final"} can be rewritten by contributions from the graphs of the set $\mathcal{D}(\eta; \gamma)$: $$\label{den1}
   T(\eta|\gamma)\;=\;\varrho^{|\eta|+|\gamma|}\exp[-\beta U(\eta)] \sum_{G\in\mathcal{D}(\eta; \gamma) }w_G(L; \eta, \gamma),$$ where $L$ is a configuration of lines(edges).
:::

The main points of *proof*. The proof is based on the induction procedure. It is very easy to see the cancellation of the contributions of the corresponding graphs, for example, for kernels $T(x_1, x_2|y_1)$ and $T(x_1, x_2|y_1, y_2)$. To facilitate these calculations, it is better to consider instead of the equation [\[final\]](#final){reference-type="eqref" reference="final"} the equation for kernels that are integrated in variables $y_1,..., y_n$:

$$\label{kern2}
   \widehat{T}(\eta|n):=\int_{\Gamma^{(n)}} T(\eta|\gamma)d\gamma =\int_{\Bbb R^{dn}} (dy)^nT(\eta|\{y\}_1^n),$$ especially since this is the value that must be substituted into the formula for the solution [\[SSCA-2\]](#SSCA-2){reference-type="eqref" reference="SSCA-2"}. $$\begin{aligned}
\label{final2}
\widehat{T}(\eta|n)&=\varrho  e^{-\beta W(x_1; \eta^{(\hat{x}_1)})}\sum_{k=0}^n {n \choose k}
\int (dy)^k K(x_1;\{y\}_1^k)\widehat{T}(\eta^{(\hat{x}_1)}\cup\{y\}_1^k)|n-k)-\notag \\
&-\sum_{k=1}^n {n \choose k}\sum_{l=1}^k {k \choose l}\int (dy)^l K(x_1;\{y\}_1^l)\widehat{T}(\eta|n-k)\widehat{T}(\{y\}_1^l|k-l).
\end{aligned}$$ For $k=0$ in the first line of formula [\[final2\]](#final2){reference-type="eqref" reference="final2"}, the term $\widehat{T}(\eta^{(\hat{x}_1)}|n)$ corresponds to the analytical contribution of all graphs $\mathcal{D}(\eta; \gamma)$, in which the vertex $x_1$ has no edges. For $k\geq 1$ the set of graphs for $\widehat{T}(\eta^{(\hat{x}_1)}\cup\{y\}_1^k)|n-k)$ is arranged in such a way that $k$ vertices from $n$ vertices of the configuration $\gamma$ are transformed into vertices, which are connected to the graphs of $\widehat{T}(\eta^{(\hat{x}_1)}|n-k)$ either by means of lines or as free vertices. If a vertex $y_i$ is already connected by at least one line, then joining a line with vertex $x_1$ leaves this graph in the set $\mathcal{D}(\eta; \gamma)$. If the vertex did not have edges, then operation $\int (dy)^l K(x_1;\{y\}_1^l)$ does not ensure that it belongs to the set $\mathcal{D}(\eta; \gamma)$, and such a diagram should be reduced.This is ensured by the presence of a similar contribution in the second line of the formula [\[final2\]](#final2){reference-type="eqref" reference="final2"}. This variant occurs in $l$ of $k$ cases for each of the graphs in $\widehat{T}(\eta|n-k)$. $\blacksquare$
