---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-007-24-twisted-torus
section_title: "Twisted torus"
section_number: 2.4
pages: 5-5
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.806
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
Let us again fix a lattice $\Gamma\isom \bZ^{\oplus n}$ equipped with a skew-symmetric form $\<-,-\>$.
The torus $\bT_+$ acts freely and transitively on the twisted torus $\bT_-$  via
\[(f\cdot g)(\gamma)=f(\gamma)\cdot g(\gamma)\in \bC^*, \quad f\in \bT_+, \quad  g\in \bT_-.\]
Choosing a base-point $g_0\in \bT_-$ therefore gives a bijection \begin{equation}
\label{bloxy}\theta_{g_0}\colon \bT_+\to \bT_-, \qquad f\mapsto f\cdot g_0.\end{equation}
We can use the identification $\theta_{g_0}$ to give $\bT_-$ the structure of an algebraic variety. The result is independent of the choice of base-point $g_0\in \bT_-$, since the translation maps on $\bT_+$ are algebraic.  
Similarly, the Poisson structure \eqref{poisson} on $\bT_+$  is invariant under translations, and hence can be transferred to $\bT_-$ via the map \eqref{bloxy}.

 

The co-ordinate ring of $\bT_-$ is spanned as a vector space by the functions
\[x_\gamma\colon \bT_-\to \bC^*, \qquad x_\gamma(g)=g(\gamma)\in \bC^*,\]
which we  refer to as twisted characters.  Thus
\begin{equation}\bC[\bT_-]=\bigoplus_{\gamma\in \Gamma} \bC\cdot x_\gamma, \qquad x_{\gamma_1}\cdot x_{\gamma_2}=(-1)^{\<\gamma_1,\gamma_2\>}\cdot x_{\gamma_1+\gamma_2}.\end{equation}

The Poisson bracket on $\bC[\bT_-]$ is given on twisted characters by 
 \begin{equation}
\label{poisson2}\{x_{\alpha}, x_{\beta}\}= \<\alpha,\beta\>\cdot x_{\alpha}\cdot x_{\beta}.\end{equation}
From now on we shall denote the twisted torus $\bT_-$ simply by $\bT$.
