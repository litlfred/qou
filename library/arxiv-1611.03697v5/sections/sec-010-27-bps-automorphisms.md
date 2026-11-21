---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-010-27-bps-automorphisms
section_title: "BPS automorphisms"
section_number: 2.7
pages: 7-8
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.908
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
\label{really}

As mentioned above, the main technical problem we have to deal with is making suitable definitions of the BPS automorphisms $\bS(\ell)$ associated to a BPS structure. Since we will use three different approaches at various points in the paper, it is perhaps worth briefly summarising  these here.

\begin{itemize}
\item[(i)] {\it Formal approach.}  If we are only interested in the elements $\bS(\ell)$ for rays $\ell\subset \bC^*$ lying in a fixed  acute sector $\Delta\subset \bC^*$, then we can work with a variant of the algebra $\bC[\bT]$ consisting of formal sums of the form \[\big.\sum_{Z(\gamma)\in \Delta} a_\gamma\cdot x_\gamma,\quad a_\gamma\in \bC,\] such that for any $H>0$ there are only finitely many terms with $|Z(\gamma)|<H$. This is the approach we shall use in Appendix \ref{two} to define variations of BPS structures: it has the advantage of not requiring any extra assumptions.\smallskip


\item[(ii)] {\it Analytic approach.} In Appendix \ref{converge},   we  associate to each convex sector $\Delta\subset \bC^*$, and each real number $R>0$, a non-empty analytic open subset $U_\Delta(R)\subset \bT$ defined to be the interior of the subset 
\[\big\{g\in \bT: Z(\gamma)\in \Delta \text{ and } \Omega(\gamma)\neq 0\implies |g(\gamma)|<\exp(-R\|\gamma\|)\big\}\subset \bT.\]
 We then show that if the BPS structure is convergent, and $R>0$ is sufficiently large, then  for any  active ray $\ell\subset \Delta$, the formal series $\DT(\ell)$ is absolutely convergent on   $U_\Delta(R)\subset \bT$, and that the time 1 Hamiltonian flow of the resulting  function defines a holomorphic  embedding \[\bS(\ell) \colon U_\Delta(R)\rightarrow \bT.\]
 We can then view this map as being a partially-defined automorphism of $\bT$. For a more precise statement see Proposition \ref{propy}.
\smallskip

\item[(iii)] {\it Birational approach.} In  the case of a generic, integral and ray-finite  BPS structure, the partially-defined automorphisms $\bS(\ell)$  discussed in (ii)  extend to birational automorphisms of $\bT$; see Propostion \ref{barneyy}. The induced pullback  of twisted characters is expressed by the formula
\begin{equation}\bS(\ell)^*(x_\beta)=x_\beta\cdot \prod_{Z(\gamma)\in \ell}(1-x_\gamma)^{\,\Omega(\gamma)\<\gamma,\beta\>}\end{equation}
which is often taken as a definition (see e.g. \cite[Section 2.2]{GMN1}). 
\end{itemize}
