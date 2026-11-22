---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-014-31-the-riemann-hilbert-problem
section_title: "The Riemann-Hilbert problem"
section_number: 3.1
pages: 9-10
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
\label{rh_intro}

Given a convergent BPS structure $(\Gamma,Z,\Omega)$ we will 
 consider an associated Riemann-Hilbert problem. It depends on a choice of a point $\xi\in \bT$ which we call the constant term.  We discuss the statement of this problem more carefully in Section \ref{rh}; for now we just give the rough idea.
 
\begin{problem}
\label{an}Fix a point $\xi\in \bT$.
Construct a piecewise holomorphic map
\[\Phi\colon \bC^*\to \bT\]
with the following three properties:
\begin{itemize}
\item[(a)] As $t\in \bC^*$ crosses an active ray $\ell\subset \bC^*$ in the clockwise direction, the function $\Phi(t)$ undergoes a discontinuous  jump described  by the formula
\[\Phi(t)\mapsto \bS(\ell)(\Phi(t)) .\]

\item[(b)] As $t\to 0$ one has $\exp(Z/t)\cdot \Phi(t)\to \xi$.\smallskip

\item[(c)] As $t\to \infty$ the element $\Phi(t)$ has at most polynomial growth.
\end{itemize}

\end{problem}

 The gist of condition (a) is that the function $\Phi$ should be holomorphic in the complement of the active rays, and for each active ray $\ell \subset \bC^*$ the analytic continuations of the two functions on either side  should differ by composition with the corresponding automorphism $\bS(\ell)$. 
 
 To make sense of (b), note that \[\exp(Z/t)\colon \Gamma\to \bC^*\] is an element of the  torus $\bT_+$, and    recall that $\bT=\bT_-$ is a torsor for $\bT_+$. We often write \begin{equation}\exp(Z/t)\cdot \Phi(t)=\Psi(t)\cdot \xi,\end{equation}
which then defines a map $\Psi\colon \bC^*\to \bT_+.$
Clearly the maps $\Phi$ and $\Psi$ are equivalent data; we use whichever is most convenient.

Composing with the (twisted) characters of $\bT_\pm$, we can alternatively encode the solution  in  either of the  two systems of maps
\[\Phi_\gamma
=x_\gamma\circ \Phi\colon \bC^*\to \bC^*, \qquad \Psi_\gamma=y_\gamma\circ \Psi\colon \bC^*\to \bC^*.\]
Condition (c) is then the statement that for each $\gamma\in \Gamma$ there should exist $k>0$ such that
\[|t|^{-k}<|\Phi_\gamma(t)|<|t|^k, \qquad |t|\gg 0.\]

Problem \ref{an} is closely analogous to the Riemann-Hilbert problems which arise in the study of differential equations with irregular singularities. In that case  the Stokes factors $\bS(\ell)$ lie in a finite-dimensional group $\GL_n(\bC)$, whereas in our situation  they are elements of the  infinite-dimensional group of Poisson automorphisms of the torus $\bT$. We will return to this analogy in the sequel to this paper \cite{Br3}.
