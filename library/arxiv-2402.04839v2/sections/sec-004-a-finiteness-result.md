---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3-manifolds"
section_id: sec-004-a-finiteness-result
section_title: "A finiteness result"
section_number: null
pages: 5-6
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 1.0
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
According to J\o{}rgensen--Thurston theory \cite{thurston-notes,Gro81, Mai10}, for each positive real number $v$, there are at most finitely many hyperbolic 3--manifolds of volume $v.$ We show that the analogous result holds for topological volume.

\begin{proposition}\label{pro:finiteness}
For each positive real number $v$, there are at most finitely many closed, orientable 3--manifolds of topological volume $v.$
\end{proposition}

\begin{proof}
Suppose there are infinitely many closed 3--manifolds of topological volume $v$. Since only finitely many of them can be hyperbolic~\cite{thurston-notes}, this implies that there are infinitely many closed {\it non-hyperbolic} 3--manifolds $M_i$ of topological volume $v.$
In each $M_i$, choose a minimiser $L_i$. Then $\volh(M_i\setminus L_i) =v$, for each $i$, and hence there are only finitely many possibilities for $M_i\setminus L_i.$ For the rest of the proof suppose the cusped hyperbolic 3--manifold $M$ is a minimiser for infinitely many closed non-hyperbolic 3--manifolds $M_i$. In particular, for these manifolds, we have $M_i = M\big{(}\frac{p^i_1}{q^i_1}, \ldots, \frac{p^i_k}{q^i_k}\big{)}$. Since $M$ is a minimiser, leaving $k-1$ cusps unfilled and filling the $j$--th cusp with surgery coefficient $\frac{p^i_j}{q^i_j}$ gives a non-hyperbolic 3--manifold, since otherwise we would have a hyperbolic link complement of smaller volume than $v$ in $M_i.$ But only finitely many slopes $\frac{p^i_j}{q^i_j}$ on the $j$--th cusp may lead to a non-hyperbolic filling~\cite{thurston-notes}. Observing this for every cusp independently, we conclude that there are only finitely many possibilities for $M_i.$
\end{proof}
