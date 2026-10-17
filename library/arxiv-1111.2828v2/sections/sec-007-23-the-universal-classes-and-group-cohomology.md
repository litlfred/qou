---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-007-23-the-universal-classes-and-group-cohomology
section_title: "The universal classes and group cohomology"
section_number: 2.3
pages: 10-11
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
toc_source: outline
text_source: latex
latex_prose_ratio: 0.854
latex_coverage_ratio: 0.909
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
\lbl{sub.universal}

The Cheeger-Chern-Simons classes are also defined for the universal flat bundle $EG^\delta\to BG^\delta$. For an explicit construction, we refer to Dupont-Kamber~\cite{DupontKamber} or Dupont-Hain-Zucker~\cite{DupontHainZucker}.
In particular, we have a class $\widehat c\in H^3(BG^\delta;\C/4\pi^2\Z)$. 
If $\rho\colon \pi_1(M)\to G$ is a representation, with classifying map $B\rho\colon M\to BG^\delta$, we thus have

\begin{equation}
\widehat c(B\rho_*([M]))=i\Vol_\C(\rho).
\end{equation}

It is well known that the homology of $BG^\delta$ is the homology of the chain complex $C_*\otimes_{\Z[G]}\Z$, where $C_*$ is any free $\Z[G]$-resolution of $\Z$. A convenient choice of free resolution is the complex $C_*$, generated in degree $n$ by tuples $(g_0,\dots, g_n)$, and with boundary map given by 
\begin{equation}
\partial (g_0,\dots,g_n)=\sum (-1)^i (g_0,\dots,\widehat g_i,\dots,g_n).
\end{equation} 

The homology of $C_*\otimes_{\Z[G]}\Z$ is denoted $H_*(G)$, so $H_*(G)=H_*(BG^\delta)$. Theorem~\ref{cocycleintro} gives a concrete cocycle formula for $\widehat c\colon H_3(\SL(n,\C))\to \C/4\pi^2\Z$.
