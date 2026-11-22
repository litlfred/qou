---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-014-4-fluctuations-in-the-non-lattice-case
section_title: "Fluctuations in the non-lattice case"
section_number: 4
pages: 25-26
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.886
latex_coverage_ratio: 0.924
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\label{sec:nonlattice}
In this section we prove the analogues of Theorems \ref{thm:mainlattice} and \ref{thm:cltlattice} when $\phi$ is not lattice-distributed; hence, by Proposition \ref{prop:latticeandnonlattice}, $|\E^{\eta(\I u)}|<1$ for any $u\neq 0$. In this setting, assuming $\phi$ absolutely continuous w.r.t.~the Lebesgue measure, there is a formula equivalent to the one given in Lemma \ref{lem:fourier}, namely,
\begin{equation}\proba[X\geq x]=\lim_{R \to \infty}\left(\frac{1}{2\pi}\int_{-R}^{R} \frac{\E^{-x(h+\I u)}}{h+\I u}\,\varphi_{X}(h+\I u)\,du\right)\label{eq:notuseful}
\end{equation}
if $\varphi_{X}(h)=\esper[\E^{hX}]<+\infty$ for $h>0$ (see \cite[Chapter XV, Section 3]{Fel71}). However, in order to manipulate this formula as in Section \ref{sec:lattice}, one would need strong additional assumptions of integrability on the characteristic functions of the random variables $X_{n}$. Thus, instead of Equation \eqref{eq:notuseful}, our main tool will be a Berry-Esseen estimate (see Proposition \ref{prop:berryesseen} hereafter), which we shall then combine with techniques of tilting of measures (Lemma \ref{lem:exponchange}) similar to those used in the classical theory of large deviations (see \cite[p. 32]{DZ98}).\bigskip
