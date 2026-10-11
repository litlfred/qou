---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-012-334-radial-asymptotic-analysis-for-the-second-tr
section_title: "Radial asymptotic analysis for the second trace"
section_number: 3.3.4
pages: 38-39
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
doc_brief: "Peacock patterns and new integer invariants in topological string theory — Topological string theory near the conifold point of a Calabi–Yau threefold gives rise to factorially divergent power series"
text_source: latex
latex_prose_ratio: 0.926
latex_coverage_ratio: 1.0
---
\label{sc:rasym-P2}

We study here the representation of the anti-holomorphic blocks in
terms of Borel resummation of asymptotic series.
In general, we find
\begin{equation}
  \ri\sqrt{3}
  \begin{pmatrix}
    \wt{H}_0(\tq)\\
    -\frac{27}{4\pi^2g_s^2}q^{1/3}\wt{H}_1(\tq)
  \end{pmatrix}
  =
  M_R(q) s_R
  \begin{pmatrix}
    \Phi_{0;2}\\
    -\frac{1}{3}q^{1/6}\Phi_{1;2}
  \end{pmatrix}(g_s)
  \label{eq:rasym-P2}
\end{equation}
with
\begin{equation}
  M_R(q) =   \begin{pmatrix}
    1 & M^{R}_{01}(q)\\
    0 & M^{R}_{11}(q)
  \end{pmatrix}
\end{equation}

where $M_{01}^R(q), M_{11}^R(q)$ are $q$-series that parametrise
non-perturbative corrections, and their expressions depend on the
sector $R$ the coupling $g_s$ is in. The Borel resummation of
$\Phi_{1;2}(g_s)$ is known exactly, and since we have 700 terms of
$\Phi_{0;2}(g_s)$, we can compute the Borel resummation with very high
numerical precision\footnote{We further improved the precision of
  Borel resummation with the help of conformal maps
  \cite{Costin:2019xql,Costin:2020hwg}.}, and therefore we are able to
compute the non-perturbative corrections to very high orders:
\begin{subequations}
\label{mP2-qseries}
\begin{align}
  M_{01}^{I}(q) =
  &-2+3q^{1/3}-6q^{2/3}+11q-18q^{4/3}+27q^{5/3}-37q^2
    +45q^{7/3}-48q^{8/3}\nn
  &+45q^{3}-36q^{10/3}+24q^{11/3}-18q^4+\ldots,
  \label{eq:M01I-P2}\\
  M_{01}^{II}(q) =
  &1+3q^{1/3}+6q^{2/3}+8q+9q^{4/3}+12q^{5/3}+17q^{2}
    +18q^{7/3}+15q^{8/3}+19q^{3}\nn
  &+30q^{10/3}+30q^{11/3}+20q^{4} +27q^{13/3}+\ldots,
  \label{eq:M01II-P2}\\
  M_{11}^{I}(q) =
  &1-6q^{1/3}+18q^{2/3}-35q+42q^{4/3}-9q^{5/3}-85q^2
    +204q^{7/3}-225 q^{8/3} \nn
  &- 10 q^3 + 522 q^{10/3}- 990 q^{11/3} + 775 q^4+\ldots,
  \label{eq:M11I-P2}\\
  M_{11}^{II}(q) =
  &1+3q^{1/3}-5q+6q^{4/3}+9q^{5/3}-25q^2-3q^{7/3}+63q^{8/3}
    -45q^3  -96q^{10/3}\nn
  &+180q^{11/3}+26 q^4+\ldots
    \label{eq:M11II-P2}
\end{align}
\end{subequations}
It is easy to identify that
\begin{equation}
  M_{11}^{I}(q)
  = \frac{(q^{1/3};q)_\infty^6}{(q;q)_\infty^{3}(q^{2/3};q)_\infty^3},  
  \quad
  M_{11}^{II}(q)
  =\frac{(q^{2/3};q)_\infty^6}{(q;q)_\infty^{3}(q^{1/3};q)_\infty^3}.
\end{equation}
By inverting the matrix $M_R(q)$ in \eqref{eq:rasym-P2} one finds
the holomorphic lift of $s_R(\Phi_{0;2})(g_s)$
\begin{equation}
  s_R(\Phi_{0;2})(g_s) = \ri\sqrt{3}\left(
    \wt{H}_0(\tq) +
    3\bb^{4}\frac{M^R_{01}}{M^R_{11}}q^{1/3} \wt{H}_1(\tq)
  \right).
\end{equation}
Comparison with \eqref{eq:hlift-P2} together with \eqref{eq:redfac}
leads to
\begin{equation}
  M_{01}^{II}(q) = \frac{(q^{2/3};q)_\infty(q;q)_\infty}
  {(q^{1/3};q)_\infty(q^{4/3};q)_\infty}
  \qhg{3}{2}{q^{1/3},q^{2/3},q^{2/3}}{q,q^{4/3}}{q}{q^{2/3}},
\end{equation}
which agrees with the numerical result \eqref{eq:M01II-P2}.
Finally by comparing \eqref{eq:rasym-P2} applied in both sectors $I$
and $II$ we find
\begin{equation}
  \ms{S}_{01;2}^+(q)=K_2(q) = -\frac{1}{3}q^{1/6}\left(M_{01}^I(q) - \frac{M_{01}^{II}(q)}{M_{11}^{II}(q)}M_{11}^I(q)\right),
\end{equation}
which yields \eqref{eq:S01-P2}.

With the above ingredients, it should be possible to obtain appropriate descendants of the 
holomorphic blocks, as in \cite{ggm1,ggm2} and section \ref{sc:block-F0}. This would make it possible to conjecture
exact expressions for the $q$-series in (\ref{mP2-qseries}), and therefore for the Stokes constants.
