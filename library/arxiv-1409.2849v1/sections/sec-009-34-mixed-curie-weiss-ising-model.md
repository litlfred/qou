---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-009-34-mixed-curie-weiss-ising-model
section_title: "Mixed Curie-Weiss-Ising model"
section_number: 3.4
pages: 17-19
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
toc_source: outline
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 0.878
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
Consider the one-dimensional Ising model of parameter $\alpha=0$, and $\beta$ arbitrary. We have shown in Section \ref{sec:ising} the complex mod-Gaussian convergence of $(n^{-1/4}\,M_n)_{n \in \N}$ with parameters $n^{1/2}\,\E^{2\beta}$ and limiting function $\psi(z)=\exp(-(3\E^{6\beta}-\E^{2\beta})\,z^4/24)$. Restricted to $\R$, this limiting function is integrable, and again one has $\mathrm{L}^1$-mod-convergence. Indeed, recall that 
$$\esper[\E^{t M_n}]=\frac{Z_n(\IS,t,\beta)}{Z_n(\IS,0,\beta)}=\frac{1}{2}\left(a_+(t,\beta)\left(\frac{\lambda_+(t,\beta)}{2\cosh \beta}\right)^{n-1}+a_-(t,\beta)\left(\frac{\lambda_-(t,\beta)}{2\cosh \beta}\right)^{n-1}\right).$$
It will be convenient to work with $n^{-1/4}\,M_{n+1}$ instead of $n^{-1/4}\,M_n$ in order to work with $n$-th powers. Then,
\begin{align*}
\psi_n(t)&=\esper\!\left[\E^{t \frac{M_{n+1}}{n^{1/4}}}\right]\,\E^{-\frac{n^{1/2}\E^{2\beta}z^2}{2}} \\
\int_{\R}\psi_n(t) dt& = \frac{n^{1/4}}{2}\int_{\R} a_+(u,\beta) \left(\frac{\lambda_+(u,\beta)}{2\cosh \beta}\,\E^{-\frac{\E^{2\beta}u^2}{2}}\right)^n + a_-(u,\beta) \left(\frac{\lambda_-(u,\beta)}{2\cosh \beta}\,\E^{-\frac{\E^{2\beta}u^2}{2}}\right)^n du
\end{align*}
and for every parameter $\beta \geq 0$, the functions 
$$u \mapsto \frac{\lambda_+(u,\beta)}{2\cosh \beta}\,\E^{-\frac{\E^{2\beta}u^2}{2}} \quad \text{and} \quad u \mapsto \frac{\lambda_-(u,\beta)}{2\cosh \beta}\,\E^{-\frac{\E^{2\beta}u^2}{2}} $$ 
attain their unique maximum at $u=0$, see Figure \ref{fig:function3} for the graph of the first function. 
\begin{center}
\vspace{-5mm}
\begin{figure}[ht]
\includegraphics[scale=0.7]{function3.png}\caption{The function $f(u,\beta)=\frac{\lambda_+(u,\beta)}{2\cosh \beta}\,\E^{-\frac{\E^{2\beta}u^2}{2}}$ (using \textsc{Mathematica}). \label{fig:function3}}
\end{figure}
\end{center}
Their Taylor expansions at $u=0$ are respectively
$$1-\frac{3\E^{6\beta}-\E^{2\beta}}{24}\,u^4+o(u^4)\quad\text{and} \quad \tanh \beta +o(1),$$
so again by the Laplace method we get $\lim_{n \to \infty} \int_{\R}\psi_n(t)\,dt = \int_{\R} \psi(t)\,dt$ and the $\mathrm{L}^1$-mod-convergence. As a consequence, consider the random configuration of spins $\sigma$ on $\lle 1,n\rre$ with probability proportional to
$$\exp\left(\beta \left(\sum_{i=1}^{n-1} \sigma(i)\sigma(i+1)\right)+\frac{1}{2n\E^{2\beta}} \left(\sum_{i=1}^n \sigma(i)\right)^2\right).$$
This model has a local interaction with coefficient $\beta$ and a global interaction with coefficient $\frac{1}{\E^{2\beta}}$, so it is a mix of the Ising model and of the Curie-Weiss model. The previous discussion and Theorem \ref{thm:mainl1} show that its magnetization satisfies the non standard limit theorem
$$\frac{M_n}{n^{3/4}} \rightharpoonup_{n \to \infty} \frac{\psi(x)\,dx}{\int_{\R}\psi(x)\,dx}\quad\text{with }\psi(x)=\exp\left(-\frac{3\E^{6\beta}-\E^{2\beta}}{24}\,x^4\right).$$
\medskip
