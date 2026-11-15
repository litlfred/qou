---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-014-41-the-fundamental-class-of-a-decorated-represen
section_title: "The fundamental class of a decorated representation"
section_number: 4.1
pages: 14-15
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
toc_source: outline
text_source: latex
latex_prose_ratio: 0.887
latex_coverage_ratio: 0.941
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
\lbl{sub.fundamental}

A flat $G$-bundle over $M$ determines a classifying map $M\to BG^\delta$, 
where the $\delta$ indicates that $G$ is regarded as a discrete group. It 
thus follows from Proposition~\ref{decorationeqreduction} that a decorated 
representation $\rho\colon\pi_1(M)\to G$ determines a map
\begin{equation}
B\rho\colon(M,\partial M)\to (BG^\delta,BH^\delta).
\end{equation}
In particular, $\rho$ gives rise to a fundamental class 
\begin{equation}
[\rho]=B\rho_*([M,\partial M])\in H_3(G,H),
\end{equation}
where, by definition, $H_*(G,H)=H_*(BG^\delta,BH^\delta)$. Note that the 
fundamental class is independent of the particular $3$-cycle structure 
on $K$.









Recall that $M$ is triangulated by truncated simplices. By 
restriction, a $(G,H)$ cocycle on $M$ determines a $(G,H)$-cocycle on each 
truncated simplex $\overline{\Delta_i}$. 
Let $\overline B_*(G,H)$ denote the chain complex generated in degree $n$ by 
$(G,H)$-cocycles on a truncated $n$-simplex. As proved in 
Zickert~\cite[Section~3]{ZickertDuke}, $\overline B_*(G,H)$ computes the 
homology groups $H_3(G,H)$. Note that a $(G,H)$-cocycle on $M$ determines (up to conjugation) a decorated $(G,H)$-representation.

\begin{proposition}
[{Zickert~\cite[Proposition~5.10]{ZickertDuke}}]
\lbl{fundclassrepprop} 
Let $\tau$ be a $(G,H)$-cocycle on $M$ representing a decorated $(G,H)$-representation $\rho$. The cycle
\begin{equation}\lbl{fundclassrep}
\sum\epsilon_i\tau_{\overline\Delta_i}\in \overline B_3(G,H),
\end{equation} 
represents the fundamental class of $\rho$.  \qed
\end{proposition}
