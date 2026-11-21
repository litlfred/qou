---
doc_id: arxiv-1908.07065v3
doc_title: "Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-007-33-solving-the-tba-equations-in-the-strong-coupl
section_title: "Solving the TBA equations in the strong coupling region"
section_number: 3.3
pages: 18-20
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.995
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve of N = 2, SU(2) super Yang–Mills"
---
\label{tbau0}

As we have argued, Borel sums of quantum periods are solutions to the TBA
equations \eqref{eq:cTBA-1},\eqref{eq:cTBA-2}. In principle the
resummed quantum periods can be computed from these TBA equations
by using the dictionaries \eqref{eq:TBA-dict-1} and
\eqref{eq:TBA-dict-2}. In practice, however, these equations are
difficult to use. First of all, one needs information on the boundary
conditions at strong coupling in order to solve the equations. In
addition, the standard tools to solve these equations numerically
converge very slowly.

Let us first consider the simplest example at $u=0$, where the TBA
system collapses to a single equation \eqref{u0TBA}, which we
reproduce here (we have absorbed the factor $\xi$ in \eqref{u0TBA} in
the angle $\theta$)

\begin{equation}\label{eq:cTBA-0}
  \epsilon(\theta) = \pi\re^{\theta} -
  \int_{\IR}\frac{\log(1+\re^{-\epsilon(\theta')})}
  {\pi\cosh(\theta-\theta')} 
  \rd \theta' \, .
\end{equation}

The solution can be identified with the quantum dyon period through
the dictionary

\begin{equation}
  \epsilon(\theta) = \frac{1}{\hbar}s(\Pi_D)(u=0,\hbar) \ ,\quad \hbar =
  \Pi^{(0)}_D \pi^{-1} \re^{-\theta}={16 \sqrt{\pi} \over \Gamma
    \left({1\over 4}\right)^2}\re^{-\theta} \ .
\end{equation}

Furthermore, the asymptotic behavior of the solution
$\epsilon(\theta)$ as $\theta \rightarrow \infty$ is of the form

\begin{equation}
  \epsilon(\theta)\sim  \pi \re^{\theta} + \sum_{n \ge 1} \epsilon^{(n)} \re^{(1-2n)\theta}, 
\end{equation}

whose coefficients are identified with the quantum corrections to the
dyon period

\begin{equation}
  \epsilon^{(n)} = \frac{1}{\pi^{2n-1}}(\Pi^{(0)}_D)^{2n-1} \Pi_D^{(n)}
  \ .
\end{equation}
 
It turns out that the equation \eqref{eq:cTBA-0} admits many possible
boundary conditions at $\theta \rightarrow -\infty$. This is in stark
contrast to the TBA equations for polynomial potentials studied in
\cite{oper, ims}, where the equations themselves fix the behavior of
the solutions at $\theta \rightarrow -\infty$. One possibility for the
boundary conditions at $\theta \rightarrow -\infty$ is the linear
behavior \eqref{zamobc}. This type of behavior was considered by
Zamolodchikov in \cite{post-zamo} but in a slightly different context,
as we will discuss in Sec. \ref{tssst} (see also
Appendix~\ref{appendixzamo}).  However, it can be seen that this is
not well suited for the quantum periods we are studying\footnote{In
  \cite{oper} it was also pointed out that \eqref{eq:cTBA-0} admits
  many boundary conditions at $\theta \rightarrow -\infty$.  However,
  it is claimed there that the correct boundary condition for the
  quantum period is precisely of the type \eqref{bcP}, namely,
  $\epsilon(\theta)\sim \theta/2+\ldots$ for $\theta\to-\infty$, which
  is not quite correct for the reasons explained here.}. One quick way
to see this is that the linear boundary condition with $P \not=0$
implies $\epsilon^{(1)}<-1/3$ (c.f. \eqref{fqc}), while from the
quantum Matone relation \eqref{eq:qMatone} we find

\begin{equation}
\label{matone-u0}
  \epsilon^{(1)} = \frac{1}{\pi}\Pi_D^{(0)}\Pi_D^{(1)} =
  \frac{1}{2\pi\ri}\(\Pi_A^{(0)}\Pi_B^{(1)} - \Pi_B^{(0)}\Pi_A^{(1)}\)
  = -\frac{1}{3}.
\end{equation}

It turns out that the appropriate boundary condition in this case is
given by

\begin{equation}\label{eq:bdy-cor}
  \epsilon(\theta)=-2 \log\left( -{2 \theta \over \pi} \right)
  +\cdots, \qquad \theta \to -\infty \ .
\end{equation}

This boundary condition for the TBA equation \eqref{eq:cTBA-0} was
also studied by Zamolodchikov in
\cite{zamo-reso}\footnote{Alternatively we can justify this boundary
  condition by using the results in section~\ref{tssst}, see equation
  \eqref{eps0}.}.  One can use a small modification of the
``dilogarithm trick" of \cite{zamo-TBA} to show that, with the
boundary condition (\ref{eq:bdy-cor}), one has indeed
(\ref{matone-u0}) (in the context of \cite{zamo-reso}, this
calculation gives the central charge $c=1$ for the corresponding
sinh-Gordon theory).

To implement numerically the boundary condition (\ref{eq:bdy-cor}), we
borrow a trick from \cite{post-zamo}. We define a continuous function

\begin{equation}
  f_1(\theta) = -2\log\left(1+\frac{2}{\pi}\log(1+\re^{-\theta})\right),
\end{equation}

 which has the same boundary behavior as
\eqref{eq:bdy-cor} and is exponentially suppressed when
$\theta \to +\infty$. We then look for a function $F_1(\theta)$ which
satisfies
\begin{equation}
  f_1(\theta) = \int_{\IR} K(\theta-\theta') F_1(\theta')\rd \theta' \
  ,\quad K(\theta) = \frac{1}{\pi\cosh(\theta)}\ .
\end{equation}
The generic solution to this linear integral equation  is

\begin{equation}
  F_1(\theta) = \frac{1}{2}\left(f_1\left(\theta+\ri\frac{\pi}{2}\right) +
  f_1 \left(\theta-\ri\frac{\pi}{2}\right)\right) \ .
\end{equation}

For our particular $f_1(\theta)$, we thus have

\begin{equation}
  F_1(\theta) =
  -\log\left(1+\frac{2}{\pi}\log(1+\ri\re^{-\theta})\right)
  -\log\left(1+\frac{2}{\pi}\log(1-\ri\re^{-\theta})\right)
  \ .
\end{equation}

This is a real function for $\theta\in\IR$. The TBA equation
\eqref{eq:cTBA-0} can then be written as
\begin{equation}\label{eq:TBA-SW2}
  \epsilon(\theta) = \pi \re^{\theta} + f_1(\theta) -
  \int_{\IR}\rd \theta'
  \frac{1}{\pi\cosh(\theta-\theta')}
  \(\log(1+\re^{-\epsilon(\theta')})+F_1(\theta')\) 
  \ ,
\end{equation}

where both boundary conditions at $\pm \infty$ are explicitly
spelt out.




The numerical solution to the
TBA equation \eqref{eq:cTBA-0} converges rather slowly, and we managed
to obtain 6 stabilised digits for $\hbar = 1$ and 7 stabilised digits
for $\hbar = 1/2$. These results, on the other hand, do agree with the
Borel resummation of the quantum dyon period. See Table~\ref{tb:TBA}.

\begin{table}
  \centering
  \begin{tabular}{cll}\toprule
    &$\hbar = 1$ & $\hbar = 1/2 $\\\midrule
    TBA & 6.62781 & 13.47880 \\    
    Borel sum & 6.62781917$\ldots$ & 13.47880936$\ldots$\\
    \bottomrule
  \end{tabular}
  \caption{Quantum dyon period at $u=0$.}\label{tb:TBA}
\end{table}











Let us now move away from the point $u=0$ but remain in
the strong coupling region with $u\in (-1,0)\cup(0,1)$. The TBA system
\eqref{eq:cTBA-1R} has two integral equations coupled to each
other. Nevertheless, at $\theta \to -\infty$ the first terms
$\propto \re^{\theta}$ on the r.h.s.\ of both equations in
\eqref{eq:cTBA-1R} are negligible, and the TBA system also collapses
to the single equation \eqref{eq:cTBA-0} (with the first term on the
r.h.s.\ suppressed). Therefore both
$\epsilon_d(\theta),\epsilon_m(\theta)$ should have the same boundary
condition as \eqref{eq:bdy-cor}, in other words
\begin{equation}
  \epsilon_d(\theta) \sim \epsilon_m(\theta) \sim
  -2\log\(-\frac{2\theta}{\pi}\) 
  +\ldots\ ,\quad \theta \to -\infty \ . 
\end{equation}
This is corroborated by the fact that the Matone relation
\eqref{matone-u0} can be reproduced with this boundary behavior by
using again a slight modification of the ``dilogarithm trick''
\cite{zamo-TBA}. We use again the trick of inserting the pair of
$f_1(\theta), F_1(\theta')$ functions, and we find that the numerical
solution to the TBA system \eqref{eq:cTBA-1R} has roughly the same
speed of convergence as the solution to \eqref{eq:cTBA-0} for
$u=0$. We tabulate the results for $u=1/3$ in
Tables~\ref{tb:dynu1o3},\ref{tb:monu1o3} and they also agree with the
Borel sum of the quantum periods. Note that the TBA system is solved
with $\theta \in \IR$, which in light of \eqref{eq:TBA-dict-1}
corresponds to real $\hbar$ for the quantum dyon period and to
imaginary $\hbar$ for the quantum monopole period.

\begin{table}
  \centering
  \begin{tabular}{c *{2}{>{$}l<{$}}}\toprule
    & \hbar = 1 & \hbar = 1/2 \\\midrule
    TBA & 9.16476 & 18.61486 \\
    Borel sum & 9.16476545\ldots & 18.61486738\ldots \\\bottomrule
  \end{tabular}
  \caption{Quantum dyon period at $u=1/3$.}
  \label{tb:dynu1o3}
\end{table}

\begin{table}
  \centering
  \begin{tabular}{c *{2}{>{$}l<{$}}}\toprule
    & \hbar = -\ri & \hbar = -\ri/2 \\\midrule
    TBA & 4.26480 & 8.716486 \\
    Borel sum & 4.26480153\ldots & 8.716486917\ldots \\\bottomrule
  \end{tabular}
  \caption{Quantum monopole period at $u=1/3$.}
  \label{tb:monu1o3}
\end{table}
