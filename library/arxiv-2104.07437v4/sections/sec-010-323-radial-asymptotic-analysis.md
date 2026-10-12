---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-010-323-radial-asymptotic-analysis
section_title: "Radial asymptotic analysis"
section_number: 3.2.3
pages: 24-25
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.992
---
One of the important lessons we learned from \cite{ggm1,ggm2} is that
it is often helpful to study the asymptotic behavior of the
anti-holomorphic blocks\footnote{In \cite{ggm1,ggm2} one studies the asymptotics of
  holomorphic blocks in the opposite limit $\bb^2\rightarrow 0$, which corresponds to the semiclassical regime.} in the limit
$g_s \propto -\bb^{-2} \rightarrow 0$ along a ray
$\re^{\ri\theta}\IR_+$, which depends crucially on the angle $\theta$.
Oftentimes, it is possible to promote these radial asymptotic behavior
of anti-holomorphic blocks to exact representations of them in terms
of the Borel resummation of the asymptotic series $\Phi_\sigma(g_s)$,
together with non-perturbative corrections parametrised by $q$-series.
This turns out to be an extremely powerful method to compute the
Stokes automorphism of the asymptotic series $\Phi_\sigma(g_s)$.

In the case of the anti-holomorphic blocks
$\tilde{g}(\tq),\tilde{G}(\tq)$ uncovered from evaluating the first
trace of local $\IF_0$, we find that they can be expressed in terms of
Borel resummations of $\Phi(g_s)$ in the following way
\begin{equation}
  \begin{pmatrix}
    \frac{1}{\sqrt{\pi g_s}} \tilde{g}(\tq)\\
    -8\sqrt{\pi g_s} \tilde{G}(\tq)
  \end{pmatrix}
  = 2^{-3/2} M_R(q) s_R(\Phi)(g_s),
  \label{eq:rasymp-Z1F0}
\end{equation}

where $M_R(q)$ is a $2\times 2$ matrix of $q$-series that encodes
non-perturbative corrections.  We parametrise it by
\begin{equation}
  M_R(q) =
  \begin{pmatrix}
    g_+^R(q) & -g_-^R(q)\\
    G_+^R(q) & G_-^R(q)
  \end{pmatrix}.
\end{equation}
Note that it depends on the sector $R$.  We will focus on the two
sectors $I,II$, as shown in Fig.~\ref{fg:rays-Z1F0}.

When $g_s$ is in the sector $I$, we find that
\begin{subequations}
  \begin{align}
    &g_+^I(q) = 1+q^{1/2} - q + 2q^{3/2}- 2q^2 + \ldots,\\
    &G_+^I(q) = 1+5q^{1/2} - q + 10q^{3/2}- 2q^2 + \ldots,\\
    &g_-^I(q) = 1+3q^{1/2} - 2q + 3q^{3/2} +\ldots,\\
    &G_-^I(q) = 1-9q^{1/2} - 2q - 9q^{3/2} +\ldots.
  \end{align}
\end{subequations}
it is easy to identify that
\begin{equation}
  g_+^I(q) = g_0(q),\quad G_+^I(q) = G_0(q),
  \label{eq:gG}
\end{equation}
and we will denote them by $g(q), G(q)$.
In addition, these four $q$-series satisfy the ``Wronskian''-like
identity
\begin{equation}
  g_+^I(q) G_-^I(q) + G_+^I(q)g_-^I (q) = 2.
\end{equation}
With the help of \eqref{eq:W-id}, we are able to identify
\begin{subequations}
  \begin{align}
    &g_-^I(q) = -\frac{1-q^{1/2}}{q^{1/4}}g_1(q) + 2 g_0(q),
    \label{eq:gprime}\\
    &G_-^I(q) = \frac{1-q^{1/2}}{2q^{1/4}}(G_1(q)+H_1(q)) - 2 G_0(q), 
      \label{eq:Gprime}
  \end{align}
\end{subequations}

which we will denote by $g'(q), G'(q)$.
Similarly in sector $II$, we find in fact

\begin{gather}
  g_-^{II}(q) = g(q),\quad G_-^{II}(q) = G(q),\nn
  g_+^{II}(q) = g'(q),\quad G_+^{II}(q) = G'(q).
\end{gather}

Once $M_{I,II}(q)$ are known, the Stokes automorphism
$\mf{S}_{I\mapsto II}(q)$ can be computed by
\begin{equation}
  \mf{S}_{I\mapsto II}(q) = M_{II}(q)^{-1} M_I(q), 
\end{equation}
which yields \eqref{eq:Sp-F0}. 

This calculation illustrates that the additional analytic structures provided by the TS/ST correspondence makes it possible 
to calculate the Stokes constants associated to the series $\Phi_{0,1}(g_s)$ and to express it in closed form, in terms of the $q$-series appearing 
in the factorization of the spectral trace (\ref{eq:W-id}) and their descendants (\ref{ABdescendants}). 

 We close this subsection by commenting that the radial
asymptotic formula \eqref{eq:rasymp-Z1F0} together with the
factorisation formula \eqref{eq:Z1fac0-F0} allows us to express the
trace in terms of Borel sum of asymptotic series:
\begin{itemize}
\item When $g_s$ is in sector $I$
  \begin{equation}
    \tr\rho_{\IF_0} = -\frac{\ri\sqrt{\pi g_s}}{2^{3/2}}
    \left(g(q)G(q)s_I(\Phi_{0})(g_s)
      +\frac{1}{2}(g(q)G'(q)-G(q)g'(q))s_I(\Phi_{1})(g_s)\right).
  \end{equation}
  Note that here $\Phi_0(g_s)$ is the dominant series.
\item When $g_s$ is in sector $II$
  \begin{equation}
    \tr\rho_{\IF_0} = -\frac{\ri\sqrt{\pi g_s}}{2^{3/2}} s_{II}(\Phi_{0})(g_s).
  \end{equation}
\end{itemize}
In both sectors in the leading order we have
\begin{equation}
  Z_1(\hbar) = \tr\rho_{\IF_0}\sim
  -\frac{\ri\sqrt{\pi g_s}}{2^{3/2}} \Phi_0(g_s),\quad |g_s|\ll 1,
\end{equation}
which is consistent with the prediction \eqref{zn-ae} from the TS/ST
correspondence.
