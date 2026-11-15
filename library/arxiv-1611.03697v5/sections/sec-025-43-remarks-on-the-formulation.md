---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-025-43-remarks-on-the-formulation
section_title: "Remarks on the formulation"
section_number: 4.3
pages: 18-19
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.995
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
The Riemann-Hilbert problem of the last subsection is the main subject of this paper.  Unfortunately we have no general results giving existence or uniqueness of its solutions. Moreover one could easily imagine various small perturbations of the statement of Problem \ref{dtsect}, and it will require further work to decide for sure exactly what the correct conditions should be. We make a few remarks on this here.

\begin{remarks}
\label{oh}
\begin{itemize}
\item[(i)] From a heuristic point-of-view it is useful to consider a Riemann-Hilbert problem involving maps from $\bC^*$ into the group $G$ of Poisson automorphisms of the torus $\bT$. The  above formulation is obtained by evaluating a $t$-dependent automorphism of $\bT$ at the chosen point $\xi\in \bT$. If we  replace the infinite-dimensional group $G$ with the finite-dimensional group $\GL_n(\bC)$ the analogous Riemann-Hilbert problems are familiar in the theory of linear differential equations with irregular singularities, and play an important r{o}le in the theory of Frobenius manifolds  \cite[Lecture 4]{D}. This connection between stability conditions and Stokes phenomena goes back to \cite{BTL}, and will be revisited in \cite{Br3}. In fact, with our conventions, the Riemann-Hilbert problem is most naturally viewed as taking values in the opposite group $G^{\operatorname{op}}$, which we can view heuristically  as the group of automorphisms of the Poisson algebra $\bC[\bT]$. This is why the compositions in \eqref{wcw} are in the anti-clockwise order, and why the Stokes data acts on the left in (RH1).\smallskip


\item[(ii)] 
In Section \ref{rh_intro} we gave a simplified formulation of the Riemann-Hilbert problem  which  considers a single function $\Phi\colon \bC^*\to \bT$ with prescribed discontinuities along active rays.  This  becomes a little tricky to make sense of when the active rays are dense in regions of $\bC^*$, so we prefer the formulation given in Problem \ref{dtsect}, which is modelled on the standard approach in the finite-dimensional case.
We can obtain a solution to Problem \ref{an} from a solution to Problem \ref{dtsect} by defining $\Phi(t)=\Phi_{\bR_{>0}\cdot t} (t)$; Remark \ref{whoopsy} shows that this defines  a holomorphic function  away from the closure of the union of the active rays. Note that Problem \ref{dtsect}  imposes strictly stronger conditions on the resulting function $\Phi(t)$, because  the conditions (RH2) and (RH3) are assumed to hold in half-planes. 
\smallskip

\item[(iii)]We can weaken the conditions in Problem \ref{dtsect} in various ways, and until we have studied more examples in detail it is not possible to be sure exactly what is the correct formulation. For example, we could allow the functions $\Phi_{\rr,\gamma}(t)$ to have poles on the half-plane $\bH_\rr$, or we could replace $\bH_\rr$ by a smaller convex sector of some fixed angle.  We can also consider a variant of Problem \ref{dtsect} where we only assume that the map $\Phi_\rr$ is defined and holomorphic on the intersection of $\bH_\rr$ with some punctured disc $\{t\in \bC^*:|t|<r\}$, and drop condition (RH3) altogether. We shall refer to this last version as the  weak Riemann-Hilbert problem associated to the BPS structure. 
\end{itemize}
\end{remarks}
