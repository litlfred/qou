---
doc_id: arxiv-2601.05136v2
doc_title: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant"
section_id: sec-010-the-action-and-state-sums
section_title: "The action and state sums"
section_number: null
pages: 9-11
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
toc_source: outline
text_source: latex
latex_prose_ratio: 0.753
latex_coverage_ratio: 0.959
doc_brief: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant — Previous work of the author and N."
---
[]{#sec:Definition of the invariant label="sec:Definition of the invariant"}

Following [@McPhailSnyderVolume Section 6] we define the action functional of a diagram. Consider the functions $$\label{eq:crossing qlog}
  \begin{aligned}
    \crossingfunction{+}{\mu}{t_{1}, t_{2}, t_{3}, t_{4}}
    &\mathrel{:=}
    \pfl{t_{4} - t_{1}}
    +
    \pfl{t_{2} - t_{3}}
    \\
    &\phantom{\mathrel{:=}}
    -
    \pfl{t_{2} - t_{1} - \mu/N+ 1 - 1/N}
    -
    \pfl{t_{4} - t_{3} + \mu/N}
    \\
    &\phantom{\mathrel{:=}}
    - \tu \mu(t_{2} + t_{3} - t_{1}- t_{4} - \mu/N)
    \\
    \crossingfunction{-}{\mu}{t_{1}, t_{2}, t_{3}, t_{4}}
    &\mathrel{:=}
    -
    \pfl{t_{1} - t_{4} + 1 - 1/N}
    -
    \pfl{t_{3} - t_{2} + 1 - 1/N}
    \\
    &\phantom{\mathrel{:=}}
    +
    \pfl{t_{1} - t_{2} + \mu/N}
    +
    \pfl{t_{3} - t_{4} - \mu/N+ 1 - 1/N}
    \\
    &\phantom{\mathrel{:=}}
    + \tu \mu(t_{2} + t_{3} - t_{1}- t_{4} - \mu/N)
  \end{aligned}$$ These are logarithmic versions of the braiding kernels of [@McPhailSnyderVolume Section 5]. As discussed there $t \mapsto \exp
\crossingfunction{\epsilon}{\mu}{t}$ is a quasi-periodic function of each $t_{i}$. The periodicity constants are related to the segment equations of [\[sec:Segment equations\]](#sec:Segment equations){reference-type="ref" reference="sec:Segment equations"}, i.e. to the gluing equations of the octahedral decomposition.

Fix an oriented framed knot $K$ and an open diagram $D$ of $K$. Assign each internal segment a complex variable $t_{i}$, assign the boundary segments $0$, and fix a complex number $\mu$ (later, a log-meridian of $K$). Construct a function $\actq{D,\mu}{t}$ of the variables $t_{i}$ by taking a sum over crossing functions $$\begin{aligned}
  \label{eq:crossing positive}
  \begin{tikzpicture}[line width=1, baseline=10, scale=1]
    \draw[->] (0,0) node[left] {\(t_{2}\)} to [out=00,in=180](1.5,1) node[right] {\(t_{4}\)};
    \draw[white, line width=10] (0,1) node[left] {} to [out=00,in=180](1.5,0) node[right] {};
    \draw[->] (0,1) node[left] {\(t_{1}\)} to [out=00,in=180](1.5,0) node[right] {\(t_{3}\)};
    
    
    
    
  \end{tikzpicture}
  \to
  \frac{1}{N}
  \crossingfunction{+}{\mu}{t_{1}, t_{2}, t_{3}, t_{4}}
  \\
  \label{eq:crossing negative}
  \begin{tikzpicture}[line width=1, baseline=10, scale=1]
    \draw[->] (0,1) node[left] {\(t_{1}\)} to [out=00,in=180](1.5,0) node[right] {\(t_{3}\)};
    \draw[white, line width=10] (0,0) node[left] {} to [out=00,in=180](1.5,1) node[right] {};
    \draw[->] (0,0) node[left] {\(t_{2}\)} to [out=00,in=180](1.5,1) node[right] {\(t_{4}\)};
  \end{tikzpicture}
  \to
  \frac{1}{N}
  \crossingfunction{-}{\mu}{t_{1}, t_{2}, t_{3}, t_{4}}
\end{aligned}$$ (the factors of $1/N$ are convenient when discussing asymptotics) and assigning critical points shifts in the variables (which we could also think of as $\delta$ functions) $$\begin{aligned}
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
    \draw[<-, looseness = 1.5] (0,0) node[right] {\(t + 1/N- 1\)}
    to [out =180, in=180] (0,1) node[right] {\(t\)};
  \end{tikzpicture}
  &
  &
  \begin{tikzpicture}[line width=1, baseline=10, scale=1]
    \draw[<-, looseness = 1.5] (0,0) node[left] {\(t + 1 - 1/N\)}
    to [out =0, in=0] (0,1) node[left] {\(t\)};
  \end{tikzpicture}
\end{aligned}$$

::: definition
We call $\actq{D, \mu}{}$ the of the diagram. Note that it depends on the diagram $D$ and on $\mu$ but *not* on a choice of representation.
:::

::: example
[]{#ex:figure eight label="ex:figure eight"} Below is an open diagram $D$ of the figure eight knot: $$\begin{tikzpicture}[line width=1, scale=1, xscale=1.5]
      \draw[<-] (0,1) node[above] {\(t_{6}\)} to [out=00,in=180](1,0) node[below] {\(t_{5}\)};
      \draw[white, line width=10] (0,0) node {} to [out=00,in=180](1,1) node {};
      \draw[->] (0,0) node[below] {\(0\)} to [out=00,in=180](1,1) node[above] {\(t_{1}\)};

      \draw[->] (1,1) node {} to [out=00,in=180](2,0) node[below] {\(t_{2}\)};
      \draw[white, line width=10] (1,0) node {} to [out=00,in=180](2,1) node {};
      \draw[<-] (1,0) node {} to [out=00,in=180](2,1) node[above] {\(t_{4}\)};

      \draw[<-] (2,1) node {} to [out=00,in=180](3,2) node {};
      \draw[white, line width=10] (2,2) node {} to [out=00,in=180](3,1) node {};
      \draw[->] (2,2) node[above] {\(t_{6}\)} to [out=00,in=180](3,1) node[below] {\(t_{7}\)};

      \draw[-] (3,1) node {} to [out=00,in=180](4,2) node {};
      \draw[white, line width=10] (3,2) node {} to [out=00,in=180](4,1) node {};
      \draw[<-] (3,2) node[above] {\(t_{3}\)} to [out=00,in=180](4,1) node[below] {\(t_{2}\)};

      \draw (2,0) to (4,0) ;
      \draw[looseness = 1.5] (4,0) to [out =0, in=0] (4,1);

      \draw (0,2) to (2,2) ;
      \draw[looseness = 1.5] (0,1) to [out =180, in=180] (0,2);

      \draw[->] (-1,0) to (0,0);

      \draw[->] (4,2) node[above] {\(0\)} to (5,2);
    \end{tikzpicture}$$ Assigning variables to the segments as shown the action is $$\begin{aligned}
    \actq{D, \mu}{t}
    &=
    \frac{1}{N}
    \crossingfunction{+}{\mu}{0, t_{5}, t_{1}, t_{6}}
    +
    \frac{1}{N}
    \crossingfunction{+}{\mu}{t_{4} + \tfrac{1}{N} - 1, t_{1}, t_{5}
    + \tfrac{1}{N} - 1, t_{2}}
    \\
    &\phantom{=}-
    \frac{1}{N}
    \crossingfunction{-}{\mu}{t_{3} + \tfrac{1}{N} - 1, t_{6}, t_{4}
    + \tfrac{1}{N} - 1, t_{7}}
    +
    \frac{1}{N}
    \crossingfunction{-}{\mu}{t_{7}, t_{2}, 0, t_{3}}
  
\end{aligned}$$ The parameter shifts come from using critical points to rotate the crossings as in [@McPhailSnyderVolume Figure 13].
:::

Let $\rho$ be a decorated representation of $K$. Choose an admissible, normalized shadow coloring $(\rho, u)$ of $D$ and a $\mu$, a logarithm of the meridian eigenvalue $m$ determined by the decoration. (Recall that a normalized shadow coloring is one where the segment parameter of the boundary segments is $1$.) Assume that the coloring is not pinched: if it is then $\qinv{}$ is still well-defined but we need to use a different expression for the $R$-matrix coefficients.

Choose logarithms $\beta_{i}$ of the segment parameters $b_{i}$ with $e^{\tu \beta_{i}} = b_{i}$. It is helpful to think of this choice as a vector $\beta \in
\mathbb{C}^{E}$, where $E$ is the set of internal segments. We call $\beta$ a . Since we are using a normalized coloring we can choose $0$ as the log-parameter of the boundary segments. Re-writing [@McPhailSnyderVolume Lemma 6.3] in our normalizations gives

::: theorem
[]{#thm:state sum label="thm:state sum"} The invariant $\qinv{}$ defined in [@McPhailSnyderVolume] is given by the sum $$\label{eq:state sum}
    \qinv{K, \rho, \mu}
    =
    \frac{1}{N^{|E|/2 + 1/2}}
    \sum_{n \in \nset{N}^{E}}
    e^{ N\actq{D}{(\beta + n)/N} }$$ where $\nset{N} \mathrel{:=}\left\{ \def\given{\ \middle| \ }  0, 1, \dots, N-1 \right\}$. $\qinv{K, \rho, \mu}$ is gauge-invariant, and in particular is independent of the choice of shadow coloring and log-coloring.
:::

::: lemma
[]{#thm:action lemmas label="thm:action lemmas"} Let $\beta$ be a log-coloring of a normalized, non-pinched shadow coloring.

::: thmenum
[]{#thm:action lemma:lattice periodic label="thm:action lemma:lattice periodic"} $t \mapsto \exp N\actq{D, \mu}{t}$ is a $\mathbb{Z}^{E}$-periodic function on the lattice $\frac{\beta}{N} + \frac{1}{N}\mathbb{Z}^{E}
      .$

[]{#thm:action lemma:no poles label="thm:action lemma:no poles"} If the shadow coloring avoids the unit circle, then none of the poles of the function $\mathbb{C}^{E} \to \mathbb{C}$ defined by $$t \mapsto \exp N\actq{D, \mu}{\beta/N+ t}$$ occur for $t \in \mathbb{R}^{E}$.
:::
:::

::: proof
*Proof.* [\[thm:action lemma:lattice periodic\]](#thm:action lemma:lattice periodic){reference-type="ref" reference="thm:action lemma:lattice periodic"} gives the quasi-periodicity relation $$e^{\pfl{\zeta/N+ 1}}
    =
    \frac{
      e^{\pfl{\zeta/N}}
    }{
      (1 - e^{\tu (\zeta + 1)/N})
      \cdots
      (1 - e^{\tu (\zeta + N)/N})
    }
    =
    \frac{
      e^{\pfl{\zeta/N}}
    }{
      1 - e^{\tu \zeta}
    }$$ so $$\begin{aligned}
    \exp
    \crossingfunction{+}{\mu}{
      \frac{\beta_{1}}{N} + 1,
      \frac{\beta_{2}}{N},
      \frac{\beta_{1'}}{N},
      \frac{\beta_{2'}}{N}
    }
    &=
    \exp
    \crossingfunction{+}{\mu}{
      \frac{\beta_{1}}{N},
      \frac{\beta_{2}}{N},
      \frac{\beta_{1'}}{N},
      \frac{\beta_{2'}}{N}
    }
    \frac{
      (1- b_{2'}/b_{1})
    }{
      m(1- b_{2}/m b_{1})
    }
    \\
    &=
    a_{1}
    \exp
    \crossingfunction{+}{\mu}{
      \frac{\beta_{1}}{N},
      \frac{\beta_{2}}{N},
      \frac{\beta_{1'}}{N},
      \frac{\beta_{2'}}{N}
    }
  
\end{aligned}$$ where $a_{1}$ is the parameter assigned to the segment by [\[eq:segment a vars\]](#eq:segment a vars){reference-type="ref" reference="eq:segment a vars"}. Similarly $$\exp
    \crossingfunction{+}{\mu}{
      \frac{\beta_{1}}{N},
      \frac{\beta_{2}}{N},
      \frac{\beta_{1'}}{N} + 1,
      \frac{\beta_{2'}}{N}
    }
    =
    a_{1'}^{-1}
    \exp
    \crossingfunction{+}{\mu}{
      \frac{\beta_{1}}{N},
      \frac{\beta_{2}}{N},
      \frac{\beta_{1'}}{N},
      \frac{\beta_{2'}}{N}
    }$$ and more generally the incoming segment variables have quasi-periodicity constant $a_{i}$ and the outgoing have $a_{i}^{-1}$. When the crossing functions $\crossingfunction{\epsilon}{\mu}{}$ are assembled together into $\actq{D,\mu}{}$ these factors cancel: the $a_{i}$ match because the $b_{i} = e^{\tu
  \beta_{i}}$ are a solution of the gluing equations.

[\[thm:action lemma:no poles\]](#thm:action lemma:no poles){reference-type="ref" reference="thm:action lemma:no poles"} Recall that the zeros and poles of $e^{\pfl{z}}$ all occur when $z \in \frac{1}{N} \mathbb{Z}$. The arguments of the quantum dilogarithms $\pfl{}$ in [\[eq:crossing positive,eq:crossing negative\]](#eq:crossing positive,eq:crossing negative){reference-type="ref" reference="eq:crossing positive,eq:crossing negative"} are of the form $\zeta/N+ t_{i} -
  t_{j}$ with $e^{\tu \zeta}$ the shape parameter of the relevant tetrahedron. Because $(\rho, u)$ avoids the unit circle $\operatorname{Im}\zeta \ne 0$ for each tetrahedron so we do not encounter any singularities when $t \in \mathbb{R}^{E}$. ◻
:::
