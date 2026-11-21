---
doc_id: arxiv-math-ph-0105039v1
doc_title: "Hyperbolic Structure Arising from a Knot Invariant"
section_id: sec-004-23-representation
section_title: "Representation"
section_number: 2.3
pages: 8-10
source_pdf: 0105039v1.pdf
source_sha256: 850e6a00721e38d0
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.909
latex_coverage_ratio: 1.0
doc_brief: "Hyperbolic Structure Arising from a Knot Invariant — We study the knot invariant based on the quantum dilogarithm function."
---
We now give  the  representation of these operators on the momentum
space;
$\Hat{p} \, |p \rangle = p \, | p \rangle$ with $p\in \mathbb{R}$,
and we take the vector space as
$\mathbf{V} = L^2(\mathbb{R})$.
The matrix elements  of the $S$-operators are  given by~\cite{Hikam00a}
\begin{subequations}
  \label{S_element}
\begin{align}
  \langle p_1, p_2 \ | \ S_{1, 2} \ | \ p_1^\prime , p_2^\prime \rangle
  & =
  \frac{1}{4 \, \pi \, \gamma} \,
  \delta(p_1 +  p_2 - p_1^\prime ) \,
  \int \mathrm{d} x \
  \Phi_\gamma(x+p_1) \,
  \mathrm{e}^{
    \frac{1}{2 \, \gamma \, \mathrm{i}} \,
    \left(
      (p_2 - p_2^\prime) \,   x
      -  \frac{1}{2}(p_2 -  p_2^\prime)^2
    \right)
    } ,
  \\[2mm]

  \langle p_1, p_2  \ | \ S_{1, 2}^{~-1} \ | \ p_1^\prime , p_2^\prime \rangle
  & =
  \frac{1}{4 \, \pi \, \gamma} \,
  \delta(p_1 -p_1^\prime - p_2^\prime ) \,
  \int \mathrm{d} x \
  \frac{1}{\Phi_\gamma(x+p_1^\prime)} \,
  \mathrm{e}^{
    \frac{1}{2 \, \gamma \, \mathrm{i}} \,
    \left(
      (p_2 - p_2^\prime) \,   x
      + \frac{1}{2}(p_2 -  p_2^\prime)^2
    \right)
    }  .
\end{align}
\end{subequations}
Due to the Fourier transform~\eqref{Fourier_transform}, these
integrals reduce to
\begin{subequations}
  \label{S_element_2}
  \begin{gather}
    \begin{split}
      & \langle p_1, p_2  \ | \ S_{1, 2}  \ | \ p_1^\prime , p_2^\prime \rangle
      \\
      &  \qquad =
      \frac{1}{\sqrt{4 \, \pi \, \gamma}} \,
      \delta(p_1 + p_2 - p_1^\prime) \cdot
      \Phi_\gamma(p_2^\prime - p_2
      + \mathrm{i} \, \pi + \mathrm{i} \, \gamma) \,
      \mathrm{e}^{\frac{1}{2 \, \mathrm{i} \, \gamma}
        \left(
          - \frac{\pi^2 + \gamma^2}{6} - \frac{\gamma \, \pi}{2}
          + p_1 \, (p_2^\prime - p_2)
        \right)
        } ,
    \end{split}
    \\[4mm]

    \begin{split}
      & \langle p_1, p_2 \ | \ S_{1, 2}^{~-1} \ | \ p_1^\prime , p_2^\prime
      \rangle
      \\
      &  \qquad =
      \frac{1}{\sqrt{4 \, \pi \, \gamma}} \,
      \delta(p_1 - p_1^\prime - p_2^\prime) \,
      \frac{1}{
        \Phi_\gamma(p_2 - p_2^\prime - \mathrm{i} \, \pi
        - \mathrm{i} \, \gamma)
        } \,
      \mathrm{e}^{
        \frac{1}{2 \mathrm{i} \gamma}
        \left(
        \frac{\pi^2 + \gamma^2}{6}
        + \frac{\gamma \, \pi}{2}
        - p_1^\prime ( p_2 - p_2^\prime)
        \right)
        } .
    \end{split}
  \end{gather}
