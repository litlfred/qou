---
doc_id: arxiv-2601.05136v2
doc_title: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant"
section_id: sec-013-classical-dilogarithms
section_title: "Classical dilogarithms"
section_number: null
pages: 12-13
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.82
doc_brief: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant — Previous work of the author and N."
---
[]{#sec:Classical dilogarithms label="sec:Classical dilogarithms"}

The computation of Chern-Simons invariants is closely related to a special function called the defined by $$\operatorname{Li}_{2}(z)
  \mathrel{:=}
  - \int_{0}^{z} \frac{\log(1 - t)}{t} \, d t$$ We refer to @Zagier2007 for more information on the dilogarithm. It has a branch point at $1$ and crossing the branch cut picks up a $\log(z)$ term, which itself has a branch point at $0$. Analytic continuation of $e^{\operatorname{Li}_{2}(z)}$ leads to the flattenings of @Neumann2004 [@Neumann2004]. To avoid dealing with these in full generality, write $X = (-\infty,
0] \cup [1, \infty)$ and consider [@Murakami2018 Chapter 4] the holomorphic function $\dll{} \colon \mathbb{C} \setminus X \to
\mathbb{C}$ defined by $$\dll{\zeta}
  \mathrel{:=}
  \begin{cases}
    \displaystyle
    \frac{
      \operatorname{Li}_{2}(e^{\tu \zeta})
    }{
      \tu
    }
    &
    \operatorname{Im}\zeta > 0
    \\
    \displaystyle
    -
    \frac{
      \operatorname{Li}_{2}(e^{-\tu \zeta})
    }{
      \tu
    }
    - \pi \ii \zeta(\zeta -1)
    - \frac{\pi \ii}{6}
    &
    \operatorname{Im}\zeta < 0
  \end{cases}$$

::: lemma
[]{#thm:dilog lemma label="thm:dilog lemma"} For fixed $\zeta \in \mathbb{C} \setminus X$, $$\exp \frac{ \mathrm{d} \dll{\zeta}}{\mathrm{d} \zeta}
    =
    \frac{
      1
    }{
      1 - e^{\tu \zeta}
    }$$ and $$e^{\pfl{\zeta}}
    =
    \exp\mathopen{}\left[
      \frac{
        \dll{\zeta + 1/2N}
      }{N}
      +
      \bigoh(N^{-1})
    \right]
    \qedhere$$
:::

::: proof
*Proof.* The first claim is an elementary computation. In the notation of @Murakami2018 we have $e^{\pfl{\zeta}} = \psi_{N}(\zeta + 1/2N)$ so the second claim follows from [@Murakami2018 eq. (4.3)]. ◻
:::
