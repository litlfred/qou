---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-016-33-variations-of-bps-structure
section_title: "Variations of BPS structure"
section_number: 3.3
pages: 11-12
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.992
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
\label{vbpss}

The variation of BPS invariants in Donaldson-Thomas theory under changes in stability parameters is controlled by the Kontsevich-Soibelman wall-crossing formula. This forms the main ingredient in the following  definition of a variation of BPS structures, which is a special case of the  notion of a continuous family of stability structures  from \cite[Section 2.3]{KS1}.
Full details can be found in Appendix \ref{two}; here we just give the rough idea.



\begin{defn}
\label{co}
A variation of BPS structure over a complex manifold $M$ consists of a collection of BPS structures $(\Gamma_p,Z_p,\Omega_p)$ indexed by the points  $p\in M$, such that

\begin{itemize}
\item[(a)] The charge lattices  $\Gamma_p$ form a local system of abelian groups, and the intersection forms $\<-,-\>_p$ are covariantly  constant.\smallskip

\item[(b)] Given a covariantly constant family of elements $\gamma_p\in \Gamma_p$, the central charges $Z_p(\gamma_p)\in \bC$ are holomorphic functions of $p\in M$.\smallskip

\item[(c)] The constant in the support property \eqref{support} can be chosen uniformly on compact subsets.\smallskip

\item[(d)] For each acute sector $\Delta\subset \bC^*$, the anti-clockwise product over active rays in $\Delta$\begin{equation}\label{wcw} \bS_p(\Delta)=\prod_{\ell\subset \Delta} \bS_p(\ell) \in \Aut(\bT_p),\end{equation}
is covariantly constant as $p\in M$ varies, providing the boundary rays of $\Delta$ are never active.
\end{itemize}
\end{defn}


Note that the local system in (a) induces a flat Ehresmann connection on the bundle of tori \[(\bT_+)_p=\Hom_\bZ(\Gamma_p,\bC^*),\]
 over the manifold $M$, and hence also on the associated bundle of twisted tori $\bT_p$.
It will require some work to make rigorous sense of the wall-crossing formula, condition (d). We do this using formal completions in Appendix \ref{two} following  \cite{KS1}. This needs no convergence assumptions and completely describes the behaviour of the BPS invariants as the point $p\in M$ varies: knowing all the  invariants $\Omega(\gamma)$ at some point of $M$ determines them at all other points.

The material of Section \ref{newnew} gives interesting examples of variations of BPS structures. For a fixed $k\geq 1$ the corresponding BPS structure $(\Gamma,Z,\Omega)$ is determined by the pair \[(Z(e_1), Z(e_2))\in \mathfrak{h}^2,\] where $\mathfrak{h}$ denotes the upper half-plane.  As this point varies we obtain a variation of BPS structures. In particular, the BPS invariants for $\nu<0$ are completely determined by the trivial case $\nu>0$ and the wall-crossing formula \eqref{wcw}.
