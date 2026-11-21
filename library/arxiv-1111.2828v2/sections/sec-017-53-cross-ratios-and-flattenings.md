---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-017-53-cross-ratios-and-flattenings
section_title: "Cross-ratios and flattenings"
section_number: 5.3
pages: 17-18
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
toc_source: outline
text_source: latex
latex_prose_ratio: 0.87
latex_coverage_ratio: 0.941
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
\lbl{sub.ptolemyB}
For $x\in\C\backslash\{0\}$, let $\widetilde x=\log(x)$, where $\log$ is 
some fixed (set theoretic) section of the exponential map. 

Given a Ptolemy assignment $c$ on $\Delta^3_{n=2}$, we endow $\Delta^3_{n=2}$ with the shape of an ideal simplex with cross-ratio $z=\frac{c_{03}c_{12}}{c_{02}c_{13}}$ and a flattening 
\begin{equation}\lambda(c)=(\widetilde c_{03}+\widetilde c_{12}
-\widetilde c_{02}-\widetilde c_{13},\widetilde 
c_{01}+\widetilde c_{23}-\widetilde c_{02}-\widetilde c_{13})\in\widehat\Pre(\C).
\end{equation}


By Propositions~\ref{PtolemyProposition} and \ref{uniquePtolemyassignment}, a Ptolemy assignment on $\Delta^3_n$ induces a Ptolemy assignment $c_\alpha$ on each subsimplex $\Delta^3(\alpha)$. We thus have a map 
\begin{equation}\lbl{defoflambda}
\lambda\colon P_n(K)\to \widehat\Pre(\C),\qquad c\mapsto \sum_i\epsilon_i\sum_{\alpha\in \Delta^3_{n-2}(\Z)}\lambda(c_\alpha^i).
\end{equation}
Similarly, we have a map $P^\sigma_n(K)\to\widehat\Pre(\C)_{\PSL}$ defined by the same formula. We next prove that these maps have image in the respective extended Bloch groups. 

\begin{remark}
The shapes associated to a Ptolemy assignment satisfy equations resembling Thurston's gluing equations. This is studied in Garoufalidis-Goerner-Zickert~\cite{GaroufalidisGoernerZickert}.
\end{remark}
