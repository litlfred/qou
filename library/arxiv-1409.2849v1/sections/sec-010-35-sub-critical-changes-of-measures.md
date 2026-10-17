---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-010-35-sub-critical-changes-of-measures
section_title: "Sub-critical changes of measures"
section_number: 3.5
pages: 19-20
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
toc_source: outline
text_source: latex
latex_prose_ratio: 0.913
latex_coverage_ratio: 0.927
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
In the mixed Curie-Weiss-Ising model, one may ask  what happens if instead of $\beta$ and $\frac{1}{\E^{2\beta}}$ one puts arbitrary coefficients for the local and the global interaction. More generally, given a sequence $(X_n)_{n \in \N}$ that converges in the $\mathrm{L}^{1}$-mod-Gaussian sense with parameters $t_n$ and limiting function $\psi$, one can look at the change of measure
$$\qproba_{n}^{(\gamma)}[dx]=\frac{\E^{\frac{\gamma x^2}{2t_n}}}{\esper\!\left[\E^{\frac{\gamma (X_n)^2}{2t_n}}\right]}\,\proba_n[dx]$$
with $\gamma \in (0,1)$ (for $\gamma >1$, the change of measure is not necessarily well-defined, since the hypotheses \eqref{hyp:laplacemod} and \eqref{hyp:l1mod} do not ensure that $\esper[\E^{\gamma (X_n)^2/2t_n}] < + \infty$). These subcritical changes of measures do not modify the order of magnitude of the fluctuations of $X_n$, and more precisely:

\begin{theorem}\label{thm:subcritical}
Suppose that $(X_n)_{n\in \N}$ converges in the $\mathrm{L}^1$-mod-Gaussian sense with parameters $t_n$ and limiting function $\psi$. Then, if $(X_{n}^{(\gamma)})_{n \in \N}$ is a sequence of random variables under the new probability measures $\qproba_{n}^{(\gamma)}$, it converges in the $\mathrm{L}^1$-mod-Gaussian sense with parameters $(1-\gamma)t_n$ and limit $\psi$.
\end{theorem}

\begin{example}
Consider a random configuration of spins $\sigma$ on $\lle 1,n\rre$ with probability proportional to
$$\exp\left(\beta \left(\sum_{i=1}^{n-1} \sigma(i)\sigma(i+1)\right)+\frac{\gamma}{2n} \left(\sum_{i=1}^n \sigma(i)\right)^2\right),$$
with $\gamma < \E^{-2\beta}$. The total magnetization of the system has order of magnitude $n^{1/2}$, and more precisely, one has the central limit theorem
$$\frac{M_n}{n^{1/2}} \rightharpoonup_{n \to \infty} \mathcal{N}(0,(1-\gamma\E^{2\beta})\E^{2\beta}),$$
and in fact a $\mathrm{L}^1$-mod-Gaussian convergence of $\frac{M_n}{n^{1/4}}$, with a limiting function $$\psi(x)=\exp(-(3\E^{6\beta}-\E^{2\beta})\,x^4/24)$$ that does not depend on $\gamma$.
\end{example}

\begin{proof}[Proof of Theorem \ref{thm:subcritical}]
We denote as before $(Y_n)_{n \in \N}$ a sequence of random variables under the laws $\qproba_n=\qproba_n^{(1)}$. We first compute the asymptotics of $Z_n^{(\gamma)}=\esper[\E^{\gamma (X_n)^2/2t_n}] $:
\begin{align*}
Z_n^{(\gamma)}&= Z_n\,\,\esper[\E^{-(1-\gamma) (Y_n)^2/2t_n}]\end{align*}
\begin{align*}
&=\sqrt{\frac{t_n}{2\pi}}\left(\int_{\R}\psi(x)\,dx\right)\,\esper\!\left[\E^{-\frac{t_n(1-\gamma)}{2}(\frac{Y_n}{t_n})^2}\right](1+o(1))\\
&=\sqrt{\frac{t_n}{2\pi}}\left(\int_{\R}\psi(x)\,dx\right)\,\esper\!\left[\E^{-\frac{t_n(1-\gamma)}{2}\,(W_n)^2}\right](1+o(1))\\
&=\sqrt{\frac{1}{1-\gamma}}\,(1+o(1))
\end{align*}
by using on the third line the same argument as in the proof of Proposition \ref{l1stronger} to replace $\frac{Y_n}{t_n}$ by $W_n$; and by using the Laplace method on the fourth line in order to compute $\int_{\R} \E^{-t_n(1-\gamma)x^2/2}\,\psi_n(x)\,dx$. The same computations give the asymptotics of
\begin{align*}
\esper[\E^{tX_n+\gamma (X_n)^2/2t_n}]&=Z_n\,\esper[\E^{tY_n-(1-\gamma) (Y_n)^2/2t_n}]\\
&=\sqrt{\frac{t_n}{2\pi}}\left(\int_{\R}\psi(x)\,dx\right)\,\esper\!\left[\E^{t_nt\,(\frac{Y_n}{t_n})-\frac{t_n(1-\gamma)}{2}(\frac{Y_n}{t_n})^2}\right](1+o(1))\\
&=\sqrt{\frac{t_n}{2\pi}}\left(\int_{\R}\psi(x)\,dx\right)\,\esper\!\left[\E^{t_nt \,W_n-\frac{t_n(1-\gamma)}{2}(W_n)^2}\right](1+o(1))\\
&=\E^{-\frac{t_nt^2}{2(1-\gamma)}} \sqrt{\frac{1}{1-\gamma}}\,\psi(t)\,(1+o(1))
\end{align*}
with again a Laplace method on the fourth line. Since
$$\esper[\E^{tX_n^{(\gamma)}}]=\frac{\esper[\E^{tX_n+\gamma (X_n)^2/2t_n}]}{Z_n^{(\gamma)}},$$
this shows the hypotheses \eqref{hyp:laplacemod} and \eqref{hyp:l1mod} for the sequence $(X_n^{(\gamma)})_{n \in \N}$. Then, since $(\frac{Y_n}{t_n})_{n \in \N}$ converges in law, by using the implication \eqref{l1ii} $\Rightarrow$ \eqref{l1iii} in Theorem \ref{thm:mainl1} for the sequence  $(X_n^{(\gamma)})_{n \in \N}$, we see that the mod-Gaussian convergence of Laplace transforms necessarily happens in $\mathrm{L}^1(\R)$.
\end{proof}
\medskip
