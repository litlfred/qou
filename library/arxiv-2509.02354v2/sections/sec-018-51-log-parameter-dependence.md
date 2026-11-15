---
doc_id: arxiv-2509.02354v2
doc_title: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms"
section_id: sec-018-51-log-parameter-dependence
section_title: "Log-parameter dependence"
section_number: 5.1
pages: 23-25
source_pdf: 2509.02354v2.pdf
source_sha256: 14680221e597fe61
toc_source: outline
text_source: latex
latex_prose_ratio: 0.839
latex_coverage_ratio: 0.841
doc_brief: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms — We derive an explicit formula for the holonomy R-matrix of quantum sl2 at a root of unity."
---
[]{#sec:log-paramater-dependence label="sec:log-paramater-dependence"}

Here we compute the dependence of the $R$-matrix on the choice of log-coloring as used in the proof of [\[thm:RIII\]](#thm:RIII){reference-type="ref" reference="thm:RIII"}.

::: lemma
[]{#thm:R-matrix transformation label="thm:R-matrix transformation"}

::: thmenum
[]{#thm:R-matrix transformation:kappa label="thm:R-matrix transformation:kappa"} The $R$-matrix coefficients of [\[def:R-mat\]](#def:R-mat){reference-type="ref" reference="def:R-mat"} are independent of the choice of $\kappa$.

[]{#thm:R-matrix transformation:gamma label="thm:R-matrix transformation:gamma"} Let $\mathfrak{f}$ and $\tilde{\mathfrak{f}}$ be log-colorings of a crossing for which the $\mu_i$ and $\beta_i$ are the same and the $\gamma_i$ differ by integers: $$\begin{aligned}
      \tilde \mu_j &= \mu_j
                   &
      \tilde \beta_j &= \beta_j
                     &
      \tilde \gamma_j &= \gamma_j + k_j
    
\end{aligned}$$ Then the coefficients of the $R$-matrix are related by $$\label{eq:R-matrix transformation:gamma}
      \rmat[\tilde{\mathfrak{f}}]{n_{1}}{n_{2}}{n_{1}'}{n_{2}'}
      =
      \omega^{
        \frac{1}{2}
        \Gamma(\tilde{\mathfrak{f}}, \mathfrak{f}) 
      }
      \omega^{
        k_{\lN}(n_{2}' - n_{1})
            +
            k_{\lS}(n_{2} - n_{1}')
            -
            k_{\lW}(n_{2} - n_{1})
            -
            k_{\lE}(n_{2}' - n_{1}')
          }
          \rmat[\mathfrak{f}]{n_{1}}{n_{2}}{n_{1}'}{n_{2}'}$$ where $$\Gamma(\tilde{\mathfrak{f}}, \mathfrak{f})
          =
          k_{\lN}\zeta_{\lN}^{0}
          +
          k_{\lS}\zeta_{\lS}^{0}
          -
          k_{\lW}\zeta_{\lW}^{0}
          -
          k_{\lE}\zeta_{\lE}^{0}$$

[]{#thm:R-matrix transformation:beta label="thm:R-matrix transformation:beta"} Let $\mathfrak{f}$ and $\tilde{\mathfrak{f}}$ be log-colorings of a crossing for which the $\mu_i$ and $\gamma_i$ are the same and the $\beta_i$ differ by integers: $$\begin{aligned}
        \tilde \mu_j &= \mu_j
                     &
        \tilde \beta_j &= \beta_j + l_j
                       &
        \tilde \gamma_j &= \gamma_j
      
\end{aligned}$$ Then the $R$-matrix coefficients are related by $$\label{eq:R-matrix transformation:beta}
          \rmat[\tilde{\mathfrak{f}}]{n_{1}}{n_{2}}{n_{1}'}{n_{2}'}
          =
          \omega^{
            \frac{1}{2} \mathrm{B}(\tilde{\mathfrak{f}}, \mathfrak{f})
          }
          \rmat[\mathfrak{f}]{n_{1} + l_{1},}{n_{2} + l_{2}}{n_{1}' + l_{1}', }{n_{2}' + l_{2}'}$$ where $$\begin{aligned}
          \mathrm{B}(\tilde{\mathfrak{f}}, \mathfrak{f})
          &=
          l_{2'}(\gamma_{\lE} - \gamma_{\lW} - \epsilon_{2'} \mu_{2})
          +
          l_{1'}(\gamma_{\lS} - \gamma_{\lE} - \epsilon_{1'} \mu_{2})
          \\
          &\phantom{=}
          +
          l_{2}(\gamma_{\lE} - \gamma_{\lW} - \epsilon_{2} \mu_{2})
          +
          l_{1}(\gamma_{\lS} - \gamma_{\lE} - \epsilon_{1} \mu_{2})
        \end{aligned}$$ and the $\epsilon_i$ are the signs of [1](#fig:crossing-log-dec-signs){reference-type="ref" reference="fig:crossing-log-dec-signs"}.
:::
:::

<figure id="fig:crossing-log-dec-signs">

<figcaption>Signs for the dependence of the <span class="math inline"><em>R</em></span>-matrix on the segment log-parameters <span class="math inline"><em>β</em><sub><em>i</em></sub></span>.</figcaption>
</figure>

::: proof
*Proof.* [\[thm:R-matrix transformation:kappa\]](#thm:R-matrix transformation:kappa){reference-type="ref" reference="thm:R-matrix transformation:kappa"} This is immediate from [\[eq:qlf-shift-1\]](#eq:qlf-shift-1){reference-type="ref" reference="eq:qlf-shift-1"}. Consider a positive crossing (the negative case is similar). If we choose $\kappa + p$ instead of $\kappa$ for $p \in \mathbb{Z}$, by [\[eq:qlf-shift-1\]](#eq:qlf-shift-1){reference-type="eqref" reference="eq:qlf-shift-1"} the new matrix coefficients are $$\begin{aligned}
      &
      \frac{
        \omega^{-(N-1)(\zeta_{\lW}^0 + \zeta_{\lW}^1 + p)}
      }{
        N
      }
      \omega^{n_2 - n_1}
      \frac{
        \qlf{\zeta_{\lN}^0, \zeta_{\lN}^1 + p}{n_2' - n_1}
        \qlf{\zeta_{\lS}^0, \zeta_{\lS}^1 + p}{n_2 - n_1'}
        }{
          \qlf{\zeta_{\lW}^0, \zeta_{\lW}^1 + p}{n_2 - n_1 - 1}
          \qlf{\zeta_{\lE}^0, \zeta_{\lE}^1 + p}{n_2' - n_1'}
      }
      \\
      &=
      \omega^{p - p(\zeta_{\lN}^0 + \zeta_{\lS}^0 - \zeta_{\lW}^0 - \zeta_{\lE}^0) - p(n_2' - n_1 + n_2 - n_1' - (n_2 - n_1 - 1) -(n_2' - n_1'))}
      \rmat{n_1}{n_2}{n_1'}{n_2'}
      \\
      &=
      \rmat{n_1}{n_2}{n_1'}{n_2'}
  
\end{aligned}$$ so we get the same coefficients as for our original choice of $\kappa$.

[\[thm:R-matrix transformation:gamma\]](#thm:R-matrix transformation:gamma){reference-type="ref" reference="thm:R-matrix transformation:gamma"} Suppose the crossing is positive. We can use [\[eq:qlf-shift-1\]](#eq:qlf-shift-1){reference-type="ref" reference="eq:qlf-shift-1"} to find $$\begin{aligned}
    \rmat[\tilde{\mathfrak{f}}]{n_1}{n_2}{n_1'}{n_2'}
    &=
    \frac{
      \omega^{-(N-1)(\zeta_{\lW}^0 + \zeta_{\lW}^1 - k_{\lW})}
    }{
      N
    }
    \omega^{n_2 - n_1}
    \frac{
      \qlf{\zeta_{\lN}^0, \zeta_{\lN}^1 - k_{\lN}}{n_2' - n_1}
      \qlf{\zeta_{\lS}^0, \zeta_{\lS}^1 - k_{\lS}}{n_2 - n_1'}
    }{
      \qlf{\zeta_{\lW}^0, \zeta_{\lW}^1 - k_{\lW}}{n_2 - n_1 - 1}
      \qlf{\zeta_{\lE}^0, \zeta_{\lE}^1 - k_{\lE}}{n_2' - n_1'}
    }
    \\
    &=
    \omega^{- k_{\lW}}
    \omega^{
      \frac{1}{2}
      (
      k_{\lN}\zeta_{\lN}^{0}
      +
      k_{\lS}\zeta_{\lS}^{0}
      -
      k_{\lW}\zeta_{\lW}^{0}
      -
      k_{\lE}\zeta_{\lE}^{0}
      )
    }
    \omega^{
      k_{\lN}(n_{2}' - n_{1})
      +
      k_{\lS}(n_{2} - n_{1}')
      -
      k_{\lW}(n_{2} - n_{1} - 1)
      -
      k_{\lE}(n_{2}' - n_{1}')
    }
    \rmat[\mathfrak{f}]{n_1}{n_2}{n_1'}{n_2'}
  
\end{aligned}$$ as claimed, and a similar computation works for negative crossings.

[\[thm:R-matrix transformation:beta\]](#thm:R-matrix transformation:beta){reference-type="ref" reference="thm:R-matrix transformation:beta"} Again suppose the crossing is positive. shows that $$\qlf{\zeta_{\lN}^0 + l_{2}' - l_{1}, \zeta_{\lN}^1}{n_2' - n_1 - l_{2}' + l_{1}}
    =
    \omega^{
      \frac{1}{2}
      (l_{2}' - l_{1}) \zeta_{\lN}^{1}
    }
    \qlf{\zeta_{\lN}^0, \zeta_{\lN}^1}{n_2' - n_1}$$ and repeating for the other factors shows that $$\begin{aligned}
    \rmat[\tilde{\mathfrak{f}}]{n_1 - l_{1},}{n_2 - l_{2}}{n_1' - l_{1}', }{n_2' - l_{2}'}
    &=
    \omega^{
      \frac{1}{2}
      \left[
      l_{2}'( \zeta_{\lN}^{1} - \zeta_{\lE}^{1} )
      +
      l_{1}'( \zeta_{\lE}^{1} - \zeta_{\lS}^{1} )
      +
      l_{2}( \zeta_{\lS}^{1} - \zeta_{\lW}^{1} )
      +
      l_{1}( \zeta_{\lW}^{1} - \zeta_{\lN}^{1} )
    \right]
    }
    \rmat[\mathfrak{f}]{n_1}{n_2}{n_1'}{n_2'}
    .
  
\end{aligned}$$ (Here the power of $\omega$ from $\omega^{n_{2} - n_{1}}$ cancels with that from $\omega^{-(N-1)\zeta_{\lW}^{0}}$.) For a positive crossing [\[eq:flattening-N,eq:flattening-E\]](#eq:flattening-N,eq:flattening-E){reference-type="ref" reference="eq:flattening-N,eq:flattening-E"} give $$\zeta_{\lN}^{1} - \zeta_{\lE}^{1}
    =
    (\kappa - \gamma_{\lN}) - ( \kappa - \gamma_{\lE} - \mu_{2})
    =
    \gamma_{\lE} - \gamma_{\lN} + \mu_{2}$$ as claimed, and for a positive crossing [1](#fig:crossing-log-dec-signs){reference-type="ref" reference="fig:crossing-log-dec-signs"} says that $\epsilon_{2} = +1$. Similar computations give the coefficients of the other $l_i$ and the negative crossing case. ◻
:::
