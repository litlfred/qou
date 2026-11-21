---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-026-44-symmetries-of-the-problem
section_title: "Symmetries of the problem"
section_number: 4.4
pages: 19-20
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
\label{sym}
There are a couple of obvious symmetries of the Riemann-Hilbert problem which deserve further comment.
For the first, note that the twisted torus $\bT$ has a canonical involution $\sigma\colon \bT\to \bT$  which acts on twisted characters by $\sigma^*(x_\gamma)=x_{-\gamma}$.  The fixed point set  is the finite subset
\begin{equation}\label{quadref}\bT^\sigma=\{g\colon \Gamma \to \{\pm 1\}: g(\gamma_1+\gamma_2)=(-1)^{\<\gamma_1,\gamma_2\>} g(\gamma_1)\cdot g(\gamma_2)\}\subset \bT,\end{equation}
whose elements are 
quadratic refinements of the form $\<-,-\>$. 

The symmetry property $\Omega(-\gamma)=\Omega(\gamma)$ of the BPS invariants implies that 
\[\bS(-\ell)\circ \sigma =\sigma\circ \bS(\ell).\]
 It follows that  given a collection of functions  $\Phi^{\xi}_\rr(t)$ solving the Riemann-Hilbert problem for the constant term $\xi$, we can generate another solution, this time for the constant term $\sigma(\xi)$, by defining \[{\Phi}^{\sigma(\xi)}_{\rr}(t)=\sigma\circ \Phi^\xi_{-\rr}(-t).\]
 In particular,  if we had uniqueness of solutions, we could  conclude that  whenever $\xi\in \bT^\sigma$ is a quadratic refinement of the form $\<-,-\>$, any solution to the  Riemann-Hilbert problem satisfies
 \[\Phi^\xi_{\rr,\gamma}(t)= \Phi^\xi_{-\rr,-\gamma}(-t).\]
 
 For the second symmetry of the Riemann-Hilbert problem, note that given a BPS structure $(\Gamma,Z,\Omega)$, we can obtain a new BPS structure $(\Gamma,\lambda Z,\Omega)$ by simply multiplying the central charges $Z(\gamma)\in \bC$ by a fixed scalar $\lambda\in \bC^*$. It is then clear that if $\Phi_\rr(t)$ is a system of solutions to the Riemann-Hilbert problem  for the BPS structure $(\Gamma,Z,\Omega)$, then the functions $\Phi_{\lambda\rr}(\lambda t)$ will be a system of solutions to the problem for $(\Gamma,\lambda Z,\Omega)$ with the same constant term. Again, if we had uniqueness of solutions, we could conclude that all solutions to Problem \ref{dtsect} are invariant under simultaneous rescaling of $Z$ and $t$.
