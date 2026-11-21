---
doc_id: arxiv-1908.07065v3
doc_title: "Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-010-42-comparison-to-borel-resummation
section_title: "Comparison to Borel resummation"
section_number: 4.2
pages: 25-29
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.995
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve of N = 2, SU(2) super Yang–Mills"
---
\label{bo}

We now have two different approaches to the calculation of (resummed)
quantum periods: on the one hand, we have the Borel resummation of the
all-orders WKB expansion in $\hbar^2$, which is also calculated by the
TBA equations of section \ref{tbagmn}. On the other hand, instanton
calculus gives a different resummation, based on a convergent
expansion in $\Lambda$, as a function of $\hbar$. An obvious question
is: what is the precise relation between these two resummations? Since
both lead to the same asymptotic expansion in powers of $\hbar$, we
expect that they will differ in non-perturbative effects. In this
section we will address this issue.  Results along these lines have
been previously obtained in \cite{kpt,ashok}. For simplicity, we will
restrict ourselves to the case in which $\hbar>0$ and $u$ is real.

Let us first consider the weak coupling region $\CW$. Here, the
all-orders WKB quantum $A$ period is Borel summable for $\hbar$ real,
and we find that its Borel sum agrees well with $2 \pi a(u, \hbar)$
obtained by inverting \eqref{mmap} or with the solution \eqref{inta}
to the Riccati equation, i.e.

\be
s(\Pi_A)(E,\hbar)= \Pi_A^{\rm ex}( E,\hbar), \qquad |u|>1, \quad \hbar>0. 
\ee

We illustrate this in Table~\ref{tb:BorelSum-A} where we compare the
Borel sum of the WKB quantum $A$ period at $u=4$ and $\hbar=1$, with
increasing number of corrections, to the result of instanton
calculus. They agree with almost all the stabilised digits (27 of
them).

\begin{table}
  \centering
  \begin{tabular}{cc}\toprule
    terms included & Borel sum \\\midrule
    190 & 35.40661948105291481767982565157 \\
    191 & \underline{35.40661948105291481767982565}207\\\midrule
    gauge theory & 35.40661948105291481767982564492 \\\bottomrule
  \end{tabular}
  \caption{Borel sum of quantum $A$ period at $u=4$ and
    $\hbar=1$. Underlined are stabilised digits.}
  \label{tb:BorelSum-A}
\end{table}

The quantum $B$ period, on the other hand, is not Borel summable along
the real axis in the weak coupling region. Nevertheless, we can make
the following observation. The ``exact" quantum $B$ period is given by
\begin{equation}
  \label{adgauge} 2 \ri a_D(u, \hbar)=4 \ri \gamma
  (a,\hbar )+2 \ri \partial_{a}F_{\rm NS}^{\rm inst}(a, \hbar)
\end{equation}
where $\gamma$ is defined in \eqref{gammadef} and has the following
asymptotic expansion for large $a/\hbar$:

\begin{equation}
  \label{asympt}
  \gamma(a, \hbar)\sim a \left( \log \left( {a \over \Lambda}
    \right)-1\right)+a \sum_{n \ge 1} {(-1)^n B_{2n} \over 2n (2n-1)}
  \left({\hbar \over a}\right)^{2n}.  
\end{equation}

The series in $\hbar/a$ in the r.h.s. is not Borel summable along the
positive real axis. More precisely, let us consider the following
formal power series:

\begin{equation}
  \varphi(z)= \sum_{n \ge0} c_n z^{2n}, \qquad c_{n-1}={ (-1)^n B_{2n}
    \over 2n (2n-1)}.   
\end{equation}

A little numerical experimentation shows that the lateral
resummations of this series along the positive real axis are given by

\begin{equation}
  \label{disc-gamma}
  s_{\pm}(\varphi)(z)= f(z) \pm {\ri \over 2z} \log \left(1- \re^{-2\pi/z} \right), 
\end{equation}

where 

\begin{equation}
  f(z)= {1\over z^2} \left( \log(z)+1 \right)-{\pi \over 4z}  -{\ri
    \over 2 z} \log {\Gamma( 1+\ri/z) \over \Gamma(1-\ri /z) }. 
\end{equation}

(A similar series has been considered in \cite{hm}). 
\begin{figure}
  \centering
  \includegraphics[width=0.45\linewidth]{phiaDformal}
  \caption{Poles of the Borel--Pad\'e transform of the ``reduced" series
    $\Pi_B^{\rm red}$ at $u=4$.}
  \label{fg:Borel-aDformal}
\end{figure}







The above analysis suggests that the non-Borel summability of the
sequence $\Pi_B^{(n)}$ along the positive real axis in the weak
coupling region is due to the asymptotic series appearing in
$\gamma(a,\hbar)$. In view of (\ref{disc-gamma}), this leads to the
right discontinuity across the positive real axis:

\begin{equation}
  -4 \hbar \log (1 -\re^{-4 \pi a/\hbar}). 
\end{equation}
 
This suggests that the ``reduced" formal power series

