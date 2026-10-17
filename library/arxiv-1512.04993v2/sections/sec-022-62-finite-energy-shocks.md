---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-022-62-finite-energy-shocks
section_title: "Finite energy shocks"
section_number: 6.2
pages: 36-38
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.986
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
In the limit studied in the last section, the time of the shock $|t_w|$ was taken to infinity, and the asymptotic energy of the shock (as compared to the mass of the black hole) $E/M$ was taken to zero, such that the quantity $h \sim e^{2\pi t_w / \beta} E/M$ was held fixed. This was to ensure that the precursor was a small perturbation and provided a simple relationship between the coordinates when crossing the shock. A relic of this limit was that the shock wave had to lie on the $u=0$ horizon. Additionally, the rate of complexity growth was always fixed at $2M$. If instead we inject finite energy into the system from the left boundary, we expect that the complexification rate should change accordingly.

Let us study precursors of finite energy $E/M$ and at finite $u$. An example of such a geometry is shown in Fig.~\ref{finite-complexity}.  The details of the construction of this geometry are left to Appendix~\ref{appendix-finite-time}. The picture for the state \eqref{eq:sinlge-precursors} is that of the perturbation emerging from the past singularity, materializing on the boundary at time $t_L=t_w$, and then traveling off into the future singularity. The past horizon shrinks by some amount after ejecting the perturbation, and the future horizon grows outward by a different amount after swallowing the perturbation. These are the analogs of the simple shifts usually considered in the infinite time shock wave geometries, see Appendix~\ref{appendix-finite-time}. Importantly, we think of the state \eqref{eq:sinlge-precursors} in the Schr\"{o}dinger picture. The perturbation is always present, and $t_w$ is simply a label that tells us when the perturbation materializes on the boundary.


 \begin{figure}
\begin{center}
\includegraphics[scale=.8]{finite-time-complexity-growth.pdf}
\caption{Complexity growth with finite time perturbation at $t_w = 0$ with finite energy $E$. The change in complexity is given by the purple shaded regions. The $t_L$ evolution will grow at rate $2(M+E)$, but $t_R$ evolution will grow at rate $2M$.}\label{finite-complexity}
\end{center}
\end{figure}

From the figure, it's clear that the increase in $t_R$ is solely in the region of spacetime with energy $M$. On the other hand, time evolution on the left boundary results in an addition to the Wheeler-DeWitt patch that is solely in the region of spacetime with energy $M+E$. Thus, we find
\be
\frac{d\CA}{dt_R} = 2M, \qquad \frac{d\CA}{dt_L} = 2(M+E), \label{eq:complexity-finite-time-shock}
\ee
which is appropriate since we injected energy $E$ into the left CFT. Even if we had looked at really early times $t_L, t_R \ll -\beta$ such that $\CW$ starts from the bottom of the Kruskal diagram, we would have still found the same rate of growth. This is indicative of the fact that the perturbation is always present in the left CFT. The energy is always $M+E$, and so the complexification rate should reflect that.
