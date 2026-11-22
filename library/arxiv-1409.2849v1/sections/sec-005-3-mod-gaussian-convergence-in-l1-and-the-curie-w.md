---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-005-3-mod-gaussian-convergence-in-l1-and-the-curie-w
section_title: "Mod-Gaussian convergence in L1 and the Curie-Weiss model"
section_number: 3
pages: 11-11
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
toc_source: outline
text_source: latex
latex_prose_ratio: 0.926
latex_coverage_ratio: 0.97
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
\label{sec:l1}

In this Section, $(X_n)_{n \in \N}$ is a sequence of random variables with entire moment generating series $\esper[\E^{zX_n}]$, and we assume the following:\vspace{2mm}
\begin{enumerate}[(A)]
\item One has mod-Gaussian convergence of the Laplace transforms, \emph{i.e.}, there is a sequence $t_n \to +\infty$ and a function $\psi$ continuous on $\R$ such that
$$\psi_n(t)=\esper[\E^{tX_n}]\,\E^{-\frac{t_n\,t^2}{2}}$$
converges locally uniformly on $\R$ to $\psi(t)$.\label{hyp:laplacemod}\vspace{1mm}
\item Each function $\psi_n$, and their limit $\psi$ are in $\mathrm{L}^1(\R)$.\label{hyp:l1mod}\vspace{1mm}
\end{enumerate}
We denote $\proba_n$ the law of $X_n$, 
\begin{equation}
\qproba_n[dx]=\frac{\E^{\frac{x^2}{2t_n}}}{\esper\!\left[\E^{\frac{(X_n)^2}{2t_n}}\right]}\,\,\proba_n[dx],\label{eq:exponchange}
\end{equation}
and $Y_n$ a random variable under the new law $\qproba_n$. Note that hypothesis \eqref{hyp:l1mod} implies that $Z_n=\esper[\E^{(X_n)^2/2t_n}]$ is finite for all $n \in \N$. Indeed,
$$
\int_{\R} \psi_n(t)\,dt = \esper\!\left[\int_{\R} \E^{t X_n-\frac{t_n \,t^2}{2}}\,dt\right]=\esper\!\left[\E^{\frac{(X_n)^2}{2t_n}}\,\left(\int_\R \E^{-\frac{(X_n-t_n t)^2}{2t_n}}\,dt\right)\right]=\sqrt{\frac{2\pi}{t_n}}\,\,\esper\!\left[\E^{\frac{(X_n)^2}{2t_n}}\right].
$$
Therefore the new probability measures $\qproba_n$ are well defined. The goal of this section is  to study the asymptotics of the new sequence $(Y_n)_{n \in \N}$. As we shall see in \S\ref{subsec:curieweiss}, the Curie-Weiss model defined by Equation \eqref{eq:curiemeasure} is one of the main examples in this framework. However, it is more convenient to look at the general problem, and we shall introduce later other models concerned by our general results.
\medskip
