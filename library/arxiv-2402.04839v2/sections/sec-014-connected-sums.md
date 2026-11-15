---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3-manifolds"
section_id: sec-014-connected-sums
section_title: "Connected sums"
section_number: null
pages: 16-17
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.927
latex_coverage_ratio: 0.788
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
\label{sec:connected_sum}

One natural question to ask is how topological volume behaves under connected sum. There is only one connected sum 
for which we can compute the topological volume exactly in \Cref{tab:complete}. Namely, we determine the topological volume
for $L(2,1) \# L(3,1)$ to be realised by $m010(-1, 1)$. Note that 
\begin{align*}
\volt(\; L(2,1) \# L(3,1) \; ) = \volh(m010) =& \volh(m009) \\
<&  \volh(m009) + \volh(m007) \\
=& \volt(\; L(2,1)\;) + \volt(\; L(3,1)\;).
\end{align*}
A surgery diagram of $m010$ that represents that manifold as the complement of a knot in $L(2,1) \# L(3,1)$ is shown in~\cref{fig:m010}.
\begin{question}
Let $M$ and $N$ be closed, orientable 3--manifolds. Is $\volt(\; M \# N \;) \le \volt(M)+\volt(N)$?
\end{question}

Note that Statement (1) in \Cref{cor:topinv} provides a similar, but weaker, result.

\begin{figure}[htb]
	\centering
	\includegraphics[width=6cm]{m010_new}
	\caption{The manifold $m010$ seen as a knot in $L(2,1) \# L(3,1)$ minimises the volume. }
	\label{fig:m010}
\end{figure}

\begin{question}
Let $M$ be a closed, orientable 3--manifold not diffeomorphic to $S^3$. What is the limit for $n\rightarrow \infty$ of
\begin{equation*}
    \frac{\volt(\#_n M)}{n\volt(M)} \; ?
\end{equation*}
\end{question}
