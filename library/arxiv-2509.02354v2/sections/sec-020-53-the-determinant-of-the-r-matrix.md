---
doc_id: arxiv-2509.02354v2
doc_title: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms"
section_id: sec-020-53-the-determinant-of-the-r-matrix
section_title: "The determinant of the R-matrix"
section_number: 5.3
pages: 28-29
source_pdf: 2509.02354v2.pdf
source_sha256: 14680221e597fe61
toc_source: outline
text_source: latex
latex_prose_ratio: 0.879
latex_coverage_ratio: 0.933
doc_brief: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms — We derive an explicit formula for the holonomy R-matrix of quantum sl2 at a root of unity."
---
Here we compute the determinant of the $R$-matrix, a key step in the proof of [\[thm:RIII\]](#thm:RIII){reference-type="ref" reference="thm:RIII"}.

::: lemma
[]{#thm:R-mat-det label="thm:R-mat-det"} Let $R$ be the $R$-matrix associated to a log-colored crossing $c$ of sign $\epsilon$. The determinant of the associated braiding $\tau R$ is $$\begin{aligned}
    \det \tau R
    =
    \exp\left(-\frac{N}{2\pi i} I(c)\right)
    \left(
      \frac{N}{\df{0}^2}
    \right)^{\epsilon N^2}
    \exp\mathopen{}\left(
      2\pi i\left( \frac{\gamma_{\lW} - \gamma_{\lE}}{2} - \epsilon(\mu_{1} + \mu_{2}) + \lambda_{1} + \lambda_{2} \right)
    \right)^{N(N-1)}
  
\end{aligned}$$ where $$\begin{aligned}
    \lambda_{1} = \frac{\epsilon}{2}(\beta_{1'} - \beta_{1})
    \\
    \lambda_{2} = \frac{\epsilon}{2}(\beta_{2} - \beta_{2'})
  
\end{aligned}$$ are the log-longitudes of each component of the crossing, $$I(c) =
      \mathcal{L}(\zeta^0_{\lN}, \zeta^1_{\lN})
      +
      \mathcal{L}(\zeta^0_{\lS}, \zeta^1_{\lS})
      -
      \mathcal{L}(\zeta^0_{\lW}, \zeta^1_{\lW})
      -
      \mathcal{L}(\zeta^0_{\lE}, \zeta^1_{\lE})$$ is a sum of dilogarithms, and $\df{0} = \exp\left( N^{-1} \sum_{k=0}^{N-1} k \log(1 - \omega^{k}) \right)$ is a constant.
:::

::: proof
*Proof.* Using the factorization [\[eq:R-factorization-positive\]](#eq:R-factorization-positive){reference-type="eqref" reference="eq:R-factorization-positive"} of [\[thm:R-factorization\]](#thm:R-factorization){reference-type="ref" reference="thm:R-factorization"} we see that $$\det \tau R =
    N^{-N^2}
    \det \mathcal{Z}_{\lE}
    \det \mathcal{Z}_{\lW}
    (\det \mathcal{Z}_{\lN})^N
    (\det \mathcal{Z}_{\lS})^N.$$ It is easy to compute the determinant of the diagonal matrices $\mathcal{Z}_{\lE}$ and $\mathcal{Z}_{\lW}$ using [\[thm:qlf-product\]](#thm:qlf-product){reference-type="ref" reference="thm:qlf-product"}: $$\begin{aligned}
    \det \mathcal{Z}_{\lE}
    &=
    \prod_{n_1, n_2}
    \frac{
      1
    }{
      \qlf{\zeta^0_{\lE} , \zeta^1_{\lE}}{n_1 - n_2}
    }
    \\
    &=
    \left[
      \prod_{n}
      \frac{
        1
      }{
        \qlf{\zeta^0_{\lE} , \zeta^1_{\lE}}{n_1 - n_2}
      }
    \right]^{N}
    \\
    &=
    \omega^{\frac{1}{2} N^2(N-1) \zeta_{\lE}^1}
    \exp
    \mathopen{}\left(
      N
      \frac{\mathcal{L}(\zeta^0_{\lE}, \zeta_{\lE}^1)}{2\pi i}
    \right)
  
\end{aligned}$$ and similarly $$\begin{aligned}
    \det \mathcal{Z}_{\lW}
    &=
    \omega^{-\frac{1}{2}N^2(N-1) (2 \zeta_{\lW}^0 + \zeta_{\lW}^1)}
    \exp
    \mathopen{}\left(
      N
      \frac{\mathcal{L}(\zeta^0_{\lW}, \zeta_{\lW}^1)}{2\pi i}
    \right)
  
\end{aligned}$$ Using [\[thm:hard-determinant\]](#thm:hard-determinant){reference-type="ref" reference="thm:hard-determinant"} to compute $\det \mathcal{Z}_{\lN}$ and $\det \mathcal{Z}_{\lS}$ we see that $$\begin{aligned}
    \det \tau R
    =
    {}
    &
      \exp \left(
        N
        \frac{
          \mathcal{L}(\zeta^0_{\lW}, \zeta^1_{\lW})
          +
          \mathcal{L}(\zeta^0_{\lE}, \zeta^1_{\lE})
          -
          \mathcal{L}(\zeta^0_{\lN}, \zeta^1_{\lN})
          -
          \mathcal{L}(\zeta^0_{\lS}, \zeta^1_{\lS})
        }{
          2\pi i
        }
      \right)
    \\
    &\times
    \left(
      \frac{N}{\df{0}^2}
    \right)^{N^2}
    \exp
    \mathopen{}\left(
    2 \pi i
    \frac{N(N-1)}{2}
    \left(
      \zeta_{\lE}^1 - \zeta_{\lW}^1
      + 2 \zeta_{\lW}^0
      - \zeta_{\lN}^0 - \zeta_{\lS}^0
    \right)
    \right)
  
\end{aligned}$$ The claim follows from checking that $$\zeta_{\lE}^1 - \zeta_{\lW}^1
    + 2 \zeta_{\lW}^0
    - \zeta_{\lN}^0 - \zeta_{\lS}^0
    =
    \gamma_{\lW} - \gamma_{\lE} - 2 \epsilon(\mu_{1} + \mu_{2}) + 2 \lambda_{1} + 2 \lambda_{2}.
    \qedhere$$ ◻
:::
