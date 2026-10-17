---
doc_id: arxiv-2601.05136v2
doc_title: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant"
section_id: sec-006-gauge-transformations-and-nondegeneracy
section_title: "Gauge transformations and nondegeneracy"
section_number: null
pages: 6-8
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.979
doc_brief: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant — Previous work of the author and N."
---
[]{#sec:Gauge transformations and admissibility label="sec:Gauge transformations and admissibility"}

The diagram $D$ determines a semi-ideal triangulation $\mathcal{T}_{D}$ of $\comp{K}$ (with two non-ideal points) called the ; we refer to [@Kim2018] for a detailed discussion and [@McphailSnyder2022hyperbolicstructureslinkcomplements; @McphailSnyder2024octahedralcoordinateswirtingerpresentation] for the relationship to our parameters. $\mathcal{T}_{D}$ assigns each crossing of $D$ four tetrahedra, with one in each corner of the crossing. The segment parameters naturally parametrize hyperbolic structures on these tetrahedra in terms of $z_{k}$. Labeling the segments and corners of a crossing as $$\label{eq:crossing labeled}
  \begin{tikzpicture}[line width=1, baseline=30, scale=1]
    \draw[->] (0,0) node[left] {\({2}\)} to [out=00,in=180](1.5,1) node[right] {\({2'}\)};
    
    
    \draw[->] (0,1) node[left] {\({1}\)} to [out=00,in=180](1.5,0) node[right] {\({1'}\)};
    \draw (0.75,1) node {\(\lN\)};
    \draw (0,0.5) node {\(\lW\)};
    \draw (0.75,0) node {\(\lS\)};
    \draw (1.5,0.5) node {\(\lE\)};
  \end{tikzpicture}$$ the shape parameters of the tetrahedra are given by $$\label{eq:shape parameters}
  \begin{aligned}
    z_{\operatorname{N}} &= \left( \frac{b_{2'}}{b_{1}} \right)^{\epsilon}
    &
    z_{\operatorname{S}} &= \left( \frac{b_{2}}{b_{1'}}\right)^{\epsilon}
    \\
    z_{\operatorname{W}} &= \left(\frac{b_{2}}{m b_{1}}\right)^{\epsilon}
    &
    z_{\operatorname{E}} &= \left(\frac{m b_{2'}}{b_{1'}}\right)^{\epsilon}
  \end{aligned}$$ where $\epsilon$ is the sign of the crossing. The shape parameters arise as cross ratios of the positions of the vertices in $\pjsp$. In particular a tetrahedron is geometrically degenerate when its shape parameter lies in $\left\{ \def\given{\ \middle| \ }  0, 1, \infty \right\}$.

If a shadow coloring is admissible as defined above then none of the shape parameters of $\mathcal{T}_{D}$ are $0$ or $\infty$. This is a necessary condition to define $\qinv{}$, and every representation $\rho$ is gauge-equivalent to an admissible one. Since $\qinv{}$ is gauge-invariant this allows us to define it for any $\rho$.

::: definition
[]{#def:gauge transformation label="def:gauge transformation"} Let $(\rho, u)$ be a shadow coloring of $D$ with segment colors $i \mapsto (g_{i}, [v_{i}])$ and region colors $j \mapsto u_{j}$. A of it is a coloring of the form

-   $i \mapsto (h^{-1} g_i h, L_i h)$ and $j \mapsto h^{-1} u_j$

-   $i \mapsto (g_i, L_i)$ and $j \mapsto h^{-1} u_j$

for some $h \in \slg$. We say the new colorings are the images of and gauge transformations .
:::

::: lemma
Let $\rho$ be a decorated representation and $D$ an open diagram of $K$. Any shadow coloring $(\rho, u)$ of $D$ is gauge-equivalent to one with an admissible shadow coloring.
:::

While we can ensure the shape parameters lie in $\mathbb{C}\setminus
\left\{ \def\given{\ \middle| \ }  0 \right\}$ we cannot necessarily ensure they avoid $1$. Having shape parameter $1$ is independent of the choice of shadow coloring and is equivalent to a natural condition on the decorated representation:

::: definition
A crossing with a decorated $\slg$-coloring $$\begin{tikzpicture}[line width=1, baseline=30, scale=1]
      \draw[->] (0,0) node[left] {\((g_{2}, [v_{2}])\)} to [out=00,in=180](1.5,1)
      node[right] {\((g_{2'}, [v_{2'}])\)};
      
      
      \draw[->] (0,1) node[left] {\((g_{1}, [v_{1}])\)} to [out=00,in=180](1.5,0)
      node[right] {\((g_{1'}, [v_{1'}])\)};
    \end{tikzpicture}$$ is if $[v_{1}] = [v_{2}]$, equivalently $[v_{i}] = [v_{j}]$ for any pair $(i,j)$ of adjacent segments. (Note that this condition does not depend on a choice of shadow coloring.) A coloring of a diagram is pinched if any of its crossings are. If $\rho$ is a decorated representation of $K$ and $D$ an open diagram of $K$ we say $D$ is if the coloring induced by $\rho$ is pinched (and conversely that $\rho$ is ). If no crossing is pinched we say $(D, \rho)$ is .
:::

A nugatory crossing is always pinched. If $D$ is a crossing-minimal diagram it has no nugatory crossings and in this case most (but not all) nontrivial representations $\rho$ are $D$-smooth. For example, up to gauge transformation the $8_{5}$ knot has $11$ boundary-parabolic representations [@Kim2018]. In the standard diagram $D$ [@Kim2018 Figure 28] of this knot $10$ are smooth and $1$ is pinched. $8_{5}$ is hyperbolic and its discrete faithful representation is $D$-smooth. According to the database of boundary-parabolic representations computed by @DiagramSite [@DiagramSite] this pattern holds in general: for crossing-minimal $D$ most but not all representations are $D$-smooth, but the hyperbolic holonomy representation is always smooth.

In the standard terminology a not $\rho_{\mathop{\mathrm{hyp}}}$-pinched diagram is said to be . By [@McphailSnyder2024octahedralcoordinateswirtingerpresentation Theorem 3] being essential is equivalent to a purely group-theoretic condition called . It is not hard to see that if $D$ is not arc-faithful then it is pinched for every decorated representation $\rho$. It is natural to conjecture (see [@McphailSnyder2024octahedralcoordinateswirtingerpresentation Section 5]) that any hyperbolic knot has an arc-faithful diagram. It is known that any reduced alternating diagram of a hyperbolic knot is arc-faithful.

At any pinched crossing the shape parameters are $1$ so the $R$-matrix elements defining $\qinv{}$ encounter the poles and zeros of the quantum dilogarithm. One can show that these cancel, but in a delicate way that prevents our state integrals from being well-defined. More generally to avoid the singularities we need to ensure that no shape parameter has norm $1$, and if no crossings are pinched then we can achieve this via a gauge transformation.

::: lemma
[]{#thm:avoid unit circle label="thm:avoid unit circle"} Let $\rho$ be a decorated representation of a knot $K$ and $D$ be an open diagram of $K$. Suppose that $D$ is not $\rho$-pinched. Then there is a representation $\rho'$ gauge-equivalent to $\rho$ and a shadow coloring $(\rho', u)$ of $D$ in which no shape parameter has norm $1$. In this case we say $(\rho', u)$ .
:::
