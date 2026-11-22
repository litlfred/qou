---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-008-22-legendre-fenchel-transforms
section_title: "Legendre-Fenchel transforms"
section_number: 2.2
pages: 12-13
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.985
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
We now present the definition and some properties of the Legendre-Fenchel transform, a classical tool in large deviation theory (see \emph{e.g.} \cite[Section 2.2]{DZ98}) that we shall use a lot in this paper. The Legendre-Fenchel transform is the following operation on (convex) functions:
\begin{definition}
The Legendre-Fenchel transform of a function $\eta$ is defined by:
$$F(x)=\sup_{h \in \R}\,( hx-\eta(h)).$$
This is an involution on convex lower semi-continuous functions. 
\end{definition}\medskip

Assume that $\eta$ is the logarithm of the moment generating series of a random variable. In this case, $\eta$ is a convex function (by H\"older's inequality). Then $F$ is always non-negative, and the unique $h$ maximizing $hx-\eta(h)$, if it exists, is then defined by the implicit equation $\eta'(h)=x$ (note that $h$ depends on $x$, but we have chosen not to write $h(x)$ to make notation lighter). This implies the following useful identities:
$$ F(x)=xh-\eta(h)\qquad;\qquad F'(x)=h\qquad;\qquad F''(x)=h'(x)=\frac{1}{\eta''(h)}.$$
\begin{example} If $\eta(z)=mz+\frac{\sigma^{2}z^{2}}{2}$ (Gaussian variable with mean $m$ and variance $\sigma^{2}$), then 
$$h=\frac{x-m}{\sigma^{2}} \qquad;\qquad F_{\mathcal{N}_{\R}(m,\sigma^{2})}(x)=\frac{(x-m)^{2}}{2\sigma^{2}}$$
whereas if $\eta(z)=\lambda(\E^{z}-1)$ (Poisson law with parameter $\lambda$), then
$$h=\log\frac{x}{\lambda}\qquad;\qquad F_{\mathcal{P}(\lambda)}(x)=\begin{cases} x\log\frac{x}{\lambda}-(x-\lambda) & \text{if }x>0,\\
+ \infty & \text{otherwise}\end{cases}.$$
\begin{center}
\vspace{-3mm}
\begin{figure}[ht]
\includegraphics{LF.pdf}
\caption{The Legendre-Fenchel transforms of a Gaussian law and of a Poisson law.}
\end{figure}
\end{center}
\vspace{-5mm}
\end{example}
\bigskip
