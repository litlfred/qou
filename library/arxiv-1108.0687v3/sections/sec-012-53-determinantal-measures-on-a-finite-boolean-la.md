---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures"
section_id: sec-012-53-determinantal-measures-on-a-finite-boolean-la
section_title: "Determinantal measures on a finite Boolean lattice"
section_number: 5.3
pages: 17-18
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.983
doc_brief: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures — Let {X1, . . ."
---
[]{#ss:finite label="ss:finite"}

We say that a probability measure ${\mathbb P}$ on ${\mathcal B}_n$ is **determinantal** (in the general sense) if there is an $n \times n$ real or complex matrix $K$ such that that for every $S \subseteq \{ 1 , \ldots , n \}$, $$\label{eq:det}
{\mathbb E}\prod_{j \in S} X_j = \det K_S$$ where $K_S$ is the submatrix of $K$ obtained by choosing only those rows and columns whose index is in $S$. In this definition, the phrase "general sense" refers to the lack of further assumptions on $K$. An important subclass is the **Hermitian** determinantal measures, for which the matrix $K$ is Hermitian. In this paper we will be interested only in the Hermitian case and will use the term **determinantal** hereafter to refer only to the case where $K$ is Hermitian. Determinantal measures are known to be negatively associated [@lyons03 Theorem 6.5]. In fact they are strong Rayleigh [@borcea-branden-liggett proof of Theorem 3.4] and therefore satisfy the stochastic covering property.

::: example
[]{#eg:spanning tree 2 label="eg:spanning tree 2"} As previously remarked, the uniform or weighted random spanning tree is a determinantal measure.
:::

In the next section we will extend the notion of a determinantal measure to the continuous setting. The extension to a countably infinite set of variables is more straightforward: the kernel $K$ is now indexed by a countably infinite set, but [\[eq:det\]](#eq:det){reference-type="eqref" reference="eq:det"} may be interpreted as holding for all finite sets $S$. The following example of a determinantal process on $\mathbb{Z}$ appeared first in [@johansson03].

::: example
[]{#eg:nonintersecting RW label="eg:nonintersecting RW"} Let $\{ Y^{(k)} : 1 \leq k \leq n \}$ be $n$ independent time homogeneous nearest neighbor random walks on $\mathbb{Z}$. Begin the walks at locations $y_1 , \ldots , y_n$ and suppose the event that the walks are all at their starting positions at time $2n$ and have not intersected has positive probability. Conditional on this event, the positions at time $n$ form a determinantal measure. That is, the indicator functions $\{ X_j \}$ have a determinantal law, where $X_j = 1$ if some $Y^{(k)}$ is at position $j$ at time $n$, and zero otherwise.
:::

::: unremark
The positions of non-colliding random walks are given by a determinant under more general conditions (see [@karlin-mcgregor]). The present situation is arranged so as to make the kernel Hermitian.
:::
