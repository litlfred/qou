---
doc_id: arxiv-2601.05136v2
doc_title: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant"
section_id: sec-005-diagrams-and-colorings
section_title: "Diagrams and colorings"
section_number: null
pages: 5-6
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
toc_source: outline
text_source: latex
latex_prose_ratio: 0.9
latex_coverage_ratio: 0.938
doc_brief: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant — Previous work of the author and N."
---
[]{#sub:Diagrams label="sub:Diagrams"}

::: definition
A of a knot $K$ is a representation $\rho \colon \pi_{1}(\comp{K}) \to \slg$ and a choice of eigenspace for the image of each peripheral subgroup of $K$ under $\rho$.
:::

More formally, given a choice of peripheral subgroup $\Pi \subset
\pi_{1}(\comp{K})$ a decoration is an eigenspace $L \subset
\mathbb{C}^{2}$ of $\rho(\Pi)$, which we take to be a right eigenspace. This does not depend on the choice of peripheral subgroup: any other choice is a conjugate $y^{-1} \Pi y$ and the corresponding eigenspace is $L \rho(y)$. An orientation of $K$ determines a meridian $\mer \in \Pi$ and the decoration $L$ determines an eigenvalue $m \in \mathbb{C}^{\times}$ by $$v \rho(\mer) = m^{-1} v$$ where $v$ is any nonzero element of $L$. The inverse is unfortunate but correct and is chosen to match the conventions of [@McPhailSnyderAlgebra; @McPhailSnyderVolume]. Clearly $m$ does not depend on the choice of $\Pi$.

::: definition
Let $K$ be an oriented, framed knot in $S^{3}$. An of $K$ is an oriented, blackboard-framed tangle diagram $D$ with one incoming and one outgoing boundary component whose closure is a diagram of $K$. The of $D$ are the edges of its underlying graph. We call the two segments incident to the boundary of the tangle the , call the remainder the , and write $E$ for the set of internal segments of $D$. Writing $\operatorname{cr}(D)$ for the crossing number of the diagram we have $2 \operatorname{cr}(D) = |E| + 1$.
:::

::: definition
A is a pair $(g, [v]) \in \slg \times
  \pjsp$ of a matrix $g$ and a right eigenspace $[v]$ for $g$. The of $(g, [v])$ is the $m
  \in \mathbb{C}^{\times}$ satisfying $$vg = m^{-1} v.$$ We define a binary operation on decorated matrices by $$(g, [v]) \qn (h, [w])
    \mathrel{:=}
    (h^{-1} g h, [v h])$$ A of a tangle diagram $D$ assigns decorated matrices to every arc of $D$ subject to the crossing relations $$\begin{aligned}
      &
      \begin{tikzpicture}[line width=1, baseline=30, scale=1]
        \draw[->] (0,0) node[left] {\(g_{2}\)} to [out=00,in=180](1.5,1)
        node[right] {\(g_{2} \qn g_{1}\)};
        \draw[white, line width=10] (0,1) node[left] {} to [out=00,in=180](1.5,0)
        node[right] {};
        \draw[->] (0,1) node[left] {\(g_{1}\)} to [out=00,in=180](1.5,0)
        node[right] {\(g_{1}\)};
      \end{tikzpicture}
      &
      &
      \begin{tikzpicture}[line width=1, baseline=30, scale=1]
        \draw[->] (0,1) node[left] {\(g_{1}\)} to [out=00,in=180](1.5,0)
        node[right] {\(g_{1} \qninv g_{2}\)};
        \draw[white, line width=10] (0,0) node[left] {} to [out=00,in=180](1.5,1)
        node[right] {};
        \draw[->] (0,0) node[left] {\(g_{2}\)} to [out=00,in=180](1.5,1)
        node[right] {\(g_{2}\)};
      \end{tikzpicture}
    \end{aligned}$$ where $\qninv$ is the inverse of $\qn$ defined by $(g, [v]) \qninv (h, [w])
    \mathrel{:=}
    (h g h^{-1}, [v h^{-1}]).$ We always require that a $\slg$-coloring of an open diagram assigns the same decorated matrix to both boundary segments, or equivalently that it gives a well-defined coloring of the closure.
:::

The Wirtinger presentation of $\pi_{1}(\comp{K})$ makes it clear that decorated representations of $K$ are in bijection with decorated $\slg$-colorings of $D$ so we denote both by $\rho$. To define our invariant we need to make an additional choice of diagram-dependent gauge data. The value of $\qinv{}$ is independent of this choice.

::: definition
A $(\rho, u)$ of a diagram $D$ is a decorated $\slg$-coloring $\rho$ of $D$ along with an assignment $u \colon j \mapsto u_{j}$ of column vectors $u_{j} \in
  \mathbb{C}^{2}$ to the regions $j$ of $D$, subject to the rule $$\begin{tikzpicture}[line width=1, baseline=00, scale=1]
      \draw[->] (0,0) node[left] {\((g, [v])\)} to (1.5,0) node[right] {};
      \node[above] at (.75,0.25){\(u\)};
      \node[below] at (.75,-0.25){\(g u\)};
    \end{tikzpicture}$$ In the diagram above we say the region labeled by $u$ is the segment.
:::

It is not hard to see that a shadow coloring is determined uniquely by the vector $u_{0} \in \mathbb{C}^{2}$ assigned to the topmost region of $D$ (or to any other region).

::: definition
A shadow coloring of a diagram $D$ defines $$a_{j} \mathrel{:=}\evec{1} u_{j}
    \text{ for each region \(j\)}$$ and $$b_{i} \mathrel{:=}
    -
    \frac{
      v_{i} \evec{2}
    }{
      v_{i} u_{i^{\uparrow}}
    }
    \text{ for each segment \(i\)}$$ where $i^{\up}$ is the region above segment $i$: $$\begin{tikzpicture}[line width=1, baseline=00, scale=1]
      \draw[->] (0,0) node[left] {\((g_{i}, [v_{i}])\)} to (1.5,0)
      node[right] {};
      \node[above] at (.75,0.25){\(u_{i^{\uparrow}}\)};
    \end{tikzpicture}$$ If none of the region or segment parameters are $0$ or $\infty$ we say the shadow coloring is .
:::

::: definition
A shadow coloring $(\rho, u)$ of an open diagram $D$ is if it is admissible and the segment parameter assigned to the open segments is $1$.
:::

Clearly one can always choose a normalized coloring by rescaling the vectors $u_{i}$. This is a special case of the type (B) gauge transformation defined below.
