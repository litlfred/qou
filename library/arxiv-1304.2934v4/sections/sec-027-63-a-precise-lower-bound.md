---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-027-63-a-precise-lower-bound
section_title: "A precise lower bound"
section_number: 6.3
pages: 47-48
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.957
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
One can then ask for an asymptotic lower bound on $\proba[X_{n} \in t_{n} B]$, and in view of the classical theory of large deviations, this lower bound should be related to open sets and to the exponent $F(B^{\mathrm{o}})$. Unfortunately, the result takes a less interesting form than Theorem \ref{thm:superellis}. If $B$ is a Borelian subset of $\R$, denote $B^{\delta}$ the union of the open intervals $(x,x+\kappa)$ of width $\kappa \geq \delta$ that are included into $B$. The interior $O=B^{\mathrm{o}}$ is a disjoint union of a countable collection of open intervals, and also the increasing union $\bigcup_{\delta >0}B^{\delta}$. 

\begin{center}
\begin{figure}[ht]\vspace{-1mm}
\includegraphics{problem.pdf}
\vspace{-2mm}
\caption{In some problematic situations, one is only able to prove a non-precise lower bound for large deviations.\label{fig:problem}}
\end{figure}
\end{center}

\noindent However, the topology of $B^{\mathrm{o}}$ may be quite intricate in comparison to the one of the $B^{\delta}$'s, as some points can be points of accumulation of open intervals included in $B$ and of width going to zero (see Figure \ref{fig:problem}). This phenomenon prevents us to state a precise lower bound when one of this point of accumulation is $a=\sup(B^{\mathrm{o}}\cap (-\infty,\eta'(0)])$ or $b=\inf (B^{\mathrm{o}} \cap [\eta'(0),+\infty))$. Nonetheless, the following is true:\medskip 

\begin{theorem}\label{thm:hyperellis}
For an admissible Borelian set $B$, 
$$\liminf_{\delta\to 0} \liminf_{n \to \infty} \big(\sqrt{2\pi t_{n}}\,\exp(t_{n}F(B^{\delta}))\,\proba[X_{n} \in t_{n} B] \big) \geq \begin{cases}
&\sum_{a \in (B^{\mathrm{o}})_{\min}} \frac{\psi(h(a))}{(1-\E^{-|h(a)|})\,\sqrt{\eta''(h(a))}}\\
&\sum_{a \in (B^{\mathrm{o}})_{\min}} \frac{\psi(h(a))}{|h(a)|\,\sqrt{\eta''(h(a))}},
\end{cases}$$
with the usual distinction of lattice/non-lattice cases. In particular, the right-hand side in Theorem \ref{thm:superellis} is the limit of $\sqrt{2\pi t_{n}}\,\exp(t_{n}F(B))\,\proba[X_{n} \in t_{n} B]$ as soon as $F(B^{\delta})=F(B)$ for some $\delta>0$.
\end{theorem}

\begin{proof}
Again we deal with the non-lattice case, and we suppose for instance that the set $(B^{\mathrm{o}})_{\min}$ consists of one point $b = \inf (B^{\mathrm{o}} \cap [\eta'(0),+\infty))$, the other situations being entirely similar. As $\delta$ goes to $0$, $B^{\delta}$ increases towards $B^{\mathrm{o}}=\bigcup_{\delta >0}B^{\delta}$, so the infimum $F(B^{\delta})$ decreases and the quantity $$L(\delta)=\liminf_{n \to \infty} \big(\sqrt{2\pi t_{n}}\,\exp(t_{n}F(B^{\delta}))\,\proba[X_{n} \in t_{n} B]\big)$$ is decreasing in $\delta$. 
Actually, if $b^{\delta} = \inf (B^{\delta} \cap [\eta'(0),+\infty))$, then for $\delta$ small enough $F(B^{\delta})=F(b^{\delta})$, so $\lim_{\delta \to 0}F(B^{\delta})=F(B^{\mathrm{o}})$ by continuity of $F$. On the other hand,  
$$R(\delta) = \frac{\psi(h(b^{\delta}))}{h(b^{\delta})\sqrt{\eta''(h(b^{\delta}))}}$$
tends to the same quantity with $b$ instead of $b^{\delta}$. Hence, it suffices to show that for $\delta$ small enough, $L(\delta)\geq R(\delta)$. However, by definition of $B^{\delta}$, the open interval $(b^{\delta},b^{\delta}+\delta)$ is included into $B$, so 
\begin{align*}\proba[X_{n} \in t_{n}B]&\geq \proba[X_{n} \in t_{n}B^{\delta}] \geq \proba[X_{n} > t_{n}b^{\delta}] - \proba[X_{n} \geq t_{n}(b^{\delta}+\delta)]\\
&\geq \left(\frac{\psi(h(b^{\delta}))\,\E^{-t_{n}F(b^{\delta})}}{h(b^{\delta})\sqrt{2\pi t_{n}\eta''(h(b^{\delta}))}}- \frac{\psi(h(b^{\delta}+\delta))\,\E^{-t_{n}F(b^{\delta}+\delta)}}{h(b^{\delta}+\delta)\sqrt{2\pi t_{n}\eta''(h(b^{\delta}+\delta))}}\right)\big(1+o(1)\big)\\
&\geq \frac{\psi(h(b^{\delta}))\,\E^{-t_{n}F(b^{\delta})}}{h(b^{\delta})\,\sqrt{2\pi t_{n}\eta''(h(b^{\delta}))}}\big(1+o(1)\big)
\end{align*}
since the second term on the second line is negligible in comparison to the first term --- $F(b^{\delta}+\delta)>F(b^{\delta})$. This ends the proof.
\end{proof}
\bigskip
