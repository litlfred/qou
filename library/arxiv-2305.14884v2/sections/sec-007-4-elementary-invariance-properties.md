---
doc_id: arxiv-2305.14884v2
doc_title: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS"
section_id: sec-007-4-elementary-invariance-properties
section_title: "Elementary invariance properties"
section_number: 4
pages: 18-19
source_pdf: 2305.14884v2.pdf
source_sha256: ebc8e64d901c9e4f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.933
---
\label{sec.elementary}

In this section, we review some basic choices needed to define the
the Neumann--Zagier data for a triangulation with $N$ tetrahedra, namely:
\begin{itemize}
\item[(a)] an ordering of the $N$ tetrahedra,
\item[(b)] an ordering of the $N$ edges,
\item[(c)] an edge equation to remove,   
\item[(d)] a path to represent the meridian curve,
\item[(e)] a flattening.
\end{itemize}
A change of these choices changes the corresponding Neumann--Zagier data in a simple
way, which we now describe. Fix a triangulation and the choices needed to define
Neumann--Zagier data
\be
\Xi\=(A,B,\nu,z,f,f'')\,.
\ee
Regarding choice (a), suppose that $\sigma\in S_{N}$ is a permutation (and also the
associated matrix) of our labelling of the tetrahedra. Then the Neumann--Zagier
matrices transform as follows
\be
  \Xi\=(A,B,\nu,z,f,f'')
  \mapsto
  (A\sigma,B\sigma,\nu,\sigma^{-1} z,\sigma^{-1} f,\sigma^{-1} f'')
  \=\Xi\cdot\sigma \,.
\ee
This implies that the integrand $f^\Xi_\hbar(x,z)$ of Equation~\eqref{integrand}
and the quadratic form $\Lambda$ of Equation~\eqref{lambda} satisfy
\be
f_{\Xi\cdot\sigma,\hbar}(\sigma^{-1} x,\sigma^{-1} z) \= f^\Xi_\hbar(x,z)
\qquad
\Lambda^{\Xi\cdot\sigma} \= \sigma^t \Lambda^\Xi \sigma\,,
\ee
which combined with the fact that integration is invariant under a linear change
of variables (see part (a) of Lemma~\ref{lem.ff1}), implies that
$\Phi^{\Xi\cdot\sigma}(\hbar)=\Phi^\Xi(\hbar)$.  

Choices (b), (c) and (d) are a special case of the following transformation of
$P\in\GL_{N}(\BZ)$ acting on Neumann--Zagier data via
\be
\Xi\=(A,B,\nu,z,f,f'') \mapsto (PA,PB,P\nu,z,f,f'') \=P\cdot\Xi\,.
\ee
It follows that the integrand and the quadratic form satisfy 
\be
f^{P\cdot\Xi}_\hbar(x,z) \= f^\Xi_\hbar(x,z), \qquad
\Lambda^{P \cdot\Xi} \= \Lambda^\Xi \,,
\ee
which implies again that $\Phi^{\Xi\cdot\sigma}(\hbar)=\Phi^\Xi(\hbar)$.

Finally, if $\Xi$ and $\widetilde\Xi$ differ by a choice of flattening, then
it is easy to see that
\be
f^{\widetilde\Xi}_\hbar(x,z) \= e^{c\hbar} f^\Xi_\hbar(x,z), \qquad
\Lambda^{\widetilde\Xi} \= \Lambda^\Xi 
\ee
for some $c \in \frac{1}{8}\BZ$, which implies that
$\Phi^{\widetilde\Xi}(\hbar)=e^{c \hbar}\, \Phi^\Xi(\hbar)$.
