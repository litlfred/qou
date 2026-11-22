---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3-manifolds"
section_id: sec-016-volume-functions-on-dehn-surgery-space
section_title: "Volume functions on Dehn surgery space"
section_number: null
pages: 18-19
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.945
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
\label{sec:dehnsurgeryspace}

Hodgson and Masai~\cite[\S 2]{Hodgson_Masai} give an excellent exposition of results of Neumann and Zagier~\cite{Neumann-volumes-1985} relating the decrease in volume during hyperbolic Dehn filling to the length of the surgery slope. Moreover, they analyse the corresponding functions for $P$ and $W$ in ~\cite[\S 4-5]{Hodgson_Masai}. We only state the main results required here and refer the reader to~\cite{Hodgson_Masai}  for a justification and further details.

For a cusped hyperbolic 3--manifold $M,$ let $\Delta \vol_M (p,q) = \volh(M) - \volh(M(p,q)),$ where it is understood that a fixed cusp of $M$ is filled.

We note that $(p,q)$--surgery on the first cusp of $M \in \{ P, W\}$ for $p^2+q^2$ sufficiently large gives a one-cusped hyperbolic 3--manifold $M((p,q), \infty)$. Since $M((p,q),(1,0)) \cong L(p,q),$ this gives $\volt(L(p,q)) \le \volh M((p,q), \infty)$ (note that other filling slopes may result in a homeomorphic lens space, which must be addressed in the proof of \Cref{prop:lens-space-limit}). Since $P$ and $W$ are of equal volume, we have
\[
\volh P((p,q),\infty)) - \volh W((p,q),\infty)) = \Delta \vol_W (p,q) - \Delta \vol_P (p,q).
\]

With respect to the Seifert framing on component $0$ on $W$, 
\cite[(5.14)]{Hodgson_Masai} gives:
\begin{align}
\Delta \vol_W (p,q) = 
\frac{2 \pi^2}{p^2 + 4 p q + 8 q^2}
& - \frac{\pi^4 (p^2 - 8 q^2) (p^2 + 8 p q + 8 q^2)}{3 (p^2 + 4 p q + 8 q^2)^4}\nonumber \\
&+O\Bigg( \frac{1}{(p^2 + 4 p q + 8 q^2)^3}\Bigg).\label{eq:DvolW}
\end{align}

With respect to the Seifert framing on component $0$ on $P$, \cite[(5.11)]{Hodgson_Masai} gives:
\begin{align}
\Delta \vol_P (p,q) = 
\frac{\pi^2}{(p - 4 q)^2 + (p - 3 q)^2}
&+
\frac{\pi^4 (4 p^4 - 80 p^3 q + 540 p^2 q^2 - 1520 p q^3 + 1535 q^4)}{24 ((p - 4 q)^2 + (p - 3 q)^2)^4}\nonumber \\
&+ 
O\Bigg( \frac{1}{((p - 4 q)^2 + (p - 3 q)^2)^3}\Bigg).\label{eq:DvolP}
\end{align}