\begin{equation}\label{piBformal}
  \Pi^{\text{red}}_B(E,\hbar):=
  \Pi_B(E,\hbar)-4 \ri \Pi_A (E,\hbar)
  \sum_{n \ge 1} {(-1)^n B_{2n} \over 2n (2n-1)}
  \left( {\hbar \over 2\Pi_A(E,\hbar)}\right)^{2n},
\end{equation}

where we subtract the non-Borel summable series in the function
$\gamma(a, \hbar)$, is actually Borel summable along the positive real
axis. We verified numerically that this indeed is true, as can be seen
from the Borel plane plot at $u=4$ given in
Figure~\ref{fg:Borel-aDformal}. In fact the Borel sum of
$\Pi^{\text{red}}_B(E,\hbar)$

agrees with the gauge theory calculation in which the contribution of
$\gamma(a,\hbar)$ has been removed; in other words,

\begin{equation}\label{ared}
  s\left( \Pi^{\text{red}}_B \right)(E,\hbar)=2\ri a_D^{\text{red}}(u,\hbar):= 4\ri
  a\(\log\(\frac{a}{\Lambda}\)-1\)
  +2\ri\frac{\pd F^{\text{inst}}_{\text{NS}}(a,\hbar)}{\pd a} \ .
\end{equation}





We illustrate this in Table~\ref{tb:BorelSum-B}, where both the Borel
sum of $\Pi^{\text{red}}_B(E,\hbar)$ and
$2\ri a_D^{\text{red}}(u,\hbar)$ are evaluated at $u=4$ and
$\hbar=1$. We find that all stabilised digits are in agreement (26 of
them)\footnote{We also notice that the exact $B$ period
  $\Pi_B^{\text{ex}}(E,\hbar)$ with $E>2$ agrees with the average of
  lateral Borel resummations of the quantum $B$ period
  $\Pi_B(E,\hbar)$.}.

We can now see a clear difference between the TBA equations of
\cite{ns} and the TBA equations of \cite{gmn}. The TBA equations of
\cite{ns} compute the Borel-summable part of the $B$ period, where we
have removed the perturbative contribution due to the $\gamma$
function, i.e.~they compute \eqref{ared}, which is the Borel
resummation of $\Pi_B^{\rm red}$ in \eqref{piBformal}.  On the
contrary, the conformal limit of the GMN TBA equations computes the
Borel resummation of the {\it full} quantum $B$ period $\Pi_B(E,\hbar)$,
including the perturbative $\gamma$ function. Since the latter is not
Borel summable, the corresponding TBA has discontinuities, as discussed in
section~\ref{sc:SW-TBA}.

\begin{table}
  \centering
  \begin{tabular}{ccl}\toprule
    & terms & \\\midrule
    \multirow{2}{*}{$\Pi^{\text{red}}_B$}
    &159 & 16.474810551500808917635392219 \\
    &161 & \underline{16.474810551500808917635392}368 \\\midrule
    \multirow{2}{*}{$2\ri a_D^{\text{red}}$}
    &14 & 16.47481055150080891763539232909\\
    &15 & \underline{16.474810551500808917635392329}20 \\\bottomrule
  \end{tabular}
  \caption{Comparison between the Borel sum of the ``reduced" quantum $B$ period
    $\Pi^{\text{red}}_B$ at $u=4$ and $\hbar=1$ (with
    increasing number of terms), and the exact, ``reduced" period
    $2\ri a_D^{\text{red}}$ defined in (\ref{ared}) (with
    increasing number of instanton corrections). Underlined are
    stabilised digits.}
  \label{tb:BorelSum-B}
\end{table}

\begin{table}
  \centering
  \begin{tabular}{cl}\toprule
    terms & first line of r.h.s. of \eqref{eq:Pi-ex}\\\midrule
    191 & $806502.11499751621351505261143$\\
    193 & $\underline{806502.11499751621351505261}260$ \\\midrule
    l.h.s. of \eqref{eq:Pi-ex}
          & $806502.11499751621351505261016$\\
    \bottomrule                  
  \end{tabular}
  \caption{Numerical verification of the characteristic exponent
    formula \eqref{eq:Pi-ex} at $u=0$ and $\hbar=1/4$, 
    with increasing number of terms for the lateral Borel
    resummations on the r.h.s.. All the stabilised digits (underlined)
    are in agreement.}
  \label{tb:Pi-ex}
\end{table}

In the strong coupling region we have the
following relation between the ``exact" quantum $A$ period and lateral 
Borel resummations of quantum periods \cite{kpt}

\begin{equation}\label{eq:Pi-ex}
\begin{aligned}
  2 \cosh(\Pi_A^{\text{ex}}/(2\hbar))
  &= \re^{\frac{1}{2\hbar}s_+(\Pi_A)} + \re^{\frac{1}{2\hbar}s_+(\Pi_A+2\Pi_B)}
  + \re^{-\frac{1}{2\hbar}s_+(\Pi_A+2\Pi_B)} \\
  &=\re^{\frac{1}{2\hbar}s_-(\Pi_A)} + \re^{-\frac{1}{2\hbar}s_-(\Pi_A)} +
    \re^{\frac{1}{2\hbar}s_-(\Pi_A+2\Pi_B)} \ .
  \end{aligned}
