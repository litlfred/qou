---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-021-51-bounds-on-cumulants-and-mod-gaussian-converge
section_title: "Bounds on cumulants and mod-Gaussian convergence"
section_number: 5.1
pages: 38-39
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.907
latex_coverage_ratio: 1.0
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\label{subsec:modgaussfromcumulants}
Let $(S_{n})_{n \in \N}$ be a sequence of real-valued centered random variables that admit moments of all order, and such that  
\begin{equation}
    |\kappa^{(r)}(S_{n})| \leq (Cr)^{r}\,\alphan (\betan)^r
    \label{eq:superbound}
\end{equation}
for all $r \geq 2$ and for some sequences $(\alphan)_{n \to \infty} \to +\infty$ and $(\beta_n)_{n\in \N}$ arbitrary. Assume moreover that there exists an integer $v \geq 3$ such that \vspace{2mm}
\begin{enumerate}
\item $\kappa^{(r)}(S_{n})=0$ for all $3 \leq r < v$ and all $n \in \N$;\vspace{2mm}
\item we have the following approximations for second and third cumulants:
    \begin{align}
        \kappa^{(2)}(S_{n}) &= \sigma^{2}\,\alphan (\betan)^{2}\,\left(1+o\!\left((\alphan)^{-\frac{v-2}{v}}\right)\right); \nonumber \\
        \kappa^{(v)}(S_{n}) &=L\,\alphan (\betan)^{v}\,\big(1+o(1)\big).
        \label{eq:cv_sndthrd_cumulants}
    \end{align}
\end{enumerate}
Set $X_{n}=\frac{S_{n}}{(\alphan)^{\frac{1}{v}}\betan}$. The cumulant generating series of $X_{n}$ is
\begin{align*}
\log \varphi_{n}(z)&=\frac{\kappa^{(2)}(S_{n})}{2\,(\alphan)^{\frac{2}{v}}\,(\betan)^2}\,z^{2}+\frac{\kappa^{(v)}(S_{n})}{v!\,\alphan (\betan)^{v}}\,z^{v}+\sum_{r=v+1}^{\infty} \frac{\kappa^{(r)}(S_{n})}{r!\,(\alphan)^{\frac{r}{v}}\,(\betan)^r}\,z^{r}\\
&=\frac{\sigma^{2}}{2}\,(\alphan)^{\frac{v-2}{v}}z^{2}+\frac{L}{v!}\,z^{v}+ \sum_{r=v+1}^{\infty} \frac{\kappa^{(r)}(S_{n})}{r!\,(\alphan)^{\frac{r}{v}}\,(\betan)^r}\,z^{r}+o(1),
\end{align*}
where the $o(1)$ is locally uniform. The remaining series is locally uniformly bounded in absolute value by
$$\sum_{r=v+1}^{\infty} C^{r}\,\frac{r^{r}}{r!}\, \frac{1}{(\alphan)^{\frac{r-v}{v}}}\,R^{r} \leq \alphan \sum_{r=v+1}^{\infty} \left(\frac{\E\, CR}{(\alphan)^{\frac{1}{v}}}\right)^{r}=(\alphan)^{-\frac{1}{v}}\,\frac{(\E\, CR)^{v+1}}{1-\E\, CR\,(\alphan)^{-\frac{1}{v}}} \to 0.$$
Hence, 
$$\psi_{n}(z)=\exp\left(-(\alphan)^{\frac{v-2}{v}}\,\frac{\sigma^{2}z^{2}}{2}\right)\,\varphi_{n}(z) \to \exp\left(\frac{L}{v!}\,z^{v}\right)$$
locally uniformly on $\C$, so one has again mod-Gaussian convergence, with parameters $t_{n}=\sigma^{2}\,(\alphan)^{\frac{v-2}{v}}$ and limiting function $\psi(z)=\E^{\frac{L}{v!}\,z^{v}}$.

\begin{remark}
The case of i.i.d.~variables --- Example \ref{ex:sumiid} --- fits in this framework, with $\alphan=n$ and $\betan=1$.However, it includes many more examples than sums of i.i.d.~variables: in particular, in Section \ref{sec:depgraph}, we show that such bounds on cumulants typically occur in the framework of dependency graphs. Concrete examples are discussed in Sections \ref{sec:erdosrenyi} and \ref{sec:central}.
\end{remark}
\bigskip
