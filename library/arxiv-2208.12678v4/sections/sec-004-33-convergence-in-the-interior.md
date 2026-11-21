---
doc_id: arxiv-2208.12678v4
doc_title: "STATIONARY CURVES UNDER THE MÖBIUS-PLATEAU ENERGY"
section_id: sec-004-33-convergence-in-the-interior
section_title: "Convergence in the Interior"
section_number: 3.3
pages: 5-6
source_pdf: 2208.12678v4.pdf
source_sha256: 406d36ff4968091d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.909
latex_coverage_ratio: 0.942
doc_brief: "STATIONARY CURVES UNDER THE MÖBIUS-PLATEAU ENERGY — Plateau problems with elastic boundary energies have been of recent theoretical and applied interest."
---
Since $\mathrm{e}(u_k)$ is uniformly bounded, we have from compactness that after passing to a subsequence, $u_k\rightharpoonup u_*$ weakly in $W^{1,2}(D,\RR^3)$ for some $u_*$, not necessarily equal to $u_\infty$, and 
\begin{align*}
    \mathrm{e}(u_*)\leq\liminf_{j \to \infty}\mathrm{e}(u_j).
\end{align*}
Furthermore, from Proposition~\ref{prop:equicontinuity}, $\{u_j\}$ is equicontinuous on $\partial D$ and by Arzela-Ascoli, a subsequence $\{u_j\}$ (not relabelled) converges uniformly on $\partial D$. Since each $u_j$ is harmonic, we have from the maximum principle that 
\begin{align*}
    \sup_D\abs{u_j-u_k}=\max_{\partial D}\abs{u_j-u_k}.
\end{align*}
Thus $\{u_j\}$ converges uniformly on $\bar{D}$ to $u_*$. Moreover, uniform convergence implies that $u_*:\partial D\rightarrow\gamma_\infty$ is monotone and onto, so therefore $u_*\in \mathcal{D}_{\gamma_\infty}$. We thus obtain the desired inequality,
\begin{align*}
    \mathrm{e}(u_\infty)=\inf_{u\in\mathcal{D}_{\gamma_\infty}}\mathrm{e}(u)\leq\mathrm{e}(u_*)\leq\liminf\limits_{j \to \infty}\mathrm{e}(u_j).
\end{align*}

With this, we have established the lower semicontinuity of $E$, and $\gamma_\infty\in\mathcal{A}$ is an energy minimizer. We can thus arrive at the main theorem for this section:
\begin{theorem}\label{thm:existence-of-minimiser}
    There exists $\gamma_\infty\in\mathcal{A}$ which minimizes $E$.
\end{theorem}