\end{equation}

Numerical evidence for this relation is presented in
Table~\ref{tb:Pi-ex} for the first line of the formula, evaluated at
$u=0$ and $\hbar=1/4$. 


The second line of \eqref{eq:Pi-ex} can be
derived from the Stokes automorphism of quantum periods discussed in
section \ref{sc:SW-TBA}.



In the strong coupling region, $\Pi_D=\Pi_B+\Pi_A$ is Borel summable
along the positive real axis, while both the Borel resummations of
$\Pi_B$ and $\Pi_A$ have discontinuities across the positive real
axis. The  discontinuities for the $B$, and $A$ periods
are:

\begin{equation}
  \begin{aligned}
    &s_+(\Pi_B) - s_-(\Pi_B) = 2\hbar \log
    (1+\re^{-\frac{1}{\hbar}s(\Pi_D)})\ ,\\
    &s_+(\Pi_A) - s_-(\Pi_A) = -2\hbar \log
    (1+\re^{-\frac{1}{\hbar}s(\Pi_D)}) \ .
  \end{aligned}
\end{equation}

Starting from the first line on the right hand side of
\eqref{eq:Pi-ex}, and applying the discontinuity formulae, we
immediately get the second line

\begin{align}
  &\text{first line}\nn
  &=
    \re^{\frac{1}{2\hbar}s_+(\Pi_A)} + \re^{\frac{1}{2\hbar}s_+(\Pi_A+2\Pi_B)}
    + \re^{-\frac{1}{2\hbar}s_+(\Pi_A+2\Pi_B)}
    \nn
  &=
    \re^{\frac{1}{2\hbar}s_-(\Pi_A)}\(1+\re^{-\frac{1}{\hbar}s(\Pi_D)}\)^{-1}
    + \re^{\frac{1}{2\hbar}s_-(\Pi_A+2\Pi_B)}\(1+\re^{-\frac{1}{\hbar}s(\Pi_D)}\)
    +
    \re^{-\frac{1}{2\hbar}s_-(\Pi_A+2\Pi_B)}
    \(1+\re^{-\frac{1}{\hbar}s(\Pi_D)}\)^{-1} 
    \nn
  &=
    \(\re^{\frac{1}{2\hbar}s_-(\Pi_A)}+\re^{-\frac{1}{2\hbar}s_-(\Pi_A+2\Pi_B)}\)
    \(1+\re^{-\frac{1}{\hbar}s(\Pi_D)}\)^{-1} +
    \re^{\frac{1}{2\hbar}s_-(\Pi_A+2\Pi_B)}+\re^{-\frac{1}{2\hbar}s_-(\Pi_A)}
    \nn
  &=
    \re^{\frac{1}{2\hbar}s_-(\Pi_A)}+\re^{-\frac{1}{2\hbar}s_-(\Pi_A)}
    +\re^{\frac{1}{2\hbar}s_-(\Pi_A+2\Pi_B)}  = \text{second line} \ .
\end{align}
On the other hand, to derive a similar result for the ``exact''
quantum $B$ period we can use results on the Fredholm determinant of
the modified Mathieu equation, which we present in
section~\ref{tssst}. Eq.\eqref{bspd2} then together \eqref{eq:Pi-ex}
imply that
\begin{equation}\label{eq:Pi-ex-2}
\begin{aligned}
  2\sinh(\Pi^{\text{ex}}_B/(2\hbar))
  &= \re^{\frac{1}{2\hbar} s_+(\Pi_B)}-\re^{-\frac{1}{2\hbar}
    s_+(\Pi_B)}
    - \re^{-\frac{1}{2\hbar} s_+(2\Pi_A+3\Pi_B)}, \\
  &= \re^{\frac{1}{2\hbar} s_-(\Pi_B)}-\re^{-\frac{1}{2\hbar} s_-(\Pi_B)}
    +\re^{-\frac{1}{2\hbar} s_-(2\Pi_A+\Pi_B)} \ ,
  \end{aligned}
\end{equation}
and we have tested these identities numerically to very high
precision.

Summarizing, in the weak coupling region the all-orders WKB quantum $A$
period and the $B$ period (once the gamma function is subtracted) are
Borel summable. Their Borel sums agree with the gauge theory
expressions of section~\ref{ic}. In the strong coupling region, the $A$ and
$B$ periods are not Borel summable, although their lateral Borel resummations can
be related to the exact quantum $A$ period via \eqref{eq:Pi-ex}. We
finally note that the combination $\Pi_D=\Pi_A+\Pi_B$ is Borel
summable in the strong coupling region (only). However, its Borel sum
does not agree with the gauge theory expression of section~\eqref{ic},
namely

\begin{equation}
s(\Pi_D)\neq  \Pi_A^{\rm ex}+\Pi_B^{\rm ex}= 2 \pi a+2 \ri a_D, 
\end{equation}

and one should include additional non-perturbative corrections.  We
will find the correct formula at the end of section~\ref{comp-zamo}.
