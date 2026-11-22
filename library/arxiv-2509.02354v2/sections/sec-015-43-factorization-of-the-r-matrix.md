---
doc_id: arxiv-2509.02354v2
doc_title: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms"
section_id: sec-015-43-factorization-of-the-r-matrix
section_title: "Factorization of the R-matrix"
section_number: 4.3
pages: 15-17
source_pdf: 2509.02354v2.pdf
source_sha256: 14680221e597fe61
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.966
doc_brief: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms — We derive an explicit formula for the holonomy R-matrix of quantum sl2 at a root of unity."
---
[]{#sec:factorization label="sec:factorization"}

A remarkable property of the $R$-matrices in [\[def:R-mat\]](#def:R-mat){reference-type="ref" reference="def:R-mat"} is that they factor into four operators, each defined in terms of a quantum dilogarithm.

<figure id="fig:build-ideal-octahedron">

<figcaption>Building an ideal octahedron.</figcaption>
</figure>

::: theorem
[]{#thm:R-factorization label="thm:R-factorization"} At a positive, non-pinched, log-colored crossing the brading matrix factors as $$\label{eq:R-factorization-positive}
    \frac{
      1
    }{
      N
    }
    \mathcal{Z}_{\lE} (\mathcal{Z}_{\lN} \otimes \mathcal{Z}_{\lS}) \mathcal{Z}_{\lW}$$ where $$\begin{aligned}
    \mathcal{Z}_{\lE}(\widehat{v}_{n_1 n_2})
    &=
    \frac{
      1
    }{
      \Lambda({\zeta^0_{\lE} , \zeta^1_{\lE}}|{n_1 - n_2})
    }
    \widehat{v}_{n_1 n_2}
    \\
    \mathcal{Z}_{\lW}(\widehat{v}_{n_1 n_2})
    &=
      \omega^{-(N-1)(\zeta_{\lW}^0 + \zeta_{\lW}^1)}
    \frac{
      \omega^{n_2 - n_1} 
    }{
      \Lambda({\zeta^0_{\lW}, \zeta^1_{\lW}}|{n_2 - n_1 -1})
    }
    \widehat{v}_{n_1 n_2}
    \\
    \mathcal{Z}_{\lN}(\widehat{v}_{n})
    &=
    \sum_{n'=0}^{N -1}
    \Lambda({\zeta^0_{\lN}, \zeta^1_{\lN}}|{n'-n})\widehat{v}_{n'}
    \\
    \mathcal{Z}_{\lS}(\widehat{v}_{n})
    &=
    \sum_{n'=0}^{N -1}
    \Lambda({\zeta^0_{\lS}, \zeta^1_{\lS}}|{n-n'})\widehat{v}_{n'}
  
\end{aligned}$$

At a negative crossing we instead have a factorization $$\label{eq:R-factorization-negative}
    \frac{
      1
    }{
      N
    }
    \overline{\mathcal{Z}}_{\lE} (\overline{\mathcal{Z}}_{\lS} \otimes \overline{\mathcal{Z}}_{\lN}) \overline{\mathcal{Z}}_{\lW}$$ in terms of operators $$\begin{aligned}
    \overline{\mathcal{Z}}_{\lE}(\widehat{v}_{n_1 n_2})
    &=
    \omega^{-(N -1)(\zeta_{\lE}^0 + \zeta_{\lE}^1)}
    \qlf{\zeta_{\lE}^0, \zeta_{\lE}^1}{n_1 - n_2 - 1}
    \widehat{v}_{n_1 n_2}
    \\
    \overline{\mathcal{Z}}_{\lW}(\widehat{v}_{n_1 n_2})
    &=
    \omega^{n_2 - n_1}
    \qlf{\zeta_{\lW}^0, \zeta_{\lW}^1}{n_2 - n_1} \widehat{v}_{n_1 n_2}
    \\
    \overline{\mathcal{Z}}_{\lN}(\widehat{v}_n)
    &=
    \omega^{(N -1)(\zeta_{\lN}^0 + \zeta_{\lN}^1)}
    \sum_{n'}
    \frac{
      1
    }{
      \qlf{\zeta_{\lN}^0, \zeta_{\lN}^1}{n - n' - 1}
    }
    \widehat{v}_{n'}
    \\
    \overline{\mathcal{Z}}_{\lS}(\widehat{v}_n)
    &=
    \omega^{(N -1)(\zeta_{\lS}^0 + \zeta_{\lS}^1)}
    \sum_{n'}
    \frac{
      1
    }{
      \qlf{\zeta_{\lS}^0, \zeta_{\lS}^1}{n' - n - 1}
    }
    \widehat{v}_{n'}
  
\end{aligned}$$
:::

In both cases the overall matrix does not depend on the choice of $\kappa$ for the crossing but the operator factors $\mathcal{Z}_i$ do.

::: proof
*Proof.* follows immediately from [\[eq:R-mat-positive\]](#eq:R-mat-positive){reference-type="ref" reference="eq:R-mat-positive"}, and similarly for the negative case. (Recall that the braiding is given by the $R$-matrix followed by a flip map.) ◻
:::

::: marginfigure
:::

This factorization has a natural geometric interpretation. Thinking of a crossing as coming out of the page we can associate it to the triangulated punctured disc shown in [\[fig:triangulated-braiding-0\]](#fig:triangulated-braiding-0){reference-type="ref" reference="fig:triangulated-braiding-0"}. The braiding can then be implemented as a series of flips in this triangulation, and each operator factor is associated to a flip. From a $3$-dimensional point of view each flip can be thought of as building an ideal tetrahedron, so the braiding corresponds to a (twisted) ideal octahedron, as in [1](#fig:build-ideal-octahedron){reference-type="ref" reference="fig:build-ideal-octahedron"}. We show a side view of the octahedron in [\[fig:octahedron-side\]](#fig:octahedron-side){reference-type="ref" reference="fig:octahedron-side"}. This leads directly to the [@Kim2018], an ideal triangulation of the tangle complement associated to a choice of diagram.

The parameters of the $\chi$-coloring are geometrically natural: they parametrize hyperbolic structures on the octahedral decomposition [@McPhailSnyder2022; @McPhailSnyder2024] and can be used to can be used to directly compute the Chern-Simons invariant via a sum of dilogarithms [@Cho2014; @McPhailSnyderVolume]. Our $R$-matrix is analogous: instead of a scalar-valued dilogarithm for each factor we have a matrix-valued quantum dilogarithm. This analogy is discussed further in [@McPhailSnyderVolume].

The crossing is pinched exactly when the ideal tetrahedra are geometrically degenerate. In this case the log-parameters $\zeta_j^0$ lie in $\mathbb{Z}$, so the quantum dilogarithms have zeros and poles. In [\[thm:R-mat-pinched\]](#thm:R-mat-pinched){reference-type="ref" reference="thm:R-mat-pinched"} we show that the overall $R$-matrix has a well-defined limit, namely Kashaev's $R$-matrix [@Kashaev1995]. However the factorization only holds in a weaker sense: we still have a product of four operators $\mathcal{Z}_j$, each of which depends on only two of the tensor indices, but there is now a cutoff term $\theta_{n_1 n_2}^{n_1' n_2'} \in \left\{ \def\given{\ \middle| \ }  0, 1 \right\}$ involving every index at the crossing.
