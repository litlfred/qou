---
doc_id: arxiv-2509.02354v2
doc_title: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms"
section_id: sec-014-42-the-normalized-r-matrix
section_title: "The normalized R-matrix"
section_number: 4.2
pages: 14-15
source_pdf: 2509.02354v2.pdf
source_sha256: 14680221e597fe61
toc_source: outline
text_source: latex
latex_prose_ratio: 0.873
latex_coverage_ratio: 0.94
doc_brief: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms — We derive an explicit formula for the holonomy R-matrix of quantum sl2 at a root of unity."
---
We need to define some more log-parameters associated to a log-colored crossing $C$. Set $\epsilon = 1$ if $C$ is positive and $\epsilon = -1$ if it is negative. If $C$ is not pinched, $$K= 
  \frac{e^{2\pi i \gamma_{\lN}}}{1 - \left(b_{2'}/b_{1}\right)^{\epsilon}}$$ is not $\infty$, so we can choose $\kappa \in \mathbb{C}$ with $$e^{2\pi i \kappa} = K.$$ We will show in [\[thm:R-matrix transformation\]](#thm:R-matrix transformation){reference-type="ref" reference="thm:R-matrix transformation"} that the $R$-matrix is independent of the choice of $\kappa$, so we do not consider it to be part of a log-coloring. Extending our earlier abbreviations, define $$\begin{aligned}
    \label{eq:flattening-N}
    \zeta_{\lN}^0
    &=
    \epsilon (\beta_{2'} - \beta_1)
    &
    \zeta_{\lN}^1
    &=
    ( \kappa - \gamma_N)
    \\
    \label{eq:flattening-W}
    \zeta_{\lW}^0
    &=
    \epsilon(\beta_{2} - \beta_{1} - \mu_1 )
    &
    \zeta_{\lW}^1
    &=
    ( \kappa - \gamma_{\lW} + \epsilon \mu_1)
    \\
    \label{eq:flattening-S}
    \zeta_{\lS}^0
    &=
    \epsilon(\beta_{2} - \beta_{1'} + \mu_2 - \mu_1 )
    &
    \zeta_{\lS}^1
    &=
    (\kappa - \gamma_{\lS} + \epsilon (\mu_1 - \mu_2))
    \\
    \label{eq:flattening-E}
    \zeta_{\lE}^0
    &=
    \epsilon(\beta_{2'} - \beta_{1'} + \mu_2 )
    &
    \zeta_{\lE}^1
    &=
    ( \kappa - \gamma_{\lE} - \epsilon \mu_2)
  
\end{aligned}$$ For $j \in \left\{ \def\given{\ \middle| \ }  {\lN}, {\lW}, {\lS}, {\lE} \right\}$ we have $$e^{2\pi i \zeta_j^1} = 
  \frac{
    1
    }{
    1 - e^{2\pi i \zeta_j^0}
  }$$ so for $n \in \mathbb{Z}$ we can consider the $\qlf{\zeta^0, \zeta^1}{n}$ discussed in [\[sec:qlog-definitions\]](#sec:qlog-definitions){reference-type="ref" reference="sec:qlog-definitions"}. For $n \ge 0$, $$\label{eq:qlf recurrence}
  \qlf{\zeta^0, \zeta^1}{n}
  =
  \qlf{\zeta^0, \zeta^1}{0}
  \frac{
    \omega^{-n\zeta^1}
  }{
    (1 - \omega^{\zeta^0 + 1})
    \cdots
    (1 - \omega^{\zeta^0 + n})
  }$$ is an $n$-independent scalar times a power of $\omega^{\zeta^1}$ times a shifted $q$-factorial at $q = \omega$. The relation $e^{2\pi i \zeta^1} = 1/(1 - e^{2\pi i \zeta^0})$ ensures $\qlfname$ is periodic modulo $N$ in the integer argument.

::: definition
[]{#def:R-mat label="def:R-mat"} The associated to a positive, log-colored crossing is $$\label{eq:R-mat-positive}
    \begin{aligned}
      \widehat R_{n_1 n_2}^{n_1' n_2'}
      =
      {}
      &\frac{
        \omega^{-(N-1)(\zeta_{\lW}^0 + \zeta_{\lW}^1)}
      }{
        N
      }
      \\
      &\times
      \omega^{n_2 - n_1}
      \frac{
        \qlf{\zeta_{\lN}^0, \zeta_{\lN}^1}{n_2' - n_1}
        \qlf{\zeta_{\lS}^0, \zeta_{\lS}^1}{n_2 - n_1'}
        }{
          \qlf{\zeta_{\lW}^0, \zeta_{\lW}^1}{n_2 - n_1 - 1}
          \qlf{\zeta_{\lE}^0, \zeta_{\lE}^1}{n_2' - n_1'}
      }.
    \end{aligned}$$ and to a negative crossing is $$\label{eq:R-mat-negative}
    \begin{aligned}
      \rmatm{n_1}{n_2}{n_1'}{n_2'}
      &=
      \frac{
        \omega^{(N-1)(\zeta_{\lE}^0 + \zeta_{\lE}^1 - \zeta_{\lS}^0 -  \zeta_{\lS}^1 -  \zeta_{\lN}^0 - \zeta_{\lN}^1)}
        }{
        N
      }
      \\
      &\phantom{=}\times
      \omega^{n_1 - n_2}
      \frac{
        \qlf{\zeta_{\lW}^0, \zeta_{\lW}^1}{n_1 - n_2}
        \qlf{\zeta_{\lE}^0, \zeta_{\lE}^1}{n_1' - n_2' - 1}
      }{
        \qlf{\zeta_{\lN}^0, \zeta_{\lN}^1}{n_1 - n_2' - 1}
        \qlf{\zeta_{\lS}^0, \zeta_{\lS}^1}{n_1' - n_2 - 1}
      }
    \end{aligned}$$

We call the $\mathcal{U}_\xi$-module morphism $$\label{eq:braiding}
    \tau R : 
    \rep{\hat{\chi}_{1}}
    \otimes
    \rep{\hat{\chi}_{2}}
    \to
    \rep{\hat{\chi}_{2'}}
    \otimes
    \rep{\hat{\chi}_{1'}},
    \vbh{n_{1} n_{2}}
    \mapsto
    \sum_{n_{1}' n_{2}'}
    \rmat{n_{1}}{n_{2}}{n_{1}'}{n_{2}'}
    \vbh{n_{2}' n_{1}'}$$ the associated to a positive log-colored crossing. For a negative crossing the braiding is $\overline{R} \tau$.
:::

The relation [\[eq:qlf recurrence\]](#eq:qlf recurrence){reference-type="eqref" reference="eq:qlf recurrence"} (and some algebra) immediately show that the positive $R$-matrix satisfies the relations of [\[eq:intertwiner-rel\]](#eq:intertwiner-rel){reference-type="ref" reference="eq:intertwiner-rel"}. One can check directly that the negative $R$-matrix is its inverse for appropriate parameter values [@McPhailSnyderVolume]. Our assumption that the crossing is not pinched ensures we avoid the poles and zeros of $\qlfname$, which occur at $\zeta^0 \in \mathbb{Z}$. In [\[sec:pinched-limit\]](#sec:pinched-limit){reference-type="ref" reference="sec:pinched-limit"} we show that despite these poles the $R$-matrix is regular in the pinched limit.
