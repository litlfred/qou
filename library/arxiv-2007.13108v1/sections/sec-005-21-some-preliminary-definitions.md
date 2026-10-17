---
doc_id: arxiv-2007.13108v1
doc_title: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-005-21-some-preliminary-definitions
section_title: "Some preliminary definitions"
section_number: 2.1
pages: 6-7
source_pdf: 2007.13108v1.pdf
source_sha256: b298478f5f5b948d
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.88
doc_brief: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube — It is well-known that measures whose density is the form e−V where V is a uniformly convex potential on Rn attain"
---
For a vector $w \in \RR^n$, define the \emph{tilt} of the measure $\nu$ as
$$
\frac{d \tau_{w} \nu(x)}{d \nu(x)} := Z_\nu(w)^{-1}  e^{\langle w, x \rangle} 
$$
where
$$
Z_\nu(w) := \int_{\DC} e^{\langle w, x \rangle} d \nu.
$$
Also define the functions
$$
a_\nu(w) := \int_{\DC} x d \tau_w \nu(x), ~~ A_\nu(w) := \int_{\DC} \left (x - a_\nu(w) \right )^{\otimes 2} d \tau_w \nu(x) = \COV(\tau_w \nu).
$$
A well-known calculation gives,
\begin{equation}\label{eq:momentgenerating}
a_\nu(w) = \nabla \mathcal{L} [\nu] (w), ~~ A_\nu(w) = \nabla^2 \mathcal{L} [\nu] (w)
\end{equation}
(this is the fact that the Log-Laplace transform is the cumulant-generating function). Thus, if $\nu$ is $\beta$-log-concave, we have
\begin{equation}\label{eq:nablaa}
\nabla a_\nu(w) = \nabla^2 \mathcal{L}[\nu] (w) \preceq \beta \Id.
\end{equation}
