---
doc_id: arxiv-2601.05136v2
doc_title: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant"
section_id: sec-015-the-classical-action
section_title: "The classical action"
section_number: null
pages: 13-15
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.535
doc_brief: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant — Previous work of the author and N."
---
[]{#sec:The classical action label="sec:The classical action"}

Here we define an action $\act{D}{}$ corresponding to the $N\to
\infty$ limit of $\actq{D}{}$. Set $$\label{eq:crossing log}
  \begin{aligned}
    \crossingfunctionclass{+}{t_{1}, t_{2}, t_{3}, t_{4}}
    &\mathrel{:=}
    \dll{t_{4} - t_{1}}
    +
    \dll{t_{2} - t_{3}}
    \\
    &\phantom{\mathrel{:=}}
    -
    \dll{t_{2} - t_{1}  + 1 }
    -
    \dll{t_{4} - t_{3} }
    \\
    &\phantom{\mathrel{:=}}
    - \tu(t_{2} - t_{1})
    \\
    \crossingfunctionclass{-}{t_{1}, t_{2}, t_{3}, t_{4}}
    &\mathrel{:=}
    -
    \dll{t_{1} - t_{4} + 1}
    -
    \dll{t_{3} - t_{2} + 1}
    \\
    &\phantom{\mathrel{:=}}
    +
    \dll{t_{1} - t_{2}}
    +
    \dll{t_{3} - t_{4} + 1}
    \\
    &\phantom{\mathrel{:=}}
    + \tu(t_{2} - t_{1})
  \end{aligned}$$ Assign complex variables $t_{i}$ to the segments as before and construct a function $\act{D}{t}$ by taking a sum over crossing functions $$\begin{aligned}
  \label{eq:crossing positive class}
  \begin{tikzpicture}[line width=1, baseline=10, scale=1]
    \draw[->] (0,0) node[left] {\(t_{2}\)} to [out=00,in=180](1.5,1) node[right] {\(t_{4}\)};
    \draw[white, line width=10] (0,1) node[left] {} to [out=00,in=180](1.5,0) node[right] {};
    \draw[->] (0,1) node[left] {\(t_{1}\)} to [out=00,in=180](1.5,0) node[right] {\(t_{3}\)};
    
    
    
    
  \end{tikzpicture}
  \to
  \crossingfunctionclass{+}{t_{1}, t_{2}, t_{3}, t_{4}}
  \\
  \label{eq:crossing negative class}
  \begin{tikzpicture}[line width=1, baseline=10, scale=1]
    \draw[->] (0,1) node[left] {\(t_{1}\)} to [out=00,in=180](1.5,0) node[right] {\(t_{3}\)};
    \draw[white, line width=10] (0,0) node[left] {} to [out=00,in=180](1.5,1) node[right] {};
    \draw[->] (0,0) node[left] {\(t_{2}\)} to [out=00,in=180](1.5,1) node[right] {\(t_{4}\)};
  \end{tikzpicture}
  \to
  \crossingfunctionclass{-}{t_{1}, t_{2}, t_{3}, t_{4}}
\end{aligned}$$ and assigning critical points shifts in the variables (which we could also think of as $\delta$ functions) $$\begin{aligned}
  &
  \begin{tikzpicture}[line width=1, baseline=10, scale=1]
    \draw[->, looseness = 1.5] (0,0) node[right] {\(t\)} to [out
    =180, in=180] (0,1) node[right] {\(t\)};
  \end{tikzpicture}
  &
  &
  \begin{tikzpicture}[line width=1, baseline=10, scale=1]
    \draw[->, looseness = 1.5] (0,0) node[left] {\(t\)} to [out =0,
    in=0] (0,1) node[left] {\(t\)};
  \end{tikzpicture}
  &
  &
  \begin{tikzpicture}[line width=1, baseline=10, scale=1]
    \draw[<-, looseness = 1.5] (0,0) node[right] {\(t - 1\)} to [out
    =180, in=180] (0,1) node[right] {\(t\)};
  \end{tikzpicture}
  &
  &
  \begin{tikzpicture}[line width=1, baseline=10, scale=1]
    \draw[<-, looseness = 1.5] (0,0) node[left] {\(t + 1\)} to [out
    =0, in=0] (0,1) node[left] {\(t\)};
  \end{tikzpicture}
\end{aligned}$$

::: definition
The construction above defines the as a holomorphic function $$\act{D}{} \colon \Omega_{D} \to \mathbb{C}$$ where $$\Omega_{D} =
    \left\{ \def\given{\ \middle| \ }  
      t \in \mathbb{C}^{E}
      \given
      t_{i} - t_{j} \not \in X
      \text{ whenever \(i,j\) meet at a corner of \(D\)}
     \right\}$$
:::

The classical action is a variant of Yokota's introduced in [@arXiv:math/0009165] and used throughout the Volume Conjecture literature. We prefer to call it an *action* to match the language used in physics, since it is essentially the Chern-Simons action if we view $\Omega_{D}$ as parametrizing flat $\mathfrak{sl}_{2}$ connections on the knot complement. Our action includes parameter shifts that appear to be related to the normalization terms $\Omega_{1}, \Omega_{2}$ studied by @zbMATH06433029 [@zbMATH06433029].

::: definition
A $\gamma \in
  \mathbb{C}^{E}$ of the classical action is one where $$\exp
    \left.
    \frac{
      \partial \act{D}{}
    }{
      \partial t_{i}
    }
    \right|_{\gamma}
    =
    1
    \text{ for all } i \in E.$$ or equivalently, a point for which there is a $k \in \mathbb{Z}^{E}$ with $$\left.
    \frac{
      \partial \act{D}{}
    }{
      \partial t_{i}
    }
    \right|_{\gamma}
    =
    \tu
    k_{i}
    \text{ for all } i \in E.$$
:::

::: proposition
[]{#thm:crit points are reps label="thm:crit points are reps"} Let $D$ be a diagram of a knot $K$. Generalized critical points of $\act{D}{}$ are in bijection with normalized non-pinched shadow colorings $(\rho,u)$ of $D$ with meridian eigenvalue $1$. If $\gamma$ is the critical point corresponding to $(\rho, u)$, then its critical value is the $\slg$ Chern-Simons invariant of $\rho$ (which is independent of $u$). In the notation of [@McPhailSnyderVolume], $$\exp \act{D}{\gamma} = \mathcal{I}^{\psi}(K, \rho, u).\qedhere$$
:::

::: proof
*Proof.* shows that generalized critical points are equivalent to the segment equations for $m = 1$, so we can apply [\[thm:segment solutions are reps\]](#thm:segment solutions are reps){reference-type="ref" reference="thm:segment solutions are reps"}. The second claim was worked out in detail by @zbMATH06370282 [@zbMATH06370282]. We explain the idea in our notation. In [@McPhailSnyderVolume] the Chern-Simons invariant $\log \mathcal{I}^{\psi}$ is defined by taking a sum of contributions over crossings. However, instead of using the crossing functions [\[eq:crossing log\]](#eq:crossing log){reference-type="eqref" reference="eq:crossing log"} defined in terms of $\dll{}$ [@McPhailSnyderVolume] uses lifted dilogarithms $$\lambda(\zeta)
    =
    \dll{\zeta} + \zeta \log(1 - e^{\tu \zeta})$$ In general the extra terms $\zeta \log(1 - e^{\tu \zeta})$ are nontrivial: they correspond to the gluing equations. At a critical point $\gamma$ these are satisfied and the extra terms vanish modulo $\mathbb{Z}$. ◻
:::

::: remark
[]{#rem:flattening vector label="rem:flattening vector"} @Neumann2004 gave an algebraic method to compute the $\slg$ Chern-Simons invariant of a triangulated manifold. The hyperbolic structure on $M$ is encoded using a solution of Thurston's gluing equations as usual, but his method requires an additional choice of combinatorial data called a . This is a coherent choice of logarithms of the shape parameters satisfying a logarithmic form of the gluing equations. For an octahedral decomposition the only nontrivial flattening equations come from the segment equations and are of the form $$\pm \mu + \log(1 - z_{j}) -  \log(1 - z_{j'})
    =
    \pm \mu + \log(1 - z_{l}) -  \log(1 - z_{l'})
    + k_{i}$$ for an integer $k_{i}$ at each segment. These are precisely the integers appearing in the flattening vector above.
:::
