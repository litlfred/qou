---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-028-71-saddle-connections
section_title: "Saddle connections"
section_number: 7.1
pages: 42-43
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.848
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:saddle-connection}

The simplest possibility
has already appeared in Figure
\ref{fig:wnet-jump} above.  It involves two $\cS$-walls,
colliding along a two-way street $p$ running
between two branch points.  We call such a two-way street
a ``saddle connection,'' following the standard terminology for trajectories of quadratic differentials
(which is literally what we are considering here in the case $K=2$).

The two $\cS$-walls support charges $\bar a$ and $\bar b$, with natural lifts $a$, $b$, and we have
\begin{equation}
\mu^-(a) = 1, \qquad \mu^-(b) = 1,
\end{equation}
with all other $\mu^-(\cdot)$ vanishing.
In this case \eqref{eq:def-Q} reads
\begin{equation}
Q(p) = 1 + X_{\cl(a+b)}.
\end{equation}
If we let $\gamma = \cl(\bar a + \bar b)$, the preferred lift is $\tilde\gamma = \cl(a+b) + H$;
we thus have
\begin{equation}
 Q(p) = 1 - X_{\tilde\gamma}.
\end{equation}
This can indeed be decomposed according to \eqref{eq:Q-exp}, taking $\alpha_\gamma(p) = 1$, and
$\alpha_{n \gamma}(p) = 0$ for $n \neq 1$.
We thus obtain the simple result
\begin{equation}
 L(\gamma) = p_\Sigma
\end{equation}
and $L(n\gamma) = 0$ for $n \neq 1$.
As we have seen above, this result completely determines the wall-crossing
at this $\cK$-wall, through the formula \eqref{eq:k-def}.

In particular, we have $[L(\gamma)] = \gamma$, so the 4d BPS degeneracy is
\begin{equation}
 \Omega(\gamma) = 1.
\end{equation}
We have thus found that a saddle connection represents a BPS hypermultiplet.
This recovers a result of \cite{Klemm:1996bj,Gaiotto:2009hg} for the case $K=2$, and extends it to arbitrary $K$.
