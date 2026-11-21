---
doc_id: arxiv-math-ph-0405028v2
doc_title: "ON THE QUANTUM INVARIANT FOR THE BRIESKORN HOMOLOGY SPHERES"
section_id: sec-006-the-ohtsuki-invariant
section_title: "The Ohtsuki Invariant"
section_number: null
pages: 20-23
source_pdf: 0405028v2.pdf
source_sha256: 90a0e4ba456988d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.825
latex_coverage_ratio: 1.0
doc_brief: "ON THE QUANTUM INVARIANT FOR THE BRIESKORN HOMOLOGY SPHERES — We study an exact asymptotic behavior of the Witten–Reshetikhin–Turaev SU(2) in- variant for the Brieskorn homology spheres Σ(p1, p2, p3)"
---
[]{#sec:Ohtsuki label="sec:Ohtsuki"}

From asymptotic expansions [\[tau_limit\]](#tau_limit){reference-type="eqref" reference="tau_limit"} and [\[tau_Poincare_limit\]](#tau_Poincare_limit){reference-type="eqref" reference="tau_Poincare_limit"} of the WRT invariant, we can introduce a formal power series which is ignored in section [\[sec:torsion\]](#sec:torsion){reference-type="ref" reference="sec:torsion"}. This series may denote a trivial connection contribution [@LRozan96f; @LRozan97a; @LawreRozan99a]. By regarding $\mathrm{e}^{2 \pi \mathrm{i}/N}$ as $q$, we can define $\tau_\infty(\mathcal{M})$ for a case of $\frac{1}{p_1} + \frac{1}{p_2} +\frac{1}{p_3} <1$ $$\label{infinity_general}
  q^{
    \frac{\phi(p_1,p_2,p_3)}{4} - \frac{1}{2} 
  } \,
  \left(
    q
    - 1
  \right)
  \,
  \tau_\infty\bigl( \Sigma(p_1, p_2, p_3) \bigr)
  =
  \frac{1}{2} \sum_{k=0}^\infty
  \frac{L(-2 \, k , \chi_{2 P}^{(1,1,1)})}{k!}
  \,
  \left(
    \frac{\log q}{
      4 \, P 
    }
  \right)^k$$ and for the Poincaré homology sphere $$\label{infinity_Poincare}
  q^{
    \frac{121}{120}
  } \,
  \left(
    q    - 1
  \right)
  \,    \tau_\infty \bigl( \Sigma(2,3,5) \bigr)
  =
  q^{\frac{1}{120} }
  +
  \frac{1}{2}
  \sum_{k=0}^\infty
  \frac{L(-2 \, k , \chi_{60}^{(1,1,1)})}{k!} \,
  \left(
    \frac{\log q}{120}
  \right)^k$$ With these definitions the Ohtsuki invariant [@TOhtsu96a] is defined by the formal series for $\tau_\infty(\mathcal{M})$; $$\tau_\infty\bigl( \Sigma(p_1, p_2, p_3) \bigr)

  =
  \sum_{n=0}^\infty
  \lambda_n \bigl( \Sigma(p_1, p_2, p_3) \bigr)

  \cdot (q-1)^{n}$$

Infinite series in eqs. [\[infinity_general\]](#infinity_general){reference-type="eqref" reference="infinity_general"} and [\[infinity_Poincare\]](#infinity_Poincare){reference-type="eqref" reference="infinity_Poincare"} originate from an asymptotic expansion of the integral $r_{\boldsymbol{p}}^{(1,1,1)}(1/N ; 0)$ defined in eq. [\[define_r_function\]](#define_r_function){reference-type="eqref" reference="define_r_function"}, which appears as a *tail* of the nearly modular property of the Eichler integral. It is noted that an integral formula for the Ohtsuki invariant was studied in Refs.  by a different method.

To compute an explicit form of $\lambda_n(\mathcal{M})$, we use the Stirling number of the first kind defined by $$\prod_{j=0}^{n-1}(x - j)
  =
  \sum_{m=0}^n
  S_n^{(m)}  \, x^m$$ As the Stirling number satisfies (see, *e.g.*, Ref. ) $$\frac{(\log q)^m}{m!}
  =
  \sum_{n=m}^\infty
  S_n^{(m)} \,
  \frac{ (q -1 )^n }{n!}$$ we can easily obtain the following expression.

::: theorem
Let the function $\Lambda_n(p_1,p_2,p_3)$ be defined by $$\begin{gathered}
    \Lambda_{n}(p_1,p_2,p_3)
    =
    \frac{1}{2} \, \frac{1}{(n+1)!} \,
    \sum_{m=1}^{n+1}
    S_{n+1}^{(m)} \,
    \left(
      \frac{2-\phi(p_1,p_2,p_3)}{4} 
    \right)^m
    \\
    \times
    \sum_{k=0}^m
    \begin{pmatrix}
      m \\
      k
    \end{pmatrix}
    \, 
    \left(
      \frac{1}{P \, (2 - \phi(p_1,p_2,p_3))}
    \right)^k \,
    L(-2 \, k , \chi_{2 P}^{(1,1,1)})
  
\end{gathered}$$ Then the invariant $\lambda_n(\mathcal{M})$ is computed as follows; $$\label{lambda_Brieskorn}
    \lambda_{n}\bigl( \Sigma(p_1, p_2, p_3) \bigr)
    =
    \begin{cases}
      \Lambda_n( p_1,p_2, p_3)
      &
      \text{for $\displaystyle
        \frac{1}{p_1} +     \frac{1}{p_2}+    \frac{1}{p_3} <1
        $}
      \\[5mm]

      \Lambda_n(2,3,5) + (-1)^{n+1}
      &
      \text{for the Poincar{\'e} homology sphere}
    \end{cases}$$
:::

We note that a value of the $L$-function, which is given by eq. [\[L_and_Bernoulli\]](#L_and_Bernoulli){reference-type="eqref" reference="L_and_Bernoulli"}, can be computed easily from a generating function for a case of $(\ell_1,\ell_2,\ell_3)=(1,1,1)$; $$\begin{aligned}
  -2 \, \mathop{\mathrm{ch}}(z)
  +








  2 \,
  \frac{
    \mathop{\mathrm{sh}}( 6 \, z) \,
    \mathop{\mathrm{sh}}( 10 \, z) \,
    }{
      \mathop{\mathrm{ch}}( 15 \, z)
    }
    & =
    - 2 \,
    \frac{\mathop{\mathrm{ch}}(9 \, z) \, \mathop{\mathrm{ch}}(5 \, z)}{
      \mathop{\mathrm{ch}}(15 \, z)
    }
    \nonumber
    \\
    & =
    \sum_{n=0}^\infty
    \frac{
      L(-2 \, n , \chi_{60}^{(1,1,1)})
    }{(2 \, n)!} \,
    z^{2 n}
  
\end{aligned}$$ and in a case of $\frac{1}{p_1} +     \frac{1}{p_2}+     \frac{1}{p_3} <1$ we have $$\label{generating_Sigma}
  4 \,
  \frac{
    \mathop{\mathrm{sh}}( p_1 \, p_2 \, z) \,
    \mathop{\mathrm{sh}}( p_1 \, p_3 \, z) \,
    \mathop{\mathrm{sh}}( p_2 \, p_3 \, z) 
    }{
      \mathop{\mathrm{sh}}( p_1 \, p_2 \, p_3 \, z)
    }
    =
    \sum_{n=0}^\infty
    \frac{
      L(-2 \, n , \chi_{2 P}^{(1,1,1)})
    }{(2 \, n)!} \,
    z^{2 n}$$

See Table [\[table:lambda\]](#table:lambda){reference-type="ref" reference="table:lambda"} for explicit values of $\lambda_n(\mathcal{M})$ for some Brieskorn spheres.

We can rewrite eq. [\[lambda_Brieskorn\]](#lambda_Brieskorn){reference-type="eqref" reference="lambda_Brieskorn"} for the first three terms as follows; $$\begin{aligned}
  \lambda_0 \bigl( \Sigma(p_1, p_2, p_3) \bigr)

  & = 1
  \\[2mm]

  \lambda_1 \bigl( \Sigma(p_1, p_2, p_3) \bigr)

  & =
  -\frac{1}{4} \,
  \left(
    \phi + P \,
    \Bigl(
      1-\frac{1}{p_1^{~2}}-\frac{1}{p_2^{~2}}-\frac{1}{p_3^{~2}}
    \Bigr)
  \right)
  \\[2mm]

  \lambda_2 \bigl( \Sigma(p_1, p_2, p_3) \bigr)

  & =
  \frac{1}{12} \,\Biggl(
    \frac{3 \, \phi^2 + 12 \, \phi -4}{8}
    +
    \frac{3 \, P}{4} \, (\phi +2) \,
    \Bigl(
      1- \sum_{j=1}^3 \frac{1}{p_j^{~2}}
    \Bigr)
    \nonumber 
    \\
    & \qquad \qquad 
    +
    \frac{P^2}{8} \,
    \left(
      2 \, \Bigl( 1- \sum_{j=1}^3 \frac{1}{p_j^{~4}} \Bigr)
      +
      5 \, \Bigl( 1- \sum_{j=1}^3 \frac{1}{p_j^{~2}} \Bigr)^2
    \right)
  \Biggr)
\end{aligned}$$ where we mean $\phi=\phi(p_1, p_2, p_3)$ defined in eq. [\[phi_definition\]](#phi_definition){reference-type="eqref" reference="phi_definition"}. As was proved in Refs.  we see that $$\begin{gathered}
  \lambda_0
  \bigl( \Sigma(p_1, p_2, p_3) \bigr)
  =
  1

  \\[2mm]

  \lambda_1
  \bigl( \Sigma(p_1, p_2, p_3) \bigr)
  =
  6 \,



  \lambda_C  \bigl( \Sigma(p_1, p_2, p_3) \bigr)
\end{gathered}$$ where

$\lambda_C(\mathcal{M})$ is the Casson invariant [\[Casson_sphere\]](#Casson_sphere){reference-type="eqref" reference="Casson_sphere"} for $\mathcal{M}$. It is noted that $\lambda_2\bigl(\Sigma(p_1,p_2,p_3)\bigr)$ is calculated in Ref. .
