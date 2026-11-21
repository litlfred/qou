---
doc_id: arxiv-2509.02354v2
doc_title: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms"
section_id: sec-013-41-recursions-for-the-r-matrix-coefficients
section_title: "Recursions for the R-matrix coefficients"
section_number: 4.1
pages: 12-14
source_pdf: 2509.02354v2.pdf
source_sha256: 14680221e597fe61
toc_source: outline
text_source: latex
latex_prose_ratio: 0.921
latex_coverage_ratio: 0.897
doc_brief: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms — We derive an explicit formula for the holonomy R-matrix of quantum sl2 at a root of unity."
---
[]{#subsec:recurrences label="subsec:recurrences"}

::: marginfigure
:::

We can now explicitly compute the matrix coefficients of $R$ as a function of the geometric parameters $\hat \chi_{i}$. We begin by fixing some terminology and conventions.

::: definition
We say a crossing is if it its segments (labeled as in [\[fig:crossing-regions\]](#fig:crossing-regions){reference-type="ref" reference="fig:crossing-regions"}) are assigned characters $\hat \chi_i$ satisfying $$(\hat \chi_{2'}, \hat \chi_{1}') =
    \begin{cases}
      B(\hat \chi_{1}, \hat \chi_{2}) & \text{for a positive crossing}
      \\
      B^{-1}(\hat \chi_{1}, \hat \chi_{2}) & \text{for a negative crossing}
    \end{cases}$$
:::

::: definition
A of a $\chi$-colored crossing is a choice of complex numbers $\beta_{i}$ for the segments, $\gamma_{i}$ for the regions, and $\mu_{1}, \mu_{2}$ for the components so that $$\begin{gathered}
      \hat \chi_{i}(x^{N}) = \omega^{N\alpha_i}
      \\
      \hat \chi_{i}(y^{N}) = \omega^{N\beta_i}
      \\
      \hat \chi_{i}(z) = \omega^{ \mu_i}
    \end{gathered}$$ for each segment, where the segment parameters $\alpha_{i}$ are determined by the region parameters as $$\begin{aligned}
    \alpha_1 &= \gamma_{\lW}-\gamma_{\lN}
             &
    \alpha_{2'} &= \gamma_{\lE} - \gamma_{\lN}
    \\
    \alpha_2 &= \gamma_{\lS}- \gamma_{\lW}
             &
    \alpha_{1'} &= \gamma_{\lS} - \gamma_{\lE}
  
\end{aligned}$$ and the labels are as in [\[fig:crossing-regions\]](#fig:crossing-regions){reference-type="ref" reference="fig:crossing-regions"}.
:::

Because $a_1 a_2 = a_{1'} a_{2'}$ it is natural to require $\alpha_1 + \alpha_2 = \alpha_{1'} + \alpha_{2'}$, and this is equivalent to a choice of region parameters $\gamma_j$ as above. Just as we associate an $R$-matrix to a crossing we assign the parametrized $R$-matrices of [\[thm:R-matrix-exists\]](#thm:R-matrix-exists){reference-type="ref" reference="thm:R-matrix-exists"} to $\chi$-colored crossings. Later in [\[sec:braid groupoids\]](#sec:braid groupoids){reference-type="ref" reference="sec:braid groupoids"} we will show our $R$-matrices satisfy a version of the Yang-Baxter equation, subject to a geometric condition on the log-colorings.

The choice of log-coloring fixes identifications $\rep{\hat \chi_{i}} \cong\rep{\alpha_{i}, \beta_{i}, \mu_{i}}$ with the weight modules of [\[def:standard-rep\]](#def:standard-rep){reference-type="ref" reference="def:standard-rep"}. It turns out to be easier to work in the Fourier dual basis $\left\{ \def\given{\ \middle| \ }  \vbh{n} \right\}$ of $\rep{\alpha, \beta, \mu}$ defined by $$\label{eq:non-weight-basis}
  \pi_{\alpha, \beta, \mu}(x) \vbh n = \omega^{\alpha} \vbh{n-1},
  \quad
  \pi_{\alpha, \beta, \mu}(y) \vbh n = \omega^{\beta + n} \vbh n,
  \quad
  \pi_{\alpha, \beta, \mu}(z) \vbh n = \omega^{\mu} \vbh n.$$ It is related to the weight basis by $$\label{eq:basis-and-dual-basis}
  \vbh n \mathrel{:=}\sum^{N-1}_{k=0} \omega^{nk} \vb k
  \text{ and }
  \vb n = \frac{1}{N} \sum_{k=0}^{N-1} \omega^{-n k} \vbh k
  .$$ Our goal is to determine the matrix coefficients $\rmat{n_1}{ n_2}{n_1'}{n_2'}$ defined by $$\label{eq:R-matrix-coefficients}
  R \cdot \vbh{n_1 n_2} = \sum_{n_1' n_2'} \rmat{n_1}{ n_2}{n_1'}{n_2'} \vbh{n_1' n_2'}$$ where we abbreviate $\vbh{n_1 n_2} = \vbh{n_1} \otimes \vbh{n_2}$. Here and below all sums are over $\mathbb{Z}/N\mathbb{Z}$.

Assume the crossing is positive. Abbreviate the structure maps of the representations at the crossing as $$\pi = \pi_1 \otimes \pi_2, \ \ \pi' = \pi_{1'} \otimes \pi_{2'}.$$ Commutativity of the diagram in [\[eq:R-mat-module-diagram\]](#eq:R-mat-module-diagram){reference-type="eqref" reference="eq:R-mat-module-diagram"} requires matrix equations $$\begin{aligned}
  \label{eq:intertwiner-rel}
  R \pi(u) &=  \pi'\left(\mathcal{R}(u)\right) R, \ \ u \in \mathcal{W}_\xi, \\
  \intertext{and}
  \label{eq:intertwiner-rel-inv}
  \pi'(u) R &= R \pi\left(\mathcal{R}^{-1}(u)\right), \ \ u \in \mathcal{W}_\xi.
\end{aligned}$$

Setting $u = y_1^{-1}$ in [\[eq:intertwiner-rel\]](#eq:intertwiner-rel){reference-type="eqref" reference="eq:intertwiner-rel"} gives the relation $$\label{eq:yinv-rel}
  \begin{aligned}
    R \pi(y_1^{-1}) &= \pi'\left( y_2^{-1} + (y_1^{-1} - z_2^{-1} y_2^{-1})x_2^{-1}\right) R \\
                    &= \pi'\left( y_2^{-1} + x_2^{-1}(y_1^{-1} - \omega^{-1} z_2^{-1} y_2^{-1})\right) R
  \end{aligned}$$ In terms of the matrix coefficients [\[eq:R-matrix-coefficients\]](#eq:R-matrix-coefficients){reference-type="eqref" reference="eq:R-matrix-coefficients"} this becomes $$\begin{aligned}
  &  \sum_{n_1' n_2'} \rmat{n_1}{n_2}{n_1'}{n_2'}  \omega^{-\beta_1 - n_1}  \vbh{n_1' n_2'} \\
  &= \sum_{n_1' n_2'} \rmat{n_1}{ n_2}{n_1'}{ n_2'} \omega^{-\beta_{2'} - n_2'} \vbh{n_1' n_2'} \\
  &\phantom{=} + \sum_{n_1' n_2'} \rmat{n_1}{ n_2}{n_1'}{ n_2'}\left[ \omega^{-\beta_{1'} - n_1'}  - \omega^{-\mu_2} \omega^{-\beta_{2'} - n_2' - 1} \right] \omega^{-\alpha_{2'}} \vbh{n_1', n_2'+1}
\end{aligned}$$ which we can rewrite as the recursion $$\rmat{n_1}{n_2}{n_1'}{n_2'} \left[ \omega^{-\beta_1 - n_1}  - \omega^{-\beta_{2'} - n_2'} \right]
  =
  \rmat{n_1}{n_2}{n_1',}{n_2'-1} \omega^{-\alpha_{2'}} \left[ \omega^{-\beta_{1'} - n_1'} - \omega^{- \mu_2 - \beta_{2'} - n_2'} \right]
  .$$ In a slightly more convenient form, this is $$\begin{aligned}
  \rmat{n_1}{n_2}{n_1'}{n_2' }
  &=
  \rmat{n_1}{n_2}{n_1',}{n_2' -1}
  \omega^{-\alpha_{2'} - \mu_2}
  \frac
  {1 - \omega^{\mu_2 + \beta_{2'} - \beta_{1'} - 1} \omega^{n_2' - n_1'}}
  {1 - \omega^{\beta_{2'} - \beta_{1}} \omega^{n_2' - n_1}} 
  .
\end{aligned}$$ Abbreviate $$\begin{aligned}
  \zeta_{\lN}^0
  &=
  \beta_{2'} - \beta_1
  \\
  \zeta_{\lW}^0
  &=
  \beta_{2} - \beta_{1} - \mu_1 
  \\
  \zeta_{\lS}^0
  &=
  \beta_{2} - \beta_{1'} + \mu_2 - \mu_1 
  \\
  \zeta_{\lE}^0
  &=
  \beta_{2'} - \beta_{1'} + \mu_2 
\end{aligned}$$ If any $\zeta_i^0 \in \mathbb{Z}$ we say that the (coloring of the) crossing is ; this condition depends only on the characters $\chi_i$, not the logarithms, and has a geometric interpretation ([\[rem:pinched eigenlines\]](#rem:pinched eigenlines){reference-type="ref" reference="rem:pinched eigenlines"}). We can obtain the $R$-matrix at pinched crossings as a limit of the general case (see [\[sec:pinched-limit\]](#sec:pinched-limit){reference-type="ref" reference="sec:pinched-limit"}), so we exclude them for now.

::: theorem
[]{#thm:R-recurrences label="thm:R-recurrences"} At a positive crossing that is not pinched the matrix coefficients satisfy recurrence relations $$\begin{aligned}
    \label{eq:R-recurrence-i}
    \rmat{n_1}{n_2}{n_1'}{n_2' }
    &=
    \rmat{n_1}{n_2}{n_1',}{n_2' -1}
    {\omega^{-\alpha_{2'} - \mu_2} }
    \frac
    {1 - \omega^{\zeta_E^0 + n_2' - n_1'}}
    {1 - \omega^{\zeta_N^0 +  n_2' - n_1}} 
    \\
    \label{eq:R-recurrence-ii}
    \rmat{n_1}{n_2}{n_1',}{n_2'}
    &=
    \rmat{n_1}{n_2}{n_1'-1,}{n_2'}
    \omega^{-\alpha_{1'} + \mu_1}
    \frac
    {1 - \omega^{\zeta_S^0 - n_2 - n_1' + 1} }
    {1 - \omega^{\zeta_E^0 + n_2' - n_1' + 1 } }
    \\
    \label{eq:R-recurrence-iii}
    \rmat{n_1,}{n_2}{n_1'}{n_2'}
    &=
    \rmat{n_1,}{n_2 -1}{n_1'}{n_2'}
    \omega^{\alpha_2 + \mu_2 + 1}
    \frac
    {1 - \omega^{\zeta_W^0 - 1 + n_2 - n_1} }
    {1 -  \omega^{\zeta_S^0 + n_2 - n_1'}}
    \\ 
    \label{eq:R-recurrence-iv}
    \rmat{n_1}{n_2}{n_1'}{n_2'}
    &=
    \rmat{n_1 - 1,}{n_2}{n_1'}{n_2'}
    \omega^{\alpha_{1} - \mu_1 - 1}
    \frac
    {1 - \omega^{\zeta_N^0 + n_2' - n_1 +1 }}
    {1 -  \omega^{\zeta_W^0 - 1 + n_2 - n_1 +1} } 
  
\end{aligned}$$ which determine $R$ uniquely up to an overall scalar.
:::

::: proof
*Proof.* We found the first recurrence above. The other three relations can be derived in a similar way by applying [\[eq:intertwiner-rel\]](#eq:intertwiner-rel){reference-type="ref" reference="eq:intertwiner-rel"} to $y_2$ and [\[eq:intertwiner-rel-inv\]](#eq:intertwiner-rel-inv){reference-type="ref" reference="eq:intertwiner-rel-inv"} to $y_1^{-1}$ and $y_2$. The relations are clearly sufficient to determine $R$ up to a scalar, and then existence and uniqueness follow from Theorem [\[thm:R-matrix-exists\]](#thm:R-matrix-exists){reference-type="ref" reference="thm:R-matrix-exists"}. ◻
:::