\end{subequations}
The $R$-matrix  is also computed from eqs.~\eqref{R_compact}
and~\eqref{S_element}
as~\cite{Hikam00a}
\begin{subequations}
  \label{R_element}
  \begin{multline}
    \langle p_1, p_2, p_3 , p_4 \ | \  \Check{R}_{1 2, 3 4}  \ | \
    p_1^\prime , p_2^\prime, p_3^\prime, p_4^\prime \rangle
    \\
    =
    \delta(p_1 -p_2+p_3- p_1^\prime) \,
    \delta(p_2^\prime - p_3^\prime - p_4  + p_4^\prime) 
    \\
    \times
    H(p_2^\prime - p_3^\prime , p_3 - p_4^\prime ,
    p_3 - p_2, p_2^\prime  - p_1)  ,











  \end{multline}

  \begin{multline}
    \langle p_1, p_2, p_3 , p_4 \  | \ ( \Check{R}_{1 2, 3 4} )^{-1}
    \ | \
    p_1^\prime , p_2^\prime, p_3^\prime, p_4^\prime \rangle
    \\
    =
    \delta(p_4^\prime  -p_2+p_3- p_4) \,
    \delta(p_1 - p_1^\prime - p_3^\prime  + p_2^\prime) 
    \\
    \times
    H(p_4^\prime - p_4, p_1 - p_3 ,
    p_1 - p_1^\prime , p_4^\prime - p_2^\prime)  .











  \end{multline}
\end{subequations}
Here the integral $H(a,b,c,d)$ is defined as
\begin{subequations}
  \label{integral_H}
  \begin{align}
    & H(a,b,c,d)
    \nonumber   \\
    & =
    \frac{1}{(4 \, \pi \, \gamma)^2} \,
    \iint \mathrm{d} x \ \mathrm{d} y \
    \frac{
      \Phi_\gamma(x+a) \, \Phi_\gamma(y+c)
      }{
      \Phi_\gamma(x+b) \, \Phi_\gamma(y+d)
      } \,
    \mathrm{e}^{ \frac{1}{2 \,  \mathrm{i} \, \gamma}
      \left(
        -(b-c) \,x + (a-d) \, y - \frac{1}{2}(a-d)^2 - \frac{1}{2}(b-c)^2
      \right)
      }
    \label{integral_H_1}
    \\
    & =
    \frac{1}{4 \, \pi \, \gamma} \,
    \frac{
      \Phi_\gamma(a - b - \mathrm{i} \pi - \mathrm{i} \gamma)
      \cdot
      \Phi_\gamma(d - a + \mathrm{i} \pi + \mathrm{i} \gamma)
      }{
      \Phi_\gamma(c - b - \mathrm{i} \pi - \mathrm{i} \gamma)
      \cdot
      \Phi_\gamma(d - c + \mathrm{i} \pi + \mathrm{i} \gamma)
      }


    \cdot
    \frac{
      \mathrm{e}^{
        \frac{1}{2 \mathrm{i} \gamma} \,
        c( -a+b-c+d)
        }
      }{
      (1- \mathrm{e}^{a-c}) \,
      (1 - \mathrm{e}^{\frac{\pi}{\gamma}(a-c)})
      } ,
  \end{align}
\end{subequations}
where the second equality follows from eq.~\eqref{Fourier_transform}.

As we see that
$H(a,b,c,d) = H(c,d,a,b)$ from eq.~\eqref{integral_H_1}, we have  the
symmetry of the $R$-matrix as
\begin{subequations}
  \label{symmetry_R}
  \begin{gather}
    \langle p_1, p_2 , p_3 , p_4 \ | \  \Check{R} \
    | \  p_1^\prime , p_2^\prime , p_3^\prime , p_4^\prime \rangle
    =
    \langle p_4^\prime , p_3^\prime , p_2^\prime , p_1^\prime \
    | \ \Check{R} \ | \
    p_4 , p_3 , p_2 , p_1 \rangle ,
    \label{R_and_R}
    \\[2mm]

    \langle p_1, p_2 , p_3 , p_4 \  | \ \Check{R}^{-1} \
    | \ p_1^\prime , p_2^\prime , p_3^\prime , p_4^\prime \rangle
    =
    \langle
    p_2^\prime , p_1^\prime, p_1 , p_2 \  | \  \Check{R} \  | \
    p_3^\prime , p_4^\prime , p_4 , p_3 \rangle .
    \label{R_and_R_inv}
  \end{gather}
\end{subequations}
