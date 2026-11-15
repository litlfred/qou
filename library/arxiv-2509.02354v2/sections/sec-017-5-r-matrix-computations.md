---
doc_id: arxiv-2509.02354v2
doc_title: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms"
section_id: sec-017-5-r-matrix-computations
section_title: "R-matrix computations"
section_number: 5
pages: 23-23
source_pdf: 2509.02354v2.pdf
source_sha256: 14680221e597fe61
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.978
doc_brief: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms — We derive an explicit formula for the holonomy R-matrix of quantum sl2 at a root of unity."
---
[]{#sec:R-matrix-computations label="sec:R-matrix-computations"} This section contains computations with the $R$-matrices. We refer frequently to the identities concerning shifted $q$-factorials and quantum dilogarithms collected in [\[sec:quantum-dilogarithms\]](#sec:quantum-dilogarithms){reference-type="ref" reference="sec:quantum-dilogarithms"}.

::: lemma
[]{#thm:R-mat-phi-form label="thm:R-mat-phi-form"} The $R$-matrix coefficients [\[eq:R-mat-positive\]](#eq:R-mat-positive){reference-type="eqref" reference="eq:R-mat-positive"} associated to a positive, log-colored crossing can be written as $$\label{eq:R-mat-positive-phi-form}
    \begin{aligned}
      \rmat{n_1}{n_2}{n_1'}{n_2'}
    &=
    \frac{
      \omega^{\Theta/2}
      (\omega^{-N\zeta_{\lW}^{0}} -1)
      }{
      N
    }
    \frac{
      \pf{\zeta_{\lN}^0 + n_2' - n_1}
      \pf{\zeta_{\lS}^0 + n_2 - n_1'}
      }{
      \pf{\zeta_{\lE}^0 + n_2' - n_1'}
      \pf{\zeta_{\lW}^0 + n_2 - n_1 - 1}
    }
    \\
    &\phantom{=}\times
    \omega^{\zeta_{\lW}^{0} + n_{2} - n_{1}}
    \omega^{
      n_1(\alpha_{1}  -\mu_1)
      +
      n_2(\alpha_{2} + \mu_2)
      -
      n_1'(\alpha_{1'} -\mu_1)
      -
      n_2'(\alpha_{2'} + \mu_2)
    }
  \end{aligned}$$ Similarly for a negative crossing the matrix coefficients [\[eq:R-mat-negative\]](#eq:R-mat-negative){reference-type="eqref" reference="eq:R-mat-negative"} are given by $$\label{eq:R-mat-negative-phi-form}
    \begin{aligned}
      \rmatm{n_1}{n_2}{n_1'}{n_2'}
    &=
    \frac{
      \omega^{-\Theta/2}
      (\omega^{-N\zeta_{\lW}^{0}} -1)
      }{
      N
    }
    \frac{
      \pf{-\zeta_{\lN}^0 + n_2' - n_1}
      \pf{-\zeta_{\lS}^0 + n_2 - n_1'}
      }{
      \pf{-\zeta_{\lE}^0 + n_2' - n_1'}
      \pf{-\zeta_{\lW}^0 + n_2 - n_1 - 1}
    }
    \\
    &\phantom{=}\times
    \omega^{\zeta_{\lW}^{0} + n_{1} - n_{2}}
    \omega^{
      n_1(\alpha_{1}  + \mu_1)
      +
      n_2(\alpha_{2} - \mu_2)
      -
      n_1'(\alpha_{1'} + \mu_1)
      -
      n_2'(\alpha_{2'} - \mu_2)
    }
    \\
    &\phantom{=}\times
    \omega^{
      -
      (\zeta_{\lW}^{0} - \zeta_{\lS}^{0} + n_{1} - n_{1}')
      (\zeta_{\lW}^{0} - \zeta_{\lN}^{0} + n_{2} - n_{2}')
    }
    \end{aligned}$$ where in both cases $$\Theta
    \mathrel{:=}
    \zeta_{\lW}^{0} \zeta_{\lW}^{1}
    +
    \zeta_{\lE}^{0} \zeta_{\lE}^{1}
    -
    \zeta_{\lN}^{0} \zeta_{\lN}^{1}
    -
    \zeta_{\lS}^{0} \zeta_{\lS}^{1}
    .
    \qedhere$$
:::

::: proof
*Proof.* The positive case [\[eq:R-mat-positive-phi-form\]](#eq:R-mat-positive-phi-form){reference-type="eqref" reference="eq:R-mat-positive-phi-form"} follows form the definition [\[eq:qlf-def\]](#eq:qlf-def){reference-type="eqref" reference="eq:qlf-def"} of $\qlf{\zeta^{0}, \zeta^{1}}{n}$ and some elementary algebra. For the negative case [\[eq:R-mat-negative-phi-form\]](#eq:R-mat-negative-phi-form){reference-type="eqref" reference="eq:R-mat-negative-phi-form"} we must also use the relation $\zeta_{\lN}^{0} + \zeta_{\lS}^{0} = \zeta_{\lW}^{0} + \zeta_{\lE}^{0}$ and the inversion relation [@Faddeev2001 equation (16)], which in our conventions is $$\label{eq:pf inversion relation}
    \pf{\zeta} \pf{- \zeta - 1} 
    =
    (1 - \omega^{- N\zeta})
    \exp\left(
      \frac{
        \pi i (N+ 1/N)
        }{
        12
      }
      - \frac{\pi i}{N} \left[ \zeta - \frac{N-1}{2} \right]^{2}
    \right)
    .$$ ◻
:::
