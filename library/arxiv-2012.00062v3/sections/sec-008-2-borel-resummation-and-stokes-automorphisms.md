---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-008-2-borel-resummation-and-stokes-automorphisms
section_title: "Borel resummation and Stokes automorphisms"
section_number: 2
pages: 9-10
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.884
latex_coverage_ratio: 0.967
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
\label{sec.borel}


\subsection{Borel resummation}
\label{sub.borel}


In this section we briefly review the process of Borel resummation of
a factorially divergent series, its Laplace integral along rays and
the corresponding Stokes automorphism across a Stokes ray. The
material in this section is classical and well-known and is explained
in detail in the books~\cite{Costin:asymptotics,Miller:applied,msauzin},
and in the references therein. We will be following the physics convention
of Borel resummation as found for example in~\cite[Sec. 3.2]{mmbook}
and~\cite[Sec.42.5]{Zinn-Zustin:QFT}, which differs by a factor of
$\tau$ from the Borel resummation found in the math literature.

Borel resummation is a 2-step process to pass from a factorially
divergent series $F(\tau)$ to the analytic function $s(F)(\tau)$
defined in the right half-plane $\Re(\tau)>0$ summarized in the
following diagram
\begin{equation}
  \label{borel-sum}
  F(\tau) \leadsto 
  \wh{F}(\zeta) \leadsto 
  s(F)(\tau) \,.
\end{equation}
Here one starts with a Gevrey-1 a formal power series $F(\tau)$
\begin{equation}
  F(\tau) = \sum_{n=0}^\infty f_n \tau^{n} ,\quad f_n = O(C^n \, n!)
\end{equation}
and defines its Borel stransform $\wh{F}(\zeta)$ by
\begin{equation}
  \wh{F}(\zeta) = \sum_{n=0}^\infty \frac{f_n}{n!} \zeta^n \,.
\end{equation}
It follows that $\wh{F}$ is the germ of an analytic function at
$\zeta=0$. If it analytically continues to an $L^1$-analytic function
along the ray $\rho_\theta:=\re^{\ri\theta}\IR_+$ where
$\theta = \arg \tau$, we define its Laplace transform by 
\begin{equation}
  s_{\theta}(F)(\tau)=
  \int_0^\infty \wh{F}(\tau\zeta) \re^{-\zeta} \rd \zeta=
  \frac{1}{\tau} \int_{\rho_\theta}
  \wh{F}(\zeta)\re^{-\zeta/\tau} \rd \zeta
  \label{eq:brlsum}
\end{equation}






The function $s(F)(\tau)$ is often called the Borel resummation of the
formal power series $F$, and we often suppress the subscript $\theta=0$
when $\tau$ is real and positive.













If we vary $\theta = \arg \tau$ and we do not encounter singularities
of $\wh{F}$, the function $s_\th(F)(\tau)$ is locally analytic. Thus,
the problem is to understand the analytic continuation of $\wh{F}$ and
to analyze what happens to the Borel resummation $s_\theta(F)(\tau)$
when $\theta =\arg(\tau)$ crosses a Stokes ray, i.e., a ray in Borel
plane that contains one or more singularities of $\wh{F}$. This is
described by a Stokes automorphism.
