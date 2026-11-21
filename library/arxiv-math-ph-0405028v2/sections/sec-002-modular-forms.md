---
doc_id: arxiv-math-ph-0405028v2
doc_title: "ON THE QUANTUM INVARIANT FOR THE BRIESKORN HOMOLOGY SPHERES"
section_id: sec-002-modular-forms
section_title: "Modular Forms"
section_number: null
pages: 7-8
source_pdf: 0405028v2.pdf
source_sha256: 90a0e4ba456988d6
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.98
doc_brief: "ON THE QUANTUM INVARIANT FOR THE BRIESKORN HOMOLOGY SPHERES — We study an exact asymptotic behavior of the Witten–Reshetikhin–Turaev SU(2) in- variant for the Brieskorn homology spheres Σ(p1, p2, p3)"
---
[]{#sec:modular label="sec:modular"}

We define the odd periodic function $\chi_{2 P}^{(\ell_1, \ell_2 ,  \ell_3)}(n)$ with modulus $2 \, P$ by $$\label{define_chi}
  \chi_{2 P}^{(\ell_1, \ell_2 ,  \ell_3)}(n)
  =
  \begin{cases}
    1 &
    \text{for
      $\displaystyle
      n=
      P \,
      \Bigl(
        1 + \sum_{j=1}^3 \varepsilon_j \, \frac{\ell_j}{p_j}
      \Bigr)
      \mod 2 \, P
      $
      where
      $\varepsilon_1 \varepsilon_2 \varepsilon_3=-1$
    }
    \\[2mm]
    -1 &
    \text{for
      $\displaystyle
      n=
      P \, 
      \Bigl(
        1 + \sum_{j=1}^3 \varepsilon_j \, \frac{\ell_j}{p_j}
      \Bigr)
      \mod 2 \, P
      $
      where
      $\varepsilon_1 \varepsilon_2 \varepsilon_3= 1$
    }
    \\[2mm]
    0 &
    \text{others}
  \end{cases}$$ Here $P=p_1 \, p_2 \, p_3$ with pairwise coprime positive integers $p_j$, and we mean $\varepsilon_j = \pm 1$. Integers $\ell_j$ are $$\label{define_ell}
  1 \leq \ell_j \leq p_j - 1$$ There exists a symmetry of the periodic function $$\begin{aligned}
  \chi_{2 P}^{(\ell_1, \ell_2, \ell_3)}(n)
  & =
  \chi_{2 P}^{(p_1-\ell_1, p_2 - \ell_2, \ell_3)}(n)
  \nonumber
  \\
  & =
  \chi_{2 P}^{(p_1-\ell_1, \ell_2, p_3 - \ell_3)}(n)
  =
  \chi_{2 P}^{(\ell_1, p_2 - \ell_2, p_3 - \ell_3)}(n)
  \label{symmetry_chi}
\end{aligned}$$

With this periodic function, we define the function $\Phi_{\boldsymbol{p}}^{(\ell_1, \ell_2, \ell_3)}(\tau)$ for $\tau$ in the upper half plane, $\tau \in \mathbb{H}$, by $$\label{modular_Phi}
  \Phi_{\boldsymbol{p}}^{(\ell_1, \ell_2, \ell_3)}(\tau)
  =
  \frac{1}{2}
  \sum_{n \in \mathbb{Z}}
  n \,
  \chi_{2 P}^{(\ell_1, \ell_2, \ell_3)}(n)
  \,
  q^{\frac{n^2}{4 P}}$$ where as usual $$q=\exp(2 \, \pi \, \mathrm{i} \, \tau)$$ Eq. [\[symmetry_chi\]](#symmetry_chi){reference-type="eqref" reference="symmetry_chi"} makes the number of the independent functions $\Phi_{\boldsymbol{p}}^{(\ell_1, \ell_2, \ell_3)}(\tau)$ to be $$D
  =
  D(p_1, p_2, p_3)
  =\frac{1}{4} \,
  (p_1 - 1) \,   (p_2 - 1) \,   (p_3- 1)$$

::: prop
The function $\Phi_{\boldsymbol{p}}^{(\ell_1, \ell_2, \ell_3)}(\tau)$ is a modular form with weight $3/2$. Namely under the ${S}$- and ${T}$-transformations [\[PSL_ST\]](#PSL_ST){reference-type="eqref" reference="PSL_ST"} we have $$\begin{aligned}
    \label{S_transformation}
    \Phi_{\boldsymbol{p}}^{(\ell_1, \ell_2, \ell_3)}(\tau)
    & =
    \left(
      \frac{\mathrm{i}}{\tau}
    \right)^{3/2} \,
    \sum_{\ell_1^\prime, \ell_2^\prime, \ell_3^\prime}
    \mathbf{S}_{\ell_1, \ell_2, \ell_3}^{\ell_1^\prime, \ell_2^\prime,
      \ell_3^\prime} \,
    \Phi_{\boldsymbol{p}}^{(\ell_1^\prime, \ell_2^\prime,
      \ell_3^\prime)}(-1/\tau)
    \\[2mm]

    \Phi_{\boldsymbol{p}}^{(\ell_1, \ell_2, \ell_3)}(\tau+1)
    & =
    \mathbf{T}^{\ell_1, \ell_2, \ell_3}
    \Phi_{\boldsymbol{p}}^{(\ell_1, \ell_2, \ell_3)}(\tau)
  
\end{aligned}$$ where the sum runs over $D(p_1,p_2,p_3)$ distinct triples. A $D\times D$ matrix $\mathbf{S}$ and diagonal matrix $\mathbf{T}$ are respectively given by $$\begin{aligned}
    \mathbf{S}_{\ell_1, \ell_2, \ell_3}^{\ell_1^\prime, \ell_2^\prime,
      \ell_3^\prime} 
    & =
    \sqrt{\frac{32}{P}} \,
    (-1)^{1+ P  + P  \sum_{j=1}^3 \frac{\ell_j + \ell_j^\prime}{p_j}
      + (\boldsymbol{\ell} \times \boldsymbol{\ell^\prime}) \cdot
      \boldsymbol{p}
    } \,
    \prod_{j=1}^3
    \sin \left(
      P \, \frac{\ell_j \, \ell_j^\prime}{p_j^{~2}}  \, \pi
    \right)
    \\[2mm]

    \mathbf{T}^{\ell_1, \ell_2, \ell_3}
    & =
    \exp \left(
      \frac{\pi \, \mathrm{i} }{2} \, P \,
      \Bigl(
      1+ \sum_{j=1}^3 \frac{\ell_j}{p_j}
      \Bigr)^2
    \right)
  
\end{aligned}$$
:::

We omit a proof as it is tedious but straightforward. We only need the Poisson summation formula $$\sum_{n \in \mathbb{Z}} f(n)
  =
  \sum_{n \in \mathbb{Z}}
  \int_{-\infty}^\infty
  \mathrm{e}^{-2 \pi \mathrm{i} t n} \,
  f(t) \,
  \mathrm{d} t$$
